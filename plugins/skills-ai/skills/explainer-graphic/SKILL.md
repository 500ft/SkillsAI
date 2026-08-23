---
name: explainer-graphic
description: This skill should be used when the user asks for an "explainer graphic", "interactive diagram", "step-by-step visual", "visual analogy", or wants to turn a dry concept or process into an interactive visual map on the slide canvas. It generates a self-contained HTML/CSS (optionally JS) explainer in the Stoic design system, revealing a concept step by step.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Explainer Graphic — concepts as interactive visual maps

Some ideas land far faster as a built visual than as text: a process, a cause→effect chain, an analogy.
This skill turns one such idea into a self-contained interactive graphic that reveals step by step, on
brand, paced for narration.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`;
motion: the **slide-animations-engine** skill; concepts: **design-creativity**. Locally `~/StoicDesign`;
in Claude Design, `github.com/500ft/StoicDesign`.

## Procedure

1. **Name the one concept** and the mental model that explains it (a flow, a crossover, a waterline, an
   analogy). If the obvious model is weak, pull a stronger one from **design-creativity**.
2. **Decompose into 3–6 steps**, each a single move in the explanation.
3. **Build** a self-contained HTML/CSS graphic: nodes/stages on the grid, brand colors, hairline
   connectors, JetBrains Mono for any numbers. Add light JS only if interaction (hover/step) earns it.
4. **Reveal step by step** using the brand motion (fade-in-up, staggered) so each step maps to a
   narration beat — see **slide-animations-engine**.
5. Verify text isn't occluded (**design-legibility**) and score with **design-taste**.

## On-brand rules

- Use the design-system tokens only — `--wax` for the active/highlighted step, `--ink-muted`/`--cream-muted`
  for inactive, hairlines for connectors. No emoji-icons, no clip-art, no gradients-as-decoration.
- Prefer SVG/CSS for shapes and connectors; an Excalidraw schematic is fine for hand-drawn mechanism
  diagrams (use the excalidraw-diagram-generator skill).
- Keep labels short; the narration carries the detail. Each step has one focal element.

## Output

A single embeddable HTML block (or `<section>` slide) that drops into the deck or Claude Design canvas,
plus the step-reveal order so it can be driven by arrow keys / narration beats.
