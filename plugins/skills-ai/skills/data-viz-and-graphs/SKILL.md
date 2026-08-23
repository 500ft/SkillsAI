---
name: data-viz-and-graphs
description: This skill should be used when the user asks to "style this chart", "fix this graph", "make this data look good", "chart design", "data viz", or builds any graph/metric for a slide. It enforces the Stoic data-visualization rules — single brand accent, no rainbow, clean gridlines, direct labels, big metric callouts — using Chart.js or pure SVG/CSS.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Data Viz & Graphs — clean, on-brand charts

Default charts are the fastest way to make a deck look templated. This skill enforces the design
system's data-viz rules so every graph reads instantly and stays in the brand.

**Reads from the StoicDesign repo.** The canonical data-viz rules are
`design-system/stoic-design-system.md` §6 — this skill is their implementation layer. Companion script:
**csv-data-summarizer**. Locally `~/StoicDesign`; in Claude Design, `github.com/500ft/StoicDesign`.

## Palette & contrast

- **One dominant accent** for the primary series: `--wax` (`#2C49A6`). Outcomes use `--data-pos`
  (`#2F7D5B`) / `--data-neg` (`#B0492F`); context/baseline uses `--data-neutral` (`#7C8597`).
- **No rainbow.** For scale/intensity, use shades of a single hue, not multiple hues.
- The **reference/break-even line** is `--data-gold` (`#BE933A`), dashed. ≤3 series colors per chart.

## Typography & cleanliness

- **Remove vertical gridlines entirely;** keep horizontal gridlines faint (`rgba(25,35,58,.06)` on
  parchment / `rgba(243,237,225,.08)` on navy).
- **Bars:** square-editorial corners — radius `2px` (brand), not the soft 8px "AI" look. Consistent bar
  width and gap.
- **Direct-label series** at their ends; avoid detached legends. Labels never overlap — for dense or
  clustered callouts hand placement to **label-collision-preventer** (it owns label overlap); otherwise
  truncate, rotate long x-labels 45°, or use tooltips in interactive charts.
- Numbers in JetBrains Mono, `tabular-nums`.

## Metric callouts

- For a single headline stat, use a **Bento** callout (**bento-layout-generator**): a huge mono number
  (`--t-data`/`--t-display`) over a small Inter caption.

## Chart.js starter (themed)

```js
const brand = { wax:'#2C49A6', neutral:'#7C8597', gold:'#BE933A', ink:'#19233A', faint:'rgba(25,35,58,.06)' };
new Chart(ctx, { type:'bar',
  data:{ labels, datasets:[{ data, backgroundColor:brand.wax, borderRadius:2, borderSkipped:false }] },
  options:{ plugins:{ legend:{display:false} },
    scales:{ x:{ grid:{display:false}, ticks:{ color:brand.ink, font:{family:'Inter'} } },
             y:{ grid:{ color:brand.faint, drawBorder:false }, ticks:{ color:brand.ink, font:{family:'JetBrains Mono'} } } } } });
```

## Rules

- Build as inline SVG or themed Chart.js — never paste a default-Office chart image (**design-repair**
  replaces those).
- Annotate the *point* (mark the outlier / break-even / peak), add a `FIGURE n ·` kicker + mono source line.
- For a "draw-itself-in" donut/radial/line reveal, apply **cinematic-chart-animations** (it owns chart
  motion); dense labels go through **label-collision-preventer**. See `design-system/skill-interactions.md`.
- Final pass through **design-taste** (Data-viz dimension).
