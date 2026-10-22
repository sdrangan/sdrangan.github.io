---
title: "SALSA: Spectrally Agile Large-Scale Arrays"
order: 1
featured: true
summary: "Wideband, frequency-agile RFICs and tileable massive MIMO radios for the upper mid-band (FR3), built as an Open Radio Unit."
sponsor: "NTIA Innovation Fund (NOFO-1 & 2)"
thumbnail: "/assets/images/projects/salsa/overview.svg"
thumbnail_fit: contain
wide: true
hero_overlap: true
site_nav: salsa
---

<div class="stat-strip">
  <div class="stat"><span class="stat-num">6&ndash;15<small>GHz</small></span><span class="stat-label">tunable RFIC range</span></div>
  <div class="stat"><span class="stat-num">1000+</span><span class="stat-label">antenna target scale</span></div>
  <div class="stat"><span class="stat-num">70&times;</span><span class="stat-label">lower cost per channel</span></div>
  <p class="stat-note">Design targets: tileable 8-channel RFIC modules, compared with today's best commercial off-the-shelf FR3 systems.</p>
</div>

<div class="two-col codesign-intro">
  <div class="about-text">
    <p class="section-label">The challenge</p>
    <h2>A vast band that must be shared</h2>
    <p>The upper mid-band, roughly 7&ndash;24 GHz, offers far more spectrum than the congested bands below 6 GHz with much better coverage than millimeter wave. It is a leading candidate for 6G. But it is a very wide range of frequencies, and it is already used by satellites, radar, and radio astronomy.</p>
    <p>Radios here will need to <strong>sense the spectrum, hop frequencies, and steer beams and nulls</strong> on the fly. SALSA builds the hardware to do that: a custom RFIC and a modular massive MIMO radio, delivered as an Open Radio Unit (O-RU) for O-RAN networks.</p>
  </div>
  <div class="pill-list">
    <div class="pill">
      <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12h3l2-6 3 12 3-9 2 6 2-3h5"/></svg></span>
      <div><h3>Spectral agility</h3><p>Wideband transmit and receive chains with fast frequency hopping, programmable filtering, and high linearity for co-existence with incumbents and resilience to jammers.</p></div>
    </div>
    <div class="pill">
      <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg></span>
      <div><h3>Scalability</h3><p>RFIC modules that tile coherently into large arrays, so the same building block serves a small research radio or a 1000+ element massive MIMO system.</p></div>
    </div>
  </div>
</div>

<figure class="figure-card">
  <a href="{{ '/assets/images/projects/salsa/overview.svg' | relative_url }}"><img src="{{ '/assets/images/projects/salsa/overview.svg' | relative_url }}" alt="SALSA targets the 6 to 15 GHz portion of the upper mid-band, with four tasks (spectrally agile RFICs, modular MIMO platforms, O-RU and O-RAN testbed, end-to-end demonstrations) and commercial opportunities in public cellular, commercial satellite, defense, and research labs" loading="lazy"></a>
  <figcaption>SALSA focuses on 6&ndash;15 GHz, where the near-term commercial and defense needs are greatest.</figcaption>
</figure>

<p class="section-label section-gap">Research</p>
<h2>Four tasks</h2>

<div class="thrusts">
  <article class="thrust">
    <span class="thrust-num">Task 1</span>
    <h3>Spectrally agile RFICs</h3>
    <p>A monolithic transceiver RFIC in GlobalFoundries 22FDX covering the full 6&ndash;15 GHz band, with sub-microsecond frequency and beam switching, N-path tunable filtering, and high-linearity front-ends.</p>
    <ul class="subthrusts">
      <li><span>Receive path</span><span>Rahmani (NYU)</span></li>
      <li><span>Transmit path &amp; power amplifiers</span><span>Sengupta (Princeton)</span></li>
    </ul>
  </article>
  <article class="thrust">
    <span class="thrust-num">Task 2</span>
    <h3>Modular MIMO platforms</h3>
    <p>RFIC packaging, compact multi-band antennas, and a tileable software-defined radio that builds up to an 8-stream, 64-antenna demonstration system.</p>
    <ul class="subthrusts">
      <li><span>Packaging, SDRs &amp; antennas</span><span>Pi-Radio</span></li>
    </ul>
  </article>
  <article class="thrust">
    <span class="thrust-num">Task 3</span>
    <h3>O-RU &amp; O-RAN testbed</h3>
    <p>Integration of the radio with an Analog Devices O-RU interface and open-source protocol stacks, then deployment in the COSMOS testbed in New York City.</p>
    <ul class="subthrusts">
      <li><span>O-RU integration</span><span>NYU</span></li>
      <li><span>COSMOS deployment</span><span>Seskar (Rutgers)</span></li>
    </ul>
  </article>
  <article class="thrust">
    <span class="thrust-num">Task 4</span>
    <h3>Capacity &amp; demonstrations</h3>
    <p>System-level capacity and coverage studies, satellite co-existence and anti-jamming, and end-to-end demonstrations of spectrum sharing and resilience on the testbed.</p>
    <ul class="subthrusts">
      <li><span>System evaluation</span><span>Nokia</span></li>
      <li><span>Algorithms &amp; demonstrations</span><span>Rangan (NYU)</span></li>
    </ul>
  </article>
