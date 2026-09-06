---
title: Search
section: Search
layout: page
wide: true
---

<p>
Search across every Human Skill, AI-Assisted Workflow, Agent Skill, and About Corpus page in
one place &mdash; title, summary, and body text all count.
</p>

<div class="search-controls">
  <input type="text" id="search-input" class="search-input" placeholder="Search Corpus&hellip;" autocomplete="off" disabled>
</div>

<p id="search-status" class="search-status">Loading search index&hellip;</p>

<div id="search-results" class="card-grid"></div>

<script>
(function () {
  var input = document.getElementById('search-input');
  var status = document.getElementById('search-status');
  var results = document.getElementById('search-results');
  var index = null;

  function escapeHtml(str) {
    return String(str).replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c];
    });
  }

  // Pull a window of plain text out of a full-body match so the result shows
  // where the query actually hit, not just the start of the page.
  function snippetAround(text, q) {
    var lower = text.toLowerCase();
    var i = lower.indexOf(q);
    if (i === -1) { return text.slice(0, 160).replace(/\s+/g, ' ').trim(); }
    var start = Math.max(0, i - 60);
    var end = Math.min(text.length, i + q.length + 100);
    var out = text.slice(start, end).replace(/\s+/g, ' ').trim();
    return (start > 0 ? '…' : '') + out + (end < text.length ? '…' : '');
  }

  function idleStatus() {
    status.textContent = 'Search ' + index.length + ' page' + (index.length === 1 ? '' : 's') + ' — type to begin.';
  }

  function render(query) {
    results.innerHTML = '';
    if (!index) { return; }
    if (!query) {
      idleStatus();
      return;
    }
    var q = query.toLowerCase();
    var matches = index.filter(function (doc) {
      return doc.title.toLowerCase().indexOf(q) !== -1 ||
        doc.summary.toLowerCase().indexOf(q) !== -1 ||
        doc.text.toLowerCase().indexOf(q) !== -1;
    });

    status.textContent = matches.length === 0
      ? 'No results for “' + query + '”.'
      : matches.length + ' result' + (matches.length === 1 ? '' : 's') + ' for “' + query + '”.';

    matches.forEach(function (doc) {
      var meta = doc.category ? (doc.section + ' · ' + doc.category) : doc.section;
      var snip = doc.summary && doc.summary.toLowerCase().indexOf(q) !== -1
        ? doc.summary
        : snippetAround(doc.text, q);
      var a = document.createElement('a');
      a.className = 'card';
      a.href = doc.url;
      a.innerHTML =
        '<h3>' + escapeHtml(doc.title) + '</h3>' +
        '<p><span class="search-result__meta">' + escapeHtml(meta) + '</span> — ' + escapeHtml(snip) + '</p>';
      results.appendChild(a);
    });
  }

  fetch('{{ '/search.json' | relative_url }}')
    .then(function (res) { return res.json(); })
    .then(function (data) {
      index = data;
      input.disabled = false;
      idleStatus();
    })
    .catch(function () {
      status.textContent = 'Search index failed to load.';
    });

  input.addEventListener('input', function () {
    render(input.value.trim());
  });
})();
</script>
