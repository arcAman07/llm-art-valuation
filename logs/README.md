# Experiment 1 — Raw Appraisal Logs

Each model appraised 20 real artworks under two conditions:

- **Image only** — painting shown, no text
- **With metadata** — title, artist, year, and description added

**Metric:** Valuation ratio = estimate ÷ true auction price. `1.000x` = perfect.

## What's in this folder

| Path | What it contains |
|---|---|
| `README.md` | This file — cross-model tables and metric guide |
| `gpt-5-4.md` | Formatted log: summary tables + per-artwork reasoning for GPT-5.4 |
| `sonnet-4-6.md` | Same for Claude Sonnet 4.6 |
| `gemini-3-1-pro.md` | Same for Gemini 3.1 Pro |
| `qwen-3-6.md` | Same for Qwen 3.6 Plus |
| `raw/gpt-5-4/` | **40 raw JSON files** — one per artwork per condition, full model output |
| `raw/sonnet-4-6/` | 40 raw JSON files |
| `raw/gemini-3-1-pro/` | 40 raw JSON files |
| `raw/qwen-3-6/` | 37 raw JSON files (3 no-parse) |

### Raw JSON format (each file)
```json
{
  "artwork_id": "mp_001",
  "condition": "image_only",
  "parsed": {
    "valuation_usd": 1800000,
    "confidence": 0.37,
    "internal_reasoning": "...",
    "key_factors": ["...", "..."]
  }
}
```
Every field the model produced is preserved verbatim.

## Files

| Model | File | Image-Only MALE | Metadata MALE | Improvement |
|---|---|---|---|---|
| Gemini 3.1 Pro | [gemini-3-1-pro.md](gemini-3-1-pro.md) | 1.106 | 0.460 | 2.4x |
| Claude Sonnet 4.6 | [sonnet-4-6.md](sonnet-4-6.md) | 1.570 | 0.713 | 2.2x |
| Qwen 3.6 Plus | [qwen-3-6.md](qwen-3-6.md) | 2.002 | 1.046 | 1.9x |
| GPT-5.4 | [gpt-5-4.md](gpt-5-4.md) | 4.577 | 0.732 | **6.3x** |

MALE = Mean Absolute Log Error. Lower is better. GPT's 6.3x improvement from adding a text label means the image is doing almost nothing for it.

---

## Cross-Model Reference — Image Only

| Artwork | True Price | GPT-5.4 | Claude | Gemini | Qwen |
|---|---|---|---|---|---|
| Salvator Mundi | $450.3M | 0.004x | 1.221x | **0.999x** | **1.055x** |
| Nu couche | $170.4M | 0.000x | 0.704x | 0.704x | **0.968x** |
| The Scream | $119.9M | 1.251x | 2.502x | 2.502x | 1.543x |
| Portrait of Dr. Gachet | $82.5M | **1.152x** | 4.242x | 3.030x | 2.242x |
| Bal du moulin de la Galette | $78.1M | 0.230x | 4.097x | 3.841x | 3.649x |
| Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer) | $236.4M | 0.762x | 0.402x | N/A | 0.305x |
| Blumenwiese (Blooming Meadow) | $86.0M | 0.099x | 0.640x | **0.872x** | 0.001x |
| Piles de romans parisiens et roses dans un verre (Romans parisiens) | $62.7M | 0.000x | **1.196x** | 0.670x | 0.007x |
| No. 31 (Yellow Stripe) | $62.2M | 0.000x | **0.885x** | 1.400x | 0.724x |
| El sueno (La cama) / The Dream (The Bed) | $54.7M | 0.064x | 0.640x | 0.457x | 0.439x |
| Knife Behind Back | $24.9M | 0.072x | 0.200x | 0.501x | N/A |
| Pie Fight Interior 12 | $10.4M | 0.001x | 0.012x | **0.817x** | 0.308x |
| Walkers With the Dawn and Morning | $10.7M | 0.001x | 0.007x | 0.419x | 0.764x |
| The Beautyful Ones | $4.7M | 0.038x | 0.591x | 0.633x | N/A |
| Force Field | $6.9M | 0.001x | 0.003x | 0.365x | 0.211x |
| A.I. God: Portrait of Alan Turing | $1.1M | 0.003x | 0.032x | N/A | 0.323x |
| Portrait of Edmond de Belamy | $432K | 0.028x | 1.272x | **0.925x** | 0.029x |
| Machine Hallucinations - ISS Dreams - A | $277K | 0.004x | 0.016x | 0.003x | 0.006x |
| Embedding Study 1 & 2 | $94K | 0.190x | 0.794x | 0.004x | 0.196x |
| Memories of Passersby I | $51K | 0.157x | **0.882x** | 2.352x | 0.055x |

## Cross-Model Reference — With Metadata

| Artwork | True Price | GPT-5.4 | Claude | Gemini | Qwen |
|---|---|---|---|---|---|
| Salvator Mundi | $450.3M | 0.777x | **0.933x** | **0.999x** | **1.055x** |
| Nu couche | $170.4M | **0.968x** | 0.763x | **0.968x** | N/A |
| The Scream | $119.9M | 1.501x | 1.751x | 2.919x | 1.293x |
| Portrait of Dr. Gachet | $82.5M | 3.333x | 3.636x | 3.030x | 2.364x |
| Bal du moulin de la Galette | $78.1M | 1.601x | 2.561x | 1.921x | 1.472x |
| Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer) | $236.4M | 0.360x | 0.465x | 0.571x | 0.613x |
| Blumenwiese (Blooming Meadow) | $86.0M | 0.488x | 0.640x | **0.988x** | 0.564x |
| Piles de romans parisiens et roses dans un verre (Romans parisiens) | $62.7M | 0.542x | 1.276x | 0.542x | **1.037x** |
| No. 31 (Yellow Stripe) | $62.2M | 0.772x | **0.885x** | 1.367x | **0.837x** |
| El sueno (La cama) / The Dream (The Bed) | $54.7M | 0.329x | **1.006x** | 0.768x | 0.768x |
| Knife Behind Back | $24.9M | 0.381x | **0.802x** | **1.002x** | 0.501x |
| Pie Fight Interior 12 | $10.4M | 0.462x | 0.433x | **0.817x** | 0.433x |
| Walkers With the Dawn and Morning | $10.7M | 0.792x | **0.978x** | **0.997x** | 0.633x |
| The Beautyful Ones | $4.7M | 1.224x | 0.591x | 0.633x | 0.306x |
| Force Field | $6.9M | 0.139x | 0.510x | 0.554x | 0.124x |
| A.I. God: Portrait of Alan Turing | $1.1M | 0.323x | 0.203x | 0.147x | 0.030x |
| Portrait of Edmond de Belamy | $432K | 1.503x | 0.416x | **1.156x** | 0.266x |
| Machine Hallucinations - ISS Dreams - A | $277K | 0.433x | 0.307x | 0.451x | 0.052x |
| Embedding Study 1 & 2 | $94K | 0.296x | 0.265x | 0.265x | 0.051x |
| Memories of Passersby I | $51K | 6.861x | 4.313x | 1.470x | 1.862x |