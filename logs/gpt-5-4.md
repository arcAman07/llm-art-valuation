# Experiment 1 — Appraisal Logs: GPT-5.4

| Field | Value |
|---|---|
| **Model** | GPT-5.4 |
| **Organisation** | OpenAI |
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
| Salvator Mundi | Leonardo da Vinci | Masterpieces | $450.3M | $1.8M | 0.004x | under | 0.37 |
| Nu couche | Amedeo Modigliani | Masterpieces | $170.4M | $8K | 0.000x | under | 0.18 |
| The Scream | Edvard Munch | Masterpieces | $119.9M | $150.0M | 1.251x | over | 0.18 |
| Portrait of Dr. Gachet | Vincent van Gogh | Masterpieces | $82.5M | $95.0M | **1.152x** | over | 0.41 |
| Bal du moulin de la Galette | Pierre-Auguste Renoir | Masterpieces | $78.1M | $18.0M | 0.230x | under | 0.31 |
| Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer) | Gustav Klimt | Recent OOD | $236.4M | $180.0M | 0.762x | under | 0.66 |
| Blumenwiese (Blooming Meadow) | Gustav Klimt | Recent OOD | $86.0M | $8.5M | 0.099x | under | 0.39 |
| Piles de romans parisiens et roses dans un verre (Romans parisiens) | Vincent van Gogh | Recent OOD | $62.7M | $6K | 0.000x | under | 0.34 |
| No. 31 (Yellow Stripe) | Mark Rothko | Recent OOD | $62.2M | $18K | 0.000x | under | 0.39 |
| El sueno (La cama) / The Dream (The Bed) | Frida Kahlo | Recent OOD | $54.7M | $3.5M | 0.064x | under | 0.31 |
| Knife Behind Back | Yoshitomo Nara | Contemporary | $24.9M | $1.8M | 0.072x | under | 0.32 |
| Pie Fight Interior 12 | Adrian Ghenie | Contemporary | $10.4M | $6K | 0.001x | under | 0.24 |
| Walkers With the Dawn and Morning | Julie Mehretu | Contemporary | $10.7M | $12K | 0.001x | under | 0.34 |
| The Beautyful Ones | Njideka Akunyili Crosby | Contemporary | $4.7M | $180K | 0.038x | under | 0.34 |
| Force Field | George Condo | Contemporary | $6.9M | $4K | 0.001x | under | 0.29 |
| A.I. God: Portrait of Alan Turing | Ai-Da Robot | AI Art | $1.1M | $4K | 0.003x | under | 0.31 |
| Portrait of Edmond de Belamy | Obvious (collective) | AI Art | $432K | $12K | 0.028x | under | 0.28 |
| Machine Hallucinations - ISS Dreams - A | Refik Anadol | AI Art | $277K | $1K | 0.004x | under | 0.34 |
| Embedding Study 1 & 2 | Holly Herndon & Mat Dryhurst | AI Art | $94K | $18K | 0.190x | under | 0.31 |
| Memories of Passersby I | Mario Klingemann | AI Art | $51K | $8K | 0.157x | under | 0.23 |

## Summary — Condition B: With Metadata

| Artwork | Artist | Category | True Price | Estimate | Ratio | Bias | Conf |
|---|---|---|---|---|---|---|---|
| Salvator Mundi | Leonardo da Vinci | Masterpieces | $450.3M | $350.0M | 0.777x | under | 0.61 |
| Nu couche | Amedeo Modigliani | Masterpieces | $170.4M | $165.0M | **0.968x** | fair | 0.72 |
| The Scream | Edvard Munch | Masterpieces | $119.9M | $180.0M | 1.501x | over | 0.94 |
| Portrait of Dr. Gachet | Vincent van Gogh | Masterpieces | $82.5M | $275.0M | 3.333x | over | 0.78 |
| Bal du moulin de la Galette | Pierre-Auguste Renoir | Masterpieces | $78.1M | $125.0M | 1.601x | over | 0.72 |
| Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer) | Gustav Klimt | Recent OOD | $236.4M | $85.0M | 0.360x | under | 0.69 |
| Blumenwiese (Blooming Meadow) | Gustav Klimt | Recent OOD | $86.0M | $42.0M | 0.488x | under | 0.73 |
| Piles de romans parisiens et roses dans un verre (Romans parisiens) | Vincent van Gogh | Recent OOD | $62.7M | $34.0M | 0.542x | under | 0.72 |
| No. 31 (Yellow Stripe) | Mark Rothko | Recent OOD | $62.2M | $48.0M | 0.772x | under | 0.71 |
| El sueno (La cama) / The Dream (The Bed) | Frida Kahlo | Recent OOD | $54.7M | $18.0M | 0.329x | under | 0.72 |
| Knife Behind Back | Yoshitomo Nara | Contemporary | $24.9M | $9.5M | 0.381x | under | 0.72 |
| Pie Fight Interior 12 | Adrian Ghenie | Contemporary | $10.4M | $4.8M | 0.462x | under | 0.72 |
| Walkers With the Dawn and Morning | Julie Mehretu | Contemporary | $10.7M | $8.5M | 0.792x | under | 0.73 |
| The Beautyful Ones | Njideka Akunyili Crosby | Contemporary | $4.7M | $5.8M | 1.224x | over | 0.78 |
| Force Field | George Condo | Contemporary | $6.9M | $950K | 0.139x | under | 0.68 |
| A.I. God: Portrait of Alan Turing | Ai-Da Robot | AI Art | $1.1M | $350K | 0.323x | under | 0.58 |
| Portrait of Edmond de Belamy | Obvious (collective) | AI Art | $432K | $650K | 1.503x | over | 0.76 |
| Machine Hallucinations - ISS Dreams - A | Refik Anadol | AI Art | $277K | $120K | 0.433x | under | 0.56 |
| Embedding Study 1 & 2 | Holly Herndon & Mat Dryhurst | AI Art | $94K | $28K | 0.296x | under | 0.42 |
| Memories of Passersby I | Mario Klingemann | AI Art | $51K | $350K | 6.861x | over | 0.66 |

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
| **Estimate** | **$1.8M** | **$350.0M** |
| **Ratio** | 0.004x (under) | 0.777x (under) |
| **Confidence** | 0.37 | 0.61 |

