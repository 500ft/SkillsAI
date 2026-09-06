# SkillsAI

Portable home for the AI skills used by 500ft. The repository packages the same 90 skill directories for Claude Code, Codex, and ChatGPT without depending on machine-specific symlinks or plugin caches.

## What is included

- 90 user-installed skills under `plugins/skills-ai/skills/`
- Claude Code and Codex plugin manifests
- Marketplace manifests for direct installation from GitHub
- The shared Stoic design system required by the presentation and visual-design skills
- Safe local installers for `~/.claude/skills` and `~/.agents/skills`
- A ChatGPT ZIP exporter for uploading individual skills
- Validation and CI checks for manifests, inventory, symlinks, local paths, and likely secrets
- Copy-paste project prompts under `Prompts/`

The inventory is in [docs/skill-catalog.md](docs/skill-catalog.md). Platform-managed skills and downloaded plugin caches are intentionally not mirrored; see [docs/scope.md](docs/scope.md).

## Reusable prompts

[Task Deliverables and Development](Prompts/TaskDeliverablesAndDevelopment.md) turns a project's verified state into a 4–7 day roadmap, starts implementation, and keeps task status and evidence ready for a later review. It includes a main prompt, a session-resume prompt, and a final-review prompt for Claude, Codex, or ChatGPT.

Open the target project, copy the main prompt, and fill in the inputs you know. The default is six days and approximately 30 focused hours, with implementation starting immediately; select `plan only` for a roadmap without implementation. These Markdown prompts are used directly and are separate from plugin installation and ChatGPT skill ZIP exports.

## Install in Claude Code

```bash
claude plugin marketplace add 500ft/SkillsAI
claude plugin install skills-ai@skills-ai
```

Restart Claude Code after installation so every skill is discovered.

## Install in Codex

```bash
codex plugin marketplace add 500ft/SkillsAI
codex plugin add skills-ai@skills-ai
```

Restart Codex after installation.

## Upload to ChatGPT

ChatGPT accepts individual Agent Skill ZIPs rather than a Git marketplace installation. Build the upload-ready files locally:

```bash
git clone https://github.com/500ft/SkillsAI.git
cd SkillsAI
./scripts/package-chatgpt.sh
```

Then upload the desired files from `dist/chatgpt/` in ChatGPT's Skills settings. Each ZIP has `SKILL.md` at its root. Stoic design skills also receive a bundled copy of the shared design-system references.

## Standalone local installation

If plugins are unavailable, clone the repository and link the skills into both clients:

```bash
git clone https://github.com/500ft/SkillsAI.git
cd SkillsAI
./scripts/install-local.sh --both
```

Existing skills are never overwritten by default. Pass `--force` to move collisions into a timestamped backup before linking the repository copy.

## Repository layout

```text
SkillsAI/
├── .agents/plugins/marketplace.json       # Codex marketplace
├── .claude-plugin/marketplace.json        # Claude Code marketplace
├── plugins/skills-ai/
│   ├── .claude-plugin/plugin.json          # Claude Code plugin
│   ├── .codex-plugin/plugin.json           # Codex/OpenAI plugin
│   ├── design-system/                      # shared Stoic design references
│   └── skills/                             # 90 portable skill packages
├── config/                                 # audited inventories
├── docs/                                   # catalog, scope, and notices
├── Prompts/                                # reusable project and task prompts
└── scripts/                                # install, package, and validation tools
```

## Maintainer checks

```bash
python3 scripts/validate.py
claude plugin validate --strict .
```

`scripts/validate.py` has no third-party Python dependencies. CI runs it on every push and pull request.

## Licensing and provenance

This repository does not apply one blanket license to every bundled skill. Existing per-skill license files are preserved. Review [docs/third-party-notices.md](docs/third-party-notices.md) before redistributing individual packages.
