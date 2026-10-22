---
title: "SALSA Team"
layout: project
permalink: /research/spectrally-agile-arrays/team/
summary: "Universities, a testbed, a start-up, and industry partners building spectrally agile radios for the upper mid-band."
sponsor: "NTIA Innovation Fund (NOFO-1 & 2)"
site_nav: salsa
wide: true
organizations:
  - name: "NYU"
    type: "University · Lead"
    role: "Project lead. Receiver RFIC, system architecture, scalable array processing, O-RU integration, and co-existence algorithms."
  - name: "Princeton"
    type: "University · NOFO-2"
    role: "Wideband transmitter and power amplifier RFICs."
  - name: "Rutgers WINLAB"
    type: "Testbed · NOFO-2"
    role: "Deployment and trials in the COSMOS O-RAN testbed in New York City."
  - name: "Pi-Radio"
    type: "Start-up"
    role: "NYU spin-off. FR3 software-defined radios, RFIC packaging, and the modular MIMO platform."
  - name: "Nokia"
    type: "Industry · NOFO-2"
    role: "System-level capacity evaluation, spectrum studies, and standards."
  - name: "Analog Devices"
    type: "Industry · NOFO-2"
    role: "O-RU interface platform for integration into O-RAN networks."
  - name: "FIU"
    type: "University · NOFO-1"
    role: "Adaptive null-forming and integrated sensing arrays in FR3."
# Photos: path relative to assets/images/. Leave "" to show initials.
# awards: which NTIA awards the person works on (shown as badges).
investigators:
  - name: "Sundeep Rangan"
    lead: true
    affiliation: "NYU"
    awards: ["NOFO-1", "NOFO-2"]
    photo: "sundeep-rangan.jpg"
    bio: "Lead PI on both awards; system architecture, scalable array processing, and co-existence algorithms."
  - name: "Hamed Rahmani"
    affiliation: "NYU"
    awards: ["NOFO-1", "NOFO-2"]
    photo: ""
    bio: "Spectrally agile receiver RFIC design."
  - name: "Aditya Dhananjay"
    affiliation: "Pi-Radio"
    awards: ["NOFO-1", "NOFO-2"]
    photo: ""
    bio: "FR3 SDRs, RFIC packaging, and the modular MIMO platform."
  - name: "Arjuna Madanayake"
    affiliation: "FIU"
    awards: ["NOFO-1"]
    photo: ""
    bio: "Adaptive null-forming and integrated sensing arrays in FR3."
  - name: "Marco Mezzavilla"
    affiliation: "Politecnico di Milano"
    awards: ["NOFO-1"]
    photo: ""
    bio: "Frequency-hopping FR3 SDR platform and multi-band system design."
  - name: "Ivan Seskar"
    affiliation: "Rutgers WINLAB"
    awards: ["NOFO-2"]
    photo: ""
    bio: "Integration into the COSMOS O-RAN testbed."
  - name: "Kaushik Sengupta"
    affiliation: "Princeton"
    awards: ["NOFO-2"]
    photo: ""
    bio: "Wideband transmitter and power amplifier RFIC design."
  - name: "Jinfeng Du"
    affiliation: "Nokia"
    awards: ["NOFO-2"]
    photo: ""
    bio: "System-level evaluation, spectrum studies, and standards."
---

<p class="section-label">People &amp; partners</p>
<h2>Participating organizations</h2>
<p class="team-note">SALSA brings together RFIC designers, systems researchers, a testbed, and a start-up with a path to commercial products.</p>

<div class="thrusts orgs">
{% for org in page.organizations %}
  <article class="thrust">
    <span class="thrust-num">{{ org.type }}</span>
    <h3>{{ org.name }}</h3>
    <p>{{ org.role }}</p>
  </article>
{% endfor %}
</div>

<p class="section-label section-gap">Project personnel</p>
<h2 id="investigators">Investigators</h2>
<p class="team-note"><strong>NOFO-1</strong>: Testing for Open, Secure and Adaptive Spectrum Sharing in FR3 (2023&ndash;2028). <strong>NOFO-2</strong>: Spectrally Agile and Scalable Open Radio Units for the Upper Mid-Band (2025&ndash;2030).</p>

<div class="pi-grid">
{% for inv in page.investigators %}
  <div class="pi-mini">
    {% if inv.photo and inv.photo != '' %}
    <img class="avatar" src="{{ inv.photo | prepend: '/assets/images/' | relative_url }}" alt="{{ inv.name }}">
    {% else %}
    {% assign parts = inv.name | split: ' ' %}
    <span class="avatar avatar-initials" aria-hidden="true">{{ parts.first | slice: 0 }}{{ parts.last | slice: 0 }}</span>
    {% endif %}
    <h4>{{ inv.name }}</h4>
    <p class="pi-aff">{{ inv.affiliation }}</p>
    <div class="award-badges">
      {% if inv.lead %}<span class="role-badge lead">Lead PI</span>{% endif %}
      {% for a in inv.awards %}<span class="role-badge">{{ a }}</span>{% endfor %}
    </div>
    <p>{{ inv.bio }}</p>
  </div>
{% endfor %}
</div>

<h3 class="students-head">Students</h3>
{% include project-members.html slug="spectrally-agile-arrays" %}

<p class="ack">This work is supported by the National Telecommunications and Information Administration (NTIA) Public Wireless Supply Chain Innovation Fund under awards 36-60-IF003 (NOFO-1) and 36-60-IF2419 (NOFO-2). Any opinions, findings, and conclusions or recommendations expressed are those of the authors and do not necessarily reflect the views of NTIA.</p>
