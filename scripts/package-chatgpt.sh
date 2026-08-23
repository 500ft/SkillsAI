#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
skills_root="$repo_root/plugins/skills-ai/skills"
design_root="$repo_root/plugins/skills-ai/design-system"
stoic_list="$repo_root/config/stoic-design-skills.txt"
output_root="${1:-$repo_root/dist/chatgpt}"

if ! command -v zip >/dev/null 2>&1; then
  printf '%s\n' "zip is required to create ChatGPT packages." >&2
  exit 1
fi

mkdir -p "$output_root"
temp_root="$(mktemp -d "${TMPDIR:-/tmp}/skills-ai-chatgpt.XXXXXX")"
trap 'rm -rf "$temp_root"' EXIT
count=0

for source in "$skills_root"/*; do
  [ -d "$source" ] || continue
  name="$(basename "$source")"
  stage="$temp_root/$name"
  mkdir -p "$stage"
  rsync -a --exclude '.DS_Store' --exclude '__pycache__' --exclude '*.pyc' "$source/" "$stage/"

  if grep -Fxq "$name" "$stoic_list"; then
    mkdir -p "$stage/design-system"
    rsync -a --exclude '.DS_Store' "$design_root/" "$stage/design-system/"
  fi

  archive="$temp_root/$name.zip"
  (
    cd "$stage"
    zip -q -r "$archive" .
  )
  mv "$archive" "$output_root/$name.zip"
  count=$((count + 1))
done

printf 'Created %d ChatGPT skill ZIPs in %s\n' "$count" "$output_root"