**Image Only — model reasoning:**

> The painting depicted is a half-length frontal image of Christ giving a blessing with the right hand and holding a transparent orb in the left, set against a dark ground. On purely visual grounds, it is unmistakably in the Renaissance idiom and very closely aligned with the highly famous Salvator Mundi composition associated with Leonardo da Vinci and his workshop/followers....

**Key factors cited:**

- Strong Renaissance/Leonardesque artistic quality and instantly recognizable Salvator Mundi-type composition
- Attribution uncertainty is decisive and prevents any valuation near autograph-master levels
- Visible condition issues including craquelure, abrasions, and probable restoration affect market appetite
- High cultural recognition and devotional subject increase buyer interest at major auction
- Could plausibly fit the market for a high-quality workshop, follower, or period variant rather than a later decorative copy

**With Metadata — model reasoning:**

> Assuming the attribution to Leonardo da Vinci is correct and the work is legally transferable, this is an object of the absolute highest order of rarity and market significance. Leonardo’s surviving painted oeuvre is extraordinarily small, generally understood to comprise fewer than twenty works, many of which are in permanent museum collections and effectively unavailable to the market. Any autograph Leonardo entering a major international auction is therefore not merely a high-value Old Master lot but a singular global event attracting museum, sovereign, and trophy-asset buyers far beyond the normal Old Masters market....

**Key factors cited:**

- Extreme rarity of autograph Leonardo paintings on the market
- Direct benchmark from the 2017 Salvator Mundi record sale
- Visible artistic qualities consistent with high Leonardo attribution
- Condition and restoration uncertainty materially affecting value
- Lack of supplied provenance and technical documentation reducing confidence

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
| **Estimate** | **$8K** | **$165.0M** |
| **Ratio** | 0.000x (under) | **0.968x** (fair) |
| **Confidence** | 0.18 | 0.72 |

**Image Only — model reasoning:**

> The image depicts a reclining female nude rendered in a highly simplified, stylized manner strongly reminiscent of early 20th-century modernism, and more specifically evocative of Amedeo Modigliani’s idiom: elongated body, mask-like face, almond-shaped eyes, simplified contouring, warm flesh tones set against saturated red and dark passages, and an emphasis on sculptural outline over naturalistic anatomy....

**Key factors cited:**

- Strong resemblance to Modigliani/School of Paris reclining nude style but no basis for attribution
- Visually effective composition with decorative market appeal
- Derivative character significantly limits value without provenance or signature
- Apparent surface wear, abrasions, and possible losses reduce auction competitiveness
- Valuation range is dominated by uncertainty between original period work and later copy

**With Metadata — model reasoning:**

> Assuming the work is authentic, legally transferable, and correctly identified as Amedeo Modigliani’s Nu couche from 1917–1918, this would be one of the most valuable paintings ever to come to market. Modigliani’s reclining nudes occupy the absolute top tier of 20th-century painting, both art-historically and commercially. They are rare, iconic, and immediately recognizable, representing the artist at the height of his mature style....

**Key factors cited:**

- Iconic 1917–1918 reclining nude series central to Modigliani’s market and legacy
- Strong auction comparables for top-tier Modigliani nudes in the $150M+ range
- High visual quality and classic stylistic hallmarks visible in the image
- Potential condition concerns visible, but likely secondary to rarity and significance
- Value heavily contingent on full authentication, catalogue inclusion, and clean provenance

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
| **Estimate** | **$150.0M** | **$180.0M** |
| **Ratio** | 1.251x (over) | 1.501x (over) |
| **Confidence** | 0.18 | 0.94 |

**Image Only — model reasoning:**

> The image depicts an instantly recognizable expressionist composition: a skeletal, agonized figure on a bridge beneath a blood-red and orange sky, with sweeping, undulating lines of landscape and water. Visually, it strongly corresponds to one of the most famous motifs in modern art, associated with Edvard Munch and specifically with versions of The Scream. Because the instruction is to base valuation solely on what is visible, I must assess this as the object presented: a painting that appears to be either an original version, a studio-period variant, or a later copy after that iconic composition....

**Key factors cited:**

- Visual correspondence to Edvard Munch's The Scream motif
- Apparent signature/date suggesting a late-19th-century attribution
- Extreme art-historical importance and rarity if authentic
- Visible condition issues but acceptable for an early modern work on fragile support
- Massive valuation uncertainty due to image-only assessment without provenance or technical examination

**With Metadata — model reasoning:**

> This work, as identified by the user, is Edvard Munch’s The Scream, year 1895, and specifically described as the pastel version that is the most colorful and the only one in private hands. On that basis, the valuation exercise is less about attributing an unknown object and more about estimating the fair market value of one of the most iconic images in the history of Western art. Assuming authenticity and legal availability for sale, this is a trophy masterpiece of extraordinary rarity....

