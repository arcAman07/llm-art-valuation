# Experiment 1 — Appraisal Logs: Gemini 3.1 Pro

| Field | Value |
|---|---|
| **Model** | Gemini 3.1 Pro |
| **Organisation** | Google |
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
| Salvator Mundi | Leonardo da Vinci | Masterpieces | $450.3M | $450.0M | **0.999x** | fair | 0.95 |
| Nu couche | Amedeo Modigliani | Masterpieces | $170.4M | $120.0M | 0.704x | under | 0.95 |
| The Scream | Edvard Munch | Masterpieces | $119.9M | $300.0M | 2.502x | over | 0.95 |
| Portrait of Dr. Gachet | Vincent van Gogh | Masterpieces | $82.5M | $250.0M | 3.030x | over | 0.95 |
| Bal du moulin de la Galette | Pierre-Auguste Renoir | Masterpieces | $78.1M | $300.0M | 3.841x | over | 0.98 |
| Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer) | Gustav Klimt | Recent OOD | $236.4M | — | N/A | — | — |
| Blumenwiese (Blooming Meadow) | Gustav Klimt | Recent OOD | $86.0M | $75.0M | **0.872x** | fair | 0.95 |
| Piles de romans parisiens et roses dans un verre (Romans parisiens) | Vincent van Gogh | Recent OOD | $62.7M | $42.0M | 0.670x | under | 0.95 |
| No. 31 (Yellow Stripe) | Mark Rothko | Recent OOD | $62.2M | $87.0M | 1.400x | over | 0.95 |
| El sueno (La cama) / The Dream (The Bed) | Frida Kahlo | Recent OOD | $54.7M | $25.0M | 0.457x | under | 0.95 |
| Knife Behind Back | Yoshitomo Nara | Contemporary | $24.9M | $12.5M | 0.501x | under | 0.95 |
| Pie Fight Interior 12 | Adrian Ghenie | Contemporary | $10.4M | $8.5M | **0.817x** | under | 0.95 |
| Walkers With the Dawn and Morning | Julie Mehretu | Contemporary | $10.7M | $4.5M | 0.419x | under | 0.85 |
| The Beautyful Ones | Njideka Akunyili Crosby | Contemporary | $4.7M | $3.0M | 0.633x | under | 0.95 |
| Force Field | George Condo | Contemporary | $6.9M | $2.5M | 0.365x | under | 0.90 |
| A.I. God: Portrait of Alan Turing | Ai-Da Robot | AI Art | $1.1M | — | N/A | — | — |
| Portrait of Edmond de Belamy | Obvious (collective) | AI Art | $432K | $400K | **0.925x** | fair | 0.98 |
| Machine Hallucinations - ISS Dreams - A | Refik Anadol | AI Art | $277K | $850 | 0.003x | under | 0.65 |
| Embedding Study 1 & 2 | Holly Herndon & Mat Dryhurst | AI Art | $94K | $400 | 0.004x | under | 0.85 |
| Memories of Passersby I | Mario Klingemann | AI Art | $51K | $120K | 2.352x | over | 0.95 |

## Summary — Condition B: With Metadata

| Artwork | Artist | Category | True Price | Estimate | Ratio | Bias | Conf |
|---|---|---|---|---|---|---|---|
| Salvator Mundi | Leonardo da Vinci | Masterpieces | $450.3M | $450.0M | **0.999x** | fair | 0.95 |
| Nu couche | Amedeo Modigliani | Masterpieces | $170.4M | $165.0M | **0.968x** | fair | 0.95 |
| The Scream | Edvard Munch | Masterpieces | $119.9M | $350.0M | 2.919x | over | 0.90 |
| Portrait of Dr. Gachet | Vincent van Gogh | Masterpieces | $82.5M | $250.0M | 3.030x | over | 0.95 |
| Bal du moulin de la Galette | Pierre-Auguste Renoir | Masterpieces | $78.1M | $150.0M | 1.921x | over | 0.90 |
| Bildnis Elisabeth Lederer (Portrait of Elisabeth Lederer) | Gustav Klimt | Recent OOD | $236.4M | $135.0M | 0.571x | under | 0.92 |
| Blumenwiese (Blooming Meadow) | Gustav Klimt | Recent OOD | $86.0M | $85.0M | **0.988x** | fair | 0.90 |
| Piles de romans parisiens et roses dans un verre (Romans parisiens) | Vincent van Gogh | Recent OOD | $62.7M | $34.0M | 0.542x | under | 0.85 |
| No. 31 (Yellow Stripe) | Mark Rothko | Recent OOD | $62.2M | $85.0M | 1.367x | over | 0.92 |
| El sueno (La cama) / The Dream (The Bed) | Frida Kahlo | Recent OOD | $54.7M | $42.0M | 0.768x | under | 0.95 |
| Knife Behind Back | Yoshitomo Nara | Contemporary | $24.9M | $25.0M | **1.002x** | fair | 0.98 |
| Pie Fight Interior 12 | Adrian Ghenie | Contemporary | $10.4M | $8.5M | **0.817x** | under | 0.92 |
| Walkers With the Dawn and Morning | Julie Mehretu | Contemporary | $10.7M | $10.7M | **0.997x** | fair | 0.98 |
| The Beautyful Ones | Njideka Akunyili Crosby | Contemporary | $4.7M | $3.0M | 0.633x | under | 0.90 |
| Force Field | George Condo | Contemporary | $6.9M | $3.8M | 0.554x | under | 0.90 |
| A.I. God: Portrait of Alan Turing | Ai-Da Robot | AI Art | $1.1M | $160K | 0.147x | under | 0.85 |
| Portrait of Edmond de Belamy | Obvious (collective) | AI Art | $432K | $500K | **1.156x** | over | 0.85 |
| Machine Hallucinations - ISS Dreams - A | Refik Anadol | AI Art | $277K | $125K | 0.451x | under | 0.82 |
| Embedding Study 1 & 2 | Holly Herndon & Mat Dryhurst | AI Art | $94K | $25K | 0.265x | under | 0.85 |
| Memories of Passersby I | Mario Klingemann | AI Art | $51K | $75K | 1.470x | over | 0.92 |

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
| **Estimate** | **$450.0M** | **$450.0M** |
| **Ratio** | **0.999x** (fair) | **0.999x** (fair) |
| **Confidence** | 0.95 | 0.95 |

