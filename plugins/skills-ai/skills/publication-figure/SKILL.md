---
name: publication-figure
description: This skill should be used when the user asks to "make this figure publication-ready", "labels are overlapping", "final figure for the paper", "fix the legend", "figure for the manuscript", or before saving any matplotlib figure that will be committed, submitted or shown to a reviewer.
---

# Publication figure

The correctness pass that a styling skill does not do. Render → check → save; never save
first and inspect after.

## Before saving

1. **Overlap check** (`scripts/overlap_check.py`): every text artist's bbox against every
   other in display coordinates. Zero collisions, or the collisions are the tick-label vs
   axis-label class you have looked at and accepted. Save only after the check returns clean.
2. **Colour threading.** The same quantity is the same colour in every panel. Interval bars
   labelled with their resampling unit (`95% actuator-cluster bootstrap`), not just `95% CI`.
3. **Name the statistic** in the label: `mean lead +0.323 life`, not `lead +0.32`. If the text
   quotes the median, the figure says which it plots.
4. **Legend over direct labels** when direct labels collide; **figure-level footer** for
   explanatory notes that do not fit inside the axes.
5. **Ticks:** thin them before shrinking the font. Fonts below 7 pt do not survive a
   two-column layout.
6. **Deployed / selected values** marked on the axis with a label that says what they are and
   whether they pass (`deployed τ* = 0.05: lead −0.145, 6/6 negative`).
7. **Regenerate from the script**; never edit the PNG. Commit the numeric output beside it
   (see `figure-manifest`).

## Reproducibility hygiene

`fig, ax = plt.subplots(); ... ; fig.savefig(path)` — never bare `plt.plot` / `plt.savefig`.
Transparent or paper-matched background if the figure will sit on a dark page. Metadata
records the renderer version; a different renderer will not byte-match, so gate on numbers.

## Iterating

Each fix can create a new collision — moving a label into a divider, a footer into a
caption. Re-run the check after every edit; three passes is normal.
