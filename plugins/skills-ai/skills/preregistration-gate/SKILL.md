---
name: preregistration-gate
description: This skill should be used when the user asks to "preregister this", "write the acceptance criterion", "what is the threshold before I run it", "hashed spec", "commit the gate first", or before any measurement, rerun, or experiment whose result will be judged against a threshold.
---

# Preregistration gate

The threshold is written down, hashed and committed **before** the thing it judges exists.
Written afterwards, it cannot fail — and a gate that cannot fail is decoration.

## What gets committed, as one spec file

1. **The quantity** and how it is measured (instrument, protocol, repeats, which statistic —
   fifth percentile, median, mean — named explicitly).
2. **The threshold** and its provenance (derived from what requirement, with the arithmetic).
3. **What a disagreement would mean.** The named outcome that would embarrass the model. If
   nothing could, the spec is not a test.
4. **What is fixed and may not move** after the result is seen: the threshold, the statistic,
   the sample, the analysis code (by commit SHA).

`scripts/prereg_spec.py` writes the spec with a content hash, refuses to run if a results
file already exists for the same id, and verifies an existing spec has not changed since it
was hashed.

## Two finish lines

Every validation-gated project gets both, as separate tasks:

- **Ceiling** — measured completion. Needs the external resource.
- **Floor** — the honest package shippable without it: preregistered gates with
  `Pending — <what>, criterion preregistered` stated plainly. Not an estimate, not a
  simulation stand-in, not a placeholder.

The floor is the realistic finish line for anything gated on a resource you do not control.
Generate tasks for both so the project is presentable either way.

## Ordering

Preregistration is its own task, placed immediately before the measurement it judges — never
folded into "run the experiment". Folded in, the ordering silently disappears, and the
ordering is the whole difference between a result and a description.

## Mistakes this exists to prevent

- Cohort-dispersion coefficients chosen after seeing the new interval: cohort width becomes
  a free parameter tuned until the interval looks good.
- A Monte Carlo "100% recovery" reported on an *assumed* geometry as though it were a result.
  Restate the gate against the measured quantity as an unknown.
- A caption quoting the mean where the text quotes the median for the same configuration.
  The spec names the statistic; both then have to use it.
