---
name: design-V0.1
description: This skill should be used when the user asks to "make slides for my lesson", "turn this lesson plan into a deck", "build a Stoic Education deck", "give me a slide-by-slide breakdown", "make a YouTube lesson slide deck", "build the deck behind my voiceover", or invokes /design-V0.1. It converts a lesson plan (and optional outline) into a graphics-heavy, narrate-over slide deck in the Stoic design system — either as a slide-by-slide breakdown (each slide's layout + visual + generation prompt + narration beat) or as a built deck (single-file HTML, or a portable build for Claude Design). It orchestrates the design-taste, design-creativity, design-legibility, and design-repair skills.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# design-V0.1 — Stoic lesson-deck builder

Turn a lesson plan into a deck that **plays behind a voiceover**: graphics-heavy, one idea per
slide, calm motion, unmistakably Stoic. The deck never reproduces the script — it gives the eye one
thing to hold while the narration does the talking.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`;
anti-AI rules: `design-system/anti-ai-rules.md`; slide patterns: `references/slide-archetypes.md`;
pacing: `references/voiceover-pacing.md`; deck skeleton: `assets/deck-template.html`. Locally the
repo is usually `~/StoicDesign`; in Claude Design, read it from `github.com/500ft/StoicDesign`.

## Inputs

- **Lesson plan** (required) — the content/argument, in any form.
- **Outline** (optional) — an existing slide list; if given, honor its order and granularity.
- **Lesson meta** — module/lesson number, lesson title (for the spine), target slide count.
- If the lesson plan is thin, draft real content from it — never lorem ipsum, never `[placeholder]`.

## Two modes

### Mode A — Breakdown  ("how this lesson should be prompted")
Produce a slide-by-slide spec, losing **no** detail from the lesson plan. One block per slide:

```
SLIDE 04 — Enumerated breakdown — ground: parchment
KICKER:    THE FOUR REAL COSTS · 4-YEAR TOTALS
HEADLINE:  Families count two. There are four.
ONE IDEA:  the real total is ~40% higher than families budget
ON-SCREEN (≤20 words + data): four rows, value chips, "REAL TOTAL ≈ $340K"
VISUAL:    numbered cost rows, bar-weight per cost; CSS/SVG (no image)
REVEALS:   1) tuition  2) +room/board  3) +travel/visa  4) +opportunity cost  5) total
NARRATION BEAT: "...the two costs nobody puts on the website..."
GEN PROMPT: <paste-ready prompt to build this slide in Claude Design / HTML>
```

Cover **every** point in the lesson plan; if a point doesn't fit one slide, split it. End with a
coverage check: list lesson-plan points → slide numbers, and flag anything not yet placed.

### Mode B — Build
Render the deck. Default target = a **single-file HTML deck** from `assets/deck-template.html`;
when the user is in **Claude Design**, instead emit the portable build prompt (tokens + per-slide
specs) for claude.ai/design to generate, since it pulls this repo via GitHub.

Build steps:
1. Read the design system; copy its `:root` tokens; load the deck skeleton.
2. For each slide, pick an archetype from `references/slide-archetypes.md` and fill it with real content.
3. Build every chart as **inline SVG** in brand colors (framed, end-labeled, annotated, captioned) —
   never a pasted Office chart. See the data-viz rules in the system.
4. Apply motion from the system (700ms dissolve, staged reveals, count-ups, reduced-motion).
5. Wire the spine: footer `STOIC EDU · <title>` + `NN / total`, section kicker, seal on title/divider/close.
6. **Gate:** run **design-taste**. Fix until verdict = SHIP. Route occlusion issues to
   **design-legibility**, broken visuals to **design-repair**.

## Visual sourcing (graphics-heavy, but earned)

Decide per slide, cheapest competent source first:
- **CSS/SVG** — charts, diagrams, kinetic typography, number counters, bar/line/area. **Default.**
- **Excalidraw** (excalidraw-diagram-generator) — mechanism/flow/system diagrams when a hand-drawn
  schematic explains better than a chart.
- **AI image** — only for a hero/illustration a slide genuinely needs (a portrait, a scene, a
  texture). Generate via the imagegen system skill, then **always** run **design-repair** to de-slop
  it and palette-match it to the brand before placing.
- **Icons** — line icons, sparingly; never emoji-as-icons.

Graphics-heavy means *visual density of meaning*, not decoration: a slide earns its visual by making
the idea faster to grasp than text would.

## Running in both Claude and Claude Design

- **Claude / Claude Code:** write the HTML deck to disk from the skeleton; open/screen-record it.
- **Claude Design (claude.ai/design):** output is a build prompt — the `:root` tokens, the font
  links, and the per-slide archetype specs — phrased so Claude Design generates on-brand slides.
  Keep it tool-agnostic: no instruction should depend on a Claude-Code-only feature.

## Orchestration

This skill is the conductor. It calls:
- **design-creativity** — upstream, when a slide's concept is generic or the lesson needs an art
  direction / visual metaphor system.
- **design-taste** — the mandatory pre-ship gate.
- **design-legibility** — when text is covered/occluded after layout.
- **design-repair** — when an image, chart, or shape is broken or looks AI.

## Definition of done

- Every lesson-plan point is on a slide (coverage check passes).
- design-taste verdict = **SHIP** (no hard-gate failure).
- Deck is navigable (arrows/click), has the spine, exports cleanly (print = one slide/page), and
  honors reduced motion.

For slide layouts read `references/slide-archetypes.md`; for word budgets, beats, and reveal timing
read `references/voiceover-pacing.md`.
