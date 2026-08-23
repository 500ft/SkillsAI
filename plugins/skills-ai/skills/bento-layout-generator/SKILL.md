---
name: bento-layout-generator
description: This skill should be used when the user asks for a "bento layout", "bento box grid", "modular grid of metrics/cards", "dashboard of stats", or wants to frame several data points, metrics, or images in a clean modular grid. It produces a Modernist bento grid harmonized to the Stoic design system (hairline borders, brand panels, one accent, tabular numbers).
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Bento Layout Generator — modular grids, Stoic-styled

A bento grid frames several items as one composition: cells of varying size on a tight grid, each
holding one metric, statement, or image. Done right it reads as deliberate and modern; done generic it
reads as a template. This skill enforces the deliberate version in the brand.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`
(tokens, grid, hairlines, tabular numbers). Locally `~/StoicDesign`; in Claude Design,
`github.com/500ft/StoicDesign`.

## Rules

- **Tight modular grid**, varied cell spans, consistent gutter (`--s4`/`--s5`). One **hero cell** per
  bento (the most important metric), sized larger.
- **Cells:** `--parchment-panel` / `--navy-panel` ground, **1px hairline** (`--rule-*`), radius `2px`
  (square-editorial — not the soft 16px "AI bento" look). No drop shadows.
- **One accent** (`--wax`) for the hero number/emphasis; everything else ink/cream + muted.
- **Numbers** in JetBrains Mono, `tabular-nums`; a metric cell = huge mono number + small Inter caption
  beneath (the "massive stat" pattern).
- Images in cells are cropped to fill, hairline-framed; de-slop via **design-repair** if AI-generated.

## CSS recipe

```css
.bento{display:grid; grid-template-columns:repeat(12,1fr); gap:var(--s5,24px)}
.cell{background:var(--parchment-panel); border:1px solid var(--rule-ink); border-radius:2px;
      padding:var(--s5,24px); display:grid; align-content:space-between}
.cell.hero{grid-column:span 6; grid-row:span 2}
.cell.wide{grid-column:span 6}  .cell.std{grid-column:span 3}
.cell .stat{font:500 clamp(40px,6vw,84px)/1 var(--font-mono); font-variant-numeric:tabular-nums;
            color:var(--wax)}
.cell .cap{font:500 13px var(--font-ui); letter-spacing:.04em; color:var(--ink-muted)}
```

(On navy, swap `--parchment-panel`→`--navy-panel`, `--rule-ink`→`--rule-cream`, captions→`--cream-muted`.)

## Use

Map 4–8 items to cells; assign the hero; balance spans so the grid has no ragged gaps. Keep one idea
per cell — a bento is many one-idea units composed, not a place to escape the word budget.

**Macro × micro:** this skill owns the **outer** grid (cell spans and sizes). For the spacing **inside**
each cell — short content pooling at the top, uneven visual weight between cells — hand off to
**layout-density-optimizer**, which balances within the bounds this grid sets (never resizing the grid).
Apply bento first, then the optimizer. Contract: `design-system/skill-interactions.md`. Finish with
**design-taste** (Layout / Craft).
