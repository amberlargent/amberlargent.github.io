from pathlib import Path
import re


def read(path):
    return Path(path).read_text(encoding='utf-8')


def write(path, text):
    Path(path).write_text(text, encoding='utf-8')


def replace_section(text, section_id, new_section):
    pattern = rf'<section id="{re.escape(section_id)}">.*?</section>'
    updated, count = re.subn(pattern, new_section, text, count=1, flags=re.S)
    if count != 1:
        raise RuntimeError(f'Could not replace section #{section_id}')
    return updated


def case_card(title, body, href):
    return f'''        <div class="card">
          <h3>{title}</h3>
          <p>{body}</p>
          <div class="button-row"><a class="button" href="{href}">View Case Study</a></div>
        </div>'''


def simple_case_page(title, eyebrow, lead, proof, start, visible, built, people, changed, learned):
    proof_html = ''.join(f'<div class="proof-item">{a}<span>{b}</span></div>' for a, b in proof)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Amber Largent | {title}</title>
  <style>
    :root {{ --sage:#CFD2B4; --blush:#F2C6D5; --pink:#E46FA1; --slate:#6A747E; --black:#030303; --white:#fffafc; }}
    a:focus-visible,.button:focus-visible {{ outline:4px solid var(--pink); outline-offset:4px; }}
    .skip-link {{ position:absolute; left:16px; top:-60px; background:var(--black); color:var(--white); padding:10px 14px; border-radius:999px; font-weight:900; z-index:100; }} .skip-link:focus {{ top:16px; }}
    * {{ box-sizing:border-box; }} html {{ scroll-behavior:smooth; }} body {{ margin:0; font-family:Arial,sans-serif; background:var(--sage); color:var(--black); line-height:1.6; }} a {{ color:inherit; }}
    .site-nav {{ position:sticky; top:0; z-index:20; background:rgba(255,250,252,.94); backdrop-filter:blur(12px); border-bottom:1px solid rgba(3,3,3,.08); }}
    .nav-inner {{ max-width:1120px; margin:0 auto; padding:16px 24px; display:flex; justify-content:space-between; align-items:center; gap:24px; }} .brand {{ font-weight:900; letter-spacing:-.02em; }} .brand span {{ display:block; color:var(--slate); font-size:13px; font-weight:700; }}
    .nav-links {{ display:flex; flex-wrap:wrap; gap:18px; font-size:14px; font-weight:800; }} .nav-links a {{ text-decoration:none; transition:color .15s ease; }} .nav-links a[href*='.html'],.nav-links a:hover {{ color:var(--pink); }} .nav-links a[href^='#'] {{ color:var(--slate); }}
    header {{ background:radial-gradient(circle at 18% 18%,rgba(242,198,213,.85),transparent 28%),radial-gradient(circle at 88% 82%,rgba(228,111,161,.24),transparent 30%),var(--sage); border-bottom:1px solid rgba(3,3,3,.08); }}
    .hero,section {{ max-width:1120px; margin:0 auto; padding-left:24px; padding-right:24px; }} .hero {{ padding-top:86px; padding-bottom:72px; }}
    .eyebrow {{ display:inline-block; background:rgba(255,250,252,.78); border:1px solid rgba(228,111,161,.4); border-radius:999px; padding:8px 14px; color:var(--slate); font-size:13px; font-weight:900; letter-spacing:.08em; text-transform:uppercase; margin-bottom:22px; }}
    h1 {{ font-size:clamp(44px,6vw,76px); line-height:.98; letter-spacing:-.055em; margin:0 0 24px; max-width:980px; }} h2 {{ font-size:clamp(34px,5vw,56px); line-height:1; letter-spacing:-.04em; margin:0 0 22px; }} .lead {{ font-size:21px; max-width:860px; margin:0 0 30px; color:#1c1c1c; }}
    section {{ margin-top:48px; margin-bottom:48px; padding-top:56px; padding-bottom:56px; background:rgba(255,250,252,.42); border:1px solid rgba(255,250,252,.7); border-radius:32px; box-shadow:0 18px 50px rgba(3,3,3,.10); }} .section-intro {{ max-width:860px; font-size:19px; color:#202020; margin-bottom:34px; }}
    .grid-2,.proof-strip {{ display:grid; gap:22px; align-items:start; }} .grid-2 {{ grid-template-columns:repeat(2,1fr); }} .proof-strip {{ grid-template-columns:repeat(4,1fr); }}
    .card,.summary-card {{ background:rgba(255,250,252,.88); border:1px solid rgba(228,111,161,.34); border-top:6px solid var(--pink); border-radius:24px; padding:26px; box-shadow:0 14px 34px rgba(3,3,3,.08); }} .summary-card {{ border-left:7px solid var(--pink); border-top:1px solid rgba(228,111,161,.34); padding:30px; }} .summary-card p {{ margin:0; font-size:22px; line-height:1.4; font-weight:800; letter-spacing:-.02em; }} .card h3 {{ margin:0 0 10px; font-size:24px; line-height:1.1; letter-spacing:-.02em; }} .card p {{ margin:0; }}
    .proof-item {{ background:rgba(255,250,252,.82); border:1px solid rgba(228,111,161,.34); border-radius:18px; padding:18px; font-weight:900; text-align:center; }} .proof-item span {{ display:block; color:var(--slate); font-size:13px; text-transform:uppercase; letter-spacing:.08em; margin-top:4px; }}
    .button-row {{ display:flex; flex-wrap:wrap; gap:14px; margin-top:28px; }} .button {{ display:inline-flex; align-items:center; justify-content:center; text-decoration:none; font-weight:900; padding:13px 20px; border-radius:999px; border:2px solid var(--black); background:var(--white); color:var(--black); box-shadow:0 6px 0 var(--black); }}
    footer {{ padding:34px 24px; text-align:center; background:var(--black); color:var(--blush); font-size:14px; }}
    @media (max-width:900px) {{ .nav-inner {{ align-items:flex-start; flex-direction:column; }} .grid-2,.proof-strip {{ grid-template-columns:1fr; }} section {{ margin:28px 14px; padding:40px 20px; }} }}
  </style>
</head>
<body>
  <a class="skip-link" href="#main">Skip to main content</a>
  <nav class="site-nav"><div class="nav-inner"><div class="brand">Amber Largent<span>Trusted to Bring Structure</span></div><div class="nav-links"><a href="index.html">Home</a><a href="experience.html">Work Evidence</a><a href="#starting-point">Starting Point</a><a href="#visible">Visibility</a><a href="#structure">Structure</a><a href="#people">People</a><a href="#outcome">Outcome</a><a href="index.html#contact">Contact</a></div></div></nav>
  <main id="main">
    <header><div class="hero"><div class="eyebrow">{eyebrow}</div><h1>{title}</h1><p class="lead">{lead}</p><div class="button-row"><a class="button" href="experience.html">Back to Work Evidence</a><a class="button" href="#outcome">View Outcome</a></div></div></header>
    <section id="starting-point"><h2>The unclear starting point</h2><p class="section-intro">{start}</p><div class="proof-strip">{proof_html}</div></section>
    <section id="visible"><h2>What needed to become visible</h2><div class="summary-card"><p>{visible}</p></div></section>
    <section id="structure"><h2>The structure I built</h2><div class="grid-2"><div class="card"><h3>Operating structure</h3><p>{built}</p></div><div class="card"><h3>Follow-through</h3><p>The work focused on practical systems people could use and sustain, not standalone artifacts.</p></div></div></section>
    <section id="people"><h2>How I brought people together</h2><div class="summary-card"><p>{people}</p></div></section>
    <section id="outcome"><h2>What changed</h2><div class="grid-2"><div class="card"><h3>Public-safe outcome</h3><p>{changed}</p></div><div class="card"><h3>What it proves</h3><p>This work shows how I turn unclear, cross-functional needs into visible, usable operating structure.</p></div></div></section>
    <section id="learning"><h2>What I learned</h2><div class="summary-card"><p>{learned}</p></div></section>
  </main>
  <footer><p>© 2026 Amber Largent · {title}</p></footer>
</body>
</html>'''

# Homepage refresh
index = read('index.html')
index = index.replace('<span>Clear paths through complex work</span>', '<span>Trusted to Bring Structure</span>')
index = index.replace('<div class="eyebrow">Clear paths through complex work</div>', '<div class="eyebrow">Trusted to Bring Structure</div>')
index = index.replace('I turn unclear work into visible, usable operating structure: the plans, workflows,\n          resources, reporting rhythms, and follow-through that help complex work move.', 'I turn unclear, cross-functional work into visible, usable operating structure: the plans,\n          workflows, resources, reporting rhythms, and follow-through that help complex work move.')
index = index.replace('My background spans project execution, learning enablement, knowledge systems, coaching,\n          reporting, and AI-assisted development and workflows, but the throughline is consistent: make the work clear,\n          make it usable, and help people act.', 'My work sits where people, process, and technology meet. I clarify what matters,\n          make ownership visible, connect the right partners, and build practical systems teams can use and sustain.')
index = replace_section(index, 'value', '''    <section id="value">
      <h2>Trusted to Bring Structure</h2>
      <p class="section-intro">I build four kinds of structure that help complex work become visible, usable, and easier to move forward.</p>
      <div class="grid-2">
        <div class="card"><h3>Project + Program Structure</h3><p>Plans, requirements, decisions, risks, dependencies, ownership, and operating rhythms that keep complex work moving.</p></div>
        <div class="card id-card"><h3>Workflow + Operational Systems</h3><p>Processes, controls, integrations, and human decision points that turn scattered work into a usable system.</p></div>
        <div class="card neutral-card"><h3>Readiness + Adoption</h3><p>Learning, communications, resources, and manager support that help people understand and apply change.</p></div>
        <div class="card"><h3>Reporting + Follow-Through</h3><p>Dashboards, audits, status rhythms, and action tracking that make progress, risks, and next steps visible.</p></div>
      </div>
    </section>''')
case_cards = '\n\n'.join([
    case_card('Finding the Right Balance Between Automation and Human Judgment', 'Cross-functional pilot management, data-informed decisions, and measurable operational improvement.', 'plj-pilot.html'),
    case_card('Turning Fragmented Planning Into a Shared Operating View', 'Capacity-planning discovery, technical partnership, integrations, and iterative development, clearly labeled as in progress.', 'capacity-planning.html'),
    case_card('From Manual Audits to Built-In Accountability', 'Audit design, backlog cleanup, policy improvement, workflow controls, and requirements for automation.', 'sonar-audit.html'),
    case_card('Building a Communications and Knowledge Function From Zero', 'Operating-model design, policy governance, platform migrations, and scalable support.', 'communications-knowledge.html'),
    case_card('Designing Tool Adoption for a Distributed Workforce', 'Asynchronous learning, hands-on practice, manager accountability, and repeatable change readiness.', 'discovery-series.html'),
    case_card('Taking a Multi-Parish Website From Idea to Launch', 'Public-facing concept-to-launch project leadership with visible work samples.', 'triparish.html'),
])
index = replace_section(index, 'evidence', f'''    <section id="evidence">
      <h2>Proof that the work moves</h2>
      <p class="section-intro">These case studies show the same pattern: clarify the need, make the work visible, build usable structure, bring people together, and move the work forward.</p>
      <div class="grid-3">
{case_cards}
      </div>
      <div class="button-row">
        <a class="button" href="experience.html">View Work Evidence</a>
        <a class="button" href="samples.html">View Proof Beyond the Role</a>
        <a class="button" href="values.html">View How I Work</a>
      </div>
    </section>''')
write('index.html', index)

# Work Evidence refresh
exp = read('experience.html')
exp = exp.replace('The throughline is practical leadership: understand what is happening, make the work visible,\n          build useful structure, and help teams move with clearer ownership and follow-through.', 'The throughline is operating structure: understand what is happening, make the work visible,\n          build systems people can use, and help teams move with clearer ownership and follow-through.')
exp = replace_section(exp, 'proof-snapshot', '''    <section id="proof-snapshot">
      <h2>Operating structure in practice</h2>
      <p class="section-intro">These proof points show the kind of operating structure I create: project and program structure, workflow and operational systems, readiness and adoption, and reporting with follow-through.</p>
      <div class="proof-grid">
        <div class="proof-stat"><strong>Global</strong><span>PLJ pilot with vendors in multiple countries</span></div>
        <div class="proof-stat"><strong>4 manager orgs</strong><span>stakeholder discovery and requirements</span></div>
        <div class="proof-stat"><strong>500+</strong><span>audit tasks closed</span></div>
        <div class="proof-stat"><strong>20-25</strong><span>knowledge spaces supported</span></div>
      </div>
    </section>''')
project_cards = f'''        <div class="card pm-card"><h3>Finding the Right Balance Between Automation and Human Judgment</h3><p>Led and project managed a global Personalized Learning Journey pilot comparing automation-only, human-led, and hybrid support models with partners across training, analytics, exam operations, vendor management, and internal teams.</p><div class="tag-list"><span class="tag">Global pilot</span><span class="tag">Hybrid model</span><span class="tag">Public-safe metrics</span></div><div class="button-row" style="margin-top: 20px;"><a class="button" href="plj-pilot.html">View Case Study</a></div></div>
        <div class="card pm-card"><h3>Turning Fragmented Planning Into a Shared Operating View</h3><p>Lead Torque, an AI-assisted, full-stack capacity-planning app, from discovery through iterative delivery across 4 manager organizations and approximately 7 teams. The in-progress platform helps leaders visualize monthly allocation, forecast overload, identify rebalancing opportunities, and connect project details with the team’s project management workflow.</p><div class="tag-list"><span class="tag">In progress</span><span class="tag">4 manager orgs</span><span class="tag">Approximately 7 teams</span><span class="tag">AI-assisted development</span></div><div class="button-row" style="margin-top: 20px;"><a class="button" href="capacity-planning.html">View Case Study</a></div></div>
        <div class="card pm-card"><h3>From Manual Audits to Built-In Accountability</h3><p>Designed and led a Sonar audit program for ER and engineering escalations, creating the audit structure, surfacing systemic gaps, driving closure of 500+ tasks, strengthening policies and workflow controls, and helping define requirements for automated assignment tracking.</p><div class="tag-list"><span class="tag">500+ tasks</span><span class="tag">Workflow controls</span><span class="tag">Automation requirements</span></div><div class="button-row" style="margin-top: 20px;"><a class="button" href="sonar-audit.html">View Case Study</a></div></div>
        <div class="card pm-card"><h3>Building a Communications and Knowledge Function From Zero</h3><p>Built the Senior Specialist Communications and knowledge-management function from zero, establishing policies, procedures, intake, ownership, leadership communications, and scalable support across a broader portfolio of 20-25 spaces and hundreds of pages.</p><div class="tag-list"><span class="tag">Function build</span><span class="tag">Knowledge governance</span><span class="tag">Platform migrations</span></div><div class="button-row" style="margin-top: 20px;"><a class="button" href="communications-knowledge.html">View Case Study</a></div></div>
        <div class="card pm-card"><h3>Designing Tool Adoption for a Distributed Workforce</h3><p>Designed the Discovery Series, a modular, self-paced adoption model for two new work-management and collaboration platforms, combining hands-on practice, SME-led Q&A, scheduling guidance, and manager sign-off.</p><div class="tag-list"><span class="tag">Readiness</span><span class="tag">Distributed workforce</span><span class="tag">Manager sign-off</span></div><div class="button-row" style="margin-top: 20px;"><a class="button" href="discovery-series.html">View Case Study</a></div></div>
        <div class="card pm-card"><h3>Taking a Multi-Parish Website From Idea to Launch</h3><p>Created and launched a public-facing website from concept to live site, showing the same structure-building pattern outside my Apple role with visible work samples.</p><div class="tag-list"><span class="tag">Public work sample</span><span class="tag">Concept to launch</span><span class="tag">Content strategy</span></div><div class="button-row" style="margin-top: 20px;"><a class="button" href="triparish.html">View Case Study</a></div></div>'''
exp = replace_section(exp, 'project-process', f'''    <section id="project-process">
      <h2>Case studies</h2>
      <p class="section-intro">These case studies use the same pattern: the unclear starting point, what needed to become visible, the structure I built, how I brought people together, what changed, and what I learned.</p>
      <div class="grid-2">
{project_cards}
      </div>
    </section>''')
exp = exp.replace('<a href="capacity-planning.html">Capacity Case Study</a>', '<a href="capacity-planning.html">Capacity Planning</a>')
write('experience.html', exp)

# Update existing case study titles.
cap = read('capacity-planning.html')
cap = cap.replace('<title>Amber Largent | Capacity Planning Platform Case Study</title>', '<title>Amber Largent | Turning Fragmented Planning Into a Shared Operating View</title>')
cap = cap.replace('<h1>Capacity Planning Platform</h1>', '<h1>Turning Fragmented Planning Into a Shared Operating View</h1>')
cap = cap.replace('A web-based operational platform built to help leaders visualize project capacity, forecast overload,\n              and rebalance work before assignment issues became urgent.', 'An in-progress, AI-assisted capacity-planning platform built to help leaders visualize project capacity, forecast overload, and rebalance work before assignment issues become urgent.')
cap = cap.replace('Functional prototype built in under two weeks, with scope expanded from a single-team tool to an org-wide initiative.', 'In progress. Functional prototype built in under two weeks, with scope expanded from a single-team tool to an org-wide initiative.')
write('capacity-planning.html', cap)

tri = read('triparish.html')
tri = tri.replace('<title>Amber Largent | Tri-Parish Website Case Study</title>', '<title>Amber Largent | Taking a Multi-Parish Website From Idea to Launch</title>')
tri = tri.replace('<h1>Tri-Parish Website Redesign</h1>', '<h1>Taking a Multi-Parish Website From Idea to Launch</h1>')
tri = tri.replace('A launched website project taken from concept to completion: audience needs, site structure,\n              content strategy, build support, domain setup, and launch readiness.', 'A public-facing Tri-Parish website project taken from idea to launch: audience needs, site structure, content strategy, build support, domain setup, and launch readiness.')
write('triparish.html', tri)

# New case-study pages.
write('plj-pilot.html', simple_case_page(
    'Finding the Right Balance Between Automation and Human Judgment',
    'Project + Program Structure Case Study',
    'A global pilot comparing automation-only, human-led, and hybrid support models to find the strongest path for customer experience and operational improvement.',
    [('Global','pilot'),('Hybrid','strongest model'),('Meaningful','AHT reduction'),('Improved','CSAT + resolution')],
    'The starting point was not simply whether automation could help. The real question was where automation helped, where human support mattered, and which model produced the best operational and customer experience outcomes.',
    'The pilot needed shared visibility into support models, partner readiness, operational signals, and the difference between efficiency gains and customer-experience gains.',
    'I created project structure around pilot models, partner coordination, readiness needs, data review, and follow-through. Public-facing metrics are generalized, with detailed results available for internal review.',
    'I connected partners across training, analytics, exam operations, vendor management, and internal teams so the pilot could move as one coordinated effort.',
    'The hybrid model delivered the strongest results, including meaningful reduction in handling time and improvements in customer satisfaction and resolution measures.',
    'Automation is strongest when it is treated as part of a system, not the whole system. The best operating model preserved human judgment where it mattered and used data to show which path worked best.'
))
write('sonar-audit.html', simple_case_page(
    'From Manual Audits to Built-In Accountability',
    'Workflow + Operational Systems Case Study',
    'An audit and workflow-control effort that moved a large backlog from manual review toward clearer ownership, stronger policy controls, and requirements for automation.',
    [('500+','tasks closed'),('Systemic','gaps surfaced'),('Controls','strengthened'),('Automation','requirements defined')],
    'The starting point was a backlog of records where eligibility, documentation, routing, ownership, and status were not visible enough to manage reliably.',
    'The work needed to make ownership, status, eligibility, documentation gaps, routing issues, and next steps visible across a large set of records.',
    'I designed and led the audit program, created and trained the audit team, reported systemic gaps, strengthened policies and workflow controls, and helped define requirements for automated assignment tracking.',
    'I trained the audit team and helped leaders see the difference between individual task cleanup and the larger accountability model that needed to change.',
    'The work drove closure of 500+ tasks, strengthened policies and workflow controls, and helped define requirements for automated assignment tracking.',
    'Manual audits can reveal the real system design problem. The strongest improvement was not only clearing records; it was using the audit to define better controls and future automation requirements.'
))
write('communications-knowledge.html', simple_case_page(
    'Building a Communications and Knowledge Function From Zero',
    'Workflow + Operational Systems Case Study',
    'A function-building effort that turned scattered communications and knowledge needs into policies, procedures, intake, ownership, leadership communications, and scalable support.',
    [('Zero','to function'),('20-25','knowledge spaces'),('Hundreds','of pages'),('Multiple','platform migrations')],
    'The starting point was a need for clearer communications, knowledge governance, ownership, and support across a growing Senior Specialist organization.',
    'The work needed to make intake, ownership, guidance, leadership communication, knowledge status, and platform migration needs visible.',
    'I established policies, procedures, intake, ownership, leadership communications, and scalable support across a broader portfolio of 20-25 spaces and hundreds of pages.',
    'I supported advisors, specialists, managers, leaders, project teams, and cross-functional partners through clearer communications and more sustainable knowledge systems.',
    'A scattered need became a scalable communications and knowledge-management function with policies, procedures, intake, ownership, and platform support.',
    'Knowledge work is operating work. The value is not only having pages; it is creating ownership, governance, and structures people can trust when work changes.'
))
write('discovery-series.html', simple_case_page(
    'Designing Tool Adoption for a Distributed Workforce',
    'Readiness + Adoption Case Study',
    'A modular, self-paced adoption model for new work-management and collaboration platforms, built for a distributed frontline support team.',
    [('2','platforms'),('Modular','self-paced model'),('SME','Q&A'),('Standard','future rollouts')],
    'The starting point was a distributed workforce that needed to adopt new work-management and collaboration platforms without relying only on one-time announcements or live training.',
    'The work needed to make learner needs, practice expectations, SME support, scheduling, manager accountability, and completion visible.',
    'I designed a modular, self-paced adoption model with hands-on practice, SME-led Q&A, scheduling guidance, and manager sign-off.',
    'I connected learners, SMEs, and managers so adoption had practice, support, and visible follow-through.',
    'The model became the team’s standard for future tool rollouts and created a more repeatable approach to distributed technology adoption.',
    'Adoption is not a message. People need time, practice, support, and visible follow-through. A repeatable model makes change less dependent on heroic effort each time.'
))
