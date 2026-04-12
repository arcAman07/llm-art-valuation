# LLM Art Valuation

**Can large language models appraise fine art? Do they see, or do they remember?**

This repository contains the code, data, and full logs for **Experiment 1** of our research project: *Do Language Models Deceive? Strategic Behavior and Emergent Deception in Multi-Agent Auctions*.

> Companion repo for Experiment 2 (auction + deception): [llm-art-auction-deception](https://github.com/arcAman07/llm-art-auction-deception)

---

## What we tested

We showed four frontier LLMs (GPT-5.4, Claude Sonnet 4.6, Gemini 3.1 Pro, Qwen 3.6 Plus) 20 artworks under two conditions:

| Condition | What the model received |
|---|---|
| **Image only** | Painting image, no text |
| **With metadata** | Title, artist, year, description + image |

**Metric:** Valuation Ratio = model estimate / true auction price. `1.00x` = perfect.  
**MALE** (Mean Absolute Log Error) = mean(|ln(estimate / true)|). Lower is better.

The results are split across two blog posts. Blog Post 1 covers 15 traditional paintings (masterpieces, recent OOD, contemporary). Blog Post 2 covers 5 AI-generated artworks separately because the interpretation of accuracy is fundamentally different when narrative drives the price.

---

## Key Findings (15 Traditional Paintings)

| Model | Image-Only MALE | Metadata MALE | Improvement |
|---|---|---|---|
| **Gemini 3.1 Pro** | **0.267** | **0.170** | **1.57x** |
| Claude Sonnet 4.6 | 0.687 | 0.203 | 3.39x |
| Qwen 3.6 Plus | 0.702 | 0.244 | 2.87x |
| GPT-5.4 | 1.963 | 0.296 | 6.62x |

Gemini leads both conditions by a wide margin. Its image-only MALE of 0.267 actually outperforms GPT's metadata MALE of 0.296, meaning Gemini from pixels alone is more accurate than GPT with full artist attribution.

GPT does genuine visual reasoning and analysis but will not commit to a price without textual verification of the painting's identity. Even when explicitly told in the system prompt to "assume the artwork is authentic and legally available for sale," GPT still required metadata before pricing. That is not a failure of visual understanding but a fundamentally different approach to art evaluation.

### Memorization vs. Genuine Reasoning

| Model | Memorized | Genuine Reasoning | Failed |
|---|---|---|---|
| Gemini 3.1 Pro | 12/15 | 3/15 | 0 |
| GPT-5.4 | 3/15 | 12/15 | 0 |
| Claude Sonnet 4.6 | 7/15 | 7/15 | 0 |
| Qwen 3.6 Plus | 7/13 | 3/13 | 3 |

Gemini, the most accurate model, is also the most aggressive memorizer. GPT, the lowest scorer, did the most genuine visual reasoning. That tension is one of the most interesting findings in the study.

### AI Art Results (5 Paintings)

| Model | Image-Only MALE | Metadata MALE | Improvement |
|---|---|---|---|
| GPT-5.4 | 1.587 | 0.479 | 3.31x |
| Claude Sonnet 4.6 | 0.708 | 0.560 | 1.26x |
| Qwen 3.6 Plus | 1.245 | 0.989 | 1.26x |
| Gemini 3.1 Pro | 1.323 (n=4) | 0.397 | 3.33x |

AI art prices are driven by cultural narrative more than visual content. Every model that overperformed on AI art image-only was memorizing the cultural moment, not reading the canvas.

---

## Prompts

All models received the same system prompt in both conditions. The key instruction was:

> *"Provide your professional estimate of its current fair market value, what this piece would realistically sell for at a major international auction today, **assuming it is authentic and legally available for sale**."*

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
│   └── raw/                    # ~37-40 raw JSON files per model
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

20 artworks across 4 categories, total value $1.46 billion:

| Category | Count | Price Range | Examples |
|---|---|---|---|
| Masterpieces | 5 | $78M - $450M | Salvator Mundi, Nu couche, The Scream |
| Recent OOD | 5 | $54M - $236M | Klimt Bildnis Elisabeth Lederer, Rothko No. 31 |
| Contemporary | 5 | $4.7M - $25M | Knife Behind Back, Walkers With the Dawn |
| AI Art | 5 | $51K - $1.08M | Memories of Passersby I, Portrait of Edmond de Belamy |

True prices span $51K to $450M. OOD artworks were sold at auction in November 2025 and are unlikely to appear in training data. AI art prices are driven primarily by cultural milestone status rather than visual quality.

---

## Read the Full Analysis

- **Blog Post 1:** [Can Frontier AI Models Read a Painting?](https://arcaman07.github.io/blog/can-llms-see-art.html) - 15 paintings across masterpieces, recent OOD, and contemporary art
- **Blog Post 2:** [When AI Models Price AI Art](https://arcaman07.github.io/blog/when-ai-models-price-ai-art.html) - 5 AI artworks where narrative drives the price
- [`experiment_1.md`](experiment_1.md) - in-depth analysis with all tables and commentary
- [`logs/README.md`](logs/README.md) - cross-model results tables
