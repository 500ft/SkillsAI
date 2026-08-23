---
name: slide-deck-builder
description: This skill should be used when the user asks to "outline my deck", "plan the slides", "structure this into slides", "turn this doc/idea into a slide sequence", "what slides do I need", or "map this out before designing". It converts a rough idea or document into a precise, numbered slide sequence with a narrative arc — one idea per slide — BEFORE any design or code happens. For Stoic lesson decks it hands the sequence to design-V0.1; for other decks, to pptx-native-writer or html-slides-engine.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Slide Deck Builder — structure before design

The most expensive slide mistake is designing before the narrative exists. This skill forces the
sequence first: a numbered list of one-idea slides with a clear arc, signed off before a single pixel
is placed.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`.
Locally usually `~/StoicDesign`; in Claude Design read from `github.com/500ft/StoicDesign`.

## Procedure

1. **Extract the spine** — thesis (one sentence), audience, and the single takeaway the viewer leaves with.
2. **Segment** the source into **one-idea units** — split anything carrying two ideas; merge fragments.
3. **Order into an arc** — hook → context → evidence → turn → payoff → recap → close. Every slide earns
   its place by moving the arc forward.
4. **Spec each slide** as a numbered row: working **action title** (a full-sentence assertion of the
   slide's point), the one idea, and the intended visual/archetype.
5. **Coverage check** — map every source point to a slide number; flag anything unplaced or doubled.
6. **Get sign-off**, then hand to a build engine. Do **not** design before the sequence is approved.

## Output format

```
DECK PLAN — <title>   Thesis: <one sentence>   Takeaway: <one sentence>
01 [Title]     <action title>                         · idea · visual/archetype
02 [Hook]      Same school, same cost, two outcomes.   · contrast · two big numbers
03 ...
Coverage: source §1→S2-3 · §2→S4 · (unplaced: none)
```

## Hand off

- **Stoic lesson deck** → this *is* design-V0.1 **Breakdown** mode; continue there for the full
  per-slide visual + generation prompt + narration beats.
- **Corporate/academic deck** → pass the plan to **academic-pptx-skill** (titles + citations), then to
  **pptx-native-writer** (native `.pptx`) or **html-slides-engine** (HTML).

## Rules

- One idea per slide; the arc is explicit, not implied.
- Titles assert, they don't label ("Need-blind aid erases the cost cliff," not "Financial Aid").
- No design, theme, or code until the numbered sequence is approved.
