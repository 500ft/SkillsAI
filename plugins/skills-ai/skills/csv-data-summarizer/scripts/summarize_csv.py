#!/usr/bin/env python3
"""summarize_csv.py — scan a CSV, print numeric summaries, emit a Stoic-brand SVG bar chart.

Stdlib only (no pandas). Part of the StoicDesign `csv-data-summarizer` skill.

Usage:
  python3 summarize_csv.py data.csv
  python3 summarize_csv.py data.csv --label region --value revenue --out chart.svg --top 8
"""
import csv, sys, json, argparse
import statistics as st

# Stoic brand tokens (keep in sync with design-system/stoic-design-system.md)
WAX = "#2C49A6"; INK = "#19233A"; MUTED = "#5C6577"; PARCH = "#F6F1E7"; RULE = "rgba(25,35,58,.14)"


def is_number(x):
    try:
        float(str(x).replace(",", "").replace("$", "").replace("₮", "").strip())
        return True
    except (ValueError, TypeError):
        return False


def to_number(x):
    return float(str(x).replace(",", "").replace("$", "").replace("₮", "").strip())


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("empty csv")
    return rows


def numeric_cols(rows):
    out = []
    for c in rows[0].keys():
        vals = [r[c] for r in rows if r[c] not in (None, "")]
        if vals and all(is_number(v) for v in vals):
            out.append(c)
    return out


def summarize(rows, cols):
    summary = {}
    for c in cols:
        v = [to_number(r[c]) for r in rows if r[c] not in (None, "")]
        summary[c] = {
            "count": len(v), "sum": sum(v), "mean": st.mean(v), "median": st.median(v),
            "min": min(v), "max": max(v), "stdev": st.pstdev(v) if len(v) > 1 else 0.0,
        }
    return summary


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def svg_bar(rows, label_col, value_col, out, top):
    data = [(r[label_col], to_number(r[value_col])) for r in rows if r[value_col] not in (None, "")]
    data.sort(key=lambda x: -x[1])
    data = data[:top]
    W, rowH, padL, padR, padT, padB = 900, 46, 220, 120, 60, 40
    H = padT + padB + rowH * len(data)
    mx = max((v for _, v in data), default=1) or 1
    barW = W - padL - padR
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="Inter,system-ui,sans-serif">']
    p.append(f'<rect width="{W}" height="{H}" fill="{PARCH}"/>')
    p.append(f'<text x="{padL}" y="34" font-size="15" font-weight="600" letter-spacing="2" fill="{WAX}">{esc(value_col).upper()}</text>')
    for i, (lab, val) in enumerate(data):
        y = padT + i * rowH
        w = barW * (val / mx)
        p.append(f'<text x="{padL-16}" y="{y+24}" text-anchor="end" font-size="15" fill="{INK}">{esc(lab)}</text>')
        p.append(f'<rect x="{padL}" y="{y+8}" width="{w:.1f}" height="24" rx="2" fill="{WAX}"/>')
        p.append(f'<text x="{padL+w+10:.1f}" y="{y+25}" font-size="14" font-family="JetBrains Mono,monospace" fill="{MUTED}">{val:,.0f}</text>')
    p.append(f'<line x1="{padL}" y1="{padT}" x2="{padL}" y2="{H-padB}" stroke="{RULE}"/>')
    p.append("</svg>")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(p))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--label"); ap.add_argument("--value")
    ap.add_argument("--out", default="chart.svg"); ap.add_argument("--top", type=int, default=10)
    a = ap.parse_args()
    rows = load(a.csv)
    nums = numeric_cols(rows)
    summ = summarize(rows, nums)
    print(json.dumps({"rows": len(rows), "numeric_columns": nums, "summary": summ}, indent=2, default=float))
    label = a.label or next((c for c in rows[0] if c not in nums), None)
    value = a.value or (nums[0] if nums else None)
    if label and value:
        path = svg_bar(rows, label, value, a.out, a.top)
        print(f"\nSVG chart -> {path}  (label={label}, value={value}, top={a.top})", file=sys.stderr)
    else:
        print("\n(no label+value pair found for a chart; pass --label/--value)", file=sys.stderr)


if __name__ == "__main__":
    main()
