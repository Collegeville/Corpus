"""Shared logic for building an Agent Skill's downloadable .zip.

Used by both build_agent_skill_zips.py (regenerates the committed zip files)
and audit.py (flags a zip that's gone stale relative to its source files).
Kept in one place so the two never drift apart.
"""
import zipfile
from io import BytesIO

# Fixed timestamp so rebuilding an unchanged skill produces byte-identical
# zip output — real file mtimes would make every rebuild look like a diff,
# and would make audit.py's stale-zip comparison always fail.
_FIXED_DATE_TIME = (2020, 1, 1, 0, 0, 0)


def build_zip_bytes(skill_dir, slug):
    """Zip every file in skill_dir (except a pre-existing <slug>.zip) under
    a top-level <slug>/ folder, so unzipping recreates the exact directory
    an agent's skills folder expects — just SKILL.md today, but this
    extends to a skill that ships supporting files alongside it too."""
    zip_name = f"{slug}.zip"
    buf = BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(skill_dir.rglob("*")):
            if not path.is_file() or path.name == zip_name:
                continue
            arcname = f"{slug}/{path.relative_to(skill_dir)}"
            info = zipfile.ZipInfo(arcname, date_time=_FIXED_DATE_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            zf.writestr(info, path.read_bytes())
    return buf.getvalue()
