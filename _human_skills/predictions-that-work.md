---
title: Predictions That Work
category: Research
tags: [prediction, forecasting, trends]
summary: Ground any predictive claim in a model of the entities and relationships at play, and back it with real evidence rather than gut feel.
source: https://collegeville.github.io/Scribe/PredictionsThatWork/
slug: predictions-that-work
---

## Definition

Any serious effort in technology development requires regularly assessing where the
opportunities lie, which uses matter, and which trends are shifting. As Yogi Berra put it, "it's
tough to make predictions, especially about the future" — and predictions grounded in nothing
but intuition tend to be wrong in the same ways over and over. The fix isn't to avoid predicting;
it's to predict from an explicit model and real evidence, not just extrapolated hope. As
economist Herbert Stein's law puts it: if a trend cannot continue, it will stop — which is a
useful check against predictions that quietly assume infinite continuation.

## Learning Outcome

After using this technique, you should be able to back a predictive claim with at least one of
five specific evidence types, rather than presenting a guess as though it were an analysis — and
you should be able to say explicitly what model of entities and relationships the prediction
rests on.

## Core Structure

**The challenge.** Prediction is genuinely hard, especially for someone new to a field. And good
technology decisions aren't purely technical — human behavior and social systems are major
factors, as is being the right person, in the right place, with the right resources, at the
right time.

**The approach.** Build a model — identify the entities and the relationships between them that
actually drive the outcome you're predicting. A model helps you separate what's essential from
what's secondary or irrelevant, the same discipline used in [Effective Mental
Models]({{ '/human-skills/effective-mental-models/' | relative_url }}).

**Five foundations for a grounded prediction.** Back any predictive claim with as many of these
as apply:

1. **Observed data** — from a similar setting.
2. **Observed trends** — data observed over time, not a single snapshot.
3. **Known constraints** — hard bounds the trend cannot cross (a global minimum or maximum).
4. **Mathematical models** — quantitative relationships that let you extrapolate with some
   rigor.
5. **Expert opinion** — informed judgment from people close to the field.

## Worked Example

How do these five foundations show up in something as familiar as weather forecasting?

- **Observed data**: current radar and satellite readings — what's actually happening right now.
- **Observed trends**: how a pressure system has moved and evolved over the last 24–48 hours.
- **Known constraints**: physical bounds a forecast can't violate — temperature can't swing 40
  degrees in an hour; a hurricane can't sustain itself over cold water indefinitely.
- **Mathematical models**: numerical weather prediction models that simulate atmospheric physics
  forward in time.
- **Expert opinion**: a meteorologist adjusting the raw model output based on experience with
  how local terrain or seasonal patterns tend to diverge from the model's assumptions.

A forecast that used only one of these — say, pure trend extrapolation with no constraint-check —
is exactly the kind of prediction Stein's Law warns about: a trend presented as though it
continues forever, when in reality something will make it stop.

## Common Pitfalls

- Extrapolating a trend without checking it against known constraints — the trend that "cannot
  continue" eventually won't.
- Treating a prediction as purely technical while ignoring the human and social factors that
  often determine what actually gets adopted.
- Presenting a single data point as though it were an observed trend.
- Skipping the modeling step entirely and jumping straight to a conclusion, so there's no way
  to say *why* the prediction should be trusted.

## Rubric / Checklist

- [ ] The prediction names the model — the entities and relationships it's based on
- [ ] At least one of the five evidence types (observed data, observed trends, known
      constraints, mathematical models, expert opinion) is explicitly cited
- [ ] The prediction has been checked against known constraints, not just extrapolated
- [ ] Non-technical factors (human behavior, timing, resource availability) are acknowledged
      where relevant
- [ ] The claim is stated with an appropriate degree of confidence, not overstated as certainty
