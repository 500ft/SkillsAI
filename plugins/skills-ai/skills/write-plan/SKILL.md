---
name: write-plan
description: Decompose an approved design into a strict, ordered list of micro-tasks (2–5 minutes of agent work each) with exact file paths, signatures, dependencies, and verifiable done-conditions — the roadmap that stops an agent from coding too early or drifting mid-build. Use this skill whenever a design document or PRD exists and implementation hasn't started, when the user asks for an implementation plan, task breakdown, or roadmap, or invokes /write-plan. Use it BEFORE writing feature code, and after /grill-me when that skill produced a design.
---

# Write Plan — Design Decomposition

Turn an approved design into micro-tasks so small and precise that executing them requires no design decisions — only execution. A good plan lets a fresh agent (or a subagent with no conversation history) pick up any task and complete it correctly from the task text alone. That property is what makes the plan parallelizable, resumable after context loss, and verifiable.

## Hard rules

- **Do not write feature code.** The deliverable is the plan file.
- **No task may contain a hidden design decision.** If decomposing reveals an unmade decision ("do we store this in SQLite or a JSON file?"), stop and surface it — it belongs in the design doc, not improvised mid-task. Update `design.md` with the user, then continue planning.
- **Every functional requirement maps to at least one task.** Untraceable requirements silently fall through; the traceability table at the end of the plan is how you catch them.
- **Real paths, real names.** Survey the codebase before writing the plan so every file path exists or has an explicitly correct location, and naming matches the repo's conventions. A plan with invented paths fails on task one.

## Process

### 1. Locate the design

Use the design doc the user points at, or the most recent `docs/specs/*/design.md` with `Status: approved`. If no approved design exists, say so and recommend running `/grill-me` first — planning from a vague prompt just moves the silent assumptions one level down. If the user insists on planning without one, write a minimal design header (goals, scope, acceptance criteria) at the top of the plan and have them confirm it.

### 2. Survey the codebase

Read the directory structure, build config, test setup, and the modules the change will touch. Note the conventions (naming, file layout, test patterns) tasks must follow. This is what makes the difference between a plan and a wish list.

### 3. Write the plan

Save to `docs/specs/<slug>/plan.md` next to the design. Structure:

```markdown
# <Feature> — Implementation Plan
Design: ./design.md
Status: draft | approved | in-progress | done
Date: YYYY-MM-DD

## Tasks

### [ ] T00 — Environment check
- Files: none
- Do: verify build, test runner, and lint pass on a clean checkout; record the exact commands here.
- Done when: all three commands run green and are written into this file.

### [ ] T01 — <short imperative title>
- Files: src/exact/path.ts (new), src/other/file.ts (modify)
- Do: <precise instruction, including key signatures, e.g.
  `export function loadWeights(path: string): Weights` — parse YAML,
  throw TypedConfigError on malformed input>
- Depends on: T00
- Done when: <objectively checkable condition — a command that passes, an output that exists>
- Parallel group: A

...

## Traceability
| Requirement | Tasks |
| FR-1 | T01, T04 |

## Execution notes
<ordering caveats, risky tasks, suggested checkpoints>
```

Task-sizing discipline:

- **2–5 minutes of focused agent work each** — one concern per task. If describing a task needs the word "and" twice, split it.
- **Done-when must be verifiable** — a command, a test, an observable output. "Code is written" is not a done-condition; "`npm test -- weights` passes" is.
- **Order topologically** by `Depends on`, and tag independent tasks with a shared `Parallel group` letter so an executor with subagents can dispatch them concurrently.
- **Interleave test tasks** rather than batching all tests at the end — each behavior-bearing task should be followed (or preceded, for test-first) by its test task, both tracing to acceptance criteria in the design.
- **End with an integration task** that runs the full suite and checks every acceptance criterion from the design doc.

### 4. Sign-off and handoff

Present the task list summary (count, parallel groups, anything risky), get the user's approval, then set `Status: approved`. Point them at `/execute-and-test` to work through the plan. The plan file is the single source of truth for execution progress — executors will check tasks off in place, which is what makes long builds survive context resets.
