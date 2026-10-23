---
title: "Teaching"
permalink: /teaching/
wide: true
intro: "Graduate courses in hardware design and wireless communications at NYU Tandon, with every lecture, lab, and notebook openly available."
---

<p class="section-label">Courses</p>
<h2>Open course material</h2>
<p class="section-intro">All of our course material is fully open source: lecture notes, slides, labs, code, and demos are on GitHub for anyone to use, adapt, and build on.</p>

<div class="project-grid">
{% for c in site.data.courses %}
  <a class="project-card course-card" href="{{ c.url }}">
    {% if c.thumbnail and c.thumbnail != '' %}
    <img class="project-thumb project-thumb-contain" src="{{ c.thumbnail | relative_url }}" alt="">
    {% else %}
    <div class="project-thumb project-thumb-blank course-thumb" aria-hidden="true">
      {% case c.icon %}
      {% when 'antenna' %}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M12 11v10M9 21h6"/><circle cx="12" cy="9" r="2"/><path d="M8.5 5.5a5 5 0 0 0 0 7M15.5 5.5a5 5 0 0 1 0 7M5.6 2.6a9 9 0 0 0 0 12.8M18.4 2.6a9 9 0 0 1 0 12.8"/></svg>
      {% when 'wave' %}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12c1.5-5 3.5-5 5 0s3.5 5 5 0 3.5-5 5 0 3.5 5 5 0"/><circle cx="4.5" cy="8.5" r=".6" fill="currentColor"/><circle cx="9.5" cy="15.5" r=".6" fill="currentColor"/><circle cx="14.5" cy="8.5" r=".6" fill="currentColor"/><circle cx="19.5" cy="15.5" r=".6" fill="currentColor"/></svg>
      {% else %}<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/></svg>
      {% endcase %}
    </div>
    {% endif %}
    <div class="project-body">
      <span class="tag">{{ c.code }}</span>
      <h3>{{ c.title }}</h3>
      <p class="course-term">Last taught {{ c.term }}</p>
      <p>{{ c.description }}</p>
      <span class="more">{{ c.url_label }} &#8599;</span>
    </div>
  </a>
{% endfor %}
</div>

<p class="section-label section-gap">Tools</p>
<h2>LLM Grader</h2>

<div class="two-col llmgrader-intro">
  <div class="about-text">
    <p>We have built <strong>LLM Grader</strong>, an open-source autograding tool for engineering courses. Traditional autograders check final answers; LLM Grader evaluates the <strong>reasoning</strong>: multi-step derivations, design trade-offs, and open-ended justifications, scored against instructor rubrics with detailed feedback.</p>
    <p>Students get immediate, rubric-based feedback as they work through problems, and can connect the course to the AI assistant they already use. It is being piloted in our graduate hardware design course.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="https://sdrangan.github.io/llmgrader/docs/">Documentation</a>
      <a class="btn btn-outline" href="https://llmgrader-e6o7.onrender.com/">Try the portal &#8599;</a>
    </div>
  </div>
  <figure class="figure-card">
    <a href="https://llmgrader-e6o7.onrender.com/"><img src="{{ '/assets/images/teaching/llmgrader-homepage.jpg' | relative_url }}" alt="LLM Grader portal showing a hardware design question, a student solution, and rubric-based feedback scoring 10 out of 10" loading="lazy"></a>
    <figcaption>The grading portal: a question, the student's solution, and rubric-by-rubric feedback.</figcaption>
  </figure>
</div>

<div class="feature-grid">
  <div class="pill">
    <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3 8-8"/><path d="M20 12v6a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h9"/></svg></span>
    <div><h3>Grades reasoning, not just answers</h3><p>LLM-based evaluation of derivations and design justifications, with optional numeric checks and web-search fact checking.</p></div>
  </div>
  <div class="pill">
    <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M8 6h13M8 12h13M8 18h13"/><path d="M3 6h.01M3 12h.01M3 18h.01"/></svg></span>
    <div><h3>Structured problems &amp; rubrics</h3><p>Each problem captures instructor intent, a reference solution, a rubric, and grading notes. Scoring is fully customizable.</p></div>
  </div>
  <div class="pill">
    <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2a3 3 0 0 0-3 3v1H7a2 2 0 0 0-2 2v3h1a2 2 0 0 1 0 4H5v3a2 2 0 0 0 2 2h3v-1a2 2 0 0 1 4 0v1h3a2 2 0 0 0 2-2v-3h-1a2 2 0 0 1 0-4h1V8a2 2 0 0 0-2-2h-2V5a3 3 0 0 0-3-3z"/></svg></span>
    <div><h3>Course MCP for students' own AI</h3><p>Publish a course as an MCP server so students can study with Claude, ChatGPT, or Copilot: problems, rubrics, solutions, and lecture slides.</p></div>
  </div>
  <div class="pill">
    <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6M10 3v6L4.5 18.5A1.7 1.7 0 0 0 6 21h12a1.7 1.7 0 0 0 1.5-2.5L14 9V3"/><path d="M7 15h10"/></svg></span>
    <div><h3>Testable grading</h3><p>Instructors write trial solutions with expected scores and rerun the suite, like unit tests, whenever a rubric or model changes.</p></div>
  </div>
  <div class="pill">
    <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"/><path d="M21 21l-4.3-4.3M8 11h6M11 8v6"/></svg></span>
    <div><h3>Transparent traces</h3><p>Instructors can inspect the reasoning behind every point awarded, and export courses to Gradescope.</p></div>
  </div>
  <div class="pill">
    <span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg></span>
    <div><h3>Privacy by design</h3><p>Ephemeral, pseudonymized sessions. Grade records are never linked to student identities and stay in the university LMS.</p></div>
  </div>
</div>
