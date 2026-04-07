# LLM Art Valuation

**Can large language models appraise fine art? Do they see, or do they remember?**

This repository contains the code, data, and full logs for **Experiment 1** of our research project: *Do Language Models Deceive? Strategic Behavior and Emergent Deception in Multi-Agent Auctions*.

> Companion repo for Experiment 2 (auction + deception): [llm-art-auction-deception](https://github.com/arcAman07/llm-art-auction-deception)

---

## What we tested

We showed four frontier LLMs — GPT-5.4, Claude Sonnet 4.6, Gemini 3.1 Pro, Qwen 3.6 Plus — 20 artworks under two conditions:

| Condition | What the model received |
|---|---|
| **Image only** | Painting image, no text |
| **With metadata** | Title, artist, year, medium, dimensions, description + image |

**Metric:** Valuation Ratio = model estimate ÷ true auction price. `1.00x` = perfect.  
**MALE** (Mean Absolute Log Error) = mean(|ln(estimate/true)|). Lower is better.

---

## Key Findings

| Model | Image-Only MALE | Metadata MALE | Improvement |
|---|---|---|---|
| Gemini 3.1 Pro | 1.155 | 0.523 | 2.2x |
| Claude Sonnet 4.6 | 1.594 | 0.672 | 2.4x |
| Qwen 3.6 Plus | 1.876 | 1.039 | 1.8x |
| **GPT-5.4** | **4.303** | **0.788** | **5.5x** |

GPT's 5.5× improvement when adding a text label reveals it functions more as a **lookup engine** than a visual appraiser — the image alone contributes almost nothing to its estimate.

---

## Repository Structure

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
│   └── raw/                    # ~37–40 raw JSON files per model
│       ├── gpt-5-4/
│       ├── sonnet-4-6/
│       ├── gemini-3-1-pro/
│       └── qwen-3-6/
├── plots/                      # Result visualizations (PNG)
├── experiment_1.md             # Full analysis write-up
└── x_blog_exp1.md              # Blog post
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

20 artworks across 4 categories:

| Category | Count | Examples |
|---|---|---|
| Masterpieces | 5 | Salvator Mundi, The Scream, Nu couché |
| Contemporary | 5 | Knife Behind Back, Walkers With the Dawn |
| Recent OOD | 5 | Klimt Portrait of Elisabeth Lederer (2024), Rothko No. 31 |
| AI Art | 5 | Memories of Passersby I, Portrait of Edmond de Belamy |

True prices span $51K → $450M. OOD artworks were sold at auction in 2024–2025 and are unlikely to appear in training data.

---

## Read the Full Analysis

- [`experiment_1.md`](experiment_1.md) — in-depth analysis with all tables and commentary
- [`x_blog_exp1.md`](x_blog_exp1.md) — blog post version
- [`logs/README.md`](logs/README.md) — cross-model results tables

