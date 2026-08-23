---
name: adaptive-plans
description: >-
  Scope a project into a tiered, trigger-driven roadmap — must-haves for v1, nice-to-haves, and
  "maybe later" items each tied to an explicit growth milestone that says when (and whether) to build them.
  Use this skill when a project's scope needs structuring over time, when the user asks "what should v1
  include", "help me prioritize features", "MVP vs later", "roadmap this", mentions
  must-haves/nice-to-haves, or invokes /adaptive-plans. Distinct from expand-and-contract (one-time in/out
  scope decision): this skill produces a living plan whose later tiers activate on milestones.
---

# Adaptive Plans — Milestone-Triggered Scoping

Split a project's ambitions into three tiers, where the deferred tiers aren't a graveyard — each deferred item carries an explicit, observable trigger stating when it earns its build. The premise: "later" without a trigger means never (or worse, means built now out of anxiety). A trigger converts scope anxiety into a decision already made.

## The three tiers

1. **Must-have** — v1 cannot ship or cannot demonstrate its core value without it. Apply the death test to every candidate: *"If v1 ships without this, is v1 pointless?"* If the honest answer is "no, just worse", it's not a must-have. Expect this tier to feel uncomfortably small — that's it working.
2. **Nice-to-have** — clear value, scheduled after v1 ships, ordered by value-to-effort. No triggers needed; these are queued, not conditional.
3. **Maybe-later** — built *only when its trigger fires*. Every item here gets a trigger that is observable and binary, plus a one-line note on why waiting is right (cost to build now vs. cost to retrofit).

Good triggers are events you can point at: "more than ~100 weekly users", "second data source gets added", "first user asks for export", "manual deploy exceeds 15 min/week", "the JSON file passes 50 MB". Bad triggers are dates, vibes, or "when we have time". If you can't name an observable trigger for an item, that's a finding — it probably belongs in Out, not Maybe-later.

Add a fourth list, **Out** — things explicitly not being built, with one line of why. The out-list is what actually prevents scope creep; review it with the user rather than letting it form silently. (If the scope is genuinely foggy, run `expand-and-contract` first to generate and sort the candidate pool, then bring the survivors here for tiering and triggers.)

## Output

Save to `docs/specs/<slug>/scope.md`:

```markdown
# <Project> — Adaptive Plan
Date: YYYY-MM-DD

## Must-have (v1)
- <item> — <one line on the core value it serves>

## Nice-to-have (post-v1 queue)
- <item> — value/effort note

## Maybe-later (trigger-gated)
- <item> · Trigger: <observable event> · Why wait: <one line>

## Out
- <item> — <why>

## Milestone watch
<the 3-5 triggers worth actively checking, and how to check them>
```

## Keeping it adaptive

- When a trigger fires, the decision is to *consider* the item with current information — promote it deliberately into the active queue, don't auto-build; the trigger was set with less knowledge than you have now.
- Revisit the plan at natural checkpoints (v1 ship, each milestone firing). Demote freely: a nice-to-have nobody missed for two months is telling you something.
- Feed the Must tier into `write-plan` for task decomposition (via `grill-me` first if requirements are still fuzzy). The tiers say *what and when*; the design and plan docs say *how*.
