---
name: "position-paper-grill"
description: "Interview an author to elicit the content of a position paper — present state, desired future state, sub-goals, case study, and risks — then assemble it into the seven-part position paper structure. Use when the user wants help drafting, outlining, or being interviewed for a position paper or whitepaper."
---

Interview the author to draw out the *content* of a position paper, then assemble that content
into the standard structure. The author owns the ideas; this skill's job is elicitation and
structural completeness, not inventing the argument for them.

This pairs with the Corpus site's Position Papers page
(https://collegeville.github.io/Corpus/human-skills/position-papers/) — consult it for the
full seven-part structure and the four-part per-point pattern (status → recommendation →
discussion → risks/requirements) if you need the definitions.

## Interview flow

Follow this order. As in `grill-me`: ask one question at a time, never dump a list, offer a
recommended answer or example when it helps the author get unstuck, and keep drilling into an
unresolved branch before moving to the next.

**1. Overarching vision (anchor first).**
Elicit the throughline before anything else:
- What's the present state, as the author sees it? (Their own read on the current situation —
  the point isn't objectivity, it's making the author's perspective explicit so a disagreeing
  reader at least understands it.)
- What's the desired future state?
- Why does this matter now — what prompted this?

Do not move on until this is reasonably clear. Everything else hangs off it.

**2. Sub-goals / components.**
Ask directly: *do you already have a sense of the distinct sub-goals or components this breaks
into?*
- If yes: capture them as given. Don't second-guess a structure the author already has.
- If no: help discover them rather than forcing a count. Useful probes: "who are the different
  audiences or teams this affects, and does each need something different?" or "if you had to
  ship just one piece of this and stop, what would it be?" Stop probing once 3–6 workable
  components emerge — don't force decomposition past what's natural.

**3. Per-component drill-down.**
For each sub-goal, elicit the four-part pattern in order:
- Present status (for this component specifically)
- Recommendation
- Discussion (the case for why this specific change, anticipating the obvious objection)
- Risks and requirements (what has to be true, or go wrong, for this not to work)

Don't let the author skip risks — if they wave it off, ask directly: "if this doesn't go the way
you expect, what fails first?"

**4. Case study (evidence branch).**
Ask whether a comparable situation exists — a precedent, a prior attempt, another team or
project that did something similar — that would give a skeptical reader confidence this isn't
untested. This is optional in the final document but worth asking about explicitly rather than
leaving it to chance. If nothing comes to mind readily, don't force it; note it as absent.

**5. Executive summary — do not elicit this separately.**
Once the full case is captured, synthesize the executive summary yourself as a compressed
restatement of the recommendations gathered in step 3. Show it to the author to confirm it
matches their intent, but don't ask them to draft it from scratch — that's redundant with work
already done.

## Assembly

Once the interview is complete, assemble the seven-part structure:

1. Abstract (half-page: background, motivation, preview)
2. Executive summary (synthesized per step 5 above)
3. Table of contents (only if the draft runs past five pages)
4. Introduction (status quo, goal, approach — drawn from step 1)
5. Case study, if one emerged in step 4
6. Full presentation — each component from step 2/3, in the four-part pattern
7. Summary and conclusion

## Completion check

Before calling this done, confirm against the site's checklist:
- [ ] Executive summary actually matches the recommendations in the full presentation
- [ ] Every component has all four parts — status, recommendation, discussion, risks
- [ ] Risks are genuinely present, not a token line
- [ ] Case study included if one exists, or explicitly noted as not applicable

Give the author a concise summary of what was captured before producing the assembled document,
the same way `grill-me` closes out an interview.
