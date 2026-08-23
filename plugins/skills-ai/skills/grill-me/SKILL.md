---
name: grill-me
description: Pre-flight requirements interrogation. Before implementing any new project, feature, or significant change, interrogate the user about requirements, surface the assumptions they didn't know they were making, and produce a strict design document that downstream planning and coding rely on. Use this skill whenever the user describes something they want built ("I want to make...", "build me...", "let's add..."), asks to start a project, or invokes /grill-me — BEFORE writing any code or implementation plan. Especially valuable when the request is vague, ambitious, or one sentence long.
---

# Grill Me — Pre-Flight Requirements Interrogation

Interrogate before you implement. An agent that starts coding from a one-line prompt fills every gap with silent assumptions, and each wrong assumption compounds through planning, coding, and testing. The cheapest place to kill a wrong assumption is here, before any code exists. The output of this skill is a design document precise enough that a separate agent with no other context could plan from it.

## Hard rules

- Write **no implementation code** during this skill. Not a prototype, not a snippet, not a scaffold. The deliverable is a design document.
- Never ask a question the repo, the conversation, or a quick search can answer. Asking lazy questions burns the user's patience and teaches them to give lazy answers. Investigate first, then ask only what genuinely requires their judgment.
- Every question must state why it matters and propose a default. A question without a default forces the user to do all the work; a default lets them say "yes" and move fast.
- Push back on vague answers. "It should be fast" is not a requirement; "search results under 200ms for 10k records" is. When you get vagueness, offer 2–3 concrete interpretations and make the user pick.

## Process

### Phase 1 — Ingest (silent)

Before asking anything, read what already exists: the repo structure, README, existing specs or docs, related code the change would touch, and anything the user attached or referenced. Form a hypothesis of what they want and where the genuine unknowns are. The quality of your questions depends entirely on this step.

### Phase 2 — Interrogation rounds

Ask in batches of 3–5 questions, highest-stakes first. If a structured question tool is available in your harness (e.g. AskUserQuestion), use it with concrete options; otherwise ask as a numbered list and wait for answers. Run 2–4 rounds — stop when no remaining unknown would materially change the design.

Cover these domains, skipping any the context already answers:

1. **Goal & users** — What does success look like, for whom? What problem does this actually solve?
2. **Scope boundary** — What is explicitly *in* v1, and what is explicitly *out*? The out-list prevents scope creep more than the in-list defines work.
3. **Data & interfaces** — What goes in, what comes out, what formats, what existing systems does it touch?
4. **Constraints** — Platform, language, dependencies allowed/banned, performance targets, deadline, budget.
5. **Failure modes & edge cases** — What happens on bad input, no network, concurrent use, empty state? What's the worst credible misuse?
6. **Success criteria** — How will the user verify it works? Each criterion must be checkable by a test or a demo step.

Format each question as: the question → one line on why it matters → your proposed default.

### Phase 3 — Assumption audit

Before writing the document, present a short list titled **"Assumptions I was about to make silently"** — the decisions you would have made on the user's behalf if they hadn't run this skill (e.g. "single-user, no auth", "data fits in memory", "English-only"). Each one gets a keep/change decision from the user. This list is the highest-value output of the interrogation; it surfaces exactly the gaps that cause rework.

### Phase 4 — Write the design document

Save to `docs/specs/<slug>/design.md` (create the directory; pick a short kebab-case slug for the feature). Use exactly this structure:

```markdown
# <Feature> — Design
Status: draft | approved
Date: YYYY-MM-DD

## Problem statement
## Goals
## Non-goals
## Users & primary flows
## Functional requirements
FR-1: <testable statement>
FR-2: ...
## Non-functional requirements
NFR-1: <with a number and a unit where possible>
## Interfaces & data
## Edge cases & failure modes
## Decisions
| Decision | Alternatives considered | Rationale |
## Open questions
## Acceptance criteria
AC-1: <verifiable check, maps to FRs>
## Out of scope
```

Functional requirements must be individually testable statements — if you can't imagine the test, the requirement is too vague to write down. The Decisions table records *why*, because six months from now the why is the only part that's not obvious from the code.

### Phase 5 — Sign-off and handoff

Present a tight summary (goals, scope boundary, key decisions, open questions) and ask the user to approve or correct. On approval, set `Status: approved` in the doc and point them at the next step: run `/write-plan` to decompose this design into executable micro-tasks. Do not start planning or coding yourself — that's a separate skill with a separate sign-off.
