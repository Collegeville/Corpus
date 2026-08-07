---
title: Using LaTeX
category: Writing
tags: [latex, technical-writing, typesetting]
summary: "LaTeX is a programming language whose output is a formatted document instead of an executable — a short annotated sample proves the point."
source: https://collegeville.github.io/Scribe/UsingLatex/
slug: using-latex
---

## Definition

LaTeX is the field-standard typesetting system for technical and academic publishing — many
journals and conferences accept it as the only source format. The fastest way to actually
understand it, especially for someone with programming experience, is a single reframe: **LaTeX
is a programming language whose compiler produces a formatted document instead of an
executable.** A `.tex` file has structure, syntax, and includes, in the same way source code
does; running it through a LaTeX toolchain "compiles" it to a PDF the way a compiler produces a
binary.

## Learning Outcome

After working through this, you should be able to read an unfamiliar `.tex` file and recognize
its structure the same way you'd recognize the structure of an unfamiliar program — imports,
declarations, named references, and a build step — rather than seeing it as an opaque wall of
backslashes.

## Core Structure

The mapping to familiar programming concepts:

| LaTeX construct | Programming analogy |
|---|---|
| `\documentclass{...}` | Declares the "type" of the whole document (like a base class or template) |
| `\usepackage{...}` | Import / include — pulls in extra functionality (tables, figures, custom boxes) |
| `\begin{...} ... \end{...}` | A block or scope — environments like `abstract`, `figure`, `table`, `itemize` |
| `\label{...}` / `\ref{...}` | A named reference / pointer — label something once, refer to it anywhere, and let the compiler resolve the actual number |
| `\cite{...}` + a `.bib` file | A dependency on an external database — the bibliography is a separate data file, referenced by key, resolved at compile time |
| `%` | Comment |

The compile model itself is also a build pipeline worth recognizing: your `.tex` source and a
separate `.bib` bibliography database are processed together (traditionally via `pdflatex` and
`bibtex`, often run automatically by an editor or online tool) to produce a single output PDF.

## Worked Example

A minimal but complete sample document demonstrates the whole structure in one file. Full
source, rendered output, and bibliography database are archived here:

- [Sample `.tex` source]({{ '/assets/examples/latex/sample.tex' | relative_url }})
- [Sample `.bib` bibliography database]({{ '/assets/examples/latex/sample.bib' | relative_url }})
- [Compiled output PDF]({{ '/assets/examples/latex/sample.pdf' | relative_url }})
- [Download the complete example as a zip]({{ '/assets/examples/latex/sample.zip' | relative_url }})

The zip is fully self-contained and ready to build: source, bibliography, the `IEEEtran`
class and style files, and the figure it references. Unzip it and run your usual
LaTeX/BibTeX toolchain to reproduce the PDF above exactly.

The document declares its type and imports, in the first few lines:

```latex
\documentclass{IEEEtran}
\usepackage{wrapfig}
\usepackage{graphicx}
\usepackage[export]{adjustbox}
\usepackage{mdframed}

\title{Sample \LaTeX\ Document}
\author{Mike Heroux}
```

It then works through the standard sections of a technical report — abstract, introduction,
body, conclusion — each as a `\section{...}` block. Along the way it demonstrates the constructs
that come up in almost any technical document: a numbered equation with a `\label` that's
referred back to later by `\ref`, a table, a figure wrapped in text via `wrapfigure`, and both
numbered (`enumerate`) and bulleted (`itemize`) lists, including a note that lists can nest.

Citations tie the document to its bibliography database. The sample cites two sources:

```latex
The former topic is covered very well in~\cite{High93} and
the latter in~\cite{Lamp86}.
...
\bibliography{sample}
```

Each citation key resolves to a full entry in `sample.bib` — a plain-text database where each
entry has a type, a key, and a set of fields:

```bibtex
@book{High93,
title = "{Handbook of Writing for the Mathematical Sciences}",
author = "Nicholas J. Higham",
publisher = "SIAM",
year = 1993}

@book{Lamp86,
title = "{LaTeX User's Guide and Reference Manual}",
author = "Leslie Lamport",
publisher = "Addison-Wesley",
year = 1986}
```

At compile time, LaTeX and BibTeX match every `\cite{key}` in the document against an entry with
that key in the `.bib` file, and generate a formatted bibliography automatically — you never
hand-format a reference list.

## Common Pitfalls

- Trying to manually control exactly where a figure or table lands on the page. LaTeX places
  floats algorithmically based on the surrounding content; you can nudge it, but you don't have
  direct control the way you would dragging an image in a word processor.
- Citing a key with `\cite{...}` that has no matching entry in the `.bib` file — this produces
  an unresolved reference rather than a build error you'd immediately notice.
- Treating `\label` and `\ref` as manual bookkeeping (writing the number yourself) instead of
  letting the compiler resolve them — which is the entire point of using them.
- Skipping the "read an existing document as a template" strategy. The source file above is
  meant to be copied from and modified, not written from scratch each time.

## Rubric / Checklist

- [ ] Document has a `\documentclass` and only the `\usepackage` imports it actually uses
- [ ] Every figure and table has a caption and a `\label` that's referenced at least once via
      `\ref`
- [ ] Every `\cite{key}` has a matching entry in the `.bib` file
- [ ] A bibliography style is declared and `\bibliography{...}` is included
- [ ] When in doubt about how to express a construct, an existing document (like the sample
      above) is used as a template rather than guessing from scratch
