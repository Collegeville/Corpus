---
title: Effective Reviews
category: Discussion
tags: [reviewing, feedback, critique]
summary: A three-part structure for reviewing someone else's technical writing so the feedback actually helps them improve it.
related_ai_skill: ai-assisted-reviewing
source: https://maherou.github.io/Teaching/files/CS373/EffectiveReviews/
slug: effective-reviews
---

## Definition

An article review is feedback given to help an author improve their work before it's
distributed or published — whether you're a colleague reading a draft, a member of a conference
program committee, or a journal reviewer. The goal isn't to render a verdict; it's to give the
author something they can actually act on.

## Learning Outcome

After using this technique, you should be able to produce a review that demonstrates you
understood the piece, credits what it does well, and turns any weaknesses into concrete,
constructive direction — rather than a list of complaints.

## Core Structure

A good review has three parts, in this order:

1. **A 1–2 paragraph summary.** Summarize your understanding of the article. This does double
   duty: it shows the author you actually read and understood the piece, and if you
   misunderstood something, your summary will make that visible to both of you.
2. **A description of strengths.** What did you like about it? Was it technically solid, with
   sufficient breadth and depth? Did it have a good story line? Was the author efficient and
   effective with their words?
3. **A description of opportunities to improve.** How could the piece be better? Be
   constructive — the skill here is turning an observation of a weakness into a positive
   statement of what could be done to address it, not just naming the flaw.

Judge breadth, depth, wording, and structure against a simple four-part rubric:

- **Breadth of topic exploration** — is anything obviously missing from the discussion?
- **Depth of topic exploration** — does the piece demonstrate real knowledge, not just
  surface familiarity?
- **Enough words, no more** — is the prose expressive and efficient, free of vague or
  imprecise language and unnecessary jargon?
- **Story integrity** — does it have a real beginning, middle, and end? Does the conclusion
  synthesize the points rather than just repeat them?

## Worked Example

Suppose you're reviewing a colleague's draft technical report on a new caching strategy.

**Summary:** "This report proposes a write-through cache with a two-tier eviction policy and
evaluates it against LRU on three workloads, finding a 12% reduction in tail latency for
read-heavy traffic."

**Strengths:** "The evaluation methodology is sound — three genuinely different workloads,
clear baseline comparison, and the write path is described in enough detail that someone else
could reproduce it. The story has a real arc: motivation, design, evaluation, and a conclusion
that ties the latency result back to the original problem."

**Opportunities for improvement:** Rather than "the write-heavy workload results are missing" —
which just names the gap — reframe it as direction: "Adding a write-heavy workload to the
evaluation would let readers judge whether the 12% improvement holds outside the read-heavy case
this report focuses on, which would strengthen the paper's central claim."

Notice the third section doesn't just point at what's wrong — each note tells the author what to
actually do next.

## Common Pitfalls

- Skipping the summary — without it, the author can't tell whether you understood the piece,
  and can't trust the rest of your feedback.
- Naming a weakness without reframing it as something actionable — "this section is weak" helps
  no one; "this section would be stronger if it addressed X" does.
- Reviewing only at the sentence level (grammar, wording) while ignoring story integrity —
  or the reverse, commenting only on structure while ignoring whether the technical content is
  actually sound.
- Vague praise or vague criticism that doesn't map to any of the four rubric dimensions —
  "good job" and "needs work" aren't reviews.

## Rubric / Checklist

- [ ] Summary shows genuine understanding of the piece (1–2 paragraphs)
- [ ] Strengths are specific, not generic praise
- [ ] Breadth of topic exploration is addressed
- [ ] Depth of topic exploration is addressed
- [ ] Wording is evaluated: expressive and efficient, free of vague terms and jargon
- [ ] Story integrity is evaluated: real beginning/middle/end, conclusion that synthesizes
- [ ] Every weakness is reframed as a positive, actionable statement
