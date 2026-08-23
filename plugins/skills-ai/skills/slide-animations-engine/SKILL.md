---
name: slide-animations-engine
description: This skill should be used when the user asks about "slide animations", "transitions", "GSAP", "cinematic transitions", "staggered reveals", or wants smooth element/slide motion in an HTML presentation. It configures high-performance CSS/GSAP animation aligned to the Stoic motion system — animating only transform/opacity, calm timing, staged reveals on the narration beat.
---

**SkillsAI portability:** Resolve shared `design-system/...` files from `../../design-system/...` relative to this file when installed as a plugin. In a ChatGPT ZIP they are bundled under this skill’s own `design-system/` directory. Use `~/StoicDesign/design-system/` only as a fallback.


# Slide Animations Engine — calm, performant motion

Motion in a narrate-over deck must support the voice, never compete with it. This skill applies the
brand's motion rules and gives the implementation patterns (CSS first, GSAP when sequencing earns it).

**Reads from the StoicDesign repo.** Canonical timing lives in `design-system/stoic-design-system.md`
(§5 Motion) and the reference implementation is the reveal engine in
`design-V0.1/assets/deck-template.html`. Locally `~/StoicDesign`; in Claude Design,
`github.com/500ft/StoicDesign`.

## Core principles

- **Animate only `transform` and `opacity`** — never `width`/`height`/`top`/`left` (they thrash layout).
  Use `translate3d` + `will-change:transform` so a recording never janks.
- **Motion has a direction.** Slides **push horizontally** (next in from the right, prev out to the left);
  elements enter from **one** consistent direction (rise, or `from-left`), never from random places.
- **Brand timing (canonical):** slide push `900ms` on `--ease-cine` (`cubic-bezier(.76,0,.24,1)`,
  easeInOutQuart); element reveal `640ms` on `--ease-out` (`cubic-bezier(.22,1,.36,1)`); stagger `~110ms`;
  count-up `~1000ms`. (A tighter profile — ~`0.3–0.4s` — is fine for fast social/carousel content.)
- **One reveal per narration beat;** never animate everything at once. Reveals auto-play on slide-enter.
- Honor `prefers-reduced-motion` → collapse to instant/opacity-only.

## Patterns

**Slide-to-slide — directional push (the default; see the deck template engine):**
```css
.slide{ position:absolute; inset:0; transform:translate3d(100%,0,0); will-change:transform;
  transition:transform var(--t-slide,900ms) var(--ease-cine); }
.slide.is-active{ transform:translate3d(0,0,0); }   /* on screen        */
.slide.is-prev  { transform:translate3d(-100%,0,0);} /* exited left      */
.slide.is-next  { transform:translate3d(100%,0,0); } /* waiting right    */
```

**Staggered content reveal (CSS), one direction:**
```css
[data-reveal]{ opacity:0; transform:translateY(24px);
  transition:opacity var(--t-rev,640ms) var(--ease-out), transform var(--t-rev,640ms) var(--ease-out); }
[data-reveal].from-left{ transform:translateX(-32px); }   /* alt single direction */
[data-reveal].shown{ opacity:1; transform:none; }
/* JS adds .shown staggered on slide-enter: setTimeout(.., 280 + i*110) */
```

Avoid wipes/spins/flip/cube and any "appear from nowhere" fade. The deck template
(`design-V0.1/assets/deck-template.html`) is the reference implementation, incl. record mode (`?play=1`).

**GSAP (for sequenced reveals / charts):**
```js
gsap.to('.fade-in-up', { opacity:1, y:0, duration:0.52, stagger:0.14, ease:'power2.out' });
```
Use a timeline to choreograph a chart draw-on + annotation landing on the beat. Keep durations within
the brand range; respect reduced-motion by gating the timeline.

## Rules

- Subtle parallax on background shapes is fine (small `transform` on scroll/step); never on text the
  viewer must read mid-motion.
- Don't introduce easing/timing that contradicts `design-system/§5` without recording it as a deliberate
  exception. Motion consistency is part of the brand.
- **Charts are the exception, and they're not yours:** donut/radial/line *draw-on* uses the heavier
  `--ease-expo` / `--t-draw` and belongs to **cinematic-chart-animations**. This skill owns slide
  transitions + element reveals (calm `--ease`). They share one timeline but disjoint elements — see
  `design-system/skill-interactions.md`.
