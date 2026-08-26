from pathlib import Path


path = Path("index.html")
text = path.read_text(encoding="utf-8")

css = r'''
    .linkedin-list { position: relative; display: grid; gap: 18px; }
    .linkedin-list::before {
      content: ""; position: absolute; left: 111px; top: 30px; bottom: 30px;
      width: 2px; background: var(--line);
    }
    .linkedin-post {
      position: relative; display: grid; grid-template-columns: 92px minmax(0, 1fr);
      gap: 38px; align-items: start;
    }
    .linkedin-post::before {
      content: ""; position: absolute; left: 103px; top: 30px; z-index: 2;
      width: 16px; height: 16px; border-radius: 50%; background: #0a66c2;
      box-shadow: 0 0 0 6px var(--bg), 0 0 0 7px var(--line);
    }
    section:nth-child(even) .linkedin-post::before {
      box-shadow: 0 0 0 6px var(--surface), 0 0 0 7px var(--line);
    }
    .linkedin-date {
      padding-top: 13px; color: var(--accent); text-align: right;
      font-size: .78rem; font-weight: 900; line-height: 1.35; letter-spacing: .03em;
      text-transform: uppercase;
    }
    .linkedin-content {
      padding: 24px 26px; border: 1px solid var(--line); border-radius: 20px;
      background: var(--surface); box-shadow: 0 10px 30px rgba(9,21,40,.045);
    }
    section:nth-child(even) .linkedin-content { background: #fbfcfe; }
    .linkedin-meta {
      display: flex; align-items: center; gap: 9px; margin-bottom: 9px;
      color: var(--teal); font-size: .78rem; font-weight: 850;
      letter-spacing: .045em; text-transform: uppercase;
    }
    .linkedin-badge {
      width: 25px; height: 25px; display: inline-grid; place-items: center;
      color: #fff; background: #0a66c2; border-radius: 5px;
      font-size: .82rem; font-weight: 900; line-height: 1;
    }
    .linkedin-content h3 { margin: 0 0 9px; color: var(--navy); font-size: 1.22rem; }
    .linkedin-content p { margin: 0; color: var(--muted); }
    .linkedin-link {
      display: inline-flex; align-items: center; gap: 7px; margin-top: 14px;
      color: #0a66c2; font-weight: 850; text-decoration-thickness: 1px;
      text-underline-offset: 4px;
    }
    .linkedin-source-note {
      margin-top: 24px; padding: 18px 22px; border-left: 4px solid #0a66c2;
      border-radius: 0 14px 14px 0; color: var(--muted); background: var(--surface-soft);
      font-size: .9rem;
    }

    @media (max-width: 720px) {
      .linkedin-list::before { left: 12px; top: 22px; bottom: 22px; }
      .linkedin-post { grid-template-columns: 1fr; gap: 8px; padding-left: 38px; }
      .linkedin-post::before { left: 4px; top: 17px; }
      .linkedin-date { padding-top: 0; text-align: left; }
      .linkedin-content { padding: 21px; }
    }
'''

if ".linkedin-list" not in text:
    marker = "    .service-list { display: grid; gap: 14px; }"
    if marker not in text:
        raise SystemExit("Could not find CSS insertion marker")
    text = text.replace(marker, css + "\n" + marker, 1)

if 'href="#linkedin"' not in text:
    marker = '        <a href="#service">Service</a>'
    if marker not in text:
        raise SystemExit("Could not find navigation insertion marker")
    text = text.replace(
        marker,
        '        <a href="#linkedin">LinkedIn</a>\n' + marker,
        1,
    )

