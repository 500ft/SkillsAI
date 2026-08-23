---
name: creativity
description: Use when the user asks for the creativity skill, creative ideation, divergent thinking, brainstorming, novel research topics, design variants, or ways to widen the option space before selecting a direction.
---

# Creativity

Use this skill as a compatibility wrapper for creative ideation. It does not replace domain-specific skills; it coordinates them.

## Workflow

1. State the creative frame: domain, constraints, target user, budget, timeline, available equipment, and what must not overlap with existing work.
2. Generate divergent options first. Do not score or collapse the list too early.
3. Route to the best installed skill when useful:
   - Research or project ideas: use `project-builder`, then `research`, `research-analysis`, or `research-deep` as needed.
   - Scope expansion and pruning: use `expand-and-contract`.
   - UI or visual directions: use `design-shotgun` or `frontend-design`.
   - Prompt concepts: use `promptimizer`.
   - Independent second opinions: use `swarm-consensus` only when the user asks for consensus or model cross-checking.
4. Convert promising ideas into concrete candidates with:
   - research question or design hypothesis
   - novelty claim and what evidence would be needed to support it
   - first experiment or prototype
   - measurable success criteria
   - expected difficulty, cost, and required skills
   - main technical risk
5. Separate creativity from proof. Do not claim a gap in scientific literature unless a literature search supports it.

## Output Standard

Prefer fewer, sharper ideas over long shallow lists unless the user explicitly asks for breadth. For research topics, include falsifiable questions and validation paths, not just titles.
