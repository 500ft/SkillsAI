---
name: engineering-prose
description: This skill should be used when the user asks to "tighten this", "make it read like a methods section", "remove editorialising", "lab-notebook register", "does this read like a paper", or when writing manuscripts, READMEs, PR bodies, captions or audit reports for a technical reader.
---

# Engineering prose

The register of a methods section or a lab notebook. The reader is scanning for the result,
the artifact, the caveat, and the next step.

## Rules

1. **One idea per sentence**, each connecting to the next. No sentence carries two claims.
2. **Name the property, not the adjective.** Not "better" — "higher-resolution", "converged to
   <1.5% on mesh refinement". Not "vanilla", "unsexy", "workhorse", "quick-and-dirty" — these
   compress a concrete property you can state, and carry a value judgement you cannot defend.
3. **Numbers carry units and a source.** `174.7 Hz (Rayleigh, 0.175 kg tip; runs/mast_hand_calc)`.
4. **State what is not claimed in the same paragraph as the claim.** Not a limitations section
   three pages later.
5. **Name the statistic.** A caption saying `+0.32 life` beside text saying `+0.346` for the
   same configuration is a contradiction until one says *mean* and the other *median*.
6. **Distinguish evidence classes** every time: simulation / measured / pending / placeholder.
7. **No emoji, no celebration, no warmth signals.** Structure instead: a header, a bold term, a
   clearer sentence.
8. **Numbered lists are one uninterrupted block.** No headers or prose between items.
9. **Narrate the work, not the plumbing.** "Regenerated from a pristine tree in the pinned
   environment", not which tool or function did it.
10. **Corrections are visible.** When a published claim was wrong, the correction names the
    wrong claim, states the right one, and stays in the record — in the commit, the PR body,
    and every other passage that repeated it.

## Before quoting anything

Compute it, read it back, then write it. Never compose a message containing a computed
identifier in the same step that computes it — a placeholder becomes a published fabrication.

## Sweep before finishing

Regex the whole document for every phrasing of any claim you corrected. Fixing one passage
and leaving the summary and the disclaimer asserting the old version is the same failure as
patching a local file while the published PR body still says the wrong thing.
