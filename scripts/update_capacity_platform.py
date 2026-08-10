from pathlib import Path

path = Path('experience.html')
text = path.read_text(encoding='utf-8')

text = text.replace(
'''        <div class="proof-stat">
          <strong>7 teams</strong>
          <span>early product policy project involvement</span>
        </div>
        <div class="proof-stat">
          <strong>Wrike</strong>
          <span>forms, blueprints, automations, dashboards</span>
        </div>''',
'''        <div class="proof-stat">
          <strong>4 manager orgs</strong>
          <span>stakeholder discovery and requirements</span>
        </div>
        <div class="proof-stat">
          <strong>2 weeks</strong>
          <span>discovery to functional prototype</span>
        </div>'''
)

text = text.replace(
'''          <h3>Wrike project hub</h3>
          <p>
            Built a Wrike operating hub that standardized intake, project setup, status visibility, repeatable workflows,
            and manager-facing reporting. The goal was not tool administration; it was to reduce ambiguity, make ownership
            visible, and give leaders a clearer view of work in motion. I have also built similar project and workflow
            structures in prior roles when teams needed a clearer way to manage the work.
          </p>
          <div class="tag-list">
            <span class="tag">Wrike</span>
            <span class="tag">Forms</span>
            <span class="tag">Blueprints</span>
            <span class="tag">Automation</span>
            <span class="tag">Dashboards</span>
            <span class="tag">Reusable structures</span>
          </div>
        </div>

        <div class="card pm-card">
          <h3>Portfolio visibility + capacity planning</h3>
          <p>
            Maintained planning and portfolio visibility for a broad AppleCare portfolio through recurring updates,
            portfolio data maintenance, and visibility support. I also built a working manager capacity planning prototype
            to help visualize workload, availability, and planning needs.
          </p>
          <div class="tag-list">
            <span class="tag">Portfolio support</span>
            <span class="tag">Recurring updates</span>
            <span class="tag">Data maintenance</span>
            <span class="tag">Capacity planning</span>
            <span class="tag">Visibility</span>
          </div>
        </div>''',
'''          <h3>Wrike operating hub</h3>
          <p>
            Built a Wrike operating hub that standardized intake, project setup, status visibility, repeatable workflows,
            and manager-facing reporting. The hub became part of a larger operating system for project visibility,
            including the capacity planning platform that connected planning data back to the team’s project management workflow.
          </p>
          <div class="tag-list">
            <span class="tag">Project intake</span>
            <span class="tag">Blueprints</span>
            <span class="tag">Automation</span>
            <span class="tag">Dashboards</span>
            <span class="tag">Operating hub</span>
            <span class="tag">Project sync</span>
          </div>
        </div>

        <div class="card pm-card">
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
        </div>'''
)

marker = '''        <div class="card pm-card">
          <h3>Capacity planning platform</h3>'''
if 'Capacity planning feature set' not in text and marker in text:
    insert_after = '''          </div>
        </div>
      </div>
    </section>'''
    new_block = '''          </div>
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
        </div>
      </div>
    </section>'''
    text = text.replace(insert_after, new_block, 1)

path.write_text(text, encoding='utf-8')
