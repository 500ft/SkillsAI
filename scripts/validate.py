#!/usr/bin/env python3
"""Validate the portable SkillsAI inventory without third-party dependencies."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "skills-ai"
SKILLS = PLUGIN / "skills"
EXPECTED = ROOT / "config" / "skills.txt"
SECRET_PATTERNS = {
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{24,}\b"),
    "Anthropic key": re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}\b"),
    "GitHub token": re.compile(r"\b(?:ghp|github_pat)_[A-Za-z0-9_]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"),
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}
FORBIDDEN_FILES = {".env", "id_rsa", "id_ed25519"}
FORBIDDEN_SUFFIXES = {".pem", ".p12", ".pfx"}
LOCAL_HOME = "/" + "Users" + "/" + "redhose"


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"invalid JSON: {path.relative_to(ROOT)} ({exc})")
        return {}
    if not isinstance(value, dict):
        errors.append(f"JSON root must be an object: {path.relative_to(ROOT)}")
        return {}
    return value


def frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"missing YAML frontmatter: {path.relative_to(ROOT)}")
        return {}
    end = text.find("\n---", 4)
    if end < 0:
        errors.append(f"unclosed YAML frontmatter: {path.relative_to(ROOT)}")
        return {}
    lines = text[4:end].splitlines()
    values: dict[str, str] = {}
    key: str | None = None
    for line in lines:
        match = re.match(r"^([A-Za-z0-9_-]+):(?:\s*(.*))?$", line)
        if match:
            key = match.group(1)
            values[key] = (match.group(2) or "").strip()
        elif key and (line.startswith(" ") or line.startswith("\t")):
            values[key] = f"{values[key]} {line.strip()}".strip()
    return values


def validate_inventory(errors: list[str]) -> int:
    expected = [line.strip() for line in EXPECTED.read_text(encoding="utf-8").splitlines() if line.strip()]
    actual = sorted(path.name for path in SKILLS.iterdir() if path.is_dir())
    if actual != sorted(expected):
        missing = sorted(set(expected) - set(actual))
        extra = sorted(set(actual) - set(expected))
        if missing:
            errors.append(f"missing skills: {', '.join(missing)}")
        if extra:
            errors.append(f"unexpected skills: {', '.join(extra)}")

    names: list[str] = []
    for directory in sorted(path for path in SKILLS.iterdir() if path.is_dir()):
        skill_file = directory / "SKILL.md"
        if not skill_file.is_file():
            errors.append(f"missing SKILL.md: {directory.relative_to(ROOT)}")
            continue
        metadata = frontmatter(skill_file, errors)
        name = metadata.get("name", "").strip(" '\"")
        description = metadata.get("description", "").strip(" '\"|>-")
        if not name:
            errors.append(f"missing skill name: {skill_file.relative_to(ROOT)}")
        else:
            names.append(name)
        if not description:
            errors.append(f"missing skill description: {skill_file.relative_to(ROOT)}")

    duplicates = sorted(name for name, count in Counter(names).items() if count > 1)
    if duplicates:
        errors.append(f"duplicate skill names: {', '.join(duplicates)}")
    return len(actual)


def validate_manifests(errors: list[str]) -> None:
    claude_plugin = load_json(PLUGIN / ".claude-plugin" / "plugin.json", errors)
    codex_plugin = load_json(PLUGIN / ".codex-plugin" / "plugin.json", errors)
    claude_market = load_json(ROOT / ".claude-plugin" / "marketplace.json", errors)
    codex_market = load_json(ROOT / ".agents" / "plugins" / "marketplace.json", errors)
    for label, payload in (("Claude plugin", claude_plugin), ("Codex plugin", codex_plugin)):
        if payload.get("name") != "skills-ai":
            errors.append(f"{label} name must be skills-ai")
        if payload.get("version") != "1.0.0":
            errors.append(f"{label} version must be 1.0.0")
    for label, payload in (("Claude marketplace", claude_market), ("Codex marketplace", codex_market)):
        if payload.get("name") != "skills-ai":
            errors.append(f"{label} name must be skills-ai")
        plugins = payload.get("plugins")
        if not isinstance(plugins, list) or len(plugins) != 1 or plugins[0].get("name") != "skills-ai":
            errors.append(f"{label} must expose exactly the skills-ai plugin")


def validate_portability(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        relative = path.relative_to(ROOT)
        if ".git" in relative.parts or "dist" in relative.parts:
            continue
        if path.is_symlink():
            errors.append(f"symlink is not portable: {relative}")
            continue
        if not path.is_file():
            continue
        if path.name in FORBIDDEN_FILES or path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"credential-like file is forbidden: {relative}")
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if LOCAL_HOME in text:
            errors.append(f"machine-specific path found: {relative}")
        for label, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{label} found in {relative}")


def main() -> int:
    errors: list[str] = []
    count = validate_inventory(errors)
    validate_manifests(errors)
    validate_portability(errors)
    if errors:
        print("SkillsAI validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"SkillsAI validation passed: {count} skills, dual manifests, portable tree")
    return 0


if __name__ == "__main__":
    sys.exit(main())
