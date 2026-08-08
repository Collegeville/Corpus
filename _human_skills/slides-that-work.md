---
title: Slides That Work
category: Presenting
tags: [presenting, slides, workflow]
summary: Build a presentation backwards — key takeaways first, then the middle, then the intro last — so every slide earns its place.
related_human_skill: presentations-that-work
source: https://maherou.github.io/Teaching/files/CS373/TalksThatWork/
related_agent_skill: deck-and-delivery-review
slug: slides-that-work
---

## Definition

Most people build a presentation in the order it's delivered: intro, then body, then a
conclusion tacked on at the end. This technique inverts that order deliberately. You decide your
key takeaways first, build the middle of the talk to support them, and only write the
introduction once you already know exactly what you're building toward. The result is a talk
where every slide can be traced back to a specific point you decided mattered — rather than a
talk padded with content you happened to have.

This is a close companion to [Presentations That Work]({{ '/human-skills/presentations-that-work/' | relative_url }}):
that skill covers the overall story structure and delivery discipline, while this one is
specifically about *the order in which you build the thing*.

## Learning Outcome

After using this technique, you should be able to construct a presentation in reverse — starting
from a small set of takeaways, building supporting content around them, and closing with an
introduction that sets up exactly the story you're about to tell — rather than starting from a
blank intro slide and hoping a coherent structure emerges.

## Core Structure

**1. Key takeaways — write these first, then iterate.**
Determine the handful of points (3–5) you want the audience to remember:
- What's the single most important point?
- What's next?
- What's next after that?
- Do you have a final takeaway that synthesizes everything above it?

**2. Middle slides — built to support the takeaways.**
Every slide in this section should connect to one of your key takeaways, either by informing the
audience about a concept they need, or by justifying a statement you're making. Anything that
doesn't inform or support a key point doesn't belong. Slides should complement what you say, not
duplicate it: put data, diagrams, and detailed information on the slide; put quotes on the slide
and trust the audience to read them rather than reading them aloud; let your spoken words carry
the story arc and the big picture, not the slide text.

**3. Intro — created last, after everything else exists.**
Only once the middle and the takeaways are locked in do you sketch the story: a beginning,
middle, and end for the talk as a whole. Writing the intro last means you're not guessing at a
structure you'll have to retrofit — you already know exactly what the talk delivers.

**4. Checklist, applied across the whole talk:**
- Pick a compelling title.
- Pick a realistic scope — the talk is advertisement for your paper, not a replacement for it;
  you won't be able to cover everything.
- Iterate across the slides: make sure each key point is understandable and believable, and cut
  anything unnecessary, even content you personally like.
- Practice against the actual time limit. Ending a minute or so early is fine — if you're
  significantly short, you missed a chance to say more. Running long is never acceptable; you
  must end on time.

## Worked Example

A talk on an adaptive caching project, built in order:

**Takeaways first:** (1) adaptive eviction beats static LRU under bursty workloads, (2) the
adaptation overhead is small enough to be worth it, (3) synthesis — this makes adaptive caching
practical for latency-sensitive services, not just a research curiosity.

**Middle, built to support them:** one slide with a benchmark chart supporting takeaway 1 (data
on the slide, the comparison story spoken aloud); one slide with an overhead measurement
supporting takeaway 2; nothing about implementation details that don't serve either takeaway,
even though there's plenty to say about them.

**Intro, written last:** now that the shape of the talk is known, the intro previews exactly
this arc — "static caching strategies fail under bursty load; here's an adaptive approach, and
here's why the overhead doesn't cancel out the benefit" — a preview that's accurate because it
was written after the talk actually existed, not guessed at beforehand.

**A real-world instance: hobby talks.** Early in the semester, before the stakes of a real
research presentation, each student gave a short talk on a hobby they knew well — chosen
precisely because hobbies are often genuinely technical (strategy in a favorite game, the
mechanics of a craft, an approach to training). There was no grade attached. Feedback was given
live, in the moment, in a deliberately friendly environment — real comments on what was working
and what could improve, not a score. The low stakes made it a safe place to practice the
takeaways-first construction method and the delivery discipline from
[Presentations That Work]({{ '/human-skills/presentations-that-work/' | relative_url }}) before applying both to work
that actually mattered.

## Common Pitfalls

- Writing the introduction first, which locks in a structure before you actually know what the
  talk's key points are.
- A middle slide that's interesting but doesn't connect to any of the chosen takeaways — cut
  it, even if it was hard to produce.
- Slide text that repeats what's being said out loud, rather than complementing it with data,
  diagrams, or quotes.
- Running over the time limit rather than cutting content in advance to fit it.

## Rubric / Checklist

- [ ] Key takeaways (3–5) were determined before the rest of the talk was built
- [ ] The takeaways include one that synthesizes the others
- [ ] Every middle slide connects to a specific takeaway
- [ ] Slides carry data, diagrams, and quotes — not a transcript of the spoken words
- [ ] The introduction was written last, after the middle and takeaways were set
- [ ] Title is compelling, not generic
- [ ] Scope is realistic — the talk advertises the paper, it doesn't replace it
- [ ] Practiced against the actual time limit; ending early is fine, running long is not
