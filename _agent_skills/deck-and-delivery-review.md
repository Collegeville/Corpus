---
title: Deck & Delivery Review
category: Presenting
tags: [slides, presentations, review, assessment]
summary: An agent skill that assesses an uploaded slide deck in a single pass against Slides That Work and Presentations That Work, producing one structured report.
related_human_skill: slides-that-work
slug: deck-and-delivery-review
---

## Definition

This is a downloadable agent skill file, not a workflow to follow yourself — you hand it to an
agent along with your slide deck, and it produces one written assessment. Unlike
[Position Paper Grill]({{ '/agent-skills/position-paper-grill/' | relative_url }}), which
interviews an author who hasn't written anything yet, this skill runs a single pass over
something that already exists: it reads the deck once and reports back, rather than holding a
conversation.

It checks a deck against two companion Human Skills together, since they're meant to be used as
a pair: [Slides That Work]({{ '/human-skills/slides-that-work/' | relative_url }}) (deck-building
order and slide content discipline) and
[Presentations That Work]({{ '/human-skills/presentations-that-work/' | relative_url }}) (story
structure, scope, and delivery readiness).

## What it does

1. **Reads the deck** — every slide's title, body content, and any speaker notes present.
2. **Reconstructs the apparent structure** — what the deck's own takeaways seem to be, whether
   the opening and closing points actually match, and which slides support which takeaway.
3. **Scores against a combined checklist**, organized into five themes rather than two separate
   raw lists: takeaways & structure, slide content discipline, scope & focus, title & framing,
   and delivery readiness. Each item comes back as Pass, Concern, or Can't assess from deck —
   with the *can't assess* items (practiced timing, backup plan, anticipated questions, dress
   code) named explicitly rather than silently skipped, since a static deck genuinely can't
   confirm those.
4. **Closes with priorities** — the top three highest-impact fixes, plus a clear self-assess
   list for whatever the deck alone couldn't verify.

## Download

- [Download the skill file]({{ '/assets/agent-skills/deck-and-delivery-review/SKILL.md' | relative_url }})

## Notes and limitations

- This is deliberately single-pass, not interactive — it assumes the deck is being edited
  outside the agentic workflow, so it produces a complete report rather than asking follow-up
  questions.
- Several checklist items (practiced timing, a backup plan, anticipated questions, dress code)
  can't be verified from a deck alone. The skill flags these explicitly as things to self-check
  rather than guessing at them or leaving them out silently.
- Providing an intended time limit or speaker notes alongside the deck sharpens the assessment,
  but isn't required — the skill notes plainly where their absence limits what it can check.
