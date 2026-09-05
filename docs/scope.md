# Repository scope

SkillsAI is an audited snapshot of user-installed, reusable skill packages—not a copy of every skill visible to one application.

The repository also contains manually used, copy-paste prompts under `Prompts/`. They are separate from the 78-skill inventory and are not installed or exported by the skill packaging scripts.

## Included

- Standalone directories from `~/.agents/skills/`
- The 21 user-installed StoicDesign skill directories that were locally linked into that collection
- The shared Stoic design-system files those skills reference
- Existing resources, scripts, assets, and per-skill license files

## Intentionally excluded

- `~/.agents/skills/.system/`: host-managed OpenAI skills such as product documentation, image generation, and skill installation
- `~/.codex/plugins/cache/`: downloaded OpenAI plugin cache
- `~/.claude/plugins/`: downloaded Claude plugin cache
- Application binaries, credentials, settings, transcripts, and machine-specific state
- Generated ChatGPT ZIPs under `dist/`

System and cached skills should be installed or updated by their owning platform. Mirroring them here would freeze platform-owned code and create duplicate skill registrations.

## Snapshot date

The initial inventory was reconciled on 2026-08-23. `config/skills.txt` is the completeness gate used by CI.
