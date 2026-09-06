#!/usr/bin/env python3
"""Validate docs/figure-manifest.json against the repository.
usage: validate_manifest.py <repo> [--manifest docs/figure-manifest.json] [--figdirs figures,results,reports/figures]
"""
import argparse, json, sys
from pathlib import Path
ENUM = {"simulation", "measured", "placeholder", "validation-pending"}
ap = argparse.ArgumentParser(); ap.add_argument("repo"); ap.add_argument("--manifest", default="docs/figure-manifest.json")
ap.add_argument("--figdirs", default="figures,results,reports/figures,analysis/figures,assets")
a = ap.parse_args(); repo = Path(a.repo); errors = []
man = json.loads((repo / a.manifest).read_text()); figs = man["figures"] if isinstance(man, dict) else man
declared = set()
for f in figs:
    for k in ("id", "outputs", "evidence_type"):
        if k not in f: errors.append(f"{f.get('id','?')}: missing {k}")
    if f.get("evidence_type") not in ENUM: errors.append(f"{f.get('id')}: evidence_type {f.get('evidence_type')!r} not in {sorted(ENUM)}")
    if not f.get("command") and f.get("evidence_type") not in ("placeholder",): errors.append(f"{f.get('id')}: no command and not a placeholder")
    for o in f.get("outputs", []):
        if str(o).startswith("runtime:"): continue
        declared.add(o)
        if not (repo / o).exists(): errors.append(f"{f.get('id')}: output missing {o}")
    if f.get("numeric") and not (repo / f["numeric"]).exists(): errors.append(f"{f.get('id')}: numeric artifact missing {f['numeric']}")
for d in a.figdirs.split(","):
    for p in (repo / d).rglob("*") if (repo / d).exists() else []:
        if p.suffix.lower() in {".png", ".svg", ".jpg", ".jpeg", ".pdf"} and str(p.relative_to(repo)) not in declared:
            errors.append(f"undeclared image: {p.relative_to(repo)}")
if isinstance(man, dict) and "prerequisites" not in man: errors.append("no top-level prerequisites block (env, install, pins)")
print(f"{len(figs)} entries, {len(declared)} declared outputs")
for e in errors: print("  !!", e)
sys.exit(1 if errors else 0)