**Image Only — model reasoning:**

> Based on the visual evidence provided, this artwork is immediately identifiable as the 'Salvator Mundi', a masterpiece widely attributed to the High Renaissance master Leonardo da Vinci. The painting depicts Christ as the Savior of the World, facing the viewer in a strict frontal pose, holding a transparent crystal orb in his left hand while raising his right hand in a classical gesture of benediction. Technically, the work exhibits several undeniable hallmarks of Leonardo's genius....

**Key factors cited:**

- Attribution to Leonardo da Vinci and extreme scarcity of his paintings
- Masterful execution of sfumato and anatomical precision in intact areas
- Significant historical condition issues, including heavy abrasion and extensive restoration
- Unprecedented 2017 auction record establishing an absolute market floor
- Status as the ultimate global trophy asset for ultra-high-net-worth collectors

**With Metadata — model reasoning:**

> The artwork presented for appraisal is Leonardo da Vinci’s 'Salvator Mundi,' a piece that occupies a unique and almost mythical space within the global art market and art-historical discourse. To appraise a painting by Leonardo da Vinci is to evaluate an asset that transcends traditional market comparables; with fewer than twenty universally or widely accepted autograph paintings by the Renaissance master in existence, any appearance on the open market is a generational event....

**Key factors cited:**

- Extreme scarcity of autograph paintings by Leonardo da Vinci (fewer than 20 known)
- Unprecedented historical market precedent (sold for $450.3M in 2017)
- Masterful execution of signature sfumato technique and complex optical rendering
- Presence of pentimenti in the benediction hand indicating original composition
- Status as an ultimate 'trophy asset' appealing to sovereign wealth funds and ultra-high-net-worth individuals

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
| **Estimate** | **$120.0M** | **$165.0M** |
| **Ratio** | 0.704x (under) | **0.968x** (fair) |
| **Confidence** | 0.95 | 0.95 |

**Image Only — model reasoning:**

> Based on a comprehensive visual analysis of the provided image, this artwork is an exceptional, museum-quality oil on canvas that can be confidently identified as a prime-period reclining nude by the Italian-born, Paris-based modernist master Amedeo Modigliani (1884–1920). The composition features a female figure lying horizontally, her arms folded behind her head, rendered against a boldly contrasting background of deep crimson and stark black or dark blue.   Stylistically, the painting is a textbook example of Modigliani’s mature visual vocabulary....

**Key factors cited:**

- Unmistakable attribution to Amedeo Modigliani's iconic 'Reclining Nude' series (c. 1916-1919).
- Extreme market scarcity of prime-period Modigliani nudes, most of which are in museum collections.
- Historical significance linked to the scandalous 1917 Galerie Berthe Weill exhibition.
- Signature stylistic elements: elongated forms, sculptural facial features, and bold color blocking.
- Precedent of recent auction comparables for similar works exceeding $150 million.

**With Metadata — model reasoning:**

> The artwork presented for appraisal is Amedeo Modigliani’s 'Nu couché', executed circa 1917-1918. This painting is not merely a masterpiece; it is a cornerstone of early 20th-century Modernism and represents the absolute zenith of the artist’s tragically brief career. The series of reclining nudes to which this canvas belongs was commissioned by Modigliani’s dealer and friend, Léopold Zborowski. When they were first exhibited at the Galerie Berthe Weill in Paris in 1917, they caused an immediate scandal and were shut down by the police on grounds of obscenity—a testament to their startling, unapologetic modernity and raw sensuality....

**Key factors cited:**

- Extreme scarcity of 1917-1918 Modigliani nudes remaining in private hands
- Monumental art historical significance and legendary 1917 exhibition scandal provenance
- Direct market precedents (2015 and 2018 sales exceeding $150 million)
- Iconic signature style featuring elongated forms and a rich, warm palette
- Status as a global 'trophy asset' with immense appeal to top-tier billionaire collectors

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
| **Estimate** | **$300.0M** | **$350.0M** |
| **Ratio** | 2.502x (over) | 2.919x (over) |
| **Confidence** | 0.95 | 0.90 |

**Image Only — model reasoning:**

> The artwork presented is immediately identifiable as Edvard Munch's "The Scream" (Skrik), specifically the 1893 version executed in tempera, oil, and pastel on cardboard. The signature and date "E. Munch 1893" are clearly visible in the lower-left corner. This piece is universally recognized as one of the most iconic and culturally significant images in the history of art, rivaling Leonardo da Vinci's "Mona Lisa" in its global recognizability and psychological impact.  Artistically, the composition is a masterclass in early Expressionism. Munch abandons realistic depiction in favor of profound psychological resonance....

**Key factors cited:**

- Iconic status as a globally recognized masterpiece of Expressionism
- Identification as the prime 1893 painted version of 'The Scream'
- Unprecedented cultural significance symbolizing modern existential anxiety
- Historical auction precedent of $119.9M set by the lesser 1895 pastel version in 2012
- Extreme scarcity of museum-grade foundational masterpieces on the open market