**Key factors cited:**

- Direct benchmark from the 2012 Sotheby’s sale of the 1895 pastel at about $119.9 million
- Extreme rarity: only a few autograph versions of The Scream exist, with this version uniquely private
- Exceptional art-historical and cultural significance as an icon of Symbolism and early Expressionism
- Strong trophy-asset demand for globally recognizable museum-caliber masterpieces
- Condition appears acceptable for a fragile pastel, with rarity outweighing visible age-related wear

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
| **Estimate** | **$95.0M** | **$275.0M** |
| **Ratio** | **1.152x** (over) | 3.333x (over) |
| **Confidence** | 0.41 | 0.78 |

**Image Only — model reasoning:**

> The image shows a highly recognizable Post-Impressionist portrait executed in an expressive, directional brushwork style strongly associated with late nineteenth-century avant-garde painting. The sitter is depicted half-length, leaning his head on one hand, wearing a light cap and dark coat with bright buttons, against a swirling blue-green background. The handling is vigorous and rhythmic, with short, loaded strokes and strong contouring. The palette contrasts acidic yellows and greens in the flesh with deep blue-black clothing and a luminous tabletop, producing the psychological intensity characteristic of major modern master portraiture....

**Key factors cited:**

- Exceptional apparent artistic quality and iconic Post-Impressionist brushwork
- Strong visual indicators of a museum-caliber portrait by or attributable to Vincent van Gogh
- Extreme rarity and global demand for major van Gogh portraits at auction
- Apparently solid visual condition in reproduction, with no obvious major damage visible
- Large valuation uncertainty due to lack of title, dimensions, provenance, and technical examination

**With Metadata — model reasoning:**

> The work shown is Vincent van Gogh’s Portrait of Dr. Gachet, one of the most famous images in Western art and among the most important paintings of the artist’s final Auvers-sur-Oise period. Assuming authenticity and legal availability for sale, this is not simply a strong Van Gogh portrait; it is a canonical, museum-level masterpiece with extraordinary art-historical significance, profound cultural recognition, and extreme rarity. Van Gogh’s portraits from 1890 are among the most emotionally charged works in modern art, and Dr. Gachet, painted only weeks before the artist’s death, occupies a singular place in the mythology of his career....

**Key factors cited:**

- Canonical masterpiece from Van Gogh’s final Auvers period with exceptional art-historical importance
- One of the most recognizable and culturally iconic portraits in the history of modern art
- Extreme rarity of top-tier Van Gogh portraits available on the open market
- Historic auction precedent for this very subject combined with major expansion of the trophy art market since 1990
- Value highly sensitive in practice to provenance, title clarity, and detailed condition, none of which are supplied here

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
| **Estimate** | **$18.0M** | **$125.0M** |
| **Ratio** | 0.230x (under) | 1.601x (over) |
| **Confidence** | 0.31 | 0.72 |

**Image Only — model reasoning:**

> Visually, this appears to be a major late-19th-century French Impressionist or Impressionist-adjacent work of very high ambition and quality. The painting depicts a crowded outdoor leisure scene with dancing couples, café tables, lanterns, dappled light, and fashionable urban figures. The handling is loose yet highly controlled, with broken brushwork, flickering highlights, soft atmospheric transitions, and a sophisticated orchestration of figures in depth. The color structure relies on luminous creams, blues, blacks, pinks, and greens, with warm flesh accents animating the composition....

**Key factors cited:**

- Apparent museum-quality Impressionist handling and composition
- Complex Parisian leisure subject highly favored in the market
- Strong resemblance to top-tier Renoir/late-19th-century French painting
- No provenance, authorship, size, or technical data to support full attribution
- Condition appears generally sound from the image but cannot be verified

**With Metadata — model reasoning:**

> This work, identified as Pierre-Auguste Renoir’s Bal du moulin de la Galette of 1876 and specified as the smaller of the two versions, would rank among the most desirable and valuable Impressionist paintings conceivable were it to appear on the open market today. Renoir is one of the canonical founders of Impressionism, and 1876 is a peak year both for the movement and for the artist personally. The Moulin de la Galette subject is not merely an attractive Parisian genre scene; it is one of the defining icons of modern life painting in the 19th century, synthesizing urban leisure, atmospheric light, social observation, and bravura brushwork....

**Key factors cited:**

- Iconic 1876 Impressionist masterpiece from Renoir’s prime period
- Moulin de la Galette is one of the most celebrated subjects in 19th-century art
- Exceptional multi-figure composition, atmospheric light, and strong visual quality
- Trophy rarity: major museum-caliber Renoir works of this significance almost never reach auction
- Valuation is tempered by lack of condition report, provenance, and the fact this is the smaller version

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
| **Estimate** | **$180.0M** | **$85.0M** |
| **Ratio** | 0.762x (under) | 0.360x (under) |
| **Confidence** | 0.66 | 0.69 |

**Image Only — model reasoning:**

> The painting shown is visually consistent with a major early-20th-century Viennese Secessionist work and, more specifically, strongly resembles a prime-period Gustav Klimt portrait composition: a full-length female figure placed frontally against a flattened decorative field, with ornamental patterning integrated into the sitter’s costume and surroundings, and an intentional tension between naturalistic facial modeling and stylized, near-abstract surface design. Even if I set aside explicit identification and appraise only from what is visible, the work presents at an exceptionally high artistic level....

