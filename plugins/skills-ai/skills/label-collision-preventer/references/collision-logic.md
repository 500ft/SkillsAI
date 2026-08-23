# Collision Logic — offset algorithm, anchoring table, template

## Vertical-offset algorithm (cluster on a curve)

```
SAFE = 16          // px min gap between label boxes
LEVELS = [0, 28, 56, 84]   // px guide-line lengths (short → tall), cycle as needed

sort points by x
level = 0
for i, p in points:
    if i > 0 and (p.xPct - points[i-1].xPct) < 10:   // crowded horizontally
        level = (level + 1) % LEVELS.length            // step to a taller guide line
    else:
        level = 0                                       // reset when there's room
    p.guideLen = LEVELS[level]
    p.labelY  = baseY - p.guideLen - SAFE
```

Result: adjacent labels ride guide lines of different lengths, so their text boxes never share a height.

## Anchoring decision table

| Local situation | Place text |
|---|---|
| Curve sloping **down**→right | above and slightly **right** of the dot |
| Curve sloping **up**→right | above and slightly **left** of the dot |
| Points extremely close | **alternate** left/right of the dot per index parity |
| Near the right edge (<120px room) | anchor text **left**, right-align to the dot |
| Near the left edge | anchor text **right**, left-align to the dot |

## Density escape hatch

If after offsetting any two label boxes still overlap (gap < SAFE), **cluster**: replace the group with a
single dot labeled `Cluster (n)` and write the detail into a footnote container below the chart baseline.
Honest and readable beats crammed.

## HTML/CSS annotation-node template (brand tokens)

```html
<div class="ann" style="position:absolute; left:[X]%; bottom:0; display:flex; flex-direction:column;
     align-items:center;">
  <div class="label" style="text-align:center; margin-bottom:8px; max-width:120px; line-height:1.25;
       transform:translateY([-labelY]px);">
    <span style="font:400 11px var(--font-ui); color:var(--ink-muted); display:block;">≈ 94th pct</span>
    <strong style="font:500 16px var(--font-mono); color:var(--wax); display:block;
            font-variant-numeric:tabular-nums;">1400</strong>
  </div>
  <div class="dot" style="width:8px; height:8px; background:var(--data-gold); border-radius:999px;"></div>
  <div class="guide" style="width:1px; border-left:1px dashed var(--data-gold); height:[guideLen]px;
       opacity:.6;"></div>
</div>
```

On a navy ground swap `--ink-muted`→`--cream-muted`. Reveal labels *after* the chart/curve draws (see
**cinematic-chart-animations**) so they never animate into each other.

## Matplotlib / static charts

Same idea: vary `annotate(xytext=...)` y-offsets per cluster index, set `wrap=True` with a width cap, and
for unresolvable density drop a single marker + a figure caption with the summary stat.
