---
name: close-session
description: End-of-session wrap-up ritual — inventory what got done and what didn't, group changes into clean commits, update changelog/docs that the work made stale, persist decisions and current state to project memory, and leave a resume note so the next session starts in one minute instead of thirty. Use this skill when the user is wrapping up ("let's close out", "wrap up", "done for today", "/close", "end session"), or when a long working session reaches a natural stopping point and the work would otherwise be left uncommitted and undocumented.
---

# Close Session — The Wrap-Up Ritual

A session that ends abruptly leaves three messes: uncommitted changes nobody remembers the intent of, docs that now lie, and a next session that burns its first half-hour reconstructing state. Closing is cheap while the context is still in your head — this skill spends five minutes now to save thirty later.

## 1. Inventory (look before touching)

- `git status` and `git diff` — what actually changed, including files you forgot about.
- The session's task state: plan.md checkboxes, todo list, anything promised in conversation but not done.
- Sort everything into: **done**, **in progress** (where exactly it stands, what the next concrete step is), and **abandoned** (and why — abandoned-with-reason is information; abandoned-silently is a trap).

Surface anything surprising in the diff (files you didn't knowingly touch, generated junk, stray debug code) before committing — closing is the last checkpoint where "what is this?" is easy to answer.

## 2. Commit

- Group the diff into logical commits — one intent per commit, not one giant "session work" blob. Stage by file/hunk accordingly.
- Messages follow the repo's existing convention (read `git log` first); state the why when it isn't obvious.
- **Check before staging**: no secrets/keys/tokens, no `.env`, no debug leftovers (`console.log`, commented-out blocks, scratch files), nothing that belongs in `.gitignore`. Finding these is normal at close — fix, don't ship them.
- Work in progress goes in as an honest `wip:` commit on the working branch — better recorded than lost. **Commit, but do not push** unless the user has asked for pushes; publishing is their call.
- If nothing should be committed (user's call, or the repo isn't theirs to commit to), record the diff summary in the resume note instead.

## 3. Docs and changelog

Only what this session made stale: add a `CHANGELOG.md` entry if the repo keeps one (match its format), fix README sections the work invalidated (changed commands, new env vars, new setup steps). Don't invent docs the repo never had — that's separate work, suggest it if warranted.

## 4. Persist context

Run the `update-memory` skill's pass if it's installed (it owns the format); otherwise, minimally: update the **Current state** block in `AGENTS.md`/`CLAUDE.md` — Goal / Done (with today's date) / In progress / Next / Gotchas — and record any significant decision made this session with its rationale. The Gotchas line is the highest-value one: the trap you just learned about is exactly what the next session will step in.

## 5. Hand back

End with a short report: commits made (hash + one-liner each), docs touched, what's parked and where to pick it up, plus anything that needs the user's action (a push, a review, a decision left open). One paragraph the user could read Monday morning cold.

Don't gold-plate the close: no refactors, no "while I'm here" cleanups, no new features. Anything tempting goes in the resume note as a suggestion. Closing is bookkeeping — the discipline is stopping.
