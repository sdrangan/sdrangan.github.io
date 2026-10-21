---
title: "Research"
permalink: /research/
eyebrow: "Projects"
intro: "Our research centers on next-generation wireless systems. Click any project for details, people, publications, and sponsors."
wide: true
---

<div class="project-grid">
{% assign projects = site.projects | sort: "order" %}
{% for p in projects %}
  {% include project-card.html project=p %}
{% endfor %}
</div>
