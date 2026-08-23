# Anti-AI Rules — what makes a slide look "generated," and the fix

Grounded in a real teardown of `Ideal_Example.pptx` (Stoic Edu, Lesson 0.3, 19 slides). Each rule
names the **tell** found in that deck and the **fix** under this design system. The **design-taste**
skill scores against this list; **design-V0.1** must satisfy it before output.

> Mental model: "AI slop" is rarely one big mistake — it's the accumulation of *defaults left
> unchanged*. The fix is almost always **a decision where there was none**.

---

### 1. Default fonts → a real type system
- **Tell:** body text in **Calibri / Calibri Light** (the Office default) under a nice serif wordmark.
- **Fix:** Fraunces (display) + Inter (UI) + JetBrains Mono (numbers). Never ship Calibri, Arial,
  Times New Roman, or "Aptos." Real scale contrast between display and body.

### 2. Default Office palette → the brand data set
- **Tell:** charts in `#4472C4 / #ED7D31 / #70AD47 / #FFC000 / #A5A5A5` — a different color world
  from the navy/cream/wax brand. Two palettes fighting in one deck.
- **Fix:** one palette. Hero series `--wax`, outcomes `--data-pos` / `--data-neg`, reference line
  `--data-gold`. ≤3 series colors per chart.

### 3. One background, reused 19× → varied grounds
- **Tell:** the same full-bleed navy and cream "stoic" watermark behind every slide. Static wallpaper.
- **Fix:** alternate navy / parchment grounds by slide *type* (§7 of the system), vary composition
  and focal element. The watermark is decoration, not a layout.

### 4. Floating chart fragments → framed, labeled, annotated figures
- **Tell:** a lone curve + dashed line on pure white — no axes, no labels, no frame, no meaning.
- **Fix:** every chart gets a baseline, a domain, end-labels on series, a `FIGURE n ·` caption, a
  source line, and an annotation of the *point* (break-even dot + year).

### 5. Wall-of-text → one idea per slide
- **Tell:** slides 2, 4, 6, 12, 16 carry paragraphs — fine to read, wrong to **narrate over**.
- **Fix:** ≤ ~20 words of on-screen prose; the narration carries the rest. Reveal points one beat
  at a time. The calculator slide is the one sanctioned exception.

### 6. Generic decoration → none
- **Tells:** emoji-as-icons; purple-on-white gradient "AI hero"; glossy 3D blobs; stock "diverse
  team" photos; lorem ipsum; drop-shadow everything.
- **Fix:** hairline rules + whitespace; line icons only if needed; real content always (draft
  plausible copy/data, never placeholder).

### 7. Center-everything monotony → grid + hierarchy
- **Tell:** every element centered, one font at three nearby sizes, no asymmetry.
- **Fix:** use the 12-col grid; deliberate asymmetry; clear kicker → headline → support hierarchy;
  let type weight and size do the work.

### 8. Sloppy numbers → tabular mono, paired currency
- **Tell:** money in a proportional font, currencies formatted inconsistently.
- **Fix:** JetBrains Mono, `tabular-nums`; pair `₮ / $` consistently; round honestly and keep
  significant figures consistent across a slide.

### 9. Flashy transitions → calm cross-dissolve
- **Tell (PowerPoint default):** wipes, spins, "morph" abuse, push.
- **Fix:** 700ms cross-dissolve + 2% settle; staged reveals; honor `prefers-reduced-motion`.

---

## Quick gate (pass/fail before any deck ships)

- [ ] Zero Calibri/Arial/Times/Aptos anywhere.
- [ ] Zero default-Office chart colors; brand data set only.
- [ ] ≥2 distinct grounds used; no single background on all slides.
- [ ] Every chart framed + labeled + captioned + annotated.
- [ ] No slide over ~20 on-screen words except the documented dense slide.
- [ ] No emoji-icons, gradients-as-hero, 3D blobs, stock photos, lorem ipsum.
- [ ] Numbers in tabular mono with paired currency.
- [ ] Transitions are dissolve/reveal only; reduced-motion respected.
