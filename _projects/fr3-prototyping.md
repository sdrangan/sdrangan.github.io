---
title: "FR3 Prototyping, Channel Measurements & Sensing"
short: "Prototyping"   # tag on the Publications page
order: 5
summary: "Hardware prototyping, channel measurement campaigns, and integrated sensing in the upper mid-band (FR3)."
sponsor: ""
thumbnail: "/assets/images/projects/fr3-prototyping/thumb.jpg"
wide: true
---

<div class="two-col project-intro">
  <div class="about-text" markdown="1">
<p class="section-label">Overview</p>

The upper mid-band (FR3, 7&ndash;24 GHz) is a leading candidate for 6G, but
little hardware exists to experiment in it. Systems in these bands must hop
across widely separated frequencies, share spectrum with satellites and radar,
and sense the environment as well as communicate.

We build **open, frequency-agile FR3 platforms** and use them end to end:
**multi-band channel measurements** that ground our models in real
propagation, **full 5G/O-RAN links** running at FR3, and a **mobile robotic
testbed** that ties every RF measurement to a precise position.
  </div>
  <figure class="figure-card">
    <img src="{{ '/assets/images/projects/fr3-prototyping/demo.jpg' | relative_url }}" alt="Team members demonstrating an FR3 O-RAN radio unit built with a Pi-Radio FR3 front end" loading="lazy">
    <figcaption>Live demonstration of our FR3 O-RAN radio unit with the Pi-Radio FR3 front end.</figcaption>
  </figure>
</div>

<div class="vectors">

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/fr3-prototyping/pi-radio-rfsoc.jpg' | relative_url }}">
      <img src="{{ '/assets/images/projects/fr3-prototyping/pi-radio-rfsoc.jpg' | relative_url }}" alt="Pi-Radio dual-channel FR3 SDR connected to a Xilinx RFSoC 4x2 board" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 1</span>
      <h3>Pi-Radio FR3 SDR</h3>
      <p>Our platforms are built on the FR3 software-defined radio developed in collaboration with <a href="https://www.pi-rad.io/">Pi-Radio</a>, an NYU start-up. The radio offers fast-tunable operation across the entire FR3 band, so a single front end can hop between frequencies for communication, sensing, and channel sounding. It plugs into common baseband boards such as USRPs and the Xilinx RFSoC.</p>
      <ul class="subthrusts">
        <li><strong>Frequency range</strong><span>6&ndash;24 GHz</span></li>
        <li><strong>Channels</strong><span>2 TX + 2 RX, phase-synchronous</span></li>
        <li><strong>Instantaneous bandwidth</strong><span>1 GHz</span></li>
        <li><a href="https://www.pi-rad.io/">Pi-Radio</a><span>NYU start-up partner</span></li>
      </ul>
    </div>
  </article>

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/fr3-prototyping/channel-measurement-setup.jpg' | relative_url }}">
      <img src="{{ '/assets/images/projects/fr3-prototyping/channel-measurement-setup.jpg' | relative_url }}" alt="Indoor FR3 measurement setup at NYU WIRELESS: a transmitter on a stand and a receiver on a rotation platform" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 2</span>
      <h3>FR3 channel measurements</h3>
      <p>FR3 systems will need to use several bands at once, for macro-diversity, co-existence with incumbents, and resilience to jamming, so we measure and model the channel across multiple frequencies simultaneously. Our open-source RFSoC channel sounder, with a rotating receiver, captures delay and angle at 6.5, 8.75, 10, and 15 GHz. The results show the trade-off for multi-band sensing: lower bands detect more paths, while higher bands give cleaner estimates.</p>
      <ul class="subthrusts">
        <li><a href="https://github.com/ali-rasteh/RFSoC_SDR">RFSoC FR3 channel sounder</a><span>Open-source code</span></li>
        <li><strong>Multi-band channel sensing</strong><span>IEEE GLOBECOM 2025</span></li>
      </ul>
    </div>
  </article>

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/fr3-prototyping/oai-end-to-end.jpg' | relative_url }}">
      <img src="{{ '/assets/images/projects/fr3-prototyping/oai-end-to-end.jpg' | relative_url }}" alt="End-to-end FR3 data link using OpenAirInterface: a gNodeB built from a USRP N310 and a UE built from a USRP B210, each with a Pi-Radio FR3 front end" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 3</span>
      <h3>End-to-end FR3 systems</h3>
      <p>We bring complete cellular stacks up in the upper mid-band. Using the open-source OpenAirInterface (OAI) 5G implementation, we run a full gNodeB-to-UE data link at FR3 with Pi-Radio front ends. We have also built an O-RAN-compliant radio unit that pairs an Analog Devices O-RU with the Pi-Radio FR3 front end, giving an open testbed for physical-layer and hardware research in new bands.</p>
      <ul class="subthrusts">
        <li><strong>OAI end-to-end link at FR3</strong><span>gNodeB + UE</span></li>
        <li><strong>Open FR3 O-RU</strong><span>O-RAN split 7.2</span></li>
        <li><strong>6G prototyping in the upper mid-band</strong><span>IEEE WCNC 2025</span></li>
      </ul>
    </div>
  </article>

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/fr3-prototyping/robot-demo.webp' | relative_url }}">
      <img src="{{ '/assets/images/projects/fr3-prototyping/robot-demo.webp' | relative_url }}" alt="Animation of a robot carrying a Pi-Radio FR3 transceiver driving through an indoor maze" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 4</span>
      <h3>Mobile robotic platform</h3>
      <p><strong>MobiFR3</strong> puts the Pi-Radio FR3 transceiver on TurtleBot4 / ROS 2 robots with LiDAR, odometry, and camera sensing, so every RF measurement is tagged with a precise robot pose. The platform collects large mobile FR3 datasets, calibrates ray-traced digital twins against hardware, and supports our work on <a href="{{ '/research/wireless-robotic-navigation/' | relative_url }}">wireless-aided robotic navigation</a>.</p>
      <ul class="subthrusts">
        <li><a href="https://panshark.github.io/projects/wireless-robotics-platform/">MobiFR3 testbed</a><span>Brooklyn 6G Summit 2025 demo</span></li>
      </ul>
    </div>
  </article>

</div>

## Publications

{% include pub-list.html project="fr3-prototyping" %}

## People

- [Ali Rasteh](https://ali-rasteh.github.io/), [Haozhe Lei](https://panshark.github.io/)
- Collaborators: Marco Mezzavilla (Politecnico di Milano), Aditya Dhananjay, Michael Zappe, and Elijah Zappe (Pi-Radio), Roberto Bomfin and Marwa Chafii (NYU Abu Dhabi)
