---
name: design-repair
description: This skill should be used when the user says "this image looks broken / AI / warped", "the hands / faces / text in the image are messed up", "make this image cleaner / less AI-generated", "de-slop this", "fix this graph / chart", "smooth out this shape", "this shape is malformed / off", or "repair this visual". It diagnoses broken or AI-looking visuals (raster images, charts/graphs, vector shapes) and either smooths/fixes them or rebuilds them in the Stoic design system, drawing concepts from design-creativity. It is invoked by design-V0.1 / design-taste when a visual is broken or derivative.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Design Repair — fix broken or AI-looking visuals

Two failure modes make a deck look cheap: visuals that are **broken** (warped AI images, malformed
charts, off shapes) and visuals that are **derivative** (technically fine, obviously generated). This
skill fixes both — preferring to **rebuild in the design system** when the asset is code, and to
**de-slop** when it's a raster image worth keeping.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`
(data-viz rules, palette); concepts: the **design-creativity** skill; playbooks:
`references/repair-playbooks.md`. Locally the repo is usually `~/StoicDesign`; in Claude Design, read
it from `github.com/500ft/StoicDesign`.

## Step 1 — Classify the asset

- **Chart / graph** → almost always **rebuild** as inline SVG in brand colors (framed, end-labeled,
  annotated, captioned). Never retouch an Office-palette chart PNG — replace it.
- **Vector shape / diagram** → fix geometry in code (align to grid, repair paths) or rebuild.
- **AI raster image** (portrait, scene, texture) → **de-slop** (Step 3), or regenerate then de-slop.

## Step 2 — Diagnose (specific, not "looks off")

Name the exact defects (full per-type checklists in the playbooks):
- **AI image tells:** warped hands/ears/eyes, asymmetric faces, gibberish text, plastic/over-smooth
  skin, HDR sheen, impossible geometry, melted backgrounds, over-saturation, generic "stock" comp.
- **Chart faults:** Office colors, no axes/labels, detached legend, distorted aspect, no annotation,
  missing source — i.e. the §6 data-viz rules unmet.
- **Shape faults:** off-grid, misaligned nodes, stray/again-overlapping paths, inconsistent stroke,
  non-brand corner radii.

## Step 3 — Repair

**Rebuild (code assets — preferred, deterministic):** redraw the chart/shape per the design system.
If the underlying *idea* is weak, get a stronger concept from **design-creativity** first — don't
cleanly render a bad idea.

**De-slop (raster images):** run the ordered pipeline (see playbooks):
1. **Regenerate** with a better prompt if the tell is structural (hands/text/faces) — imagegen system
   skill, with the non-AI prompt recipe.
2. **Crop** out the worst tells; recompose to rule-of-thirds.
3. **Grade to brand** — pull color temperature toward navy/cream, desaturate ~10–20%, tame highlights
   to kill the HDR sheen.
4. **Add texture** — subtle film grain / paper tooth so it doesn't read as plastic-clean.
5. **Integrate** — match the ground, add a hairline frame or duotone toward `--wax` if it must sit on
   navy/parchment.
6. **Fix residue** — inpaint/regenerate extra fingers, artifacts, or watermarks; if unfixable, crop or
   obscure.
Use ImageMagick/Pillow for crop/grade/grain when available; otherwise regenerate with the corrected
prompt. Keep edits honest — never fabricate data or faces that imply real people.

## Step 4 — Re-check

Pass the result to **design-taste** (Data-viz / Craft / Brand dimensions). If repair moved or
re-grounded any text, run **design-legibility**. Re-score only what changed.

## Output

```
REPAIR — <asset>
Type: AI raster (portrait)   Decision: regenerate + de-slop
Defects: warped left hand; HDR skin sheen; teal/orange grade off-brand; gibberish on book spine.
Actions: 1) regen with non-AI recipe (85mm, soft window light, no text) 2) crop to 3:2
  3) grade toward navy, -15% sat 4) +film grain 5) hairline frame on parchment.
Result: <path / new asset>   Re-score: Data-viz n/a · Craft 4 · Brand 4 — SHIP.
```

For the AI-tell table, the de-slop pipeline details, the non-AI prompt recipe, and chart/shape rebuild
rules, read `references/repair-playbooks.md`.
