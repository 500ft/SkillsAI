# Curation gate (Stage 5) — blocking

Every claim retrieved in Stage 4 (STORM web output in Mode A, or `research-*` output
in Mode B) must clear **all** checks below before it can be written into the paper.
Anything that fails is recorded as an **open question / lead to verify**, not a citation.

## Checklist

1. **Source class.** Is the source peer-reviewed or primary (journal, conference,
   standards body, thesis, dataset paper)? A manufacturer datasheet is allowed **only**
   if flagged as such in-text. Blogs, Wikipedia, vendor marketing, forums, and LLM
   summaries are **leads, not citations** — they may point you to a real source, which
   you must then locate and cite directly.
2. **Traceability.** Do you have authors, year, venue, and a DOI or stable URL? No →
   it cannot be cited yet.
3. **Claim actually supports the sentence.** Read enough of the source to confirm it
   says what you are about to cite it for. No citation-by-title.
4. **Evidence tier tag.** Label the claim: **confirmed evidence** / **reasonable
   inference** / **open question**. Only confirmed evidence may be stated flatly;
   inference must be hedged; open questions go to a to-verify list, not the prose.
5. **Honesty-stance preserved.** The addition must not:
   - upgrade a **simulation/prediction** to a **measurement/finding**;
   - assert a measured number the study has not collected;
   - overturn an existing hedge (e.g. "optical properties to be measured",
     "no material is universally best", "pre-qualification screening, not certification").
6. **No data-locked section touched.** Results, measured values, and any
   sim-vs-measurement labels are off-limits (see the playbook).
7. **Bookkeeping.** A surviving citation must be added with full rigor to the paper's
   bibliography **and** its literature tracker (and a per-paper analysis stub if the
   project keeps them), matching the format of existing entries.

## Output of the gate

- **Passed** → goes into the proposed integration diff (Stage 6).
- **Failed** → goes into an "Open questions / to-verify" list returned to the user,
  with the reason it failed and what would be needed to promote it.

Never silently drop a failed item and never silently promote one.
