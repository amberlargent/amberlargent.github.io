from pathlib import Path

p = Path('index.html')
text = p.read_text(encoding='utf-8')
text = text.replace(
'''        <p class="lead">
          I help teams turn unclear work into structure, movement, and follow-through.
        </p>

        <p class="lead">
          I help teams turn unclear work into visible, usable operating structure: the plans, workflows,
          resources, reporting rhythms, and follow-through that help complex work move.
        </p>''',
'''        <p class="lead">
          I turn unclear work into visible, usable operating structure: the plans, workflows,
          resources, reporting rhythms, and follow-through that help complex work move.
        </p>''')
text = text.replace(
'''          <div class="stat"><strong>PM</strong><span>Project + Process</span></div>
          <div class="stat"><strong>L&D</strong><span>Learning + Enablement</span></div>
          <div class="stat"><strong>AI</strong><span>Knowledge + Workflow</span></div>''',
'''          <div class="stat"><strong>Structure</strong><span>Projects + Process</span></div>
          <div class="stat"><strong>Enablement</strong><span>Learning + Adoption</span></div>
          <div class="stat"><strong>Visibility</strong><span>Reporting + Knowledge</span></div>''')
p.write_text(text, encoding='utf-8')
