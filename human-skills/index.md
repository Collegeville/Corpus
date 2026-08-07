---
title: Human Skills
section: Human Skills
layout: page
---
<p>
Timeless techniques for research, writing, presenting, and discussion. Each
follows the same template: Definition, Learning Outcome, Core Structure,
Worked Example, Common Pitfalls, and a Rubric or Checklist &mdash; so a skill
can be scanned quickly or read in full.
</p>

<div class="card-grid">
{% assign human_docs = site.human_skills | sort: "title" %}
{% for doc in human_docs %}
  <a class="card" href="{{ doc.url | relative_url }}">
    <h3>{{ doc.title }}</h3>
    <p>{{ doc.summary }}</p>
  </a>
{% endfor %}
</div>

<p><em>This index fills in automatically as pages are added to <code>_human_skills/</code> &mdash; no manual list to maintain.</em></p>
