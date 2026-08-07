---
title: Captions That Work
category: Writing
tags: [figures, captions, technical-writing]
summary: Write multi-sentence, stand-alone captions that let a figure be understood without the reader needing the main text.
source: https://maherou.github.io/Teaching/files/CS373/CaptionsThatWork/
slug: captions-that-work
---

## Definition

A narrative caption is a multi-sentence, stand-alone caption that turns a figure into a small,
self-contained story: what's being shown, how it was produced, and what it means. This is
distinct from the short, purely labeling caption most people default to ("Figure 1. Growth rates
of Strain A and Strain B at different temperatures"), which tells a reader *what* they're
looking at but not *why it matters*.

This isn't an idiosyncratic preference — it's grounded in how style guides and working
scientists actually write. Style guides call it the "extended" or "narrative" caption. Edward
Tufte argues for figures with rich, integrated explanatory text rather than bare labels. The CSE
Manual's guidance for scientific writing is explicit: a figure legend should be complete enough
that a reader can understand the figure without reading the surrounding text. Joshua Schimel
frames it as "telling the story of the figure." *Nature* and *Science* both expect multi-sentence
legends that explain what's shown, how it was generated, and what it means.

## Learning Outcome

After using this technique, you should be able to write a caption that stands on its own —
giving context, describing the method or metric behind the data, and interpreting the result —
and to scale that caption's length and tone appropriately for the venue you're writing for.

## Core Structure

A strong stand-alone caption does four things, in this order:

1. **Start with context** — what is being shown, and why does it matter?
2. **Describe the method or metric** — how was the data obtained or calculated?
3. **Interpret the result** — what should the reader take away from it?
4. **Reference the main text only if needed** — for readers who want more depth, not as a
   crutch for the caption itself.

This matters because of how people actually read technical papers: they skim by jumping from
figure to figure before committing to the full text. A caption that only labels forces the
reader back into the prose to understand what they're looking at. A narrative caption lets the
figure carry its own weight — which also makes it easier to reuse in talks, reports, or teaching
material later, independent of the paper it came from.

**Scaling by audience.** The same figure gets a differently-shaped caption depending on where
it's going:

| Audience | Focus | Length | Tone |
|---|---|---|---|
| Journal article | Accuracy, replicability | Medium (~4–6 sentences) | Formal, technical |
| Technical report | Completeness, documentation | Long (~5–10 sentences) | Formal, readable |
| Grant proposal | Significance, impact | Medium (~3–5 sentences) | Narrative, persuasive |
| Conference presentation | Fast comprehension | Short (~2–3 sentences) | Crisp, conversational |

## Worked Example

Same figure — bacterial growth rates for two strains across a temperature range — written four
different ways.

**Short (labeling) caption**, for comparison:
> Figure 1. Growth rates of Strain A and Strain B at different temperatures.

**Journal article** (medium, formal/technical):
> Figure 1. Growth rates of Strain A and Strain B across temperatures from 10°C to 40°C, measured
> in triplicate under controlled laboratory conditions. Strain A peaks near 30°C and declines
> sharply above it, indicating a narrow thermal tolerance window; Strain B holds a stable growth
> rate across the full range, consistent with broad thermal adaptation. Error bars represent
> standard deviation. These results may inform strain selection for thermally variable industrial
> applications.

**Grant proposal** (medium, narrative/persuasive):
> Figure 1. Strain A thrives at 30°C but declines sharply thereafter, while Strain B maintains
> steady growth across the full temperature range tested. This robustness suggests Strain B could
> support reliable bio-production in environments with variable temperature.

**Conference presentation** (short, crisp):
> Figure 1. Strain A grows best at 30°C but drops off sharply at higher temperatures. Strain B
> grows steadily across a wide range — the kind of thermal tolerance that matters for
> variable-temperature bio-industrial use.

Notice what's constant across all four: the core claim (Strain B is more thermally resilient) and
the interpretation (why that matters). What changes is length and how directly the significance
is stated. The short label version, by contrast, requires the reader to go find that story
somewhere else in the paper.

## Common Pitfalls

- Restating what's already obvious from the figure or the main text — a caption should add
  context and interpretation, not just repeat the axis labels in words.
- Describing the figure but never interpreting it — "the line goes up" is not the same as "the
  line going up means X."
- Using the same caption style regardless of venue — a conference-slide caption dropped into a
  journal submission reads as thin; a journal-length caption on a slide will lose the room.
- Leaving the caption unconnected to the actual research question the figure is meant to
  support.

## Rubric / Checklist

A good figure legend:
- [ ] Gives sufficient background without being redundant with the main text
- [ ] Focuses the reader's attention on the important pattern or anomaly, not just "what's
      plotted"
- [ ] States or clearly implies an interpretation, not just a description
- [ ] Relates explicitly back to the research question or hypothesis
- [ ] Is scaled in length and tone to its actual venue (see the audience table above)