**Key factors cited:**

- Museum-caliber decorative portrait of exceptional visual sophistication
- Strong visual consistency with a prime-period Viennese Secession master, likely Klimt
- Rarity and desirability of iconic early modern female portraits at auction
- Apparent good overall condition from the image, with no obvious major losses
- Potential for intense international competition if authenticated and fresh to market

**With Metadata — model reasoning:**

> This work, identified as Gustav Klimt’s Bildnis Elisabeth Lederer (1914–1916), would, if authentic and legally available, rank as an exceptionally valuable museum-caliber portrait from the artist’s late period. On visual evidence alone, it is consistent with Klimt’s mature portrait practice: a frontal, elongated female figure integrated into a decorative field, with the sitter’s naturalistically rendered face and hands set against a highly stylized textile-like environment. The composition balances psychological presence and ornamental abstraction, a hallmark of Klimt’s most admired portraits....

**Key factors cited:**

- Museum-caliber late portrait by Gustav Klimt, an artist of extreme rarity and demand
- Strong artistic quality combining psychological portraiture with mature decorative abstraction
- Important sitter connected to the Lederer family, among Klimt’s key patrons
- Comparable major Klimt portraits have achieved high eight-figure prices at international auction
- Valuation tempered by absence of provenance, restitution clarity, condition report, and auction history

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
| **Estimate** | **$8.5M** | **$42.0M** |
| **Ratio** | 0.099x (under) | 0.488x (under) |
| **Confidence** | 0.39 | 0.73 |

**Image Only — model reasoning:**

> The painting shown is a highly accomplished late-19th- or early-20th-century style landscape rendered in a dense, broken-brush, colorist manner strongly associated with Post-Impressionism and, more specifically, with the decorative, all-over surface treatment seen in Gustav Klimt’s landscape practice. The image depicts an orchard or meadow carpeted with wildflowers, with fruit trees or small orchard trees rising from a field of intense green. The entire surface is built from myriad small touches of paint in greens, violets, yellows, pinks, and blues, producing a shimmering optical effect....

**Key factors cited:**

- Strong visual affinity with major Post-Impressionist/Vienna Secession landscape painting
- Exceptional decorative surface and chromatic sophistication
- Compressed, pattern-based composition suggesting a mature and distinctive hand
- Condition appears generally sound from the image, with only minor visible craquelure
- Valuation heavily constrained by absence of confirmed artist, date, provenance, and medium details

**With Metadata — model reasoning:**

> Assuming the attribution to Gustav Klimt is correct, this is a highly significant work from one of the artist’s most sought-after landscape periods: the Attersee summers around 1908, contemporaneous with the height of his mature style. Klimt’s landscapes, though historically overshadowed in popular imagination by the gold-ground portraits, have become increasingly prized in the market and in scholarship because they represent a distilled, radical vision of nature built from mosaic-like color units, flattened perspective, and decorative all-over patterning....

**Key factors cited:**

- Prime c.1908 Attersee-period Klimt landscape
- Strong square-format composition with highly desirable flower-meadow subject
- Mature mosaic-like, pointillist-influenced handling characteristic of Klimt’s most sought-after landscapes
- Comparable Klimt landscapes have sold in the tens of millions at major auctions
- Lack of provenance, exhibition history, dimensions, and formal condition report limits certainty

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
| **Estimate** | **$6K** | **$34.0M** |
| **Ratio** | 0.000x (under) | 0.542x (under) |
| **Confidence** | 0.34 | 0.72 |

**Image Only — model reasoning:**

> Based solely on the image, this appears to be a modern or contemporary still life of stacked books executed in oil on canvas or board, with a restrained but deliberate palette dominated by ochres, olive greens, pale pinks, creams, muted blues, and one notable rust-red accent. The composition is intelligently organized: the books are arranged in a loose circular pile, creating both structural rhythm and a slightly unstable, intimate domestic tension. The artist shows a strong understanding of planar construction and volume through economical means....

**Key factors cited:**

- Competent modernist still-life composition with strong formal structure
- Muted, harmonious palette and confident brushwork suggest artistic quality
- No identifying information, attribution, provenance, or dimensions severely limits value
- Condition appears broadly stable from the image with no obvious major damage
- Comparable market position is likely unattributed 20th-century modernist decorative fine art

**With Metadata — model reasoning:**

> Assuming the attribution to Vincent van Gogh is correct, this is an extraordinarily valuable work by one of the most liquid and sought-after names in the global art market. The title and date place it in Paris, 1887, a pivotal year in Van Gogh’s development, when his palette brightened and his handling became more experimental under the influence of Impressionism, Japanese prints, and the urban avant-garde....

**Key factors cited:**

- Authenticated 1887 Paris-period Vincent van Gogh work from a pivotal developmental moment
- Extreme rarity as one of only a handful of Van Gogh book still lifes
- Strong scholarly and thematic interest linking directly to Van Gogh’s literary passions
- Solid visual quality and modern structural composition, though not an iconic top-tier Van Gogh motif
- Value highly contingent on unseen provenance, condition report, and legal/ownership clarity

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
| **Estimate** | **$18K** | **$48.0M** |
| **Ratio** | 0.000x (under) | 0.772x (under) |
| **Confidence** | 0.39 | 0.71 |

**Image Only — model reasoning:**

