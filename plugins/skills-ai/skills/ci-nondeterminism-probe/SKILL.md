---
name: ci-nondeterminism-probe
description: This skill should be used when the user says "CI is red on my branch but green on main", "flaky check", "is this failure mine", "re-run the check", "same code different result", or needs to decide whether a failing check is caused by the branch or by the job itself.
---

# CI nondeterminism probe

A red check on the branch with green on `main` implicates the branch — until you prove
otherwise. "It cannot be the cause" is an argument; identical trees with different outcomes
is evidence.

## Procedure

1. `git diff --stat main..branch`. If the branch differs only by inert files (docs, patches
   under `ci-proposed/`), proceed; otherwise the branch is a suspect and this probe does not
   apply yet.
2. Check the run history: has any single commit SHA produced both a pass and a fail? If yes,
   done — flaky. If no SHA has run twice, you cannot call it flaky yet.
3. Push an **empty commit** (`scripts/probe.sh`) to re-run the job on an identical tree.
4. Compare `git rev-parse <sha1>^{tree}` and `git rev-parse <sha2>^{tree}`. **Compute the
   hashes first and read them back**; never write them into a comment in the same step —
   a placeholder hash was published once this way.
5. Same tree, different outcome → the job is nondeterministic. Record it on the PR as a
   finding about the *job*, with the likely lead (tolerances close to run-to-run variation;
   time- or network-dependent steps). If it fails again on the identical tree, the branch
   is exonerated and the job is consistently broken on that runner.

## When logs are unreachable

If the container cannot be built locally and job logs are not readable with the available
token, CI is the only instrument and a new commit is the only way to re-trigger it. Say so,
rather than reasoning about the failure from the step name alone.

## Why this matters beyond the PR

A release-gating check that can fail on an unchanged tree cannot distinguish a regression
from noise. That is a defect in the gate, independent of any branch.
