---
title: "Satellite-Terrestrial Co-Existence"
order: 2
summary: "Detection, channel estimation, interference nulling, and anti-jamming for shared terrestrial and satellite operation in the upper mid-band."
sponsor: ""
thumbnail: "/assets/images/projects/satellite/thumb.jpg"
wide: true
---

<div class="two-col project-intro">
  <div class="about-text" markdown="1">
<p class="section-label">Overview</p>

The upper mid-band (FR3, 7&ndash;24 GHz) is a prime candidate for 5G and 6G
expansion, but much of it overlaps the satellite Ku-band, where commercial
satellite systems already operate. At the same time, LEO mega-constellations
are becoming critical infrastructure, and their exposed, predictable
geometries make them targets for ground-based jamming.

We develop **spatial signal processing** that lets terrestrial and satellite
networks share spectrum safely: base stations that **detect and null**
satellite receivers before interfering with them, and satellite constellations
that **cooperate** to reject jammers no single satellite can separate.
Methods are evaluated with site-specific ray tracing and realistic Starlink
orbital geometries.
  </div>
  <figure class="figure-card">
    <img src="{{ '/assets/images/projects/satellite/coexistence-overview.svg' | relative_url }}" alt="LEO satellites linked by inter-satellite links serve a VSAT terminal, while a terrestrial base station serving a mobile user interferes with the VSAT terminal and the satellites" loading="lazy">
    <figcaption>Terrestrial and satellite networks sharing spectrum: interference and jamming can reach both satellite terminals on the ground and the satellites themselves.</figcaption>
  </figure>
</div>

<div class="vectors">

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/satellite/nulling-radio-maps.jpg' | relative_url }}">
      <img src="{{ '/assets/images/projects/satellite/nulling-radio-maps.jpg' | relative_url }}" alt="Ray-traced interference radio maps for a rural area near Boulder, Colorado, before (left) and after (right) interference nulling at the terrestrial base station" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 1</span>
      <h3>Terrestrial-satellite co-existence</h3>
      <p>High-power terrestrial base stations can overwhelm nearby satellite downlink receivers, but a base station can only null a victim it knows about. We propose having satellite terminals periodically transmit beacons that base stations use to detect them, estimate their channels, and place spatial nulls in their directions. Analysis and multi-user ray-tracing studies (left: interference before nulling; right: after) show the approach is effective even at high victim densities, with massive MIMO arrays preserving terrestrial downlink quality.</p>
      <ul class="subthrusts">
        <li><a href="https://arxiv.org/abs/2510.08824">Joint detection, estimation &amp; nulling</a><span>IEEE GLOBECOM 2025</span></li>
        <li><a href="https://github.com/SJ00425/NTN-Nulling">NTN-Nulling</a><span>Code</span></li>
      </ul>
    </div>
  </article>

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/satellite/anti-jamming-beampatterns.jpg' | relative_url }}">
      <img src="{{ '/assets/images/projects/satellite/anti-jamming-beampatterns.jpg' | relative_url }}" alt="Sky-view beampatterns of a dish jammer and of the ground transmitter's equilibrium beamformer when cooperating with 1, 3, and 5 Starlink satellites" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 2</span>
      <h3>Multi-satellite anti-jamming</h3>
      <p>From orbit, a ground jammer close to a legitimate transmitter is nearly impossible to separate spatially, even with a large array on a single satellite. We exploit the dense coverage and inter-satellite links of LEO mega-constellations so that several satellites jointly receive the uplink. Modeling the transmitter and jammer as players in a convex-concave game, we compute the equilibrium beamformers with a fast min&ndash;max solver. With realistic Starlink geometries, cooperation among a handful of satellites restores capacity that a single satellite loses entirely.</p>
      <ul class="subthrusts">
        <li><a href="https://arxiv.org/abs/2601.15557">Distributed uplink anti-jamming</a><span>IEEE ICC 2026</span></li>
        <li><a href="https://github.com/SJ00425/NTN-Anti-Jamming">NTN-Anti-Jamming</a><span>Code</span></li>
      </ul>
    </div>
  </article>

</div>

## Publications

- S. Jia, M. Ying, M. Mezzavilla, D. Calin, T. S. Rappaport, and S. Rangan,
  "Joint Detection, Channel Estimation and Interference Nulling for
  Terrestrial-Satellite Downlink Co-Existence in the Upper Mid-Band," *IEEE
  GLOBECOM*, 2025. [arXiv:2510.08824](https://arxiv.org/abs/2510.08824)
- S. Jia, M. Ying, M. Mezzavilla, T. S. Rappaport, and S. Rangan, "Distributed
  Uplink Anti-Jamming in LEO Mega-Constellations via Game-Theoretic
  Beamforming," *IEEE ICC*, 2026.
  [arXiv:2601.15557](https://arxiv.org/abs/2601.15557)

## People

- [Shizhen Jia](https://shizhen-jia.github.io/) (lead), Mingjun Ying
- Collaborators: Marco Mezzavilla (Politecnico di Milano), Doru Calin (MediaTek), Theodore S. Rappaport
