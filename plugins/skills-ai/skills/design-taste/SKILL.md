---
name: design-taste
description: This skill should be used when the user asks to "design taste check", "make this look less AI", "why does this look generic/cheap/templated", "is this on-brand", "review this slide/deck/graphic", "critique this design", "does this look AI-generated", or before finalizing any Stoic Education deck. It scores a design against the Stoic design system and the anti-AI rules, then returns prioritized, specific, actionable fixes. It is also invoked automatically by design-V0.1 before any deck is shipped.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Design Taste — the anti-AI-slop gate

Taste is not a vibe here; it is a checklist applied with judgment. "AI slop" is the accumulation
of defaults left unchanged — a default font, a default palette, a default centered layout. This
skill finds those un-made decisions and turns each into a specific fix.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`;
anti-AI rules: `design-system/anti-ai-rules.md`; scoring rubric: `references/taste-rubric.md`.
Locally the repo is usually at `~/StoicDesign`; in Claude Design, read it from
`github.com/500ft/StoicDesign`.

## When to run

- Before **design-V0.1** outputs any deck (mandatory gate).
- On demand: a user drops a slide, deck, PNG, or screenshot and asks if it looks AI / on-brand / cheap.
- After **design-repair** or **design-legibility** edits, to confirm the fix didn't introduce new tells.

## Procedure

1. **Load the standard.** Read the design system and `anti-ai-rules.md` so the judgment is measured
   against Stoic's actual decisions, not generic design opinion.
2. **Ingest the artifact.** Accept an HTML deck, an image/screenshot, a PDF, or a slide spec. For
   images, look — do not assume. For HTML, inspect the actual CSS (fonts, colors, layout), not just
   the rendered guess.
3. **Score with the rubric** (`references/taste-rubric.md`): eight dimensions, 0–5 each. Record the
   evidence for each score (the specific font name, hex, word count, etc.) — a score with no cited
   evidence is not allowed.
4. **Apply the hard gate.** Any single dimension scoring **≤2** means "ships looking AI — fix before
   release," regardless of the total. The nine checklist items in `anti-ai-rules.md` are pass/fail.
5. **Return prioritized fixes.** Order by impact. Each fix names the **offending element**, the
   **rule broken**, and the **exact change** (font → Fraunces 600; `#4472C4` → `--wax`; cut 60 words
   to 14). Vague advice ("add more contrast") is a failure of this skill.

## Output format

```
TASTE REPORT — <artifact>
Verdict: <SHIP / FIX FIRST / REWORK>   Score: NN/40

Scores:  Type 4 · Color 2 · Layout 3 · Restraint 1 · Data-viz 3 · Motion 4 · Brand 4 · Craft 3
Hard gate: FAIL (Restraint 1, Color 2)

Fixes (priority order):
1. [Restraint] Slide 4 has 78 on-screen words behind the VO → cut to ≤20; move the cost
   breakdown to 4 staged reveals, one per narration beat.
2. [Color] Chart series use #4472C4/#70AD47 (Office) → re-map to --wax / --data-pos / --data-gold.
3. ...
```

## Judgment notes (what separates taste from a linter)

- **The voiceover is the content.** The most common Stoic failure is a slide that *competes* with the
  narration instead of supporting it. When unsure, cut text and add whitespace.
- **One palette, one accent.** If you can point to two color worlds on a slide, that is the tell —
  collapse to the brand set before anything else.
- **Type carries the brand.** Fraunces + Inter + JetBrains Mono is most of the "expensive" feeling.
  A correct palette in Calibri still looks generated.
- **Restraint reads as confidence.** Decoration reads as insecurity. Prefer removing over adding.
- **Be specific or be silent.** If a fix can't be stated as a concrete change to a named element,
  it isn't ready to report.

## Handing off

- If fixes are layout/text-occlusion problems (a label hidden behind a shape, a number under the
  footer), route them to **design-legibility**.
- If fixes are broken visuals (warped AI image, malformed chart/shape), route them to **design-repair**.
- If a slide is generically conceived (right rules, boring idea), route to **design-creativity** for a
  stronger art-direction, then re-score.

For the full dimension-by-dimension anchors and weighting, read `references/taste-rubric.md`.
