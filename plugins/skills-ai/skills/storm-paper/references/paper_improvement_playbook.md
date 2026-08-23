# Paper-improvement playbook (Enclosure-Research reference example)

Revised after repo-validated critique (2026-07-08). Principle: **fix attackable claims
before adding breadth.** §2 is already the paper's strongest section (19 sources, full
coverage per `analysis/check_literature_coverage.py`) — broad lit-review expansion is
explicitly deprioritized.

## Ordered sequence

1. **PI decision items (run in parallel, gate publishing not fixing):** publish from
   `main` or `DifferentApplication`; keep or cut the defense/installation content
   (§4.7, §5.4 — already removed on `origin/main`); target venue (Sensors / HardwareX /
   AMT). Venue is a parallel decision, **not** a blocker: citation verification and
   thermal bracketing improve the paper regardless of venue.
2. **Verify the existing 19 citations.** Remove every "confirm later" note (e.g. the
   Botero-Valencia flag at `paper/manuscript_v1.md` §2.3). Confirm each source actually
   supports the sentence citing it. One mischaracterized source costs more than ten new
   ones buy.
3. **Bracket the thermal model with published measured values.** `analysis/
   thermal_bias_results.md` claims its magnitudes match "documented bands" with no
   citations — the most attackable sentence in the modeling work. Retrieve *measured*
   shield/enclosure error ranges (Tarara & Hoheisel; Holden; Theisen RMSE-vs-wind;
   WMO intercomparisons) and rewrite as "prediction consistent with measured X–Y °C
   [refs]". **This is the sanctioned exception to the thermal-numbers lock:** comparing
   a labeled prediction to published measurement is allowed; changing the prediction or
   upgrading simulation → measurement is not.
4. **Add standards/protocol support to §4 Methods:** EPA air-sensor performance
   protocols + collocation guidance (Air Sensor Toolbox / Duvall et al.), WMO CIMO
   Guide (No. 8) exposure/shield practice, relevant ASTM sensor standards,
   reference-instrument uncertainty budget, and a defensible calibration validation
   split (justify the 14/30-day duration from precedent).
5. **§2: narrow standards/protocol additions only.** No broad "more papers" search.
6. **Then** reviewer-skeptic passes on §6 Discussion and §7 Design Criteria (benchmark
   the weighted-criteria table against published evaluation frameworks; test the
   novelty claim against the chosen venue), and finally tighten Abstract/§1.

## Off-limits (unchanged)

§5 Results placeholders, §3 hardware description, and all modeled numbers in
`analysis/thermal_bias*` / `docs/cad_fea_plan.md` — pending real lab/co-location data.
Sole exception: step 3's bracketing (adds cited measured context *around* predictions).

## Output discipline

Every step returns a reviewable diff + bibliography/matrix updates. Never auto-commit;
never push — repo is public and the PI visibility/embargo question is unresolved.
