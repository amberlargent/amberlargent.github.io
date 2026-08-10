from pathlib import Path

path = Path('experience.html')
text = path.read_text(encoding='utf-8')

old = '''        <div class="card pm-card">
          <h3>Capacity planning platform</h3>
          <p>
            Built a web-based capacity planning platform for a large project management organization. The tool helps leaders
            balance workload across teams by visualizing monthly resource allocation, forecasting overload before it happens,
            and surfacing rebalancing opportunities across the org.
          </p>
          <p>
            Led discovery with stakeholders across four manager organizations, evaluated five solution paths, designed the
            interaction model, data architecture, and visual design system, and built and deployed a functional prototype in
            under two weeks using GenAI as an engineering partner.
          </p>
          <p>
            Created an API integration with the team’s project management platform to support project sync and managed scope
            expansion from a single-team tool to an org-wide initiative.
          </p>
          <div class="tag-list">
            <span class="tag">Large PM org</span>
            <span class="tag">4 manager orgs</span>
            <span class="tag">5 solution paths</span>
            <span class="tag">Under 2 weeks</span>
            <span class="tag">REST APIs</span>
            <span class="tag">GenAI-assisted build</span>
            <span class="tag">Project platform integration</span>
          </div>
        </div>

        <div class="card pm-card">
          <h3>Capacity planning feature set</h3>
          <p>
            Designed the platform around a monthly heat map with a 7-tier capacity color scale, portfolio-level utilization
            rollups, forward-looking overload alerts with cross-team availability suggestions, per-manager configurable views
            using progressive disclosure, multi-assignee allocation tracking, priority scoring for intake decisions, and
            contractor offload opportunity detection.
          </p>
          <div class="tag-list">
            <span class="tag">Heat map</span>
            <span class="tag">Utilization rollups</span>
            <span class="tag">Overload alerts</span>
            <span class="tag">Rebalancing</span>
            <span class="tag">Priority scoring</span>
            <span class="tag">Contractor offload</span>
          </div>
        </div>

        <div class="card pm-card">
          <h3>Why it matters</h3>
          <p>
            This project shows how I approach ambiguous operational problems: listen first, map the real workflow, test
            solution paths, build practical structure, and create tools that help leaders make better decisions faster.
          </p>
          <div class="tag-list">
            <span class="tag">Operational clarity</span>
            <span class="tag">Leadership decisions</span>
            <span class="tag">Workflow design</span>
            <span class="tag">Practical structure</span>
          </div>
        </div>'''

new = '''        <div class="card pm-card">
          <h3>Capacity planning platform</h3>
          <p>
            Built a web-based capacity planning platform for a large project management organization. The tool helps leaders
            balance workload across teams by visualizing monthly resource allocation, forecasting overload before it happens,
            and surfacing rebalancing opportunities across the org.
          </p>
          <p>
            <strong>Challenge:</strong> Leaders needed a clearer way to see capacity across teams, compare project load,
            and make assignment decisions before workload issues became urgent.
          </p>
          <p>
            <strong>Action:</strong> Led discovery with stakeholders across four manager organizations, evaluated five solution
            paths, designed the interaction model, data architecture, and visual design system, built and deployed a functional
            prototype in under two weeks using GenAI as an engineering partner, and created an API integration with the team’s
            project management platform to support project sync.
          </p>
          <p>
            <strong>Features:</strong> Monthly heat map with a 7-tier capacity color scale, portfolio-level utilization rollups,
            forward-looking overload alerts, cross-team availability suggestions, per-manager configurable views, multi-assignee
            allocation tracking, priority scoring for intake decisions, and contractor offload opportunity detection.
          </p>
          <p>
            <strong>Tools and methods:</strong> HTML/CSS/JavaScript, REST APIs, internal enterprise hosting, GitHub Enterprise,
            GenAI (Claude), and project management platform integration.
          </p>
          <p>
            <strong>Value:</strong> Managed scope expansion from a single-team tool to an org-wide initiative and created a
            practical operating tool that helps leaders make better project assignment decisions faster.
          </p>
          <div class="tag-list">
            <span class="tag">Case Study</span>
            <span class="tag">Capacity Planning</span>
            <span class="tag">4 Manager Orgs</span>
            <span class="tag">5 Solution Paths</span>
            <span class="tag">Under 2 Weeks</span>
            <span class="tag">REST APIs</span>
            <span class="tag">GitHub Enterprise</span>
            <span class="tag">GenAI (Claude)</span>
          </div>
        </div>'''

if old not in text:
    raise SystemExit('Expected multi-card capacity planning block not found')

text = text.replace(old, new)
path.write_text(text, encoding='utf-8')
