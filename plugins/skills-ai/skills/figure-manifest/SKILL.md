---
name: figure-manifest
description: This skill should be used when the user asks to "add a figure manifest", "declare how this figure is generated", "what produces this PNG", "register the figures", "mark this figure as a placeholder", or when a repository's committed images have no declared generator, inputs or evidence type.
---

# Figure manifest

`docs/figure-manifest.json`: one entry per committed image, so every figure has a declared
generator, inputs, evidence class and prerequisites — and an audit can run it without
reverse-engineering the repo.

## Entry schema

```json
{
  "id": "study3-correlation",
  "command": "python -m scripts.run_study3",
  "cwd": ".",
  "outputs": ["figures/study3_fig3.png"],
  "numeric": "data/sim/study3_results.json",
  "inputs": ["data/sim/dataset.npz"],
  "evidence_type": "simulation | measured | placeholder | validation-pending",
  "notes": "what is and is not claimed"
}
```

Top-level `prerequisites`: `{"env": {"PYTHONPATH": "gym", "MPLBACKEND": "Agg"}, "install":
"pip install -e .", "python": "3.9", "pins": "environment.yml"}`. Commands that assume an
editable install or a `PYTHONPATH` without saying so are a finding — the RoboRacer manifest
did, and every generator failed on a clean checkout.

## Rules

- `numeric` names the machine-readable file the generator writes. **That file, not the PNG,
  is the reproducibility gate** (see `figure-regeneration-audit`). If the generator writes
  none, add one.
- Placeholder figures are labelled `placeholder` here **and** in the results README, with
  the blocking dependency named. Never let a placeholder look like a result.
- `runtime:` outputs (diagrams built at page render) are declared so the audit skips them
  deliberately rather than reporting them missing.
- `scripts/validate_manifest.py` checks: every committed image under the figure directories
  has an entry, every entry's outputs exist, every `numeric` exists, every `evidence_type` is
  from the enum.
