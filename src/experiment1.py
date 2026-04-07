"""Experiment 1: Sealed-bid art valuation across two information conditions.

Variant A (image_only): Model sees only the artwork image.
Variant B (basic_metadata): Model sees image + title, artist, year, description.

No budget cap — models report their honest estimate of fair market value.
"""

import asyncio
import csv
import json
import random
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

from .llm_client import UnifiedLLMClient, LLMResponse, MODELS


# ---------------------------------------------------------------------------
# Prompts
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = """\
You are one of the world's foremost art appraisers, with decades of experience \
advising major auction houses (Christie's, Sotheby's, Phillips) and museums on \
acquisitions. You have deep expertise in art history, market dynamics, condition \
assessment, and provenance research.

Your task: Examine the artwork presented and provide your professional estimate \
of its current fair market value — what this piece would realistically sell for \
at a major international auction today, assuming it is authentic and legally \
available for sale.

Consider all factors visible to you: artistic quality, technique, historical \
significance, cultural importance, condition (as far as you can judge), and \
market comparables.

IMPORTANT: Respond with ONLY a valid JSON object in the following format — \
no markdown fences, no commentary before or after:

{
    "internal_reasoning": "Your detailed appraisal analysis. Discuss artistic \
merit, technique, art-historical context, condition observations, market \
comparables, and how you arrived at your valuation. Be thorough — at least \
400 words.",
    "valuation_usd": <integer — your estimate of fair market value in US dollars>,
    "confidence": <float between 0.0 and 1.0 — how confident you are in this \
valuation>,
    "key_factors": ["factor 1", "factor 2", "factor 3", "factor 4", "factor 5"]
}"""


USER_PROMPT_IMAGE_ONLY = """\
Please appraise the artwork shown in the image above.

Base your valuation solely on what you can see. You have not been provided \
with any identifying information — no title, artist, date, or provenance."""


USER_PROMPT_BASIC_METADATA = """\
Please appraise the following artwork:

**Title:** {title}
**Artist:** {artist}
**Year:** {year}
**Description:** {description}

The image of the artwork is shown above. Base your valuation on the image \
and the metadata provided. No provenance documentation, condition report, \
or auction history has been supplied."""


# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------

@dataclass
class ValuationResult:
    """One model's valuation of one artwork under one condition."""
    model_key: str
    model_display: str
    artwork_id: str
    artwork_title: str
    artwork_category: str
    true_value_usd: float
    condition: str          # "image_only" or "basic_metadata"
    run_idx: int
    valuation_usd: int
    confidence: float
    internal_reasoning: str
    key_factors: list[str]
    parse_success: bool
    error: Optional[str]
    latency_ms: float
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

    # Derived
    @property
    def valuation_ratio(self) -> Optional[float]:
        if self.true_value_usd > 0:
            return self.valuation_usd / self.true_value_usd
        return None

    def to_dict(self) -> dict:
        return {
            "model_key": self.model_key,
            "model_display": self.model_display,
            "artwork_id": self.artwork_id,
            "artwork_title": self.artwork_title,
            "artwork_category": self.artwork_category,
            "true_value_usd": self.true_value_usd,
            "condition": self.condition,
            "run_idx": self.run_idx,
            "valuation_usd": self.valuation_usd,
            "confidence": self.confidence,
            "internal_reasoning": self.internal_reasoning,
            "key_factors": self.key_factors,
            "parse_success": self.parse_success,
            "error": self.error,
            "latency_ms": self.latency_ms,
            "timestamp": self.timestamp,
            "valuation_ratio": self.valuation_ratio,
        }


# ---------------------------------------------------------------------------
# JSON parsing
# ---------------------------------------------------------------------------

