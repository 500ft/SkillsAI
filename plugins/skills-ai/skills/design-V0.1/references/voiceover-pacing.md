# Voiceover Pacing

The deck plays **under a voice**. Every pacing decision serves the narration, not the reader.

## Word budget

- **One idea per slide.** If you can't name the single idea in a sentence, split the slide.
- **On-screen prose ≤ ~20 words** (data, labels, axis text, numbers are exempt).
- **Headline ≤ 8 words.** Kicker is a label, not a sentence.
- The script lives in the voiceover; the slide shows the *evidence* (number, chart, contrast) the
  voice is pointing at.

## Beats and reveals

- Map **one reveal step to one narration beat.** As the voice introduces the third cost, the third
  row reveals — not before.
- Derive reveal steps directly from the script: mark each sentence/beat, attach the on-screen element
  it justifies, order them. That ordered list *is* the slide's `data-reveal` sequence.
- Aim for **6–12 seconds of screen time per slide**; 2–5 reveal steps is typical. A slide with zero
  reveals is fine for a quiet aside; a slide needing 8 reveals is two slides.

## Timing (from the design system)

- Slide transition 700ms dissolve + 2% settle; reveals fade+rise 520ms, stagger 140ms; count-ups
  ~1000ms; chart lines stroke on ~900ms. Honor `prefers-reduced-motion`.
- Numbers that matter **count up** (mono, tabular) so the eye lands as the voice says the figure.

## Slide-count math

`slides ≈ lesson_minutes × 60 ÷ avg_slide_seconds`. At ~9s/slide, a 3-minute lesson ≈ 20 slides —
which matches the source deck's 19. Don't pad: a slide with nothing new to show is a slide that
competes with the voice.

## Two ways to run it under a voiceover

1. **Manual sync (default).** Record the VO, then advance reveals/slides by arrow key while screen-
   recording the deck (1080p or 4K, 60fps), or step in a video editor. Best sync, most control.
2. **Auto-advance.** Set `data-duration` per slide (ms) and toggle auto mode (`A`) for a hands-off
   continuous render. Use when the VO is tightly timed to the planned durations.

## Citations & sources

- Keep sources off the content slides. Put a mono source line under any figure
  (`Source: NACE 2024 · Glassdoor UB`) and a consolidated sources line on the **Close** slide.
- Round numbers honestly and keep significant figures consistent within a slide; pair currencies
  (`₮ / $`) the same way every time.

## Export checklist

- [ ] Reveals match the VO beat list.
- [ ] 1 idea / slide; ≤20 on-screen words (except the sanctioned calculator slide).
- [ ] Recorded at ≥1080p, 60fps; reduced-motion not triggering during capture.
- [ ] Print/PDF fallback renders one slide per page (for thumbnails / static reuse).