**With Metadata — model reasoning:**

> As an appraiser evaluating this submission, the first and most crucial step is to address a glaring discrepancy between the provided metadata and the visual evidence of the artwork itself. While the metadata explicitly describes the 1895 pastel version of Edvard Munch's 'The Scream'—noting it as the most colorful and the only one in private hands—the image provided is unequivocally the 1893 tempera and crayon on cardboard version. This is immediately identifiable by the specific textural qualities of the unprimed cardboard, the distinct application of the tempera, and most definitively, the visible signature and date 'E....

**Key factors cited:**

- Unparalleled global recognition and status as a universal cultural icon of existential dread
- Historical hierarchy: The image shows the definitive 1893 painted version, vastly superior in market desirability to the 1895 pastel
- Precedent of the 1895 pastel version selling for $119.9 million in 2012, adjusted for ultra-high-end market inflation
- Extreme scarcity of 'Mona Lisa-tier' masterpieces ever becoming legally available on the open market
- Fragility of the tempera and crayon on cardboard medium, requiring specialized conservation but acting as an authentic historical patina

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
| **Estimate** | **$250.0M** | **$250.0M** |
| **Ratio** | 3.030x (over) | 3.030x (over) |
| **Confidence** | 0.95 | 0.95 |

**Image Only — model reasoning:**

> Based on the visual evidence provided, this is undeniably Vincent van Gogh's masterpiece, 'Portrait of Dr. Gachet' (the first version, painted in June 1890). As an appraiser, encountering a work of this magnitude requires evaluating not just the physical object, but its monumental status within the Western art historical canon. Visually, the painting exhibits Van Gogh's mature, late-period style developed in Auvers-sur-Oise. The technique is characterized by highly expressive, undulating brushstrokes and a thick, sculptural impasto. The composition centers on Dr....

**Key factors cited:**

- Unquestionable authorship by Vincent van Gogh (Auvers-sur-Oise period, 1890)
- Iconic status as one of the most recognizable and famous portraits in global art history
- Exceptional Post-Impressionist execution featuring intense impasto and emotional resonance
- Immense historical significance, painted mere weeks before the artist's death
- Extreme scarcity of tier-one Van Gogh masterpieces available in the private market

**With Metadata — model reasoning:**

> The artwork presented for appraisal is Vincent van Gogh’s iconic Portrait of Dr. Gachet, specifically the first version painted in June 1890, distinguished by the presence of two yellow novels on the table. As an appraiser with decades of experience evaluating the world's most significant masterpieces, I can state unequivocally that this is one of the most important paintings in private hands, representing the absolute pinnacle of Post-Impressionist portraiture. Artistically, the work is a tour de force....

**Key factors cited:**

- Extreme rarity of late-period Van Gogh portraits on the open market
- Historical significance as one of the artist's final and most iconic masterpieces
- Exceptional artistic merit, characterized by dynamic impasto and profound psychological depth
- Historical auction record-holder (sold for $82.5 million in 1990)
- Unparalleled global brand recognition and demand among ultra-high-net-worth collectors

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
| **Estimate** | **$300.0M** | **$150.0M** |
| **Ratio** | 3.841x (over) | 1.921x (over) |
| **Confidence** | 0.98 | 0.90 |

**Image Only — model reasoning:**

> Based on a comprehensive visual analysis, the artwork presented is unequivocally Pierre-Auguste Renoir's magnum opus, 'Bal du moulin de la Galette' (Dance at Le moulin de la Galette), executed in 1876. This is not merely a painting; it is one of the foundational pillars of the French Impressionist movement and arguably among the most recognizable masterpieces in the Western art historical canon.   Artistically, the canvas is a tour de force of Impressionist technique. Renoir masterfully captures the vibrant, joyous atmosphere of a Sunday afternoon at the original Moulin de la Galette in Montmartre....

**Key factors cited:**

- Unquestionable attribution to Pierre-Auguste Renoir (1876)
- Apex masterpiece of the French Impressionist movement
- Revolutionary technical execution of dappled light and movement
- Iconic, globally recognized subject matter of Parisian leisure
- Extreme market scarcity for prime, large-scale Impressionist museum works

**With Metadata — model reasoning:**

> The artwork presented is Pierre-Auguste Renoir's 'Bal du moulin de la Galette' (1876), specifically the smaller of the two versions he painted of this iconic scene. As an appraiser, evaluating a work of this magnitude requires looking beyond standard metrics and entering the realm of ultra-rare 'trophy' masterpieces. This painting is not merely a work of art; it is a cultural artifact and a defining image of the French Impressionist movement. Artistically, the piece is a tour de force of Impressionist technique and philosophy. Renoir captures the vibrant, transient atmosphere of a Sunday afternoon at the Moulin de la Galette in Montmartre....

**Key factors cited:**

- Iconic status as a defining masterpiece of the 1870s French Impressionist movement
- Legendary auction provenance, having previously held the record for the most expensive painting ever sold ($78.1M in 1990)
- Exceptional execution of dappled light, color theory, and dynamic, modern Parisian subject matter
- Extreme rarity of a museum-quality, universally recognized composition of this caliber appearing on the open market
- Strong global demand for 'trophy' assets among ultra-high-net-worth collectors, comparable to recent $100M+ Impressionist sales

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
| **Estimate** | **—** | **$135.0M** |
| **Ratio** | N/A (—) | 0.571x (under) |
| **Confidence** | — | 0.92 |

**Image Only:** *No parseable response.*

**With Metadata — model reasoning:**

