---
name: bibliography-coverage
description: This skill should be used when the user asks to "check the literature matrix", "do the bib entries match the sources", "how many sources do we actually have", "literature coverage", "citation count badge", or when a repository carries a literature review whose counts appear in more than one place.
---

# Bibliography coverage

A source count stated in four places (matrix CSV, per-paper notes, `.bib`, README badge) is
four numbers that can drift. One script asserts they agree, and CI runs it.

## Procedure

1. Enumerate each surface: rows in `literature_matrix.csv`; per-paper analysis files
   (minus README/template/consolidated files); `@entries` in every `.bib`; the number in the
   README badge or the roadmap sentence.
2. Join on a stable key (DOI, or a slug shared by the matrix row, the note filename and the
   bib key). Report entries present on one surface and absent on another, not just counts.
3. Fail on any mismatch. Print the offending keys.
4. When a stale count is found in prose ("19-source matrix" when there are 26), fix the
   prose *and* add it to the gate so it cannot drift again.

`scripts/check_coverage.py` implements 1–3 for the common layout; adapt the globs.
