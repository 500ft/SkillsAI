---
name: quality-gates
description: Enforce automated quality gates — typecheck → lint → test → build — after every meaningful code change, halting all feature work the moment any gate fails until it's green again. Use this skill whenever the user wants disciplined verification while coding ("run the quality gates", "spartan mode", "make sure everything passes before moving on", "stop if anything breaks"), at the end of any implementation session before declaring work done, or when invoked as /quality-gates. Also use it to set up gates in a project that has none.
---

# Quality Gates — Halt-on-Red Verification

Run a fixed ladder of checks after every meaningful change, and treat any red as a full stop: no new feature work until the gate is green. The discipline matters because failures compound — a type error ignored at 2pm becomes three test failures and a confusing diff by 4pm. Cheap checks run first so failure arrives in seconds, not minutes.

## The gate ladder

Order is cheapest-first, and a failure at any rung stops the ladder:

1. **Typecheck** — `tsc --noEmit`, `mypy`, `cargo check`, etc.
2. **Lint/format** — `eslint`, `ruff`, `gofmt`, with autofix applied where safe.
3. **Tests** — the suite relevant to the change first, then the full suite at session end.
4. **Build** — production build / compile, when the project has one.

## Discovering the gates

Before the first run, find the project's real commands — never guess:

- Read `package.json` scripts, `Makefile`, `pyproject.toml`, `Cargo.toml`, CI config (`.github/workflows/`) — CI is the ground truth for what "passing" means to this repo.
- Record the four commands at the top of your working notes (or the plan file if one exists) so every subsequent run uses identical invocations.
- **If a rung doesn't exist** (no typecheck configured, no tests), tell the user and offer to set up the missing rung — a project with no test runner is a finding, not an excuse to skip the rung.

## Halt semantics

- A failed gate means **stop feature work now**. Fix the failure, then rerun from rung 1 — a lint fix can introduce a type error.
- **Never bypass a gate to get green**: no `--no-verify`, no `eslint-disable` sprinkled to silence the rule, no `.skip` on a failing test, no loosening tsconfig. If a rule or test is genuinely wrong, that's a decision to surface to the user explicitly, changed in its own commit with the reasoning stated.
- Two honest failed fix attempts on the same gate → stop and present the failure output, your diagnosis, and options. Thrashing against a red gate burns context and usually means a wrong assumption upstream.
- Report gate status honestly at session end as a simple matrix (gate / command / pass-fail). "Done" claims require all gates green — anything less is "done except", said in those words.

## Automating the halt (optional, Claude Code)

The manual loop above works in any harness (Codex included). In Claude Code specifically, gates can be enforced mechanically with hooks — e.g. a `PostToolUse` hook running typecheck after every file edit, or a `Stop` hook that blocks ending the turn while gates are red. If the user wants that, set it up via the harness's hook configuration (the `update-config` / `hook-development` skills cover the mechanics). Recommend hooks when the user says "always" or "automatically"; a skill can only enforce discipline while it's loaded — hooks enforce it unconditionally.
