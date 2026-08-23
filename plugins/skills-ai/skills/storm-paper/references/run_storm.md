# Running Mode A (the real STORM pipeline)

STORM is cloned at `~/Developer/storm` with an isolated venv at
`~/Developer/storm/.venv` and `knowledge-storm` installed. Runners live in
`examples/storm_examples/`. Use Mode A only for a **scoped subtopic** of the paper,
then pass output through the curation gate — never paste a STORM article into the paper.

## Configure once (pick ONE LLM row + ONE retriever row)

Copy `~/Developer/storm/secrets.toml.template` → `~/Developer/storm/secrets.toml`
(already git-ignored, `chmod 600`) and fill the pair you're using.

**LLM (need one):**
- Hosted API — set `OPENAI_API_KEY` (or Anthropic/Gemini/DeepSeek/Groq/Mistral key)
  and use the matching runner (`run_storm_wiki_gpt.py`, `_claude.py`, `_gemini.py`, …).
- **Local, no key** — run [Ollama](https://ollama.com) and use
  `run_storm_wiki_ollama.py` (or `_ollama_with_searxng.py` for a fully local stack).

**Retriever (need one):**
- Keyed web search — set one of `SERPER_API_KEY` / `BING_SEARCH_API_KEY` /
  `BRAVE_API_KEY` / `TAVILY_API_KEY` / `YDC_API_KEY`.
- **Keyless / local** — SearXNG (`run_storm_wiki_ollama_with_searxng.py`) or
  **VectorRM over your own corpus** (`run_storm_wiki_gpt_with_VectorRM.py`) — point it
  at your `.bib`/PDFs so retrieval stays inside vetted literature. Preferred for a
  citation-disciplined paper.

## Run (example: OpenAI + Serper)

```bash
cd ~/Developer/storm
./.venv/bin/python examples/storm_examples/run_storm_wiki_gpt.py \
  --output-dir ./storm_runs \
  --retriever serper \
  --do-research --do-generate-outline \
  --do-generate-article --do-polish-article
# then, when prompted / via --topic, use a SCOPED subtopic, not the whole paper title
```

Fully-local, no keys:
```bash
./.venv/bin/python examples/storm_examples/run_storm_wiki_ollama_with_searxng.py --help
```

Check each runner's `--help` for exact flags (they differ slightly per model).

## Scope the topic to a paper subsection

Do **not** use the paper's title as the STORM topic — you'll get a generic survey.
Instead run one tight subtopic per gap, e.g.:
- "Passive radiation shield geometry effects on low-cost outdoor temperature accuracy"
- "Field calibration transferability of low-cost electrochemical gas sensors over time"
- "Reported failure modes and uptime of long-term outdoor sensor-node deployments"

Take STORM's **citations and question coverage** as leads, locate the real
peer-reviewed sources, run them through `references/curation_gate.md`, and only then
integrate. Outputs land in `~/Developer/storm/storm_runs/` (git-ignored scratch).
