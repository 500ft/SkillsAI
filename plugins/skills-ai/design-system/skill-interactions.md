# Skill Interactions — how the StoicDesign skills compose

This file is the **referee**. Several skills touch the same surface (timelines, labels, density, motion).
Left undefined, an agent picks one arbitrarily and they fight. This map defines **who owns what**, **who
hands to whom**, and **which rule wins** when two overlap. Every skill links here; read it before
combining skills.

Golden rule: **`design-system/` always wins.** A skill's local rule never overrides a token, the
restraint ethos, or the anti-AI rules. Skills implement the system; they don't amend it.

---

## Macro → micro layering (the order to apply skills)

```
1. PLAN        slide-deck-builder → academic-pptx-skill → deep-planning      (sequence & titles)
2. MACRO LAYOUT bento-layout-generator / slide archetypes                    (the outer skeleton)
3. MICRO LAYOUT layout-density-optimizer                                     (inner spacing of each box)
4. COMPONENTS   data-viz-and-graphs · timeline-pin-mapper · timeline-and-shapes · explainer-graphic
5. LABELS       label-collision-preventer                                    (place dense labels safely)
6. MOTION       slide-animations-engine · cinematic-chart-animations         (reveal it)
7. SAFETY NET   design-legibility → design-repair                            (catch what slipped)
8. GATE         design-taste                                                 (score; SHIP or loop)
```

Apply outermost-first. A later layer never breaks an earlier one (density never overflows the bento
cell; labels never escape the chart frame; motion never moves text mid-read).

---

## Overlap resolutions (who owns the boundary)

### Timelines — `timeline-pin-mapper` vs `timeline-and-shapes`
- **timeline-and-shapes** — *evenly spaced* process maps, roadmaps, phase steps where the gaps carry
  **no real time scale**. Flexbox `space-between`, alternating above/below.
- **timeline-pin-mapper** — *chronological* timelines where **time gaps are meaningful and unequal**
  (history, evolution). Absolute `left:%` from a date→percent formula.
- **Decision:** real dates with uneven gaps → pin-mapper. Equal conceptual steps → and-shapes.
- **Handoff:** pin-mapper positions pins, then **label-collision-preventer** resolves any crowding, and
  **layout-density-optimizer** balances the content cards. Both share the node-styling rules in
  timeline-and-shapes (dot sizes, brand colors) so the two timeline types look like one family.

### Labels — `label-collision-preventer` vs `design-legibility`
- **label-collision-preventer** — *preventive, at build time.* Places dense data labels/annotations on
  charts and curves so they never collide (vertical offsetting, anchoring, clustering).
- **design-legibility** — *corrective, after layout.* Catches text occluded by images/shapes/footer or
  failing contrast anywhere on the slide, and relocates it.
- **Decision:** chart/curve annotation clusters → collision-preventer. Anything else, or a problem found
  after the fact → legibility. They are sequential, not competing: prevent first, then the net catches
  the rest.

### Density vs restraint — `layout-density-optimizer` vs the design system
- **The trap:** the source deck's failure was *wall-of-text*, not empty space. Stoic whitespace is
  **intentional**. So density-optimizer must **never add filler words, decorative shapes, or watermark
  icons to "fill" a slide** — that re-introduces AI slop and fails design-taste.
- **What it may do:** redistribute *existing* elements (split-anchoring `space-between`, fluid
  `min-height`, tall-card → wide-row), tune line-height/rhythm, and add **only brand-sanctioned**
  grounding (a hairline rule; the seal used sparingly per §1). Nothing else.
- **Decision:** "barren" = elements *pooled* leaving an accidental void → optimizer rebalances.
  "Calm" = intentional, distributed whitespace → **leave it**; restraint wins. When unsure, prefer
  fewer elements well-distributed over more elements.

### Bento × density — macro owns the box, micro owns its contents
- **bento-layout-generator** sets each cell's span and max size (the skeleton).
- **layout-density-optimizer** steps **inside** each cell to balance its contents so cells of unequal
  text feel like equal visual weight. It must respect the cell's bounds set by bento — it tunes inner
  spacing, never resizes the grid. (This is the exact macro/micro contract the user specified.)

### Motion — `cinematic-chart-animations` vs `slide-animations-engine`
- **slide-animations-engine** owns slide transitions + element reveals → calm `--ease`, 520–700ms.
- **cinematic-chart-animations** owns **chart/donut/radial draw-on only** → heavier `--ease-expo`,
  `--t-draw` (900–1200ms), the sanctioned exception in `design-system/§5`.
- **Decision:** a chart drawing itself = cinematic. Everything else on the slide = animations-engine.
  They run in one timeline: the chart draws (expo) while legend rows fade-in-up (calm) — different
  curves, same orchestration, no contradiction because each owns a disjoint set of elements.

---

## Shared invariants (every skill obeys, so combinations stay safe)

- **Tokens only** — colors/type/spacing/motion come from `design-system/`. No skill hardcodes a hex that
  isn't a token (the source pastes' `#D9A74A`, `#0A2540`, `#1E3A8A` map to `--data-gold`, `--navy`/`--ink`,
  `--wax`).
- **One accent per view; ≤3 data colors.** Holds no matter how many skills touch a slide.
- **Reduced motion + AA contrast + title-safe margins** are floors any skill can tighten, none can break.
- **design-taste is terminal.** Whatever the pipeline did, the gate scores it; a hard-gate failure loops
  back regardless of which skill "finished."

If two skills still appear to conflict on a real slide, that's a bug in this map — resolve it here, in
one place, not by forking a rule into a skill.
