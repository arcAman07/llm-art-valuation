# Can LLMs Actually See Art? We Tested 4 Frontier Models on 20 Real Paintings.

We showed four frontier AI models — GPT-5.4, Claude Sonnet 4.6, Gemini 3.1 Pro, and Qwen 3.6 Plus — twenty real paintings and asked each one a simple question: *"What is this worth?"*

No auction history. No artist biography. Just the question every art dealer faces when a work walks through the door.

We ran each model under two conditions. First, **image only** — nothing but the painting itself. Then the **same painting with basic catalog metadata**: title, artist, year, and a one-paragraph description.

The gap between those two conditions turns out to be the most revealing finding in the experiment — because it tells you exactly *how* each model thinks about art, and whether it is actually looking at the image at all.

---

## Why This Experiment?

Art valuation sits at a fascinating intersection of visual perception, cultural knowledge, and market reasoning. A human expert appraiser does all three simultaneously: they look at the brushwork, recognize the style, recall comparable sales, and factor in provenance. We wanted to know which of these a large multimodal model actually does — and which it merely simulates by recalling text from training data.

The image-only vs. metadata comparison is the diagnostic. If a model is genuinely doing visual appraisal, metadata should help only a little — it already knows most of what it needs from the pixels. If a model is primarily doing database lookup, metadata unlocks everything and the image-only estimate will be near-useless.

---

## The Dataset

We curated 20 artworks with verified auction prices spanning five orders of magnitude — from $51,000 to $450 million. Each category was chosen to test a specific failure mode.

**Total true value of all 20 artworks combined: $1.46 billion.**

### Category 1 — Masterpieces ($78M–$450M)

Works so famous that every model almost certainly encountered them — and their prices — in training data. These test whether models can *recognize* iconic works from images alone and whether that recognition leads to calibrated estimates.

| Title | Artist | Year | True Auction Price |
|---|---|---|---|
| Salvator Mundi | Leonardo da Vinci | c. 1499–1510 | $450.3M |
| Nu couché | Amedeo Modigliani | 1917–18 | $170.4M |
| The Scream | Edvard Munch | 1895 | $119.9M |
| Portrait of Dr. Gachet | Vincent van Gogh | 1890 | $82.5M |
| Bal du moulin de la Galette | Pierre-Auguste Renoir | 1876 | $78.1M |

### Category 2 — Recent Out-of-Distribution ($54M–$236M)

Works by famous artists — Klimt, Van Gogh, Rothko, Kahlo — but *specific pieces* that sold at auction in November 2025, well after most model training cutoffs. Models know the artist's style and general market tier. They almost certainly have not memorized these specific prices. This is the **cleanest test of genuine visual appraisal ability**: a model that does well here is actually reading the image, not recalling a database entry.

| Title | Artist | Year | True Auction Price |
|---|---|---|---|
| Bildnis Elisabeth Lederer | Gustav Klimt | 1914–16 | $236.4M |
| Blumenwiese (Blooming Meadow) | Gustav Klimt | c. 1908 | $86.0M |
| Romans Parisiens (still life) | Vincent van Gogh | 1887 | $62.7M |
| No. 31 (Yellow Stripe) | Mark Rothko | 1958 | $62.2M |
| El sueño (The Dream) | Frida Kahlo | 1940 | $54.7M |

### Category 3 — Contemporary Art ($4.7M–$25M)

Living or recently active artists whose market value comes from gallery representation, critical reputation, and collector networks — none of which is visible in a pixel. A Yoshitomo Nara painting sells for $25M not because it looks expensive but because Nara is represented by top galleries, collected by major institutions, and critically validated. This category tests whether models understand that contemporary art value is *socially constructed*, invisible to visual analysis alone.

| Title | Artist | Year | True Auction Price |
|---|---|---|---|
| Knife Behind Back | Yoshitomo Nara | 2000 | $24.9M |
| Pie Fight Interior 12 | Adrian Ghenie | 2014 | $10.4M |
| Walkers With the Dawn and Morning | Julie Mehretu | 2008 | $10.7M |
| The Beautyful Ones | Njideka Akunyili Crosby | 2012 | $4.7M |
| Force Field | George Condo | 2010 | $6.9M |

