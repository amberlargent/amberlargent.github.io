from pathlib import Path

ROOT = Path('.')

def write(path, text):
    Path(path).write_text(text, encoding='utf-8')

def read(path):
    return Path(path).read_text(encoding='utf-8')

def replace_required(text, old, new, label):
    if old not in text:
        raise RuntimeError(f'Missing expected block: {label}')
    return text.replace(old, new)

# Shared case study page template. Keep CSS compact but aligned to the existing visual system.
def case_page(title, eyebrow, lead, visual_title, visual_meta, proof_items, story_h2, story_intro, summary, overview_cards, challenge_cards, process_steps, structure_cards, people_cards, outcome_cards, learning_text, footer_label):
    proof_html = '\n'.join(f'        <div class="proof-item">{big}<span>{small}</span></div>' for big, small in proof_items)
    overview_html = '\n'.join(f'''        <div class="card {klass}">\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </div>''' for h, p, klass in overview_cards)
    challenge_html = '\n'.join(f'''        <div class="card {klass}">\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </div>''' for h, p, klass in challenge_cards)
    process_html = '\n'.join(f'''        <div class="timeline-item">\n          <div class="timeline-number">{i}</div>\n          <div class="timeline-content">\n            <h3>{h}</h3>\n            <p>{p}</p>\n          </div>\n        </div>''' for i, (h, p) in enumerate(process_steps, start=1))
    structure_html = '\n'.join(f'''        <div class="card {klass}">\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </div>''' for h, p, klass in structure_cards)
    people_html = '\n'.join(f'''        <div class="card {klass}">\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </div>''' for h, p, klass in people_cards)
    outcome_html = '\n'.join(f'''        <div class="card {klass}">\n          <h3>{h}</h3>\n          <p>{p}</p>\n        </div>''' for h, p, klass in outcome_cards)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Amber Largent | {title}</title>
  <style>
    :root {{ --sage:#CFD2B4; --blush:#F2C6D5; --pink:#E46FA1; --slate:#6A747E; --black:#030303; --white:#fffafc; }}
    a:focus-visible,.button:focus-visible {{ outline:4px solid var(--pink); outline-offset:4px; }}
    .skip-link {{ position:absolute; left:16px; top:-60px; background:var(--black); color:var(--white); padding:10px 14px; border-radius:999px; font-weight:900; z-index:100; }}
    .skip-link:focus {{ top:16px; }}
    * {{ box-sizing:border-box; }} html {{ scroll-behavior:smooth; }}
    body {{ margin:0; font-family:Arial,sans-serif; background:var(--sage); color:var(--black); line-height:1.6; }}
    a {{ color:inherit; }}
    .site-nav {{ position:sticky; top:0; z-index:20; background:rgba(255,250,252,.94); backdrop-filter:blur(12px); border-bottom:1px solid rgba(3,3,3,.08); }}
    .nav-inner {{ max-width:1120px; margin:0 auto; padding:16px 24px; display:flex; justify-content:space-between; align-items:center; gap:24px; }}
    .brand {{ font-weight:900; letter-spacing:-.02em; }} .brand span {{ display:block; color:var(--slate); font-size:13px; font-weight:700; }}
    .nav-links {{ display:flex; flex-wrap:wrap; gap:18px; font-size:14px; font-weight:800; }} .nav-links a {{ text-decoration:none; transition:color .15s ease; }} .nav-links a:hover,.nav-links a[href*='.html'] {{ color:var(--pink); }} .nav-links a[href^='#'] {{ color:var(--slate); }}
    header {{ background:radial-gradient(circle at 18% 18%,rgba(242,198,213,.85),transparent 28%),radial-gradient(circle at 88% 82%,rgba(228,111,161,.24),transparent 30%),var(--sage); border-bottom:1px solid rgba(3,3,3,.08); }}
    .hero {{ max-width:1120px; margin:0 auto; padding:86px 24px 72px; }}
    .hero-grid {{ display:grid; grid-template-columns:1fr .95fr; gap:36px; align-items:center; }}
    .eyebrow {{ display:inline-block; background:rgba(255,250,252,.78); border:1px solid rgba(228,111,161,.4); border-radius:999px; padding:8px 14px; color:var(--slate); font-size:13px; font-weight:900; letter-spacing:.08em; text-transform:uppercase; margin-bottom:22px; }}
    h1 {{ font-size:clamp(44px,6vw,76px); line-height:.98; letter-spacing:-.055em; margin:0 0 24px; max-width:980px; }}
    h2 {{ font-size:clamp(34px,5vw,56px); line-height:1; letter-spacing:-.04em; margin:0 0 22px; }}
    .lead {{ font-size:21px; max-width:860px; margin:0 0 30px; color:#1c1c1c; }}
    .button-row {{ display:flex; flex-wrap:wrap; gap:14px; margin-top:28px; }}
    .button {{ display:inline-flex; align-items:center; justify-content:center; text-decoration:none; font-weight:900; padding:13px 20px; border-radius:999px; border:2px solid var(--black); background:var(--white); color:var(--black); box-shadow:0 6px 0 var(--black); transition:transform .15s ease,box-shadow .15s ease,background .15s ease; }}
    .button:hover {{ background:var(--pink); transform:translateY(2px); box-shadow:0 4px 0 var(--black); }}
    .platform-frame {{ background:var(--white); border:2px solid var(--black); border-radius:24px; box-shadow:0 14px 0 var(--black); overflow:hidden; }}
    .platform-bar {{ display:flex; gap:8px; align-items:center; padding:12px 16px; background:rgba(242,198,213,.72); border-bottom:2px solid var(--black); }} .dot {{ width:12px; height:12px; border-radius:999px; background:var(--pink); border:1px solid var(--black); }}
    .platform-url {{ margin-left:8px; background:rgba(255,250,252,.86); border:1px solid rgba(3,3,3,.18); border-radius:999px; padding:4px 12px; font-size:13px; font-weight:800; color:var(--slate); overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }}
    .platform-visual {{ padding:24px; background:linear-gradient(135deg,rgba(207,210,180,.55),rgba(242,198,213,.5)),var(--white); }}
    .platform-header {{ background:var(--black); color:var(--white); border-radius:18px; padding:24px; margin-bottom:18px; }} .platform-header strong {{ display:block; font-size:24px; line-height:1.05; letter-spacing:-.03em; }} .platform-header span {{ display:block; margin-top:8px; color:var(--blush); font-weight:800; }}
    .mini-grid {{ display:grid; grid-template-columns:repeat(2,1fr); gap:12px; }} .mini-tile {{ min-height:72px; border-radius:16px; background:rgba(255,250,252,.86); border:1px solid rgba(3,3,3,.12); padding:14px; font-weight:900; }}
    section {{ max-width:1120px; margin:48px auto; padding:56px 32px; background:rgba(255,250,252,.42); border:1px solid rgba(255,250,252,.7); border-radius:32px; box-shadow:0 18px 50px rgba(3,3,3,.10); }}
    .section-intro {{ max-width:840px; font-size:19px; color:#202020; margin-bottom:34px; }}
    .grid-2,.grid-3,.proof-strip {{ display:grid; gap:22px; align-items:start; }} .grid-2 {{ grid-template-columns:repeat(2,1fr); }} .grid-3 {{ grid-template-columns:repeat(3,1fr); }} .proof-strip {{ grid-template-columns:repeat(4,1fr); }}
    .card,.summary-card {{ background:rgba(255,250,252,.88); border:1px solid rgba(228,111,161,.34); border-top:6px solid var(--pink); border-radius:24px; padding:26px; box-shadow:0 14px 34px rgba(3,3,3,.08); }}
    .summary-card {{ border-left:7px solid var(--pink); border-top:1px solid rgba(228,111,161,.34); padding:30px; }} .summary-card p {{ margin:0; font-size:22px; line-height:1.4; font-weight:800; letter-spacing:-.02em; }}
    .card h3 {{ margin:0 0 10px; font-size:24px; line-height:1.1; letter-spacing:-.02em; }} .card p {{ margin:0 0 14px; }} .card p:last-child {{ margin-bottom:0; }} .slate-card {{ border-top-color:var(--slate); }} .blush-card {{ border-top-color:var(--blush); }}
    .timeline {{ display:grid; gap:18px; }} .timeline-item {{ display:grid; grid-template-columns:54px 1fr; gap:18px; align-items:start; }} .timeline-number {{ display:inline-flex; align-items:center; justify-content:center; width:44px; height:44px; border-radius:999px; background:var(--blush); border:2px solid var(--black); box-shadow:0 4px 0 var(--black); font-weight:900; }} .timeline-content {{ background:rgba(255,250,252,.88); border:1px solid rgba(228,111,161,.34); border-radius:20px; padding:20px; }} .timeline-content h3 {{ margin:0 0 8px; font-size:22px; letter-spacing:-.02em; }} .timeline-content p {{ margin:0; }}
    .proof-item {{ background:rgba(255,250,252,.82); border:1px solid rgba(228,111,161,.34); border-radius:18px; padding:18px; font-weight:900; text-align:center; }} .proof-item span {{ display:block; color:var(--slate); font-size:13px; text-transform:uppercase; letter-spacing:.08em; margin-top:4px; }}
    footer {{ padding:34px 24px; text-align:center; background:var(--black); color:var(--blush); font-size:14px; }}
    @media (max-width:900px) {{ .nav-inner {{ align-items:flex-start; flex-direction:column; }} .hero-grid,.grid-2,.grid-3,.proof-strip,.mini-grid {{ grid-template-columns:1fr; }} section {{ margin:28px 14px; padding:40px 20px; }} .timeline-item {{ grid-template-columns:1fr; }} }}
    @media (prefers-reduced-motion:reduce) {{ .button {{ transition:none; }} .button:hover {{ transform:none; }} }}
  </style>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <nav class="site-nav"><div class="nav-inner"><div class="brand">Amber Largent<span>Trusted to Bring Structure</span></div><div class="nav-links"><a href="index.html">Home</a><a href="experience.html">Work Evidence</a><a href="#story">Story</a><a href="#structure">Structure</a><a href="#people">People</a><a href="#outcome">Outcome</a><a href="learning.html">Learning</a><a href="values.html">How I Work</a><a href="index.html#contact">Contact</a></div></div></nav>
  <main id="main">
    <header><div class="hero"><div class="hero-grid"><div><div class="eyebrow">{eyebrow}</div><h1>{title}</h1><p class="lead">{lead}</p><div class="button-row"><a class="button" href="experience.html">Back to Work Evidence</a><a class="button" href="#outcome">View Outcome</a></div></div><div class="platform-frame" aria-label="Visual summary of the case study"><div class="platform-bar"><span class="dot"></span><span class="dot"></span><span class="dot"></span><div class="platform-url">case study view</div></div><div class="platform-visual"><div class="platform-header"><strong>{visual_title}</strong><span>{visual_meta}</span></div><div class="mini-grid"><div class="mini-tile">Starting point</div><div class="mini-tile">Visibility</div><div class="mini-tile">Structure</div><div class="mini-tile">Outcome</div></div></div></div></div></div></header>
    <section id="story"><h2>{story_h2}</h2><p class="section-intro">{story_intro}</p><div class="summary-card"><p>{summary}</p></div><div class="proof-strip">{proof_html}</div></section>
    <section id="overview"><h2>What I owned</h2><p class="section-intro">Each case study follows the same operating-structure pattern: identify what was unclear, make the work visible, build usable structure, bring the right people together, and create movement.</p><div class="grid-3">{overview_html}</div></section>
    <section id="challenge"><h2>The unclear starting point</h2><div class="grid-2">{challenge_html}</div></section>
    <section id="process"><h2>What needed to become visible</h2><p class="section-intro">The work moved forward when the hidden parts became easier to see: decisions, ownership, risks, workflow steps, learner needs, or operational signals.</p><div class="timeline">{process_html}</div></section>
    <section id="structure"><h2>The structure I built</h2><div class="grid-2">{structure_html}</div></section>
    <section id="people"><h2>How I brought people together</h2><div class="grid-2">{people_html}</div></section>
    <section id="outcome"><h2>What changed</h2><p class="section-intro">Outcomes are written for public use and avoid exposing internal details, tool configurations, or exact metrics that should stay internal.</p><div class="grid-2">{outcome_html}</div><div class="button-row"><a class="button" href="experience.html">Back to Work Evidence</a><a class="button" href="index.html">Main Portfolio</a></div></section>
    <section id="learning"><h2>What I learned</h2><div class="summary-card"><p>{learning_text}</p></div></section>
  </main>
  <footer><p>© 2026 Amber Largent · {footer_label}</p></footer>
</body>
</html>'''

# Update homepage positioning.
index_path = Path('index.html')
index = read(index_path)
index = replace_required(index, '<span>Clear paths through complex work</span>', '<span>Trusted to Bring Structure</span>', 'home brand span')
index = replace_required(index, '<div class="eyebrow">Clear paths through complex work</div>', '<div class="eyebrow">Trusted to Bring Structure</div>', 'home eyebrow')
index = replace_required(index, '''          I turn unclear work into visible, usable operating structure: the plans, workflows,
          resources, reporting rhythms, and follow-through that help complex work move.''', '''          I turn unclear, cross-functional work into visible, usable operating structure: the plans,
          workflows, resources, reporting rhythms, and follow-through that help complex work move.''', 'home lead one')
index = replace_required(index, '''          My background spans project execution, learning enablement, knowledge systems, coaching,
          reporting, and AI-assisted development and workflows, but the throughline is consistent: make the work clear,
          make it usable, and help people act.''', '''          My work sits where people, process, and technology meet. I clarify what matters,
          make ownership visible, connect the right partners, and build practical systems teams can use and sustain.''', 'home lead two')
index = replace_required(index, '<h2>How I Bring Structure</h2>', '<h2>Trusted to Bring Structure</h2>', 'home structure heading')
index = replace_required(index, 'My strongest work sits where projects, people, process, learning, technology, and communication meet.', 'I build four kinds of structure that help complex work become visible, usable, and easier to move forward.', 'home structure intro')
old_cards = '''        <div class="card">
          <h3>Project + Process</h3>
          <p>Clarify ownership, timelines, decisions, risks, dependencies, project artifacts, and follow-through for complex work.</p>
        </div>
        <div class="card id-card">
          <h3>Learning + Enablement</h3>
          <p>Design learning, guidance, and resources that help people understand change and apply new approaches in real work.</p>
        </div>
        <div class="card neutral-card">
          <h3>Visibility + Knowledge Systems</h3>
          <p>Build reporting, dashboards, knowledge spaces, audits, and resource hubs that make work easier to find, trust, and act on.</p>
        </div>
        <div class="card">
          <h3>Coaching + Team Support</h3>
          <p>Use observation, data, call evaluation, feedback, facilitation, and mentorship to identify patterns and practical next steps.</p>
        </div>'''
new_cards = '''        <div class="card">
          <h3>Project + Program Structure</h3>
          <p>Plans, requirements, decisions, risks, dependencies, ownership, and operating rhythms that keep complex work moving.</p>
        </div>
        <div class="card id-card">
          <h3>Workflow + Operational Systems</h3>
          <p>Processes, controls, integrations, and human decision points that turn scattered work into a usable system.</p>
        </div>
        <div class="card neutral-card">
          <h3>Readiness + Adoption</h3>
          <p>Learning, communications, resources, and manager support that help people understand and apply change.</p>
        </div>
        <div class="card">
          <h3>Reporting + Follow-Through</h3>
          <p>Dashboards, audits, status rhythms, and action tracking that make progress, risks, and next steps visible.</p>
        </div>'''
index = replace_required(index, old_cards, new_cards, 'home four structure cards')
old_evidence_grid = '''      <div class="grid-3">
        <div class="card">
          <h3>Global PLJ pilot</h3>
          <p>Led and project managed a global Personalized Learning Journey pilot with partners across training, analytics, exam operations, vendors, and readiness.</p>
          <p>Public-facing details are limited, but the pilot improved key customer experience and efficiency indicators across selected tracks. Detailed metrics are available for internal review.</p>
        </div>

        <div class="card">
          <h3>Wrike project hub</h3>
          <p>Built a Wrike operating hub that standardized intake, project setup, status visibility, repeatable workflows, and manager-facing reporting. The goal was not tool administration; it was to reduce ambiguity, make ownership visible, and give leaders a clearer view of work in motion.</p>
        </div>

        <div class="card">
          <h3>Capacity planning platform</h3>
          <p>Built a web-based capacity planning platform for a large project management organization, moving from discovery to functional prototype in under two weeks.</p>
        </div>
      </div>'''
new_evidence_grid = '''      <div class="grid-3">
        <div class="card">
          <h3>Finding the Right Balance Between Automation and Human Judgment</h3>
          <p>Cross-functional pilot management, data-informed decisions, and measurable operational improvement.</p>
          <div class="button-row"><a class="button" href="plj-pilot.html">View Case Study</a></div>
        </div>

        <div class="card">
          <h3>Turning Fragmented Planning Into a Shared Operating View</h3>
          <p>Capacity-planning discovery, technical partnership, integrations, and iterative development, clearly labeled as in progress.</p>
          <div class="button-row"><a class="button" href="capacity-planning.html">View Case Study</a></div>
        </div>

        <div class="card">
          <h3>From Manual Audits to Built-In Accountability</h3>
          <p>Audit design, backlog cleanup, policy improvement, workflow controls, and requirements for automation.</p>
          <div class="button-row"><a class="button" href="sonar-audit.html">View Case Study</a></div>
        </div>

        <div class="card">
          <h3>Building a Communications and Knowledge Function From Zero</h3>
          <p>Operating-model design, policy governance, platform migrations, and scalable support.</p>
          <div class="button-row"><a class="button" href="communications-knowledge.html">View Case Study</a></div>
        </div>

        <div class="card">
          <h3>Designing Tool Adoption for a Distributed Workforce</h3>
          <p>Asynchronous learning, hands-on practice, manager accountability, and repeatable change readiness.</p>
          <div class="button-row"><a class="button" href="discovery-series.html">View Case Study</a></div>
        </div>

        <div class="card">
          <h3>Taking a Multi-Parish Website From Idea to Launch</h3>
          <p>Public-facing concept-to-launch project leadership with visible work samples.</p>
          <div class="button-row"><a class="button" href="triparish.html">View Case Study</a></div>
        </div>
      </div>'''
index = replace_required(index, old_evidence_grid, new_evidence_grid, 'home evidence case studies')
write(index_path, index)

# Update Work Evidence positioning and case study links.
exp_path = Path('experience.html')
exp = read(exp_path)
exp = exp.replace('AI-assisted development, workflow design, and knowledge systems.', 'AI-assisted development, workflow and operational systems, readiness and adoption, reporting, follow-through, and knowledge systems.')
exp = replace_required(exp, '''        <p class="lead">
          The throughline is practical leadership: understand what is happening, make the work visible,
          build useful structure, and help teams move with clearer ownership and follow-through.
        </p>''', '''        <p class="lead">
          The throughline is operating structure: understand what is happening, make the work visible,
          build systems people can use, and help teams move with clearer ownership and follow-through.
        </p>''', 'experience lead throughline')
exp = replace_required(exp, '<h2>Scope and evidence</h2>', '<h2>Operating structure in practice</h2>', 'experience proof heading')
exp = replace_required(exp, '''        These proof points show work I have done repeatedly: structuring projects, building visibility,
        documenting systems, surfacing risks, supporting decisions, and creating momentum across complex work.''', '''        These proof points show the kind of operating structure I create: project and program structure,
        workflow and operational systems, readiness and adoption, and reporting with follow-through.''', 'experience proof intro')
exp = replace_required(exp, '<h2>Structure for work in motion</h2>', '<h2>Case studies</h2>', 'experience case heading')
exp = replace_required(exp, '''        My project and process work builds the systems, artifacts, and rhythms teams need to see ownership,
        decisions, status, risks, dependencies, and next steps.''', '''        These case studies use the same pattern: the unclear starting point, what needed to become visible,
        the structure I built, how I brought people together, what changed, and what I learned.''', 'experience case intro')
exp = replace_required(exp, 'Personalized Learning Journey global pilot', 'Finding the Right Balance Between Automation and Human Judgment', 'experience PLJ title')
exp = replace_required(exp, '''            Led and project managed a global Personalized Learning Journey pilot with partners across training, analytics,
            exam operations, vendors, and readiness.''', '''            Led and project managed a global Personalized Learning Journey pilot comparing automation-only, human-led,
            and hybrid support models with partners across training, analytics, exam operations, vendor management,
            and internal teams.''', 'experience PLJ body')
exp = exp.replace('</div>\n        </div>\n\n        <div class="card pm-card">\n          <h3>Product support policy project</h3>', '</div>\n          <div class="button-row" style="margin-top: 20px;"><a class="button" href="plj-pilot.html">View Case Study</a></div>\n        </div>\n\n        <div class="card pm-card">\n          <h3>Product support policy project</h3>', 1)
exp = replace_required(exp, 'Product support policy project', 'From Manual Audits to Built-In Accountability', 'experience sonar title')
exp = replace_required(exp, '''            Coordinated early-stage product support policy work across approximately seven teams by creating project
            artifacts that tracked status, decisions, risks, and next steps.''', '''            Designed and led a Sonar audit program for ER and engineering escalations, creating the audit structure,
            surfacing systemic gaps, driving closure of 500+ tasks, and helping define requirements for automated
            assignment tracking.''', 'experience sonar body')
exp = exp.replace('<span class="tag">Co-PM</span>', '<span class="tag">Audit program</span>')
exp = exp.replace('<span class="tag">7 teams</span>', '<span class="tag">500+ tasks</span>')
exp = exp.replace('<span class="tag">Project artifacts</span>', '<span class="tag">Workflow controls</span>')
exp = exp.replace('<span class="tag">Status tracking</span>', '<span class="tag">Policy improvement</span>')
exp = exp.replace('<span class="tag">Decision visibility</span>', '<span class="tag">Requirements</span>')
exp = exp.replace('<span class="tag">Risk tracking</span>', '<span class="tag">Accountability</span>')
exp = exp.replace('</div>\n        </div>\n\n        <div class="card pm-card">\n          <h3>Wrike operating hub</h3>', '</div>\n          <div class="button-row" style="margin-top: 20px;"><a class="button" href="sonar-audit.html">View Case Study</a></div>\n        </div>\n\n        <div class="card pm-card">\n          <h3>Wrike operating hub</h3>', 1)
exp = replace_required(exp, 'Wrike operating hub', 'Workflow + operating hub', 'experience hub title')
exp = replace_required(exp, '''Built a Wrike operating hub that standardized intake, project setup, status visibility, repeatable workflows,
            and manager-facing reporting. The hub became part of a larger operating system for project visibility,
            including the capacity planning platform that connected planning data back to the team’s project management workflow.''', '''Built a workflow and operating hub that standardized intake, project setup, status visibility, repeatable workflows,
            and manager-facing reporting. The hub became part of a larger operating system for project visibility,
            including the capacity planning platform that connected planning data back to the team’s project management workflow.''', 'experience hub body')
exp = replace_required(exp, 'Capacity planning platform', 'Turning Fragmented Planning Into a Shared Operating View', 'experience capacity title')
exp = replace_required(exp, '''            Built a web-based capacity planning platform for a large project management organization, moving from stakeholder
            discovery to functional prototype in under two weeks. The platform helps leaders visualize monthly allocation,
            forecast overload, identify rebalancing opportunities, and sync project details with the team’s project management platform.''', '''            Lead Torque, an AI-assisted, full-stack capacity-planning app, from discovery through iterative delivery across
            4 manager organizations and approximately 7 teams. The in-progress platform helps leaders visualize monthly
            allocation, forecast overload, identify rebalancing opportunities, and connect project details with the team’s
            project management workflow.''', 'experience capacity body')
# Add two additional case cards before the grid closes in project-process.
needle = '''          <div class="button-row" style="margin-top: 20px;">
            <a class="button" href="capacity-planning.html">View Case Study</a>
          </div>
        </div>
      </div>
    </section>'''
addition = '''          <div class="button-row" style="margin-top: 20px;">
            <a class="button" href="capacity-planning.html">View Case Study</a>
          </div>
        </div>

        <div class="card pm-card">
          <h3>Building a Communications and Knowledge Function From Zero</h3>
          <p>
            Built the Senior Specialist Communications and knowledge-management function from zero, establishing policies,
            procedures, intake, ownership, leadership communications, and scalable support across a broader portfolio of
            20-25 spaces and hundreds of pages.
          </p>
          <div class="tag-list">
            <span class="tag">Function build</span>
            <span class="tag">Knowledge governance</span>
            <span class="tag">Platform migrations</span>
            <span class="tag">20-25 spaces</span>
          </div>
          <div class="button-row" style="margin-top: 20px;"><a class="button" href="communications-knowledge.html">View Case Study</a></div>
        </div>

        <div class="card pm-card">
          <h3>Designing Tool Adoption for a Distributed Workforce</h3>
          <p>
            Designed the Discovery Series, a modular, self-paced adoption model for two new work-management and collaboration
            platforms, combining hands-on practice, SME-led Q&A, scheduling guidance, and manager sign-off.
          </p>
          <div class="tag-list">
            <span class="tag">Readiness</span>
            <span class="tag">Tool adoption</span>
            <span class="tag">Distributed workforce</span>
            <span class="tag">Manager sign-off</span>
          </div>
          <div class="button-row" style="margin-top: 20px;"><a class="button" href="discovery-series.html">View Case Study</a></div>
        </div>
      </div>
    </section>'''
exp = replace_required(exp, needle, addition, 'experience add extra case cards')
# Nav wording generalization.
exp = exp.replace('<a href="capacity-planning.html">Capacity Case Study</a>', '<a href="capacity-planning.html">Capacity Planning</a>')
write(exp_path, exp)

# Update capacity page title/H1 to story title and in-progress language.
cap_path = Path('capacity-planning.html')
cap = read(cap_path)
cap = cap.replace('<title>Amber Largent | Capacity Planning Platform Case Study</title>', '<title>Amber Largent | Turning Fragmented Planning Into a Shared Operating View</title>')
cap = cap.replace('<h1>Capacity Planning Platform</h1>', '<h1>Turning Fragmented Planning Into a Shared Operating View</h1>')
cap = cap.replace('A web-based operational platform built to help leaders visualize project capacity, forecast overload,\n              and rebalance work before assignment issues became urgent.', 'An in-progress, AI-assisted capacity-planning platform built to help leaders visualize project capacity, forecast overload, and rebalance work before assignment issues become urgent.')
cap = cap.replace('Functional prototype built in under two weeks, with scope expanded from a single-team tool to an org-wide initiative.', 'In progress. Functional prototype built in under two weeks, with scope expanded from a single-team tool to an org-wide initiative.')
cap = cap.replace('© 2026 Amber Largent · Capacity Planning Platform Case Study', '© 2026 Amber Largent · Turning Fragmented Planning Into a Shared Operating View')
write(cap_path, cap)

# Update Tri-Parish case title for consistency while keeping project specificity.
tri_path = Path('triparish.html')
tri = read(tri_path)
tri = tri.replace('<title>Amber Largent | Tri-Parish Website Case Study</title>', '<title>Amber Largent | Taking a Multi-Parish Website From Idea to Launch</title>')
tri = tri.replace('<h1>Tri-Parish Website Redesign</h1>', '<h1>Taking a Multi-Parish Website From Idea to Launch</h1>')
tri = tri.replace('A launched website project taken from concept to completion: audience needs, site structure,\n              content strategy, build support, domain setup, and launch readiness.', 'A public-facing Tri-Parish website project taken from idea to launch: audience needs, site structure, content strategy, build support, domain setup, and launch readiness.')
tri = tri.replace('© 2026 Amber Largent · Tri-Parish Website Case Study', '© 2026 Amber Largent · Taking a Multi-Parish Website From Idea to Launch')
write(tri_path, tri)

# New case study pages.
write('plj-pilot.html', case_page(
    'Finding the Right Balance Between Automation and Human Judgment',
    'Project + Program Structure Case Study',
    'A global pilot comparing automation-only, human-led, and hybrid support models to find the strongest path for customer experience and operational improvement.',
    'Balancing automation with human judgment',
    'Pilot management • Data-informed decisions • Operational improvement',
    [('Global','pilot scope'),('Hybrid','strongest model'),('Meaningful','handling-time reduction'),('Improved','CSAT + resolution')],
    'From support-model questions to measurable pilot learning',
    'The starting point was not simply whether automation could help. The real question was where automation helped, where human support mattered, and which model produced the best operational and customer experience outcomes.',
    'I led and project managed a global Personalized Learning Journey pilot that compared automation-only, human-led, and hybrid support models with partners across training, analytics, exam operations, vendor management, and internal teams.',
    [('Role','Pilot project manager, partner coordinator, readiness supporter, and outcome translator.',''),('Scope','Global pilot coordination, stakeholder alignment, readiness planning, model comparison, and public-safe outcome reporting.','slate-card'),('Status','Completed pilot with public-safe results. Detailed metrics are available for internal review.','blush-card')],
    [('The best support model was unclear.','The team needed to compare support approaches without assuming automation alone would produce the strongest outcome.',''),('Success needed more than one measure.','The work needed to consider efficiency, customer satisfaction, issue resolution, readiness, and operational feasibility.','slate-card'),('Partners needed shared visibility.','Training, analytics, exam operations, vendor management, and internal teams needed a common view of what was changing and why.','blush-card'),('Results needed responsible handling.','The project produced measurable outcomes, but public portfolio language needed to protect internal details and exact metrics.','')],
    [('Clarified the support models','Compared automation-only, human-led, and hybrid approaches so the pilot could test real operating choices instead of a single assumed solution.'),('Coordinated cross-functional partners','Connected training, analytics, exam operations, vendor management, and internal teams around pilot needs, data, readiness, and follow-through.'),('Tracked signals across measures','Looked at customer experience and efficiency measures together so the work did not reduce success to a single number.'),('Improved the pilot approach','Designed and improved pilot additions, including elements that showed the strongest performance lift.'),('Translated outcomes responsibly','Kept public language high-level while preserving the ability to discuss detailed metrics in internal review settings.')],
    [('Project + program structure','Created pilot structure around models, partners, readiness needs, data review, and follow-through.',''),('Reporting + follow-through','Connected pilot outcomes to public-safe evidence while keeping detailed metrics available for internal review.','slate-card')],
    [('Cross-functional alignment','Brought together partners across training, analytics, exam operations, vendor management, and internal teams.',''),('Human judgment in the loop','Kept the pilot focused on where people added value, not only where automation could be applied.','slate-card')],
    [('What changed','The hybrid model delivered the strongest results, including a meaningful reduction in handling time and improvements in customer satisfaction and resolution measures.',''),('What it demonstrates','This case study shows how I manage pilots where data, human judgment, operational feasibility, and partner alignment all matter.','slate-card')],
    'Automation is strongest when it is treated as part of a system, not the whole system. The best operating model preserved human judgment where it mattered and used data to show which path worked best.',
    'Finding the Right Balance Between Automation and Human Judgment'
))

write('sonar-audit.html', case_page(
    'From Manual Audits to Built-In Accountability',
    'Workflow + Operational Systems Case Study',
    'An audit and workflow-control effort that moved a large backlog from manual review toward clearer ownership, stronger policy controls, and requirements for automation.',
    'Turning audit work into accountability',
    'Audit design • Workflow controls • Requirements for automation',
    [('500+','tasks closed'),('Systemic','gaps surfaced'),('Controls','strengthened'),('Automation','requirements defined')],
    'From hidden backlog risk to visible accountability',
    'The starting point was a backlog of records where eligibility, documentation, routing, ownership, and status were not visible enough to manage reliably. The work needed more than cleanup. It needed accountability built into the workflow.',
    'I designed and led a Sonar audit program for ER and engineering escalations, creating and training the audit team, reporting systemic gaps, driving closure of 500+ tasks, updating policies and workflow controls, and helping define requirements for automated assignment tracking.',
    [('Role','Audit-program designer, audit-team lead, process improver, and requirements partner.',''),('Scope','Audit structure, team training, backlog review, gap reporting, policy updates, workflow controls, and automation requirements.','slate-card'),('Status','Completed major cleanup and moved the work toward stronger built-in accountability.','blush-card')],
    [('The backlog was too hard to read.','Records existed, but the real ownership, status, and next steps were not visible enough to manage confidently.',''),('Manual review was doing too much work.','Audits were needed, but the workflow also needed controls that reduced avoidable manual follow-up.','slate-card'),('Gaps were systemic.','The issues pointed to eligibility, documentation, routing, ownership, and status patterns, not just one-off misses.','blush-card'),('Future automation needed real requirements.','The next step required a clearer understanding of what an assignment tool would need to track and support.','')],
    [('Defined the audit structure','Created the program structure needed to review records consistently and see patterns across the backlog.'),('Built and trained the audit team','Helped others understand what to look for and how to apply the audit approach consistently.'),('Made the gaps visible','Reported recurring eligibility, documentation, routing, ownership, and status issues so leaders could address the system, not only individual records.'),('Drove closure and process updates','Supported closure of 500+ tasks while strengthening policies and workflow controls.'),('Translated findings into automation requirements','Helped define requirements for automated assignment tracking so accountability could move closer to the workflow itself.')],
    [('Workflow + operational systems','Turned scattered audit needs into a structured program with clearer controls and follow-up.',''),('Reporting + follow-through','Used audit findings to surface patterns, support policy improvement, and move work toward closure.','slate-card')],
    [('Audit-team enablement','Created and trained the audit team so the work could scale beyond one person.',''),('Leader visibility','Made systemic gaps visible so leaders could make better decisions about process controls and future automation.','slate-card')],
    [('What changed','The work drove closure of 500+ tasks, strengthened policies and workflow controls, and helped define requirements for automated assignment tracking.',''),('What it demonstrates','This case study shows how I move work from manual cleanup toward built-in accountability and more sustainable operating controls.','slate-card')],
    'Manual audits can reveal the real system design problem. The strongest improvement was not only clearing records; it was using the audit to define better controls and future automation requirements.',
    'From Manual Audits to Built-In Accountability'
))

write('communications-knowledge.html', case_page(
    'Building a Communications and Knowledge Function From Zero',
    'Workflow + Operational Systems Case Study',
    'A function-building effort that turned scattered communications and knowledge needs into policies, procedures, intake, ownership, leadership communications, and scalable support.',
    'From scattered guidance to a scalable function',
    'Operating model • Knowledge governance • Platform migrations',
    [('Zero','to operating function'),('20-25','knowledge spaces'),('Hundreds','of pages'),('Multiple','platform migrations')],
    'From informal support to a sustainable communications and knowledge function',
    'The starting point was a need for clearer communications, knowledge governance, ownership, and support across a growing Senior Specialist organization. The work needed standards, maintainable pathways, and guidance people could trust.',
    'I built the Senior Specialist Communications and knowledge-management function from zero, establishing policies, procedures, intake, ownership, leadership communications, and scalable support across iOS, CPU, and the full Senior Specialist organization.',
    [('Role','Function builder, communications lead, knowledge manager, governance partner, and migration supporter.',''),('Scope','Policies, procedures, intake, ownership, leader communications, hours-compliant guidance, platform migrations, and knowledge-space governance.','slate-card'),('Status','Scaled support into a broader portfolio of 20-25 spaces and hundreds of pages.','blush-card')],
    [('The function did not exist yet.','The work needed an operating model before it could scale reliably.',''),('Knowledge needed ownership.','Guidance needed clear maintenance, review, and accountability so people could trust what they found.','slate-card'),('Platforms changed over time.','Content needed to move across knowledge platforms without losing structure, accuracy, or usability.','blush-card'),('Support needed to scale.','What started in smaller spaces needed to support a broader organization with consistent, aligned guidance.','')],
    [('Established the operating model','Created policies, procedures, intake, ownership, and leadership communication rhythms.'),('Built scalable guidance structures','Organized knowledge so users could find, trust, and apply information more consistently.'),('Governed platform migrations','Supported migrations across ConnectMe, Gather, and Chorus by cleaning, restructuring, and maintaining content through change.'),('Expanded organizational support','Scaled support from iOS and CPU into the broader Senior Specialist organization.'),('Maintained aligned guidance','Kept hours-compliant guidance and leadership communications aligned across a large knowledge portfolio.')],
    [('Workflow + operational systems','Built the function structure, intake, ownership model, and procedures needed to sustain the work.',''),('Readiness + adoption','Created communications and knowledge resources that helped people understand and apply guidance consistently.','slate-card')],
    [('Leadership communications','Created clearer pathways for leadership guidance and team-facing communication.',''),('Distributed knowledge users','Supported advisors, specialists, managers, leaders, project teams, and cross-functional partners through more usable knowledge systems.','slate-card')],
    [('What changed','A scattered need became a scalable communications and knowledge-management function with policies, procedures, intake, ownership, and platform support.',''),('What it demonstrates','This case study shows how I build operating functions, not just documents, and how I sustain knowledge through growth and platform change.','slate-card')],
    'Knowledge work is operating work. The value is not only having pages; it is creating ownership, governance, and structures people can trust when work changes.',
    'Building a Communications and Knowledge Function From Zero'
))

write('discovery-series.html', case_page(
    'Designing Tool Adoption for a Distributed Workforce',
    'Readiness + Adoption Case Study',
    'A modular, self-paced adoption model for new work-management and collaboration platforms, built for a distributed frontline support team.',
    'Making tool adoption repeatable',
    'Asynchronous learning • Hands-on practice • Manager accountability',
    [('2','platforms'),('Modular','self-paced model'),('SME','Q&A'),('Standard','for future rollouts')],
    'From tool rollout to repeatable adoption model',
    'The starting point was a distributed workforce that needed to adopt new work-management and collaboration platforms without relying only on one-time announcements or live training.',
    'I designed the Discovery Series, a modular, self-paced adoption model for two new work-management and collaboration platforms. The model combined hands-on practice, SME-led Q&A, scheduling guidance, and manager sign-off.',
    [('Role','Learning designer, readiness partner, adoption strategist, and facilitator.',''),('Scope','Self-paced modules, hands-on practice, SME-led Q&A, scheduling guidance, manager sign-off, and rollout support.','slate-card'),('Status','The model became the team’s standard for future tool rollouts.','blush-card')],
    [('The workforce was distributed.','People needed a way to learn and practice that worked across schedules and locations.',''),('Announcements were not enough.','The rollout needed active practice, support, and accountability, not only awareness.','slate-card'),('Managers needed a clear role.','Adoption depended on manager follow-up and sign-off, not only individual completion.','blush-card'),('The model needed to repeat.','The team needed a scalable pattern that could support future tool rollouts, not one custom effort.','')],
    [('Designed the adoption model','Built a modular, self-paced structure that made learning easier to schedule and complete.'),('Created hands-on practice','Included applied activities so users could practice real tool behaviors instead of only reading about features.'),('Connected SMEs and learners','Built in SME-led Q&A so questions could be answered close to the work.'),('Added manager accountability','Included scheduling guidance and manager sign-off so adoption had visible follow-through.'),('Created a repeatable standard','Built the model in a way the team could reuse for future tool rollouts.')],
    [('Readiness + adoption','Turned tool rollout into structured learning, practice, support, and manager follow-through.',''),('Reporting + follow-through','Used completion expectations, manager sign-off, and recurring support to make adoption visible.','slate-card')],
    [('SME partnership','Brought subject matter experts into the learning experience so answers stayed close to real use cases.',''),('Manager support','Gave managers a clear role in helping distributed teams complete and apply the change.','slate-card')],
    [('What changed','The Discovery Series became the team’s standard for future tool rollouts and created a more repeatable approach to distributed technology adoption.',''),('What it demonstrates','This case study shows how I design readiness systems that help people apply change, not just hear about it.','slate-card')],
    'Adoption is not a message. People need time, practice, support, and visible follow-through. A repeatable model makes change less dependent on heroic effort each time.',
    'Designing Tool Adoption for a Distributed Workforce'
))