def parse_valuation_response(raw: str) -> dict:
    """Extract valuation JSON from an LLM response string."""
    content = raw.strip()

    # Strip markdown fences if present
    if "```json" in content:
        content = content.split("```json", 1)[1].split("```", 1)[0]
    elif "```" in content:
        parts = content.split("```")
        if len(parts) >= 3:
            content = parts[1]

    content = content.strip()
    if content.startswith("json"):
        content = content[4:].strip()

    try:
        data = json.loads(content)
        return {
            "valuation_usd": int(data.get("valuation_usd", 0)),
            "confidence": float(data.get("confidence", 0.5)),
            "internal_reasoning": str(data.get("internal_reasoning", "")),
            "key_factors": list(data.get("key_factors", [])),
            "parse_success": True,
            "error": None,
        }
    except (json.JSONDecodeError, ValueError, TypeError) as exc:
        # Fallback: try to find JSON object in response
        import re
        match = re.search(r'\{[\s\S]*"valuation_usd"\s*:\s*\d+[\s\S]*\}', content)
        if match:
            try:
                data = json.loads(match.group())
                return {
                    "valuation_usd": int(data.get("valuation_usd", 0)),
                    "confidence": float(data.get("confidence", 0.5)),
                    "internal_reasoning": str(data.get("internal_reasoning", "")),
                    "key_factors": list(data.get("key_factors", [])),
                    "parse_success": True,
                    "error": None,
                }
            except Exception:
                pass

        return {
            "valuation_usd": 0,
            "confidence": 0.0,
            "internal_reasoning": "",
            "key_factors": [],
            "parse_success": False,
            "error": f"JSON parse error: {exc}",
        }


# ---------------------------------------------------------------------------
# Main experiment class
# ---------------------------------------------------------------------------