### Category 4 — AI Art ($51K–$1.08M)

The newest and most volatile category. Market value here is driven almost entirely by narrative: who made it first, which auction house sold it, what the press said. The Portrait of Edmond de Belamy sold for $432K in 2018 — 43 times its high estimate — because it was the first AI artwork sold at a major auction house, not because it looked like $432K. None of that narrative is visible in the image.

| Title | Artist | Year | True Auction Price |
|---|---|---|---|
| A.I. God: Portrait of Alan Turing | Ai-Da Robot | 2024 | $1.08M |
| Portrait of Edmond de Belamy | Obvious (collective) | 2018 | $432K |
| Machine Hallucinations – ISS Dreams | Refik Anadol | 2025 | $277K |
| Embedding Study 1 & 2 | Holly Herndon & Mat Dryhurst | 2024 | $94.5K |
| Memories of Passersby I | Mario Klingemann | 2018 | $51K |

---

## The Setup

Each model appraised each artwork under both conditions, producing **307 successful valuations** out of 320 attempted (95.9% parse rate). Each model was given a structured prompt:

> **System:** "You are one of the world's foremost art appraisers. Examine the artwork and provide your estimate of fair market value."
>
> **Image-only prompt:** "Appraise the artwork shown. No identifying information has been provided."
>
> **Metadata prompt:** Title, artist, year, and a short description added. No auction history, no provenance, no price estimates.

Models responded in structured JSON with four fields: a dollar estimate, a confidence score (0–1), internal reasoning (private, only researchers see), and key factors. The internal reasoning field is unfiltered — the model's actual thought process before it commits to a number.

![Experiment 1 Setup](diagram_exp1_setup.png)

---

## How We Measure Accuracy

The core metric is the **valuation ratio**: model estimate ÷ true auction price.

- **1.00** = perfect
- **2.00** = model overvalued by 2×
- **0.50** = model undervalued by 2×

Art prices here span five orders of magnitude. A naive dollar-error metric would be completely dominated by the most expensive works — being off by $50M on a $450M Leonardo and being off by $50M on a $62M Rothko look identical, but one is an 11% error and the other is an 80% error. We need a metric that treats proportional errors consistently.

The correct tool is **Mean Absolute Log Error (MALE)**:

```
MALE = mean( |ln(estimate ÷ true)| )
```

**How to read MALE:**
- MALE = 0.0 → perfect
- MALE = 0.5 → off by ~1.6× on average
- MALE = 1.0 → off by ~2.7× on average
- MALE = 2.0 → off by ~7.4× on average
- MALE = 4.3 → off by ~73× on average ← GPT without a label

Crucially, MALE treats a 2× overestimate and a 2× underestimate as equally wrong. It penalizes proportional errors symmetrically, and it does not let a single massive overestimate blow up the average.

We also report the **median ratio** throughout — the middle estimate when all ratios are sorted. It is resistant to outliers and directly readable: a median of 0.76 means half the estimates were above 76% of true price and half were below.

---

## The Results

![Accuracy Bar Chart](exp1_accuracy_bar.png)

### Image Only — How Well Can Each Model See?

| Model | MALE ↓ (lower = better) | Median Ratio | Avg Confidence |
|---|---|---|---|
| **Gemini 3.1 Pro** | **1.106** | 0.761 | 0.91 |
| Claude Sonnet 4.6 | 1.570 | 0.672 | 0.57 |
| Qwen 3.6 Plus | 2.002 | 0.315 | 0.84 |
| GPT-5.4 | 4.577 | 0.033 | 0.33 |

Gemini wins by a large margin. Its median ratio of 0.761 means that in a typical appraisal, it lands within 25% of the true price from the image alone. GPT's median of 0.033 means it typically prices artworks at about 3 cents on the dollar.

### With Metadata — How Well Can Each Model Look Up?

| Model | MALE ↓ | Median Ratio | Avg Confidence |
|---|---|---|---|
| **Gemini 3.1 Pro** | **0.460** | 0.978 | 0.91 |
| Claude Sonnet 4.6 | 0.713 | 0.782 | 0.59 |
| GPT-5.4 | 0.732 | 0.657 | 0.70 |
| Qwen 3.6 Plus | 1.046 | 0.613 | 0.84 |

