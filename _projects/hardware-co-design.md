---
title: "Hardware-Algorithm Co-Design"
order: 3
summary: "Energy-efficient, reconfigurable wireless networks built from low-power, approximate, non-linear, and noisy components."
sponsor: "NSF CNS-2504400"
thumbnail: "/assets/images/projects/hardware-co-design/new-regime.png"
thumbnail_fit: contain
wide: true
hero_overlap: true
# Photos: put headshots in assets/images/people/ and set `photo` (path relative
# to assets/images/). Leave "" to show initials.
investigators:
  - name: "Sundeep Rangan"
    role: "PI"
    photo: "sundeep-rangan.jpg"
    bio: "Co-founder of Flarion (first cellular OFDM system); co-director of NYU WIRELESS. Leads the co-design methodology, algorithms, and capacity analysis."
  - name: "Elza Erkip"
    role: "Co-PI"
    photo: ""
    bio: "Information and communication theory of wireless networks; 2021 IEEE ComSoc Armstrong Award. Leads capacity with hardware impairments and multi-user modeling."
  - name: "Hamed Rahmani"
    role: "Co-PI"
    photo: ""
    bio: "Low-power, high-frequency silicon ICs; formerly Qualcomm (mmWave PAs) and IBM Research. Leads the low-power RF circuit design."
  - name: "Brandon Reagen"
    role: "Co-PI"
    photo: ""
    bio: "Low-power hardware accelerators and hardware for AI; DARPA RISER. Leads the low-voltage digital hardware and the emulation platform."
---

<div class="stat-strip">
  <div class="stat"><span class="stat-num">230<small>Mbps</small></span><span class="stat-label">data rate</span></div>
  <div class="stat"><span class="stat-num">20<small>m</small></span><span class="stat-label">range</span></div>
  <div class="stat"><span class="stat-num">&lt;7<small>mW</small></span><span class="stat-label">TX + RX power</span></div>
  <p class="stat-note">Target link from preliminary calculations: Bluetooth-class power, with data rates orders of magnitude higher.</p>
</div>

<div class="two-col codesign-intro">
  <div class="about-text">
    <p class="section-label">The challenge</p>
    <h2>High data rates at milliwatt power</h2>
    <p>mmWave cellular delivers massive data rates at a staggering power cost, while today's low-power radios run on milliwatts but are limited in data rate. Embedded and wearable devices increasingly need both.</p>
    <p>We develop the theory, algorithms, and design for reliable, high-performance wireless systems built from <strong>low-power, approximate, non-linear, and noisy components</strong>.</p>
  </div>
  <div class="pill-list">
    <div class="pill">
      <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/></svg></span>
      <div><h3>Co-design</h3><p>Allow very low-power but approximate, noisy, or distorted processing in the RF and digital hardware, and compensate with communication algorithms.</p></div>
    </div>
    <div class="pill">
      <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 6h10M18 6h2M4 12h4M12 12h8M4 18h12M20 18h0"/><circle cx="16" cy="6" r="2"/><circle cx="10" cy="12" r="2"/><circle cx="18" cy="18" r="2"/></svg></span>
      <div><h3>Reconfigurability</h3><p>Adapt power-performance trade-offs across components dynamically as channel, interference, and network conditions change.</p></div>
    </div>
  </div>
</div>

<figure class="figure-card">
  <a href="{{ '/assets/images/projects/hardware-co-design/new-regime.png' | relative_url }}"><img src="{{ '/assets/images/projects/hardware-co-design/new-regime.png' | relative_url }}" alt="Data rate and range versus power for BLE, sub-6 GHz cellular, mmWave cellular and mmWave WiFi, with the project's target regime at 230 Mbps, 20 m and 7 mW" loading="lazy"></a>
  <figcaption>Approximate operating regimes of commercial wireless systems. Today's systems are either high rate and high power (WiFi, cellular) or low power and low rate (Bluetooth). The project targets the new regime at the upper left.</figcaption>
</figure>

<p class="section-label section-gap">Research</p>
<h2>Four research thrusts</h2>

<div class="thrusts">
  <article class="thrust">
    <span class="thrust-num">Thrust 1</span>
    <h3>Low-power RF &amp; capacity analysis</h3>
    <p>New low-power RF components: a polar amplifier with configurable filtering, an injection-locked ring oscillator, and a reconfigurable LNA. Fundamental capacity bounds and signaling for the resulting noise, non-linearity, and low-resolution quantization.</p>
    <ul class="subthrusts">
      <li><span>Low-power RF circuits</span><span>Rahmani</span></li>
      <li><span>Capacity with hardware impairments</span><span>Erkip &middot; Rangan</span></li>
    </ul>
  </article>
  <article class="thrust">
    <span class="thrust-num">Thrust 2</span>
    <h3>Algorithms &amp; digital hardware</h3>
    <p>Low-voltage digital hardware that saves power but introduces occasional bit flips, with equalization, filtering, and decoding algorithms that compensate for impairments across RF and digital, and end-to-end power optimization.</p>
    <ul class="subthrusts">
      <li><span>Communication algorithms</span><span>Rangan</span></li>
      <li><span>Low-voltage digital hardware</span><span>Reagen</span></li>
    </ul>
  </article>
  <article class="thrust">
    <span class="thrust-num">Thrust 3</span>
    <h3>Multi-user &amp; multi-antenna systems</h3>
    <p>Compact low-power antenna-in-package arrays with low-power beamforming and mutual-coupling compensation, adjacent-carrier interference models, and components that adapt their dynamic range to interference.</p>
    <ul class="subthrusts">
      <li><span>Multi-user &amp; interference modeling</span><span>Erkip</span></li>
    </ul>
  </article>
  <article class="thrust">
    <span class="thrust-num">Thrust 4</span>
    <h3>Test circuits &amp; validation</h3>
    <p>Custom low-power RFIC fabrications, plus an emulation platform that captures RF non-linearity and noise together with digital approximation and bit flips, evaluated in link-layer and multi-user experiments.</p>
    <ul class="subthrusts">
      <li><span>RFIC fabrication</span><span>Rahmani</span></li>
      <li><span>Low-power emulation platform</span><span>Reagen</span></li>
    </ul>
  </article>
</div>

<p class="section-label section-gap">Team</p>
<h2>Investigators</h2>
<p class="team-note">All investigators are with the Department of Electrical and Computer Engineering, NYU Tandon School of Engineering, and NYU WIRELESS.</p>

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
    <span class="role-badge{% if inv.role == 'PI' %} lead{% endif %}">{{ inv.role }}</span>
    <p>{{ inv.bio }}</p>
  </div>
{% endfor %}
</div>

<h3 class="students-head">Students</h3>
{% include project-members.html %}

<div class="note related">
  <strong>Related:</strong> <a href="https://sdrangan.github.io/waveflow/docs/">WaveFlow</a>, our Python framework for algorithm-hardware co-design, is supported in part by this award.
</div>

<p class="ack">This material is based upon work supported by the National Science Foundation under award <a href="https://www.nsf.gov/awardsearch/show-award?AWD_ID=2504400">CNS-2504400</a>. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the authors and do not necessarily reflect the views of the National Science Foundation.</p>
