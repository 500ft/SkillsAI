# Stoic Taste Rubric

Eight dimensions, 0–5 each (40 total). Score with cited evidence. **Any dimension ≤2 fails the hard
gate** regardless of total — a deck that scores 30/40 but sets body type in Calibri still ships
looking AI.

Anchors are given for 0, 3, and 5. Score 1/2/4 by interpolation.

---

### 1. Typography  *(carries most of the "expensive" feeling)*
- **0** — Calibri/Arial/Times/Aptos; one font at three nearby sizes.
- **3** — correct families (Fraunces/Inter/JetBrains Mono) but weak scale contrast or wrong weights.
- **5** — full system: Fraunces display with tracking, Inter kickers uppercase-tracked, JetBrains
  Mono tabular numbers; clear display-vs-body contrast.

### 2. Color discipline
- **0** — default Office palette; ≥3 unrelated hues; two color worlds fighting.
- **3** — mostly brand, but an off-palette accent or chart color slips in.
- **5** — one palette, one accent per slide, ≤3 data series colors, gold reserved for the reference line.

### 3. Layout & grid
- **0** — everything centered; no grid; no hierarchy; no spine.
- **3** — grid present, spine (footer/kicker/number) present, but timid or symmetric throughout.
- **5** — deliberate 12-col composition, asymmetry with intent, clear kicker→headline→support hierarchy.

### 4. Restraint / narrate-over fit  *(the Stoic-specific one)*
- **0** — wall of text; the slide reproduces the script; multiple ideas competing.
- **3** — one idea, but ~30–40 words or two competing focal points.
- **5** — one idea, ≤~20 on-screen words, staged so each reveal maps to a narration beat.

### 5. Data-viz craft
- **0** — floating chart fragment on white; no axes/labels; Office colors; no caption.
- **3** — framed and labeled, but a detached legend, missing annotation, or no source line.
- **5** — framed, end-labeled series, brand palette, gold reference line, `FIGURE n ·` caption,
  source line, and the *point* annotated (break-even dot + year).

### 6. Motion
- **0** — PowerPoint wipes/spins/morph; or motion that fights the voiceover.
- **3** — fades present but untimed or no `prefers-reduced-motion`.
- **5** — 700ms dissolve + 2% settle, staged reveals on the beat, count-ups, reduced-motion honored.

### 7. Brand identity
- **0** — no Stoic signal; could be any template; hype voice.
- **3** — palette/type on-brand but emblem/wordmark/voice underused or off.
- **5** — seal used correctly (title/divider/close only), Fraunces wordmark, calm exact voice, the
  page "feels like a serious book."

### 8. Craft details
- **0** — misaligned, ad-hoc spacing, proportional-font numbers, drop-shadows everywhere.
- **3** — mostly aligned, spacing on the scale, but a few off-grid or inconsistent details.
- **5** — pixel-aligned to the grid, spacing strictly from the scale, tabular paired-currency numbers,
  hairlines instead of shadows.

---

## Verdict bands

| Total | Hard gate | Verdict |
|---|---|---|
| 34–40 | all ≥3 | **SHIP** |
| 26–33 | all ≥3 | **FIX FIRST** — address top fixes, re-score |
| any | any dimension ≤2 | **FIX FIRST** — gate failure overrides the total |
| ≤25 | — | **REWORK** — return to design-V0.1 / design-creativity |

## Scoring discipline

- Cite evidence per score (the actual font, hex, word count, element).
- Prefer the lower score when on the boundary — taste is a high bar.
- Re-score only the changed dimensions after a fix; don't re-litigate the whole deck.
