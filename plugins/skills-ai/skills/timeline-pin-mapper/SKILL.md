---
name: timeline-pin-mapper
description: This skill should be used when the user asks for a "timeline" with real dates/years, a "history timeline", "evolution chart", "roadmap with dates", or wants milestone pins placed by *when they happened* rather than evenly. It calculates exact percentage-based horizontal coordinates (date → X%) so uneven time gaps render proportionally, with a clamping rule that keeps crowded pins scannable. Distinct from timeline-and-shapes (evenly spaced steps).
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Timeline Pin Mapper — dates become proportional positions

A real chronological timeline must place 2011 and 2012 nearly touching at the left and leave a wide,
honest gap across to 2020 — not space every pin evenly like Flexbox `space-between` would. This skill
maps each date to an absolute `left:%` on a percentage track so the spacing *means* something.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md`; routing:
`design-system/skill-interactions.md`; formula + blueprint + clamping: `references/pin-math.md`. Locally
`~/StoicDesign`; in Claude Design, `github.com/500ft/StoicDesign`.

## When this vs. `timeline-and-shapes`

- **This skill** — dates/years with **unequal, meaningful gaps** (history, evolution, funding rounds).
- **timeline-and-shapes** — **evenly spaced** conceptual steps/phases with no real time scale.
See the referee note in `skill-interactions.md`. Both share the same node/dot styling so the two
timeline types look like one family.

## The proportional formula

1. **Start Year = 0%**, **End Year = 100%**. `Total Span = End − Start`.
2. Each milestone: `pct = ((year − Start) / Total Span) × 100`.
3. **Clamp for scannability:** if two pins land < 8% apart, enforce a **minimum 10% visual buffer** and
   shift the later pin forward (cascade through the cluster), keeping chronological order. The track may
   over-run 100% internally; rescale so the last pin sits at 100%. Full algorithm in `references/pin-math.md`.

## Brand styling (tokens, not the paste's raw hexes)

- **Track line:** 2px solid `--data-gold` (`#BE933A`) — the paste's `#D9A74A` maps here.
- **Pins:** historical entries `--navy`/`--ink` dots; the **final / active** pin highlighted in
  `--data-gold` (larger, with a soft ring) per the timeline-and-shapes node spec.
- **Content card:** date in JetBrains Mono `--ink-muted`; title Fraunces `--ink`; description Inter
  `--ink-muted`; strict `max-width:180px`.
- **Below-line alerts** (a global warning like the reference's orange note): a full-width block cleared
  **below the lowest pin card**, in `--data-neg` for warnings — never overlapping a pin.

## Compose with siblings

- After positioning, run **label-collision-preventer** on any crowded cluster (it owns label overlap).
- Balance the content cards with **layout-density-optimizer** (it owns inner spacing).
- Reveal with **slide-animations-engine** (pins fade-in-up left-to-right along the track).
- Then **design-legibility** (net) and **design-taste** (gate).

For the worked example (2010–2026, pins at 2011/2012/2020/2026, 2026 gold), the clamp algorithm, and the
full HTML/CSS blueprint, read `references/pin-math.md`.
