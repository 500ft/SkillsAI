---
name: layout-density-optimizer
description: This skill should be used when a card or container looks "barren", "empty", "unbalanced", "top-heavy", or "swimming in whitespace" — content pooling at the top of a big box with an accidental void below. It rebalances by redistributing existing elements (split-anchoring, fluid heights, tall→wide layout) and tuning vertical rhythm — WITHOUT adding filler text or decoration. Operates inside the boxes that bento-layout-generator defines (macro skeleton → this is the micro spacing).
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Layout Density Optimizer — balance, don't fill

A slide feels unfinished when short content pools at the top of a tall box and leaves an accidental void.
The fix is **redistribution**, not stuffing. This skill rebalances what's already there so the whitespace
reads as *intentional* — the Stoic look — instead of *leftover*.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`; routing:
`design-system/skill-interactions.md`. Locally `~/StoicDesign`; in Claude Design,
`github.com/500ft/StoicDesign`.

## The line you must not cross (restraint wins)

The source deck's failure was **wall-of-text**, not empty space. Stoic whitespace is a feature. So:

- **Never add filler** — no padding words, no invented bullet points, no decorative shapes, no oversized
  watermark icons, no low-opacity "AI hero" blobs to occupy a void. That re-creates the slop this repo
  exists to kill, and it fails **design-taste**.
- **"Barren" vs "calm":** content *pooled* leaving an accidental gap → rebalance. Whitespace *distributed*
  and deliberate → **leave it**. When unsure, fewer elements well-distributed beats more elements.
- Allowed grounding only: a **hairline rule** (already brand) or the **seal used sparingly** (§1). Nothing
  else from the "visual filling" playbook.

## Corrections (in priority order)

1. **Split-anchoring (preferred).** Keep the title at top, push supporting data/footnote to the bottom
   bound with Flexbox:
   ```css
   .card{ display:flex; flex-direction:column; justify-content:space-between; padding:32px; min-height:100%; }
   ```
2. **Fluid heights.** Replace hardcoded `height:500px` with `height:auto` / `min-height` + uniform
   padding, so the card shrinks to frame its content tightly and elegantly.
3. **Tall → wide.** If three short items sit in tall columns, convert to three **wide stacked rows** —
   horizontal layouts carry short copy without leaving vertical voids.
4. **Vertical rhythm.** Open the `gap` between kicker, title, and body so they span the height naturally;
   nudge body `line-height` to 1.5–1.6 (within the type scale) — *tasteful breathing*, not stretching.
5. **Proportional gaps over fixed.** Distribute space *between* elements rather than dumping it below them.

## The bento contract (macro × micro)

**bento-layout-generator owns the box; this skill owns the box's contents.** Bento sets each cell's span
and max size; this skill steps **inside** each cell to make cells of unequal text read as equal visual
weight — it tunes inner spacing and never resizes the grid or overflows the cell. Apply bento first, then
this. (Exact contract in `skill-interactions.md`.)

## Compose with siblings

Runs at the **micro-layout** layer (step 3 of the pipeline). After rebalancing, components fill in
(charts, timelines), then **design-legibility** and the **design-taste** gate confirm the result reads as
intentional, not padded.
