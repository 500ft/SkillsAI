#!/usr/bin/env bash
# Turn an uncommitted .github/workflows change into an appliable patch under ci-proposed/,
# then revert the workflow file so the branch never carries a workflow write.
# usage: make_ci_patch.sh <patch-name> "<one-line description>"
set -eu
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null
name="$1"; desc="$2"
mkdir -p ci-proposed
git add -N .github/workflows 2>/dev/null || true
git diff -- .github/workflows > "ci-proposed/$name"
[ -s "ci-proposed/$name" ] || { echo "no workflow diff to capture"; exit 1; }
git checkout -- .github/workflows 2>/dev/null || true
git clean -fdq .github/workflows 2>/dev/null || true
git apply --check "ci-proposed/$name" && echo "git apply --check: OK"
cat > ci-proposed/README.md <<EOF
# Proposed CI change — not active

\`ci-proposed/$name\` is a workflow change that **is not installed**. Nothing here is executed
by GitHub Actions until someone applies it.

The token used to open this pull request cannot write \`.github/workflows/**\` (no \`workflow\`
scope). That restriction is deliberate — it stops an automated token from silently changing
what CI runs — so this ships as a reviewable diff instead of routing around it.

## Apply

\`\`\`bash
git apply ci-proposed/$name
git add .github/workflows
git commit -m "ci: $desc"
\`\`\`

Then delete this directory.
EOF
echo "wrote ci-proposed/$name and ci-proposed/README.md"
