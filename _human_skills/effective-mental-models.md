---
title: Effective Mental Models
category: Research
tags: [mental-models, understanding, diagrams]
summary: Build an explicit model of entities and relationships to understand any system, and know the three phases you pass through while building one.
source: https://maherou.github.io/Teaching/files/CS373/MentalModels/
slug: effective-mental-models
---

## Definition

A mental model is a collection of *entities* and the *relationships* between those entities. It's
how we understand systems, communities, or any environment with dynamic behavior. A good mental
model is typically accurate but not too precise — it exposes the characteristics that actually
drive the dynamics of the environment, and deliberately leaves out the ones that don't.

In technical fields we constantly build mental models implicitly, without ever naming them.
Making a model explicit — by drawing a diagram or otherwise externalizing it — lets you name,
question, and refine the entities and relationships in it, rather than leaving them as a vague
intuition you can't inspect or share.

## Learning Outcome

After using this technique, you should be able to produce an explicit diagram of any topic
you're learning, showing its key entities and relationships, and recognize which of three phases
you're in as you build understanding of something genuinely new.

## Core Structure

**Why an explicit model matters.** A documented mental model lets you communicate your thinking
to others, refine it through their feedback, and use it as a foundation for decisions and
predictions about the future — the same discipline used in
[Predictions That Work]({{ '/human-skills/predictions-that-work/' | relative_url }}). An undocumented model, by
contrast, can't be checked, shared, or improved by anyone but you.

**The three phases of building a mental model.** You don't arrive at a good mental model in one
pass — you move through three distinct phases as your understanding deepens:

1. **Sketching a preliminary model.** At the start, you don't know what you don't know. This
   phase means dedicating real blocks of time to reading, watching, and listening broadly
   enough to bootstrap a first rough model, before you're even able to name what's missing from
   it.
2. **Building a robust model.** Once you have a preliminary model, you have names for the
   concepts you don't yet understand — which means you can now go learn them specifically,
   rather than searching blindly.
3. **Establishing expertise.** At this point you know enough to speak with authority on a
   narrower slice of the topic, defend your model under questioning, and answer follow-ups
   without notes.

A model built in Phase 1 should look rough and incomplete — that's not a failure, it's what a
Phase 1 model is supposed to look like. Trying to make a Phase 1 model precise wastes the time
that phase is meant to spend on breadth instead.

## Worked Example

A student's topic is graph neural networks. In Phase 1, a rough sketch might just connect
"graphs," "neural networks," and "node embeddings" with an arrow, gestured at from an
introductory video — accurate in spirit, thin on detail. By Phase 2, the same diagram has grown
real structure: nodes, edges, message-passing steps between them, an embedding layer, and a
downstream task, each labeled precisely enough to explain to someone else. By Phase 3, the model
has narrowed rather than kept growing — most of it is now focused on one specific message-passing
variant the student can defend in detail, with the broader context compressed into a single
box labeled "prior approaches" rather than spelled out.

## Common Pitfalls

- Trying to make a Phase 1 model precise and complete — precision belongs to later phases;
  Phase 1's job is breadth, not accuracy.
- Leaving a mental model entirely implicit, so it can never be checked, shared, or corrected.
- A model so precise it has no room left to expose the dynamics that actually matter — an
  overly literal diagram of every detail is often less useful than a simpler one that highlights
  the right relationships.
- Never revisiting the model as understanding deepens — treating the Phase 1 sketch as final
  rather than as a draft to be replaced.

## Rubric / Checklist

- [ ] The model names specific entities, not vague categories
- [ ] The model shows relationships between entities, not just a list of things
- [ ] The model is externalized (a diagram or written description), not left implicit
- [ ] The level of precision matches the current phase — rough and broad early, narrow and
      exact later
- [ ] You can explain the model to someone else and defend it under questions
