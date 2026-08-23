---
name: storm-paper
description: >-
  Use when the user asks to improve, strengthen, or deepen a research paper or
  manuscript — especially the literature review / related work, gap-finding,
  or discussion framing. Applies Stanford STORM's multi-perspective research
  methodology (stanford-oval/storm) on top of the deep-research / research-*
  skills, behind a mandatory academic-honesty curation gate. Triggers:
  "improve my paper", "make this paper better", "strengthen related work",
  "expand the literature review", "find gaps in my paper", "STORM my paper",
  "what am I missing", "harden the discussion".
---

# storm-paper

Improve an existing research manuscript by applying **STORM's** research method —
*perspective-guided question asking* + *outline-first grounded synthesis* — and
feeding it through your existing `research-*` skills, then through a **mandatory
curation gate** so nothing ungrounded reaches the paper.

STORM (`stanford-oval/storm`, cloned at `~/Developer/storm`) natively writes
Wikipedia-style articles from live web search. That is powerful for **breadth,
missed related work, and multi-perspective gap-finding** — but its raw web output
is the opposite of what a citation-disciplined paper needs. **This skill uses
STORM's method, never its raw output verbatim.**

## Two modes

- **Mode A — Pipeline** (use when a working LLM + retriever are configured): run the
  real `knowledge_storm` package on a *scoped subtopic* of the paper, capture its
  researched draft + citations, then pass everything through the curation gate.
  "Configured" = an LLM litellm can reach (API key **or** a local/self-hosted model)
  **and** a retriever (keyed: Serper/Bing/Brave/Tavily/You.com; or keyless/local:
  a VectorRM over your own corpus). Setup + commands: `references/run_storm.md`.
- **Mode B — Methodology fallback** (default; no external config): *you* execute
  STORM's method — generate perspectives, ask each one's questions, answer them by
  driving `research` → `research-deep` → `research-analysis` → `research-report`
  over vetted sources. Same six stages, same gate, zero cost.

Default to **Mode B** unless the user says an LLM+retriever are configured or asks
to run the real pipeline. Announce which mode you are in.

## The six stages (both modes)

1. **Scope.** Pick the exact section(s) to strengthen. Read the target section and
   the paper's honesty constraints first. **Never** target data-locked sections
   (results, measured numbers, sim-vs-measurement labels) — see the playbook.
2. **Perspective generation** (STORM's core trick). Enumerate 4–6 distinct expert
   viewpoints a thorough reviewer would bring, e.g. for an instrumentation paper:
   metrologist, field-deployment engineer, calibration statistician,
   materials/thermal analyst, and a skeptical peer reviewer. Tailor to the domain.
3. **Multi-perspective questioning.** From each perspective, interrogate the
   section: What evidence is missing? What competing method/standard is unaddressed?
   What assumption is unstated? What would a referee attack? Collect as a question list.
4. **Grounded retrieval.** Answer the questions — Mode A via the STORM run, Mode B via
   the `research-*` chain. **Capture every citation** (authors, year, venue, DOI/URL).
5. **Curation gate (mandatory, blocking).** Apply `references/curation_gate.md`.
   Anything that fails is demoted to an "open question / lead," not written in.
6. **Integration.** Produce a **reviewable diff** of proposed edits + new bibliography
   entries + updated literature-tracking rows. **Never auto-commit; never push.**

## Hard rules

- STORM/web output is a **lead generator**, not a source of truth. Only peer-reviewed
  or primary sources (or explicitly-flagged datasheets) become citations.
- Preserve the paper's existing honesty stance verbatim (e.g. simulation ≠ measurement,
  "to be measured" optical properties, "no universally-best" claims).
- Tag every added claim: **confirmed evidence / reasonable inference / open question**
  (reuse the deep-research output standard).
- Every new citation must land in the paper's bibliography **and** its literature
  tracker with the same rigor as existing entries.
- Output diffs for review. Do not commit or push — respect any repo publication embargo.

## References

- `references/curation_gate.md` — the blocking honesty checklist (Stage 5).
- `references/paper_improvement_playbook.md` — which sections STORM may touch vs. never,
  worked for the Enclosure-Research manuscript as the reference example.
- `references/run_storm.md` — how to configure + run Mode A (LLM + retriever options,
  secrets.toml, scoping a STORM topic to one paper subsection).

## Relationship to other skills

Composes, does not replace: `deep-research` (chains `research` / `research-deep` /
`research-analysis` / `research-report`). Use `graphify` for code questions, not this.
