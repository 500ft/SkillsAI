---
name: frontend-slides
description: Convert rough UI concepts into exact, production-grade HTML/CSS that follows saved brand guidelines — palette, typography, spacing, layout preferences — instead of generic AI styling, and remember stated preferences for next time. Also builds keyboard-navigable single-file HTML slide decks. Use this skill whenever the user asks for a web page, landing page, UI mockup, component, dashboard shell, or an HTML pitch/slide deck, or invokes /frontend-slides — even if they only give a rough one-line concept like "make me a landing page for X".
---

# Frontend Slides — Brand-Driven UI Generation

Turn a rough concept into exact UI output that looks like *this user's* product, not like every AI-generated page. The mechanism is simple: brand decisions live in a guidelines file that is read before generating and updated whenever the user states a lasting preference — so taste accumulates across sessions instead of being re-litigated every time.

## Step 0 — Load the brand guidelines

Resolution order:

1. `docs/brand-guidelines.md` in the current project (project-specific brand wins)
2. `references/brand-guidelines.md` inside this skill (the user's personal defaults)

If only template placeholder values exist, ask the user the three highest-impact questions — palette mood (dark/light, accent color), typography personality (geometric/humanist/technical), and density (airy marketing vs. dense dashboard) — then **write their answers into the guidelines file** before proceeding. If the user is absent, proceed with the template defaults and say so in the handoff.

**Preference persistence is a standing rule:** any time the user states a durable preference during iteration ("always Inter", "never gradients", "rounder corners everywhere"), update the guidelines file in the same turn. One-off requests ("make this one red") don't get persisted.

## Step 1 — Pin down the concept (lightly)

This is not a requirements interrogation (that's `/grill-me`). Settle just enough to build: purpose and audience, the key content/sections, and the output mode —

- **Page** — landing page, dashboard shell, full view
- **Component** — a card, nav, form, table to drop into an existing app
- **Deck** — slide-based presentation in HTML

Where the user gave only a one-liner, draft real content from it (real headlines, plausible copy, realistic data) — lorem ipsum and `[Your text here]` make every design look fake and push the judgment work back onto the user.

## Step 2 — Build

- **Tokens first.** Translate the guidelines into CSS custom properties on `:root` (`--bg`, `--surface`, `--text`, `--accent`, `--font-display`, `--font-body`, `--space-1..n`, `--radius`, `--shadow`) and style exclusively through them. This is what makes output exact and revisions cheap.
- **Self-contained single file** (HTML + embedded CSS + minimal JS, system/Google fonts) unless the project has a framework — then match the project's stack and component conventions instead.
- **Semantic + accessible as a floor**: real landmarks and heading order, WCAG AA contrast, visible `:focus-visible` states, `prefers-reduced-motion` respected, alt text on images.
- **Responsive**: design mobile and desktop deliberately, not as an afterthought.

Quality bar — the anti-generic rules:

- No default AI look: no purple-gradient-on-white, no emoji-as-icons, no three-equal-cards-with-rounded-shadows reflex. Commit to the brand personality in the guidelines, including its `Hard avoids`.
- Typography does the heavy lifting: real scale contrast between display and body, deliberate weights and letter-spacing — most "AI-looking" pages are one font at three nearby sizes.
- One accent used for action and emphasis; restraint elsewhere. Spacing from the scale, never ad-hoc pixel values.

## Deck mode

Each slide is a full-viewport `<section>`; navigation by arrow keys, click, and on-screen prev/next; slide counter / progress indicator; URL hash per slide so refresh keeps your place; print stylesheet that renders one slide per page (instant PDF export). Keep the JS tiny, inline, dependency-free. Same tokens, same brand — a deck is the brand at presentation scale, with bigger type (titles readable from the back of a room) and one idea per slide.

## Step 3 — Iterate

Present the output (render/screenshot it if the harness can, otherwise tell the user the file path to open). Take feedback as numbered changes, apply, repeat. Route durable preferences to the guidelines file as they appear. When the user is satisfied, note in one line where the file lives and which guidelines file governed it — so the next session starts from the same taste.