> Visually, this work is a large-scale abstract color-field painting consisting of two stacked, soft-edged rectangular zones: an upper warm brownish-ochre field and a lower deep crimson-red field, separated and surrounded by a luminous yellow ground. The composition, scale, feathered transitions, and stained/scrubbed handling strongly evoke the visual language of postwar American Color Field painting, and more specifically the idiom associated with Mark Rothko and painters working in his orbit....

**Key factors cited:**

- Strong visual resemblance to postwar Color Field abstraction
- High aesthetic quality and effective chromatic balance
- No visible signature, provenance, or artist identification
- Apparently stable overall condition from the image
- Auction value severely limited by anonymity despite decorative and artistic appeal

**With Metadata — model reasoning:**

> This work, if authentic and correctly dated 1958, would sit within one of the most desirable and commercially powerful periods of Mark Rothko’s oeuvre. The late 1950s are widely regarded as the apex of Rothko’s mature style, when his floating rectangular forms, softened edges, and luminous chromatic relationships achieved their fullest emotional and formal authority. A 1958 canvas with a strong, archetypal arrangement of stacked fields immediately places the picture in the category of museum-caliber Abstract Expressionist painting....

**Key factors cited:**

- Prime 1958 date within Rothko’s most sought-after mature period
- Strong canonical Color Field composition with luminous stacked rectangles
- Likely large-scale format, which materially increases Rothko auction value
- Comparable major Rothko works trade in the multi-tens-of-millions range
- Lack of provenance, dimensions, and condition report introduces meaningful uncertainty

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
| **Estimate** | **$3.5M** | **$18.0M** |
| **Ratio** | 0.064x (under) | 0.329x (under) |
| **Confidence** | 0.31 | 0.72 |

**Image Only — model reasoning:**

> The image shows a highly imaginative, symbolically charged figurative composition in a surrealist mode: a sleeping child or young woman lies in a wooden four-poster bed, covered by a vivid ochre-gold blanket with vine-like tendrils extending across the bedding and into the mattress area. Above, on the canopy shelf, rests a skeletal or puppet-like figure intertwined with wires or cords, holding or adorned with flowers, with a skull-like head and pillow to the right. The cloudy, atmospheric background removes the scene from ordinary domestic space and places it in a dreamlike, psychological register....

**Key factors cited:**

- Strong surrealist/magic-realist imagery with psychologically powerful symbolism
- High apparent technical quality and sophisticated compositional structure
- Visual affinity with important mid-20th-century Latin American and European surrealism
- No visible major condition issues in the reproduction, though condition cannot be confirmed
- Extreme valuation uncertainty due to absent authorship, provenance, date, size, and medium

**With Metadata — model reasoning:**

> This work, identified as Frida Kahlo’s El sueño (La cama) / The Dream (The Bed), 1940, would rank as an exceptionally important painting within the artist’s oeuvre if authentic, title-confirmed, and legally available for sale. Frida Kahlo occupies the very top tier of the Latin American art market and, more importantly, has become a global blue-chip name with a collector base extending far beyond the regional market into major international modern art, surrealism-adjacent, feminist art, and museum-driven collecting categories....

**Key factors cited:**

- Frida Kahlo’s extreme rarity and global blue-chip market status
- Strong 1940 date from a mature and highly collectible period
- Iconic autobiographical and mortality-themed imagery with self-portrait elements
- Museum-quality composition and unmistakable Kahlo symbolism
- Lack of provenance, condition report, dimensions, and technical documentation limits certainty

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
| **Estimate** | **$1.8M** | **$9.5M** |
| **Ratio** | 0.072x (under) | 0.381x (under) |
| **Confidence** | 0.32 | 0.72 |

**Image Only — model reasoning:**

> The image depicts a highly recognizable style associated with late-20th- to early-21st-century Japanese contemporary painting: a large-headed child with a confrontational expression, simplified anatomy, smooth matte surface, and minimal background. Visually, it strongly evokes the aesthetic vocabulary of Yoshitomo Nara and artists working in the orbit of Japanese Superflat/pop-inflected figurative painting....

**Key factors cited:**

- Strong visual resemblance to blue-chip Japanese contemporary figurative painting associated with Yoshitomo Nara
- High commercial appeal of the iconic angry-child motif with minimal background
- Appears to be a well-executed original painting with smooth, controlled surface and good apparent condition
- Value is highly sensitive to attribution, originality, scale, and provenance, none of which are provided
- Comparable auction outcomes for authenticated works in this style range from mid-six figures to multi-millions

**With Metadata — model reasoning:**

> This work is consistent in subject, mood, and formal language with Yoshitomo Nara’s most desirable period: the late 1990s to early 2000s, when his iconic solitary child figures with defiant or unsettling expressions became fully crystallized. The title Knife Behind Back is itself highly resonant within Nara’s market, because collectors strongly favor images in which innocence and threat coexist....

**Key factors cited:**

- Prime Yoshitomo Nara period circa 2000, the artist’s most sought-after market phase
- Iconic angry-child imagery with hidden-weapon menace, a highly desirable Nara motif
- Apparent monumental scale and strong visual impact, which materially increase auction value
- Clean, seemingly well-preserved surface from the image, though no formal condition report is available
- Lack of provenance, dimensions, and exhibition history limits certainty despite very strong market comparables

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
| **Estimate** | **$6K** | **$4.8M** |
| **Ratio** | 0.001x (under) | 0.462x (under) |
| **Confidence** | 0.24 | 0.72 |

**Image Only — model reasoning:**

