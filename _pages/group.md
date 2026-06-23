---
title: "Group"
permalink: /group/
author_profile: false
toc: true
toc_label: "On this page"
toc_sticky: true
---

## Sundeep Rangan

<div class="pi-profile">
  <img class="pi-photo" src="{{ '/assets/images/sundeep-rangan.jpg' | relative_url }}" alt="Sundeep Rangan">
  <div class="pi-bio" markdown="1">
Professor, ECE, NYU Tandon School of Engineering &middot; Director, [NYU WIRELESS](http://wireless.engineering.nyu.edu/)

Sundeep Rangan received the B.A.Sc. at the University of Waterloo, Canada and the
M.Sc. and Ph.D. at the University of California, Berkeley, all in Electrical
Engineering. He has held postdoctoral appointments at the University of Michigan,
Ann Arbor and Bell Labs.

In 2000, he co-founded (with four others) Flarion Technologies, a spin-off of
Bell Labs, that developed Flash OFDM, one of the first cellular OFDM data systems
and pre-cursor to 4G systems including LTE and WiMAX. In 2006, Flarion was
acquired by Qualcomm Technologies where Dr. Rangan was a Director of Engineering
involved in OFDM infrastructure products. He joined the ECE department at NYU
Tandon (formerly NYU Polytechnic) in 2010. He is a Fellow of the IEEE and
Director of NYU WIRELESS, an academic-industry research center researching
next-generation wireless systems. His research interests are in wireless
communications, signal processing, information theory and control theory.

[Email](mailto:srangan@nyu.edu) &middot; [Google Scholar](https://scholar.google.com/citations?user=fzSHXS8AAAAJ&hl=en&oi=ao)
  </div>
</div>

## Current Members

<div class="member-grid">
{% for m in site.data.members %}
  <div class="member-card">
    {% if m.website and m.website != '' %}<a href="{{ m.website }}">{% endif %}
    <img class="member-photo"
         src="{% if m.photo and m.photo != '' %}{{ m.photo | prepend: '/assets/images/' | relative_url }}{% else %}{{ '/assets/images/placeholder-person.svg' | relative_url }}{% endif %}"
         alt="{{ m.name }}">
    {% if m.website and m.website != '' %}</a>{% endif %}
    <div class="member-info">
      <h3 class="member-name">{{ m.name }}</h3>
      {% if m.role and m.role != '' %}<p class="member-role">{{ m.role }}</p>{% endif %}
      {% if m.interests and m.interests != '' %}<p class="member-interests">{{ m.interests }}</p>{% endif %}
      <p class="member-links">
        {% if m.email and m.email != '' %}<a href="mailto:{{ m.email }}">Email</a>{% endif %}
        {% if m.website and m.website != '' %}{% if m.email and m.email != '' %} &middot; {% endif %}<a href="{{ m.website }}">Website</a>{% endif %}
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
