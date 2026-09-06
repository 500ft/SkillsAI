---
name: figure-regeneration-audit
description: This skill should be used when the user asks "does this figure still regenerate", "audit the figures", "is this plot stale", "check the committed PNGs against the script", "regenerate from the manifest", or wants to know whether committed figures reproduce from their committed data and scripts.
---

# Figure regeneration audit

Decide, for every committed figure, whether it reproduces from the committed generator — and
when it does not, whether the difference is data or rendering. Wrong answers in both
directions are common and were both made during the audit this skill is extracted from.

## Procedure

1. **Pristine tree.** `git archive HEAD | tar -x -C <scratch>`. Never copy the working tree —
   it carries the committed images into the scratch dir and produces a false pass. Set
   `GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null` or `git archive` can silently
   produce nothing under a sandboxed home.
2. **Delete the expected outputs** before running, so a match cannot be a leftover.
3. **Match the renderer.** Read `Software` from the PNG metadata (`scripts/regen_audit.py`
   prints it). A figure rendered by matplotlib 3.8 will never byte-match one from 3.10; build
   the environment the figure was made in before calling anything drift.
4. **Run the manifest command** with its declared prerequisites (`PYTHONPATH`, `MPLBACKEND=Agg`,
   editable install). If the manifest does not state them, that is a finding.
5. **Compare in this order, stopping at the first decisive result:**
   - byte-identical → `BYTE_IDENTICAL`, done.
   - the generator writes a numeric artifact (JSON/CSV) → diff **that**, with a relative
     tolerance (`1e-9` is wide enough for BLAS reassociation and ~1e6 tighter than anything
     physical). If the numbers agree, the figure agrees; report `RENDER_ONLY`.
   - otherwise pixel-diff, **localised by position** (`scripts/pixel_localize.py`).
6. **Localising a pixel diff.** Split rows into text bands vs axes interiors (find the axes
   frame as the dark rectangle). Count differing pixels inside the axes. Check whether any
   differing pixel carries a data-line colour. Zero inside the axes and zero data-coloured =
   glyph rasterisation (font build), not data.
7. **But:** when the layout depends on text extents, a font-metric shift moves the axes edge by
   a few pixels and rescales every curve — thousands of *data-coloured* pixels differ with no
   data change. Check the axes-frame position in both images; if it moved, only the numeric
   output is decisive.

## Verdicts

`BYTE_IDENTICAL` · `RENDER_ONLY` (numbers agree, pixels differ) · `NUMERIC_DRIFT` (report worst
relative difference and the key) · `FAILED_RUN` · `NOT_PRODUCED` · `NO_GENERATOR`.

## Mistakes this exists to prevent

- Inferring "solid-region content change" from connected-component **size**. Runs of text
  form components hundreds of pixels wide. Extent is not position.
- Attributing a mismatch to an unpinned dependency without testing it. Build the second
  environment; if both render byte-identical to each other, the theory is disproved.
- Mixing colourspaces: a grayscale pass and an RGB max-channel pass give different per-band
  counts. Pick one and use it throughout.
- Restoring the working tree to HEAD and then diffing files against HEAD — vacuous.

## Durable fix when pixels are the wrong gate

Commit the numeric output (counts, per-item geometry, metrics table) next to the figure and
test **that** with a tolerance. Add a negative control (perturb one value, gate must fail).
Record the verified environments in a sidecar `.env.json`.
