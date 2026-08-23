---
name: research-analysis
description: Systematic analysis of research literature — triaging papers, judging relevance, ranking importance, grading evidence, and synthesizing findings with full traceability. Use this skill whenever the task involves academic papers, literature reviews, citation analysis, ranking or filtering search results from scholarly databases (OpenAlex, Semantic Scholar, arXiv, PubMed), evaluating evidence quality, building research maps, or deciding which papers/sources matter for a topic — even if the user just says "find papers on X", "what's the state of the art", or "is this source any good".
---

# Research Analysis

A doctrine for analyzing research literature so conclusions are evidence-backed, ranked honestly, and traceable to sources.

## The core separation: aboutness vs. importance

The single most common failure in literature analysis is letting *importance signals* (citations, venue prestige, author fame) answer a *relevance question* (is this paper about my topic?). A 10,000-citation paper that is tangential to the query is still tangential.

Always run two separate decisions:

1. **Eligibility gate (aboutness only).** Is the paper about the question? Inputs: title, abstract, keywords, topics. Forbidden inputs: citation counts, venue, recency, author reputation.
2. **Importance ranking (eligible papers only).** Among papers that passed the gate, which matter most? Now citations, citation velocity, venue, and network position are legitimate inputs.

Never blend the two into one score. A blended scalar lets fame buy relevance and makes every downstream conclusion suspect.

## Workflow

### 1. Define the question precisely
Write the research question as one sentence with the system, the method (if constrained), and the outcome of interest. A vague query produces a vague evidence set; diagnose query focus before trusting results.

### 2. Retrieve broadly, then gate
Cast a wide net (synonyms, adjacent terminology, both US/UK spellings). Then grade each candidate on an ordinal aboutness scale:

- **0 — off-topic:** exclude entirely; must not influence any downstream analysis
- **1 — tangential:** background only; never cite as primary support
- **2 — relevant:** addresses the question's domain directly
- **3 — core:** directly answers or tests the question

A paper with no abstract is *unverified*, not relevant — retain it but cap it below grade-2 papers and flag it. Absence of information never upgrades a source.

### 3. Rank importance within the eligible set
Useful signals, roughly in order of reliability:

- **Citations relative to peers** (percentile within field and year) beats raw counts — a 2024 paper with 80 citations may outrank a 2010 paper with 800.
- **Citation velocity** (citations/year) indicates rising influence, but shrink the estimate for papers under ~2 years old: tiny denominators produce flukes.
- **Network position:** papers referenced by multiple independent important papers are structurally important even with modest counts.
- **Source quality** is a weak tiebreaker, not a primary signal.

### 4. Grade the evidence, not just the paper
For each claim you extract, note the evidence type behind it:

| Grade | Evidence type |
|---|---|
| A | Replicated experiments, meta-analysis, validated against independent data |
| B | Single well-controlled experiment or validated simulation |
| C | Simulation/model without experimental validation; small-n results |
| D | Position paper, preprint claims, qualitative argument |

A field where every supporting paper is grade C/D has weak foundations — say so explicitly.

### 5. Synthesize with a claim ledger
Every claim in the output maps to specific papers. Use this structure:

```
Claim: [one sentence]
Support: [Author Year] (grade B), [Author Year] (grade C)
Counter-evidence or gaps: [...]
Confidence: high / moderate / low — and why
```

If a claim has no entry in the ledger, delete the claim.

## Pitfalls to actively check for

- **Citation-as-relevance leakage** — the failure mode this skill exists to prevent.
- **Survivorship of search results:** the database's ranking already filtered what you see; note what the query may have missed.
- **Recency framing:** "recent" must mean age-since-publication, not position within an arbitrary date window.
- **Redundancy masquerading as consensus:** five papers from one lab is one line of evidence, not five.
- **Retracted/withdrawn papers:** check before citing anything as support.
- **Distinctiveness ≠ novelty:** you can show an idea is distinct within the retrieved evidence; you cannot prove it is globally novel from one database.

## Output standard

Deliverables include: the precise question, the gating criteria used, an evidence table (paper, year, aboutness grade, evidence grade, key finding), the claim ledger, explicit gaps/limitations, and a one-paragraph honest summary of evidence strength. Every displayed ranking must be explainable from its inputs — if you can't say *why* a paper ranked where it did, re-derive the ranking.
