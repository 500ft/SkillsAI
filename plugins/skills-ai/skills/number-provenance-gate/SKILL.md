---
name: number-provenance-gate
description: This skill should be used when the user asks to "check the headline numbers", "does the README match the results", "gate the manuscript numbers", "add a numbers test", "find stale numbers", or wants every reported number in docs traced to a committed artifact and tested against it.
---

# Number provenance gate

Every number a document reports must be **computed** from a committed artifact by a test, so
drift fails CI instead of waiting for a reviewer.

## The rule

> No document **asserts** a superseded value as current.

Not "no document mentions a superseded value". `BOM.md` saying "vs the prior 129.76 g" is a
correct description of a change; the first version of this gate flagged it. Lines carrying an
explicit historical marker are exempt (`prior`, `previous`, `was`, `were`, `formerly`,
`superseded`, `corrected`, `used to`, `earlier`, `old`).

## Procedure

1. Find the source of truth for each number: the script or CSV that produces it. If a
   document's number has no committed source, that is the first finding.
2. Write the gate to **compute** the expected values from that source. Never type them into
   the test — a test with hand-typed constants drifts exactly like the document did.
3. Compare against every document that quotes them, including derived values one step
   removed (a per-motor thrust computed from a frozen maximum goes stale when the maximum
   does).
4. Formatting is part of the contract: `0.9495` renders `0.950` at `.3f`, not `0.949`; an
   abstract with a character cap is gated on the cap.
5. **Two negative controls, every time:** reintroduce the stale value → gate must fail;
   perturb the source artifact → gate must fail. A gate that has never failed proves nothing.
6. Wire it into whatever already runs (`unittest discover`, `pytest`, a `check_*.py` in CI).

## Template

`scripts/numbers_gate_template.py` is a `unittest` module: subclass, set `SOURCE` (a callable
returning the expected dict) and `DOCS` (paths), and it does the rest — including the
historical-marker exemption and a `--negative-control` mode that perturbs and expects failure.

## What edit recency does not tell you

`current-results.md` was edited *after* the CSV changed, without its table being touched. A
recent commit on a document is not evidence its numbers are current. Only the gate is.
