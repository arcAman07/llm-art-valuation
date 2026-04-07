#!/usr/bin/env python3
"""Run Experiment 1: Art Valuation (image-only vs basic-metadata).

Usage:
    python run_experiment1.py                    # full run
    python run_experiment1.py --pilot            # 2 artworks, 1 run, 1 model
    python run_experiment1.py --runs 1           # single run
    python run_experiment1.py --models gpt-5.4 sonnet-4.6  # subset of models
"""

import asyncio
import argparse
import json
import os
import sys
from pathlib import Path

# Ensure src is importable
sys.path.insert(0, str(Path(__file__).parent))

from src.experiment1 import Experiment1
from src.llm_client import MODELS


OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY", "")
if not OPENROUTER_API_KEY:
    print("ERROR: OPENROUTER_API_KEY environment variable not set.")
    print("  export OPENROUTER_API_KEY=your_key_here")
    sys.exit(1)
DATASET_PATH = Path(__file__).parent / "data" / "processed" / "dataset.json"
OUTPUT_DIR = Path(__file__).parent / "results" / "experiment1"


async def main():
    parser = argparse.ArgumentParser(description="Experiment 1: Art Valuation")
    parser.add_argument("--dataset", type=Path, default=DATASET_PATH)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--models", nargs="+", default=list(MODELS.keys()),
                        choices=list(MODELS.keys()))
    parser.add_argument("--runs", type=int, default=2)
    parser.add_argument("--temperature", type=float, default=0.7)
    parser.add_argument("--pilot", action="store_true",
                        help="Quick pilot: 2 artworks, 1 run, 1 model")
    args = parser.parse_args()

    # Load dataset
    if not args.dataset.exists():
        print(f"Dataset not found: {args.dataset}")
        sys.exit(1)

    with open(args.dataset) as f:
        dataset = json.load(f)

    print(f"Loaded {len(dataset['artworks'])} artworks from {args.dataset}")

    # Check images exist
    base_dir = Path(__file__).parent
    images_ok = 0
    for art in dataset["artworks"]:
        img = base_dir / art["image_path"]
        if img.exists():
            images_ok += 1
        else:
            print(f"  WARNING: image missing for {art['id']}: {img}")
    print(f"Images found: {images_ok}/{len(dataset['artworks'])}")

    # Pilot mode
    if args.pilot:
        dataset["artworks"] = dataset["artworks"][:2]
        args.runs = 1
        args.models = args.models[:1]
        print(f"\nPILOT MODE: {len(dataset['artworks'])} artworks, "
              f"{args.runs} run, models: {args.models}")

    # Run experiment
    experiment = Experiment1(
        openrouter_api_key=OPENROUTER_API_KEY,
        model_keys=args.models,
        num_runs=args.runs,
        temperature=args.temperature,
        output_dir=args.output_dir,
        randomize_order=True,
    )

    try:
        result = await experiment.run(dataset)
        print(f"\nDone. {result['total_valuations']} valuations saved to {result['output_dir']}")
    finally:
        await experiment.close()


if __name__ == "__main__":
    asyncio.run(main())
