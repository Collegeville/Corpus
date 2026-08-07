---
title: Generative AI Tools
category: Research
tags: [ai-workflow, prompting, tooling]
summary: Three practical patterns for using AI tools in research work — structured prompting, bootstrapping an unfamiliar API, and the "how, how, how" question.
related_human_skill: level-of-expertise-dialogue
source: https://maherou.github.io/Teaching/files/CS373/GenerativeAITools/2025-08-Heroux-GenerativeAITools.pdf
slug: generative-ai-tools
---

*As of this writing (2026), distilled from a 2025 presentation. AI tool capabilities change
quickly — revisit this page periodically rather than treating it as permanent guidance.*

## Definition

Generative AI tools show up in research work in three broad ways: handling tedious writing
tasks (citation formatting, summarizing, translating a result for a different audience),
upscaling technical skills you don't have yet (bootstrapping an unfamiliar API or algorithm),
and changing the shape of the research process itself (custom-tuned assistants, structured
prompting). This page collects the practical patterns from those first two categories that hold
up independent of which specific tool you're using.

## Learning Outcome

After using these patterns, you should be able to structure a prompt so an AI tool's response is
actually useful for your specific situation, and use AI tools to bootstrap unfamiliar technical
territory faster than starting from nothing.

## Core Structure

**Persona, Context, Task — a structure for prompts that need to produce something specific.**
Rather than asking a generic question, specify:
- **Persona**: who should the AI act as, or who is it helping? ("A student with this
  coursework and these interests...")
- **Context**: what constraints or reference material apply? ("...pursuing a research topic that
  must satisfy these course requirements...")
- **Task**: what specific output do you need? ("...suggest three research topics, with
  justification and the specific algorithms each would require.")

A vague prompt gets a vague answer; specifying who, under what constraints, and toward what
output gets something you can actually use.

**Bootstrapping an unfamiliar API or technique, in four steps:**
1. Ask for advice on the general approach before asking for code — "what's a good way to do X?"
   surfaces the landscape before you commit to one path.
2. Ask for a working example based on that advice.
3. Ask about anything in the generated example you don't understand (a specific API concept, an
   unfamiliar function) before using it.
4. Experiment — modify the example yourself and see what breaks, rather than treating the first
   working version as final.

**The "how, how, how" question, for getting value out of a new AI tool quickly.** Rather than
exploring a tool's features abstractly, ask it directly: "I do \<your actual job or task\>. How
can you help me do it better?" This surfaces concrete, situated suggestions faster than browsing
generic capability lists.

## Worked Example

Bootstrapping unfamiliar work with a GitHub API: step 1 asks "what's a good way to extract
metadata from a GitHub repo?" rather than jumping straight to code. Step 2 asks for a script that
extracts commit, pull-request, and release counts for a specific repository. Step 3 asks how to
generate the personal access token the script needs, since that's an unfamiliar prerequisite.
Step 4 modifies the script to also list contributors and their commit counts — testing
understanding by extending the example rather than just running it as given. The result: a
working, understood script built in a fraction of the time cold research would have taken.

## Common Pitfalls

- Asking a vague question and getting a vague, generically-applicable answer — persona, context,
  and task specificity matters.
- Running generated code without asking about the parts you don't understand, so nothing is
  actually learned in the process.
- Treating a first working example as finished rather than as something to test and extend.
- Assuming AI-assisted drafting or scripting removes the need to demonstrate real understanding
  — the check on this isn't a stricter AI policy, it's being able to hold your own in a
  [Level of Expertise Dialogue]({{ '/human-skills/level-of-expertise-dialogue/' | relative_url }}) afterward.

## Checklist

- [ ] Prompts specify persona, context, and task rather than asking generically
- [ ] Unfamiliar territory is bootstrapped in stages (advice → example → clarification →
      experimentation), not accepted whole from a single response
- [ ] Anything unfamiliar in a generated result is asked about before being used
- [ ] A new tool's value is tested against your actual task, not just its feature list
- [ ] You can still explain and defend the resulting work without the AI's help
