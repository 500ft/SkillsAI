---
name: engineering-problem-solving
description: Rigorous first-principles approach to engineering analysis, design, calculations, debugging, and technical review — at professional design-review standard, not classroom standard. Use this skill whenever the task involves engineering calculations, mechanical/structural/thermal/fluid analysis, design decisions, material selection, failure analysis, tolerancing, safety factors, test planning, reviewing technical work, or any problem where a wrong number or missed failure mode has real consequences — even if the user just asks "check my math", "will this part hold", "review my design", or "why did this break".
---

# Engineering Problem Solving

Solve and review engineering problems the way a senior engineer does in a design review: assumptions explicit, units carried, load paths traced, failure modes enumerated, every number defensible.

## The method

### 1. Frame before you compute
State in writing: what is being asked, knowns, unknowns, and the success criterion with a number and a unit ("deflection < 2 mm at 500 N", not "stiff enough"). If the requirement has no number, getting one *is* the first task.

### 2. Make every assumption explicit — then attack it
List assumptions before analysis: boundary conditions, load cases (including worst credible case, not just nominal), material state (as-rolled vs. annealed vs. welded HAZ), temperature, environment, duty cycle. For each, note whether it is conservative or optimistic. An unstated optimistic assumption is the most common root cause of analysis being wrong.

### 3. Draw the free body / trace the path
For mechanics: a free-body diagram with every force, moment, and reaction, checked for equilibrium. For other domains, the equivalent discipline: trace the load path, heat path, current path, or signal path end-to-end. Anything that enters must exit. Interfaces (joints, welds, bolts, connectors) are where paths concentrate and designs fail — give them their own analysis, never assume them rigid and perfect.

### 4. Governing equations before numbers
Write the symbolic relationship first, check its limiting behavior (does deflection → 0 as stiffness → ∞?), then substitute numbers. Carry units through every line — a units check catches a large share of all calculation errors. Use consistent SI internally; convert at the boundary.

### 5. Sanity-check every result three ways
- **Order of magnitude:** is 10⁴ MPa stress in aluminum plausible? (No — yield is ~10² MPa.)
- **Independent path:** estimate the same quantity by a different method (hand calc vs. simulation, energy method vs. force method).
- **Comparable hardware:** does the answer match what similar real designs use?

A result that fails any check is wrong until shown otherwise.

### 6. Enumerate failure modes, not just the obvious one
Run the checklist even when the answer "obviously" passes static strength: yield, fracture, fatigue (mean + alternating stress, stress concentrations Kt, surface finish), buckling (any slender member in compression), creep (T > ~0.4·Tm), wear, corrosion/galvanic pairs, vibration/resonance (forcing vs. natural frequencies), thermal expansion mismatch, loosening of fasteners. State which modes govern and which were screened out and why. Fatigue and buckling are the two most-missed governing modes.

### 7. Safety factors with justification
A safety factor is a claim about uncertainty, not a tradition. Justify the value from: load uncertainty, material property scatter, model fidelity, consequence of failure, and the applicable code/standard (ASME, AISC, ISO, FAA…). "FoS = 2 because that's typical" is not engineering. Distinguish factor against yield vs. ultimate vs. fatigue life.

### 8. Design for manufacturing and verification
Every dimension that matters gets a tolerance, and tolerances stack — check the worst-case (or RSS) stack against the functional requirement. Confirm the part can be made by the assumed process (draft angles, tool access, minimum wall, weldability) and *inspected* (a requirement you can't measure isn't a requirement). Define the test that would prove the design: load case, instrumentation, pass/fail number, and sample size.

## Reviewing someone else's work

Use the same method in reverse — and report findings in this format:

| Issue | Why it matters | Severity | How to fix it | Strong approach |
|---|---|---|---|---|

Severity scale: **Critical** (unsafe / fails requirement), **Major** (wrong result or unjustified margin), **Minor** (clarity, formatting, traceability). Check, in order: requirement defined → assumptions stated → FBD/load path correct → equations and units → numbers and arithmetic → failure modes covered → margins justified → manufacturable and testable → claims traceable to evidence. Be direct: a soft review that misses a governing failure mode helps no one.

## Communication standard

State the answer first, with its margin and governing failure mode. Then assumptions, method, and the numbers. Figures get axes, units, and captions; tables get sources. Distinguish *calculated* from *assumed* from *looked-up* values — and cite where looked-up values came from. Flag every result that depends on an unverified assumption.

## Anti-patterns

- Computing before framing ("plug and chug")
- Nominal-load-only analysis with no worst case
- Simulation results accepted without a hand-calc cross-check or mesh/convergence evidence
- Safety factor applied to the wrong quantity (stress vs. load vs. life — they differ for nonlinear problems)
- Treating a datasheet "typical" value as a minimum
- Reporting more significant figures than the inputs justify
