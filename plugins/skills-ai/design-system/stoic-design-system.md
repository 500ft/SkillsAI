# Stoic — Design System (canonical)

Single source of truth for the **StoicDesign** suite. Every skill in this repo reads this
file before producing or judging design. Change values **here**; never fork them into an
individual skill. Repo-relative path: `design-system/stoic-design-system.md`.

---

## 0. The brief

Stoic Education is an editorial finance/education channel. Decks **play behind a voiceover**
on YouTube. The job of a slide is to give the eye **one thing to hold** while the narration
carries the argument — not to reproduce the script on screen. Default to restraint: a Stoic
slide looks like a page from a serious book, not a marketing landing page.

Design north star: **classical · rigorous · calm.** If a choice looks "AI-generated,"
"templated," or "hype," it is wrong by definition here — see `anti-ai-rules.md`.

---

## 1. Identity

- **Name:** `STOIC EDUCATION` (titles) / `STOIC EDU` (running footer).
- **Emblem:** the blue wax seal — `design-system/assets/stoic-seal.png` (philosopher profile).
  Use on the **title**, **section dividers**, and **close** slides only — one mark per section,
  never wallpapered on every slide.
- **Wordmark:** the word *Stoic* set in **Fraunces italic**, sentence-case. The all-caps
  `STOIC EDUCATION` is the Inter kicker lockup, not the wordmark.
- **Voice:** plain, exact, unhurried. State numbers honestly, with their caveats. No hype, no
  exclamation marks, no "unlock / supercharge / seamless," no rhetorical questions as filler.

---

## 2. Color

Two grounds (navy + parchment), one accent family (wax blue), a disciplined data set.
**Never** the default Office palette (`#4472C4`, `#ED7D31`, `#70AD47`, `#FFC000`, `#A5A5A5`).

| Token | Hex | Use |
|---|---|---|
| `--navy` | `#15243F` | primary **dark** ground (title, dividers, figures, emphasis) |
| `--navy-panel` | `#1E3257` | raised panel / inset on navy |
| `--parchment` | `#F6F1E7` | primary **light** ground (content slides) |
| `--parchment-panel` | `#ECE4D3` | raised panel / inset on parchment |
| `--ink` | `#19233A` | primary text on parchment |
| `--ink-muted` | `#5C6577` | secondary text / captions on parchment |
| `--cream` | `#F3EDE1` | primary text on navy |
| `--cream-muted` | `#AAB1C2` | secondary text on navy |
| `--wax` | `#2C49A6` | brand accent · primary action · hero data series |
| `--wax-bright` | `#3D5FCB` | hover / active / emphasis highlight |
| `--data-pos` | `#2F7D5B` | gain · breaks-even · positive outcome |
| `--data-neg` | `#B0492F` | loss · never-breaks-even · negative outcome |
| `--data-neutral` | `#7C8597` | baseline · "the friend who stayed" · context series |
| `--data-gold` | `#BE933A` | **reference / break-even line**, single highlight (replaces `#FFC000`) |
| `--rule-ink` | `rgba(25,35,58,0.14)` | hairlines on parchment |
| `--rule-cream` | `rgba(243,237,225,0.16)` | hairlines on navy |

**Rules.** One accent (`--wax`) per slide for emphasis. Data-viz uses **≤3 series colors**;
gold is reserved for the reference/break-even line. WCAG AA contrast is a floor (ink on
parchment and cream on navy both pass).

---

## 3. Typography

| Role | Family | Token |
|---|---|---|
| Display / headings / pull-quotes | **Fraunces** (serif) | `--font-display` |
| Kickers, labels, body, UI | **Inter** (grotesque) | `--font-ui` |
| Numbers, money, years, code | **JetBrains Mono** (tabular) | `--font-mono` |

```
--font-display: 'Fraunces', 'Iowan Old Style', Georgia, serif;
--font-ui:      'Inter', system-ui, -apple-system, sans-serif;
--font-mono:    'JetBrains Mono', 'SF Mono', ui-monospace, monospace;
```

