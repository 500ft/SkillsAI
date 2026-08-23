# Pin Math — formula, clamping algorithm, blueprint

## Formula

```
pct(year) = ((year − startYear) / (endYear − startYear)) × 100
```

## Clamping algorithm (keep crowded pins scannable)

Raw percentages can crowd (e.g. 2011 and 2012 over a 16-year span are ~6.25% apart < the 8% threshold).
Enforce a minimum buffer, then renormalize so the last pin still ends at 100%:

```
MIN_GAP = 10            // % minimum visual buffer
THRESHOLD = 8           // % below which a pair is "crowded"

raw = years.map(y => pct(y))            // proportional, ascending
adj = [raw[0]]
for i in 1..n-1:
    gap = raw[i] - adj[i-1]
    adj[i] = (gap < THRESHOLD) ? adj[i-1] + MIN_GAP : raw[i]
// renormalize so the spread still spans 0..100 (preserves the big honest gaps)
span = adj[last] - adj[0]
final = adj.map(v => (v - adj[0]) / span * 100)
```

This keeps tight clusters readable **without** flattening the large gaps that make the timeline honest —
the pandemic-era jump from 2012 → 2020 stays visually huge.

## Worked example — 2010–2026, pins 2011/2012/2020/2026

Span = 16. Raw: 2011→6.25%, 2012→12.5%, 2020→62.5%, 2026→100%.
2011 vs start-of-track is fine; 2011↔2012 gap = 6.25% < 8 → push 2012 to 16.25%. Renormalize to end at
100%. Result: a tight 2011/2012 pair at the left, a wide leap to 2020, final **gold** pin at 100% right.

## HTML/CSS blueprint (brand tokens)

```html
<div class="tl" style="position:relative; width:100%; height:220px;">
  <div class="tl-line" style="position:absolute; top:48px; left:0; width:100%; height:2px;
       background:var(--data-gold);"></div>

  <!-- one per milestone; left = final[i] -->
  <div class="tl-pin" style="position:absolute; left:16.25%; transform:translateX(-50%); top:0;">
    <div class="dot" style="width:12px; height:12px; background:var(--ink); border-radius:999px;
         margin:42px auto 12px;"></div>
    <div class="card" style="max-width:180px; text-align:left;">
      <span style="font:500 12px var(--font-mono); color:var(--ink-muted); display:block;">2012</span>
      <h4 style="font:500 15px var(--font-display); color:var(--ink); margin:4px 0;">Title</h4>
      <p style="font:400 12px var(--font-ui); color:var(--ink-muted); line-height:1.4;">Description.</p>
    </div>
  </div>

  <!-- final / active pin: gold, larger, ringed -->
  <div class="tl-pin" style="position:absolute; left:100%; transform:translateX(-50%); top:0;">
    <div class="dot" style="width:18px; height:18px; background:var(--data-gold); border-radius:999px;
         box-shadow:0 0 0 6px rgba(190,147,58,.18); margin:39px auto 12px;"></div>
    <div class="card" style="max-width:180px;"> … 2026 … </div>
  </div>

  <!-- below-line global alert: cleared under the lowest card, full width -->
  <div class="tl-alert" style="position:absolute; left:0; right:0; bottom:0;
       font:500 13px var(--font-ui); color:var(--data-neg);">⚠ Global note spans the full track width.</div>
</div>
```

Notes: on a navy ground swap `--ink`→`--cream`, `--ink-muted`→`--cream-muted`. Alternate card placement
above/below the line for dense clusters (reuse `timeline-and-shapes` odd/even rule). Hand crowded
clusters to **label-collision-preventer**; balance cards with **layout-density-optimizer**.

> **Edge pins (must-do, else the card clips off-canvas).** `translateX(-50%)` centers a card on its dot —
> fine in the interior, but a pin at **0%** or **100%** then pushes half its card past the track edge. At
> the extremes, keep the dot on the date but anchor the **card inward**: at 0% left-align it to the dot
> (`left:0; transform:none`), at 100% right-align it (`right:0; text-align:right`). This is the same
> edge-anchoring rule **label-collision-preventer** applies near a chart's edges. Verified against
> `examples/pipeline-demo.html` (the 2026 gold pin).

## PowerPoint (python-pptx) equivalent

Compute `final[]` the same way, then place each pin at `left = Inches(slide_w_in * final[i]/100)`; draw
the track as a 2px line shape in `--data-gold`. Reuse the helpers in **pptx-native-writer**.
