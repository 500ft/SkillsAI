---
name: task-ledger
description: This skill should be used when the user asks to "make a task list to completion", "what is left on this project", "task cards", "task-development PR", "tasks to reach the ceiling", or wants a project's remaining work as an anchored, tiered, date-free ledger.
---

# Task ledger

A completion plan whose every row can defend its own existence, with no dates.

## The objective, written once at the top of every ledger

> Produce the strongest, most honestly-packaged evidence — not a completed project. Priority
> flows from leverage (does it unblock other work, or add decisive evidence) and
> executability. Never from a calendar, and never from the project's ceiling.

## Rules

1. **Anchor to verified state.** Every task comes from a checked fact (audit result, file:line,
   real number). An unaudited project gets one task — "audit it" — and everything else stays
   provisional.
2. **Two finish lines per project**, stated separately: ceiling (measured) and floor (honest
   package without the resource). Tasks for both.
3. **Atomic.** One artifact or one decision, finishable in one sitting. If it contains "and",
   split it. Preregistration, the run, each figure, each manuscript edit are separate tasks.
4. **Schema** (`templates/tasks.csv`): `id, project, task, gate_type
   (preregister|external|build|hygiene), why_it_matters, what_it_adds, done_when, depends_on,
   executable_now (yes | blocked-on-<resource>), tier (0 finish | 1 package | 2 park)`.
   `why_it_matters` and `what_it_adds` are mandatory — anything that cannot fill both is
   filler and comes off.
5. **Order:** preregistration immediately before the measurement it judges.
6. **Tier by executability, not importance.** A task whose blocker is not secured cannot be
   Tier 0 however decisive it is; list what would flip it.
7. **Cross-cutting tasks** (reconcile repo ↔ resume ↔ portfolio; CI wire-ups needing scope the
   token lacks) appear in every repo they touch.
8. **End with the commitment, not the list:** "These I finish (Tier 0); these I package and
   park (1/2)."

## Delivery

`scripts/ledger_to_md.py tasks.csv > docs/TASKS.md`, one file per repo, on branch
`audit/task-development`, PR titled `task-development-<Project>`. Contributor-facing cards
(`templates/task_card.md`) when someone else will pick the work up cold.

## Mistake this exists to prevent

Hand-typed summary tables. Print counts from the saved CSV and copy them; a retyped
per-project table was wrong in four rows of five once.
