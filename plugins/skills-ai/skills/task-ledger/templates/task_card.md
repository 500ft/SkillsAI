# <ID> · <task title>

| | |
|---|---|
| track | <hardware / analysis / docs> |
| owner type | <Agent / Owner / External> |
| needs | <resources, access, prior tasks> |
| blocks | <task ids this unblocks> |
| files owned | <paths this card may touch> |
| branch | `task/<id>-<slug>` |
| ledger row | `<ID>` in `docs/TASKS.md` |

## Why this exists
<why_it_matters — what stays broken, weak or unfalsifiable without it>

## What to build
<one artifact or one decision>

## Files
- `path/to/file.py` (NEW)
- `path/to/existing.md`

## Not in scope — do not touch
<explicit exclusions>

## Done when
- [ ] <checkable line from done_when>
- [ ] negative control passes, where applicable

## How to verify
```
<exact command and expected output>
```

## How to submit
PR to `main` from the branch above; owner reviews against **Done when** and merges.

## References
<file:line anchors, prior PRs, the ledger row>
