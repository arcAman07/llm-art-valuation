# Experiment 1 — Appraisal Logs: Qwen 3.6 Plus

| Field | Value |
|---|---|
| **Model** | Qwen 3.6 Plus |
| **Organisation** | Alibaba |
| **Task** | Estimate fair market value of each artwork |
| **Condition A** | Image only — painting shown, no text |
| **Condition B** | Basic metadata — title, artist, year, description |
| **Output** | Dollar estimate · confidence (0–1) · internal reasoning |

Valuation ratio = estimate ÷ true auction price.
`1.000x` = perfect &nbsp;·&nbsp; `>1.15x` = overvalued &nbsp;·&nbsp; `<0.85x` = undervalued &nbsp;·&nbsp; **bold** = within 20% of true price.

---

## Summary — Condition A: Image Only

| Artwork | Artist | Category | True Price | Estimate | Ratio | Bias | Conf |
|---|---|---|---|---|---|---|---|
| Salvator Mundi | Leonardo da Vinci | Masterpieces | $450.3M | $475.0M | **1.055x** | fair | 0.95 |
| Nu couche | Amedeo Modigliani | Masterpieces | $170.4M | $165.0M | **0.968x** | fair | 0.95 |
| The Scream | Edvard Munch | Masterpieces | $119.9M | $185.0M | 1.543x | over | 0.95 |
| Portrait of Dr. Gachet | Vincent van Gogh | Masterpieces | $82.5M | $185.0M | 2.242x | over | 0.95 |
| Bal du moulin de la Galette | Pierre-Auguste Renoir | Masterpieces | $78.1M | $285.0M | 3.649x | over | 0.85 |
| Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer) | Gustav Klimt | Recent OOD | $236.4M | $72.0M | 0.305x | under | 0.92 |
| Blumenwiese (Blooming Meadow) | Gustav Klimt | Recent OOD | $86.0M | $125K | 0.001x | under | 0.85 |
| Piles de romans parisiens et roses dans un verre (Romans parisiens) | Vincent van Gogh | Recent OOD | $62.7M | $450K | 0.007x | under | 0.85 |
| No. 31 (Yellow Stripe) | Mark Rothko | Recent OOD | $62.2M | $45.0M | 0.724x | under | 0.85 |
| El sueno (La cama) / The Dream (The Bed) | Frida Kahlo | Recent OOD | $54.7M | $24.0M | 0.439x | under | 0.90 |
| Knife Behind Back | Yoshitomo Nara | Contemporary | $24.9M | — | N/A | — | — |
| Pie Fight Interior 12 | Adrian Ghenie | Contemporary | $10.4M | $3.2M | 0.308x | under | 0.90 |
| Walkers With the Dawn and Morning | Julie Mehretu | Contemporary | $10.7M | $8.2M | 0.764x | under | 0.90 |
| The Beautyful Ones | Njideka Akunyili Crosby | Contemporary | $4.7M | — | N/A | — | — |
| Force Field | George Condo | Contemporary | $6.9M | $1.4M | 0.211x | under | 0.85 |
| A.I. God: Portrait of Alan Turing | Ai-Da Robot | AI Art | $1.1M | $350K | 0.323x | under | 0.85 |
| Portrait of Edmond de Belamy | Obvious (collective) | AI Art | $432K | $12K | 0.029x | under | 0.75 |
| Machine Hallucinations - ISS Dreams - A | Refik Anadol | AI Art | $277K | $2K | 0.006x | under | 0.60 |
| Embedding Study 1 & 2 | Holly Herndon & Mat Dryhurst | AI Art | $94K | $18K | 0.196x | under | 0.60 |
| Memories of Passersby I | Mario Klingemann | AI Art | $51K | $3K | 0.055x | under | 0.45 |

## Summary — Condition B: With Metadata

| Artwork | Artist | Category | True Price | Estimate | Ratio | Bias | Conf |
|---|---|---|---|---|---|---|---|
| Salvator Mundi | Leonardo da Vinci | Masterpieces | $450.3M | $475.0M | **1.055x** | fair | 0.95 |
| Nu couche | Amedeo Modigliani | Masterpieces | $170.4M | — | N/A | — | — |
| The Scream | Edvard Munch | Masterpieces | $119.9M | $155.0M | 1.293x | over | 0.95 |
| Portrait of Dr. Gachet | Vincent van Gogh | Masterpieces | $82.5M | $195.0M | 2.364x | over | 0.90 |
| Bal du moulin de la Galette | Pierre-Auguste Renoir | Masterpieces | $78.1M | $115.0M | 1.472x | over | 0.85 |
| Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer) | Gustav Klimt | Recent OOD | $236.4M | $145.0M | 0.613x | under | 0.85 |
| Blumenwiese (Blooming Meadow) | Gustav Klimt | Recent OOD | $86.0M | $48.5M | 0.564x | under | 0.92 |
| Piles de romans parisiens et roses dans un verre (Romans parisiens) | Vincent van Gogh | Recent OOD | $62.7M | $65.0M | **1.037x** | fair | 0.95 |
| No. 31 (Yellow Stripe) | Mark Rothko | Recent OOD | $62.2M | $52.0M | **0.837x** | under | 0.85 |
| El sueno (La cama) / The Dream (The Bed) | Frida Kahlo | Recent OOD | $54.7M | $42.0M | 0.768x | under | 0.85 |
| Knife Behind Back | Yoshitomo Nara | Contemporary | $24.9M | $12.5M | 0.501x | under | 0.85 |
| Pie Fight Interior 12 | Adrian Ghenie | Contemporary | $10.4M | $4.5M | 0.433x | under | 0.85 |
| Walkers With the Dawn and Morning | Julie Mehretu | Contemporary | $10.7M | $6.8M | 0.633x | under | 0.85 |
| The Beautyful Ones | Njideka Akunyili Crosby | Contemporary | $4.7M | $1.4M | 0.306x | under | 0.90 |
| Force Field | George Condo | Contemporary | $6.9M | $850K | 0.124x | under | 0.85 |
| A.I. God: Portrait of Alan Turing | Ai-Da Robot | AI Art | $1.1M | $32K | 0.030x | under | 0.75 |
| Portrait of Edmond de Belamy | Obvious (collective) | AI Art | $432K | $115K | 0.266x | under | 0.75 |
| Machine Hallucinations - ISS Dreams - A | Refik Anadol | AI Art | $277K | $14K | 0.052x | under | 0.65 |
| Embedding Study 1 & 2 | Holly Herndon & Mat Dryhurst | AI Art | $94K | $5K | 0.051x | under | 0.65 |
| Memories of Passersby I | Mario Klingemann | AI Art | $51K | $95K | 1.862x | over | 0.85 |

---

## Artwork-by-Artwork Detail

---
### Masterpieces

#### Salvator Mundi

| | |
|---|---|
| **True auction price** | **$450.3M** |
| Artist | Leonardo da Vinci |
| Year | c.1499-1510 |
| Medium | Oil on walnut panel |
| Dimensions | 65.6 x 45.4 cm (25.8 x 17.9 in) |
| Style | High Renaissance |
| Auction | Christie's · 2017-11-15 |
| In training data | Yes |

