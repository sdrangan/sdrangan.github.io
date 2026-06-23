---
title: "Teaching"
permalink: /teaching/
author_profile: false
toc: false
---

{% if site.data.courses and site.data.courses.size > 0 %}
<ul class="course-list">
{% for c in site.data.courses %}
  <li class="course-item">
    <a href="{{ c.url }}"><strong>{% if c.code and c.code != '' %}{{ c.code }}: {% endif %}{{ c.title }}</strong></a>
    {% if c.term and c.term != '' %}<span class="course-term"> &middot; {{ c.term }}</span>{% endif %}
    {% if c.description and c.description != '' %}<div class="course-desc">{{ c.description }}</div>{% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
*Course listings coming soon. Each course will link to its own course page.*

<!-- To add courses, edit _data/courses.yml -->
{% endif %}
