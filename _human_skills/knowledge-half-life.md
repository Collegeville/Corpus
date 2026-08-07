---
title: Knowledge Half-Life
category: Research
tags: [continuing-education, self-teaching, judgment]
summary: A short set of questions for judging whether something you're learning right now will still matter in five years, or be stale in six months.
slug: knowledge-half-life
---

*This page is the practical, applied companion to the [Knowledge Half-Life]({{ '/about-corpus/knowledge-half-life/' | relative_url }})
philosophy in About Corpus, which explains why the whole site is split into Human Skills and AI
Skills in the first place. This page is the reusable technique version — how to size up any
specific thing you're learning, not just why the split exists.*

## Definition

Not everything you learn ages the same way. Some knowledge is durable — the underlying
principles barely change even as the tools around them do. Other knowledge is closer to a
snapshot of a specific tool's current interface, and will need replacing within months. Knowing
which kind of knowledge you're looking at, before you invest hours in it, changes how you learn
it and how much you should expect to rely on it later.

## Learning Outcome

After using this technique, you should be able to look at something you're about to spend time
learning and make a reasonable prediction about how long it will stay useful — and adjust how
deeply you invest accordingly.

## Core Structure

Three questions to ask about anything you're learning:

1. **Is this a fundamental concept, or an interface?** A fundamental concept (how a hash table
   achieves average O(1) lookup) tends to outlast any particular tool. An interface (the exact
   menu structure of a specific piece of software) is tied to whatever's currently shipping.
2. **How fast is this domain actually changing?** Some fields move in decades, others in months.
   The same question — "how do I structure a technical argument" — has a very different half-life
   than "which prompt pattern works best with the current generation of a specific AI model."
3. **Who's still teaching this in ten years?** If a concept would still show up in a course or a
   textbook a decade from now, it's durable. If it would only make sense as a historical
   footnote, it's timely — useful now, but you shouldn't build your long-term understanding
   on top of it.

## Worked Example

Learning "how relational databases use indexes to speed up queries" versus learning "the current
UI for creating an index in a specific database product's admin console." The first is a
fundamental concept — the underlying tradeoff (faster reads, slower writes, extra storage) will
still be true and still be taught in ten years, regardless of which database you use next. The
second is an interface — genuinely useful today, but it'll need to be relearned the next time
that product redesigns its console, or the next time you switch products entirely. Both are worth
learning, but they deserve different levels of investment: the concept is worth understanding
deeply and remembering; the interface is worth knowing well enough to use right now, without
expecting it to still be accurate next year.

## Common Pitfalls

- Treating every skill as equally durable, so time gets spent memorizing interface details that
  will be obsolete before they'd ever be needed again.
- Dismissing something as "just an interface" when it's actually built on a durable concept
  worth extracting and keeping — the goal is to separate the two, not throw out anything
  tool-specific.
- Never revisiting the assessment — a domain's rate of change isn't fixed forever; something
  that was fast-changing can stabilize, and vice versa.

## Rubric / Checklist

- [ ] Identified whether this is closer to a fundamental concept or an interface
- [ ] Made an honest estimate of how fast this specific domain is changing
- [ ] Asked whether this would still be taught in ten years
- [ ] Adjusted depth of investment to match: durable knowledge gets real study time; timely
      knowledge gets "know it well enough for now"
- [ ] Extracted any durable principle hiding inside an otherwise timely, tool-specific skill
