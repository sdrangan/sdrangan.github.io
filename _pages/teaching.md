---
title: "Teaching"
permalink: /teaching/
intro: "Courses taught by Prof. Rangan at NYU Tandon. Each links to its own course page."
---

{% if site.data.courses and site.data.courses.size > 0 %}
<ul class="course-list">
{% for c in site.data.courses %}
  <li class="course-item">
    <a href="{{ c.url }}">{% if c.code and c.code != '' %}{{ c.code }}: {% endif %}{{ c.title }}</a>
    {% if c.term and c.term != '' %}<span class="course-term"> &middot; {{ c.term }}</span>{% endif %}
    {% if c.description and c.description != '' %}<div class="course-desc">{{ c.description }}</div>{% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
<div class="empty-state">
  <p>Course listings coming soon.</p>
</div>

<!-- To add courses, edit _data/courses.yml -->
{% endif %}
