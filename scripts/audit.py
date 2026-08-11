#!/usr/bin/env python3
"""Static audit of the Corpus Jekyll source tree — no Ruby/Jekyll required.
Checks: front matter YAML validity, slug uniqueness, related_* cross-link
resolution, internal markdown link resolution, permalink collisions,
and basic Liquid tag balance in layouts/includes.
"""
import re, sys, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ISSUES = []
WARNINGS = []

def log_issue(msg): ISSUES.append(msg)
def log_warn(msg): WARNINGS.append(msg)

FM_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)

def parse_front_matter(path):
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        log_issue(f"{path}: no valid front matter block found")
        return {}, ""
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError as e:
        log_issue(f"{path}: YAML front matter error: {e}")
        return {}, m.group(2)
    return fm, m.group(2)

# --- Collect all collection docs ------------------------------------------
collections = {
    "human_skills": ROOT / "_human_skills",
    "ai_workflows": ROOT / "_ai_workflows",
    "agent_skills": ROOT / "_agent_skills",
    "about_corpus": ROOT / "_about_corpus",
}

# Collections that follow the slug/category/tags/summary skill template
# (about_corpus is title/summary/order instead, with no slug-based cross-linking).
SKILL_COLLECTIONS = ("human_skills", "ai_workflows", "agent_skills")

docs = {}          # coll_name -> {slug: (path, fm)}
slug_index = {}     # slug -> [(coll_name, path)]  (for global collision check)
url_index = {}      # generated url -> [(coll_name, path)]

PERMALINKS = {
    "human_skills": "/human-skills/{}/",
    "ai_workflows": "/ai-workflows/{}/",
    "agent_skills": "/agent-skills/{}/",
    "about_corpus": "/about-corpus/{}/",
}

for coll, dirpath in collections.items():
    docs[coll] = {}
    if not dirpath.exists():
        log_issue(f"Missing collection directory: {dirpath}")
        continue
    for f in sorted(dirpath.glob("*.md")):
        fm, body = parse_front_matter(f)
        slug = fm.get("slug")
        filename_base = f.stem
        if coll in SKILL_COLLECTIONS and not slug:
            log_issue(f"{f}: missing required 'slug' front matter field")
        # Jekyll uses filename (not slug field) to build :path in permalink
        # unless a custom permalink is set — flag mismatch since our whole
        # cross-link system relies on 'slug' matching the filename.
        if slug and slug != filename_base:
            log_issue(f"{f}: front matter slug '{slug}' does not match filename '{filename_base}' — "
                      f"generated URL will use '{filename_base}', but related_* lookups elsewhere "
                      f"search by the 'slug' field. This WILL break cross-links if anything points to '{slug}'.")
        required_common = ["title"]
        for field in required_common:
            if field not in fm:
                log_issue(f"{f}: missing required front matter field '{field}'")
        if coll in SKILL_COLLECTIONS:
            for field in ["category", "tags", "summary"]:
                if field not in fm:
                    log_warn(f"{f}: missing recommended field '{field}'")
        docs[coll][filename_base] = (f, fm, body)
        slug_index.setdefault(filename_base, []).append((coll, f))
        url = PERMALINKS[coll].format(filename_base)
        url_index.setdefault(url, []).append((coll, f))

# --- Slug / URL collisions --------------------------------------------------
for slug, entries in slug_index.items():
    colls = set(c for c, _ in entries)
    if len(entries) > 1 and len(colls) == 1:
        log_issue(f"Duplicate filename '{slug}' within {entries[0][0]}: {[str(p) for _, p in entries]}")

for url, entries in url_index.items():
    if len(entries) > 1:
        log_issue(f"URL collision at {url}: {[str(p) for _, p in entries]}")

# --- related_ai_workflow / related_agent_skill / related_human_skill resolution ---
for coll in SKILL_COLLECTIONS:
    for filename_base, (f, fm, body) in docs[coll].items():
        for field, target_coll in [
            ("related_ai_workflow", "ai_workflows"),
            ("related_agent_skill", "agent_skills"),
            ("related_human_skill", "human_skills"),
        ]:
            val = fm.get(field)
            if val and val not in docs[target_coll]:
                log_issue(f"{f}: {field}: '{val}' does not match any slug/filename in {target_coll}")

