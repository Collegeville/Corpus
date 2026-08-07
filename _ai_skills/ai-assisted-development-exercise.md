---
title: AI-Assisted Development Exercise
category: Research
tags: [ai-coding, tooling, benchmarking]
summary: A current landscape of AI coding assistants, run through the solitaire-simulator benchmark before you need one for real work.
related_human_skill: benchmarking-a-new-tool
source: https://maherou.github.io/Teaching/files/CS373/AiAssistedDevelopment/
slug: ai-assisted-development-exercise
---

*As of this writing (2026). This tool landscape changes fast — treat the table below as a
snapshot, not a current recommendation, and revisit it periodically.*

## Definition

This is the applied, current-tools version of
[Benchmarking a New Tool]({{ '/human-skills/benchmarking-a-new-tool/' | relative_url }}): pick an AI coding assistant,
use it to build a solitaire simulator, and produce an evidence-based reflection on the
experience — before you have to rely on an AI coding tool for something that actually matters,
like a real research demo.

## Learning Outcome

After completing this exercise, you should have hands-on experience with at least one current AI
coding assistant on a low-stakes, checkable task, and a documented, specific sense of what it's
good and bad at — rather than a vague general impression of "AI coding tools."

## Core Structure

**The benchmark tool landscape, as of 2026** (each entry: what it's good for in this context):

| Tool | IDE Compatibility | Why It's Good Here |
|---|---|---|
| GitHub Copilot | VS Code, JetBrains, Neovim, Visual Studio | Industry-standard; strong completions, refactoring, and tests while keeping the student responsible for correctness |
| Claude Code | VS Code (via extension), web | Strong at reasoning about game logic and state transitions; explanatory, conversational, promotes actual learning |
| Replit | Browser-based IDE | Very low setup friction; good for rapid prototyping and sharing a playable version |
| Amazon Q Developer | VS Code, JetBrains, AWS Cloud9 | Exposure to enterprise-style AI assistance and secure-coding hints |
| Zed | Zed Editor (macOS, Linux) | Good for tooling- and performance-focused students; modern editor design with emerging AI features |
| Tabnine | VS Code, JetBrains, Eclipse, others | Solid autocomplete with a privacy focus; less conversational |
| AntiGravity | Experimental standalone IDE | Useful for discussing intent-driven programming paradigms; not mature enough for full projects yet |
| OpenAI Codex | API-based, no IDE | Less suited as a primary learning tool here; obscures the human-in-the-loop workflow this exercise is meant to build |

**The exercise itself:**
1. Build a solitaire simulator using one or more of the tools above.
2. Play at least 1000 simulated games and compute the win rate (wins ÷ games played).
3. Write a short report (roughly two pages) covering: which tool(s) you used, your experience
   with them (both positive and negative, specifically), and your winning percentage with the
   details of how you computed it.

Working alone or in a group is fine, but in a group, every person needs their own code, results,
and report — the point is individual hands-on experience with the tool, not a shared output.

## Worked Example

A student picks Claude Code for its conversational, explanatory style. Early on, the tool
correctly implements the core deal-and-draw logic but needs a follow-up question to get the
three-pass-through-the-deck rule right — a concrete, specific data point for the report, not just
"it mostly worked." After 1000 simulated games, the win rate comes out in a plausible range,
which is itself a useful sanity check: an implausible result (near 0% or near 100%) would be a
signal that either the game logic or the tool's implementation of it has a bug, caught cheaply
because the benchmark's checkable.

## Common Pitfalls

- Running too few trials to get a stable estimate — a win rate from 20 games is much noisier
  than one from 1000.
- Reporting only whether the tool "worked," without the specific detail (what needed a
  follow-up, what it got right immediately) that actually builds calibrated judgment.
- Treating an implausible result as acceptable rather than as a signal to debug the
  implementation.
- Skipping ahead to using an AI tool on the real project without ever having exercised it on
  something checkable first.

## Checklist

- [ ] At least one current AI coding tool used hands-on
- [ ] 1000+ simulated games run to produce a stable win-rate estimate
- [ ] Report documents specific positive and negative experiences, not just a verdict
- [ ] Result checked for plausibility, not just reported
- [ ] If working in a group, each person has their own code, results, and report
