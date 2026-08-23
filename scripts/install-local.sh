#!/usr/bin/env bash
set -euo pipefail

usage() {
  printf '%s\n' "Usage: $0 [--both|--claude|--codex] [--force]"
}

mode="both"
force="false"
for arg in "$@"; do
  case "$arg" in
    --both) mode="both" ;;
    --claude) mode="claude" ;;
    --codex) mode="codex" ;;
    --force) force="true" ;;
    -h|--help) usage; exit 0 ;;
    *) usage >&2; exit 2 ;;
  esac
done

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source_root="$repo_root/plugins/skills-ai/skills"
shared_design="$repo_root/plugins/skills-ai/design-system"
stamp="$(date +%Y%m%d-%H%M%S)"
install_home="${SKILLS_AI_HOME_OVERRIDE:-$HOME}"

install_tree() {
  destination="$1"
  label="$2"
  backup_root="$(dirname "$destination")/skills-ai-backup-$stamp"
  linked=0
  skipped=0

  mkdir -p "$destination"
  for source in "$source_root"/*; do
    [ -d "$source" ] || continue
    name="$(basename "$source")"
    target="$destination/$name"

    if [ -L "$target" ] && [ "$(readlink "$target")" = "$source" ]; then
      continue
    fi

    if [ -e "$target" ] || [ -L "$target" ]; then
      if [ "$force" != "true" ]; then
        printf 'skip %s: %s already exists\n' "$label" "$target"
        skipped=$((skipped + 1))
        continue
      fi
      mkdir -p "$backup_root"
      mv "$target" "$backup_root/$name"
    fi

    ln -s "$source" "$target"
    linked=$((linked + 1))
  done

  platform_root="$(dirname "$destination")"
  design_target="$platform_root/design-system"
  if [ ! -e "$design_target" ] && [ ! -L "$design_target" ]; then
    ln -s "$shared_design" "$design_target"
  fi

  printf '%s: linked %d skills; skipped %d conflicts\n' "$label" "$linked" "$skipped"
  if [ -d "$backup_root" ]; then
    printf '%s backups: %s\n' "$label" "$backup_root"
  fi
}

case "$mode" in
  both)
    install_tree "$install_home/.agents/skills" "Codex"
    install_tree "$install_home/.claude/skills" "Claude"
    ;;
  codex) install_tree "$install_home/.agents/skills" "Codex" ;;
  claude) install_tree "$install_home/.claude/skills" "Claude" ;;
esac

stoic_target="$install_home/StoicDesign"
if [ ! -e "$stoic_target" ] && [ ! -L "$stoic_target" ]; then
  ln -s "$repo_root/plugins/skills-ai" "$stoic_target"
  printf 'Shared StoicDesign compatibility link: %s\n' "$stoic_target"
fi
