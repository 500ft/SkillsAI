---
name: deep-planning
description: This skill should be used when the user asks to "plan deeply", "break down this topic", "decompose before building", "verify layout edge cases", or "think through the deck structure" for an abstract or complex presentation. It decomposes a topic into atomic components and self-verifies layout edge cases (overflow, illegible charts, label collisions, missing sources) BEFORE any content is drafted, producing a verified plan with risks resolved.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Deep Planning — decompose, then self-verify before drafting

Complex topics fail when drafting starts before the structure and its failure modes are understood.
This skill decomposes the topic and pre-solves the layout edge cases, so the build starts from a plan
that already survives its own hard cases.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`
(word budgets, grid, data-viz, motion). Locally `~/StoicDesign`; in Claude Design,
`github.com/500ft/StoicDesign`.

## Procedure

1. **Decompose** the topic into atomic concepts and their dependencies (what must be understood before
   what). Order follows dependency, not the source document's order.
2. **Map** each concept to a slide and an intended visual/archetype.
3. **Self-verify edge cases** — for each slide, check the failure modes below and **resolve each in the
   plan** (split a slide, cut words, choose a different encoding, add a source).
4. **Output a verified plan** with the risks and their resolutions noted.
5. Only then draft / build.

## Edge-case checklist (resolve before drafting)

- **Word budget** — does any slide exceed ~20 on-screen words (narrate-over) or carry >1 idea? → split.
- **Chart legibility** — will this data read at slide size? Too many series/points? → re-encode or reduce.
- **Label collisions** — will any label overlap a shape/series/footer? → pre-place, or flag for
  **design-legibility**.
- **Missing data/sources** — is every number sourced and consistent? → mark gaps to fill.
- **Concept overflow** — does a concept actually need two slides? → split now, not mid-build.
- **Motion vs. voice** — will any reveal/animation fight the narration? → simplify.

## Relationship to other skills

Complements **slide-deck-builder** (narrative sequence) and the general **grill-me** / **write-plan**
skills — but scoped to *slide/layout* risk. Hands the verified plan to **design-V0.1** (Stoic) or the
chosen build engine.
