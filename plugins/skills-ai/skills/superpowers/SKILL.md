---
name: superpowers
description: Workflow enforcer that runs any non-trivial build through a strict phase sequence — clarify → spec → plan → execute → review → close — with an explicit gate between each phase, so the agent never blindly writes code without a blueprint. Use this skill when the user starts a substantial project or feature and wants the full disciplined pipeline ("do this properly", "full workflow", "don't skip steps"), invokes /superpowers, or asks for the spec-then-plan-then-code treatment. For a single quick fix, don't use this — it's deliberately heavyweight.
---

# Superpowers — Phase-Gated Build Workflow

Run substantial work through six phases with a hard gate between each. The premise (borrowed from Obra's well-known Superpowers workflow): almost every agent failure on a big task traces back to skipping a phase — coding before the requirement was understood, planning before scope was settled, reviewing nothing. The gates make skipping impossible.

## The phases

Each phase has an owner skill if it's installed (check the available skills); if it isn't, follow the inline fallback. Either way, a phase ends only with explicit user sign-off — that's the gate.

1. **Clarify** — interrogate the user until the requirement has no high-impact unknowns. Owner: `grill-me`. Fallback: batched questions covering goal, scope boundary, data/interfaces, constraints, failure modes, success criteria; list the assumptions you'd otherwise make silently.
2. **Spec** — write the design document with testable requirements and acceptance criteria to `docs/specs/<slug>/design.md`. Owner: `grill-me` (it produces this). Gate: user marks it approved.
3. **Plan** — decompose the approved spec into micro-tasks with exact paths, dependencies, and verifiable done-conditions in `plan.md`. Owner: `write-plan`. Gate: user approves the task list.
4. **Execute** — work the plan task-by-task, tests derived from the spec, progress checked off in the plan file. Owner: `execute-and-test`.
5. **Review** — structural pass (owner: `arch-review`) plus a line-level diff review for bugs. Findings the user accepts loop back into Plan as new tasks, not ad-hoc edits.
6. **Close** — commit cleanly, update docs/changelog, persist decisions and state. Owners: `close-session` / `update-memory`.

## Rules that make the gates real

- **Announce the phase.** Start each phase by naming it and what its exit looks like. Track the current phase at the top of `docs/specs/<slug>/plan.md` so a future session resumes in the right place.
- **No code before phase 4.** Not scaffolds, not "just a quick prototype". Discovering code is needed to answer a question is fine — a throwaway experiment in /tmp, reported as evidence, then deleted.
- **No silent phase-skipping, including by the user's enthusiasm.** If the user says "just build it" mid-clarify, present the cost honestly (one sentence: which unknowns remain and what rework they risk) and let them overrule — they're the boss; the skill's job is making the trade visible, not refusing.
- **Backwards moves are normal.** Execution revealing an unmade decision sends you back to Spec, not into improvisation. Say so plainly: "This needs a decision, going back to the spec."
- **Scale the ceremony to the job.** A medium feature might clear Clarify in one round and Spec in half a page. The sequence is fixed; the depth per phase is judgment.

This skill is an orchestration layer inspired by (not a copy of) [Obra's Superpowers](https://github.com/obra/superpowers); the full original is a much larger plugin collection installable in Claude Code via its plugin marketplace, and these phases remain compatible with it.
