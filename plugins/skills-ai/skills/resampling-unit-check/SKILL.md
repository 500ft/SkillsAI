---
name: resampling-unit-check
description: This skill should be used when the user asks "is this confidence interval right", "bootstrap by actuator", "cluster bootstrap", "leave-one-out", "why is the interval degenerate", "resample by specimen", or whenever a bootstrap or CI is computed on data with repeated measurements per unit.
---

# Resampling-unit check

The unit you resample must be the unit the design varies. Thirty points from six specimens
is six clusters, not thirty observations.

## Procedure

1. Identify the design unit (actuator, specimen, subject, run). Count them. If it is small
   (≤ 8), **enumerate the cluster resample exhaustively** (6⁶ = 46,656) instead of sampling.
2. Report three intervals side by side — point-level (what was probably committed),
   cluster-level, and leave-one-cluster-out (jackknife). The *spread between them* is a
   finding, not a nuisance.
3. Jackknife in Fisher-z space; the raw version pushes onto the boundary as r → 1.
4. Compare the pooled estimand to the per-cluster values. Pooled r below every per-cluster r
   means pooling attenuates it; the within-cluster estimand answers "does the indicator track
   drift as *this* unit ages", which is usually the question.
5. If every cluster gives an identical statistic, the interval is **degenerate** — a fact about
   the generator (or a hard-coded grid), not a precision claim. Report `degenerate` with an
   interpretation warning; never report `[0.600, 0.600]` as a CI.
6. Pass/fail counts: exact binomial (Clopper–Pearson). For 0 of n, the one-sided 95% upper
   bound, not "0%".

`scripts/cluster_bootstrap.py` does 1–5 from a CSV with `cluster,x,y` columns.

## The result may be negative for your hypothesis

The cluster interval came out *narrower* than the point-level one in the case this was
extracted from, because the synthetic clusters were near-homogeneous. The committed interval
was not anti-conservative; the cohort was degenerate. Investigating *why* the quality metrics
saturated found the indicator was invariant to every unit parameter — the single cause behind
the degenerate intervals, the identical per-unit correlations, and the saturated metrics.
Report that, rather than the confirmation you went in for.
