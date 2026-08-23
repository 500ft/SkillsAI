# Repair Playbooks

## AI image tells → fix

| Tell | Fix |
|---|---|
| Warped hands / extra fingers / fused limbs | regenerate (hands are structural); or crop out; or inpaint |
| Asymmetric / uncanny faces, wrong eyes | regenerate with a tighter prompt; avoid implying a real person |
| Gibberish text, fake logos on signs/books | regenerate with "no text"; or crop/blur the region; never leave fake words |
| Plastic, over-smooth skin / HDR sheen | desaturate ~10–20%, lower micro-contrast/clarity, add grain |
| Over-saturated teal-orange grade | regrade toward brand temperature (navy/cream), pull saturation |
| Melted/illogical background geometry | crop to a clean region; shorten depth of field; regenerate |
| Generic stock composition (centered, symmetric) | recompose to rule-of-thirds; off-center the subject |
| Floating subject with no ground | add a ground/shadow or place on a brand panel with a hairline frame |

## De-slop pipeline (ordered)

1. **Triage:** structural tell (hands/face/text) → regenerate; cosmetic tell (grade/sheen/comp) →
   post-process the existing image.
2. **Crop & recompose** to 3:2 or 16:9, subject off-center.
3. **Grade to brand:** color temperature toward `--navy`/`--cream`; saturation −10–20%; highlights
   tamed; blacks lifted slightly to match parchment, not crushed.
4. **Texture:** add fine film grain or paper tooth (low opacity) — defeats the plastic-clean look.
5. **Integrate:** hairline frame, or duotone toward `--wax` when the image must live on navy/parchment;
   match edges to the ground.
6. **QA:** zoom to 100% on hands, eyes, text, edges. No fabricated data, no implied real individuals.

Tools: ImageMagick / Pillow for crop, grade, grain, frame when available; otherwise regenerate with the
corrected prompt below. Save de-slopped assets beside the deck, not over the original.

## Non-AI image prompt recipe (for imagegen)

Build prompts from **specific photographic/illustrative facts**, not slop adjectives:

- **Subject + action + setting**, concrete and singular.
- **Optics:** lens + distance ("85mm portrait," "35mm environmental"), aperture/DOF.
- **Light:** named, directional ("soft north-window light," "low afternoon sun"), not "cinematic."
- **Palette:** name the brand colors ("muted navy and cream, restrained, low saturation").
- **Medium:** if illustration, name a real register ("engraving line work," "risograph," "matte gouache").
- **Negatives:** `no text, no logos, no watermark, no extra fingers, not hyperreal, not HDR, not
  oversaturated, not 3D render, no lens flare`.
- **Avoid:** "trending on artstation," "8k ultra detailed," "masterpiece," "award-winning" — these pull
  toward the slop average.

## Chart / graph rebuild (don't retouch — replace)

Rebuild as inline SVG to the design system §6: framed baseline + minimal ticks; brand palette only
(hero `--wax`, outcomes `--data-pos`/`--data-neg`, reference line `--data-gold` dashed); series
**end-labeled**, no detached legend; the *point* annotated (break-even dot + year); `FIGURE n ·`
caption + mono source line. Reuse the chart pattern in `design-V0.1/assets/deck-template.html`.

## Shape / diagram repair

- Snap nodes to the grid; equalize stroke widths; remove stray/duplicate paths and open sub-paths.
- Smooth jagged hand-traced curves (simplify points; consistent bézier tension) — unless a deliberate
  engraving/woodcut texture is the intent.
- Brand corner radii (square default; 2px chips; 999px only seal/pills); hairline rules, no heavy shadow.
- If the diagram is conceptually weak, get a stronger structure from **design-creativity**, then redraw
  (an Excalidraw schematic is fine for mechanism/flow).