> Gustav Klimt's full-length society portraits are among the most coveted and historically significant masterpieces in the global art market, occupying a rarefied tier of valuation. 'Portrait of Elisabeth Lederer' (1914-1916) represents the absolute zenith of his late portraiture style. As an expert appraiser, I must first gently correct a minor historical nuance in the provided metadata: Serena Lederer was the wife of the industrialist August Lederer, while the subject of this painting, Elisabeth (later Baroness Bachofen-Echt), was their daughter....

**Key factors cited:**

- Extreme scarcity of finished, full-length Klimt portraits on the open market
- Exceptional provenance connected to his primary patrons, the Lederer family
- Spectacular visual appeal featuring highly sought-after East Asian decorative motifs
- Recent market comparables for late Klimt works exceeding the $100 million threshold
- Fascinating WWII-era historical backstory adding to the painting's aura and mystique

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
| **Estimate** | **$75.0M** | **$85.0M** |
| **Ratio** | **0.872x** (fair) | **0.988x** (fair) |
| **Confidence** | 0.95 | 0.90 |

**Image Only — model reasoning:**

> Upon rigorous visual examination, this artwork is unmistakably a prime example of Gustav Klimt’s mature landscape painting, a genre that constitutes some of the most highly coveted and art-historically significant works of the early 20th century. The piece immediately announces itself through its characteristic square format—a deliberate geometric choice Klimt adopted around 1899, often measuring exactly 110 by 110 centimeters. This format neutralizes traditional panoramic perspective, allowing the artist to flatten the picture plane and treat the canvas as a continuous, decorative surface rather than a window into a three-dimensional world....

**Key factors cited:**

- Unmistakable attribution to Gustav Klimt's highly coveted mature landscape period
- Characteristic square canvas format and radical flattened perspective
- Masterful Pointillist-inspired 'mosaic' brushwork and vibrant floral palette
- Extreme scarcity of major Klimt landscapes on the open market
- Strong auction comparables for similar works ranging from $50M to over $100M

**With Metadata — model reasoning:**

> The artwork presented for appraisal is Gustav Klimt’s 'Blumenwiese' (Blooming Meadow), circa 1908. This is an exceptional example of the artist’s celebrated landscape paintings, executed during his annual summer retreats to Lake Attersee in the Salzkammergut region of Austria. Klimt’s landscapes constitute roughly a quarter of his entire oeuvre and are among the most highly prized works in the global art market, offering a profound counterbalance to his formal society portraits and allegorical works. Artistically, 'Blumenwiese' is a masterpiece of early twentieth-century modernism....

**Key factors cited:**

- Gustav Klimt's highly coveted Attersee landscape series
- Signature square format and flattened, tapestry-like composition
- Execution during the artist's peak 'Golden Phase' (c. 1908)
- Vibrant, pointillist-inspired brushwork and mosaic-like color palette
- Strong market comparables for prime Klimt landscapes ranging from $50M to over $100M

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
| **Estimate** | **$42.0M** | **$34.0M** |
| **Ratio** | 0.670x (under) | 0.542x (under) |
| **Confidence** | 0.95 | 0.85 |

**Image Only — model reasoning:**

> Based on a rigorous visual examination of the provided image, this artwork is unmistakably an autograph painting by the Dutch Post-Impressionist master, Vincent van Gogh. The visual evidence points definitively to his Paris period, likely executed around 1887. The subject matter—a chaotic, dynamic pile of yellow-covered French paperback novels—is deeply characteristic of the artist's intellectual preoccupations during this era....

**Key factors cited:**

- Autograph work by Post-Impressionist master Vincent van Gogh (Paris period, c. 1887)
- Iconic use of impasto technique and vibrant, complementary color palette
- Subject matter holds deep biographical significance, representing his devotion to modern French literature
- Transitional stylistic elements showing the influence of Pointillism and Impressionism
- High global market demand for blue-chip Impressionist and Modern still lifes

**With Metadata — model reasoning:**

> Based on a meticulous visual examination of the provided image, the artwork presented is a quintessential example of Vincent van Gogh's Paris period, specifically identifiable as his 1887 composition 'Still Life with French Novels' (often cataloged as F358). It is important to note for the sake of strict accuracy that while the provided metadata title mentions 'roses dans un verre' (which corresponds to a sister painting, F359), the visual evidence here exclusively depicts the stacks of yellow-bound books on a patterned surface. My valuation is based strictly on the visual composition provided, assuming full authenticity and legal title....

**Key factors cited:**

- Authenticated 1887 Paris-period execution by Vincent van Gogh
- Transitional Post-Impressionist brushwork and signature use of yellow
- Extreme rarity of subject matter (one of approximately nine book still lifes)
- Deep biographical and intellectual significance regarding modern literature
- Severe market scarcity for museum-grade Van Gogh paintings

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
| **Estimate** | **$87.0M** | **$85.0M** |
| **Ratio** | 1.400x (over) | 1.367x (over) |
| **Confidence** | 0.95 | 0.92 |

**Image Only — model reasoning:**

> Based on the visual evidence presented, this artwork is an archetypal and monumental example of Abstract Expressionism, specifically belonging to the mature 'Color Field' period of Mark Rothko. The composition is famously reductive yet emotionally expansive, featuring two softly defined rectangular forms—a luminous, slightly translucent orange-terracotta block hovering above a denser, deeper crimson-red block—both suspended against a vibrant yellow ground. The technique visible here is the hallmark of the artist's genius....

**Key factors cited:**

