---
title: Titles and Abstracts That Work
category: Writing
tags: [abstracts, titles, technical-writing]
summary: Koopman's five-part abstract structure — motivation, problem, approach, results, conclusions — for writing an abstract that earns the rest of the read.
related_ai_workflow: ai-assisted-abstract-drafting
source: https://collegeville.github.io/Scribe/TitlesAndAbstractsThatWork/
slug: titles-and-abstracts-that-work
---

## Definition

Writers want their work to be read, and a title and abstract are often the only chance to catch
a reader's attention before they decide whether to continue. The abstract in particular isn't a
summary written after the fact — it's a structured argument for why the work matters, built from
five specific parts (following Phil Koopman's widely-used structure): motivation, problem
statement, approach, results, and conclusions.

## Learning Outcome

After using this technique, you should be able to write an abstract where each sentence does one
of five specific jobs, state your results in numbers rather than vague qualifiers, and title the
work so it's both accurate and short enough to actually get read.

## Core Structure

Koopman's five parts of an abstract:

1. **Motivation** — why do we care about the problem and the results? If the problem isn't
   obviously interesting, lead with motivation; if it's a widely-recognized problem and you're
   making incremental progress on one piece of it, lead with the problem statement instead so
   readers know which piece you're addressing.
2. **Problem statement** — what problem are you solving, and what's the scope (a general
   approach, or a specific situation)? Avoid unnecessary jargon.
3. **Approach** — how did you go about it? Simulation, analytic models, a prototype,
   analysis of field data? What was the extent of the work, and what variables did you control,
   ignore, or measure?
4. **Results** — what's the actual answer, in numbers? Most strong technical papers conclude
   that something is a specific percentage faster, cheaper, or smaller than the alternative.
   Avoid vague hand-waving ("very," "significant") — the only license to be vague is when
   you're reporting an order-of-magnitude improvement, where exact figures would be misleading
   anyway.
5. **Conclusions** — what are the implications? Is this a major shift, a solid win, a useful
   negative result (a road sign that a path is a dead end), or something narrower? Are the
   results general, potentially generalizable, or specific to one case?

## Worked Example

A short abstract, with each sentence labeled by which Koopman part it fulfills:

> *(Motivation)* Search engines need up-to-date results, but re-crawling the entire web on every
> query is infeasible at scale. *(Problem statement)* We study how frequently individual web
> pages actually change, to determine how often a search index needs to be refreshed to stay
> current. *(Approach)* We collected weekly snapshots of 150 websites over one year and measured
> content and link-structure change using cosine distance between successive versions.
> *(Results)* Pages showed high turnover: 40% of pages present at the start of the year were gone
> by the end, and pages that changed significantly in one week were 3x more likely to change
> significantly again the following week than pages that had been stable. *(Conclusions)* Search
> engines could use a page's recent change history to predict its near-term volatility, targeting
> re-crawl budget toward pages likely to have changed rather than re-crawling uniformly.

Notice the Results sentence has actual numbers (40%, 3x) rather than "many pages changed
frequently" — that's the difference between a vague claim and one a reader can evaluate.

## Common Pitfalls

- Reporting results in vague qualifiers ("significant improvement") instead of numbers a
  reader can judge for themselves.
- Missing the problem statement — motivation without a clearly scoped problem leaves the
  reader unsure what was actually solved.
- A conclusions sentence that just repeats the results instead of stating their implication or
  scope of generality.
- A title so long or so clever it obscures what the work is actually about — catchy and short
  beats catchy and long.

## Rubric / Checklist

- [ ] Motivation is present and placed appropriately (before or after the problem statement,
      depending on how well-known the problem already is)
- [ ] Problem statement is clear and appropriately scoped
- [ ] Approach describes the actual method, not just "we studied X"
- [ ] Results are stated in numbers, not vague qualifiers
- [ ] Conclusions state implications and scope of generality
- [ ] Title is accurate and as short as it can be while staying accurate