Gemini's median with metadata is 0.978 — essentially the market price. GPT dramatically recovers (MALE 4.6 → 0.7) and jumps over Qwen in the rankings. The order changes because GPT's recovery is driven by database lookup, not visual understanding. More on this below.

---

## The Four Models: What Each One Is Actually Doing

### Gemini 3.1 Pro — The Visual Appraiser

Gemini is the best model in both conditions, and the gap to second place is wide. But the more important question is *how* it appraises — and the answer reveals something genuinely impressive.

**The metadata gap tells the story.** Gemini's MALE changes from 1.106 (image-only) to 0.460 (with metadata) — a 2.4× improvement. Compare that to GPT's 4.577 → 0.732 (6.3× improvement). Gemini already has most of the information it needs from the image alone. Metadata helps, but it does not unlock a completely different mode.

**The Recent OOD test is the proof.** These are 2025 auction results — prices the model almost certainly never saw in training. On image-only Recent OOD works, Gemini's MALE is **0.414**. That means it is off by less than 1.5× on average from the true price, from pixels alone, on works it has never seen priced. This is genuine visual appraisal.

Here is Gemini appraising Salvator Mundi (true: $450.3M) from the image only:

> *"Based on the visual evidence provided, this artwork is immediately identifiable as the 'Salvator Mundi', widely attributed to Leonardo da Vinci... the sfumato, the interlaced knotwork on the stole, the curling ringlets of hair... The market comparable for this piece is explicitly its own unprecedented sale history."*
> **Estimate: $450,000,000** — ratio: **0.999** — Confidence: 0.95

Near-perfect, from a JPEG.

**Does Gemini memorize or truly see?** This is the key question. For famous masterpieces, it does recognize them from the image (Salvator Mundi, Edmond de Belamy) and anchors on memorized prices. But for Recent OOD works it *cannot* have memorized — a Klimt landscape that sold for $86M in late 2025 — it still estimates $75M (ratio 0.872) from the image alone. It is reading visual style, artist tier, and compositional quality to estimate market position, then translating that to a price range. That is a distinct skill from lookup.

**Gemini's weaknesses:** It overvalues masterpieces dramatically (Dr. Gachet: $250M estimate vs. $82.5M true, ratio 3.03; Renoir: $300M vs. $78M, ratio 3.84). It recognizes "this is a Van Gogh portrait" and assigns Van Gogh-level prestige across the board, regardless of which specific Van Gogh it is. And on AI Art without labels, it is nearly as lost as everyone else — the AI art market signal simply does not live in pixels.

---

### Claude Sonnet 4.6 — The Bold Recognizer With Poor Calibration

Claude ranks second overall (MALE 1.570 image-only) but with a striking failure pattern: it recognizes artworks from visual style and then *dramatically overvalues* them.

On masterpieces, Claude's average ratio image-only is **2.553** — it overvalues by 2.5× on average. The paradigm case is Portrait of Dr. Gachet (true: $82.5M):

> *"This bears unmistakable stylistic hallmarks of Vincent van Gogh, specifically his late Auvers-sur-Oise period (1890)... the Portrait of Dr. Paul Gachet, one of the most iconic and valuable paintings in art history."*
> **Estimate: $350,000,000** — ratio: **4.242** — Confidence: 0.82

Claude correctly identifies the painting. It correctly reasons that Van Gogh masterpieces command extraordinary prices. But it lands at $350M against a true value of $82.5M — 4.2× off. This is **memorized prestige without calibrated price knowledge**. Claude learned "Van Gogh masterpiece = one of the most valuable paintings ever" but did not internalize *which specific Van Goghs* set which specific records.

The same pattern across masterpieces: Renoir's Bal du moulin estimated at $320M (true: $78M, ratio 4.097), The Scream at $300M (true: $120M, ratio 2.502). Claude sees a famous Impressionist or Post-Impressionist painting, escalates to "museum-quality masterpiece" reasoning, and overshoots.

**Where Claude genuinely falls apart: contemporary art.** On Force Field by George Condo (true: $6.9M) from image only:

> *"This is a large-format, square-format painting executed in acrylic on canvas."*
> **Estimate: $22,000** — ratio: **0.003** — Confidence: 0.25