- Unmistakable attribution to Mark Rothko's highly coveted mature Color Field period.
- Highly desirable vibrant palette (orange, red, yellow) which commands a massive market premium over darker works.
- Masterful execution of feathered edges and luminous color layering typical of the artist's absolute best work.
- Strong market precedent for similar masterpieces achieving $80M+ at top-tier contemporary evening sales.
- Apparent excellent condition with no visible pigment degradation, fading, or canvas compromise.

**With Metadata — model reasoning:**

> The artwork presented for appraisal is an exceptional example of Mark Rothko’s mature Color Field painting, titled 'No. 31 (Yellow Stripe)' and dated 1958. To evaluate a Rothko of this caliber, one must examine the intersection of its execution date, palette, technical mastery, and current high-end market dynamics. Historically and artistically, 1958 represents the absolute zenith of Rothko’s career. By this time, he had entirely abandoned the surrealist and multiform experiments of his early years, distilling his vision into the iconic format of stacked, hovering rectangles....

**Key factors cited:**

- Prime 1958 execution date during the artist's most critically and commercially successful period
- Highly coveted warm palette (red, orange, yellow) which commands the highest auction premiums for the artist
- Signature Color Field composition featuring floating, luminous rectangles with characteristic feathered edges
- Exceptional scale and visual impact, evoking the profound emotional resonance central to Rothko's philosophy
- Direct comparability to record-breaking Rothko sales such as 'Orange, Red, Yellow' ($86.9M) and 'No. 10' ($81.9M)

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
| **Estimate** | **$25.0M** | **$42.0M** |
| **Ratio** | 0.457x (under) | 0.768x (under) |
| **Confidence** | 0.95 | 0.95 |

**Image Only — model reasoning:**

> The artwork presented is unmistakably 'The Dream (The Bed)' (El Sueño), a seminal 1940 oil on canvas by the legendary Mexican artist Frida Kahlo. As an appraiser, encountering a work of this caliber on the open market is a generational event. The composition centers on a four-poster bed floating ethereally against a dynamic, cloudy sky. In the bed, the artist depicts herself in a state of deep sleep, shrouded in a vibrant yellow blanket from which leafy vines and roots emerge—a recurring motif in Kahlo's oeuvre symbolizing her profound connection to the earth, fertility, and the cyclical nature of life....

**Key factors cited:**

- Unquestionable attribution to Frida Kahlo, representing a major 1940 masterwork
- Extreme scarcity of prime-period Kahlo paintings on the international open market
- Deeply personal and iconic iconography including the bed, roots, and the Judas skeleton
- Exceptional provenance and cultural significance tied to Mexican heritage
- Recent market precedents for Kahlo's work easily exceeding the $30 million threshold

**With Metadata — model reasoning:**

> The artwork presented for appraisal is Frida Kahlo’s masterwork 'El sueño (La cama)' (The Dream (The Bed)), executed in 1940. Evaluating a piece of this magnitude requires recognizing that Kahlo is not merely a blue-chip artist; she is a global cultural icon whose works possess a level of extreme market scarcity and intense collector desirability that transcends traditional art market metrics. This specific painting is a profound encapsulation of Kahlo's central thematic preoccupations: mortality, physical suffering, her deep connection to the Mexican earth, and the permeable boundary between waking reality and the subconscious....

**Key factors cited:**

- Extreme scarcity of 1940s Frida Kahlo masterworks on the open market
- Iconic inclusion of signature motifs: self-portraiture, the bed, roots, and Mexican Judas figures
- Recent market precedent set by the $34.9M sale of 'Diego y yo' in 2021
- High global demand for blue-chip female artists and Surrealist-associated works
- Exceptional compositional complexity and deep biographical/psychological resonance

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
| **Estimate** | **$12.5M** | **$25.0M** |
| **Ratio** | 0.501x (under) | **1.002x** (fair) |
| **Confidence** | 0.95 | 0.98 |

**Image Only — model reasoning:**

> Based on a comprehensive visual examination, this artwork is unmistakably a major painting by the internationally acclaimed Japanese contemporary artist Yoshitomo Nara. The piece features his most iconic and commercially sought-after subject: a solitary, stylized young child—often referred to universally as the 'Nara girl'—rendered with disproportionate features, most notably an oversized head and piercing, almond-shaped eyes.   Nara's technique here is exemplary of his prime period, likely dating from the late 1990s to the early 2000s....

**Key factors cited:**

- Unmistakable attribution to Yoshitomo Nara
- Highly sought-after 'angry girl' iconic subject matter
- Premium medium (Acrylic on canvas) with visible masterful layering
- Prime period stylistic execution (late 1990s/early 2000s)
- Exceptional auction market demand for top-tier Superflat contemporary works

**With Metadata — model reasoning:**

> The artwork presented for appraisal is Yoshitomo Nara's undisputed masterpiece, "Knife Behind Back," executed in the pivotal year of 2000. To evaluate this piece is to engage with the absolute zenith of the artist's market and critical acclaim. Yoshitomo Nara is one of the most celebrated living contemporary artists, and his deceptively simple portraits of children tap into a profound well of universal psychological complexity, blending innocence with deep-seated angst, rebellion, and vulnerability.  Artistically, "Knife Behind Back" is a tour de force....

**Key factors cited:**

- Execution in 2000, a highly sought-after transitional period marking Nara's return to Japan
- Monumental scale and flawless execution of the artist's signature luminous acrylic layering technique
- Masterful subversion of 'kawaii' culture through implied psychological tension and menace
- Provenance as the artist's current world auction record holder (Sotheby's Hong Kong, 2019)
- Robust, sustained blue-chip contemporary market demand, particularly from elite Asian collectors

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
| **Estimate** | **$8.5M** | **$8.5M** |
| **Ratio** | **0.817x** (under) | **0.817x** (under) |
| **Confidence** | 0.95 | 0.92 |

