---
title: "Research"
permalink: /research/
author_profile: true
toc: false
---

Our research centers on next-generation wireless systems. Below are our current
projects &mdash; click any project for details, people, publications, and
sponsors.

<div class="project-grid">
{% assign projects = site.projects | sort: "order" %}
{% for p in projects %}
  <a class="project-card" href="{{ p.url | relative_url }}">
    <img class="project-thumb"
         src="{% if p.thumbnail and p.thumbnail != '' %}{{ p.thumbnail | relative_url }}{% else %}{{ '/assets/images/placeholder-project.svg' | relative_url }}{% endif %}"
         alt="{{ p.title }}">
    <div class="project-body">
      <h3>{{ p.title }}</h3>
      {% if p.sponsor and p.sponsor != '' %}<p class="project-sponsor">{{ p.sponsor }}</p>{% endif %}
      <p class="project-summary">{{ p.summary }}</p>
    </div>
  </a>
{% endfor %}
</div>
