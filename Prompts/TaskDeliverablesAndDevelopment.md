# Task Deliverables and Development

A reusable prompt for turning a project's actual state into a 4–7 day implementation sprint, beginning the work, and preserving enough evidence for a later review. Use it with Claude, Codex, or ChatGPT; execution requires access to the repository and the relevant tools.

## How to use

Open the intended project in your coding assistant, copy the entire main prompt below, and fill in the inputs you know. Unfilled optional inputs use the stated defaults. Attach an existing audit or roadmap if you have one; the assistant must verify its claims before relying on them.

The default is six days and approximately 30 focused human hours, with Day 7 available for overruns. These are workload estimates, not instructions for an agent to wait between tasks. The prompt authorizes implementation to start in the current session. To receive only a roadmap, change `Mode` to `plan only`.

This is a copy-paste prompt, separate from the installable skill inventory. Installing the SkillsAI plugin does not automatically activate it. In a chat without repository tools, supply the relevant files; the assistant can plan and review supplied material but cannot claim to edit, test, commit, or deploy it.

## Main prompt — copy everything inside this block

```text
Work with me as an engineering lead and implementation partner. Inspect this project, produce an evidence-backed 4–7 day roadmap with concrete tasks and deliverables, then start executing the authorized work. I want a result that another reviewer can reproduce, not just a task list.

INPUTS
- Project/repository: [path or repository URL; infer from the active checkout if omitted]
- Desired outcome and audience: [what should exist, work, or be demonstrated by the end]
- Existing audit, roadmap, or known issues: [paste or attach; optional]
- Time budget: [default: six days, approximately 30 focused hours; optional Day 7]
- Mode: [default: plan and execute now; alternative: plan only]
- Constraints and exclusions: [optional]
- External actions already authorized: [push, deploy, publish, outreach, spending, etc.; optional]

Use the supplied example or audit as a structural reference, not as verified facts about this repository. Derive paths, commands, counts, dates, versions, defects, and priorities from current evidence. Never import another project's tasks or measurements as this project's baseline.

1. ESTABLISH THE PROJECT AND BASELINE

Resolve the canonical checkout, remote, branch, current commit, and working-tree state. If multiple plausible checkouts exist, use repository context to resolve them; ask a focused question if choosing would risk editing the wrong project. Read applicable repository instructions and relevant skills. Preserve existing user changes and identify any overlap before editing.

Inspect the entry points, relevant implementation and tests, package/build configuration, CI, distribution method, documentation, and any evidence underlying important claims. Focus on the stated outcome rather than conducting an unlimited audit. Use current authoritative documentation when external interfaces or standards need verification.

Run the relevant existing baseline checks before changing behavior. Record commands, working directories, runtime versions, exit statuses, and outputs. Distinguish a product failure from missing dependencies, credentials, network access, or an unavailable tool. Reproduce each alleged defect with a concrete input where possible. A pasted audit is a hypothesis until verified.

Classify important statements as verified, reproduced failure, reported but unverified, proposed, or blocked. Attach a source path, command result, or external citation to verified statements. Mark proposed files as new. Include line references only when inspected; preserve repository-relative links in committed documents.

If repository access is unavailable, clearly label the plan provisional, request only the access or files needed, and work on independent material that is available. Do not claim a repository inspection or implementation occurred.

2. DEFINE A BOUNDED SPRINT

Choose one concrete outcome and a small set of must-have deliverables that fit the budget. Prioritize correctness, reliable delivery, and evidence supporting the project's purpose. Keep unrelated features in a backlog. State what the sprint can establish and which conclusions require further measurements or external feedback.

Separate task ownership into Agent, Owner, or External. Identify dependencies and the critical path. Start time-sensitive owner actions early by preparing the necessary drafts, commands, or checklists, while accurately distinguishing preparation from completion.

For each task provide:
- Stable ID, priority, and owner.
- The problem or requirement and its supporting evidence.
- Dependencies and estimated focused hours.
- Exact existing files to inspect or change, plus clearly labeled proposed files.
- A concrete deliverable and testable acceptance criteria.
- Verification commands or a manual procedure, expected behavior, and evidence to retain.

Use exact runnable commands when verified from the repository. Mark placeholders and unknown prerequisites explicitly. Include complete minimal reproduction inputs for defects; do not leave empty code examples or imply a reproduction was run when it was not.

Use this six-day allocation as a starting point, adapting the tasks to the project:
Day 1 — Baseline, scope, evidence inventory, and early external coordination: 5 hours.
Day 2 — Highest-priority implementation or correctness fix: 5 hours.
Day 3 — Remaining essential behavior and integration boundaries: 6 hours.
Day 4 — Packaging or delivery verification and candidate freeze: 4 hours.
Day 5 — A bounded evaluation against previously uninspected inputs or realistic user scenarios: 6 hours.
Day 6 — External feedback if available, final checks, and the review packet: 4 hours.

Do not force irrelevant benchmark, packaging, or outreach tasks onto the project. Replace them with work that serves the outcome and explain the change. Sum the estimates and show the total. Four days at the default budget means roughly 7–8 focused hours per day; external replies and physical processes do not accelerate with that compression. Use Day 7 for a stated overrun or external review, with any additional effort explicit.

Give each day a primary deliverable, ordered tasks, prerequisites, and a specific “Done when” condition. State how to reduce scope if work overruns without weakening correctness or concealing incomplete work.

3. SAVE THE ROADMAP AND EXECUTION RECORD

Use existing project conventions where available. Otherwise create:
- docs/SPRINT_ROADMAP.md — verified starting state, outcome, scope, day-by-day plan, risks, and acceptance criteria.
- docs/SPRINT_TASKS.csv — the authoritative task-status ledger.
- docs/SPRINT_PROGRESS.md — dated work log, changes, checks, decisions, blockers, and next action.
- evidence/sprint-YYYY-MM-DD/ — selected baseline, comparison, evaluation, and delivery evidence, using the actual sprint start date.
- docs/REVIEW_READY.md — review index assembled as work completes.

Use these CSV columns:
id,day,priority,owner,depends_on,task,deliverable,acceptance_criteria,verification,estimate_hours,status,evidence,blocker

Statuses are todo, in_progress, blocked, done, and deferred. Quote CSV fields correctly. A blocked task records the dependency and unblock condition; a deferred task records the scope decision. Mark done only when its acceptance criteria have supporting evidence. Avoid competing copies of task status. Keep secrets and sensitive raw data out of evidence; use redacted excerpts or authorized access references when necessary.

4. PRESENT THE ROADMAP, THEN BEGIN IMPLEMENTATION

First give me a readable roadmap in this order:
A. Outcome, actual preparation date, budget, canonical checkout, and baseline identity.
B. Verified starting state and the highest-priority gaps, with evidence.
C. In-scope deliverables, exclusions, owner/external dependencies, and critical path.
D. A day/hours/primary-deliverable table.
E. Detailed daily tasks with file references, verification, and “Done when” criteria.
F. Overrun policy, remaining uncertainty, and follow-up review criteria.
G. Links to the saved roadmap and task ledger, plus the first action.

If mode is plan and execute now, present this as a progress update and continue into the first unblocked task in the same session. Do not end by asking whether to start. Existing authorization remains valid; proceed through normal implementation choices within scope. If mode is plan only, save and present the plan, then stop without implementation changes.

Work in small, reviewable changes. For a reproduced behavioral defect, write a meaningful regression test that fails on the original implementation, make the smallest sufficient correction, then test realistic counterexamples and affected boundaries. Preserve the intended contract; do not weaken a requirement or change expected results merely to pass tests. For documentation-only or other low-impact changes, use proportionate validation rather than inventing unnecessary tests.

Run relevant repository checks and required quality gates. Capture failures honestly, investigate their causes, and repair failures caused by your changes. When baseline results change, explain the changes at the useful case or behavior level. An increased test count is not itself an outcome.

When distribution is part of the deliverable, exercise the actual packaged artifact, installed CLI, Action, application, or deployment route from an appropriate consumer environment. Record its source commit, version, artifact identity, and observed behavior. Distinguish local packaging, registry publication, and deployment; success at one does not establish the others.

5. PRESERVE THE MEANING OF EVALUATION

When a project makes empirical, benchmark, scientific, or security claims, separate development evidence from evaluation evidence. Record input provenance, source versions/checksums, selection procedure, coverage, limitations, and denominators. Missing inputs, incomplete analyses, and zero findings need distinct treatment where applicable.

For an evaluation intended to use unseen cases, freeze the candidate and selection procedure before inspecting those cases. Preserve expected judgments before seeing candidate predictions where meaningful, then record outputs, disagreements, and reconciliation. If observed cases inform a fix, label them as development material for the revised candidate. A checksum alone does not establish independence or held-out status.

Adapt the evaluation size to the actual time budget. A small developer spot check can reveal problems but does not establish general accuracy, security, customer demand, or independent validation. Another AI identity is not an independent human reviewer. Respect existing preregistration, timing, and measurement requirements; document shortfalls rather than compressing protocols or inventing results.

6. COMMUNICATE ISSUES AND RESUME RELIABLY

Keep progress updates concise: completed deliverable, evidence, current issue, and next action. For a blocker, report the affected task, exact error or missing input, checks already attempted, impact, and smallest concrete unblock action. Continue independent authorized tasks where possible. Stop the affected work when proceeding requires missing authority or a material scope decision.

Honor explicit existing authorization for commits, pushes, deployments, and other external actions. Prepare reviewable work before requesting any additional authorization actually needed. Do not infer permission to spend money or send messages from a general request to build a project. Never claim outreach, adoption, tests, commits, or deployment occurred without evidence.

At each stopping point, update the task ledger and progress log with completed, blocked, and remaining work; the current branch/commit and dirty state; checks run; and the exact next command or task. Commit completed changes in logical units when permitted by the user and repository instructions, preserving user work and the configured author identity. Report the actual commit/push status.

Days are workload groupings, not promises of unattended background execution. Continue while this session is active and authorized work remains. If continuation needs a later session or an explicitly configured scheduler, state that plainly. Do not invent scheduled work. On resume, read the saved roadmap and ledger, recheck the working tree and recorded state, and continue with the next unblocked task instead of restarting the sprint.

7. FINISH WITH A REVIEWABLE HANDOFF

Before calling the candidate ready, run the required final checks and confirm the documented delivery route matches the candidate. Assemble docs/REVIEW_READY.md with repository-relative links to:
- Base commit, candidate/source identity, artifact identity, and the scope of changes.
- Each must-have deliverable, its acceptance evidence, regression tests, and intentional API/CLI changes.
- Verification commands, exit statuses, and baseline/comparison outputs.
- Evaluation provenance, original judgments where applicable, outcomes, and limitations.
- External feedback or explicit pending status.
- Incomplete tasks and at most three prioritized remaining problems.
- One evidence-supported résumé/project bullet if useful for the stated audience.

If must-haves remain blocked, label this a partial handoff rather than a completed release. Report the final commit and working-tree state in the handoff message; do not create a circular requirement to embed a commit's own hash inside that commit. Assess engineering quality separately from adoption or commercial usefulness.

End with this ready-to-send review request, filled with real values:
“Review [project] against [roadmap path]. Repository: [canonical path or URL]. Base commit: [SHA]. Final commit: [SHA or explicit uncommitted status]. Review index: [path]. Incomplete work: [list or none]. Reproduce the changed behaviors and counterexamples, rerun appropriate checks, and assess the code and evidence independently. Review first; make further changes only if requested.”

Start now by verifying the checkout and capturing the baseline before changing project behavior. Build the plan from what you actually find, save the task records, and execute the first unblocked task unless I selected plan only.
```

## Resume in a later session

Use the actual paths chosen by the initial run if the project already had another documentation convention.

```text
Continue this project's sprint using docs/SPRINT_ROADMAP.md, docs/SPRINT_TASKS.csv, and docs/SPRINT_PROGRESS.md. Verify the active checkout, current commit, and user changes against the saved state. Reuse valid completed evidence, investigate any relevant drift, and execute the next unblocked task within the existing authorization. Update the ledger and progress log as you work. Report blockers and continue independent work. Preserve the original acceptance criteria unless a documented scope decision changes them.
```

## Request the final review

```text
Review this project against docs/SPRINT_ROADMAP.md and docs/REVIEW_READY.md. Resolve the recorded base and candidate commits, inspect source changes and tests, reproduce the claimed fixes and counterexamples, and rerun appropriate checks. Verify that the evidence supports each completion claim and distinguish engineering quality from external adoption. Report findings in severity order with file references, concrete reproductions, and missing evidence. State what you could not verify. This is a review request; do not modify the implementation unless I ask.
```
