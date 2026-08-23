---
name: pptx-native-writer
description: This skill should be used when the user asks to "make a native pptx", "editable PowerPoint file", "generate a .pptx", "python-pptx deck", "enterprise/corporate PowerPoint", or wants a true editable Microsoft PowerPoint output (not markdown or HTML). It builds a real .pptx in the Stoic design system via python-pptx from a JSON deck spec and a brand guide.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# PPTX Native Writer — true editable PowerPoint, on-brand

Some contexts need a real `.pptx` the user can open and edit in PowerPoint/Keynote, not an HTML deck.
This skill generates one via `python-pptx`, applying the Stoic brand (navy/parchment grounds, Fraunces/
Inter/JetBrains Mono, wax accent, footer spine) from a JSON spec.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`; the
`.pptx`-side mirror of the tokens is `assets/brand_guide.json` (keep the two in sync). Locally
`~/StoicDesign`; in Claude Design, `github.com/500ft/StoicDesign`.

## Workflow

1. **Plan** the sequence with **slide-deck-builder**; write **action titles** (**academic-pptx-skill**).
2. **Author a deck spec** as JSON (schema below) — one entry per slide.
3. **Generate:**
   ```bash
   pip install python-pptx        # one-time
   python3 scripts/generate_deck.py --spec deck.json \
           --brand assets/brand_guide.json --out deck.pptx
   ```
   A runnable example ships at `assets/example_deck.json`:
   ```bash
   python3 scripts/generate_deck.py --spec assets/example_deck.json \
           --brand assets/brand_guide.json --out example.pptx
   ```
4. Open in PowerPoint — every element is native and editable.

## Deck spec schema

```json
{
  "lesson": "True ROI of a U.S. Degree",
  "slides": [
    {"type":"title",   "kicker":"Stoic Education · Lesson 0.3", "title":"The true ROI of a U.S. degree", "subtitle":"..."},
    {"type":"section", "kicker":"Part One", "title":"The four real costs"},
    {"type":"content", "kicker":"The Four Real Costs", "title":"Families count two of the four costs.", "bullets":["...","..."]},
    {"type":"stat",    "kicker":"Opportunity cost", "stat":"$40–80K", "caption":"The income you didn't earn in 4 years."},
    {"type":"close",   "kicker":"Stoic Education", "title":"Now you can run the number.", "subtitle":"Next — Lesson 1.1", "sources":"NACE 2024 · IRS SOI"}
  ]
}
```

Slide types: `title`, `section`, `stat`, `close` (navy grounds) and `content` (parchment). Every slide
gets the footer spine (`STOIC EDU · lesson` + `NN / total`).

## Notes

- **Fonts:** the script sets Fraunces/Inter/JetBrains Mono by name; if they aren't installed on the
  machine opening the file, PowerPoint substitutes — install the fonts for exact rendering.
- **Real corporate template:** to start from an enterprise `.potx`, drop it in `assets/` and open it
  with `Presentation("assets/your_template.potx")` instead of a blank deck; the helpers still apply.
- **Charts:** generate brand SVG/PNG via **csv-data-summarizer** / **data-viz-and-graphs** and add as
  pictures, or extend the script with native `python-pptx` charts for fully-editable graphs.
- Keep `brand_guide.json` synced to `design-system/` — it is the single source of truth, mirrored.