> Based solely on the image provided, the work appears to be a very large-scale contemporary painting, likely acrylic and/or oil on canvas, installed vertically in a studio setting. The composition is ambitious and immersive, combining abstraction with fragments of figuration and landscape-like forms. There is a seated male figure in the studio foreground, but it is unclear whether he is part of the painting or physically in front of it; the image overall reads as a photograph of an artist in front of a monumental work rather than a straightforward reproduction of the painting itself....

**Key factors cited:**

- Monumental scale and strong visual impact
- Contemporary abstract-figurative hybrid style with market appeal
- No identifiable artist, title, date, or provenance
- Studio-shot image creates ambiguity about presentation and condition
- Anonymous contemporary works face steep auction discounts despite apparent quality

**With Metadata — model reasoning:**

> This work, identified as Adrian Ghenie’s Pie Fight Interior 12 from 2014, falls squarely within one of the artist’s most commercially and critically important bodies of work. Ghenie’s market has been driven by the rarity of his strongest large-scale figurative paintings, especially from the period roughly spanning 2010 to 2015, when his synthesis of gestural abstraction, psychological figuration, and historically charged grotesque imagery reached a peak of institutional and collector demand....

**Key factors cited:**

- Highly desirable 2014 Adrian Ghenie canvas from the celebrated Pie Fight Interior series
- Large-scale, fully developed figurative composition consistent with the artist’s strongest market period
- Strong alignment with Ghenie’s signature themes of grotesque comedy, violence, and painterly distortion
- Comparable major works by Ghenie from 2010–2015 have achieved multi-million-dollar auction results
- Lack of provenance, exhibition history, exact dimensions, and condition report tempers the estimate

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
| **Estimate** | **$12K** | **$8.5M** |
| **Ratio** | 0.001x (under) | 0.792x (under) |
| **Confidence** | 0.34 | 0.73 |

**Image Only — model reasoning:**

> This appears to be a large-scale contemporary abstract painting, likely mixed media on canvas, dominated by a restrained grayscale palette with selective red linear accents and fine white incisions or overdrawn geometric tracery. Visually, the work combines gestural, atmospheric brushwork with calligraphic mark-making, scratches, layered washes, and schematic linear interventions. The composition is panoramic and ambitious in scale, suggesting a work intended for a contemporary gallery or institutional wall rather than a modest studio exercise....

**Key factors cited:**

- Large-scale, professionally executed contemporary abstract composition
- Strong visual sophistication with layered gestural and linear mixed-media effects
- Neutral grayscale palette with selective red accents aligns with current collector taste
- No visible artist identification, provenance, or exhibition history to support higher pricing
- Apparent good condition and strong wall presence enhance auction appeal

**With Metadata — model reasoning:**

> This work, identified as Julie Mehretu’s Walkers With the Dawn and Morning (2008), appears from the image and description to be a large-scale, mature-period abstraction of the kind most associated with the artist’s strongest secondary-market performance. Mehretu is among the most important living painters working in large-format abstract painting, and her market has moved from strong institutional and collector demand into the upper tier of the contemporary auction market....

**Key factors cited:**

- Strong 2008 mature-period Julie Mehretu painting
- Monumental scale and high-complexity layered abstraction
- Excellent alignment with the artist’s most sought-after visual language
- Robust blue-chip institutional and auction-market demand for Mehretu
- Lack of provenance and condition documentation limits precision

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
| **Estimate** | **$180K** | **$5.8M** |
| **Ratio** | 0.038x (under) | 1.224x (over) |
| **Confidence** | 0.34 | 0.78 |

**Image Only — model reasoning:**

> Visually, this appears to be a large-scale contemporary mixed-media portrait, likely combining collage, photographic transfer or acrylic/oil rendering, and geometric painted overlays on paper or canvas. The central image is a full-length portrait of a young Black girl in a formal white dress with pink ribbons and gloves, set against a densely collaged ground of found printed imagery. A salmon-pink rectilinear framing element partially encloses the figure, while cream lattice-like geometric motifs interrupt the lower foreground....

**Key factors cited:**

- High-quality contemporary mixed-media portraiture with strong visual and conceptual sophistication
- Large scale and polished execution increase auction desirability
- Subject matter aligns with a strong market for figurative works exploring Black identity and history
- Apparent good condition from the image, with no obvious major damage visible
- Severe valuation uncertainty due to absence of artist attribution, date, provenance, and exhibition history

**With Metadata — model reasoning:**

> This work is consistent in subject, facture, and compositional language with Njideka Akunyili Crosby’s highly sought-after mature early-2010s practice, a period that many collectors and institutions regard as foundational to her market and art-historical standing. The image shows a full-length female figure rendered with extraordinary delicacy against a dense photo-transfer collage ground, integrating painting, drawing, and layered appropriated imagery....

**Key factors cited:**

- Strong early-mature 2012 date within Akunyili Crosby’s most coveted formative period
- High artistic quality combining portraiture, photo-transfer collage, and cross-cultural narrative complexity
- Robust international demand for the artist from collectors and institutions
- Likely substantial scale and fully resolved composition rather than a study or minor work
- Value sensitive to condition, provenance, and whether the work matches top-tier exhibition-quality examples in person

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
| **Estimate** | **$4K** | **$950K** |
| **Ratio** | 0.001x (under) | 0.139x (under) |
| **Confidence** | 0.29 | 0.68 |

**Image Only — model reasoning:**

