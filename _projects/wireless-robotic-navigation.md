---
title: "Wireless-Aided Robotic Navigation"
order: 6
summary: "Robots that localize radio sources and navigate with wireless signals, from probabilistic RF localization to a 10-GHz robotic testbed."
sponsor: ""
thumbnail: "/assets/images/projects/robotic-navigation/thumb.jpg"
wide: true
---

<div class="two-col project-intro">
  <div class="about-text" markdown="1">
<p class="section-label">Overview</p>

Wireless signals carry rich spatial information in their multipath, and a robot
can use them to find a radio source and navigate toward it, even when cameras
and maps are incomplete. But a single RF measurement is usually ambiguous:
blockage and reflections leave several plausible source locations.

We treat this as **probabilistic inference**: learn full belief maps over where
a transmitter could be, use those beliefs to **guide a robot's search**, and
validate everything on a **10-GHz robotic testbed** in the upper mid-band (FR3).

[Full project details on Haozhe Lei's site &rarr;](https://panshark.github.io/projects/){: .btn .btn-primary}
  </div>
  <figure class="video-embed">
    <div class="video-embed-frame">
      <iframe src="https://www.linkedin.com/embed/feed/update/urn:li:ugcPost:7518355941885612033?compact=1" title="Finding the Invisible: Wireless Source Localization" loading="lazy" allowfullscreen></iframe>
    </div>
    <figcaption>Finding the Invisible: Wireless Source Localization. H. Lei, R. Chen, Y. Jiang, A. Dhananjay, S. Rangan. <a href="https://www.linkedin.com/feed/update/urn:li:ugcPost:7518355941885612033/">View on LinkedIn</a></figcaption>
  </figure>
</div>

<div class="vectors">

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/robotic-navigation/localization.jpg' | relative_url }}">
      <img src="{{ '/assets/images/projects/robotic-navigation/localization.jpg' | relative_url }}" alt="LOCUS-DT: a measured RF snapshot is matched against ray-traced digital-twin candidates to produce a posterior over transmitter location" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 1</span>
      <h3>Probabilistic source localization</h3>
      <p>Rather than forcing an ambiguous RF snapshot into one coordinate, we learn full posterior distributions over transmitter location, preserving directional and multimodal uncertainty. Our methods match measured multipath against ray-traced wireless digital twins, learn measurement-conditioned likelihoods, jointly infer position and heading, and keep working when the robot has mapped only part of its environment.</p>
      <ul class="subthrusts">
        <li><a href="https://panshark.github.io/projects/locus-dt-digital-twin-localization/">LOCUS-DT</a><span>Digital-twin posterior localization</span></li>
        <li><a href="https://panshark.github.io/projects/mccle-full-posterior-localization/">MC-CLE</a><span>Learned full-posterior likelihoods</span></li>
        <li><a href="https://panshark.github.io/projects/magnetar-joint-rf-pose-inference/">MAGNETAR</a><span>Joint position &amp; heading inference</span></li>
        <li><a href="https://panshark.github.io/projects/maple-rf-partial-map-localization/">MAPLE-RF</a><span>Localization with partial maps</span></li>
      </ul>
    </div>
  </article>

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/robotic-navigation/navigation.webp' | relative_url }}">
      <img src="{{ '/assets/images/projects/robotic-navigation/navigation.webp' | relative_url }}" alt="Animation of a robot's camera view and predicted map as a wireless-guided navigation policy searches an indoor environment" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 2</span>
      <h3>Wireless-aided navigation</h3>
      <p>Belief maps become guidance for a robot's search policy. Using ray-traced digital twins as a physics-informed prior, our reinforcement-learning agents navigate unseen indoor environments toward a transmitter zero-shot, with the robot's SLAM system supplying the map and pose.</p>
      <ul class="subthrusts">
        <li><a href="https://panshark.github.io/projects/wireless-indoor-navigation/">Wireless-guided indoor navigation</a><span>Physics-informed RL</span></li>
      </ul>
    </div>
  </article>

  <article class="vector">
    <a class="vector-media" href="{{ '/assets/images/projects/robotic-navigation/mobifr3.jpg' | relative_url }}">
      <img src="{{ '/assets/images/projects/robotic-navigation/mobifr3.jpg' | relative_url }}" alt="The MobiFR3 robot, a TurtleBot4 carrying a Pi-Radio FR3 transceiver, at the Brooklyn 6G Summit 2025" loading="lazy">
    </a>
    <div class="vector-text">
      <span class="thrust-num">Research area 3</span>
      <h3>Robotic experimental platform</h3>
      <p><strong>MobiFR3</strong> is our 10-GHz robotic RF testbed. It pairs Pi-Radio SDR channel sounding and Vivaldi antennas with TurtleBot4 / ROS 2 robots, LiDAR, odometry, and RGB sensing, so every RF measurement is tied to a precise robot pose. Measurement-aligned Sionna RT scenes calibrate simulation to the hardware, connecting simulation-trained models to physical experiments.</p>
      <ul class="subthrusts">
        <li><a href="https://panshark.github.io/projects/wireless-robotics-platform/">MobiFR3 testbed</a><span>Brooklyn 6G Summit 2025 demo</span></li>
      </ul>
    </div>
  </article>

</div>

<p class="credit">Figures and video courtesy of Haozhe Lei.</p>

## People

- [Haozhe Lei](https://panshark.github.io/) (lead), Ruibin Chen, Yuhan Jiang
- Collaborator: Aditya Dhananjay
