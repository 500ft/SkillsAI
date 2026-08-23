---
name: label-collision-preventer
description: >-
  This skill should be used when the user plots close data points, callouts, or
  annotations that risk overlapping — "labels are colliding", "stagger these
  callouts", "bell curve with peaks at 1400/1450/1500", "percentile markers on
  a curve", dense scatter/line labels — or when building any chart with
  clustered labels. It applies collision-avoidance: dynamic vertical
  offsetting, adaptive anchoring, max-width wrapping, and clustering.
  Preventive at build time; design-legibility is the after-the-fact net.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Label Collision Preventer — dense labels that never overlap

When several callouts sit close along a curve or axis, fixed-height labels collide into mush. This skill
places them with deliberate offsets, anchoring, and (when truly dense) clustering — so every label reads.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`; routing:
`design-system/skill-interactions.md`; the offset algorithm: `references/collision-logic.md`. Locally
`~/StoicDesign`; in Claude Design, `github.com/500ft/StoicDesign`.

## This vs. `design-legibility`

Preventive vs. corrective. **This skill** places chart/curve annotation clusters correctly *as they're
built*. **design-legibility** is the slide-wide net that catches text occluded by images/footer or low
contrast *after* layout. Prevent here first; the net catches the rest. (See `skill-interactions.md`.)

## Rules

1. **Dynamic vertical offsetting** — never one fixed label height. When X-coords are within ~10%, stagger
   labels with **varying dashed-guide-line lengths** (short / tall / taller) so text blocks sit at
   different heights and clear each other.
2. **Adaptive anchoring to the curve trend** — if the curve slopes **down** to the right, place the label
   **above-right** of the dot; if points are extremely close, **alternate left/right** of the dot.
3. **Bounding-box constraints** — every absolute label has a strict `max-width` (≈120px) and `line-height`
   floor; keep a **16px** min safe-zone between adjacent label boxes.
4. **Smart wrapping** — prefer stacked multi-line (`≈94th pct` / `1400`) over long single lines to save
   horizontal room.
5. **Cluster + offload** — if points are mathematically too dense to separate, collapse them to one
   "Cluster" dot and **offload** the detail to a spacious caption/footnote under the baseline
   (`mean ≈ 1030 · most land 800–1300`).

## Brand styling (tokens)

Anchor dots `--data-gold`; dashed guide lines `--data-gold` at low alpha; meta text Inter `--ink-muted`;
value text **JetBrains Mono** `--wax` (the paste's `#1E3A8A` → `--wax`; `#D9A74A` → `--data-gold`;
`#6B7280` → `--ink-muted`). Tabular numbers always.

## Compose with siblings

Pairs with **data-viz-and-graphs** (which now delegates label overlap here), **timeline-pin-mapper**
(crowded pin clusters), and **cinematic-chart-animations** (labels fade-in-up *after* the chart draws, so
they never animate into a collision). Final gate: **design-taste**.

For the full vertical-offset algorithm, the anchoring decision table, and the HTML/CSS annotation-node
template, read `references/collision-logic.md`.