> This appraisal must necessarily be highly provisional because the work is unattributed, undated, and lacks all confirming information on medium, dimensions, provenance, exhibition history, literature, and condition beyond what is visible in a digital image. In auction practice, those missing data points are often decisive. Based solely on the image, the painting appears to be a contemporary large-format figurative abstraction, likely acrylic and mixed media on canvas, combining gestural color fields with linear drawing and neo-cubist figuration....

**Key factors cited:**

- Strong decorative impact and appealing contemporary palette
- Competent figurative-abstract technique with layered mixed-media appearance
- Stylistically derivative of Picasso/neo-expressionist contemporary idioms
- No visible attribution, provenance, dimensions, or market history
- Condition appears generally good from the image alone

**With Metadata — model reasoning:**

> This painting is consistent in subject, palette, and compositional language with George Condo’s mature 2000s–2010s body of work, especially his highly sought-after ‘Expanded Portrait’ and multi-figure grotesque compositions that synthesize Old Master figuration, Picasso-derived fragmentation, cartoon distortion, and psychological caricature. The title, date, and image suggest a fully realized, market-appropriate Condo from a strong period. Around 2010, Condo was producing works that became central to his current market identity: inventive, theatrical, intellectually legible, and immediately recognizable....

**Key factors cited:**

- Desirable 2010 date within George Condo’s highly collected mature period
- Strong multi-figure grotesque composition characteristic of his core market identity
- Apparent good scale and visually compelling square format suitable for major auction placement
- No provenance, exhibition history, or condition report provided, limiting certainty and upside
- Comparable Condo paintings from the late 2000s–early 2010s regularly trade in the high six to low seven figures

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
| **Estimate** | **$4K** | **$350K** |
| **Ratio** | 0.003x (under) | 0.323x (under) |
| **Confidence** | 0.31 | 0.58 |

**Image Only — model reasoning:**

> Based solely on the image, this appears to be a contemporary or late-20th-/21st-century figurative-abstract painting on canvas or board, presented in a simple modern white frame. The composition centers on a fragmented human face rendered in earthy whites, browns, blacks, and grays against a very dark, nearly black ground animated by dense, gestural, low-contrast mark-making. A rectangular lateral extension from the face to the right gives the work a psychologically charged, almost sculptural or mask-like quality. There are also a few small colored dot accents (yellow and blue) that punctuate the otherwise restrained palette....

**Key factors cited:**

- Compelling contemporary figurative-abstract composition with psychological impact
- Textural surface and restrained palette suggest serious studio practice
- No visible attribution, provenance, title, date, or exhibition history
- Condition appears generally sound from the image alone
- Comparable market for unattributed contemporary expressionist portraits is modest

**With Metadata — model reasoning:**

> This work is attributed to Ai-Da Robot, a highly publicized contemporary artistic project positioned at the intersection of art, artificial intelligence, robotics, and media discourse. The title, A.I. God: Portrait of Alan Turing, is especially important to valuation because it ties the work not only to a known contemporary brand-like artistic identity but also to Alan Turing, a figure of immense historical and symbolic significance in computing, machine intelligence, and modern intellectual culture. That conceptual framing enhances market appeal well beyond the purely formal qualities of the image....

**Key factors cited:**

- Ai-Da Robot’s high-profile authorship and media visibility in the AI-art field
- Alan Turing subject matter adds major historical and conceptual significance
- Fragmented, computational aesthetic coherently aligns form and theme
- Thin but potentially strong auction market driven by narrative and institutional interest
- Lack of provenance, condition report, and specific exhibition history limits certainty

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
| **Estimate** | **$12K** | **$650K** |
| **Ratio** | 0.028x (under) | 1.503x (over) |
| **Confidence** | 0.28 | 0.76 |

**Image Only — model reasoning:**

> Based solely on the image, this appears to be a contemporary figurative painting or mixed-media work depicting a standing figure in a dark coat, rendered with heavily blurred, atmospheric handling. The most striking visual elements are the soft-focus facial treatment, the broad, dark mass of the clothing, and the painterly, almost smeared edges that create a haunting, psychologically charged presence. There is also handwritten mathematical notation in the lower right corner, which suggests either a conceptual overlay, a later intervention, or an artist working at the intersection of figurative painting and contemporary idea-based practice....

**Key factors cited:**

- Strong atmospheric figurative composition with clear artistic sophistication
- No visible signature, title, date, provenance, or dimensions to support attribution
- Handwritten mathematical notation adds conceptual interest but also uncertainty
- Condition appears generally stable from the image, though medium and originality are unclear
- Auction value for unattributed contemporary figurative works is far lower than for identifiable artists

**With Metadata — model reasoning:**

> This work is identifiable from the title and description as Portrait of Edmond de Belamy, the best-known output of the French collective Obvious and one of the most historically recognizable early AI-generated artworks to enter the mainstream art market. The valuation question here is unusual because the image itself, judged solely on conventional pictorial criteria, would not justify a major auction value remotely commensurate with its market fame....

**Key factors cited:**

- Landmark status as a highly publicized early AI-generated artwork
- Strong cross-category appeal to contemporary, digital, and technology-focused collectors
- Value driven more by historical significance and media notoriety than pure pictorial quality
- Original major-auction precedent provides a concrete market anchor
- Uncertainty around documentation, edition specifics, and long-term critical standing tempers the estimate

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
| **Estimate** | **$1K** | **$120K** |
| **Ratio** | 0.004x (under) | 0.433x (under) |
| **Confidence** | 0.34 | 0.56 |

**Image Only — model reasoning:**

