---
title: About Corpus
section: About Corpus
layout: page
---
<p>
Corpus is an archive, not a syllabus. It exists so the durable parts of
CS373 &mdash; how to scope a topic, write a caption that works, defend your
own research in conversation &mdash; outlive any one semester or instructor.
</p>

<div class="card-grid">
{% assign about_docs = site.about_corpus | sort: "order" %}
{% for doc in about_docs %}
  <a class="card" href="{{ doc.url | relative_url }}">
    <h3>{{ doc.title }}</h3>
    <p>{{ doc.summary }}</p>
  </a>
{% endfor %}
</div>
