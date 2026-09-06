#!/usr/bin/env python3
"""Assert literature-matrix rows, per-paper notes, .bib entries and the README count agree.
usage: check_coverage.py <repo> [--matrix literature/literature_matrix.csv] [--notes-glob "ProConsList/*.md"]
                         [--exclude README.md,TEMPLATE.md,consolidated.md] [--bib-glob "**/*.bib"] [--badge-regex "literature_sources-(\d+)"]
"""
import argparse, csv, glob, re, sys
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("repo")
ap.add_argument("--matrix", default="literature/literature_matrix.csv"); ap.add_argument("--notes-glob", default="ProConsList/*.md")
ap.add_argument("--exclude", default="README.md,TEMPLATE.md,consolidated.md"); ap.add_argument("--bib-glob", default="**/*.bib")
ap.add_argument("--badge-regex", default=r"literature_sources-(\d+)"); ap.add_argument("--key", default=None, help="matrix column used as join key (default: first column)")
a = ap.parse_args(); R = Path(a.repo); errs = []
rows = list(csv.DictReader(open(R / a.matrix))); key = a.key or list(rows[0])[0]
mkeys = {r[key].strip().lower() for r in rows}
ex = set(a.exclude.split(","))
notes = [Path(p) for p in glob.glob(str(R / a.notes_glob)) if Path(p).name not in ex]
nkeys = {p.stem.lower() for p in notes}
bib = "".join(Path(p).read_text() for p in glob.glob(str(R / a.bib_glob), recursive=True))
bkeys = {m.lower() for m in re.findall(r"^@\w+\{([^,]+),", bib, re.M)}
readme = (R / "README.md").read_text() if (R / "README.md").exists() else ""
badge = [int(x) for x in re.findall(a.badge_regex, readme)]
print(f"matrix rows {len(rows)} | notes {len(notes)} | bib entries {len(bkeys)} | README badge {badge}")
if len({len(rows), len(notes), len(bkeys)} | set(badge)) != 1: errs.append("counts disagree")
for label, s in (("notes", nkeys), ("bib", bkeys)):
    if mkeys - s: errs.append(f"in matrix, not in {label}: {sorted(mkeys - s)[:8]}")
    if s - mkeys: errs.append(f"in {label}, not in matrix: {sorted(s - mkeys)[:8]}")
for e in errs: print("  !!", e)
print("coverage complete" if not errs else "coverage INCOMPLETE"); sys.exit(1 if errs else 0)
