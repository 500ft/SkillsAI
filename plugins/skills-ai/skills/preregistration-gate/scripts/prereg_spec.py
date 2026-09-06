#!/usr/bin/env python3
"""Write, hash and verify a preregistration spec.

  prereg_spec.py write  <id> --quantity ... --statistic ... --threshold ... --unit ... \
                        --protocol ... --disagreement-means ... [--fixed key=value ...] \
                        [--results-glob "data/**/<id>*"] [--out prereg/<id>.json]
  prereg_spec.py verify <spec.json>          # hash unchanged, and the spec predates any results file

Refuses to WRITE if a results file matching --results-glob already exists: a threshold written
after the result is not a preregistration.
"""
import argparse, glob, hashlib, json, subprocess, sys, time
from pathlib import Path

def canonical(d): return json.dumps(d, sort_keys=True, separators=(",", ":")).encode()
def git_head():
    try: return subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    except Exception: return None

def write(a):
    hits = glob.glob(a.results_glob, recursive=True) if a.results_glob else []
    if hits:
        sys.exit(f"REFUSED: results already exist for this id ({hits[:3]}). A threshold written after the result is not preregistered.")
    body = {
        "id": a.id, "quantity": a.quantity, "statistic": a.statistic,
        "threshold": a.threshold, "unit": a.unit, "comparison": a.comparison,
        "protocol": a.protocol, "disagreement_means": a.disagreement_means,
        "fixed_after_registration": dict(kv.split("=", 1) for kv in a.fixed),
        "analysis_code_commit": git_head(), "registered_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    }
    body["sha256"] = hashlib.sha256(canonical({k: v for k, v in body.items() if k != "sha256"})).hexdigest()
    out = Path(a.out or f"prereg/{a.id}.json"); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(body, indent=1) + "\n")
    print(f"wrote {out}  sha256 {body['sha256'][:16]}...  (commit this BEFORE generating any result)")

def verify(a):
    spec = json.loads(Path(a.spec).read_text())
    h = spec.pop("sha256", None)
    ok = h == hashlib.sha256(canonical(spec)).hexdigest()
    print("hash", "OK" if ok else "MISMATCH - spec was edited after registration")
    if a.results_glob:
        for p in glob.glob(a.results_glob, recursive=True):
            m = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(Path(p).stat().st_mtime))
            print(f"  result {p} mtime {m}  registered {spec['registered_utc']}  ->", "OK" if m > spec["registered_utc"] else "!! result predates registration")
    sys.exit(0 if ok else 1)

def main():
    ap = argparse.ArgumentParser(); sub = ap.add_subparsers(dest="cmd", required=True)
    w = sub.add_parser("write"); w.add_argument("id")
    for k in ("quantity", "statistic", "threshold", "unit", "protocol", "disagreement_means"):
        w.add_argument(f"--{k.replace('_', '-')}", required=True, dest=k)
    w.add_argument("--comparison", default=">=", choices=[">=", "<=", "within"])
    w.add_argument("--fixed", nargs="*", default=[]); w.add_argument("--results-glob", default=None); w.add_argument("--out", default=None)
    w.set_defaults(fn=write)
    v = sub.add_parser("verify"); v.add_argument("spec"); v.add_argument("--results-glob", default=None); v.set_defaults(fn=verify)
    a = ap.parse_args(); a.fn(a)

if __name__ == "__main__":
    main()