Twenty-two thousand dollars. For a $6.9M painting. Claude correctly senses it is uncertain (confidence 0.25), but it has no framework at all for pricing contemporary figurative painting. The social signals that make a George Condo worth millions — his gallery relationships, his museum retrospectives, his collector base — are entirely invisible from the canvas.

**Metadata helps Claude substantially** (MALE 1.570 → 0.713, 2.2× improvement), suggesting it was doing genuine visual recognition that labels then calibrate. But it remains directionally biased — it undervalues almost everything except famous masterpieces.

---

### Qwen 3.6 Plus — Highly Confident, Frequently Wrong

Qwen presents the most counterintuitive result: it reports the highest average confidence (0.84) while having the second-worst MALE (2.002 image-only). It is very confident about deeply wrong answers.

Its median ratio image-only is **0.315** — it typically prices artworks at about 30 cents on the dollar, far more conservative than Gemini or Claude. But it reports this with a confidence of 0.83 regardless. The confidence score is decorrelated from accuracy.

**The misidentification problem.** Where other models express uncertainty when they cannot identify a work, Qwen confidently assigns the wrong identity. Klimt's Blooming Meadow (true: $86M), image only:

> *"The artwork presented is a quintessential example of French Divisionism from the late 19th or early 20th century. The visual evidence points strongly towards the work of Henri Martin (1860–1943), a significant figure who transitioned from academic painting to a vibrant Divisionist style."*
> **Estimate: $125,000** — ratio: **0.001** — Confidence: 0.85

It looked at a Klimt worth $86 million and confidently priced it as a minor Henri Martin. The estimate is off by 688×. The confidence is 0.85. This is not uncertainty — this is wrong certainty.

**When Qwen does recognize a work, it performs reasonably.** Salvator Mundi: $475M estimate (ratio 1.055, confidence 0.95). Qwen 3.6 is a VL model trained extensively on visual data, and when it has enough context to recognize a famous work, its estimates are competitive with Gemini. The problem is that its recognition is brittle and its failure mode is loud — high-confidence wrong answers rather than low-confidence hedged answers.

**With metadata, Qwen still underperforms** (MALE 1.046 with labels, vs. 0.460 for Gemini). Even knowing the artist and title, Qwen's price calibration is worse than Gemini from pixels alone. This suggests its weakness is not primarily visual recognition but price calibration overall.

---

### GPT-5.4 — A Database Lookup Engine Disguised as an Appraiser

GPT is the most striking result in the dataset. Its image-only median ratio is **0.033**. GPT typically values artworks at about 3% of their true price from the image alone.

The extreme case: Modigliani's Nu couché (true: $170.4M), image only:

> *"The image depicts a reclining female nude... strongly reminiscent of early 20th-century modernism, and more specifically evocative of Amedeo Modigliani's idiom: elongated body, mask-like face, almond-shaped eyes..."*
> **Estimate: $8,000** — ratio: **0.000** — Confidence: 0.18

Read that carefully. GPT explicitly recognizes Modigliani's style — it names the elongated body, the mask-like face, the almond-shaped eyes. It has performed visual analysis. But having recognized a "Modigliani-esque" work, it then prices it as if attribution is unresolved, landing at $8,000 for something worth $170 million.

Now give it four words — "Nu couché, Modigliani, 1917":

> *"Assuming the work is authentic and correctly identified as Amedeo Modigliani's Nu couché from 1917–1918... Modigliani's reclining nudes occupy the absolute top tier of 20th-century painting."*
> **Estimate: $165,000,000** — ratio: **0.968** — Confidence: 0.72

From $8,000 to $165 million. A **20,625× increase** from adding a text label.

This is not metadata *helping* GPT appraise better. This is GPT switching from "unidentified object" mode to "database lookup" mode. In image-only mode, GPT's policy is essentially: *without confirmed attribution, I will not assign auction-house value regardless of visual evidence*. With the label, it retrieves the memorized price and produces a competent estimate.

GPT's MALE improvement from metadata is 6.3× — more than double the next-highest model (Gemini at 2.4×). Nothing else comes close.

