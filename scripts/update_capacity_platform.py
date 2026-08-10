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
          <strong>90-person</strong>
          <span>PM org capacity planning platform</span>
        </div>
        <div class="proof-stat">
          <strong>Wrike API</strong>
          <span>two-way project sync and operating hub</span>
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
            and manager-facing reporting. That hub became part of a larger operating system for project visibility,
            including a capacity planning platform tied directly to Wrike project data.
          </p>
          <div class="tag-list">
            <span class="tag">Wrike</span>
            <span class="tag">Intake</span>
            <span class="tag">Blueprints</span>
            <span class="tag">Automation</span>
            <span class="tag">Dashboards</span>
            <span class="tag">Operating hub</span>
          </div>
        </div>

        <div class="card pm-card">
          <h3>Capacity planning platform</h3>
          <p>
            Built a web-based capacity planning tool for a 90-person project management organization. The platform helps
            leadership balance workload across teams by visualizing monthly resource allocation, forecasting overload before
            it happens, and surfacing rebalancing opportunities across the org.
          </p>
          <p>
            Led discovery with stakeholders across four manager organizations, evaluated five solution paths, designed the
            interaction model, data architecture, and visual design system, and built and deployed a functional prototype in
            under two weeks using GenAI as an engineering partner.
          </p>
          <p>
            Created a Wrike API integration for two-way project sync and managed scope expansion from a single-team tool to
            an org-wide initiative.
          </p>
          <div class="tag-list">
            <span class="tag">90-person PM org</span>
            <span class="tag">Capacity planning</span>
            <span class="tag">Wrike API</span>
            <span class="tag">Two-way sync</span>
            <span class="tag">REST APIs</span>
            <span class="tag">GenAI build partner</span>
            <span class="tag">Shuri</span>
            <span class="tag">GitHub Enterprise</span>
          </div>
        </div>'''
)

# Add a concise feature card after the main capacity card if it is not already present.
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
            rollups, forward-looking overload alerts, cross-team availability suggestions, per-manager configurable views,
            multi-assignee allocation tracking, priority scoring for intake decisions, and contractor offload opportunity detection.
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
      </div>
    </section>'''
    text = text.replace(insert_after, new_block, 1)

path.write_text(text, encoding='utf-8')
