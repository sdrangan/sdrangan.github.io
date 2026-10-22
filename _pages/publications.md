---
title: "Publications"
permalink: /publications/
intro: "Selected recent papers, newest first, tagged by project: a place to start reading. For a complete list, see Google Scholar."
wide: true
---

[All publications on Google Scholar](https://scholar.google.com/citations?user=fzSHXS8AAAAJ&hl=en&oi=ao){: .btn .btn-primary}

{% comment %}Papers come from _data/publications.yml, grouped by year (newest first); within a year they keep file order.
Only papers co-authored by S. Rangan appear here; collaborators' papers appear on their project pages only.{% endcomment %}
{%- assign own = site.data.publications | where_exp: "p", "p.authors contains 'S. Rangan'" -%}
{%- assign years = own | group_by: "year" | sort: "name" | reverse -%}
{%- for y in years -%}
<section class="pub-group" id="y{{ y.name }}">
  <h2>{{ y.name }}</h2>
  {%- include pub-list.html pubs=y.items tags=true -%}
</section>
{%- endfor -%}
