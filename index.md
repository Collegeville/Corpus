---
title: Corpus
layout: default
wide: true
---
<div class="eyebrow">Welcome</div>
<h1>Corpus</h1>
<p class="home-tagline">{{ site.tagline }}</p>
<hr class="rule">

<!-- Reuses the skill-page layout classes (skill-layout / skill-body /
     marginalia) so the homepage shares the same visual language as every
     other page, rather than introducing a one-off hero pattern. The
     marginalia rail here holds site facts instead of page metadata. -->
<div class="skill-layout">
  <div class="skill-body">
    <p>
    This Corpus website provides a consolidation and reorganization of a collection of research resources developed by Mike Heroux as part of the Computer Science Senior Research Seminar capstone at the College of St. Benedict and St. John's
    University. Corpus preserves what that course taught about doing and communicating research well &mdash; independent of any one semester, tool, or assignment.
    </p>

    <p>The material is split into three kinds of knowledge, plus the
    thinking behind that split:</p>

    <div class="card-grid">
      <a class="card" href="{{ '/about-corpus/' | relative_url }}">
        <h3>About Corpus</h3>
        <p>Why the site exists, and the philosophy behind the split.</p>
      </a>
      <a class="card" href="{{ '/human-skills/' | relative_url }}">
        <h3>Human Skills</h3>
        <p>Timeless techniques for research, writing, and speaking that don't expire.</p>
      </a>
      <a class="card" href="{{ '/ai-workflows/' | relative_url }}">
        <h3>AI-Assisted Workflows</h3>
        <p>Timely, tool-dependent workflows a human follows with an AI tool's help.</p>
      </a>
      <a class="card" href="{{ '/agent-skills/' | relative_url }}">
        <h3>Agent Skills</h3>
        <p>Downloadable skill files handed to an agent to do the work directly.</p>
      </a>
      <a class="card" href="{{ '/sample-semester-schedule/' | relative_url }}">
        <h3>Sample Semester Schedule</h3>
        <p>A worked example: one semester's class meetings and assignment due dates, merged into a single schedule.</p>
      </a>
    </div>
  </div>

  <aside class="marginalia">
    <div class="marginalia__item">
      <span class="marginalia__label">Years taught</span>
      <span class="marginalia__value">28</span>
    </div>
    <div class="marginalia__item">
      <span class="marginalia__label">Human Skills</span>
      <span class="marginalia__value">{{ site.human_skills | size }}</span>
    </div>
    <div class="marginalia__item">
      <span class="marginalia__label">AI-Assisted Workflows</span>
      <span class="marginalia__value">{{ site.ai_workflows | size }}</span>
    </div>
    <div class="marginalia__item">
      <span class="marginalia__label">Agent Skills</span>
      <span class="marginalia__value">{{ site.agent_skills | size }}</span>
    </div>
    <div class="marginalia__item">
      <span class="marginalia__label">About Corpus pages</span>
      <span class="marginalia__value">{{ site.about_corpus | size }}</span>
    </div>
    <div class="marginalia__item">
      <span class="marginalia__label">Institution</span>
      <span class="marginalia__value">CSB &amp; SJU</span>
    </div>
  </aside>
</div>
