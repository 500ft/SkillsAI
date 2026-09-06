# Proposed CI change — not active

`ci-proposed/ci-zip-count-90.patch` is a workflow change that **is not installed**. Nothing here is executed
by GitHub Actions until someone applies it.

The token used to open this pull request cannot write `.github/workflows/**` (no `workflow`
scope). That restriction is deliberate — it stops an automated token from silently changing
what CI runs — so this ships as a reviewable diff instead of routing around it.

## Apply

```bash
git apply ci-proposed/ci-zip-count-90.patch
git add .github/workflows
git commit -m "ci: expect 90 packaged skills"
```

Then delete this directory.