- **Headings** — Fraunces 500–600, tracking `-0.02em` at display sizes. `opsz` high; soft/wonky off.
- **Kickers / footer** — Inter 600, **UPPERCASE**, tracking `+0.16em` (e.g. `THE HOOK`, `CASE FILE A`, `FIGURE 1 ·`).
- **Body / lead** — Inter 400, line-height 1.4; lead 1.3.
- **Numbers** — JetBrains Mono 500, `font-variant-numeric: tabular-nums`. Always pair currencies
  as the channel does (`₮1.16B / $340K`). Never set money in a proportional font.

**Type scale (px @ 1920×1080):**
`--t-kicker:15` · `--t-body:22` · `--t-lead:28` · `--t-h3:36` · `--t-h2:56` · `--t-h1:84` ·
`--t-display:120` · `--t-data:64`.

The single biggest "AI tell" in the source deck was **Calibri body text**. Calibri / Arial /
Times defaults are banned outputs.

---

## 4. Spacing, grid & layout spine

- **Base unit 8px.** Steps: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128`.
- **Title-safe margins** (YouTube): `--margin-x:96px`, `--margin-y:72px` (~5%). Nothing critical
  outside this box.
- **Grid:** 12 columns, 24px gutter, max content width 1728px, centered.
- **Radius:** square by default (editorial). `2px` on chips; `999px` only for the seal/pills.
- **Depth:** hairline rules (`1px` at low alpha) + whitespace **instead of** drop shadows. One
  soft shadow allowed for the seal (it is a physical object).

**The spine (every content slide):**
- Running footer with a hairline above it: left `STOIC EDU · <LESSON TITLE>`, right `NN / 19`.
- Section **kicker** top-left (`THE HOOK`, `CASE FILE B`, `FIGURE 2 ·`) in `--wax` or `--data-gold`.
- One headline, one idea. On-screen prose **≤ ~20 words** (labels/callouts/data exempt).
  Deliberate dense-reference slides (e.g. the calculator) are the documented exception.

---

## 5. Motion (narrate-over)

Calm, slow, purposeful — it plays under a voice, so it must never grab attention from the words.

- **Slide transition — directional push (the cinematic default):** slides translate **horizontally**.
  The next slide enters from the **right**; the leaving slide exits **left** (reverse when going back).
  900ms on `--ease-cine` (`cubic-bezier(.76,0,.24,1)`, easeInOutQuart) — one smooth, weighted glide.
  Animate **only `transform: translate3d(...)`** (GPU, `will-change:transform`) so it never janks when
  recorded. This replaces the old fade/scale, which "appeared from nowhere"; motion must have a direction.
  No wipes, spins, cube/flip, or random fades.
- **Element reveals (staged, one direction):** each element fades + **rises** 24px over 640ms on
  `--ease-out` (`cubic-bezier(.22,1,.36,1)`), staggered ~110ms, auto-playing on slide-enter — **one reveal
  per narration beat**. Every element enters from the *same* direction (rise, or `from-left`); never from
  random places. A row of items reveals left-to-right.
- **Number count-up:** money/years count from a baseline over ~1000ms (mono, tabular).
- **Chart draw-on (the one sanctioned exception):** SVG strokes draw in over **900–1200ms** using
  `--ease-expo` (`cubic-bezier(.16,1,.3,1)`, easeOutExpo). This is *slower and heavier* than slide/element
  motion on purpose — a chart drawing itself is the focal moment, not a background transition. Lines
  stroke left-to-right; radial/donut charts draw clockwise from 12 o'clock; the reference line fades
  first. Everything **else** stays on the calm `--ease` timing above. See the **cinematic-chart-animations**
  and **slide-animations-engine** skills.
- **Reduced motion:** honor `prefers-reduced-motion` → collapse to plain fades, no movement.
- **Record mode (it must read as a movie):** the engine autoplays with `?play=1` — reveals cascade, the
  slide holds for its `data-dwell`, then auto-advances with the push. Screen-record that at ≥1080p/60fps.
  Manual (←/→/click) for authoring; `F` fullscreen.
- **No empty voids:** layouts **fill** the frame — a header row plus content that stretches to the footer,
  or a 3-band bleed (kicker top / hero centered / support bottom). Short content is balanced by stretching
  or a full-height divider, **never** left floating in a centered band. (Enforced by the deck template's
  `.fill` / `.bleed` primitives; see **layout-density-optimizer**.)
- **Pacing:** 6–12s of screen time per slide; one idea per slide. Tokens:
  `--ease-cine` (slide push), `--ease-out` (reveals), `--ease-expo` (chart draw), `--t-slide:900ms`,
  `--t-rev:640ms`, `--stagger:110ms`, `--t-count:1000ms`, `--t-draw:1100ms`.

---

## 6. Charts & data-viz

Charts are where the source deck looked most "template." Rules:

1. **Build as inline SVG**, brand-styled and animatable — **never** paste a default-Office chart PNG.
2. **Always framed:** a baseline axis, minimal ticks, and a clear domain. No graph floating on white.
3. **Direct-label series at their ends** (`Mech eng → Detroit`, `+$40K`) — no detached legends.
4. **Brand palette only:** hero series `--wax`; outcomes `--data-pos` / `--data-neg`; context
   `--data-neutral`; the break-even/reference line is `--data-gold`, dashed.
5. **Annotate meaning, not just data:** mark the break-even dot + `Year 6`, arrow the `+$1.1M`.
6. **Caption convention:** `FIGURE n · <title>` kicker, and a mono source line
   (`Source: NACE 2024 · Glassdoor UB`).

---

## 7. Grounds & slide types

Alternate grounds to create rhythm — the fix for "same background on all 19 slides."

- **Title / Close** — `--navy` ground + seal + Fraunces display + Inter kicker lockup.
- **Section divider** — `--navy`, oversized Fraunces number + section name; brief.
- **Content** — `--parchment` ground, editorial grid, one idea.
- **Figure** — may invert to `--navy` to make a chart the hero.
- **Case file** — parchment, a "dossier" header band (`CASE FILE A` + verdict chip
  `STRONG ROI` / `TRADE-OFF` / `NET-NEGATIVE`) over a two-column math/verdict layout.
- **Calculator / reference** — the sanctioned dense slide; tabular mono, numbered steps.
- **Recap** — parchment, 2–3 numbered takeaways, generous space.

---

## 8. Ready-to-use CSS tokens

Copy into the deck's `:root` (or hand to Claude Design verbatim):

```css
:root{
  --navy:#15243F; --navy-panel:#1E3257; --parchment:#F6F1E7; --parchment-panel:#ECE4D3;
  --ink:#19233A; --ink-muted:#5C6577; --cream:#F3EDE1; --cream-muted:#AAB1C2;
  --wax:#2C49A6; --wax-bright:#3D5FCB;
  --data-pos:#2F7D5B; --data-neg:#B0492F; --data-neutral:#7C8597; --data-gold:#BE933A;
  --rule-ink:rgba(25,35,58,.14); --rule-cream:rgba(243,237,225,.16);
  --font-display:'Fraunces','Iowan Old Style',Georgia,serif;
  --font-ui:'Inter',system-ui,-apple-system,sans-serif;
  --font-mono:'JetBrains Mono','SF Mono',ui-monospace,monospace;
  --t-kicker:15px; --t-body:22px; --t-lead:28px; --t-h3:36px; --t-h2:56px;
  --t-h1:84px; --t-display:120px; --t-data:64px;
  --margin-x:96px; --margin-y:72px;
  --ease:cubic-bezier(.22,.61,.36,1); --ease-expo:cubic-bezier(.16,1,.3,1);
  --t-slide:700ms; --t-reveal:520ms; --stagger:140ms; --t-count:1000ms; --t-draw:1100ms;
}
```

Fonts (Google): `Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600` · `Inter:wght@400;500;600` ·
`JetBrains+Mono:wght@400;500`.

---

## 9. Hard anti-AI rules (summary)

The full, example-grounded list lives in `design-system/anti-ai-rules.md` and is enforced by the
**design-taste** skill. In short: no Calibri/Arial/default fonts; no default Office data palette;
no one background reused on every slide; no floating unframed charts; no wall-of-text behind a
voiceover; no emoji-icons, purple-gradient slop, 3D blobs, or lorem ipsum; use the grid and real
type hierarchy instead of centering everything; numbers always tabular mono.
