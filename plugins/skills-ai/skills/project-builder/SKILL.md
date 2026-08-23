---
name: project-builder
description: Turn evidence (papers, data, prior art, requirements) into well-scoped, executable project plans with concrete first experiments and honest feasibility assessment. Use this skill whenever the task involves generating project ideas, scoping a research or engineering project, choosing between project directions, planning an MVP or prototype, defining milestones and first experiments, or evaluating whether a proposed project is feasible and worth doing — even if the user just says "what should I build", "give me project ideas from these papers", or "help me plan this project".
---

# Project Builder

Generate and scope projects that are evidence-backed, specific, executable, and honest about what they can claim.

## Doctrine

A good project direction is a *supported combination*, not an invention. It assembles ingredients that the evidence actually contains, and its first step is an experiment someone can run next week. Avoid the two failure poles: the vague aspiration ("use ML to improve manufacturing") and the unsupported fantasy (a method/system pairing no evidence connects).

## Step 1 — Extract ingredients from the evidence

From the papers, prior art, or requirements at hand, list:

- **Methods:** techniques with a track record (CFD, surrogate modeling, PID control, fatigue testing, topology optimization…)
- **Systems / applications:** concrete hardware or domains (HVAC diffusers, battery packs, robotic grippers…)
- **Outcomes:** measurable quantities (pressure drop, temperature uniformity, cycle life, positioning accuracy…)
- **Data & materials available:** datasets, test rigs, sensor logs, materials on hand
- **Limitations in the evidence:** weak validation, sparse benchmarks, fragmented results — these are project opportunities, not just caveats

## Step 2 — Form candidates under hard constraints

A candidate qualifies only if it:

1. Has at least one supporting source per claimed ingredient
2. Combines **at least two of**: method, system/application, measurable outcome
3. Uses only method↔system pairings the evidence supports (or explicitly labels the pairing as the hypothesis being tested)
4. Is not a duplicate of another candidate with different outcome words
5. Names a concrete first experiment
6. Traces every element back to its sources

## Step 3 — Score and rank candidates

```
30% evidence strength   — how many independent sources support it, and how directly
25% specificity         — named method + named system + numeric outcome beats generalities
20% execution fit       — matches available skills, equipment, budget, and timeline
15% distinctiveness     — different from the other candidates and from what the evidence already saturates
10% traceability        — every claim maps to a source
```

Use **distinctiveness, not novelty** — you can show a project differs from the retrieved evidence; you cannot prove global novelty from one search. Never claim "no one has done this."

## Step 4 — Merge duplicates, keep real distinctions

Merge candidates into one multi-objective project when their outcomes can be measured by the **same experiment or dataset** (e.g., three surrogate-modeling-for-HVAC projects differing only in outcome metric). Keep candidates separate when they need different methods, different physics, different data sources, special safety evidence, or substantially different experiments. Fewer, stronger directions beat a full card deck of near-duplicates.

## Step 5 — Define the first experiment

Every project ships with a first experiment specified to this standard:

- **Hypothesis:** one falsifiable sentence
- **Setup:** equipment/data/tools, with what already exists vs. must be acquired
- **Variables:** what is varied, what is measured, what is held constant
- **Success criterion:** a number — "surrogate predicts pressure drop within 10% of CFD on 20 held-out cases"
- **Timebox:** smallest version runnable in 1–2 weeks
- **Kill criterion:** the result that would tell you to stop or pivot

If you can't write the kill criterion, the project isn't scoped yet.

## Output format

For each project direction:

```
## [Project title — method + system + outcome]
Why this, why now: [2-3 sentences grounded in the evidence's gaps]
Supporting evidence: [sources, with what each contributes]
Scope: in / out
First experiment: [the 6-field spec above]
Risks & honest limits: [feasibility risks; what this project cannot claim]
Score: [the 5-factor breakdown, not just a total]
```

## Pitfalls

- Filling every slot: present 3 strong directions over 8 weak ones
- Outcome-word duplication dressed as variety
- "Novel" claims from limited evidence
- First experiments that are actually month-three experiments — shrink until it fits two weeks
- Scoring execution fit against an idealized team instead of the actual person/resources
- Ignoring the limitations in the evidence — the gaps are where the best projects live