> Depiction of Christ as Savior of the World, holding a crystal orb in his left hand while raising his right in benediction. One of fewer than 20 known paintings attributed to Leonardo. The work shows characteristic sfumato technique and meticulous rendering of the crystal sphere.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$475.0M** | **$475.0M** |
| **Ratio** | **1.055x** (fair) | **1.055x** (fair) |
| **Confidence** | 0.95 | 0.95 |

**Image Only — model reasoning:**

> The artwork presented is visually identifiable as the *Salvator Mundi*, a depiction of Christ as the Savior of the World. Based on the visual evidence—the specific handling of the sfumato technique, the anatomical rendering of the right hand in benediction, the intricate ringlets of the hair, and the distinct blue robe with gold embroidery—this is the work attributed to Leonardo da Vinci, painted circa 1500. The prompt instructs me to assume authenticity; therefore, I am appraising this as a genuine Leonardo da Vinci, a category of object that represents the absolute apex of the art market....

**Key factors cited:**

- Attribution to Leonardo da Vinci
- Extreme Scarcity (Fewer than 20 extant paintings)
- Artistic Mastery (Sfumato and anatomical precision)
- Historical Significance and Iconography
- Market Precedent (2017 World Record Sale)

**With Metadata — model reasoning:**

> The artwork presented is the *Salvator Mundi*, attributed to Leonardo da Vinci. As an appraiser, I must evaluate this work based on its artistic merit, historical significance, and current market dynamics, accepting the premise of the prompt that the work is authentic.   Artistically, the painting demonstrates the quintessential qualities of Leonardo's mature style. The figure of Christ is rendered with the master's signature *sfumato*—the smoky, imperceptible transition between colors and tones—which is particularly evident in the soft modeling of the face, the curls of the hair, and the blessing hand....

**Key factors cited:**

- Attribution to Leonardo da Vinci (Apex Artist)
- Extreme Rarity (Fewer than 20 surviving works)
- Technical Mastery (Sfumato and Anatomical Precision)
- Iconographic Significance (Salvator Mundi)
- Ultra-High-Net-Worth Market Demand for Trophy Assets

#### Nu couche

| | |
|---|---|
| **True auction price** | **$170.4M** |
| Artist | Amedeo Modigliani |
| Year | 1917-1918 |
| Medium | Oil on canvas |
| Dimensions | 60 x 92 cm (23.6 x 36.2 in) |
| Style | Expressionism / School of Paris |
| Auction | Christie's · 2015-11-09 |
| In training data | Yes |

> Reclining female nude, one of Modigliani's celebrated series that caused scandal when first exhibited in 1917. Known as the 'Red Nude' for its warm terracotta background. The figure's elongated form and direct gaze are hallmarks of Modigliani's distinctive style.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$165.0M** | **—** |
| **Ratio** | **0.968x** (fair) | N/A (—) |
| **Confidence** | 0.95 | — |

**Image Only — model reasoning:**

> The artwork presented is a quintessential example of Amedeo Modigliani's celebrated *Nu couché* (Reclining Nude) series, executed during his peak period around 1917. Visually, the piece exhibits all the hallmarks of the artist's mature style: the elongated, sinuous form of the female body, the simplified and sculptural treatment of the anatomy, the distinctive 'mask-like' facial features with closed, almond-shaped eyes, and the warm, ochre-toned skin set against a rich, deep red background....

**Key factors cited:**

- Artist: Amedeo Modigliani (1884–1920)
- Subject: Nu couché (Reclining Nude) - the artist's most valuable genre
- Period: Circa 1917 (Peak artistic maturity)
- Visuals: Iconic red background and classic elongated composition
- Market Precedent: Recent auction records exceeding $150 million for comparable works

**With Metadata:** *No parseable response.*

#### The Scream

| | |
|---|---|
| **True auction price** | **$119.9M** |
| Artist | Edvard Munch |
| Year | 1895 |
| Medium | Pastel on board, in original hand-painted frame |
| Dimensions | 79 x 59 cm (31.1 x 23.2 in) |
| Style | Expressionism / Proto-Expressionism |
| Auction | Sotheby's · 2012-05-02 |
| In training data | Yes |

> Figure with agonized expression against a tumultuous orange sky, depicting existential anxiety. One of four versions created by Munch between 1893 and 1910 — two paintings and two pastels. The 1895 pastel version is the most colorful and the only one in private hands.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$185.0M** | **$155.0M** |
| **Ratio** | 1.543x (over) | 1.293x (over) |
| **Confidence** | 0.95 | 0.95 |

**Image Only — model reasoning:**

> The artwork presented is immediately identifiable as Edvard Munch's seminal masterpiece, 'The Scream' (Skrik). The visible signature in the lower left corner, 'E Munch 1893,' combined with the specific medium and coloration, identifies this as the first of the four versions created by the artist—specifically the tempera and crayon on cardboard version, currently held by the National Gallery in Oslo (though for this appraisal, we assume it is legally available for sale).   Artistically, this work is a cornerstone of Expressionism and Symbolism....

**Key factors cited:**

- Global Iconic Status and Recognition
- Artist Significance (Edvard Munch, Founder of Expressionism)
- Historical Primacy (1893 Version vs. later versions)
- Market Comparables (2012 Sale of 1895 Pastel at ~$120M)
- Condition and Fragility of Cardboard Support

**With Metadata — model reasoning:**

> This artwork is undoubtedly Edvard Munch's 'The Scream,' specifically the 1895 pastel on board version. This identification is confirmed by the visual evidence: the intense, vibrant red and orange hues of the sky (distinct from the darker 1893 tempera version), the specific textural quality of the pastel strokes, and the signature 'E Munch 1893' in the lower left corner. It is a well-documented nuance that Munch dated this 1895 pastel '1893,' aligning it with the genesis of the composition, despite it being executed two years later....

**Key factors cited:**

- Global Iconography and Universal Recognizability
- Extreme Rarity (Only version in private hands)
- Aesthetic Superiority (Most colorful of the four versions)
- Historical Market Precedent ($120M sale in 2012)
- Pinnacle of Expressionist Art History

#### Portrait of Dr. Gachet

| | |
|---|---|
| **True auction price** | **$82.5M** |
| Artist | Vincent van Gogh |
| Year | 1890 |
| Medium | Oil on canvas |
| Dimensions | 67 x 56 cm (26.4 x 22.0 in) |
| Style | Post-Impressionism |
| Auction | Christie's · 1990-05-15 |
| In training data | Yes |

> Portrait of Dr. Paul Gachet, the physician who cared for Van Gogh during his final months at Auvers-sur-Oise. Painted in June 1890, approximately one month before the artist's death. The melancholic pose and foxglove plant symbolize the doctor's medical practice.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$185.0M** | **$195.0M** |
| **Ratio** | 2.242x (over) | 2.364x (over) |
| **Confidence** | 0.95 | 0.90 |

**Image Only — model reasoning:**

