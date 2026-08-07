# Corpus

An archive of Mike Heroux's CS373 (Senior Research Seminar) teaching material —
College of St. Benedict / St. John's University — split into timeless **Human
Skills** and timely, tool-dependent **AI Skills**, with an **About Corpus**
section explaining the philosophy behind that split.

## Status

**The site is content-complete.** All 8 About Corpus pages, all 16 Human
Skills, and all 5 AI Skills are fully written — site structure, navigation,
styling, and content are all in place.

*About Corpus:* Origins, Philosophy, A Tale of Three Students, Knowledge
Half-Life, ReVeaL, Dialogue and Community, Self-Assessment, AI as
Collaborator.

*Human Skills (16):* Scoping a Thesis Statement, Captions That Work,
Effective Reviews, Position Papers, Titles and Abstracts That Work, Using
LaTeX, Predictions That Work, Retrospectives, Effective Mental Models,
Discussions That Work, Presentations That Work, Better Technical Writing,
Level of Expertise Dialogue, Knowledge Half-Life, Talks That Work,
Benchmarking a New Tool.

*AI Skills (5):* AI-Assisted Reviewing, AI-Assisted Abstract Drafting,
Generative AI Tools, AI-Assisted Development Exercise, AI Usage Policy
Development Kit.

A few pages (`ReVeaL`, `Dialogue and Community`) were written from
adjacent/related source material rather than a single dedicated source
page, since no single page covered them directly — each notes what it
draws from inline. `Knowledge Half-Life` and `Talks That Work` /
`Presentations That Work` each exist in two cross-linked forms (About
Corpus philosophy vs. Human Skill technique; two closely related but
distinct techniques) — see each page for how the split works.

**Not yet done:** exact hex/font polish pass beyond the current token
system (see Design notes below), and no actual `bundle exec jekyll build`
has been run against this exact final content set — worth a full local
build + link-check pass before publishing.

## Deployment

This site is set up to deploy as a **project site** at `collegeville.github.io/Corpus/`,
living alongside — not replacing — the org's existing root homepage. `_config.yml`'s
`baseurl` is set to `"/Corpus"` accordingly. Every internal link in this repo goes
through the `relative_url` filter, so if the deployment target ever changes (e.g. this
becomes the org's root site instead), `baseurl` is the only line that needs to change.

This repo should live at `Collegeville/Corpus` on GitHub (a separate repo from
`Collegeville/Collegeville.github.io`, which serves the existing root homepage), with
GitHub Pages enabled for it.

There's no `CNAME` file, since there's currently no separate custom domain
pointed at this site — add one later if that changes.

## Local development

```bash
bundle install
bundle exec jekyll serve
```

Then visit `http://localhost:4000`.

## Checking your work

Before committing, or in CI, run the static audit script — it doesn't need
Ruby or a Jekyll build, just Python 3 and PyYAML:

```bash
python3 scripts/audit.py
```

It checks front matter validity, slug/URL collisions, that every
`related_ai_skill` / `related_human_skill` cross-link actually resolves,
that every internal link in page bodies is correctly wrapped with
`relative_url` (so it respects `baseurl`) and points at a real page, and
basic Liquid tag balance in layouts/includes. A clean run prints
`ISSUES: 0`.

## Structure

```
_config.yml          site config, nav, collection definitions
_layouts/             default.html (shell), page.html (About Corpus pages),
                       skill.html (Human/AI Skills pages)
_includes/             head.html, sidebar.html, footer.html
assets/css/style.scss  design tokens + all site styling
assets/examples/         functional resources a skill page depends on to work
                          (e.g. assets/examples/latex/ — the Using LaTeX worked
                          example), mirrored locally rather than linked out to
                          an external repo so the page keeps working if that
                          repo is later reorganized or removed
_about_corpus/          About Corpus section pages (collection)
_human_skills/          Human Skills (collection)
_ai_skills/              AI Skills (collection)
about-corpus/index.md    About Corpus landing page
human-skills/index.md    Human Skills landing page (auto-lists the collection)
ai-skills/index.md       AI Skills landing page (auto-lists the collection)
index.md                 site homepage
```

Landing pages loop over their collection automatically — adding a new file to
`_human_skills/` or `_ai_skills/` makes it show up in the nav sidebar and on
the section's index page with no other edits required.

## Adding a Human Skill

Create a new file in `_human_skills/`, e.g. `_human_skills/my-skill.md`:

```yaml
---
title: My Skill Title
category: Writing        # Writing | Presenting | Research | Discussion | etc.
tags: [tag-one, tag-two]
summary: One sentence, shown on the index card and in <meta description>.
source: https://maherou.github.io/Teaching/files/CS373/...   # optional
related_ai_skill: my-ai-skill-slug                            # optional, must match
                                                                 # an AI Skill's `slug`
slug: my-skill                                                 # used for cross-linking
---
```

Then write the body using these H2 sections, in order (skip any that
genuinely don't apply, but don't reorder them):

1. **Definition** — what the skill is, in plain terms. The opening
   paragraph gets a manuscript-style drop cap automatically; no markup
   needed, just make sure the Definition section's first paragraph is the
   one you want that treatment on.
2. **Learning Outcome** — what someone should be able to do afterward.
3. **Core Structure** — the technique itself, broken into steps or parts.
4. **Worked Example** — a concrete, specific example, not a hypothetical
   sketch.
5. **Common Pitfalls** — a short bulleted list of ways this goes wrong.
6. **Rubric / Checklist** — a scannable list someone can check their own
   work against.

See `_human_skills/scoping-a-thesis-statement.md` for a complete example,
including how a merged-in secondary framework (the Good Topic Checklist)
was folded into Core Structure as a distinct earlier stage rather than
force-fit into the main flow.

## Adding an AI Skill

Same idea, in `_ai_skills/`, with `related_human_skill: <slug>` instead of
`related_ai_skill` if it pairs with a Human Skill. AI Skill pages should
carry a visible "last verified" or "as of" note in the body once they have
real content — these are explicitly expected to go stale and need
periodic refreshing, unlike Human Skills.

## Adding an About Corpus section

Add a file to `_about_corpus/`, with `title`, `summary`, and an `order`
field controlling its position in the sidebar and on the About Corpus
index page. Layout and section label are applied automatically via
`_config.yml` defaults — no front matter needed for those.

## Design notes

Palette and type are defined as CSS custom properties at the top of
`assets/css/style.scss` — change values there, not throughout the
stylesheet. The palette leans on CSB/SJU navy as the primary accent and a
muted vellum gold as a secondary accent (used for the "AI companion" /
"Human Skill companion" cross-link chips), against a warm paper
background — a quiet, restrained nod to the Benedictine/manuscript
setting rather than a literal one.

## Maintainers

Duong Do ([@duongdo27](https://github.com/duongdo27)),
Jim Willenbring ([@jwillenbring](https://github.com/jwillenbring)),
Mike Heroux ([@maherou](https://github.com/maherou)).
