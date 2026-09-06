#!/usr/bin/env python3
"""Point-level vs cluster vs leave-one-cluster-out intervals for a Pearson r.
usage: cluster_bootstrap.py data.csv [--cluster cluster] [--x x] [--y y] [--n 20000] [--seed 0]
"""
import argparse, csv, itertools, math
import numpy as np

def pearson(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    if x.std() == 0 or y.std() == 0: return float("nan")
    return float(np.corrcoef(x, y)[0, 1])

def fisher_ci(r, n, z=1.959964):
    if n <= 3 or abs(r) >= 1: return (r, r)
    zr = math.atanh(r); se = 1 / math.sqrt(n - 3)
    return (math.tanh(zr - z * se), math.tanh(zr + z * se))

def clopper_pearson_upper(k, n, alpha=0.05):
    from math import lgamma, exp
    # one-sided upper bound via bisection on the binomial CDF
    def cdf(p):
        return sum(exp(lgamma(n+1)-lgamma(i+1)-lgamma(n-i+1) + i*math.log(p) + (n-i)*math.log(1-p)) for i in range(0, k+1))
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if cdf(mid) > alpha: lo = mid
        else: hi = mid
    return hi

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("csv"); ap.add_argument("--cluster", default="cluster")
    ap.add_argument("--x", default="x"); ap.add_argument("--y", default="y"); ap.add_argument("--n", type=int, default=20000); ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()
    rows = list(csv.DictReader(open(a.csv)))
    groups = {}
    for r in rows: groups.setdefault(r[a.cluster], []).append((float(r[a.x]), float(r[a.y])))
    ids = sorted(groups); k = len(ids)
    X = [p[0] for g in ids for p in groups[g]]; Y = [p[1] for g in ids for p in groups[g]]
    r0 = pearson(X, Y); rng = np.random.default_rng(a.seed)
    print(f"n_points={len(X)} n_clusters={k}  pooled r={r0:.4f}")

    # point-level bootstrap
    idx = np.arange(len(X)); bs = []
    for _ in range(a.n):
        s = rng.choice(idx, len(idx)); bs.append(pearson(np.array(X)[s], np.array(Y)[s]))
    lo, hi = np.nanpercentile(bs, [2.5, 97.5]); print(f"point-level bootstrap 95% CI [{lo:.4f}, {hi:.4f}]  width {hi-lo:.4f}")

    # cluster bootstrap: exhaustive if k**k manageable
    total = k ** k
    combos = itertools.product(range(k), repeat=k) if total <= 200000 else (tuple(rng.integers(0, k, k)) for _ in range(a.n))
    cb = []
    for c in combos:
        xs = [p[0] for i in c for p in groups[ids[i]]]; ys = [p[1] for i in c for p in groups[ids[i]]]
        cb.append(pearson(xs, ys))
    cb = np.array(cb); lo, hi = np.nanpercentile(cb, [2.5, 97.5])
    print(f"cluster bootstrap     95% CI [{lo:.4f}, {hi:.4f}]  width {hi-lo:.4f}  ({'exhaustive ' if total <= 200000 else ''}{len(cb)} resamples)")
    if np.nanstd(cb) < 1e-12: print("!! DEGENERATE: every cluster resample gives the same statistic — a fact about the generator, not a precision claim")

    # leave-one-cluster-out jackknife in Fisher z
    loo = []
    for drop in ids:
        xs = [p[0] for g in ids if g != drop for p in groups[g]]; ys = [p[1] for g in ids if g != drop for p in groups[g]]
        loo.append(pearson(xs, ys))
    z = np.arctanh(np.clip(loo, -0.999999, 0.999999)); zbar = z.mean()
    se = math.sqrt((k - 1) / k * ((z - zbar) ** 2).sum())
    print(f"LOAO jackknife (Fisher z) 95% CI [{math.tanh(zbar-1.96*se):.4f}, {math.tanh(zbar+1.96*se):.4f}]  se_z {se:.4f}")

    # per-cluster and within-cluster
    per = {g: pearson([p[0] for p in groups[g]], [p[1] for p in groups[g]]) for g in ids}
    vals = np.array([v for v in per.values() if not math.isnan(v)])
    print(f"per-cluster r: median {np.median(vals):.4f} range [{vals.min():.4f}, {vals.max():.4f}]")
    if r0 < vals.min(): print("!! pooled r is BELOW every per-cluster r: pooling attenuates it; report the within-cluster estimand too")
    xw = [p[0] - np.mean([q[0] for q in groups[g]]) for g in ids for p in groups[g]]
    yw = [p[1] - np.mean([q[1] for q in groups[g]]) for g in ids for p in groups[g]]
    rw = pearson(xw, yw); print(f"within-cluster r (cluster-mean-centred) = {rw:.4f}  Fisher CI at n_points {fisher_ci(rw, len(X))}")
    print(f"\nreference: 0 of {len(X)} failures -> one-sided 95% upper bound {100*clopper_pearson_upper(0, len(X)):.2f}%")

if __name__ == "__main__":
    main()