section = r'''
    <section id="linkedin">
      <div class="container">
        <div class="section-head">
          <div><p class="kicker">Public professional activity</p><h2>Recent LinkedIn updates</h2></div>
          <p class="section-intro">Selected publicly indexed posts from Dr. Gupta’s LinkedIn profile, arranged newest to oldest. The list reflects posts visible through public search and may not include every LinkedIn update.</p>
        </div>

        <div class="linkedin-list" aria-label="Recent LinkedIn posts in reverse chronological order">
          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2026-07">July<br>2026</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Conference presentation</div>
              <h3>LLM evaluation at the Agentic AI Summit 2026</h3>
              <p>Announcement of an August 1 presentation at the UC Berkeley campus on LLM evaluation, responsible AI, and agentic AI.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/posts/kishordattagupta_agentic-ai-summit-2026-activity-7483766424897921024-BzJP" target="_blank" rel="noopener">Read the LinkedIn post <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2026-07">July<br>2026</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Conference activity</div>
              <h3>Presenting two papers at the ALVR Workshop at ACL 2026</h3>
              <p>Shared plans to present two papers in San Diego and engage with researchers working in multimodal AI, vision-language models, and computer vision.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/in/kishordattagupta/recent-activity/all/" target="_blank" rel="noopener">Open public LinkedIn activity <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2026-06">June<br>2026</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Paper acceptance</div>
              <h3>Two papers accepted for ALVR 2026 poster presentations</h3>
              <p>Announced <em>VLCE: A Knowledge-Enhanced Framework for Image Description in Disaster Assessment</em> and <em>Beyond Visual Similarity: Rule-Guided Multimodal Clustering with Explicit Domain Rules</em>.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/posts/kishordattagupta_acl2026-alvr-artificialintelligence-activity-7474676607077527552-ILIo" target="_blank" rel="noopener">Read the LinkedIn post <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2026-05">May<br>2026</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Research appointment</div>
              <h3>Third year in the AFRL Visiting Faculty Research Program</h3>
              <p>Shared his return to Rome, New York, for a third year as Visiting Faculty, continuing collaborative research in AI and intelligent systems supporting national defense.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/posts/kishordattagupta_afrl-vfrp-researchcollaboration-activity-7459736642942210048-_pYJ" target="_blank" rel="noopener">Read the LinkedIn post <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2026-04">Spring<br>2026</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Student research</div>
              <h3>Student presentations at the CAU Annual Research Symposium</h3>
              <p>Recognized Ph.D. students Savannah Shannon and Frank Dadzie for presenting their research and representing the laboratory at Clark Atlanta University.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/in/kishordattagupta/recent-activity/all/" target="_blank" rel="noopener">Open public LinkedIn activity <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2026-03">March<br>2026</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Tutorial</div>
              <h3>LiteVLA at the Edge tutorial at NICE 2026</h3>
              <p>Promoted a tutorial led by Ph.D. students Justin Williams and Mohd Ariful Haque on CPU-only vision-language-action control for neuro-inspired edge robotics.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/in/kishordattagupta/recent-activity/all/" target="_blank" rel="noopener">Open public LinkedIn activity <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2026-03">March<br>2026</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Student presentation</div>
              <h3>Justin Williams presenting at IEEE PerCom 2026</h3>
              <p>Highlighted a Ph.D. student presentation in Pisa, Italy, connected with work partially supported through a NASA University Student Research Challenge grant.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/posts/kishordattagupta_ieeepercom-percom2026-clarkatlanta-activity-7440233988469739520-_xjR" target="_blank" rel="noopener">Read the LinkedIn post <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2026">Early<br>2026</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Book publication</div>
              <h3><em>Securing Industrial Control Systems</em> available</h3>
              <p>Shared the availability of the book <em>Securing Industrial Control Systems: Advanced Strategies and Technologies</em>, developed with co-authors and collaborators.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/in/kishordattagupta/recent-activity/all/" target="_blank" rel="noopener">Open public LinkedIn activity <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2025-12">December<br>2025</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Faculty recognition</div>
              <h3>Outstanding Scholar Award for 2024–2025</h3>
              <p>Announced receipt of Clark Atlanta University’s Outstanding Scholar Award and acknowledged university leadership and academic colleagues.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/posts/kishordattagupta_clarkatlantauniversity-cauproud-scholarship-activity-7404164522250301440-fFjU" target="_blank" rel="noopener">Read the LinkedIn post <span aria-hidden="true">↗</span></a>
            </div>
          </article>

          <article class="linkedin-post">
            <time class="linkedin-date" datetime="2025-09">September<br>2025</time>
            <div class="linkedin-content">
              <div class="linkedin-meta"><span class="linkedin-badge" aria-hidden="true">in</span>Research platform</div>
              <h3>Introducing MonitorLLM</h3>
              <p>Introduced a developing platform for continuously tracking changes in large language model behavior over time without relying on fixed, repeated prompts.</p>
              <a class="linkedin-link" href="https://www.linkedin.com/posts/kishordattagupta_monitorllm-activity-7371736786496299008-nb8v" target="_blank" rel="noopener">Read the LinkedIn post <span aria-hidden="true">↗</span></a>
            </div>
          </article>
        </div>

        <p class="linkedin-source-note">LinkedIn controls public visibility and indexing. Some posts expose a direct public URL, while others are available through the profile’s public activity page.</p>
        <div class="actions"><a class="btn btn-primary" href="https://www.linkedin.com/in/kishordattagupta/recent-activity/all/" target="_blank" rel="noopener">View public LinkedIn activity</a></div>
      </div>
    </section>
'''

if '<section id="linkedin">' not in text:
    marker = '    <section id="service">'
    if marker not in text:
        raise SystemExit("Could not find section insertion marker")
    text = text.replace(marker, section + "\n\n" + marker, 1)

old_footer = 'This GitHub Pages profile uses information published on <a href="https://www.kishordgupta.com/" target="_blank" rel="noopener">kishordgupta.com</a>.'
new_footer = 'This GitHub Pages profile uses information published on <a href="https://www.kishordgupta.com/" target="_blank" rel="noopener">kishordgupta.com</a> and selected publicly indexed posts from <a href="https://www.linkedin.com/in/kishordattagupta/" target="_blank" rel="noopener">LinkedIn</a>.'
if old_footer in text:
    text = text.replace(old_footer, new_footer, 1)

path.write_text(text, encoding="utf-8")
