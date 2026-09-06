#!/usr/bin/env bash
# Re-run CI on an identical tree and report whether the tree hashes match.
# usage: probe.sh <remote-url-with-token> <branch>
set -eu
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null
url="$1"; branch="$2"
before=$(git rev-parse HEAD)
git commit -q --allow-empty -m "ci: re-run on an identical tree to test for nondeterminism

No file changes. If this run's outcome differs from ${before:0:7}, the job is
nondeterministic; the tree hashes below are identical by construction."
after=$(git rev-parse HEAD)
git push -q "$url" "HEAD:$branch"
t1=$(git rev-parse "${before}^{tree}"); t2=$(git rev-parse "${after}^{tree}")
echo "commit before ${before:0:7} tree $t1"
echo "commit after  ${after:0:7} tree $t2"
[ "$t1" = "$t2" ] && echo "TREES IDENTICAL — compare the two check outcomes" || echo "trees differ (unexpected)"
