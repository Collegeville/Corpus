---
title: Scoping a Thesis Statement
category: Research
tags: [topic-selection, scoping, writing]
summary: Two short tests — one for picking a topic, one for sizing it — that keep a research project both meaningful and finishable.
source: https://maherou.github.io/Teaching/files/CS373/ThesisStatement/
slug: scoping-a-thesis-statement
---

## Definition

A thesis statement here does two jobs at once: it commits you to a topic, and it commits you
to a *scope*. Most struggling projects fail at one of those two commitments, not both — either
the topic doesn't actually need the researcher's technical background, or it's the right topic
stretched over far too much (or too little) ground. This skill is a pair of short tests you run
before you invest real time: one for whether the topic *area* is sound, and one for whether your
specific thesis statement is sized correctly within it.

## Learning Outcome

After using this technique, you should be able to look at a candidate research topic and state,
in a few sentences, why it requires your specific technical background, and whether the scope
you've picked is closer to "a chapter of a thesis" or "a full thesis" — and adjust before you've
sunk weeks into the wrong size.

## Core Structure

**Stage 1 — Is the topic area sound?**
Ask five questions before you commit to a topic area at all:

1. Does it have a genuine computer science component — does it actually require your CS
   background to do the research, not just to talk about it?
2. Are there sufficient high-quality, openly available resources to work from?
3. Is it an active area, with ongoing work and discussion happening now?
4. Can you build a demonstration or prototype in this area?
5. Is there real intellectual substance here, or is it thin once you look past the buzzwords?

A good way to narrow an overly broad topic area is to intersect a technology with an
application: not "artificial intelligence" but "artificial intelligence for recommendation
systems"; not "iris recognition" but "iris recognition in security applications." The
intersection does the narrowing for you.

**Stage 2 — Is your thesis statement the right size?**
Once the topic area passes Stage 1, test the specific thesis statement you've drafted along two
axes:

*Sufficiency* — does it require real technical depth?
- Sophisticated algorithms → sufficient
- Detailed data management approaches → sufficient
- Advanced software architecture and design → sufficient
- Reads like a marketing brochure → not sufficient
- Covers many concepts at a very high level → not sufficient

*Achievability* — can you actually finish it?
- Could you build a prototype or otherwise demonstrate the concepts? If not, it's not
  achievable in the time you have.
- Would a thorough treatment of this statement be one chapter of a thesis, or would it require
  a full thesis on its own? One chapter's worth is achievable; a full thesis is not.

## Worked Example

Take the narrowed topic from Stage 1: *iris recognition in security applications.* A first-draft
thesis statement might read: "Iris recognition is transforming how we secure sensitive systems."
Run it through Stage 2 — it fails sufficiency (no algorithms, data structures, or architecture
named; reads like a product pitch) and fails achievability (impossible to tell what would even
be built or tested).

A revised version: "This project evaluates the false-acceptance/false-rejection trade-off of two
open-source iris-recognition algorithms under degraded image conditions typical of low-cost
security cameras, and prototypes a preprocessing pipeline to improve match accuracy under those
conditions." That version names a concrete algorithmic comparison (sufficient), and describes a
prototype that could plausibly be built and evaluated within a semester (achievable) — one
chapter's worth of work, not a full thesis.

## Common Pitfalls

- Choosing a topic before checking whether resources actually exist for it (see: any topic
  whose "sources" turn out to be a company's own marketing pages).
- A thesis statement that could be true of a magazine article, not a technical project.
- Scoping at the level of a full thesis rather than a single chapter — ambition without a
  finish line.
- Confusing "an active, trendy area" with "an area with genuine technical substance available
  to study."
- Picking a topic area that's sound, but never re-testing the *specific* thesis statement drawn
  from it — Stage 1 and Stage 2 are both required, not either/or.

## Rubric / Checklist

**Topic area** (Stage 1 — all should be yes)
- [ ] Requires my CS background specifically
- [ ] Sufficient high-quality resources are available
- [ ] The field is active right now
- [ ] I can prototype or demonstrate something in it
- [ ] There's real intellectual substance here

**Thesis statement** (Stage 2)
- [ ] Sufficient: names algorithms, data management, or architecture — not brochure language
- [ ] Achievable: a prototype or demonstration is plausible
- [ ] Achievable: scoped to one thesis chapter, not a full thesis