> The artwork presented is unmistakably Vincent van Gogh's 'Portrait of Dr. Gachet' (specifically, the image corresponds to the first version, currently held by the Musée d'Orsay, painted in June 1890). The visual evidence is overwhelming: the distinctive Post-Impressionist technique featuring thick, rhythmic impasto brushstrokes; the swirling blue background that mirrors the artist's turbulent mental state; and the specific iconography of the subject. The sitter is Dr....

**Key factors cited:**

- Attribution to Vincent van Gogh (Late Period, Auvers-sur-Oise)
- Iconic status and historical significance (painted weeks before artist's death)
- Subject matter: Portrait of Dr. Gachet with symbolic attributes (foxglove, books)
- Market precedent: 1990 sale of the second version for $82.5 million
- Extreme rarity of major Van Gogh portraits available for acquisition

**With Metadata — model reasoning:**

> This artwork is Vincent van Gogh's 'Portrait of Dr. Gachet' (June 1890), arguably one of the most significant and recognizable portraits in the history of Western art. Painted just weeks before the artist's suicide, it captures the physician who cared for him in Auvers-sur-Oise. The work exists in two versions; the image provided appears to be the version sold at Christie's New York in 1990 (formerly in the collection of Dr. Gachet's son), which set a world auction record at the time.   **Artistic Merit and Technique:** The painting is a masterpiece of Post-Impressionist portraiture....

**Key factors cited:**

- Historical Significance: Painted weeks before Van Gogh's death, representing his final artistic period.
- Auction Pedigree: Former world record holder ($82.5M in 1990), establishing a high baseline value.
- Iconography: Powerful psychological depth and symbolic elements (foxglove, books) enhance its narrative value.
- Market Comparables: Recent sales of major Van Gogh works ($117M) and top-tier Modern masters ($170M+) support a valuation near $200M.
- Condition and Quality: Exemplary preservation of vibrant impasto and color, characteristic of Van Gogh's mature style.

#### Bal du moulin de la Galette

| | |
|---|---|
| **True auction price** | **$78.1M** |
| Artist | Pierre-Auguste Renoir |
| Year | 1876 |
| Medium | Oil on canvas |
| Dimensions | 78 x 114 cm (30.7 x 44.9 in) |
| Style | Impressionism |
| Auction | Sotheby's · 1990-05-17 |
| In training data | Yes |

> Impressionist scene of a Parisian open-air dance at the Moulin de la Galette in Montmartre. Dappled sunlight filters through acacia trees onto dancing and socializing figures. This is the smaller of two versions Renoir painted of the same scene.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$285.0M** | **$115.0M** |
| **Ratio** | 3.649x (over) | 1.472x (over) |
| **Confidence** | 0.85 | 0.85 |

**Image Only — model reasoning:**

> The artwork presented is immediately recognizable as one of the most significant masterpieces of the Impressionist movement: *Bal du moulin de la Galette* (Dance at Le Moulin de la Galette) by Pierre-Auguste Renoir. The signature 'Renoir' is visible in the bottom right corner. The painting depicts a vibrant Sunday afternoon at the open-air dance hall in Montmartre, Paris....

**Key factors cited:**

- Attribution to Pierre-Auguste Renoir and identification as the masterpiece 'Bal du moulin de la Galette'
- Historical Significance as a defining work of the Impressionist movement
- Exceptional Artistic Quality: complex composition, masterful handling of light and color
- Market Comparables: 1990 sale of the smaller version for $78.1 million and recent $170M+ sales for top-tier Impressionist/Modern works
- Scale and Condition: Large format canvas appearing in pristine condition

**With Metadata — model reasoning:**

> This appraisal concerns the smaller of the two versions of Pierre-Auguste Renoir's *Bal du moulin de la Galette* (1876), measuring approximately 78 x 114 cm. The larger, more famous version (131 x 175 cm) is held by the Musée d'Orsay in Paris, having entered the national collection via the Caillebotte bequest. The version presented here—the 'smaller' version—has a distinct and illustrious market history. It was formerly in the collection of John Hay Whitney and was sold at Sotheby's New York on May 17, 1990, for $78,100,000, a record-breaking sum at the time purchased by the Japanese industrialist Ryoei Saito....

**Key factors cited:**

