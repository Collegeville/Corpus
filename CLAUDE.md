# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Jekyll static site archiving Mike Heroux's CS373 (Senior Research Seminar)
teaching material, split into three collections plus a philosophy section:
**Human Skills** (timeless techniques), **AI-Assisted Workflows** (timely,
tool-dependent, human-follows-with-AI-help), and **Agent Skills**
(downloadable `SKILL.md` files handed directly to an agent), under an
**About Corpus** section explaining the split. Deploys as a GitHub Pages
project site at `collegeville.github.io/Corpus/`.

## Commands

```bash
bundle install
bundle exec jekyll serve         # local dev server at http://localhost:4000
python3 scripts/audit.py         # static content audit — no Ruby/Jekyll needed, just PyYAML
```

`scripts/audit.py` checks front matter validity, slug/URL collisions,
that `related_ai_workflow` / `related_agent_skill` / `related_human_skill`
cross-links resolve, that internal links are wrapped in `relative_url`, and
Liquid tag balance in layouts/includes. Run it before committing content
changes. A clean run prints `ISSUES: 0`.

## Architecture

**Collections and where content lives.** Four Jekyll collections defined in
`_config.yml`, each backed by a `_<name>/` source directory and a matching
top-level `<name>/index.md` landing page that auto-lists the collection
(new files just need to be added to the `_<name>/` directory — no other
edits required for nav/index inclusion):

- `_about_corpus/` → `/about-corpus/` — uses `page.html` layout, ordered by
  a `title`/`summary`/`order` front matter field (no layout needed in the
  file itself, applied via `_config.yml` defaults).
- `_human_skills/` → `/human-skills/` — uses `skill.html` layout.
- `_ai_workflows/` → `/ai-workflows/` — uses `skill.html` layout.
- `_agent_skills/` → `/agent-skills/` — uses `skill.html` layout (collection
  entry only; the actual downloadable file lives separately under
  `assets/agent-skills/<slug>/SKILL.md`).

`_layouts/skill.html` is shared by all three skill-like collections and
renders the cross-link "marginalia" sidebar (category, tags, and the
`related_ai_workflow` / `related_agent_skill` / `related_human_skill`
companion links) by looking up `site.<collection>` for a doc whose `slug`
field matches — the lookup is by front-matter `slug`, not filename, so slug
must equal filename stem (`_human_skills/foo.md` needs `slug: foo`) or
cross-links silently fail to resolve. `scripts/audit.py` checks for this
mismatch across all three collections.

**baseurl discipline.** Deployed as a project site (`baseurl: "/Corpus"`,
not root), so every internal link in page bodies and templates must go
through Jekyll's `relative_url` filter — `{{ '/human-skills/foo/' |
relative_url }}` in Liquid, or the equivalent in Markdown body links. A
bare `/human-skills/foo/` link works locally at root but breaks once
deployed under `/Corpus/`. `scripts/audit.py` flags unwrapped internal
links across all four collections.

**Content templates.** Each Human Skill / AI-Assisted Workflow follows a
fixed 6-section H2 body structure (Definition → Learning Outcome → Core
Structure → Worked Example → Common Pitfalls → Rubric / Checklist) — see
README.md's "Adding a Human Skill" section for the full front matter shape
and an example file to copy from. AI-Assisted Workflow pages additionally
carry a visible "last verified" / "as of" note since they're expected to go
stale, unlike Human Skills. Agent Skills split into two files that must be
added together: the downloadable `assets/agent-skills/<slug>/SKILL.md`
(fully self-contained — any cross-reference to a Human Skill must be a full
`https://collegeville.github.io/Corpus/...` URL since the file travels
without the repo) and the `_agent_skills/<slug>.md` collection entry
(human-facing description + download link, repo-relative links are fine
here).

**Styling.** All design tokens (palette, type) are CSS custom properties at
the top of `assets/css/style.scss` — change values there, not scattered
through the stylesheet. Palette: CSB/SJU navy primary, muted vellum gold
secondary (used for the workflow/skill/companion cross-link chips), warm
paper background.

**`assets/examples/`** mirrors functional resources that Human Skill pages
depend on (e.g. the Using LaTeX worked example) locally in-repo rather than
linking to an external repo, so pages keep working if that source is
reorganized or removed.
