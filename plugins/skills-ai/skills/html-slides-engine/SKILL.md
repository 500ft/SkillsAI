---
name: html-slides-engine
description: This skill should be used when the user asks for an "HTML presentation", "Reveal.js deck", "Slidev deck", "animated keyboard-navigable slides", or a web-based deck framework. It renders the Stoic design system into a navigable, animated HTML presentation — either the self-contained deck template, or a Reveal.js/Slidev project themed to the brand.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# HTML Slides Engine — navigable animated web decks

For a deck that lives on the web — keyboard-navigable, animated, exportable — pick the lightest engine
that fits, and theme it to the Stoic brand rather than accepting framework defaults.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`; the
reference implementation is `design-V0.1/assets/deck-template.html`; motion via
**slide-animations-engine**. Locally `~/StoicDesign`; in Claude Design, `github.com/500ft/StoicDesign`.

## Choose the engine

- **Self-contained template (default).** Reuse `design-V0.1/assets/deck-template.html` — one file,
  brand tokens, transitions, staged reveals, auto-advance, inline-SVG charts, print-to-PDF. No
  dependencies. Best for narrate-over lesson decks and quick delivery.
- **Reveal.js.** When the user wants a known framework, fragment system, speaker notes, and plugins.
  Theme it to the brand (below).
- **Slidev.** When the deck is authored in Markdown + Vue components and lives in a dev workflow.

## Theme Reveal.js to Stoic

Drop the design-system `:root` tokens into a custom theme and override Reveal's variables:

```css
:root{ /* paste the design-system :root tokens here */ }
.reveal{ font-family:var(--font-ui); color:var(--ink); background:var(--parchment); }
.reveal section.navy{ background:var(--navy); color:var(--cream); }
.reveal h1,.reveal h2,.reveal h3{ font-family:var(--font-display); letter-spacing:-.02em; text-transform:none; }
.reveal .kicker{ font:600 .42em var(--font-ui); letter-spacing:.16em; text-transform:uppercase; color:var(--wax); }
.reveal .num,.reveal .mono{ font-family:var(--font-mono); font-variant-numeric:tabular-nums; }
```

Set transitions to brand calm: `Reveal.initialize({ transition:'fade', transitionSpeed:'slow', controls:true, progress:true })`.
Use `.fragment` for staged reveals (timing per **slide-animations-engine**).

## Rules

- Same tokens, same grounds, same spine (footer + kicker + numbering) regardless of engine.
- Charts are inline SVG in brand colors (**data-viz-and-graphs** / **csv-data-summarizer**), never
  framework default chart styles.
- Honor `prefers-reduced-motion`; ensure print/PDF renders one slide per page.
- Final pass through **design-taste**.
