---
name: audit-pr-conventions
description: This skill should be used when the user asks to "open a PR for this fix", "push the audit branch", "write the commit message", "supersede the earlier attempt", "stack this on the other PR", or when any change from an automated audit is being delivered to a repository the user owns.
---

# Audit PR conventions

How an automated audit delivers changes to someone else's repository without ever becoming a
liability to it.

## Hard rules

- Branch `audit/<topic>`. **Never push to `main`.** Never change settings or collaborators.
- Commits attributed to the repository owner (read `login` and `id` from the API; email
  `<id>+<login>@users.noreply.github.com`).
- One concern per branch. Stack on an unmerged audit branch when the work builds on it;
  GitHub retargets to `main` when the base merges.
- Stacked PRs show **no checks** when workflows are `pull_request: branches: [main]`. Verify
  locally, and say in the PR body that you did and how.
- Wrong turns stay in history as **superseding commits** with a PR comment, never a
  force-push once a PR exists. Before a PR exists, `--force-with-lease` only, after a fresh
  fetch (`scripts/verify_push.sh` does the fetch-and-compare).
- A correction applied to a local file leaves the wrong value live in the published PR body.
  Patch the body, post a superseding comment, and sweep the punch list for every other
  passage asserting the old claim.
- A red check on the branch with green on `main` implicates the branch until proven
  otherwise — but prove it (see `ci-nondeterminism-probe`) rather than assume in either
  direction.

## PR body (`templates/pr_body.md`)

`## What this fixes` · `## Why` (mechanism, not symptom) · `## Verification` (the actual
command and its output, with the environment named) · `## Negative control` · `## Not
changed` (what was deliberately left alone and why) · `## Still needs you` (anything the
token cannot do).

## Commit message

First line under 72 characters, imperative. Body states mechanism, what was verified and in
which environment, what was deliberately excluded, and — when superseding — which earlier
commit it supersedes and what that one got wrong.

## The workflow-scope gap

A token without `workflow` scope cannot write `.github/workflows/**`, via `git push` or the
Contents API. Do **not** route around this; it exists to stop an automated token silently
changing what CI executes. Ship the change as a `git apply`-able patch under `ci-proposed/`
with a README (`scripts/make_ci_patch.sh`). Verify with `git apply --check`.

## Shell gotchas

- `git push ... | grep -v token` makes `$?` grep's status. Confirm a push by fetching and
  comparing SHAs, not by exit code.
- `sed -i` differs between GNU and BSD; use Python for in-place edits that must assert their
  anchor matched exactly once.
- Two PRs on one head branch: close the one whose base is not `main`.
