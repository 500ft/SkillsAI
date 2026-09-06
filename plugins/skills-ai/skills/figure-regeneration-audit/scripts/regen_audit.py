#!/usr/bin/env python3
"""Regenerate every figure in a manifest from a pristine tree and classify the result.

usage: regen_audit.py <repo> [--manifest docs/figure-manifest.json] [--out audit.json]
                      [--rel-tol 1e-9] [--timeout 1800]

Manifest entries need: id, command, outputs (list). Optional: numeric (path of a JSON/CSV the
generator writes, used as the authoritative comparison), env (dict), cwd.
"""
import argparse, csv, hashlib, io, json, math, os, shutil, subprocess, sys, tempfile
from pathlib import Path

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def png_software(p):
    try:
        from PIL import Image
        return Image.open(p).info.get("Software")
    except Exception:
        return None

def flat(o, pre=""):
    if isinstance(o, dict):
        for k, v in o.items(): yield from flat(v, f"{pre}.{k}")
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from flat(v, f"{pre}[{i}]")
    else:
        yield pre, o

def load_numeric(path):
    text = Path(path).read_text()
    if path.suffix.lower() == ".json":
        return {k: v for k, v in flat(json.loads(text)) if isinstance(v, (int, float)) and not isinstance(v, bool)}
    rows = list(csv.DictReader(io.StringIO(text)))
    out = {}
    for i, r in enumerate(rows):
        key = r.get("metric") or r.get("name") or str(i)
        for k, v in r.items():
            try: out[f"{key}.{k}"] = float(v)
            except (TypeError, ValueError): pass
    return out

def numeric_diff(old, new, tol):
    worst, worst_key, n = 0.0, None, 0
    for k, a in old.items():
        if k not in new: continue
        b = new[k]
        if a == b: continue
        rel = abs(b - a) / max(abs(a), 1e-300)
        n += 1
        if rel > worst: worst, worst_key = rel, k
    return dict(n_differ=n, n_keys=len(old), worst_rel=worst, worst_key=worst_key,
                status="NUMERIC_DRIFT" if worst > tol else "RENDER_ONLY")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo"); ap.add_argument("--manifest", default="docs/figure-manifest.json")
    ap.add_argument("--out", default="regen_audit.json"); ap.add_argument("--rel-tol", type=float, default=1e-9)
    ap.add_argument("--timeout", type=int, default=1800)
    a = ap.parse_args()
    repo = Path(a.repo).resolve()
    env = dict(os.environ, GIT_CONFIG_GLOBAL="/dev/null", GIT_CONFIG_SYSTEM="/dev/null", MPLBACKEND="Agg")
    man = json.loads((repo / a.manifest).read_text())
    figs = man["figures"] if isinstance(man, dict) else man
    pre = (man.get("prerequisites", {}) if isinstance(man, dict) else {}) or {}
    scratch = Path(tempfile.mkdtemp(prefix="regen_"))
    tar = subprocess.run(["git", "-C", str(repo), "archive", "HEAD"], capture_output=True, env=env)
    if tar.returncode or not tar.stdout:
        sys.exit(f"git archive produced nothing (rc={tar.returncode}): {tar.stderr.decode()[:200]}")
    subprocess.run(["tar", "-x", "-C", str(scratch)], input=tar.stdout, check=True)
    results = []
    for f in figs:
        rec = {"id": f.get("id"), "outputs": []}
        cmd = f.get("command")
        if not cmd:
            rec["status"] = "NO_GENERATOR"; results.append(rec); continue
        outs = [o for o in f.get("outputs", []) if not str(o).startswith("runtime:")]
        for o in outs:
            committed = repo / o
            rec["outputs"].append({"path": o, "committed_sha": sha(committed) if committed.exists() else None,
                                   "committed_renderer": png_software(committed) if committed.suffix == ".png" and committed.exists() else None})
            (scratch / o).unlink(missing_ok=True)
        if f.get("numeric"): (scratch / f["numeric"]).unlink(missing_ok=True)
        run_env = dict(env); run_env.update(pre.get("env", {})); run_env.update(f.get("env", {}))
        cwd = scratch / f.get("cwd", ".")
        try:
            p = subprocess.run(cmd, shell=True, cwd=cwd, env=run_env, capture_output=True, text=True, timeout=a.timeout)
        except subprocess.TimeoutExpired:
            rec["status"] = "FAILED_RUN"; rec["stderr_tail"] = "timeout"; results.append(rec); continue
        rec["rc"] = p.returncode; rec["stderr_tail"] = (p.stderr or "")[-1500:]
        if p.returncode:
            rec["status"] = "FAILED_RUN"; results.append(rec); continue
        missing = [o for o in outs if not (scratch / o).exists()]
        if missing:
            rec["status"] = "NOT_PRODUCED"; rec["missing"] = missing; results.append(rec); continue
        for o in rec["outputs"]:
            o["regen_sha"] = sha(scratch / o["path"]); o["regen_renderer"] = png_software(scratch / o["path"]) if o["path"].endswith(".png") else None
            o["byte_identical"] = o["regen_sha"] == o["committed_sha"]
        if all(o["byte_identical"] for o in rec["outputs"]):
            rec["status"] = "BYTE_IDENTICAL"
        elif f.get("numeric") and (repo / f["numeric"]).exists() and (scratch / f["numeric"]).exists():
            rec["numeric"] = numeric_diff(load_numeric(repo / f["numeric"]), load_numeric(scratch / f["numeric"]), a.rel_tol)
            rec["status"] = rec["numeric"]["status"]
        else:
            rec["status"] = "PIXEL_DIFF"
            rec["next"] = f"python pixel_localize.py {repo / outs[0]} {scratch / outs[0]}"
        results.append(rec)
    Path(a.out).write_text(json.dumps({"repo": str(repo), "scratch": str(scratch), "results": results}, indent=1))
    from collections import Counter
    print(Counter(r["status"] for r in results))
    for r in results:
        line = f'{r["status"]:15s} {r["id"]}'
        if r.get("numeric"): line += f'  worst_rel={r["numeric"]["worst_rel"]:.2e} ({r["numeric"]["worst_key"]})'
        print(line)
    print("scratch tree kept at", scratch)

if __name__ == "__main__":
    main()