**GPT's confidence tells the honest story.** Image-only average confidence: **0.33** — the lowest of any model. GPT knows it cannot see art. Its confidence jumps to 0.70 with metadata, tracking the genuine improvement. This is the one calibration finding that is actually accurate: GPT reports low confidence when it is unreliable and higher confidence when it has real information.

**GPT is not a bad model overall** — with labels, its MALE (0.732) is actually better than Qwen (1.046). The problem is that this performance is entirely contingent on having identifying text. Remove the label and GPT is useless as an art appraiser.

---

## The Metadata Effect: A Visual Analysis

![Metadata Effect](exp1_metadata_effect.png)

The single chart that summarizes the whole experiment:

| Model | Image-Only MALE | With Metadata MALE | Improvement Factor |
|---|---|---|---|
| GPT-5.4 | 4.577 | 0.732 | **6.3×** |
| Qwen 3.6 Plus | 2.002 | 1.046 | 1.9× |
| Claude Sonnet 4.6 | 1.570 | 0.713 | 2.2× |
| Gemini 3.1 Pro | 1.106 | 0.460 | 2.4× |

The improvement factor measures how much of each model's performance depends on the text label. Gemini (2.4×) and Claude (2.2×) improve modestly — they were already doing something useful from the image. GPT's 6.3× improvement is a category difference: it was essentially non-functional without the label.

### Does Adding Metadata Cause Overbidding or Underbidding?

The direction of the metadata effect varies significantly by category.

**Masterpieces — metadata makes models *more* overvalued:**
Every model already overvalues masterpieces from image alone (they recognize "museum-quality painting" and assign prestige premiums). Adding the label "Van Gogh" or "Leonardo" amplifies this further — their training data says "Van Gogh = record prices" and they anchor there regardless of which specific Van Gogh. Portrait of Dr. Gachet: GPT goes from 1.152× (image-only) to **3.333×** (with metadata). The label made GPT *worse*. The problem is not visual recognition — it is that the price signal for "Van Gogh" in training data is "hundreds of millions" without granularity between specific works.

**Recent OOD — metadata helps, but models still undershoot:**
With the artist name known, all models improve substantially but still cluster around 0.5–0.9× of true value. They know Klimt is expensive, but without the specific November 2025 sale data, they cannot reach $236M for Bildnis Elisabeth Lederer. Gemini's best estimate with metadata: $135M — real and grounded, but still 0.57× true. This is rational conservatism, not error: the model correctly knows this specific work's price is uncertain.

**Contemporary — the biggest rescue from metadata:**
Without a label, models price contemporary works as if they are decorative art — $22K for a $6.9M Condo, $75K for a $10.7M Mehretu. With the label, they recover dramatically: knowing it is a Julie Mehretu, models understand gallery-level market pricing and produce estimates in the right range. This confirms that contemporary art value truly *is* encoded in social context, not in the image.

**AI Art — metadata causes wild overshooting:**
With identifying information, *all* models massively overvalue Memories of Passersby I ($51K true). GPT: **$350K (6.9× true)**. Claude: **$220K (4.3×)**. Qwen: **$95K (1.9×)**. Gemini: **$75K (1.5×)**. Why? Because all models absorbed the cultural narrative around early AI art auctions ("first AI artwork sold at Sotheby's," "pioneering generative art") and convert narrative significance into price. The actual hammer price of $51K is dwarfed by the cultural footprint in training data.

---

## Category Deep Dive

![Category Heatmap](exp1_category_heatmap.png)

### Image-Only MALE by Category

| Category | Gemini | Claude | Qwen | GPT |
|---|---|---|---|---|
| **Masterpieces** | 0.75 | 0.87 | 0.52 | 3.46 |
| **Recent OOD** | **0.41** | **0.42** | 2.76 | 4.55 |
| **Contemporary** | **0.65** | 3.46 | 1.00 | 5.55 |
| **AI Art** | 3.05 | 1.63 | 2.87 | 3.66 |

**Masterpieces:** Qwen and Gemini are most accurate here — interestingly, even though Qwen struggles overall. Both recognize the iconic works and price them within 1–2× of true. GPT is worst (MALE 3.46) because it refuses to assign high values without a confirmed label, and most masterpiece estimates come in well under true value.

