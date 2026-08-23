---
name: design-creativity
description: This skill should be used when the user asks for "visual ideas for this slide/lesson", says a slide is "boring / generic / obvious", asks for "art direction", "a visual metaphor for X", "make this concept stronger", "design creativity", or "how should I show this". It generates several distinct, on-brand visual concepts for a lesson or a single slide — each with a thesis, a sketch, and a motion idea — so the build starts from a strong art direction instead of the first obvious treatment. It feeds concepts to design-V0.1 (to build) and design-repair (when a fix needs a fresh idea).
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Design Creativity — concepts before the obvious

The fastest route to "AI slop" is building the first idea that comes to mind: ROI becomes a piggy
bank, costs become coins, a comparison becomes two gray columns. This skill widens the option space
*before* the build — several genuinely different ways to show the idea, each still unmistakably Stoic.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`;
anti-AI rules: `design-system/anti-ai-rules.md`; methods + cliché table: `references/concepting-methods.md`.
Locally the repo is usually `~/StoicDesign`; in Claude Design, read it from `github.com/500ft/StoicDesign`.

## When to use

- A slide or lesson moment needs an art direction and the obvious treatment is weak.
- **design-V0.1** flags a generically-conceived slide during a build.
- **design-repair** needs a stronger concept to rebuild a broken/derivative visual.
- The user wants a few directions to choose from before committing.

## What stays fixed vs. what you vary

Brand is a constraint, not a canvas. **Fixed:** palette, type system, voice, the seal/wordmark,
restraint. **Free to explore:** visual metaphor, data encoding, composition/asymmetry, focal element,
ground (navy/parchment), and motion. A "creative" slide that breaks the palette or sets a new font is
not creative — it's off-brand.

## Method

1. **Name the idea** the slide must land, in one sentence (the same "one idea" design-V0.1 uses).
2. **List the obvious treatment** — and set it aside. (Knowing the cliché is how you avoid it; see the
   cliché→stronger table in the reference.)
3. **Generate 3–5 distinct concepts**, each varying a *different* dimension (metaphor, encoding,
   composition, motion). Distinct means structurally different, not recolored.
4. **Pressure each against the brand:** does it stay calm, classical, restrained? Cut any that need
   decoration to work.
5. **Rank** by clarity-per-second (it plays under a voice) then by craft, and recommend one.

## Output format

```
CONCEPTS — <slide / lesson moment>   Idea: <the one idea>
Obvious treatment (avoid): <cliché>

1. ★ "Crossover" — break-even as the moment two lines cross a gold zero-line; everything before is
   cost, everything after is gain. Encoding: cumulative line. Motion: lines stroke on, dot lands on
   the crossing. On-brand: navy figure, brand data colors. Effort: SVG, low.
2. "Iceberg of cost" — the 4 costs as a weighted stack, the hidden one below a waterline. ...
3. "Ledger" — a classical double-entry ledger; earnings vs. spend tally. ...
Recommend: #1 — fastest to read, strongest annotation moment.
```

## Staying Stoic while being creative

Lean on the brand's classical register — ledgers, seals, columns, engraving/woodcut linework,
typographic figures — but **used with restraint and rendered in the design system**, never as literal
clip-art. One strong motif beats three decorations. When a concept calls for a bespoke image (a
portrait, a scene, a texture), hand it to the imagegen system skill and then **design-repair** to
de-slop and palette-match it.

## Handoff

- Chosen concept → **design-V0.1** to build into the deck.
- Concept needs a generated image → imagegen, then **design-repair**.
- After building, the result still passes through **design-taste** like any slide.

For divergence techniques and the full cliché→stronger table, read `references/concepting-methods.md`.
