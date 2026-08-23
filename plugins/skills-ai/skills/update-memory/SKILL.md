---
name: update-memory
description: Persist project context across sessions — capture architectural decisions (and the why), workflow constraints, conventions, and the current state of long-running work into durable files (AGENTS.md / CLAUDE.md plus docs/decisions ADRs) so any future session, in any agent tool, starts from a single source of truth instead of re-deriving everything. Use this skill at the end of a significant work session, after a major decision or direction change, when long-running work risks losing context, or when the user says "save context", "update memory", "remember this for next time", "write this down", or invokes /update-memory.
---

# Update Memory — Persistent Project Context

Long-running projects die a little every time a session ends: decisions lose their rationale, constraints get re-discovered the hard way, and the next session spends its first hour re-deriving what the last one knew. This skill writes the durable parts down — in the files agent tools actually load — so every future session (Claude Code, Codex, or a human) starts from one source of truth.

## Where memory lives

Project memory belongs in the repo, in files agents auto-load:

- **Canonical file**: `AGENTS.md` if it exists (the cross-tool standard Codex reads), otherwise `CLAUDE.md`. If neither exists, create `AGENTS.md`.
- **Cross-tool sync**: whichever file is non-canonical should exist as a pointer so both tools see the same truth. For Claude Code, a `CLAUDE.md` containing `@AGENTS.md` imports the canonical file; for other tools a one-line "See AGENTS.md — single source of truth" works. Never maintain two diverging copies — that's worse than no memory.
- **Decision records**: `docs/decisions/NNNN-<slug>.md`, one per significant decision. The canonical file stays short by pointing here.

## What qualifies as memory

Scan the session (and ask the user what they'd add) for exactly four kinds of durable fact:

1. **Architectural decisions + why** — what was chosen, what was rejected, and the reason. The *why* is the whole point: the choice itself is visible in the code; the rationale evaporates.
2. **Workflow constraints** — the exact build/test/run commands that work, environment quirks ("tests need Docker running", "use Python 3.11, 3.13 breaks pydantic"), credentials locations (never the credentials themselves), things that bit you this session.
3. **Conventions** — naming, layout, patterns the team/user enforces, especially corrections the user made ("don't use barrel files", "commit messages in imperative").
4. **State of long-running work** — for multi-session efforts: what's done, what's in progress, what's next, where the bodies are buried.

What does **not** qualify: anything derivable from the code or git history, session play-by-play, speculation, or secrets. Memory files are loaded into every future session's context — every stale or redundant line is a tax paid forever.

## Canonical file structure

Keep the canonical file under ~150 lines. It is an index and a briefing, not a journal:

```markdown
# <Project>

## Overview
<2-4 stable sentences: what this is, for whom>

## Commands
<build / test / run / lint — the exact incantations that work>

## Conventions
<bulleted, terse>

## Architecture decisions
<one line each, linking to docs/decisions/NNNN-*.md for the full record>

## Current state (updated YYYY-MM-DD)
- Goal: <the current push>
- Done: <recently landed, with absolute dates>
- In progress: <and exactly where it stands>
- Next: <the agreed next moves>
- Gotchas: <traps the next session must know>
```

Decision records use ADR shape — `Status / Context / Decision / Alternatives considered / Consequences` — and are immutable once accepted; a reversal gets a new ADR superseding the old.

## The update pass

1. **Read existing memory first.** Update and correct in place rather than appending duplicates — two entries about the same thing that disagree are poison.
2. **Convert relative to absolute.** "Yesterday" and "currently" rot; "2026-06-12" doesn't.
3. **Prune.** Anything contradicted by the current code gets fixed or deleted — verify against the repo before deleting, and flag (don't silently drop) anything you're unsure about.
4. **Refresh the Current state block and its date** — this section is the single highest-value paragraph for the next session's first minute.
5. **Show the user the diff** of what you added, changed, and pruned. Memory edits are cheap to review now and expensive to discover wrong later.

If the harness has its own persistent memory system (e.g. Claude Code auto-memory), store *user* preferences there — but project facts belong in the repo, where every tool and every collaborator gets them.
