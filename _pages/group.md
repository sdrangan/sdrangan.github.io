---
title: "Group"
permalink: /group/
author_profile: true
toc: true
toc_label: "On this page"
toc_sticky: true
---

## Current Members

<div class="member-grid">
{% for m in site.data.members %}
  <div class="member-card">
    <img class="member-photo"
         src="{% if m.photo and m.photo != '' %}{{ m.photo | prepend: '/assets/images/' }}{% else %}/assets/images/placeholder-person.svg{% endif %}"
         alt="{{ m.name }}">
    <div class="member-info">
      <h3 class="member-name">{{ m.name }}</h3>
      {% if m.role and m.role != '' %}<p class="member-role">{{ m.role }}</p>{% endif %}
      {% if m.interests and m.interests != '' %}<p class="member-interests">{{ m.interests }}</p>{% endif %}
      <p class="member-links">
        {% if m.email and m.email != '' %}<a href="mailto:{{ m.email }}">Email</a>{% endif %}
        {% if m.website and m.website != '' %} &middot; <a href="{{ m.website }}">Website</a>{% endif %}
        {% if m.scholar and m.scholar != '' %} &middot; <a href="{{ m.scholar }}">Scholar</a>{% endif %}
      </p>
    </div>
  </div>
{% endfor %}
</div>

## Alumni

{% if site.data.alumni and site.data.alumni.size > 0 %}
<ul class="alumni-list">
{% for a in site.data.alumni %}
  <li>
    <strong>{{ a.name }}</strong>{% if a.degree and a.degree != '' %} ({{ a.degree }}){% endif %}{% if a.now and a.now != '' %} &mdash; now {{ a.now }}{% endif %}{% if a.website and a.website != '' %} &middot; <a href="{{ a.website }}">website</a>{% endif %}
  </li>
{% endfor %}
</ul>
{% else %}
*Alumni will be listed here.*
{% endif %}

---

*Group members: to update your entry, edit [`_data/members.yml`](https://github.com/sdrangan/sdrangan.github.io/blob/main/_data/members.yml) and add a photo to `assets/images/members/`. See the comments at the top of that file.*
{: .notice}
