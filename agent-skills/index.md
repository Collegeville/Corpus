---
title: Agent Skills
section: Agent Skills
layout: page
---
<p>
Downloadable skill files that pair with specific Human Skills &mdash; instead of a human
following a workflow themselves, these get handed to an agent, which does the work directly
(interviewing the author, checking structure, and so on). Where AI-Assisted Workflows keep a
human in the driver's seat, an Agent Skill delegates the driving.
</p>

<div class="card-grid">
{% assign agent_docs = site.agent_skills | sort: "title" %}
{% for doc in agent_docs %}
  <a class="card" href="{{ doc.url | relative_url }}">
    <h3>{{ doc.title }}</h3>
    <p>{{ doc.summary }}</p>
  </a>
{% endfor %}
</div>

<p><em>This index fills in automatically as pages are added to <code>_agent_skills/</code> &mdash; no manual list to maintain.</em></p>
