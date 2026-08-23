---
name: arch-review
description: >-
  Big-picture architecture and abstraction review — map the codebase structure, find structural problems
  (cyclic dependencies, god modules, leaky or duplicated abstractions, wrong-layer logic), and propose the
  smallest abstractions that fix them, before the codebase grows tangled. Use this skill when a feature is
  complete and needs a structural look before finalizing, when the user asks "review the architecture",
  "is this well structured", "propose better abstractions", says the code "feels messy" or "tangled",
  or invokes /arch-review. Distinct from a line-level code review: this is about module boundaries and
  shape, not bugs.
---

# Arch Review — Architecture & Abstraction Review

Step back from the diff and look at the shape of the system. Line-level review catches bugs; this review catches the structural drift that makes month six of a project slower than week one. The output is a ranked report of structural findings with proposed abstractions — it is a review, not a refactor: change no code unless the user explicitly asks afterward.

## Process

### 1. Map the system as it actually is

Read the directory layout, entry points, and import/dependency relationships between modules (use the dependency graph tooling the ecosystem provides if available — `madge`, `pydeps`, `go mod graph`, etc. — otherwise trace imports manually). Sketch the result as a short text diagram: modules and the direction dependencies point. Trace one or two core data flows end-to-end (request → response, input file → output). The map is the deliverable's foundation — findings without a map are vibes.

### 2. Hunt for structural problems

Work through this list deliberately; each item names the smell, because "look for problems" finds nothing:

- **Dependency direction violations & cycles** — low-level modules importing high-level ones; A→B→A loops. Cycles are the single best predictor of "can't change anything without changing everything".
- **God modules** — files everything imports, or that import everything; `utils.py` graveyards holding unrelated concepts.
- **Leaky abstractions** — callers reaching into a module's internals, knowing its storage format, or re-implementing its logic because the interface doesn't expose what they need.
- **Duplicated concepts** — the same idea implemented twice with different names/shapes (two retry mechanisms, two config loaders, two "User" shapes). Worse than duplicated code: fixes land in one and not the other.
- **Wrong-layer logic** — business rules living in UI handlers, IO glue, or CLI parsing, where they can't be tested or reused.
- **Missing seams** — behavior untestable without heavy mocking or a live network/database; usually means a hidden dependency that should be injected.
- **Speculative abstraction** — interfaces with one implementation, plugin systems with one plugin, config nobody sets. Cut these; they're complexity paid forward for flexibility never used.
- **Data-shape drift** — the same entity reshaped slightly at each layer boundary, with ad-hoc conversion code accumulating between them.

### 3. Write the report

Save to `docs/reviews/arch-review-YYYY-MM-DD.md`:

```markdown
# Architecture Review — YYYY-MM-DD
Scope: <what was reviewed>

## System map (as-is)
<text diagram + 2-3 sentences on intended vs. actual structure>

## Findings (ranked by severity)
### F1 — <title> [high | medium | low]
- Evidence: path/file.ts:120, path/other.ts:33
- Why it hurts as the code grows: <the concrete future cost>
- Proposed fix: <the smallest abstraction or move that resolves it>
- Effort: S/M/L · Risk: <what could break>

## Top 3 moves
<the highest leverage-to-effort changes, in order>

## Explicitly fine — do not refactor
<things that look impure but aren't worth touching, and why>
```

Every finding needs file:line evidence — a finding you can't point at is an opinion. "Why it hurts" must name the concrete future cost (the next feature this blocks, the bug class it invites), not aesthetics.

## Judgment rules

- **Propose the smallest abstraction that fixes the issue.** The failure mode of architecture review is prescribing a grand redesign; the goal is targeted moves a person or agent can execute in bounded time.
- **Prefer deletion.** Removing a needless layer beats adding a clever one.
- **No rewrites without a migration path.** Any proposal touching many call sites must include the incremental route (strangler pattern, adapter at the boundary) or it doesn't get proposed.
- **Calibrate to the project.** A 500-line script doesn't need hexagonal architecture; a 50k-line product shouldn't be excused its cycles. Judge structure against where the project is actually headed — and the "do not refactor" section is mandatory, because telling the user what's *fine* is half the value.

If the user asks to apply the fixes, treat each accepted finding as design input: run it through `/write-plan` so the refactor gets the same micro-task discipline as a feature.
