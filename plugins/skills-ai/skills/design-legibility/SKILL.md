---
name: design-legibility
description: This skill should be used when the user says "the text is covered / hidden / behind the image", "fix the overlapping text", "this label is on top of something", "text is cut off / clipped / off the slide", "the number is under the footer", "I can't read this", "check legibility", or "nothing should be hidden". It detects text that is occluded, clipped, off-safe-area, or low-contrast against what is behind it, and relocates it to the nearest readable position that stays near its intended spot — without breaking the grid or the brand. It is invoked automatically by design-taste / design-V0.1 when occlusion is found.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Design Legibility — nothing important hidden

A slide that plays under a voiceover must read instantly. If a label sits behind an image, a number
slips under the footer, or text falls outside the title-safe area, the slide fails silently. This
skill finds those cases and **moves the text to the nearest readable place that keeps its meaning** —
close to what it labels, on the grid, in the brand.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`
(title-safe margins, grid, contrast floor); checks + recipes: `references/occlusion-checks.md`.
Locally the repo is usually `~/StoicDesign`; in Claude Design, read it from `github.com/500ft/StoicDesign`.

## What counts as an occlusion

1. **Overlap** — text under a higher-z element (image, shape, panel, the seal).
2. **Off-safe-area** — text outside the title-safe box (`--margin-x` / `--margin-y`) or off-canvas.
3. **Spine collision** — text under the footer bar or the progress line (bottom 56px).
4. **Low contrast** — text whose color fails WCAG AA against the actual pixels behind it (dark text on
   a dark photo region, cream on parchment, etc.).
5. **Clipping / truncation** — text cut by a container, overflow hidden, or a fixed-height box.

## Procedure

1. **Inventory** every text element: its anchor (what it labels / where it's meant to be), bounding
   box, z-order, and the background actually behind it.
   - HTML deck: read computed layout/CSS (positions, z-index, overflow) — don't guess from source order.
   - Image/screenshot: look; locate each text run and judge contrast and overlap by eye.
2. **Detect** against the five cases above. Record each hit with evidence (element, problem, the box it
   collides with).
3. **Relocate, staying near intent.** For each occlusion, find the nearest position that is on the grid,
   inside the title-safe area, clear of higher-z elements and the spine, and meets AA contrast — while
   staying as close as possible to the original anchor and preserving reading order. Prefer, in order:
   nudge within the same cell → move to the adjacent free cell → re-anchor to the labeled object's open
   side. Never fling a label across the slide.
4. **When moving isn't right, treat the background instead** (see recipes): drop a brand scrim/panel
   (`--parchment-panel` / `--navy-panel` or a low-alpha ground) behind the text, switch the text token
   (`--ink`↔`--cream`) for contrast, or shrink the image so the text has clear space. Keep one accent,
   keep hairlines — no glows or heavy shadows to force contrast.
5. **Re-verify** the fix introduced no new overlap or contrast failure, then pass back to design-taste.

## Output

```
LEGIBILITY — <slide N>
1. [overlap] "Mech eng → Detroit" label sits under the chart line at x≈120
   → move 24px up into the open upper-left cell (still beside its series). AA ok on navy.
2. [spine] "$19K/yr" callout overlaps the footer
   → raise into the content row; 48px clearance from the 56px footer.
3. [contrast] caption #19233A over a dark photo region (ratio 2.1)
   → add a --parchment-panel scrim at 92% behind the caption (ratio 9.4). Anchor unchanged.
```

## Boundaries

- This skill moves and reframes **text/elements**; it does not redraw artwork. If the *background image
  itself* is the problem (baked-in text, a busy region that can't host a label), hand off to
  **design-repair**.
- It never changes the message, the type system, or the palette — only position, contrast treatment,
  and container.
- **This vs. `label-collision-preventer`:** that skill *prevents* dense chart/curve labels from colliding
  at build time; this skill is the *corrective* net for text occluded by images/footer or low contrast
  after layout. Prevent there first; this catches the rest. (`design-system/skill-interactions.md`.)

For the detection checklist, the relocation order-of-preference, and the scrim/contrast recipes, read
`references/occlusion-checks.md`.
