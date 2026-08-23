# Occlusion Checks + Relocation Recipes

## Detection checklist

Run per slide; for each text run record anchor, box, z-order, background-behind.

- [ ] **Overlap** — does the text box intersect any higher-z element (image, shape, panel, seal)?
- [ ] **Safe-area** — is every edge inside the title-safe box (`--margin-x` 5vw, `--margin-y` 5vh)?
- [ ] **Spine** — does anything intrude into the bottom 56px (footer) or sit on the progress line?
- [ ] **Contrast** — does the text meet **AA** (≥4.5:1 body, ≥3:1 large ≥24px) against the *actual*
      pixels behind it, not the nominal ground? Sample the darkest/lightest region it covers.
- [ ] **Clipping** — is any glyph cut by `overflow:hidden`, a fixed height, or the canvas edge?
- [ ] **Crowding** — is there <8px (≥`--s1`) of clear space to the nearest element? Treat as a soft hit.

## Relocation — order of preference

Keep the text near what it means. Try in this order; stop at the first that clears all checks:

1. **Nudge in place** — move within the same grid cell by a spacing step (`--s2`..`--s5`) to clear the
   collision.
2. **Adjacent free cell** — shift to the nearest empty cell on the grid, same row/column band.
3. **Re-anchor to the object** — place on the labeled object's open side (a series' end, a bar's top),
   with a hairline leader line if the link isn't obvious.
4. **Last resort: reflow the slide** — if nothing is free, the slide is overfull → flag for design-V0.1
   to split or reduce (it likely also violates the ≤20-word rule).

Never move a label more than necessary; never break reading order (top-left → down/right).

## Treat-the-background recipes (when moving isn't ideal)

- **Brand scrim** — a panel behind the text in `--parchment-panel` / `--navy-panel`, or the ground at
  86–94% alpha with a 1px hairline. Sized to the text + `--s3` padding. Calm, on-brand, no blur glow.
- **Token swap** — switch text to `--cream` on dark regions / `--ink` on light; re-check AA.
- **Demote the image** — scale or crop the image so the text occupies clear negative space; the image
  rarely needs to be full-bleed where a label lives.
- **Hairline plate** — for a single number/callout, a small bordered chip (`--rule-*`, radius 2px)
  reads as intentional, not patched.

Avoid: drop shadows, outer glows, text outlines/strokes, or semi-transparent black boxes — these read
as "fixed in a hurry" and break the Stoic restraint.

## Verify

After any fix: re-run the checklist on the moved element **and** anything it now sits near. Confirm AA
with the new background. Then return to design-taste for the craft score.