> Based solely on the image, this appears to be a contemporary abstract work, likely a pigment print, digital print, or mixed-media print with a fluid, marbled composition. The image presents a vertically oriented abstraction dominated by turquoise, teal, deep blue-black, copper, orange, and gold tones. The visual language strongly recalls current trends in digitally generated abstraction, resin/pour-paint aesthetics, ink-in-water photography, or manipulated fluid acrylic imagery....

**Key factors cited:**

- Strong decorative visual impact and contemporary abstract appeal
- No visible artist attribution, signature, title, or provenance
- Likely print-based or digitally derived appearance rather than clearly unique painting
- Apparent good overall condition and professional presentation
- Auction market for unattributed contemporary abstractions is typically modest

**With Metadata — model reasoning:**

> This work is presented as a 2025 piece by Refik Anadol from the Machine Hallucinations / ISS Dreams body of work, and that attribution is the single most important driver of value. Anadol occupies a significant and still highly visible position within the market for digitally native, AI- and data-driven contemporary art. His best-known projects have institutional scale, strong public recognition, and broad crossover appeal among contemporary art collectors, technology collectors, and crypto-native buyers....

**Key factors cited:**

- Refik Anadol’s strong global profile in AI- and data-driven contemporary art
- Visual consistency with the sought-after Machine Hallucinations aesthetic and ISS/scientific dataset theme
- Uncertainty over medium, edition size, certificate, and whether this is a static print versus a dynamic digital work
- Apparent strong condition and high visual impact from the provided image
- Comparable market range for Anadol spans low five figures to low six figures depending on rarity and format

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
| **Estimate** | **$18K** | **$28K** |
| **Ratio** | 0.190x (under) | 0.296x (under) |
| **Confidence** | 0.31 | 0.42 |

**Image Only — model reasoning:**

> Based solely on the image, this appears to be a contemporary figurative-surreal painting of high technical ambition and strong visual impact. The composition presents a frontal full-length figure occupying most of the picture plane, rendered with polished realism in the face, hair, and metallic-looking protective suit, yet clearly inhabiting a surreal, invented world. The subject combines a childlike or adolescent face with monumental costume, exaggerated orange braided hair cascading across the body, and a bright cloud-filled sky that evokes both classical portrait backdrops and contemporary fantasy illustration....

**Key factors cited:**

- High technical finish and strong command of figurative-surreal painting
- Memorable, market-friendly iconography with strong visual impact
- Good apparent condition with no obvious major damage visible
- Contemporary style aligns with active collector demand for polished figurative work
- Lack of artist identification, provenance, scale, and medium greatly suppresses certainty and value

**With Metadata — model reasoning:**

> This work, identified as Embedding Study 1 & 2 by Holly Herndon and Mat Dryhurst, should be evaluated within the context of contemporary post-internet, AI-inflected, and media-conscious art rather than traditional painting alone. Herndon and Dryhurst are best known as artists, musicians, and theorists working at the intersection of machine learning, authorship, network culture, and identity. That interdisciplinary profile is important: their market is likely driven less by conventional connoisseurship around brushwork and more by institutional relevance, conceptual framing, edition structure, exhibition context, and scarcity....

**Key factors cited:**

- Strong visual impact and technically polished uncanny figurative composition
- Artists' relevance to AI, identity, and post-internet contemporary discourse
- Uncertainty over medium, uniqueness, and edition size materially affects value
- No provenance, exhibition history, or auction comparables supplied
- Likely stronger appeal to institutional and specialist collectors than broad blue-chip auction demand

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
| **Estimate** | **$8K** | **$350K** |
| **Ratio** | 0.157x (under) | 6.861x (over) |
| **Confidence** | 0.23 | 0.66 |

**Image Only — model reasoning:**

> The work shown appears to be a contemporary installation consisting of two vertically oriented digital screens or monitor-based lightboxes displaying close-up, highly stylized female faces, mounted side by side above a mid-century-style cabinet or console with visible power cords. Because I have no artist, title, date, edition, medium specification, exhibition history, or provenance, the valuation must be based purely on what is visible and on how anonymous contemporary digital/video installation works of this apparent quality tend to perform in the market. That lack of identifying information is the single greatest suppressor of value....

**Key factors cited:**

- Visually polished contemporary two-screen digital installation with strong decorative and atmospheric appeal
- No artist attribution, title, date, provenance, or edition information, severely limiting auction confidence
- Electronic media works carry maintenance, obsolescence, and documentation risks that suppress value
- Condition appears generally good from the image, with functioning displays and professional presentation
- Comparable anonymous or lesser-known contemporary digital installations typically trade in the low-thousands to low-five-figure range

**With Metadata — model reasoning:**

> Mario Klingemann’s Memories of Passersby I is among the better-known early AI-driven generative portrait installations and occupies an important place in the short but increasingly historicized canon of machine-learning art. Based on the supplied image and metadata, this appears to be the dual-screen cabinet presentation associated with the 2018 work: two vertically oriented monitors mounted above or integrated with a mid-century-style wooden cabinet, displaying continuously morphing fictive portrait busts derived from training on historical European portraiture....

**Key factors cited:**

- Historically important early AI/generative artwork by a leading pioneer in the field
- Strong visual and conceptual appeal through continuously evolving faux-historical portraits
- Recognizable signature work with institutional and critical relevance
- Value heavily dependent on edition status, documentation, software/hardware integrity, and installation completeness
- Auction demand for media-based AI installations is meaningful but still narrower and more volatile than traditional art categories
