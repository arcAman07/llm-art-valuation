# LLM Art Valuation

**Can frontier multimodal models actually read a painting, or are they just reading the label next to it?**

This repository contains the code, dataset, and per-painting reasoning logs for Experiment 1 of my **LLM Art Auctions** research series. Four frontier multimodal models (Gemini 3.1 Pro, Claude Sonnet 4.6, GPT-5.4, Qwen 3.6 Plus) appraise the same set of paintings in two conditions, and the gap between the two conditions turns out to be the most revealing part of the experiment.

> **Blog Post 1:** [Can Frontier AI Models Read a Painting?](https://arcaman07.com/blog/can-llms-see-art.html)
>
> This is the first post in the LLM Art Auctions series. Subsequent posts cover AI-generated art and a multi-agent English ascending-price auction with all four models bidding against each other.

---

## The setup

Each model appraises each artwork twice:

| Condition | What the model receives |
|-----------|------------------------|
| **Image only** | The painting image, with no title, artist, year, or description |
| **With metadata** | The painting image plus title, artist, year, and a brief description |

**Web search and any other external tools were disabled in both conditions.** Every estimate comes from the image plus (optionally) the four-word metadata label and whatever the model has internalized from training. No live lookups.

The system prompt in both conditions told every model to assume the artwork was authentic and legally available for sale and to give its professional fair-market estimate. Each model returned a dollar estimate, a self-reported confidence score from 0 to 1, and an internal reasoning trace that is logged verbatim in `logs/raw/`.

### Metric

**MALE** (Mean Absolute Log Error) = mean( |log₁₀(estimate / true)| ). Lower is better.

MALE treats overestimates and underestimates symmetrically, which matters on a dataset that spans five orders of magnitude in dollar price. Every MALE value translates to a typical multiplicative error factor via 10^MALE: a MALE of 0.3 means off by about 2x on average, 1.0 means 10x, and 1.963 means about 90x. A flat $50M constant guess scores around 0.46 on this dataset as a sanity-check baseline.

---

## Headline results (15 traditional paintings, run 0)

| Model | Image-Only MALE | Metadata MALE | Improvement Factor |
|-------|----------------:|--------------:|-------------------:|
| **Gemini 3.1 Pro** | **0.267** | **0.170** | 1.57x |
| Claude Sonnet 4.6 | 0.687 | 0.203 | 3.39x |
| Qwen 3.6 Plus | 0.649 | 0.259 | 2.51x |
| GPT-5.4 | 1.963 | 0.296 | **6.62x** |

Gemini 3.1 Pro leads both conditions by a wide margin. Its image-only MALE of 0.267 is actually lower than GPT-5.4's *metadata* MALE of 0.296, which means Gemini 3.1 Pro from pixels alone outperforms GPT-5.4 with the artist name and title handed to it.

GPT-5.4 does genuine visual reasoning but refuses to commit to a price without textual verification of the painting's identity. The Modigliani example from the blog post is the cleanest single illustration: GPT-5.4 correctly reads the style in the image-only run and names Amedeo Modigliani in its reasoning, then prices the work at $8,000 because the trace says "no basis for attribution" without provenance. With four words of metadata the same model prices the same image at $165M. The vision model did not change between the two runs; a policy gate opened.

## Recognition vs Commitment

The blog post argues that the right axis for distinguishing these four models is not "can they see" but what they do with recognition once they have it. I classified every image-only reasoning trace on three things: did the model name the correct artist from the pixels, did it name the specific painting, and did it cite a specific auction price or sale history.

| Model | Named the artist | Named the title | Cited auction price / year |
|-------|------------------|------------------|----------------------------|
| Gemini 3.1 Pro | 15 / 15 | 10 / 15 | 13 / 15 |
| Claude Sonnet 4.6 | 15 / 15 | 8 / 15 | 13 / 15 |
| GPT-5.4 | 10 / 15 | 6 / 15 | 6 / 15 |
| Qwen 3.6 Plus | 12 / 15 (3 API failures) | 8 / 15 | 12 / 15 |

Recognition is nearly saturated. Three of the four models named the correct artist from the image alone on essentially every painting, including paintings that sold at auction in November 2025 (after every model's training cutoff). The four models split into archetypes on what they do with that recognition:

- **Gemini 3.1 Pro** recognizes and commits, with calibration. Best model in both conditions.
- **Claude Sonnet 4.6** recognizes and commits, but miscalibrates. It assigns peak prices to recognized artists regardless of which specific work is in front of it (Dr. Gachet at $350M against a true $82.5M).
- **GPT-5.4** recognizes the artist and then refuses to commit without a text label authenticating the attribution. I call this the **commit threshold**. The blog post walks through it with verbatim reasoning traces and a two-state diagram.
- **Qwen 3.6 Plus** commits enthusiastically, including on the small number of works where its recognition is wrong. Two of its fifteen runs are confident misidentifications at 0.85 confidence.

## AI art subset (5 paintings, covered in Blog Post 2)

| Model | Image-Only MALE | Metadata MALE | Improvement Factor |
|-------|----------------:|--------------:|-------------------:|
| GPT-5.4 | 1.587 | 0.479 | 3.31x |
| Claude Sonnet 4.6 | 0.708 | 0.560 | 1.26x |
| Qwen 3.6 Plus | 1.245 | 0.989 | 1.26x |
| Gemini 3.1 Pro | 1.323 (n=4) | 0.397 | 3.33x |

AI art prices are driven by cultural narrative more than by visual content. Every model that "overperformed" on AI art image-only was memorizing the cultural moment rather than reading the canvas. The separate Blog Post 2 covers this subset in depth.

---

## Prompts

All models received the same system prompt in both conditions. The key instruction was:

> *"Provide your professional estimate of its current fair market value, what this piece would realistically sell for at a major international auction today, assuming it is authentic and legally available for sale."*

### Image-Only Condition

> Please appraise the artwork shown in the image above. Base your valuation solely on what you can see. You have not been provided with any identifying information — no title, artist, date, or provenance.

### Metadata Condition

> Please appraise the following artwork:
> - **Title:** {title}
> - **Artist:** {artist}
> - **Year:** {year}
> - **Description:** {description}
>
> The image of the artwork is shown above. Base your valuation on the image and the metadata provided. No provenance documentation, condition report, or auction history has been supplied.

The full prompt implementation is in [`src/experiment1.py`](src/experiment1.py).

---

## Repository structure

```
├── run_experiment1.py          # Entry point
├── src/
│   ├── llm_client.py           # Unified API client (OpenRouter + AWS Bedrock)
│   └── experiment1.py          # Experiment logic, prompts, valuation runner
├── data/
│   └── processed/
│       ├── dataset.json        # 20 artworks: true prices, categories, metadata
│       └── original_descriptions.json
├── logs/
│   ├── README.md               # Cross-model results tables
│   ├── gpt-5-4.md              # GPT-5.4: per-artwork reasoning + ratios
│   ├── sonnet-4-6.md           # Claude Sonnet 4.6
│   ├── gemini-3-1-pro.md       # Gemini 3.1 Pro
│   ├── qwen-3-6.md             # Qwen 3.6 Plus
│   └── raw/                    # Raw JSON reasoning traces per model
│       ├── gpt-5-4/
│       ├── sonnet-4-6/
│       ├── gemini-3-1-pro/
│       └── qwen-3-6/
├── plots/                      # Result visualizations (PNG)
├── experiment_1.md             # Full analysis write-up
└── x_blog_exp1.md              # Blog post draft
```

---

## Setup

```bash
# 1. Clone
git clone https://github.com/arcAman07/llm-art-valuation.git
cd llm-art-valuation

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API keys
cp .env.example .env
# Edit .env with your OpenRouter key and AWS credentials
export OPENROUTER_API_KEY=your_key_here
# AWS Bedrock: configure via `aws configure` or set env vars

# 4. Add artwork images to data/raw/images/
#    (not tracked in git — filenames listed in data/processed/dataset.json)

# 5. Run
python run_experiment1.py --pilot        # quick test: 2 artworks, 1 model
python run_experiment1.py --runs 1       # full run
```

---

## Dataset

20 artworks across 4 categories, total value roughly $1.46 billion:

| Category | Count | Price Range | Examples |
|----------|------:|-------------|----------|
| Masterpieces | 5 | $78M – $450M | Salvator Mundi, Nu couché, The Scream, Dr. Gachet, Moulin de la Galette |
| Recent OOD | 5 | $54M – $236M | Bildnis Elisabeth Lederer, Blumenwiese, Romans Parisiens, No. 31 Yellow Stripe, El sueño |
| Contemporary | 5 | $4.7M – $25M | Knife Behind Back (Nara), Pie Fight Interior 12 (Ghenie), Walkers With the Dawn (Mehretu), The Beautyful Ones (Akunyili Crosby), Force Field (Condo) |
| AI Art | 5 | $51K – $1.08M | Memories of Passersby I, Portrait of Edmond de Belamy, Machine Hallucinations, Embedding Study, A.I. God: Portrait of Alan Turing |

The Recent OOD artworks were sold at auction in November 2025, close to or just past most model training cutoffs, and were chosen specifically because the specific hammer prices were unlikely to be memorized from training data. They are the cleanest test of genuine visual appraisal in the dataset.

---

## Auditing the reasoning traces

Every model call is logged verbatim in `logs/raw/{model}/`. File naming follows `{artwork_id}_{condition}_run{run}_{model}.json`. Each file contains the full internal reasoning trace, the dollar estimate, the confidence score, and the key factors the model identified.

For example, to read GPT-5.4's image-only reasoning on Salvator Mundi:

```bash
cat logs/raw/gpt-5-4/mp_001_image_only_run0_gpt-5.4.json
```

Cross-model per-artwork tables are also available in the human-readable per-model logs at `logs/gpt-5-4.md`, `logs/sonnet-4-6.md`, `logs/gemini-3-1-pro.md`, and `logs/qwen-3-6.md`.

---

## Read the full analysis

- **Blog Post 1:** [Can Frontier AI Models Read a Painting?](https://arcaman07.com/blog/can-llms-see-art.html) — 15 traditional paintings across masterpieces, recent OOD, and contemporary art, with the Recognition vs Commitment axis and the GPT commit threshold
- **Blog Post 2:** [When the Price Is Not in the Image](https://arcaman07.com/blog/when-ai-models-price-ai-art.html) — a stress test of the metadata improvement diagnostic on five AI-generated artworks where the price lives in the narrative rather than the pixels (coming soon)
- [`experiment_1.md`](experiment_1.md) — in-depth analysis with all tables and commentary
- [`logs/README.md`](logs/README.md) — cross-model results tables

## Citation

```bibtex
@misc{sharma2026llmartvaluation,
  title = {Can Frontier AI Models Read a Painting? Recognition vs Commitment in Multimodal Art Valuation},
  author = {Sharma, Aman},
  year = {2026},
  url = {https://arcaman07.com/blog/can-llms-see-art.html}
}
```

## License

MIT License
