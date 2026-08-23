---
name: design-shotgun
description: >-
  Generate 3-5 deliberately distinct design variants of a UI concept — each with its own design thesis
  (layout, typography, color treatment) — and open them side-by-side in the browser for the user to compare
  and pick from before any production build. Use this skill when the user wants design options rather than
  one answer: "give me a few versions", "show me some directions", "not sure what style I want",
  "design shotgun", early-stage landing pages or dashboards where taste isn't settled yet, or /design-shotgun.
  If the user already knows exactly what they want, skip this and build it directly (frontend-slides /
  frontend-design).
---

# Design Shotgun — Variants Before Commitment

When taste isn't settled, one polished design is a coin flip — the user can't say what they want until they see what they don't. Shotgun the decision: several genuinely different directions, viewed side-by-side, picked from in minutes. The cost of 4 variants is far below the cost of building the wrong one well.

## Rules that make the comparison honest

- **Same content, different design.** Every variant carries identical real copy, data, and sections (draft real content from the concept — never lorem ipsum). If content varies, the user picks the better *words*, not the better design.
- **Each variant gets a named thesis** — one word plus a sentence, e.g. *Editorial* (magazine grid, serif display, generous whitespace), *Brutalist* (raw borders, mono, flat color), *Soft* (rounded, muted palette, airy), *Dense* (data-forward, tight spacing, dashboard energy), *Bold* (oversize type, high contrast). Theses must differ **structurally** — layout, typography, density — not just hue. Four variants that are the same card layout in four accent colors is a failed shotgun.
- **3-5 variants.** Fewer isn't a spread; more dilutes the craft of each and overwhelms the choice.
- If brand guidelines exist (`docs/brand-guidelines.md` or the frontend-slides skill's `references/brand-guidelines.md`), treat the *fixed* decisions (logo, mandated palette) as constraints and shotgun the *unfixed* axes. No guidelines — full freedom.

## Build

Create a working dir (`design-shotgun/<slug>/` in the project, or `/tmp` if outside one):

- `variant-1.html` … `variant-N.html` — each fully self-contained (inline CSS, system/Google fonts, responsive, accessible floor: contrast, focus states, semantic markup). Each one production-quality *for its thesis* — a sloppy variant poisons the comparison.
- `index.html` — the compare page: a grid of labeled cards, one per variant, each showing the live page in a scaled iframe with the thesis name + one-line description, an "open full" link, and a keyboard shortcut (1-N) to open it. Keep this chrome minimal and neutral so it doesn't bias the vote.

Open it for the user: `open index.html` on macOS (`xdg-open` on Linux); if the harness can't open a browser, give the exact file path and say what they'll see.

## Decide and record

Take the verdict — usually "variant 3, but with variant 1's header" — and treat blends as normal: merge the named pieces into a final direction. Then:

1. **Record the winning direction** into the brand guidelines file (create `docs/brand-guidelines.md` from the choice if none exists): palette, type, spacing, the thesis adjectives. This is the lasting payoff — next time, generation starts from settled taste instead of another shotgun.
2. Delete or archive the losing variants (user's call), and hand off to the production build (`frontend-slides` or the project's real stack) using the recorded direction.
