---
name: academic-pptx-skill
description: This skill should be used when the user asks for an "academic deck", "corporate/research presentation", "action titles", "complete-sentence slide titles", "cite sources in slides", or wants rigorous, citation-disciplined formatting for a complex or corporate topic. It overrides vague default layouts by forcing assertion (action) titles and strict citation discipline, harmonized to the Stoic design system.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Academic / Corporate Slides — action titles + citation discipline

Default decks title slides with topics ("Financial Aid") and leave claims un-sourced. For serious or
corporate material that fails. This skill enforces two disciplines: **assertion titles** and
**citations on every claim** — within the Stoic look.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`
(type, the `FIGURE n ·` + mono source-line conventions). Locally `~/StoicDesign`; in Claude Design,
`github.com/500ft/StoicDesign`.

## Rule 1 — Action (assertion) titles

Every slide title is a **complete sentence stating the slide's conclusion**, and the body proves it.

- ✅ "Need-blind aid erases the cost cliff for ~15 U.S. schools."
- ❌ "Financial Aid" / "Costs Overview" / "Background."

If the body doesn't prove the title, the title is wrong or the slide is unfocused. One claim per slide.

## Rule 2 — Citation discipline

- Every figure and non-obvious claim carries a source. Use a short inline cite where the claim sits and
  a **mono source line** under each figure (`Source: NACE 2024 · Glassdoor UB`), per the design system.
- Consolidate full references on a **Sources** slide near the close.
- No number appears without provenance. Keep units and significant figures consistent across a slide.

## Formatting (within the Stoic system)

- Set type in Fraunces / Inter / JetBrains Mono; titles are Fraunces, sized down from display since they
  are sentences (use `--t-h3`/`--t-h2`, not `--t-display`).
- Tables and figures are labeled (`Figure n ·`, `Table n ·`), framed, brand-colored — never Office defaults.
- Stay restrained: one claim, its evidence, its source. No decorative filler.

## Hand off

- Plan first with **slide-deck-builder** (assertion titles belong in the plan).
- Build native `.pptx` with **pptx-native-writer**, or HTML with **design-V0.1** / **html-slides-engine**.
- Charts via **data-viz-and-graphs**; final pass through **design-taste**.
