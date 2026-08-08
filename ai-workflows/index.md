---
title: AI-Assisted Workflows
section: AI-Assisted Workflows
layout: page
---
<p>
Timely, tool-dependent workflows a human follows with an AI tool's help &mdash; the human
stays in the driver's seat throughout. Because these depend on the current state of
generative AI tools, they're expected to need periodic refreshing &mdash; that's the point of
splitting them out rather than mixing them into the timeless material.
</p>

<div class="card-grid">
{% assign ai_docs = site.ai_workflows | sort: "title" %}
{% for doc in ai_docs %}
  <a class="card" href="{{ doc.url | relative_url }}">
    <h3>{{ doc.title }}</h3>
    <p>{{ doc.summary }}</p>
  </a>
{% endfor %}
</div>

<p><em>This index fills in automatically as pages are added to <code>_ai_workflows/</code> &mdash; no manual list to maintain.</em></p>