# --- Internal markdown links: /human-skills/x/, /ai-workflows/x/, /agent-skills/x/, /about-corpus/x/ ---
# Matches both bare root-relative links (a bug, since they ignore baseurl) and
# the correct Jekyll-relative_url-wrapped form.
LINK_RE = re.compile(r"\((/(?:human-skills|ai-workflows|agent-skills|about-corpus)/([a-z0-9\-]+)/)\)")
LIQUID_LINK_RE = re.compile(r"\{\{\s*'(/(?:human-skills|ai-workflows|agent-skills|about-corpus)/([a-z0-9\-]+)/)'\s*\|\s*relative_url\s*\}\}")

all_md_files = []
for coll, dirpath in collections.items():
    all_md_files.extend(sorted(dirpath.glob("*.md")))
for extra in ["index.md", "human-skills/index.md", "ai-workflows/index.md", "agent-skills/index.md", "about-corpus/index.md"]:
    p = ROOT / extra
    if p.exists():
        all_md_files.append(p)

section_map = {
    "human-skills": "human_skills",
    "ai-workflows": "ai_workflows",
    "agent-skills": "agent_skills",
    "about-corpus": "about_corpus",
}

for f in all_md_files:
    text = f.read_text(encoding="utf-8")
    for full_url, target_slug in LINK_RE.findall(text):
        log_issue(f"{f}: hardcoded internal link {full_url} bypasses baseurl — "
                  f"should be wrapped as {{{{ '{full_url}' | relative_url }}}}")
    for full_url, target_slug in LIQUID_LINK_RE.findall(text):
        section = full_url.strip("/").split("/")[0]
        target_coll = section_map[section]
        if target_slug not in docs[target_coll]:
            log_issue(f"{f}: broken internal link {full_url} — no matching file in {target_coll}")

# --- Liquid tag balance in layouts/includes ---------------------------------
def check_liquid_balance(path):
    text = path.read_text(encoding="utf-8")
    tag_re = re.compile(r"\{%-?\s*(\w+)")
    stack = []
    block_openers = {"if": "endif", "for": "endfor", "unless": "endunless", "capture": "endcapture"}
    closers = {v: k for k, v in block_openers.items()}
    for m in tag_re.finditer(text):
        tag = m.group(1)
        if tag in block_openers:
            stack.append(tag)
        elif tag in closers:
            if not stack:
                log_issue(f"{path}: unmatched '{{% {tag} %}}' with no open block")
            elif block_openers[stack[-1]] != tag:
                log_issue(f"{path}: mismatched close tag '{{% {tag} %}}', expected '{{% {block_openers[stack[-1]]} %}}'")
            else:
                stack.pop()
    if stack:
        log_issue(f"{path}: unclosed Liquid block(s): {stack}")
    # rough brace balance
    if text.count("{{") != text.count("}}"):
        log_issue(f"{path}: unbalanced {{{{ }}}} output tags ({text.count('{{')} open vs {text.count('}}')} close)")
    if text.count("{%") != text.count("%}"):
        log_issue(f"{path}: unbalanced {{% %}} tags ({text.count('{%')} open vs {text.count('%}')} close)")

for pattern in ["_layouts/*.html", "_includes/*.html"]:
    for f in sorted(ROOT.glob(pattern)):
        check_liquid_balance(f)

# --- _config.yml sanity ------------------------------------------------------
cfg_path = ROOT / "_config.yml"
try:
    cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
    for coll in ["human_skills", "ai_workflows", "agent_skills", "about_corpus"]:
        if coll not in cfg.get("collections", {}):
            log_issue(f"_config.yml: collection '{coll}' not declared")
except yaml.YAMLError as e:
    log_issue(f"_config.yml: YAML error: {e}")

# --- head.html / sidebar.html reference check (asset paths) -----------------
head = (ROOT / "_includes/head.html").read_text(encoding="utf-8")
if "style.css" not in head:
    log_warn("_includes/head.html: doesn't reference /assets/css/style.css")
scss = ROOT / "assets/css/style.scss"
if not scss.exists():
    log_issue("assets/css/style.scss missing")
elif not scss.read_text(encoding="utf-8").startswith("---"):
    log_issue("assets/css/style.scss missing required '---' front matter (Jekyll won't process it as Sass without this)")

# --- Report -------------------------------------------------------------
print(f"\nDocs found: human_skills={len(docs['human_skills'])} ai_workflows={len(docs['ai_workflows'])} "
      f"agent_skills={len(docs['agent_skills'])} about_corpus={len(docs['about_corpus'])}")
print(f"\n{'='*60}\nISSUES: {len(ISSUES)}\n{'='*60}")
for i in ISSUES:
    print(f"  ✗ {i}")
print(f"\n{'='*60}\nWARNINGS: {len(WARNINGS)}\n{'='*60}")
for w in WARNINGS:
    print(f"  ! {w}")
print()