class Experiment1:
    """Run Experiment 1: sealed-bid valuation, two conditions."""

    CONDITIONS = ["image_only", "basic_metadata"]

    def __init__(
        self,
        openrouter_api_key: str,
        model_keys: list[str] | None = None,
        num_runs: int = 2,
        temperature: float = 0.7,
        output_dir: str | Path = "results/experiment1",
        randomize_order: bool = True,
    ):
        self.client = UnifiedLLMClient(openrouter_api_key)
        self.model_keys = model_keys or list(MODELS.keys())
        self.num_runs = num_runs
        self.temperature = temperature
        self.output_dir = Path(output_dir)
        self.randomize_order = randomize_order

        # Create output dirs
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.output_dir / "logs").mkdir(exist_ok=True)

        # Accumulate results
        self.results: list[ValuationResult] = []

    async def close(self):
        await self.client.close()

    # ----- single valuation call -----

    async def get_valuation(
        self,
        model_key: str,
        artwork: dict,
        condition: str,
        run_idx: int,
    ) -> ValuationResult:
        """Get one model's valuation of one artwork."""
        system_prompt = SYSTEM_PROMPT

        if condition == "image_only":
            user_prompt = USER_PROMPT_IMAGE_ONLY
        else:
            user_prompt = USER_PROMPT_BASIC_METADATA.format(
                title=artwork["title"],
                artist=artwork["artist"],
                year=artwork.get("year_created", "Unknown"),
                description=artwork.get("description", "No description available."),
            )

        image_path = artwork.get("image_path", "")
        # Resolve relative to project root
        base_dir = Path(__file__).parent.parent
        abs_image = base_dir / image_path
        if not abs_image.exists():
            abs_image = None

        model_display = MODELS[model_key]["display_name"]

        try:
            resp: LLMResponse = await self.client.complete(
                model_key=model_key,
                system_prompt=system_prompt,
                user_prompt=user_prompt,
                image_path=str(abs_image) if abs_image else None,
                temperature=self.temperature,
                max_tokens=4096,
            )
            parsed = parse_valuation_response(resp.content)

            result = ValuationResult(
                model_key=model_key,
                model_display=model_display,
                artwork_id=artwork["id"],
                artwork_title=artwork["title"],
                artwork_category=artwork["category"],
                true_value_usd=artwork.get("true_value_usd", 0),
                condition=condition,
                run_idx=run_idx,
                valuation_usd=parsed["valuation_usd"],
                confidence=parsed["confidence"],
                internal_reasoning=parsed["internal_reasoning"],
                key_factors=parsed["key_factors"],
                parse_success=parsed["parse_success"],
                error=parsed["error"],
                latency_ms=resp.latency_ms,
            )

            # Save raw response log
            log_file = self.output_dir / "logs" / f"{artwork['id']}_{condition}_run{run_idx}_{model_key}.json"
            log_entry = {
                "model_key": model_key,
                "artwork_id": artwork["id"],
                "condition": condition,
                "run_idx": run_idx,
                "raw_response": resp.content,
                "parsed": parsed,
                "latency_ms": resp.latency_ms,
                "input_tokens": resp.input_tokens,
                "output_tokens": resp.output_tokens,
                "timestamp": result.timestamp,
            }
            with open(log_file, "w") as f:
                json.dump(log_entry, f, indent=2)

            return result

        except Exception as exc:
            return ValuationResult(
                model_key=model_key,
                model_display=model_display,
                artwork_id=artwork["id"],
                artwork_title=artwork["title"],
                artwork_category=artwork["category"],
                true_value_usd=artwork.get("true_value_usd", 0),
                condition=condition,
                run_idx=run_idx,
                valuation_usd=0,
                confidence=0.0,
                internal_reasoning=f"ERROR: {exc}",
                key_factors=[],
                parse_success=False,
                error=str(exc),
                latency_ms=0.0,
            )

    # ----- print helpers -----

    @staticmethod
    def _print_valuation(result: ValuationResult, idx: int, total: int):
        status = "OK" if result.parse_success else "FAIL"
        val_str = f"${result.valuation_usd:>15,}" if result.valuation_usd else "  $0 (parse err)"

        ratio_str = ""
        if result.true_value_usd > 0 and result.valuation_usd > 0:
            ratio = result.valuation_usd / result.true_value_usd
            ratio_str = f"  ({ratio:.2f}x true value)"

        print(f"      [{idx}/{total}] [{status:4}] {result.model_display:20} -> {val_str}{ratio_str}")
        print(f"             Confidence: {result.confidence:.2f}  |  Latency: {result.latency_ms:.0f}ms")
        if result.key_factors:
            print(f"             Factors: {', '.join(result.key_factors[:3])}")

    # ----- run experiment -----

    async def run(self, dataset: dict) -> dict:
        """Run the full experiment across all artworks, conditions, and runs."""
        artworks = dataset["artworks"]
        total_calls = len(artworks) * len(self.CONDITIONS) * self.num_runs * len(self.model_keys)

        print("=" * 72)
        print("  EXPERIMENT 1: ART VALUATION (Sealed-Bid)")
        print("=" * 72)
        print(f"  Models:       {', '.join(MODELS[k]['display_name'] for k in self.model_keys)}")
        print(f"  Artworks:     {len(artworks)}")
        print(f"  Conditions:   {', '.join(self.CONDITIONS)}")
        print(f"  Runs/cond:    {self.num_runs}")
        print(f"  Temperature:  {self.temperature}")
        print(f"  Total calls:  {total_calls}")
        print("=" * 72)

        call_count = 0

        for run_idx in range(self.num_runs):
            print(f"\n{'='*72}")
            print(f"  RUN {run_idx + 1}/{self.num_runs}")
            print(f"{'='*72}")

            for condition in self.CONDITIONS:
                print(f"\n{'─'*56}")
                print(f"  Condition: {condition}")
                print(f"{'─'*56}")

                # Randomize artwork order per run+condition
                order = list(range(len(artworks)))
                if self.randomize_order:
                    random.shuffle(order)

                for art_idx in order:
                    artwork = artworks[art_idx]
                    cat_label = artwork["category"].upper()
                    print(f"\n  [{cat_label}] {artwork['title']}  —  {artwork['artist']}")
                    print(f"  True value: ${artwork.get('true_value_usd', 0):,.0f}")

                    for m_idx, model_key in enumerate(self.model_keys, 1):
                        call_count += 1
                        print(f"    ({call_count}/{total_calls})", end="")

                        result = await self.get_valuation(
                            model_key, artwork, condition, run_idx
                        )
                        self.results.append(result)
                        self._print_valuation(result, m_idx, len(self.model_keys))

                        # Save incrementally after each call
                        self._save_results()

                        # Rate-limit pause
                        await asyncio.sleep(1.0)

        # Final save
        self._save_results()
        self._print_summary()

        return {
            "total_valuations": len(self.results),
            "output_dir": str(self.output_dir),
        }

    # ----- persistence -----

    def _save_results(self):
        """Save results to JSON and CSV."""
        # JSON — full detail
        json_path = self.output_dir / "results.json"
        with open(json_path, "w") as f:
            json.dump(
                {
                    "experiment": "experiment1_valuation",
                    "models": self.model_keys,
                    "num_runs": self.num_runs,
                    "conditions": self.CONDITIONS,
                    "temperature": self.temperature,
                    "total_results": len(self.results),
                    "timestamp": datetime.now().isoformat(),
                    "results": [r.to_dict() for r in self.results],
                },
                f,
                indent=2,
            )

        # CSV — flat for analysis
        csv_path = self.output_dir / "results.csv"
        if self.results:
            fieldnames = [
                "model_key", "model_display", "artwork_id", "artwork_title",
                "artwork_category", "true_value_usd", "condition", "run_idx",
                "valuation_usd", "confidence", "valuation_ratio",
                "parse_success", "error", "latency_ms", "timestamp",
                "key_factors",
            ]
            with open(csv_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for r in self.results:
                    row = r.to_dict()
                    row["key_factors"] = "; ".join(row.get("key_factors", []))
                    # Drop reasoning from CSV (too long) — it's in JSON + logs
                    writer.writerow({k: row.get(k, "") for k in fieldnames})

        # Summary stats JSON
        summary_path = self.output_dir / "summary.json"
        summary = self._compute_summary()
        with open(summary_path, "w") as f:
            json.dump(summary, f, indent=2)

    def _compute_summary(self) -> dict:
        """Compute summary statistics."""
        if not self.results:
            return {}

        summary: dict = {
            "total_valuations": len(self.results),
            "parse_success_rate": sum(1 for r in self.results if r.parse_success) / len(self.results),
            "by_model": {},
            "by_condition": {},
            "by_category": {},
        }

        for model_key in self.model_keys:
            model_results = [r for r in self.results if r.model_key == model_key and r.parse_success]
            if model_results:
                valuations = [r.valuation_usd for r in model_results]
                ratios = [r.valuation_ratio for r in model_results if r.valuation_ratio is not None]
                summary["by_model"][model_key] = {
                    "display_name": MODELS[model_key]["display_name"],
                    "count": len(model_results),
                    "avg_valuation": sum(valuations) / len(valuations),
                    "median_valuation": sorted(valuations)[len(valuations) // 2],
                    "avg_confidence": sum(r.confidence for r in model_results) / len(model_results),
                    "avg_ratio": sum(ratios) / len(ratios) if ratios else None,
                }

        for cond in self.CONDITIONS:
            cond_results = [r for r in self.results if r.condition == cond and r.parse_success]
            if cond_results:
                valuations = [r.valuation_usd for r in cond_results]
                summary["by_condition"][cond] = {
                    "count": len(cond_results),
                    "avg_valuation": sum(valuations) / len(valuations),
                }

        for cat in ["masterpiece", "ai_art", "recent_ood", "contemporary"]:
            cat_results = [r for r in self.results if r.artwork_category == cat and r.parse_success]
            if cat_results:
                valuations = [r.valuation_usd for r in cat_results]
                summary["by_category"][cat] = {
                    "count": len(cat_results),
                    "avg_valuation": sum(valuations) / len(valuations),
                    "avg_true_value": sum(r.true_value_usd for r in cat_results) / len(cat_results),
                }

        summary["timestamp"] = datetime.now().isoformat()
        return summary

    def _print_summary(self):
        """Print final summary to console."""
        summary = self._compute_summary()

        print("\n" + "=" * 72)
        print("  EXPERIMENT 1 COMPLETE — SUMMARY")
        print("=" * 72)
        print(f"  Total valuations:    {summary.get('total_valuations', 0)}")
        print(f"  Parse success rate:  {summary.get('parse_success_rate', 0):.1%}")

        print("\n  MODEL PERFORMANCE:")
        print("  " + "-" * 60)
        for model_key, stats in summary.get("by_model", {}).items():
            print(f"    {stats['display_name']}:")
            print(f"      Avg valuation:  ${stats['avg_valuation']:,.0f}")
            print(f"      Avg confidence: {stats['avg_confidence']:.2f}")
            if stats.get("avg_ratio") is not None:
                print(f"      Avg ratio:      {stats['avg_ratio']:.2f}x true value")

        print("\n  BY CONDITION:")
        print("  " + "-" * 60)
        for cond, stats in summary.get("by_condition", {}).items():
            print(f"    {cond}: avg ${stats['avg_valuation']:,.0f}  (n={stats['count']})")

        print("\n  BY CATEGORY:")
        print("  " + "-" * 60)
        for cat, stats in summary.get("by_category", {}).items():
            print(f"    {cat}:")
            print(f"      Avg valuation:  ${stats['avg_valuation']:,.0f}")
            print(f"      Avg true value: ${stats['avg_true_value']:,.0f}")

        print(f"\n  Results saved to: {self.output_dir}")
        print("=" * 72)
