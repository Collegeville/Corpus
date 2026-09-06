#!/usr/bin/env python3
"""Regenerate the downloadable .zip for every Agent Skill.

Run this after adding or editing anything under assets/agent-skills/<slug>/
and commit the updated .zip together with the source change —
scripts/audit.py flags a zip that's gone stale relative to its source files.
"""
from pathlib import Path

from agent_skill_zip import build_zip_bytes

ROOT = Path(__file__).resolve().parent.parent
AGENT_SKILLS_DIR = ROOT / "assets" / "agent-skills"


def main():
    for skill_dir in sorted(AGENT_SKILLS_DIR.iterdir()):
        if not skill_dir.is_dir():
            continue
        slug = skill_dir.name
        zip_path = skill_dir / f"{slug}.zip"
        new_bytes = build_zip_bytes(skill_dir, slug)
        if zip_path.exists() and zip_path.read_bytes() == new_bytes:
            print(f"up to date: {zip_path.relative_to(ROOT)}")
            continue
        zip_path.write_bytes(new_bytes)
        print(f"wrote: {zip_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