**Recent OOD — the fairest test:** Gemini (0.414) and Claude (0.421) are essentially tied, both genuinely impressive. They are reading visual style, medium, and artist-tier signals from the image to land within 1.5× of true on artworks with prices they never saw. Qwen (2.76) and GPT (4.55) collapse — their performance depends almost entirely on recognition, and when they cannot confidently recognize the specific work, they fail.

**Contemporary — Gemini dominates:** MALE of 0.65 means Gemini is off by about 1.9× on average for contemporary works from image alone. It correctly understands that a monumental abstract painting at major auction format has a market in the millions. Claude (3.46) and GPT (5.55) have no framework for this at all without labels — their estimates range from $4K to $120K for works worth $5M–$25M.

**AI Art — nobody wins:** Every model has MALE above 1.6 for AI art. Gemini is actually *worst* here (3.05) because it overestimates Memories of Passersby I by 2.4× after recognizing it. The AI art market is too new, too narrative-driven, and too disconnected from visual properties for any model to price reliably.

---

## Overvaluing vs. Undervaluing: The Direction of Errors

Most of the interesting story is not just *how wrong* each model is, but *in which direction*:

**Overvaluing (ratio > 1.0) happens when:**
- A model recognizes a famous work and assigns memorized prestige pricing (all models on The Scream, Gemini on Salvator Mundi)
- A model assigns cultural narrative significance to AI art (all models with metadata on Memories of Passersby I)
- Claude recognizes any famous artist's style and escalates to "masterpiece tier" pricing regardless of the specific work

**Undervaluing (ratio < 1.0) happens when:**
- A model cannot identify the work and defaults to "decorative art" or "commodity" pricing (GPT on virtually everything image-only)
- A model correctly identifies the style but lacks calibration for specific price levels (Qwen on most Recent OOD)
- A model correctly identifies contemporary medium/format but cannot access the social context that drives the premium (all models on contemporary art image-only)

**The asymmetry that matters most:** Overvaluation errors in masterpieces and undervaluation errors in contemporary art both stem from the same root cause — models use visual style as a proxy for prestige tier, and prestige tier as a proxy for price. This works when price tracks prestige (Impressionist masters), fails when price is determined by social networks (contemporary market), and fails catastrophically when cultural narrative overshadows actual transaction price (AI art).

---

## The Confidence Paradox

![Confidence vs Accuracy](exp1_confidence_vs_accuracy.png)

Each model's confidence score tells a secondary story about self-knowledge.

| Model | Avg Confidence (Image Only) | Avg Confidence (Metadata) | Calibration |
|---|---|---|---|
| Gemini 3.1 Pro | 0.92 | 0.91 | Earns it — accuracy matches |
| Qwen 3.6 Plus | 0.83 | 0.84 | Dangerously miscalibrated |
| Claude Sonnet 4.6 | 0.54 | 0.59 | Partially calibrated |
| GPT-5.4 | 0.33 | 0.70 | Honest about its limits |

**Gemini's calibration is the most impressive secondary finding.** When it reports 0.95 confidence — as it does on Salvator Mundi, Portrait of Edmond de Belamy, and several others — those estimates are within 5% of true. When it reports 0.65 or 0.85, the estimates are less precise. Confidence tracks accuracy.

**Qwen's miscalibration is a serious problem.** It reported 0.85 confidence while misidentifying a Klimt as Henri Martin ($86M work priced at $125K). It reported 0.85 confidence on a $62M Van Gogh still life priced at $450K. High confidence is Qwen's default output, not a signal of accuracy. Any system relying on Qwen's confidence scores as a quality indicator would be badly misled.

**GPT's honesty is notable given its poor performance.** Average image-only confidence of 0.33 is the only confidence score in the experiment that honestly reflects an inability to appraise. GPT knows it is guessing. Its confidence rises to 0.70 with metadata, accurately tracking a genuine improvement in estimate quality.

---

## Full Per-Artwork Results

The complete valuation ratios for every artwork and every model. **Bold** = within 20% of true price (ratio 0.80–1.20).

### Image Only

