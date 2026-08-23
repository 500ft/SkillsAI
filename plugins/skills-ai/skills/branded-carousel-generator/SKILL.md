---
name: branded-carousel-generator
description: This skill should be used when the user asks to "make a carousel", "turn this post/report into a carousel", "Instagram/LinkedIn carousel", "swipeable social slides", or wants to compress long-form content into brand-consistent social cards. It produces a tight, high-engagement carousel in the Stoic design system (hook → value cards → CTA), one idea per card.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Branded Carousel Generator — long-form → swipeable cards

Compress a blog post, report, or lesson into a short swipeable carousel that holds the brand and earns
the swipe. The discipline is ruthless reduction: one idea per card, a hook that stops the scroll, a
close that asks for the next action.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`.
Locally `~/StoicDesign`; in Claude Design, `github.com/500ft/StoicDesign`.

## Format

- **Aspect:** square `1080×1080` (IG/LinkedIn) or portrait `1080×1350` (more screen, better reach). Pick
  one and keep every card identical.
- **Length:** 6–10 cards. Structure: **01 Hook** → **02 stakes/why** → **03–N value** (one point each)
  → **last CTA**.
- **Spine:** small `STOIC EDU` wordmark + card index (`03 / 08`) bottom corner; seal on the hook + CTA
  cards only.
- **Type:** Fraunces headline (large — readable as a thumbnail), Inter support, JetBrains Mono numbers.
  ≤ ~15 words per card; the headline does the work.
- **Ground:** alternate navy / parchment to create swipe rhythm; the hook and CTA on navy.

## Card patterns

- **Hook** — one provocative line or number, max type, seal. No sub-points.
- **Value** — one assertion headline + one supporting line or a single stat/mini-chart (brand colors).
- **CTA** — the takeaway + a clear action ("Run your own number — full lesson in bio"), seal.

## Build

Draft real copy from the source (never lorem ipsum). Output as a self-contained HTML deck (reuse the
`design-V0.1/assets/deck-template.html` engine, set to the square/portrait aspect) or as per-card specs
for Claude Design. Generated images get de-slopped via **design-repair**; charts via
**data-viz-and-graphs**. Final pass through **design-taste**.

## Rules

- One idea per card — if a card needs a second point, it's a second card.
- Identical safe-margins and spine on every card; consistency *is* the brand at carousel scale.
- The hook promises and the CTA pays off; the middle delivers exactly what the hook promised.
