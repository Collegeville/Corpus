---
title: Position Paper Grill
category: Writing
tags: [position-papers, elicitation, interview]
summary: An agent skill that interviews an author to elicit the content of a position paper, then assembles it into the standard seven-part structure.
related_human_skill: position-papers
slug: position-paper-grill
---

## Definition

This is a downloadable agent skill file, not a workflow to follow yourself — you hand it to an
agent (for example, by dropping it into a Claude Skills folder), and the agent does the
interviewing. It draws out the *content* of a position paper from an author through a structured
conversation, then assembles that content into the seven-part structure documented on
[Position Papers]({{ '/human-skills/position-papers/' | relative_url }}).

The author still owns the ideas and the argument. The skill's job is elicitation and structural
completeness — making sure nothing essential gets skipped, not inventing the case for the
author.

## What it does

The interview runs in a fixed order, anchoring the big picture before drilling into detail:

1. **Overarching vision** — present state and desired future state, elicited first since
   everything else hangs off it.
2. **Sub-goals or components** — captured directly if the author already has them in mind;
   otherwise drawn out through guided probes, without forcing a decomposition that isn't there
   yet.
3. **Per-component drill-down** — each component walked through the four-part pattern: status,
   recommendation, discussion, risks and requirements.
4. **Case study** — an explicit check for precedent or a comparable situation that would give a
   skeptical reader confidence the idea isn't untested.
5. **Executive summary** — synthesized afterward by the agent as a compressed restatement of the
   recommendations, rather than elicited separately from the author.

Once the interview is complete, the skill assembles the full seven-part document and checks it
against the same rubric used on the Position Papers page — the executive summary actually
matches the full presentation, every component has all four parts, risks aren't a token line.

## Download

- [Download the skill file]({{ '/assets/agent-skills/position-paper-grill/SKILL.md' | relative_url }})

## Notes and limitations

- This skill assumes the author already has an idea worth writing about — it elicits and
  structures, it doesn't generate the underlying insight.
- Sub-goal discovery is deliberately bounded (roughly 3–6 components) so the interview doesn't
  spiral indefinitely for an idea that doesn't naturally decompose further.
- The case study step is optional by design, matching the Position Papers page's own treatment
  of it — the skill asks, but doesn't force one where none exists.
