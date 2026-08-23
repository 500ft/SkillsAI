---
name: execute-and-test
description: Execute an implementation plan task-by-task with strict test discipline — derive tests from the design/PRD acceptance criteria, implement until green, track progress in the plan file so work survives context loss, and (when the harness supports subagents) dispatch independent tasks in parallel and verify their output independently. Use this skill whenever a plan.md or task list exists and it's time to build, when the user says "execute the plan", "start implementing", "work through the tasks", or invokes /execute-and-test.
---

# Execute and Test — Disciplined Plan Execution

Work through an approved plan one micro-task at a time, proving each task with tests before moving on. The discipline exists for one reason: an agent that implements twenty things and then tests has no idea which of the twenty broke what. An agent that tests after every task always knows exactly what just changed.

## Inputs

Find the plan: the file the user points at, or the most recent `docs/specs/*/plan.md` that is `approved` or `in-progress`. Read its companion `design.md` too — the acceptance criteria there are the source of truth for tests. No plan? Recommend `/write-plan` first; executing without one means improvising design and scope mid-build. For a genuinely tiny task the user wants done now, write a 3-line inline plan (task, test, done-when) and proceed.

## The per-task loop

For each unchecked task, in dependency order:

1. **Read the task** and the design requirements it traces to.
2. **Write the test first** when the task produces observable behavior. Derive the assertion from the design's acceptance criteria — never from the implementation you're about to write. A test derived from your own implementation can only confirm what you did, not what was asked.
3. **Implement minimally** — exactly what the task says, in the files it names, matching repo conventions. Resist improving adjacent code; note it for `/arch-review` instead.
4. **Verify**: run the task's done-when condition, the relevant tests, and the project's lint/typecheck. Green means done; anything else means fix before proceeding.
5. **Check the task off in plan.md** with a one-line note (what changed, test that proves it). The plan file is the execution ledger — if context is lost or a new session takes over, the next unchecked task is the resume point. Update it in place, every task, no exceptions.
6. If the project uses git and the user wants commits, commit per task or per parallel group — small commits make the review and any rollback surgical.

## Subagent dispatch (when the harness supports it)

If your harness can spawn subagents (e.g. a Task/Agent tool), dispatch tasks in the same parallel group concurrently. If it can't (e.g. Codex CLI today), execute the same loop sequentially yourself — the protocol is identical, only the parallelism is lost.

Rules that make dispatch safe:

- **Self-contained prompts.** A subagent has no conversation history. Its prompt must include the full task text, the design excerpt it traces to, the repo conventions to follow, and the done-when condition.
- **Disjoint files.** Only dispatch tasks in parallel when their file sets don't overlap; two agents editing one file produces garbage.
- **Verify independently.** A subagent's "done" is a claim, not a fact. Re-run its done-when condition and tests yourself before checking the task off. This is the step that lets a reviewer (or a stronger model) do structural review instead of mechanical debugging — by the time work reaches them, "does it run" is already proven.

## Test discipline

- Tests encode the **design**, not the code. Each acceptance criterion in design.md gets at least one test; keep the mapping in `docs/specs/<slug>/test-report.md` as you go.
- **Never weaken, skip, or delete a failing test to get green.** If a test looks wrong, check it against the design doc. If design and test disagree, stop and surface the mismatch to the user — that's a requirements bug, and silently "fixing" the test hides it.
- Cover the edge cases the design enumerated (bad input, empty state, failure modes) — those sections were written precisely so they'd become tests.

## When a task fails repeatedly

Two honest failed attempts on one task means stop, not thrash. Re-read the design and the task; the usual causes are a task that hides an unmade design decision or a wrong assumption upstream. Surface what you found, propose the fix (often: amend design.md or split the task), and let the user decide. Looping a third time on the same error wastes context and erodes the plan's integrity.

## Completion

When all tasks are checked: run the full test suite plus lint/typecheck, then finish `test-report.md`:

```markdown
# <Feature> — Test Report
Date: YYYY-MM-DD
Suite: <command> — PASS/FAIL summary

## Acceptance criteria coverage
| Criterion | Test(s) | Status |

## Deviations from plan
## Deferred / known gaps
```

Set the plan `Status: done` and report honestly — including anything deferred or flaky. Suggest `/arch-review` for a structural pass, and `/update-memory` to persist what was decided and learned.