</div>

<p class="section-label section-gap">Progress</p>
<h2>Where things stand</h2>

<div class="thrusts">
  <article class="thrust">
    <span class="thrust-num">Now</span>
    <h3>First chips back from fabrication</h3>
    <p>The first receiver and transmitter test chips are back from the foundry and in lab testing. The receiver uses a wideband mixer-first architecture with switchable filtering for high linearity against strong interferers.</p>
  </article>
  <article class="thrust">
    <span class="thrust-num">Now</span>
    <h3>Self-calibrating array processing</h3>
    <p>A real-time, self-calibrating beam- and null-former on an RFSoC FPGA has been built and verified, ready to drive the FR3 RFICs as they come up.</p>
  </article>
  <article class="thrust">
    <span class="thrust-num">Now</span>
    <h3>FR3 radios in COSMOS</h3>
    <p>Pi-Radio FR3 SDRs are running in the COSMOS testbed, carrying OFDM and 5G links in the upper mid-band and emulating satellite-terrestrial interference.</p>
  </article>
  <article class="thrust">
    <span class="thrust-num">Next</span>
    <h3>Algorithms for 1000+ antennas</h3>
    <p>Distributed long-term beamforming and fast iterative solvers that cut the computation of very large fully digital arrays by orders of magnitude.</p>
  </article>
</div>

<p class="section-label section-gap">Foundations</p>
<h2>Building on NOFO-1</h2>

<div class="vectors">

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/salsa/pi-radio-demo.jpg' | relative_url }}">
      <img src="{{ '/assets/images/projects/salsa/pi-radio-demo.jpg' | relative_url }}" alt="The team demonstrating the Pi-Radio FR3 software-defined radio at the Brooklyn 6G Summit" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">From discrete parts to silicon</span>
      <h3>The Pi-Radio FR3 SDR</h3>
      <p>Under the first NTIA award (NOFO-1), NYU and Pi-Radio built a two-channel software-defined radio covering the entire 6&ndash;24 GHz range with fast frequency hopping, entirely from commercial parts. It has been demonstrated at O-RAN workshops, ICC, and the Brooklyn 6G Summit. SALSA moves that functionality onto a custom RFIC to cut cost per channel and scale to massive arrays.</p>
      <ul class="subthrusts">
        <li><a href="https://doi.org/10.1109/SPAWC60668.2024.10694319">Frequency-hopping FR3 SDR</a><span>IEEE SPAWC 2024</span></li>
      </ul>
    </div>
  </article>

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/salsa/multiband-rate.png' | relative_url }}">
      <img src="{{ '/assets/images/projects/salsa/multiband-rate.png' | relative_url }}" alt="CDF of user rate in a dense urban ray-tracing study at 6, 12, 18, and 24 GHz, with the best-choice multi-band system outperforming every single band" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Key paper</span>
      <h3>Why spectral agility pays off</h3>
      <p>Our ray-tracing study of a dense urban network shows that a radio able to pick the best band for each user beats any single fixed band, with fallback to lower frequencies under blockage. The paper also evaluates satellite-terrestrial interference and a compact multi-band array design.</p>
      <ul class="subthrusts">
        <li><a href="https://doi.org/10.1109/OJCOMS.2024.3373368">Cellular wireless networks in the upper mid-band</a><span>IEEE OJ-COMS 2024</span></li>
      </ul>
    </div>
  </article>

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/salsa/nulling.png' | relative_url }}">
      <img src="{{ '/assets/images/projects/salsa/nulling.png' | relative_url }}" alt="Base station beam pattern in azimuth and elevation with a main beam toward the terrestrial user and deep nulls toward Starlink satellites" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Co-existence</span>
      <h3>Sharing spectrum with satellites</h3>
      <p>Large arrays can steer nulls toward satellites while serving terrestrial users, keeping interference to satellite uplinks below protection limits with negligible loss to the cellular link. This work continues in our satellite-terrestrial co-existence project.</p>
      <ul class="subthrusts">
        <li><a href="{{ '/research/satellite-terrestrial-coexistence/' | relative_url }}">Satellite-terrestrial co-existence</a><span>Project page</span></li>
      </ul>
    </div>
  </article>

</div>

<p class="section-label section-gap">Team</p>
<h2>Who we are</h2>
<p class="team-note">SALSA is led by NYU with Princeton, Rutgers WINLAB, and the NYU spin-off Pi-Radio, together with industry partners Nokia and Analog Devices.</p>

<a class="btn btn-primary" href="{{ '/research/spectrally-agile-arrays/team/' | relative_url }}">Meet the team &rarr;</a>

<p class="ack">This work is supported by the National Telecommunications and Information Administration (NTIA) Public Wireless Supply Chain Innovation Fund under awards 36-60-IF003 (NOFO-1) and 36-60-IF2419 (NOFO-2). Any opinions, findings, and conclusions or recommendations expressed are those of the authors and do not necessarily reflect the views of NTIA.</p>
