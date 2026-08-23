---
name: csv-data-summarizer
description: This skill should be used when the user asks to "summarize this CSV", "chart this data", "get insights from this dataset", "turn this CSV into a graph", or hands over a numeric dataset for a slide. It scans a CSV (stdlib only, no pandas), prints per-column summary statistics, and emits a Stoic-brand SVG chart ready to drop into a deck — then prompts annotating the one insight that matters.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# CSV Data Summarizer — dataset → brand chart + insight

Turn a raw CSV into (1) clean summary statistics and (2) an on-brand SVG chart, without hand-styling a
graph each time. The script does the mechanical part; the skill's job is to surface the **one insight**
the slide should make and annotate it.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`;
chart rules: the **data-viz-and-graphs** skill. Locally `~/StoicDesign`; in Claude Design,
`github.com/500ft/StoicDesign`.

## Use

```bash
python3 scripts/summarize_csv.py data.csv                       # stats + auto chart.svg
python3 scripts/summarize_csv.py data.csv --label region --value revenue --out rev.svg --top 8
```

- Prints JSON: row count, numeric columns, and per-column `count/sum/mean/median/min/max/stdev`.
- Writes a horizontal **bar chart SVG** in brand colors (`--wax` bars, parchment ground, hairline
  baseline, JetBrains Mono value labels, square 2px bars). Pure stdlib — runs anywhere with Python 3.

## Procedure

1. Run the script on the CSV; read the printed stats.
2. **Name the insight** — the one comparison/outlier/trend the slide must land (the script ranks and
   trims to top-N to make this obvious). Don't just show the data; state its point.
3. Drop the SVG into the deck / Claude Design canvas, then **annotate the insight** (mark the outlier,
   add the takeaway) per the design system's "annotate meaning, not just data" rule.
4. For line/area/slope encodings or multi-series charts, hand to **data-viz-and-graphs** to build the
   SVG (this script covers ranked bars / distributions); de-slop any image via **design-repair**.

## Notes

- Numbers are parsed leniently (`$`, `₮`, thousands commas stripped). Verify the auto-detected
  label/value columns; override with `--label` / `--value`.
- Keep it honest: consistent units and significant figures; cite the source on the slide (mono line).
- For heavy analysis (joins, regressions), escalate beyond this stdlib summarizer.
