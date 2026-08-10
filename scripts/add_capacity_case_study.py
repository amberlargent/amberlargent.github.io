from pathlib import Path

# Update Work Evidence tools line / tags for the Capacity Planning Platform.
exp = Path('experience.html')
text = exp.read_text(encoding='utf-8')
old = '''          <div class="tag-list">
            <span class="tag">Large PM org</span>
            <span class="tag">4 manager orgs</span>
            <span class="tag">5 solution paths</span>
            <span class="tag">Under 2 weeks</span>
            <span class="tag">REST APIs</span>
            <span class="tag">GenAI-assisted build</span>
            <span class="tag">Project platform integration</span>
          </div>'''
new = '''          <p>
            <strong>Tools and methods:</strong> HTML/CSS/JavaScript, REST APIs, internal enterprise hosting,
            GitHub Enterprise, GenAI (Claude), and project management platform integration.
          </p>
          <div class="tag-list">
            <span class="tag">Large PM org</span>
            <span class="tag">4 manager orgs</span>
            <span class="tag">5 solution paths</span>
            <span class="tag">Under 2 weeks</span>
            <span class="tag">HTML/CSS/JavaScript</span>
            <span class="tag">REST APIs</span>
            <span class="tag">GitHub Enterprise</span>
            <span class="tag">GenAI (Claude)</span>
          </div>'''
if old not in text:
    raise SystemExit('Expected capacity platform tag block not found in experience.html')
text = text.replace(old, new)
exp.write_text(text, encoding='utf-8')

# Add Capacity Planning Platform as a second featured case-study-level project on Proof Beyond the Role.
samples = Path('samples.html')
text = samples.read_text(encoding='utf-8')
if 'Capacity Planning Platform' not in text:
    anchor = '''        </article>

        <article class="sample-card learning-card">
          <div class="category">Community Learning Design</div>'''
    block = '''        </article>

        <article class="sample-card featured-sample technology-card">
          <div class="category">Featured Operational Platform</div>
          <h3>Capacity Planning Platform</h3>
          <p>
            Built a web-based capacity planning platform for a large project management organization, using GenAI-assisted development to move from stakeholder discovery to functional prototype in under two weeks.
          </p>
          <p>
            The platform helps leaders visualize monthly resource allocation, forecast overload, identify rebalancing opportunities, and sync project details with the team’s project management platform.
          </p>
          <h4>Skills demonstrated</h4>
          <p>
            Stakeholder discovery, solution evaluation, interaction design, data architecture, visual design systems, REST API integration, GenAI-assisted development, and operational product thinking.
          </p>
          <div class="tag-list">
            <span class="tag">Case Study</span>
            <span class="tag">Capacity Planning</span>
            <span class="tag">4 Manager Orgs</span>
            <span class="tag">5 Solution Paths</span>
            <span class="tag">Under 2 Weeks</span>
            <span class="tag">REST APIs</span>
            <span class="tag">GenAI (Claude)</span>
          </div>
          <div class="approach">
            <p><strong>Challenge:</strong> Leaders needed a clearer way to see capacity across teams, compare project load, and make assignment decisions before workload issues became urgent.</p>
            <p><strong>Action:</strong> Led stakeholder discovery, evaluated solution paths, designed the interaction model and data structure, built a functional prototype, and connected the platform to the team’s project management workflow.</p>
            <p><strong>Value:</strong> Created a practical operating tool that helps leaders forecast overload, identify rebalancing opportunities, and make better project assignment decisions faster.</p>
          </div>
          <div class="sample-actions">
            <a class="button" href="experience.html#project-process">View Work Evidence</a>
          </div>
        </article>

        <article class="sample-card learning-card">
          <div class="category">Community Learning Design</div>'''
    if anchor not in text:
        raise SystemExit('Expected insertion anchor not found in samples.html')
    text = text.replace(anchor, block)
samples.write_text(text, encoding='utf-8')
