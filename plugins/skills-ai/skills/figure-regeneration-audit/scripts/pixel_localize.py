#!/usr/bin/env python3
"""Localise a PNG difference by POSITION, and test whether it is data or rendering.

usage: pixel_localize.py committed.png regenerated.png [--band 50] [--data-colors "#d55e00,#0072b2"]

Reports: per-row-band differing pixel counts, axes-frame rows/cols in both images (did the
frame move?), differing pixels strictly inside the axes, and how many differing pixels carry
a data-line colour. All counts are RGB max-channel; do not mix with a grayscale pass.
"""
import argparse, sys
import numpy as np
from PIL import Image

def frames(g, frac=0.25):
    dark = g < 120
    rows = np.nonzero(dark.sum(axis=1) > frac * g.shape[1])[0]
    cols = np.nonzero(dark.sum(axis=0) > frac * g.shape[0])[0]
    return rows, cols

def hexrgb(s):
    s = s.strip().lstrip("#"); return tuple(int(s[i:i+2], 16) for i in (0, 2, 4))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a"); ap.add_argument("b"); ap.add_argument("--band", type=int, default=50)
    ap.add_argument("--data-colors", default="", help="comma-separated hex colours of data lines")
    ap.add_argument("--color-tol", type=int, default=40)
    x = ap.parse_args()
    A = np.asarray(Image.open(x.a).convert("RGB")).astype(int)
    B = np.asarray(Image.open(x.b).convert("RGB")).astype(int)
    if A.shape != B.shape:
        sys.exit(f"shapes differ: {A.shape} vs {B.shape} -> canvas changed; compare after checking dpi/figsize")
    m = np.abs(A - B).max(axis=2) > 0
    n = int(m.sum()); print(f"differing pixels: {n} of {m.size} ({100*m.mean():.3f}%)")
    if n == 0: return
    rows = m.sum(axis=1)
    print("per-band counts (row0 = top):")
    for y in range(0, m.shape[0], x.band):
        c = int(rows[y:y+x.band].sum())
        if c: print(f"  rows {y:4d}-{min(y+x.band-1, m.shape[0]-1):4d}: {c}")
    ga = np.asarray(Image.open(x.a).convert("L")).astype(int); gb = np.asarray(Image.open(x.b).convert("L")).astype(int)
    ra, ca = frames(ga); rb, cb = frames(gb)
    print(f"axes-frame rows committed={ra.tolist()[:6]} regenerated={rb.tolist()[:6]}")
    print(f"axes-frame cols committed={ca.tolist()[:6]} regenerated={cb.tolist()[:6]}")
    moved = (len(ra) and len(rb) and (ra.min() != rb.min() or ra.max() != rb.max())) or \
            (len(ca) and len(cb) and (ca.min() != cb.min() or ca.max() != cb.max()))
    if moved: print("!! axes frame MOVED -> layout shift; data-coloured diffs are NOT evidence of data change. Use the numeric output.")
    if len(ra) >= 2:
        r0, r1 = ra.min() + 2, ra.max() - 2
        inside = int(m[r0:r1].sum())
        print(f"differing pixels strictly inside axes rows {r0}-{r1}: {inside}   outside (text bands): {n - inside}")
    if x.data_colors:
        cols = [hexrgb(c) for c in x.data_colors.split(",") if c.strip()]
        ys, xs = np.nonzero(m); pa, pb = A[ys, xs], B[ys, xs]
        hit = 0
        for c in cols:
            hit += int(((np.abs(pa - c).max(axis=1) <= x.color_tol) | (np.abs(pb - c).max(axis=1) <= x.color_tol)).sum())
        print(f"differing pixels carrying a data-line colour (tol {x.color_tol}): {hit}")
    d = (A.astype(float) - B.astype(float))[m]
    print(f"signed diff over differing px: mean {d.mean():+.2f} std {d.std():.1f} min {d.min():+.0f} max {d.max():+.0f}"
          "  (symmetric about 0 on white = glyph edges)")

if __name__ == "__main__":
    main()