**Image Only — model reasoning:**

> Based on a rigorous visual examination of the monumental canvas depicted in this studio setting, we are looking at a masterwork of contemporary painting. The artwork is characterized by its massive scale—likely exceeding 10 by 15 feet—and a highly visceral, aggressive application of paint. The composition is a striking dichotomy: the upper right quadrant is dominated by a vast, engulfing expanse of deep, resonant cobalt and lapis blue, creating a sense of void or cinematic backdrop. In stark contrast, the left and lower sections are a chaotic, heavily textured maelstrom of fleshy tones, earth colors, and sudden, vivid chromatic bursts....

**Key factors cited:**

- Monumental scale and commanding physical presence suitable for institutional or major private collections
- Signature synthesis of classical figuration and violent, scraped-paint abstraction
- Unequivocal identification with a top-tier, blue-chip contemporary artist (Adrian Ghenie)
- Presence of a distinct central figure, which commands a premium in the artist's market
- Robust auction comparables for works of similar size, period, and stylistic complexity

**With Metadata — model reasoning:**

> The artwork presented is 'Pie Fight Interior 12' (2014) by the celebrated Romanian contemporary artist Adrian Ghenie. To appraise this monumental canvas, one must evaluate the artist's current standing in the global market, the specific art-historical significance of the 'Pie Fight' series, the technical execution, and comparable auction records. Adrian Ghenie is undeniably one of the most successful and critically acclaimed painters of his generation, often associated with the 'Cluj School'....

**Key factors cited:**

- Monumental scale and visual impact
- Iconic 'Pie Fight' series subject matter
- Signature heavy impasto and scraping techniques
- Execution year (2014) aligning with peak critical acclaim
- Strong demand for the artist in global evening sales

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
| **Estimate** | **$4.5M** | **$10.7M** |
| **Ratio** | 0.419x (under) | **0.997x** (fair) |
| **Confidence** | 0.85 | 0.98 |

**Image Only — model reasoning:**

> Based on a comprehensive visual examination, the artwork presented overwhelmingly exhibits the signature visual vocabulary, technique, and conceptual framework of the internationally acclaimed contemporary artist Julie Mehretu. The composition is characterized by a highly complex, labor-intensive layering process that merges architectural drawing, mapping, and gestural abstraction. The substrate appears to feature a smooth, atmospheric ground—likely utilizing layers of acrylic or silica—upon which thousands of meticulous marks in ink and graphite have been applied. Visually, the piece is a tour de force of dynamic tension....

**Key factors cited:**

- Unmistakable visual attribution to blue-chip contemporary artist Julie Mehretu
- Signature complex layering of architectural vectors and organic gestural marks
- High international market demand for large-scale contemporary abstraction
- Excellent apparent condition with crisp line work and unblemished grounds
- Strong secondary market comparables frequently achieving multi-million dollar results

**With Metadata — model reasoning:**

> Julie Mehretu is undeniably one of the most critically acclaimed and commercially successful contemporary abstract painters working today. 'Walkers With the Dawn and Morning,' executed in 2008, stands as a quintessential and monumental example of her highly sought-after mid-career practice. To appraise this work, one must first examine its profound artistic merit and technical complexity. Mehretu's signature method involves building up the canvas with dozens of layers of acrylic paint, clear resin, ink, and graphite....

**Key factors cited:**