| Artwork | True Price | GPT-5.4 | Claude | Gemini | Qwen |
|---|---|---|---|---|---|
| **— Masterpieces —** | | | | | |
| Salvator Mundi | $450.3M | 0.004 | 1.221 | **0.999** | **1.055** |
| Nu couché | $170.4M | 0.000 | 0.704 | 0.704 | **0.968** |
| The Scream | $119.9M | 1.251 | 2.502 | 2.502 | 1.543 |
| Portrait of Dr. Gachet | $82.5M | 1.152 | 4.242 | 3.030 | 2.242 |
| Bal du moulin de la Galette | $78.1M | 0.230 | 4.097 | 3.841 | 3.649 |
| **— Recent OOD —** | | | | | |
| Bildnis Elisabeth Lederer (Klimt) | $236.4M | 0.762 | 0.402 | N/A | 0.305 |
| Blooming Meadow (Klimt) | $86.0M | 0.099 | 0.640 | **0.872** | 0.001 |
| Romans Parisiens (Van Gogh) | $62.7M | 0.000 | 1.196 | 0.670 | 0.007 |
| No. 31 Yellow Stripe (Rothko) | $62.2M | 0.000 | **0.885** | 1.400 | 0.724 |
| El sueño (Kahlo) | $54.7M | 0.064 | 0.640 | 0.457 | 0.439 |
| **— Contemporary —** | | | | | |
| Knife Behind Back (Nara) | $24.9M | 0.072 | 0.200 | 0.501 | N/A |
| Pie Fight Interior 12 (Ghenie) | $10.4M | 0.001 | 0.012 | **0.817** | 0.308 |
| Walkers With the Dawn (Mehretu) | $10.7M | 0.001 | 0.007 | 0.419 | 0.764 |
| The Beautyful Ones (Crosby) | $4.7M | 0.038 | 0.591 | 0.633 | N/A |
| Force Field (Condo) | $6.9M | 0.001 | 0.003 | 0.365 | 0.211 |
| **— AI Art —** | | | | | |
| A.I. God: Alan Turing (Ai-Da) | $1.08M | 0.003 | 0.032 | N/A | 0.323 |
| Edmond de Belamy (Obvious) | $432K | 0.028 | 1.272 | **0.925** | 0.029 |
| Machine Hallucinations (Anadol) | $277K | 0.004 | 0.016 | 0.003 | 0.006 |
| Embedding Study (Herndon) | $94.5K | 0.190 | 0.794 | 0.004 | 0.196 |
| Memories of Passersby I (Klingemann) | $51K | 0.157 | **0.882** | 2.352 | 0.055 |

### With Metadata

| Artwork | True Price | GPT-5.4 | Claude | Gemini | Qwen |
|---|---|---|---|---|---|
| **— Masterpieces —** | | | | | |
| Salvator Mundi | $450.3M | 0.777 | **0.933** | **0.999** | **1.055** |
| Nu couché | $170.4M | **0.968** | 0.763 | **0.968** | N/A |
| The Scream | $119.9M | 1.501 | 1.751 | 2.919 | 1.293 |
| Portrait of Dr. Gachet | $82.5M | 3.333 | 3.636 | 3.030 | 2.364 |
| Bal du moulin de la Galette | $78.1M | 1.601 | 2.561 | 1.921 | 1.472 |
| **— Recent OOD —** | | | | | |
| Bildnis Elisabeth Lederer (Klimt) | $236.4M | 0.360 | 0.465 | 0.571 | 0.613 |
| Blooming Meadow (Klimt) | $86.0M | 0.488 | 0.640 | **0.988** | 0.564 |
| Romans Parisiens (Van Gogh) | $62.7M | 0.542 | 1.276 | 0.542 | **1.037** |
| No. 31 Yellow Stripe (Rothko) | $62.2M | 0.772 | **0.885** | 1.367 | **0.837** |
| El sueño (Kahlo) | $54.7M | 0.329 | **1.006** | 0.768 | 0.768 |
| **— Contemporary —** | | | | | |
| Knife Behind Back (Nara) | $24.9M | 0.381 | **0.802** | **1.002** | 0.501 |
| Pie Fight Interior 12 (Ghenie) | $10.4M | 0.462 | 0.433 | **0.817** | 0.433 |
| Walkers With the Dawn (Mehretu) | $10.7M | 0.792 | **0.978** | **0.997** | 0.633 |
| The Beautyful Ones (Crosby) | $4.7M | 1.224 | 0.591 | 0.633 | 0.306 |
| Force Field (Condo) | $6.9M | 0.139 | 0.510 | 0.554 | 0.124 |
| **— AI Art —** | | | | | |
| A.I. God: Alan Turing (Ai-Da) | $1.08M | 0.323 | 0.203 | 0.147 | 0.030 |
| Edmond de Belamy (Obvious) | $432K | 1.503 | 0.416 | 1.156 | 0.266 |
| Machine Hallucinations (Anadol) | $277K | 0.433 | 0.307 | 0.451 | 0.052 |
| Embedding Study (Herndon) | $94.5K | 0.296 | 0.265 | 0.265 | 0.051 |
| Memories of Passersby I (Klingemann) | $51K | 6.861 | 4.313 | 1.470 | 1.862 |

