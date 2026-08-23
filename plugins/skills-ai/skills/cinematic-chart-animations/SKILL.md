---
name: cinematic-chart-animations
description: This skill should be used when the user wants a chart to "draw itself in", a "buttery"/"premium" donut or radial reveal, "animate the ring clockwise", "stroke-dasharray chart animation", or sequential segment/legend reveals for circular charts. It enforces high-performance SVG stroke animations (clockwise from 12 o'clock, easeOutExpo) for donut/pie/radial charts — the one sanctioned heavier-motion exception in the Stoic system.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Cinematic Chart Animations — charts that draw themselves

A donut that fades or pops in looks cheap; one that strokes itself clockwise with heavy easing looks
premium. This skill owns that motion — and only that. It is the **sanctioned exception** to Stoic's
otherwise-calm motion, because a chart drawing itself *is* the focal moment, not a background transition.

**Reads from the StoicDesign repo.** Motion authority: `design-system/stoic-design-system.md` §5 (the
`--ease-expo` / `--t-draw` tokens live there); routing: `design-system/skill-interactions.md`; static
chart styling: **data-viz-and-graphs**. Locally `~/StoicDesign`; in Claude Design,
`github.com/500ft/StoicDesign`.

## Scope (so it never fights slide-animations-engine)

This skill animates **charts only** (donut/pie/radial, and chart line draw-on). Slide transitions and
element reveals stay with **slide-animations-engine** on the calm `--ease` timing. In one timeline they
coexist: the ring draws on `--ease-expo` while the legend rows fade-in-up on `--ease` — disjoint elements,
no contradiction. (Referee: `skill-interactions.md`.)

## 1. Clockwise stroke reveal (the 12 o'clock rule)

- Rotate the SVG so 0% sits at top center: `transform: rotate(-90deg); transform-origin: center;`.
- Draw with `stroke-dasharray` / `stroke-dashoffset`: init offset = path length, transition to `0`.
- Easing + duration from the tokens — **never** linear or plain ease-in-out:
  ```css
  .ring{ will-change: stroke-dashoffset; transition: stroke-dashoffset var(--t-draw,1100ms) var(--ease-expo); }
  ```

## 2. Staggered segments

Multi-segment donuts (e.g. Required ~54% / Optional ~38% / Blind ~8%) draw **sequentially**, ~`0.15s`
offset, not all at once. Scale each segment's duration roughly to its arc length so the *angular speed*
feels uniform — the small 8% slice draws proportionally faster, so the pen appears to move at one pace
around the ring.

## 3. Legend reveal, synced

As the ring draws, stagger the legend rows in with a compact fade-in-up (`translateY(15px); opacity:0`),
delays `0.4s / 0.5s / 0.6s`, on the calm `--ease`. Hand dense legend/label placement to
**label-collision-preventer** so rows never reveal into a collision.

## 4. Performance + accessibility

- `will-change: stroke-dashoffset, transform;` on the animated paths to force GPU compositing (no
  micro-stutter on weak presentation hardware).
- **Honor `prefers-reduced-motion`** → render the chart in its final state instantly (no draw). This is a
  floor from the design system, not optional.
- In Reveal.js, trigger on slide-active (`Reveal.on('slidechanged', …)` or a fragment) so the draw starts
  when the slide appears, not on page load.

## Compose with siblings

Build the static chart per **data-viz-and-graphs** (brand palette, framing), then apply this motion;
place labels via **label-collision-preventer**; gate with **design-taste**. The reference line still fades
in first, per §5.
