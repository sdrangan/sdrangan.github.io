---
title: "News"
permalink: /news/
intro: "Events, awards, and updates from TORCH Lab and NYU WIRELESS."
---

<ul class="news-list">
{% for item in site.data.news %}
  <li class="news-item">
    <time>{{ item.date }}</time>
    <p>{{ item.text }}{% if item.link %} <a href="{{ item.link | relative_url }}">{{ item.link_label | default: "Read more" }} &rarr;</a>{% endif %}</p>
  </li>
{% endfor %}
</ul>