- Recent and definitive auction precedent (sold for $10.7M at Sotheby's in November 2023)
- Monumental scale and museum-quality execution
- Created during a highly coveted, peak period of the artist's career (2008)
- Signature layered technique combining architectural mapping and gestural abstraction
- Deep socio-political resonance, referencing the poetry of Langston Hughes

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
| **Estimate** | **$3.0M** | **$3.0M** |
| **Ratio** | 0.633x (under) | 0.633x (under) |
| **Confidence** | 0.95 | 0.90 |

**Image Only — model reasoning:**

> Based on a rigorous visual examination, this artwork is an exceptional example of contemporary mixed-media portraiture, overwhelmingly exhibiting the signature style, techniques, and thematic preoccupations of the internationally acclaimed Nigerian-American artist Njideka Akunyili Crosby. The composition centers on a remarkably rendered portrait of a young Black girl dressed in formal, western-style celebratory attire—likely a First Communion or flower girl dress, complete with ruffled sleeves, pink ribbons, white gloves, and a delicate veil....

**Key factors cited:**

- Unmistakable signature style of Njideka Akunyili Crosby, featuring acetone photo-transfer collage and highly rendered figurative painting.
- Visual evidence strongly aligns with the artist's highly acclaimed and sought-after 'The Beautyful Ones' portrait series.
- Exceptional historical market performance, with major comparable works by the artist routinely achieving between $2.5 million and $3.5 million at auction.
- Complex mixed-media technique that successfully bridges Western art historical traditions with contemporary African diaspora and transcultural narratives.
- High level of institutional validation for the artist, including major museum exhibitions and the MacArthur 'Genius' Grant, solidifying blue-chip status.

**With Metadata — model reasoning:**

> The artwork presented for appraisal is a seminal piece by Njideka Akunyili Crosby, hailing from her highly acclaimed series, 'The Beautyful Ones.' Executed in 2012, this work marks a critical period in the artist's career, coinciding with the development of her mature, signature style that would catapult her to international art market stardom. The series title adopts its name from Ayi Kwei Armah’s classic 1968 novel, 'The Beautyful Ones Are Not Yet Born,' and focuses on portraits of Nigerian youth—often family members—symbolizing the promise and complex identity of the postcolonial generation....

**Key factors cited:**

- Significance of 'The Beautyful Ones' series
- Signature acetone photo-transfer and mixed media technique
- Extreme scarcity of primary market supply driving secondary demand
- Strong historical auction comparables in the $2.5M - $3.5M range
- High institutional and critical acclaim (MacArthur Fellow)

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
| **Estimate** | **$2.5M** | **$3.8M** |
| **Ratio** | 0.365x (under) | 0.554x (under) |
| **Confidence** | 0.90 | 0.90 |

**Image Only — model reasoning:**

> The piece presented is a quintessential example of contemporary figurative painting, strongly exhibiting the hallmarks of 'Artificial Realism,' a term frequently used to describe the synthesis of traditional European Old Master painting with American Pop and cartoon culture. The visual vocabulary—specifically the psychological cubism, the fractured facial planes, and the juxtaposition of the grotesque with the classical—points unmistakably to the oeuvre of American contemporary artist George Condo. Evaluated purely on its visual merit and assuming authenticity, this work stands as a masterclass in contemporary figuration....

**Key factors cited:**

- Unmistakable 'Artificial Realism' style characteristic of George Condo
- Complex, multi-figure composition featuring highly sought-after archetypes (classical nudes, cartoonish grotesques)
- Strong, vibrant color palette with confident, expressive linework
- High market demand for contemporary psychological cubism
- Excellent apparent condition with intentional gestural elements

**With Metadata — model reasoning:**

> The artwork presented for appraisal is 'Force Field,' a quintessential 2010 canvas by the highly acclaimed American contemporary artist George Condo. Condo is internationally celebrated for his unique visual language, which he terms 'Artificial Realism' and 'Psychological Cubism.' This specific work is a masterful demonstration of his ability to synthesize the gravitas of Old Master portraiture and the fractured perspectives of European Cubism with the frenetic, low-brow aesthetics of American cartoon culture....

**Key factors cited:**

- Execution year (2010) aligns with peak critical acclaim and his New Museum retrospective
- Signature 'Psychological Cubism' style blending Old Master tropes with cartoon grotesquerie
- Highly desirable multi-figure composition, which commands a premium over single portraits
- Vibrant, complex execution characteristic of his sought-after 'Drawing Paintings' series
- Robust blue-chip contemporary market demand for Condo's large-scale canvases

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
| **Estimate** | **—** | **$160K** |
| **Ratio** | N/A (—) | 0.147x (under) |
| **Confidence** | — | 0.85 |

**Image Only:** *No parseable response.*

**With Metadata — model reasoning:**

> The artwork presented, "A.I. God: Portrait of Alan Turing" by Ai-Da Robot, occupies a fascinating and historically unprecedented space within the contemporary art market. As an appraiser, evaluating a physical artwork conceived and executed by an ultra-realistic humanoid robot requires a paradigm shift, moving beyond traditional metrics of human virtuosity to assess algorithmic complexity, conceptual resonance, and the rapidly evolving market for artificial intelligence in fine art. Artistically, the piece is a compelling study in fragmentation and the uncanny valley....

**Key factors cited:**

- Artist identity as a pioneering ultra-realistic humanoid robot (Ai-Da)
- High conceptual synergy between the AI artist and the subject, Alan Turing
- Current strong market appetite and premium for historically significant AI/algorithmic art
- Institutional validation of the Ai-Da project (Venice Biennale, United Nations)
- Provocative aesthetic combining digital fragmentation with physical, impasto-like execution

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
| **Estimate** | **$400K** | **$500K** |
| **Ratio** | **0.925x** (fair) | **1.156x** (over) |
| **Confidence** | 0.98 | 0.85 |

**Image Only — model reasoning:**

> Upon examining the artwork, it is immediately recognizable to any contemporary art market expert as 'Portrait of Edmond de Belamy' (2018), created by the French art collective Obvious. While the prompt asks to base the valuation on what is visible, the visual evidence here is highly specific and acts as an undeniable fingerprint. The image presents a heavily distorted, blurred portrait of a gentleman in what appears to be 18th or 19th-century attire—a dark coat with a stark white collar. However, the aesthetic is decidedly not human; it lacks brushstrokes, anatomical coherence, or traditional compositional intent....

**Key factors cited:**

- Historical primacy as the first AI artwork sold at a major auction house (Christie's 2018)
- Presence of the GAN mathematical formula serving as a conceptual signature
- Status as a seminal artifact representing the intersection of artificial intelligence and fine art
- Publicly documented realized auction price of $432,500 establishing a strong market comparable
- Ongoing art-historical relevance despite the rapid technical obsolescence of its specific algorithmic aesthetic

**With Metadata — model reasoning:**

> The artwork presented for appraisal is the highly celebrated 'Portrait of Edmond de Belamy,' created in 2018 by the Paris-based collective Obvious. This piece holds a singular, watershed position in the history of contemporary art and the art market: it is widely recognized as the first AI-generated artwork to be sold at a major international auction house. From a technical and aesthetic standpoint, the portrait was generated using a Generative Adversarial Network (GAN). The collective trained the algorithm on a dataset of approximately 15,000 portraits painted between the 14th and 20th centuries....

**Key factors cited:**

- First AI-generated artwork ever sold at a major international auction house (Christie's, 2018).
- Immense historical and cultural significance as the primary catalyst for the mainstream AI art market.
- Conceptual brilliance of utilizing the GAN loss function algorithm as the artist's signature.
- Insulated from recent AI art market saturation due to its unique 'first-mover' premium and status as a historical artifact.
- High desirability for major museums and institutional collections focused on the intersection of technology and 21st-century art.

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
| **Estimate** | **$850** | **$125K** |
| **Ratio** | 0.003x (under) | 0.451x (under) |
| **Confidence** | 0.65 | 0.82 |

**Image Only — model reasoning:**

> The artwork presented is a striking, highly detailed abstract composition characterized by undulating, organic forms and a granular, almost sand-like texture. The color palette is intensely vibrant, relying on the classic complementary pairing of cool cyans, teals, and deep blues against warm, earthy coppers, rust reds, oranges, and golds. This chromatic contrast creates a dynamic visual tension, drawing the viewer's eye across the sweeping, topographical ridges and valleys of the composition....

**Key factors cited:**

- Absence of known artist attribution or provenance
- High-resolution digital or macro-photographic medium
- Strong decorative appeal with complementary color palette
- Granular, topographical abstract composition
- Assumed format as an archival fine art print

**With Metadata — model reasoning:**

> As an appraiser evaluating Refik Anadol’s 'Machine Hallucinations - ISS Dreams - A' (2025), one must first acknowledge the artist's undisputed position at the vanguard of contemporary digital and AI-driven art. Anadol has successfully bridged the historical gap between generative digital art and blue-chip contemporary fine art. His recent monumental installations at institutions such as the Museum of Modern Art (MoMA) in New York and the Serpentine Galleries in London have provided him with the highest level of institutional validation, which directly translates to robust confidence and premium valuations in the secondary auction market....

**Key factors cited:**

- Artist's blue-chip status and recent major institutional validation (e.g., MoMA, Serpentine).
- High aesthetic appeal of the fluid, particle-based visual rendering and vibrant, contrasting color palette.
- Thematic resonance and market premium associated with space-exploration (ISS) datasets.
- Current strong auction demand for 'phygital' lots combining physical prints with blockchain-based digital twins.
- Historical significance of the 'Machine Hallucinations' series within the contemporary AI and generative art movements.

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
| **Estimate** | **$400** | **$25K** |
| **Ratio** | 0.004x (under) | 0.265x (under) |
| **Confidence** | 0.85 | 0.85 |

**Image Only — model reasoning:**

> Upon rigorous examination of the provided artwork, we are presented with a highly stylized, surrealist portrait that immediately commands attention through its bold palette and bizarre subject matter. The image depicts a central, seemingly female figure encased in a voluminous, heavily padded, metallic-green suit—reminiscent of a hybridized spacesuit, medieval armor, and a quilted sleeping bag. This rigid, synthetic attire is dramatically juxtaposed with an excessive, almost parasitic network of thick, bright orange braided hair that wraps around the torso, acts as a hood, and trails down to the ground....

**Key factors cited:**

- Lack of established provenance or artist attribution
- Strong visual indicators of AI or algorithmic generation
- Pop-surrealist aesthetic with high decorative appeal
- Structural inconsistencies in composition and anatomy
- Absence of traditional physical medium indicators

**With Metadata — model reasoning:**

> The artwork presented, titled "Embedding Study 1 & 2" (2024) by the acclaimed collaborative duo Holly Herndon and Mat Dryhurst, is a striking example of contemporary digital practice intersecting with artificial intelligence. Herndon and Dryhurst are pioneering figures in the realm of machine learning, data sovereignty, and generative art. Their work often interrogates the philosophical and ethical dimensions of AI, specifically how human identity, voice, and likeness are processed into data....

**Key factors cited:**

- Artists' pioneering status and institutional recognition in the AI and digital art space
- Conceptual depth regarding machine learning, latent space embeddings, and digital identity
- Striking hyper-surrealist aesthetic combining organic elements with synthetic AI textures
- Current market maturation and sustained demand for conceptually rigorous generative art
- Assumption of a unique, museum-quality physical format or 1-of-1 digital provenance

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
| **Estimate** | **$120K** | **$75K** |
| **Ratio** | 2.352x (over) | 1.470x (over) |
| **Confidence** | 0.95 | 0.92 |

**Image Only — model reasoning:**

> Based on the distinct visual and structural evidence presented in the image, this artwork can be confidently identified as a seminal piece of early Artificial Intelligence art, specifically Mario Klingemann's groundbreaking installation 'Memories of Passersby I' (circa 2018). The work is a multi-media installation comprising two digital screens, exposed cabling, and a mid-century modern wooden console cabinet. Artistically and historically, this is a museum-grade artifact from the dawn of the contemporary AI art movement....

**Key factors cited:**

- Pioneering use of Generative Adversarial Networks (GANs) in fine art
- Historical significance as an early, 'living' AI installation auctioned at a major house
- Artist's established reputation as a foundational figure in machine learning art
- Unique juxtaposition of mid-century physical hardware with real-time digital generation
- Rarity of self-contained, real-time generative algorithms presented as physical sculpture

**With Metadata — model reasoning:**

> As an appraiser evaluating Mario Klingemann’s 'Memories of Passersby I' (2018), we are examining a foundational masterpiece of the contemporary Artificial Intelligence art movement. Klingemann, recognized globally as a pioneer in the use of Generative Adversarial Networks (GANs), created this piece during a critical inflection point in the art market’s acceptance of machine-generated art. Unlike earlier, more rudimentary AI outputs that simply printed a static image onto canvas (such as the Obvious collective's 'Portrait of Edmond de Belamy'), Klingemann’s work is a self-contained, live AI computing entity....

**Key factors cited:**

- Pioneering status of the artist in the AI and GAN art movement
- Historical significance as the first autonomous AI installation sold at Sotheby's (2019)
- Technological complexity involving real-time, non-repeating generative output
- Aesthetic dialogue bridging Old Master portraiture and contemporary digital surrealism
- Physical manifestation of digital art through custom hardware and vintage casing that appeals to institutional collectors
