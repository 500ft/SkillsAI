#!/usr/bin/env python3
"""Render a tasks CSV (task-ledger schema) into docs/TASKS.md grouped by tier.
usage: ledger_to_md.py tasks.csv [--project NAME] [--ceiling TEXT] [--floor TEXT] > docs/TASKS.md
"""
import argparse, csv, collections, sys
ap = argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--project"); ap.add_argument("--ceiling", default="<ceiling>"); ap.add_argument("--floor", default="<floor>")
a = ap.parse_args()
rows = [r for r in csv.DictReader(open(a.csv)) if not a.project or r["project"] == a.project]
if not rows: sys.exit("no rows")
name = a.project or rows[0]["project"]
n0 = sum(r["tier"] == "0" for r in rows); ex = sum(r["executable_now"] == "yes" for r in rows)
out = [f"# {name} — tasks to completion", "",
"> **Objective.** Produce the strongest, most honestly-packaged evidence — not a completed project.",
"> Priority flows from leverage and executability. Never from a calendar, never from the ceiling.", "",
"## Two finish lines", "", f"**Ceiling.** {a.ceiling}", "", f"**Floor.** {a.floor}", "",
f"_{len(rows)} tasks · {n0} Tier 0 · {ex} executable now._", "", "---", ""]
for tier, label in (("0", "finish"), ("1", "package"), ("2", "park")):
    t = [r for r in rows if r["tier"] == tier]
    if not t: continue
    out += [f"## Tier {tier} — {label}", ""]
    for r in t:
        meta = f"`{r['gate_type']}` · " + ("executable now" if r["executable_now"] == "yes" else f"**{r['executable_now']}**")
        if r["depends_on"]: meta += f" · after {r['depends_on']}"
        out += [f"### {r['id']} · {r['task']}", "", meta, "",
                f"**Why it matters.** {r['why_it_matters']}", "", f"**What it adds.** {r['what_it_adds']}", "",
                f"**Done when.** {r['done_when']}", ""]
c = collections.Counter(r["tier"] for r in rows)
out += ["---", "", f"**Commitment.** Finish the {c['0']} Tier-0 items; package the {c['1']} Tier-1; park the {c['2']} Tier-2 until their resource is secured."]
print("\n".join(out))
