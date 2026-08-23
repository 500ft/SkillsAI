# SkillsAI

Portable home for the AI skills used by 500ft. The repository packages the same 78 skill directories for Claude Code, Codex, and ChatGPT without depending on machine-specific symlinks or plugin caches.

## What is included

- 78 user-installed skills under `plugins/skills-ai/skills/`
- Claude Code and Codex plugin manifests
- Marketplace manifests for direct installation from GitHub
- The shared Stoic design system required by the presentation and visual-design skills
- Safe local installers for `~/.claude/skills` and `~/.agents/skills`
- A ChatGPT ZIP exporter for uploading individual skills
- Validation and CI checks for manifests, inventory, symlinks, local paths, and likely secrets

The inventory is in [docs/skill-catalog.md](docs/skill-catalog.md). Platform-managed skills and downloaded plugin caches are intentionally not mirrored; see [docs/scope.md](docs/scope.md).

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
│   └── skills/                             # 78 portable skill packages
├── config/                                 # audited inventories
├── docs/                                   # catalog, scope, and notices
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
