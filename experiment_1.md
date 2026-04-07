# Experiment 1: Sealed-Bid Art Valuation — In-Depth Analysis

## Setup

- **20 artworks** across 4 categories (masterpiece, contemporary, AI art, recent OOD)
- **4 LLMs**: GPT-5.4, Claude Sonnet 4.6, Gemini 3.1 Pro, Qwen 3.6 Plus
- **2 conditions**: image-only vs. basic metadata (title, artist, year, description)
- ~2 runs per combination = **307 successful valuations** (out of 320 attempted, 95.9% parse rate)
- Key metric: **valuation ratio** (predicted / actual auction price), where **1.0 = perfect**

## Overall Accuracy Rankings

| Model | Mean Absolute Error from 1.0 (lower = better) | Median Ratio (image-only) | Median Ratio (metadata) |
|---|---|---|---|
| **Gemini 3.1 Pro** | **0.559** | 0.817 | 0.973 |
| Qwen 3.6 Plus | 0.707 | 0.308 | 0.633 |
| GPT-5.4 | 0.808 | 0.006 | 0.720 |
| Claude Sonnet 4.6 | 0.830 | 0.675 | 0.751 |

## Which LLM Best Mirrors Human Aesthetic Appreciation?

### Gemini 3.1 Pro — The Best Art Critic

Gemini is the most calibrated appraiser by a clear margin. Its valuations hug true auction prices most closely across all categories. With metadata, its median ratio is 0.973 — near perfect. It also has the highest confidence scores (avg 0.91), and unlike other models, that confidence is justified.

Critically, Gemini shows the **smallest metadata effect** — its average ratio barely changes from 1.086 (image-only) to 1.068 (metadata). This stability suggests Gemini genuinely evaluates visual qualities rather than relying on identification and memory retrieval.

### Claude Sonnet 4.6 — Bold but Erratic

Claude is willing to assign high values from images alone (especially for masterpieces) but frequently overshoots. It has genuine visual sensitivity — it can distinguish quality — but lacks calibration. Its confidence is low-moderate (avg 0.57), appropriately reflecting its uncertainty. It dramatically overvalues masterpieces (avg 2.725x in image-only) while dramatically undervaluing contemporary art (avg 0.191x).

### Qwen 3.6 Plus — Conservative Undervaluer

Qwen systematically prices things below market value in both conditions. Paradoxically, it reports the second-highest confidence (avg 0.84) despite being wrong in a conservative direction. Its confidence calibration mechanism is disconnected from its valuation accuracy — overconfident in its lowball estimates.

### GPT-5.4 — Lookup Engine, Not an Appraiser

GPT-5.4 is essentially non-functional as a visual art appraiser. Its image-only median ratio of **0.006** means it priced most artworks at less than 1% of their true value. It treats unidentified art as nearly worthless. However, with metadata it becomes reasonably competent (median 0.720), revealing that it is primarily matching titles/artists to memorized auction data rather than performing aesthetic evaluation. Its low confidence (avg 0.51) is at least honest about its uncertainty.

## The Metadata Effect: Critical Caveat

The basic_metadata condition provides **title, artist, year, and description** — which for famous works is sufficient for any model to identify the piece and recall memorized auction prices from training data. This means:

- **The image-only condition is the only real test of aesthetic/visual valuation ability.**
- GPT-5.4's dramatic jump (median 0.006 to 0.720) is almost entirely memory retrieval activating, not metadata enhancing visual appraisal.
- All models' improvement with metadata is at least partly driven by recognition and memory, not by genuine enhancement of visual assessment.

### Metadata Impact by Model (average ratio)

| Model | Image-Only | With Metadata | Delta |
|---|---|---|---|
| GPT-5.4 | 0.219 | 1.092 | +0.873 |
| Qwen 3.6 Plus | 0.698 | 0.766 | +0.068 |
| Claude Sonnet 4.6 | 1.070 | 1.185 | +0.115 |
| Gemini 3.1 Pro | 1.086 | 1.068 | -0.018 |

## Category-Level Analysis

### Masterpieces (Salvator Mundi, The Scream, Nu couche, Portrait of Dr. Gachet, Bal du moulin de la Galette)

Every model **overvalues masterpieces** from image-only — Claude at 2.725x, Gemini at 2.174x, Qwen at 1.915x. This implies training data contamination or learned associations between "looks like a famous painting" and high value. GPT-5.4 is the exception: it undervalues from image alone (0.600x avg), then overcorrects with metadata (1.639x) — pure lookup behavior.

### Contemporary Art (Force Field, Knife Behind Back, Pie Fight Interior 12, The Beautyful Ones, Walkers With the Dawn and Morning)

The **hardest category** for all models in image-only:

| Model | Image-Only Avg | Metadata Avg |
|---|---|---|
| Gemini 3.1 Pro | 0.594 | 0.858 |
| Qwen 3.6 Plus | 0.222 | 0.330 |
| Claude Sonnet 4.6 | 0.191 | 0.634 |
| GPT-5.4 | 0.012 | 0.541 |

Models struggle to assess the market premium from artist reputation, gallery representation, and critical discourse — factors invisible in the image.

### AI Art (Edmond de Belamy, Memories of Passersby I, Machine Hallucinations, Embedding Study 1 & 2, A.I. God)

The most volatile category. Metadata causes wild swings — "Memories of Passersby I" is valued at 0.255x by GPT image-only but 5.587x with metadata (a 22x swing). Claude goes from 0.716x to 4.607x. Once models identify a "famous AI art piece," they massively overvalue it, likely because these pieces received outsized media attention relative to their actual prices.

### Recent OOD (Out-of-Distribution) Works

These are less-famous works the models are least likely to have memorized. This is the **cleanest test of pure aesthetic appreciation**:

| Model | Image-Only Avg (recent_ood) |
|---|---|
| **Gemini 3.1 Pro** | **0.886** |
| Claude Sonnet 4.6 | 0.735 |
| Qwen 3.6 Plus | 0.405 |
| GPT-5.4 | 0.176 |

Gemini wins convincingly in the fairest comparison.

## Key Surprising Findings

1. **GPT-5.4's metadata dependence is the headline result.** A median ratio going from 0.006 to 0.720 is not a refinement — it is a completely different mode of operation. No other model shows anything close to this dependence.

2. **All models overvalue masterpieces** even from image alone. This is the opposite of what you would expect from pure visual appraisal and implies learned associations or image-based recognition of iconic works.

3. **Contemporary art is universally undervalued** in image-only. The market premium from reputation, gallery backing, and critical discourse is invisible in pixels.

4. **Gemini barely changes with metadata** (1.086 to 1.068 avg ratio). This could reflect genuinely good visual appraisal, or it could mean Gemini is already recognizing artworks from images alone. The recent OOD results (0.886 image-only) suggest it is genuinely the strongest visual appraiser.

5. **Qwen is overconfident yet conservative** — a paradoxical combination. It systematically undervalues (avg 0.732) but reports high confidence (0.84). Its confidence mechanism is disconnected from valuation accuracy.

## Raw Summary Statistics

- Total valuations attempted: 320
- Parse success rate: 95.9%
- By condition: image_only avg $72.6M, basic_metadata avg $79.6M
- Masterpieces avg valuation: $240.7M (true avg: $182.4M) — overvalued
- AI art avg valuation: $142K (true avg: $360K) — undervalued
- Recent OOD avg valuation: $57.9M (true avg: $97.3M) — undervalued
- Contemporary avg valuation: $5.0M (true avg: $11.3M) — undervalued
