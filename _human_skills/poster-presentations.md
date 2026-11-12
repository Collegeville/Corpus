---
title: Poster Presentations
category: Presenting
tags: [presenting, posters, visual-communication]
related_human_skill: [presentations-that-work, slides-that-work]
related_agent_skill: deck-and-delivery-review
slug: poster-presentations
summary: A poster has no narrator — every panel has to carry its own argument, in two formats, for a visitor who may only stop for thirty seconds.
---

## Definition

A poster presentation condenses a research project onto a single static page, built to work in
two different settings at once: a physical poster a visitor walks past and reads unassisted, and
an on-screen version for virtual or hybrid sessions. The defining constraint is the one a slide
deck never has — there's often no presenter standing there to fill in gaps. A visitor may read
the whole thing in silence, or stop for thirty seconds and move on. Every panel has to make its
point on its own, in the order a reader's eye naturally travels.

This is a close companion to
[Presentations That Work]({{ '/human-skills/presentations-that-work/' | relative_url }}) and
[Slides That Work]({{ '/human-skills/slides-that-work/' | relative_url }}): the same discipline
about scope, a real through-line, and data over adjectives applies, but a poster trades delivery
and timing for layout and self-sufficiency.

## Learning Outcome

After using this technique, you should be able to lay out a poster — in both a print and an
on-screen format — where each panel answers one specific question and the whole thing argues a
single thesis without a presenter narrating it, rather than a poster that's just a shrunken
slide deck or a wall of paragraphs.

## Core Structure

A poster is built from a fixed sequence of panels, each answering one question. Work through
them in this order:

1. **Takeaway.** The one sentence a visitor should be able to repeat to a friend afterward —
   your main finding or claim, stated plainly, not hedged.
2. **Motivation.** Two or three plain sentences on why a visitor should care. What problem or
   opportunity makes this topic matter right now?
3. **Thesis / Scope.** Your thesis in one sentence, paired with the real technical content you
   studied — the specific algorithm, dataset, or architecture, named directly.
4. **Foundations.** Only the two or three concepts a reader outside your topic needs before the
   center panel makes sense. Resist the urge to teach everything you learned.
5. **Exploration.** What you built or tested, and what it showed — numbers, not adjectives. A
   headline result stated in one line, backed by a small chart, table, or screenshot.
6. **Central visual.** Your strongest single visual, with a caption that stands alone: what it
   shows, how you produced it, and what the visitor should conclude — written so the caption
   works even if the visitor skips every other panel.
7. **A panel of your own.** Rename this one for what the project actually needs — a limits panel,
   a comparison, a deep dive, a method detail. Don't force content into a slot it doesn't fit.
8. **Futures.** One or two predictions, each backed by evidence — a trend, a known limit, a
   model, or an expert opinion — not a bare guess at what's next.
9. **Go Deeper / Sources / AI Acknowledgment.** A QR code or link to the full paper, video, or
   code; three to five key references; and a plain statement of which AI tools you used and for
   what. You own every claim on the poster regardless.

Build the poster once, then produce **both formats** from it — a print layout and a 16:9
on-screen layout — rather than stretching one to stand in for the other. The content and panel
order stay identical; only the layout reflows to fit the medium and viewing distance.

## Worked Example

The CSCI 373 poster kit provides blank templates in both formats, plus a complete worked example
by a real student (Emily Hed, on the limits of SHAP model explanations) showing every panel
filled in:

- [Poster-format template]({{ '/assets/examples/poster-presentations/CSCI373-Poster-Template.pptx' | relative_url }})
  ([View PDF]({{ '/assets/examples/poster-presentations/CSCI373-Poster-Template.pdf' | relative_url }}))
- [On-screen-format template]({{ '/assets/examples/poster-presentations/CSCI373-OnScreen-Template.pptx' | relative_url }})
  ([View PDF]({{ '/assets/examples/poster-presentations/CSCI373-OnScreen-Template.pdf' | relative_url }}))
- [Worked example — poster format]({{ '/assets/examples/poster-presentations/Hed-SHAP-Poster.pptx' | relative_url }})
  ([View PDF]({{ '/assets/examples/poster-presentations/Hed-SHAP-Poster.pdf' | relative_url }}))
- [Worked example — on-screen format]({{ '/assets/examples/poster-presentations/Hed-SHAP-OnScreen.pptx' | relative_url }})
  ([View PDF]({{ '/assets/examples/poster-presentations/Hed-SHAP-OnScreen.pdf' | relative_url }}))
- [Download the complete kit as a zip]({{ '/assets/examples/poster-presentations/poster-presentations-kit.zip' | relative_url }})

The worked example follows the panel sequence exactly. **Takeaway:** "SHAP exposed a pattern my
earlier analysis missed, yet its math can still mislabel which features matter. Pair it with
other methods." **Motivation:** models now help decide loans, hiring, and medical care, and
regulation increasingly expects a reason behind automated decisions. **Thesis/Scope:** "SHAP is a
valuable explanation tool, but its Shapley-based attributions can diverge from logical
relevance" — scoped specifically to TreeSHAP on an XGBoost survival model trained on the Titanic
dataset. **Foundations:** a two-sentence explanation of Shapley values as credit-splitting in a
cooperative game — just enough to read the central visual, not a tutorial. **Central visual:** a
SHAP value plot with a caption that states the finding on its own ("class matters more for
women") without requiring the motivation panel to make sense of it. The "panel of your own" is
renamed **Limits**, citing specific failure modes from the literature rather than a vague
disclaimer. **Futures** predicts growth in explanation tooling, tied to named regulation (the EU
AI Act, GDPR) rather than an unsupported guess.

## Common Pitfalls

- **A panel that only makes sense with the presenter standing there to explain it** — defeats
  the format; a poster has to work in silence.
- **A central-visual caption that doesn't stand alone**, forcing a visitor to hunt through other
  panels to understand the one visual that's supposed to be the anchor.
- **Reusing one layout for both formats** instead of reflowing for the different aspect ratio
  and viewing distance — text sized for a screen six feet away is often unreadable printed, and
  vice versa.
- **A foundations panel that teaches everything you learned** instead of only what's needed to
  follow the center panel.
- **Adjectives instead of numbers** in the exploration panel — "significant improvement" instead
  of the actual measurement.
- **Skipping the sources or AI-acknowledgment panels**, or leaving them vague about which tools
  did what.

## Rubric / Checklist

- [ ] Takeaway panel states one plain, repeatable claim — not hedged, not a topic label
- [ ] Motivation panel gives a concrete reason to care, in two or three sentences
- [ ] Thesis/Scope names the actual technical content studied, not just the general topic
- [ ] Foundations panel covers only what's needed for the center panel — nothing more
- [ ] Exploration panel reports numbers, not adjectives
- [ ] Central visual's caption stands alone, with no other panel required to understand it
- [ ] The custom panel is renamed for what the project actually needs
- [ ] Futures panel's predictions are each backed by stated evidence
- [ ] Sources and AI-acknowledgment panels are filled in, not placeholders
- [ ] Both a print and an on-screen format exist, reflowed rather than stretched from one to
      the other
- [ ] A visitor with no presenter present could read the whole poster and get the argument