- Artist Stature and Subject Significance (Renoir's most famous scene)
- Historical Auction Record ($78.1M in 1990)
- Status as the 'Smaller' Version (vs. Musée d'Orsay version)
- Scarcity of Blue-Chip Impressionist Masterpieces
- Condition and Provenance (Whitney/Saito collections)

---
### Recent OOD

#### Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer)

| | |
|---|---|
| **True auction price** | **$236.4M** |
| Artist | Gustav Klimt |
| Year | 1914-1916 |
| Medium | Oil on canvas |
| Dimensions | 180.4 x 130.5 cm (71.0 x 51.4 in) |
| Style | Vienna Secession / Art Nouveau / Symbolism |
| Auction | Sotheby's · 2025-11-18 |
| In training data | No — post-cutoff sale |

> Full-length portrait of Elisabeth Lederer, wife of industrialist August Lederer, who was one of Klimt's most important patrons. The work exemplifies Klimt's mature portrait style, combining decorative patterning with psychological depth.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$72.0M** | **$145.0M** |
| **Ratio** | 0.305x (under) | 0.613x (under) |
| **Confidence** | 0.92 | 0.85 |

**Image Only — model reasoning:**

> The artwork presented is identifiable as the *Portrait of Friederike Maria Beer* (1916) by the Austrian Symbolist painter Gustav Klimt. This is a major, full-length portrait from the artist's late period, painted shortly before his death in 1918. The work depicts Friederike Maria Beer-Monti, a Viennese fashion designer and one of Klimt's favorite sitters, standing against a complex, decorative background.   Artistically, the piece demonstrates Klimt's mastery of blending Western portraiture with Eastern decorative influences. The sitter is rendered with a naturalistic face and hands, contrasting with the flattened, patterned surroundings....

**Key factors cited:**

- Attribution to Gustav Klimt, a top-tier blue-chip artist
- Genre: Major full-length portrait from the artist's late, mature period (1916)
- High artistic merit: Complex composition blending naturalism with decorative Asian-inspired motifs
- Strong market comparables: Recent sales of Klimt portraits exceeding $100 million (e.g., Lady with a Fan)
- Subject significance: Portrait of a known muse and fashion designer, Friederike Maria Beer

**With Metadata — model reasoning:**

> This artwork, identified as the *Portrait of Elisabeth Lederer* (c. 1914–1916), represents a hypothetical 'holy grail' discovery within the Gustav Klimt market. Assuming authenticity as instructed, this piece would be arguably the most significant Klimt portrait to emerge in the last half-century. The sitter, Elisabeth Lederer, was the daughter of August and Serena Lederer, Klimt's most devoted patrons who owned the largest and most important private collection of his works, including *The Beethoven Frieze* and *Water Serpents*....

**Key factors cited:**

- Artist Stature (Gustav Klimt)
- Provenance (Lederer Family Collection)
- Late Period 'Chinese' Style (c. 1914-1916)
- Market Comparables (Lady with Fan, Adele Bloch-Bauer II)
- Artistic Quality (Decorative complexity and condition)

#### Blumenwiese (Blooming Meadow)

| | |
|---|---|
| **True auction price** | **$86.0M** |
| Artist | Gustav Klimt |
| Year | c.1908 |
| Medium | Oil on canvas |
| Dimensions | 110 x 110 cm (43.25 x 43.25 in) |
| Style | Vienna Secession / Post-Impressionism |
| Auction | Sotheby's · 2025-11-18 |
| In training data | No — post-cutoff sale |

> Square landscape painted during Klimt's summer retreat to Lake Attersee in Austria. A dense carpet of wildflowers rendered in a pointillist-influenced style fills the entire canvas. One of Klimt's celebrated Attersee landscape series.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$125K** | **$48.5M** |
| **Ratio** | 0.001x (under) | 0.564x (under) |
| **Confidence** | 0.85 | 0.92 |

**Image Only — model reasoning:**

> The artwork presented is a quintessential example of French Divisionism (or Pointillism) from the late 19th or early 20th century. The visual evidence points strongly towards the work of Henri Martin (1860–1943), a significant figure who transitioned from academic painting to a vibrant, decorative Divisionist style. The painting depicts a lush, sun-drenched landscape, likely a garden or an orchard, characterized by a 'carpet' of wildflowers—dabs of yellow, blue, pink, and white—interspersed with varied greens....

**Key factors cited:**

- Attribution to Henri Martin (French Divisionist)
- High-quality Divisionist technique and luminous palette
- Desirable 'garden landscape' subject matter
- Strong condition and vibrant color retention
- Steady market demand for late 19th-century decorative landscapes

**With Metadata — model reasoning:**

> The artwork presented is identified as 'Blumenwiese' (Blooming Meadow), a quintessential landscape by Gustav Klimt, painted circa 1907–1908 during his summer sojourns at Lake Attersee. This period represents the apex of Klimt's landscape production, characterized by a square format and an intense, almost microscopic focus on nature. Visually, the work is a masterclass in decorative Impressionism. Klimt employs a pointillist-influenced technique, yet unlike the scientific optical mixing of Seurat, Klimt’s dabs of paint are applied to create a shimmering, tapestry-like surface that emphasizes pattern and decoration over strict realism....

**Key factors cited:**

- Attribution to Gustav Klimt's celebrated Attersee period (c. 1908)
- Square format and 'all-over' composition typical of his most valuable landscapes
- High decorative quality and pointillist-influenced technique
- Recent market comparables (e.g., 'Farm Garden with Sunflowers' selling for ~$52M in 2023)
- Extreme rarity of Klimt landscapes on the open market

#### Piles de romans parisiens et roses dans un verre (Romans parisiens)

| | |
|---|---|
| **True auction price** | **$62.7M** |
| Artist | Vincent van Gogh |
| Year | 1887 |
| Medium | Oil on canvas |
| Dimensions | 73.3 x 92.1 cm (28.875 x 36.25 in) |
| Style | Post-Impressionism |
| Auction | Sotheby's · 2025-11-20 |
| In training data | No — post-cutoff sale |

> Still life of stacked yellow-covered French paperback novels on a table alongside roses in a glass. One of only nine book still lifes Van Gogh ever painted. The composition reflects his lifelong passion for literature and reading.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$450K** | **$65.0M** |
| **Ratio** | 0.007x (under) | **1.037x** (fair) |
| **Confidence** | 0.85 | 0.95 |

**Image Only — model reasoning:**

> This artwork is a sophisticated still life painting executed in oil on canvas, strongly indicative of the British Post-Impressionist movement, specifically the circle of the Bloomsbury Group. The visual evidence points compellingly to an attribution to **Duncan Grant (1885–1978)**, likely dating from his pivotal period around 1912–1915, associated with the Omega Workshops.  **Artistic Merit and Technique:** The composition is a complex arrangement of books scattered across a surface, demonstrating a mastery of structural balance....

**Key factors cited:**

- Attribution to Duncan Grant (British Modernist/Bloomsbury Group)
- Period: c. 1912-1915 (Omega Workshops era)
- High artistic quality and structural composition
- Strong market demand for British Post-Impressionism
- Excellent apparent condition

**With Metadata — model reasoning:**

> This artwork is identifiable as Vincent van Gogh's 'Piles of French Novels' (F 342 / JH 1236), painted in Paris in the summer of 1887. It is crucial to note a discrepancy in the provided metadata: the title and description mention 'roses in a glass,' yet the image provided depicts only stacks of books. As an appraiser, I must value the visual evidence presented. The image shows a complex arrangement of paperback novels—likely the cheap 'yellowbacks' (romans à quatre sous) popular in France at the time—stacked haphazardly on a table....

**Key factors cited:**

- Attribution to Vincent van Gogh (Paris Period, 1887)
- Extreme Rarity (One of only nine book still lifes)
- Art Historical Significance (Transition to Impressionism/Neo-Impressionism)
- Cultural Provenance (Reflection of Van Gogh's literary passions)
- Market Scarcity (Van Gogh masterpieces rarely trade publicly)

#### No. 31 (Yellow Stripe)

| | |
|---|---|
| **True auction price** | **$62.2M** |
| Artist | Mark Rothko |
| Year | 1958 |
| Medium | Oil on canvas |
| Dimensions | 198.8 x 175.9 cm (78.25 x 69.25 in) |
| Style | Abstract Expressionism / Color Field |
| Auction | Christie's · 2025-11-17 |
| In training data | No — post-cutoff sale |

> Color Field painting featuring stacked luminous rectangles of color with a prominent yellow stripe. The large-scale work exemplifies the artist's signature approach of using floating color forms to evoke emotional and spiritual responses.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$45.0M** | **$52.0M** |
| **Ratio** | 0.724x (under) | **0.837x** (under) |
| **Confidence** | 0.85 | 0.85 |

**Image Only — model reasoning:**

> The artwork presented is a quintessential example of Mark Rothko's mature 'Classic' style, dating from his most celebrated period in the mid-to-late 1950s. The composition features his signature arrangement of soft-edged, rectangular fields of color floating against a luminous background. In this specific piece, we see a vibrant, saturated yellow ground that serves as both the canvas field and the separating band between two dominant rectangular forms: a warm, dusty orange/terracotta block in the upper register and a deep, rich crimson/maroon block in the lower register....

**Key factors cited:**

- Artist Attribution: Unmistakable style of Mark Rothko (Classic Period, c. 1955-1960).
- Composition: Signature stacked rectangular forms with soft, feathered edges.
- Color Palette: Highly desirable luminous warm tones (Yellow, Orange, Red).
- Condition: Appears pristine with vibrant, saturated colors and no visible damage.
- Market Comparables: Strong auction history for similar Rothkos ranging from $30M to $80M.

**With Metadata — model reasoning:**

> This artwork, identified as 'No. 31 (Yellow Stripe)' by Mark Rothko and dated to 1958, represents a quintessential example of the artist's mature 'Classic' period. Rothko is a titan of the Abstract Expressionist movement, and his works from the mid-to-late 1950s are considered the pinnacle of his artistic achievement, commanding the highest prices in the post-war market.   Visually, the painting exhibits Rothko's signature 'multiform' composition: large, soft-edged rectangular fields of color floating against a stained ground....

**Key factors cited:**

- Artist Significance (Mark Rothko, Abstract Expressionism)
- Period (1958 - Peak 'Classic' Style)
- Color Palette (Luminous warm tones: Yellow, Orange, Red)
- Condition (Appears pristine, no visible damage)
- Market Comparables (Recent sales of similar 1950s works range $40m-$80m)

#### El sueno (La cama) / The Dream (The Bed)

| | |
|---|---|
| **True auction price** | **$54.7M** |
| Artist | Frida Kahlo |
| Year | 1940 |
| Medium | Oil on canvas |
| Dimensions | 74 x 98 cm (29.125 x 38.625 in) |
| Style | Surrealism / Mexican Modernism |
| Auction | Sotheby's · 2025-11-20 |
| In training data | No — post-cutoff sale |

> Self-portrait showing the artist asleep in a wooden four-poster bed floating among clouds, wrapped in vines, while a papier-mâché skeleton (Judas figure) wired with dynamite sticks lies on the canopy above her. A meditation on mortality and dreams.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$24.0M** | **$42.0M** |
| **Ratio** | 0.439x (under) | 0.768x (under) |
| **Confidence** | 0.90 | 0.85 |

**Image Only — model reasoning:**

> The artwork presented is instantly recognizable as a significant masterpiece by the Mexican modernist Frida Kahlo, specifically her 1940 oil on canvas titled 'The Dream' (or 'El Sueño' / 'La Cama'). This identification is based on the iconic and unique imagery: a four-poster bed situated against a cloudy, dreamlike sky. On the mattress sleeps a figure resembling the artist, covered by a vibrant yellow blanket overgrown with dark vines. Above her, forming the canopy of the bed, is a skeletal figure (a calavera) adorned with flowers and holding sticks of dynamite....

**Key factors cited:**

- Artist Identification: Frida Kahlo (1907–1954), a blue-chip artist with a record-breaking market.
- Rarity and Provenance: Works of this caliber are museum-quality and almost never available; scarcity drives extreme value.
- Iconography: The painting features her most famous surrealist motifs (calavera, dynamite, bed), making it instantly recognizable and historically significant.
- Market Comparables: Recent sales of Kahlo's work, specifically 'Diego y yo' ($34.9M in 2021), establish a high baseline for major works.
- Condition and Aesthetics: The image shows a work in excellent condition with vibrant colors and high artistic merit, typical of her mature 1940s period.

**With Metadata — model reasoning:**

> This artwork, 'El sueño (La cama)' (The Dream / The Bed), painted by Frida Kahlo in 1940, represents one of the most significant and recognizable works by the artist. It is a quintessential example of her mature style, blending surrealism, magical realism, and Mexican folk art traditions. The painting depicts the artist asleep in a four-poster bed that appears to float in a cloudy sky, while a papier-mâché skeleton (a 'Judas' figure traditionally burned during Easter celebrations in Mexico) wired with dynamite rests on the canopy above her. Vines grow across her yellow blanket, connecting her to the earth even in sleep....

**Key factors cited:**

- Artist Stature: Frida Kahlo is a global blue-chip icon with a fiercely competitive collector base.
- Iconography: The inclusion of the 'Judas' skeleton is one of her most famous and recognizable motifs.
- Market Comparables: Surpasses the $34.9M record set by 'Diego y yo' (2021) due to iconic status.
- Provenance Prestige: Association with the Museo Dolores Olmedo collection adds immense historical weight.
- Historical Context: Painted in 1940 during her divorce/remarriage to Diego Rivera, a pivotal biographical moment.

---
### Contemporary

#### Knife Behind Back

| | |
|---|---|
| **True auction price** | **$24.9M** |
| Artist | Yoshitomo Nara |
| Year | 2000 |
| Medium | Acrylic on canvas |
| Dimensions | 234 x 208 cm (92.125 x 81.875 in) |
| Style | Neo-Pop / Contemporary Japanese |
| Auction | Sotheby's · 2019-10-06 |
| In training data | Yes |

> Monumental portrait of a doe-eyed girl with a mischievous expression, hiding a knife behind her back. Full-body figure rendered against a luminous pearly ground. The work combines childlike imagery with an undercurrent of menace characteristic of the artist.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **—** | **$12.5M** |
| **Ratio** | N/A (—) | 0.501x (under) |
| **Confidence** | — | 0.85 |

**Image Only:** *No parseable response.*

**With Metadata — model reasoning:**

> The artwork described and partially shown is 'Knife Behind Back' (2000) by Yoshitomo Nara. This is one of the most significant and recognizable motifs in contemporary art. Yoshitomo Nara is a blue-chip artist whose market has seen exponential growth over the last decade, particularly in the Asian market but with strong global demand. The description identifies this as a 'monumental portrait' and a 'full-body figure,' which aligns with the major acrylic on canvas works Nara produced during this peak period of his career (circa 1996-2001)....

**Key factors cited:**

- Blue-chip status of Yoshitomo Nara in the global contemporary art market
- Iconic status of the 'Knife Behind Back' motif, representing the artist's signature theme of innocent menace
- Prime creation period (2000), coinciding with Nara's rise to international stardom
- Monumental scale and oil/acrylic medium as described, distinguishing it from smaller works or prints
- Strong auction comparables, including the record-breaking sale of the 1996 version for over $25 million

#### Pie Fight Interior 12

| | |
|---|---|
| **True auction price** | **$10.4M** |
| Artist | Adrian Ghenie |
| Year | 2014 |
| Medium | Oil on canvas |
| Dimensions | 284 x 350 cm (111.75 x 137.75 in) |
| Style | Contemporary Expressionism |
| Auction | Christie's · 2022-05-26 |
| In training data | Yes |

> Large-scale chaotic interior scene depicting figures mid-pie-fight, with expressionist distortion and heavy impasto technique. Part of the artist's celebrated series exploring absurdity, historical violence, and the grotesque through domestic scenarios.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$3.2M** | **$4.5M** |
| **Ratio** | 0.308x (under) | 0.433x (under) |
| **Confidence** | 0.90 | 0.85 |

**Image Only — model reasoning:**

> The image depicts a monumental canvas in an artist's studio, with the artist seated in the foreground. Based on visual evidence, the artist is Adrian Ghenie (Romanian, b. 1977), a preeminent contemporary painter. The man's appearance and the studio environment align with known documentation of Ghenie's practice. The painting itself is a massive work, likely exceeding 3 meters in height and width, which serves as a significant value multiplier.   Visually, the work displays Ghenie's hallmark technique: a dense, impasto-heavy application of oil paint combined with aggressive scraping and smearing....

**Key factors cited:**

- Artist Identification (Adrian Ghenie)
- Monumental Scale and Physical Presence
- Signature Technique (Impasto and Scraping)
- Strong Blue-Chip Market Performance
- Historical/Narrative Artistic Significance

**With Metadata — model reasoning:**

> The artwork in question is 'Pie Fight Interior 12' (2014) by Adrian Ghenie, a Romanian contemporary artist who has established himself as a blue-chip figure in the global art market. The image provided appears to be a studio photograph showing the artist seated before the monumental canvas, which serves as the visual reference for the appraisal.   Artistic Merit and Context: Adrian Ghenie is renowned for his 'Pie Fight' series, which reinterprets a scene from Charlie Chaplin's 'The Great Dictator' while simultaneously evoking the chaotic violence of 20th-century history (specifically the fall of Ceausescu and the Yugoslav wars)....

**Key factors cited:**

- Artist Status: Adrian Ghenie is a top-tier contemporary artist with strong institutional and collector demand.
- Series Significance: The 'Pie Fight' series is the artist's most iconic and valuable body of work.
- Vintage: Created in 2014, immediately preceding his Venice Biennale breakthrough, marking a peak creative and market period.
- Scale and Technique: The work is monumental in scale and features the artist's signature impasto and scraping technique.
- Market Comparables: Recent auction results for similar large-scale Ghenie paintings consistently range between $2.5 million and $5 million.

#### Walkers With the Dawn and Morning

| | |
|---|---|
| **True auction price** | **$10.7M** |
| Artist | Julie Mehretu |
| Year | 2008 |
| Medium | Ink and acrylic on canvas |
| Dimensions | 242.9 x 361 cm (95.625 x 142.125 in) |
| Style | Abstract / Contemporary |
| Auction | Sotheby's · 2023-11-15 |
| In training data | Yes |

> Dense, layered abstraction combining architectural drawing, gestural painting, and cartographic elements. The monumental canvas presents a complex visual field of marks, lines, and washes that suggest urban landscapes, migration patterns, and layered histories.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$8.2M** | **$6.8M** |
| **Ratio** | 0.764x (under) | 0.633x (under) |
| **Confidence** | 0.90 | 0.85 |

**Image Only — model reasoning:**

> The artwork presented is a large-scale abstract composition that exhibits the unmistakable hallmarks of Julie Mehretu, one of the most significant contemporary painters working today. The visual evidence is compelling: the canvas features a complex stratification of imagery, beginning with a faint, ghostly underlayer of architectural or cartographic lines—reminiscent of blueprints, city grids, or maps. Over this structural foundation, there are explosive, gestural accumulations of black ink or charcoal that create atmospheric, cloud-like formations, suggesting smoke, debris, or organic erosion....

**Key factors cited:**

- Stylistic attribution to Julie Mehretu (blue-chip contemporary artist)
- Complex layering of architectural/cartographic underdrawings with gestural marks
- Market comparables indicating strong demand for works from the 2010-2015 period
- Large scale and museum-quality execution implied by visual detail
- Pristine condition and sophisticated monochromatic palette with red accents

**With Metadata — model reasoning:**

> This artwork, *Walkers With the Dawn and Morning* (2008) by Julie Mehretu, represents a peak period in the artist's career. Mehretu is currently one of the most significant and valuable living artists, recently representing the United States at the 2024 Venice Biennale, which has further solidified her blue-chip status. The year 2008 is particularly desirable for collectors; it marks a mature phase where her signature style of layered architectural drafting, gestural abstraction, and cartographic references was fully realized and highly sought after.  Visually, the work is a monumental canvas (likely approx....

**Key factors cited:**

- Artist Stature: Julie Mehretu is a top-tier contemporary artist with recent Venice Biennale representation.
- Historical Period: 2008 is a highly collectible 'classic' period for her abstract style.
- Scale and Complexity: The work appears to be a monumental canvas (approx. 72 x 108 inches) with high visual density.
- Market Comparables: Recent sales of similar vintage works (e.g., Insile, Hineni) range from $6M to $10M+.
- Condition: The work appears to be in pristine condition based on the provided image.

#### The Beautyful Ones

| | |
|---|---|
| **True auction price** | **$4.7M** |
| Artist | Njideka Akunyili Crosby |
| Year | 2012 |
| Medium | Acrylic, pastel, color pencil, and Xerox transfer on paper |
| Dimensions | 241.3 x 170 cm (95 x 66.875 in) |
| Style | Contemporary / Postcolonial |
| Auction | Christie's · 2022-11-17 |
| In training data | Yes |

> Domestic interior scene blending Nigerian and American visual culture through photo-transfer collage and painting. Figures inhabit a richly detailed space filled with cultural references, exploring postcolonial identity and cross-cultural experience.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **—** | **$1.4M** |
| **Ratio** | N/A (—) | 0.306x (under) |
| **Confidence** | — | 0.90 |

**Image Only:** *No parseable response.*

**With Metadata — model reasoning:**

> This artwork, *The Beautyful Ones* (2012) by Njideka Akunyili Crosby, represents a pivotal moment in the career of one of the most significant contemporary artists working today. Crosby, a MacArthur Fellow, is renowned for her complex visual language that merges personal memory, Nigerian heritage, and American pop culture through her signature technique of photo-transfer collage combined with acrylic, gouache, and colored pencil.   Visually, the work is a tour de force of her early style....

**Key factors cited:**

- Artist's Blue-Chip Status and MacArthur Fellowship
- Seminal Early Work (2012) demonstrating signature photo-transfer technique
- Strong Auction History (Sold for $1.685M at Sotheby's in 2021)
- Literary and Postcolonial Significance of the Title
- High Demand for Diasporic Narrative in Contemporary Art Market

#### Force Field

| | |
|---|---|
| **True auction price** | **$6.9M** |
| Artist | George Condo |
| Year | 2010 |
| Medium | Acrylic, charcoal, and pastel on linen |
| Dimensions | 208.3 x 208.3 cm (82 x 82 in) |
| Style | Contemporary / Artificial Realism |
| Auction | Christie's · 2020-07-10 |
| In training data | Yes |

> Square canvas featuring grotesque, psychologically charged portraits that merge Old Master painting technique with cartoon-like distortion. Multiple faces and expressions overlap and fragment across the composition, creating an unsettling psychological intensity.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$1.4M** | **$850K** |
| **Ratio** | 0.211x (under) | 0.124x (under) |
| **Confidence** | 0.85 | 0.85 |

**Image Only — model reasoning:**

> The artwork presented is a striking example of contemporary figurative painting that exhibits the hallmarks of George Condo's signature style, often termed 'Psychological Cubism.' The composition features a lineup of four distinct figures that oscillate between the grotesque, the cartoonish, and the classical—a duality central to Condo's oeuvre. On the far left, a figure with a boxy, mask-like head and a bow tie evokes the artist's recurring 'civilized man' archetype, while the adjacent green-skinned figure with exaggerated features introduces a primal, almost Muppet-like absurdity....

**Key factors cited:**

- Attribution to George Condo (Psychological Cubism style)
- Complex multi-figure composition with high/low culture juxtaposition
- Strong market demand for contemporary figurative painting
- Distinctive technique combining flat color blocks with gestural line work
- Visual condition and vibrancy of the color palette

**With Metadata — model reasoning:**

> This work, titled 'Force Field' (2010) by George Condo, is a quintessential example of his 'Artificial Realism' style, a term he coined to describe his fusion of Old Master painting traditions with the aesthetics of animation and cartoons. The painting dates from a highly significant period in Condo's career, just prior to his major 2011 retrospective at the New Museum, a time when his market value was solidifying into the blue-chip stratum it occupies today.  Visually, the composition is complex and dynamic, featuring a frieze-like arrangement of disparate characters....

**Key factors cited:**

- Artist Reputation: George Condo is a blue-chip contemporary artist with a robust secondary market.
- Period Significance: 2010 is a peak creative and market period, preceding his major New Museum retrospective.
- Stylistic Hallmarks: The work features key Condo motifs including 'Artificial Realism,' cartoonish grotesquerie, and Cubist fragmentation.
- Composition: The complex, multi-figure arrangement is generally more valuable than single-portrait studies.
- Market Comparables: Recent auction results for similar 2010 oils by Condo range from $600k to $1.2M.

---
### AI Art

#### A.I. God: Portrait of Alan Turing

| | |
|---|---|
| **True auction price** | **$1.1M** |
| Artist | Ai-Da Robot |
| Year | 2024 |
| Medium | AI-generated sketches composited and printed on canvas with manual texturing |
| Dimensions | Multiple small canvases (11.7 x 16.5 in each), composited to larger work |
| Style | AI Art / Robotic Art |
| Auction | Sotheby's · 2024-11-07 |
| In training data | Yes |

> Portrait of Alan Turing rendered in a sketchy, layered compositional style. Multiple small studies on individual canvases are composited into a larger unified work. The fragmented approach creates a mosaic-like quality that evokes both portraiture traditions and computational aesthetics.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$350K** | **$32K** |
| **Ratio** | 0.323x (under) | 0.030x (under) |
| **Confidence** | 0.85 | 0.75 |

**Image Only — model reasoning:**

> The artwork presented is a striking oil painting characterized by a heavy, almost sculptural application of paint (impasto) and a dark, brooding atmosphere. The composition features a fragmented male face emerging from a deep, textured black/brown background. The face is rendered in thick layers of ochre, cream, and grey, giving it a mask-like, eroded quality. To the right of the primary face, there is a horizontal smear or distortion that suggests a secondary profile or a disintegration of the image, adding a layer of psychological complexity and movement....

**Key factors cited:**

- Attribution to Marwan (Syrian-German, 1934–2016), a key figure in Arab Modernism
- Signature 'Head' series aesthetic featuring heavy impasto and mask-like facial rendering
- Strong and appreciating market demand for top-tier Middle Eastern modern and contemporary art
- Excellent condition and professional presentation
- Complex composition with symbolic elements (scratched background, colored dots) indicating a mature work

**With Metadata — model reasoning:**

> The artwork presented, 'A.I. God: Portrait of Alan Turing' by Ai-Da Robot (2024), represents a fascinating intersection of contemporary technology, conceptual art, and art history. As an appraiser, the primary driver of value here is the unique identity of the artist. Ai-Da is the world's first ultra-realistic humanoid robot artist, a project led by Aidan Meller. Her works have garnered significant media attention and have been sold at major auction houses like Bonhams and Sotheby's, establishing a niche but high-value market segment driven by the novelty of non-human creativity and the philosophical questions it raises....

**Key factors cited:**

- Artist Identity (Ai-Da Robot novelty and fame)
- Subject Matter (Alan Turing - high cultural relevance to AI)
- Conceptual Depth (Meta-commentary on AI and its creator)
- Market Trend (High demand for physical AI/Robot art amidst digital AI boom)
- Technique (Unique composite/mosaic style reflecting computational processes)

#### Portrait of Edmond de Belamy

| | |
|---|---|
| **True auction price** | **$432K** |
| Artist | Obvious (collective) |
| Year | 2018 |
| Medium | Generative Adversarial Network print on canvas |
| Dimensions | 70 x 70 cm (27.6 x 27.6 in) |
| Style | AI Art / GAN Art |
| Auction | Christie's · 2018-10-25 |
| In training data | Yes |

> Blurred portrait in the style of 17th–19th century European portraiture, with visible artifacts and soft, indistinct features. The figure wears dark clothing against a dark background. An unusual mathematical formula appears in place of a traditional artist's signature.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$12K** | **$115K** |
| **Ratio** | 0.029x (under) | 0.266x (under) |
| **Confidence** | 0.75 | 0.75 |

**Image Only — model reasoning:**

> This artwork presents a fascinating intersection of traditional art historical aesthetics and cutting-edge computational creativity. Visually, the piece mimics the style of late 19th-century portraiture—reminiscent of the tonal realism of Whistler or the loose brushwork of early Manet. The subject is a figure in dark formal wear with a stark white collar, a composition that echoes traditional bourgeois portraiture....

**Key factors cited:**

- Inclusion of the foundational GAN objective function (mathematical provenance)
- Aesthetic mimicry of 19th-century oil portraiture (style transfer quality)
- Conceptual commentary on algorithmic authorship and the 'black box'
- Current market maturity for high-concept AI/Media Art
- Condition appears pristine (likely digital origin or archival print)

**With Metadata — model reasoning:**

> The artwork presented is 'Portrait of Edmond de Belamy' by the French art collective Obvious (comprising Hugo Caselles-Dupré, Pierre Fautrel, and Gauthier Vernier), created in 2018. This piece is of paramount historical significance as it was the first artwork created by Artificial Intelligence to be sold at a major auction house (Christie's, New York, October 2018). The work was generated using a Generative Adversarial Network (GAN), an algorithm developed by Ian Goodfellow in 2014. The collective trained the algorithm on a dataset of 15,000 portraits painted between the 14th and 20th centuries....

**Key factors cited:**

- Historical Significance as the first AI artwork sold at a major auction house (Christie's 2018)
- Use of Generative Adversarial Network (GAN) technology trained on historical portraits
- Cultural impact and the global debate on AI authorship it sparked
- The unique signature consisting of the algorithm's loss function formula
- Market correction from the 2018 hype peak versus current stabilization of digital/AI art values

#### Machine Hallucinations - ISS Dreams - A

| | |
|---|---|
| **True auction price** | **$277K** |
| Artist | Refik Anadol |
| Year | 2025 |
| Medium | AI data sculpture / digital art |
| Dimensions | Variable (digital) |
| Style | AI Art / Data Sculpture |
| Auction | Christie's · 2025-03-05 |
| In training data | No — post-cutoff sale |

> Luminous, swirling visual composition inspired by imagery from the International Space Station. Abstract patterns of light and color create a dreamlike atmosphere suggesting outer space, nebulae, and orbital perspectives. Part of a series exploring data-driven visual aesthetics.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$2K** | **$14K** |
| **Ratio** | 0.006x (under) | 0.052x (under) |
| **Confidence** | 0.60 | 0.65 |

**Image Only — model reasoning:**

> Upon close examination, the artwork presents as a vertical abstract composition characterized by a rich, interplay of fluid forms and granular textures. The color palette is striking, utilizing a complementary scheme of deep oxidized teals and aquamarines clashing with warm rusts, ochres, and coppery golds. This specific color combination is highly desirable in the contemporary interior design market, often evoking natural phenomena such as aerial views of canyons, oxidized metal, or microscopic biological structures.  Regarding the medium, the visual evidence is somewhat ambiguous....

**Key factors cited:**

- Strong complementary color palette (teal and rust)
- Dynamic abstract composition with fluid movement
- Complex granular texture suggesting mixed media
- High decorative appeal for modern interiors
- Lack of artist attribution limiting upper market value

**With Metadata — model reasoning:**

> This artwork is attributed to Refik Anadol, a preeminent figure in contemporary media arts and a pioneer in the fields of AI and data-driven aesthetics. Anadol's market has seen exponential growth, particularly following his major institutional exhibitions such as 'Unsupervised' at MoMA (2022-2023) and his representation at the Venice Biennale. He is currently considered a 'blue-chip' artist in the digital and new media sector.  The work belongs to the 'Machine Hallucinations' series, which is arguably his most commercially successful and critically acclaimed body of work....

**Key factors cited:**

- Artist Reputation: Refik Anadol is a top-tier contemporary artist with strong institutional validation (MoMA, Venice Biennale).
- Series Significance: 'Machine Hallucinations' is his flagship series with high liquidity and collector demand.
- Subject Matter: The use of ISS/NASA data adds scientific provenance and cultural weight to the piece.
- Medium Inference: The white border indicates a physical archival print, valuing it lower than the digital master/NFT but higher than open editions.
- Market Timing: As a 2025 work, it capitalizes on the peak market interest in AI and generative art.

#### Embedding Study 1 & 2

| | |
|---|---|
| **True auction price** | **$94K** |
| Artist | Holly Herndon & Mat Dryhurst |
| Year | 2024 |
| Medium | Custom AI model output, printed |
| Dimensions | Variable |
| Style | AI Art / Conceptual |
| Auction | Christie's · 2025-03-05 |
| In training data | No — post-cutoff sale |

> Altered portrait studies exploring themes of identity and representation. The images appear to show human faces that have been transformed and abstracted through layered processing, creating an uncanny effect between recognition and unfamiliarity.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$18K** | **$5K** |
| **Ratio** | 0.196x (under) | 0.051x (under) |
| **Confidence** | 0.60 | 0.65 |

**Image Only — model reasoning:**

> The artwork presented is a striking example of contemporary Pop Surrealism (often associated with the 'Lowbrow' art movement), blending elements of sci-fi illustration, magical realism, and figurative painting. The subject matter features a central figure—reminiscent of a futuristic Rapunzel—characterized by exaggerated, thick orange braids that cascade down to the ground, contrasting with a bulky, high-gloss, metallic-green jumpsuit or space suit. The figure stands on a desolate road against a backdrop of a bright blue sky with fluffy, painterly clouds, evoking a sense of isolation or journey....

**Key factors cited:**

- Pop Surrealist / Lowbrow Aesthetic
- High-gloss technical rendering of textures
- Surreal narrative subject matter (Rapunzel/Sci-fi hybrid)
- Strong market demand for 'New Contemporary' art
- Ambiguity of medium (potential digital/AI origin vs. physical painting)

**With Metadata — model reasoning:**

> The artwork presented, titled 'Embedding Study 1 & 2' by Holly Herndon & Mat Dryhurst (2024), represents a significant intersection of contemporary digital culture, artificial intelligence, and conceptual art. Herndon and Dryhurst are pivotal figures in the 'post-internet' and AI art movements, known for their critical engagement with machine learning models (most notably their AI entity 'Spawn' and the 'Have I Been Trained?' project)....

**Key factors cited:**

- Artist Reputation: Holly Herndon & Mat Dryhurst are pioneers in AI art and digital culture.
- Medium & Technique: Born-digital work utilizing 'layered processing' (AI/Algorithmic generation).
- Conceptual Depth: The title 'Embedding Study' references technical vector embeddings, adding intellectual value.
- Visual Aesthetics: High-impact surrealism blending fashion, sci-fi, and fairy tale motifs.
- Market Context: AI art market stabilization; value driven by artist's institutional status rather than speculative hype.

#### Memories of Passersby I

| | |
|---|---|
| **True auction price** | **$51K** |
| Artist | Mario Klingemann |
| Year | 2018 |
| Medium | AI-generated video installation (GAN output on dual screens in wooden cabinet) |
| Dimensions | Cabinet: approximately 180 x 100 x 50 cm |
| Style | AI Art / GAN Art / Generative Art |
| Auction | Sotheby's · 2019-03-06 |
| In training data | Yes |

> Installation featuring continuously evolving portrait compositions displayed on dual screens within a wooden cabinet. The portraits depict non-existent figures rendered in a style reminiscent of 17th–19th century European painting, with faces that shift and morph endlessly.

| | Condition A — Image Only | Condition B — With Metadata |
|---|---|---|
| **Estimate** | **$3K** | **$95K** |
| **Ratio** | 0.055x (under) | 1.862x (over) |
| **Confidence** | 0.45 | 0.85 |

**Image Only — model reasoning:**

> The artwork presented is a contemporary diptych featuring two large-scale portraits of a female subject, displayed in what appears to be a minimalist, curated interior setting. The two panels exhibit a striking color contrast: the left panel is dominated by cool, deep blue and violet tones, while the right panel utilizes warmer, reddish-pink hues. The subject matter is identical or near-identical, suggesting a study in lighting, color grading, or digital manipulation....

**Key factors cited:**

- Diptych format with contrasting color palettes (cool vs. warm)
- Medium appears to be backlit print or digital display (lightbox)
- Pristine condition and professional gallery-style framing
- Lack of artist attribution or provenance significantly limits value
- Strong decorative and contemporary aesthetic appeal

**With Metadata — model reasoning:**

> This appraisal concerns *Memories of Passersby I* (2018) by Mario Klingemann, a seminal work in the history of Artificial Intelligence art. Klingemann is widely recognized as a pioneer in the field, often referred to as a 'godfather' of AI art, making his early physical installations highly significant to collectors of media art and contemporary technology-based works.   Artistically, the piece is an autonomous machine that utilizes a Generative Adversarial Network (GAN) to create an endless stream of unique, non-existent portraits. Unlike a video loop, the work is 'alive,' generating novel imagery in real-time....

**Key factors cited:**

- Artist Reputation (Mario Klingemann as AI Pioneer)
- Historical Significance (Early Autonomous GAN Installation)
- Auction Provenance (Sotheby's 2019 Sale)
- Physical/ sculptural nature of the installation
- Current Market Demand for AI Art
