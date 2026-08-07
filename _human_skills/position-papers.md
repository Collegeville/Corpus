---
title: Position Papers
category: Writing
tags: [position-papers, whitepapers, persuasive-writing]
summary: A tiered document structure for socializing and promoting an idea in an organization or community too large for everyone to read everything.
source: https://collegeville.github.io/Scribe/PositionPapers/
slug: position-papers
---

## Definition

In any organization or community larger than a few dozen people, a position paper — often
called a whitepaper, though "whitepaper" is the broader term — is the standard vehicle for
socializing and promoting a new idea. Its defining feature is that it's *tiered*: someone should
be able to get the primary points from a single-page executive summary, while someone who wants
the full case can read on. Not every reader owes you their full attention; the format assumes
that and plans for it.

## Learning Outcome

After using this technique, you should be able to structure an argument for change so that a
skimming reader gets the recommendation and a committed reader gets the full case — without
forcing either one through the wrong amount of material.

## Core Structure

A position paper has seven parts:

1. **Abstract** — a half-page description covering background, motivation, and a preview of
   what the document contains.
2. **Executive Summary** — a brief statement of the recommendations, essentially a restatement
   of the point-by-point items from part 6.
3. **Table of contents** — useful past five pages, important past ten.
4. **Introduction** — background, motivation, a description of the status quo, a vision of the
   goal, and a preview of your approach.
5. **Case study** *(optional)* — if a comparable situation exists that illustrates what you
   want to accomplish and how, include it. Not essential, but strengthens the argument when
   available.
6. **Full presentation of your case** — point by point, in compact language, for why change
   must happen and how it can be accomplished. Anticipate concerns and acknowledge risks. Each
   point follows the same four-part pattern:
   - Present status
   - Recommendation
   - Discussion
   - Risks and requirements
7. **Summary and conclusion**

## Worked Example

Point 6 (full presentation) applied to one item in a hypothetical position paper on adopting
continuous integration for a research software team:

> **Present status:** Code is merged to the main branch without automated testing; regressions
> are typically caught by users in production, weeks after the change that caused them.
>
> **Recommendation:** Require a passing automated test suite before any merge to main.
>
> **Discussion:** This shifts defect discovery from "a user reports it" to "a merge is blocked,"
> shortening the feedback loop from weeks to minutes and making the responsible change easy to
> identify.
>
> **Risks and requirements:** Requires initial investment in test coverage for currently
> untested modules, and may slow merge velocity in the short term while the team adjusts to the
> new gate.

That four-part pattern — status, recommendation, discussion, risk — repeats for each point in
the full presentation, giving the reader the same structure to follow throughout, even as the
specific content changes.

## Common Pitfalls

- Skipping the tiering — writing a single flat document forces every reader through the same
  depth, defeating the format's purpose.
- An executive summary that doesn't actually match the full presentation's recommendations,
  so a skimming reader walks away with the wrong takeaway.
- A "full presentation" that argues in prose rather than point by point, making it hard to
  follow which risk goes with which recommendation.
- Omitting risks and requirements — an argument for change that doesn't acknowledge cost or
  risk reads as unconvincing, not persuasive.

## Rubric / Checklist

- [ ] Abstract present (half-page, background + motivation + preview)
- [ ] Executive summary matches the recommendations in the full presentation
- [ ] Table of contents included if the document exceeds five pages
- [ ] Introduction lays out status quo, goal, and approach
- [ ] Case study included where one strengthens the argument
- [ ] Each point in the full presentation follows status → recommendation → discussion →
      risks/requirements
- [ ] Risks and anticipated concerns are acknowledged, not omitted