*N/A = model did not return a parseable valuation. Bold = within 20% of true price. Memories of Passersby I (true: $51K) is overvalued by all models with metadata — because all models absorbed the cultural narrative around early AI art auctions and priced the story, not the work.*

---

## How This Compares to Human Appraisers

A professional art appraiser working from an image alone would be expected to:

1. Identify style, period, and probable artist range from visual evidence
2. Assess condition and quality within the identified context
3. Translate that to a market tier and price range based on recent comparables

Gemini is doing steps 1 and 3 reasonably well — enough to land within 1.5× of true value on Recent OOD works it has never seen priced. That is genuinely competitive with a professional assessment under conditions of no provenance information.

Claude is doing step 1 well (recognition) but failing step 3 (calibration) — it identifies artist and style correctly but then assigns "most valuable work by this artist" pricing regardless of the specific piece.

Qwen and GPT are not doing step 1 reliably without labels, and GPT does essentially nothing without them.

The deeper difference from humans: a human expert would have tacit knowledge about what makes *this specific Van Gogh* worth $82M rather than $350M — provenance, condition history, exhibition record, collector pedigree. None of that is in the image or the brief metadata we provided. Models are working from a cruder signal: style → artist → prestige tier → approximate price range. For the most famous works, that signal is calibrated from training data. For everything else, it degrades rapidly.

---

## Key Takeaways

**1. Gemini 3.1 Pro is the best visual art appraiser** — in both conditions, by a clear margin. Its image-only performance on out-of-distribution works (MALE 0.414) is the strongest evidence of genuine visual understanding in the dataset. It reads style, quality, and market tier from pixels in a way that produces calibrated estimates even without memorized prices.

**2. GPT-5.4 is a lookup engine, not an appraiser.** Its 20,625× improvement on Nu couché from adding a four-word label is not metadata helping it appraise better. It is a completely different cognitive process activating. Without a label, it treats art as near-worthless. With a label, it retrieves the memorized price. The image is not doing meaningful work.

**3. Claude overvalues famous artists, undervalues everything else.** Its pattern of correct recognition followed by inflated price assignment is distinctive and consistent. It knows Van Gogh is expensive; it does not know which Van Gogh is which price.

**4. Qwen is overconfident and brittle.** High confidence is its default regardless of accuracy. Its misidentification failures (Klimt priced as Henri Martin at $125K) are uniquely dangerous because they come with 0.85 confidence attached.

**5. Contemporary art value is invisible from pixels.** No model can price contemporary works well from images alone — MALE ranges from 0.65 (Gemini) to 5.55 (GPT). The market premium for living artists lives in social context, not visual properties.

**6. AI art is unpriceable from either images or labels.** The narrative premium in training data overwhelms the actual market price. With labels, all models overshoot Memories of Passersby I — they price the cultural story of "first AI artwork at Sotheby's" rather than the $51K hammer price.

**7. The metadata gap is a diagnostic for cognitive mode.** Measure how much a model improves from adding a text label. A large improvement (GPT: 6.3×) means the model is primarily doing database retrieval. A small improvement (Gemini: 2.4×) means it was already doing something useful visually. This diagnostic generalizes: whenever you ask an LLM to "evaluate" anything, you can measure whether it is reasoning from evidence or recalling from training by varying the contextual cues.

---

*In the next experiment, we put all four models in a live competitive auction with $500 million budgets and real-time bidding against each other. They started lying to each other within the first round. None of them were told to.*
