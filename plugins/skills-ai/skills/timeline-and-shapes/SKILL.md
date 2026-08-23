---
name: timeline-and-shapes
description: This skill should be used when the user asks to build a "timeline", "process map", "roadmap", "milestones", "phases", or "step diagram", or needs precise alignment for connected nodes and shapes. It gives exact geometry for horizontal timelines and process diagrams — connector lines, node sizing, alternating labels — styled in the Stoic design system so nothing overlaps or looks unaligned.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Timeline & Shapes — precise process geometry

Timelines and process maps look amateur the moment nodes misalign or labels collide. This skill uses
fixed geometry rules so they come out clean, in the brand.

**Reads from the StoicDesign repo.** Canonical system: `design-system/stoic-design-system.md` (tokens,
grid, hairlines); routing: `design-system/skill-interactions.md`. Locally `~/StoicDesign`; in Claude
Design, `github.com/500ft/StoicDesign`.

> **This vs. `timeline-pin-mapper`:** use **this** skill for *evenly spaced* conceptual steps/phases with
> no real time scale. For *chronological* timelines where the year gaps are unequal and meaningful (history,
> evolution), use **timeline-pin-mapper** (date→% positioning). Both share the node/dot styling below so the
> two timeline types look like one family.

## Horizontal timeline geometry

- Flexbox container, `justify-content:space-between`, nodes evenly spaced.
- The connector is an **absolute-positioned `::before`**, `height:2px`, centered vertically *behind* the
  node dots, colored `--rule-ink` (or `--data-neutral` for an active track).

## Node engineering

- **Current milestone:** `24px` circle, `--wax` fill, a soft outer ring (`box-shadow:0 0 0 6px rgba(44,73,166,.15)`).
- **Completed:** `16px` circle, fill = connector color (`--data-neutral`/`--wax`), interior checkmark in `--cream`.
- **Future:** `12px` circle, hollow — `2px solid --rule-ink`, `--parchment` interior.

## Content alignment (prevents overlap)

- **Alternate** label placement: odd nodes place title+text **above** the line, even nodes **below** —
  maximizes whitespace and stops blocks colliding.
- Each label block has a **fixed `max-width`** (e.g. `180px`) so text wraps predictably.
- Title in Fraunces (`--t-h3` down), supporting line in Inter `--ink-muted`, any date in JetBrains Mono.

## CSS recipe

```css
.timeline{ position:relative; display:flex; justify-content:space-between; align-items:center; padding:48px 0; }
.timeline::before{ content:''; position:absolute; left:0; right:0; top:50%; height:2px;
  background:var(--rule-ink); transform:translateY(-1px); z-index:0; }
.node{ position:relative; z-index:1; width:24px; height:24px; border-radius:999px; background:var(--wax); }
.node.done{ width:16px; height:16px; background:var(--data-neutral); }
.node.future{ width:12px; height:12px; background:var(--parchment); border:2px solid var(--rule-ink); }
.node .label{ position:absolute; left:50%; transform:translateX(-50%); max-width:180px; }
.node:nth-child(odd) .label{ bottom:36px; }   /* above */
.node:nth-child(even) .label{ top:36px; }      /* below */
```

## Process maps / other shapes

- Snap all nodes/boxes to the grid; equalize stroke widths; brand corner radii (square default, `2px`
  chips, `999px` dots). Hairlines, not heavy shadows.
- For freeform mechanism/flow diagrams, use the **excalidraw-diagram-generator** skill; for broken or
  misaligned shapes, route to **design-repair**. Final pass through **design-taste**.
