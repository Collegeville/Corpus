---
title: AI-Assisted Abstract Drafting
category: Writing
tags: [abstracts, ai-workflow, drafting]
summary: A six-step workflow for generating a first-draft abstract with an AI tool, anchored to Koopman's five-part structure.
related_human_skill: titles-and-abstracts-that-work
source: https://maherou.github.io/Teaching/files/CS373/BetterAbstracts/
slug: ai-assisted-abstract-drafting
---

*As of this writing (2026). AI tool behavior changes quickly — revisit this page periodically
rather than treating it as permanent guidance.*

## Definition

Writing a good abstract is hard even when you know the structure to aim for. This workflow uses
an AI tool to generate a fast first draft, anchored explicitly to the same five-part structure
covered in [Titles and Abstracts That Work]({{ '/human-skills/titles-and-abstracts-that-work/' | relative_url }}) —
motivation, problem statement, approach, results, conclusions — so the AI's output is judged
against a real standard, not accepted as-is.

## Learning Outcome

After using this workflow, you should be able to produce a solid first-draft abstract in
minutes rather than hours, while still doing the real work of revising it against a known
structure rather than treating the AI's draft as finished.

## Core Structure

Six steps:

1. **Upload the paper.** Provide the full paper to an AI tool (ChatGPT, Gemini, Claude, or
   similar).
2. **Provide the abstract-writing criteria.** Paste in a description of what makes a good
   abstract — Koopman's five-part structure works well here — so the model has an explicit
   standard to follow rather than guessing at abstract conventions generically.
3. **Ask for a draft abstract using that structure.** The goal is a draft to improve, not a
   finished product.
4. **Revise the draft.** Treat it as a starting point — adjust wording, tighten claims, and make
   sure results are stated in numbers, not vague qualifiers.
5. **Insert it into your document.** For a LaTeX paper, this means placing the revised text
   inside `\begin{abstract} ... \end{abstract}`.
6. **(Optional) Generate title options.** Ask the tool for several accurate, pithy title
   candidates for the paper and presentation.

## Worked Example

Applied to a paper on adaptive caching: after uploading the paper and providing the five-part
structure, a first AI draft might state results vaguely ("the approach performs well under
various workloads"). Step 4 is where the real work happens — revising that sentence to state the
actual numbers ("reduces p99 latency by 18% under bursty workloads"), matching the standard set
in Titles and Abstracts That Work rather than accepting the AI's vaguer phrasing.

## Common Pitfalls

- Skipping step 2 — asking for "a good abstract" without providing explicit criteria produces a
  generic result with no structure to check it against.
- Treating the AI's draft as final rather than as something to revise — step 4 isn't optional.
- Letting vague results language from the AI draft survive into the final version, when the
  underlying skill explicitly calls for numbers over qualifiers.
- Using this workflow as a substitute for understanding your own results, rather than as a
  drafting accelerant.

## Checklist

- [ ] Full paper provided to the AI tool
- [ ] Explicit abstract-structure criteria provided, not just a generic request
- [ ] Draft reviewed against all five Koopman parts, not just accepted
- [ ] Results are stated in numbers after revision, not left as vague qualifiers
- [ ] Final version inserted correctly into the document
