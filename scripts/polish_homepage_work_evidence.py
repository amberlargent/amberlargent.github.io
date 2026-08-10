from pathlib import Path

replacements = {
    'index.html': [
        (
            'My background spans project execution, learning enablement, knowledge systems, coaching,\n          reporting, and AI-supported workflows, but the throughline is consistent: make the work clear,',
            'My background spans project execution, learning enablement, knowledge systems, coaching,\n          reporting, and AI-assisted development and workflows, but the throughline is consistent: make the work clear,'
        ),
        (
            '<a class="button" href="experience.html">View Work Evidence</a>\n        <a class="button" href="capacity-planning.html">View Capacity Case Study</a>',
            '<a class="button" href="experience.html">View Work Evidence</a>\n          <a class="button" href="capacity-planning.html">View Capacity Case Study</a>'
        ),
        (
            '<h2>Where I create value</h2>',
            '<h2>How I Bring Structure</h2>'
        ),
        (
            '<p>Create ownership, timelines, decisions, risks, dependencies, project artifacts, and follow-through for complex work.</p>',
            '<p>Clarify ownership, timelines, decisions, risks, dependencies, project artifacts, and follow-through for complex work.</p>'
        ),
        (
            '<p>Spearheaded and led a global Personalized Learning Journey pilot with partners across training, analytics, exam operations, vendors, and readiness.</p>',
            '<p>Led and project managed a global Personalized Learning Journey pilot with partners across training, analytics, exam operations, vendors, and readiness.</p>'
        ),
    ],
    'experience.html': [
        (
            'portfolio visibility, reporting rhythms, stakeholder alignment, risk identification, Wrike systems,\n          AI workflow design, and knowledge systems.',
            'portfolio visibility, reporting rhythms, stakeholder alignment, risk identification, Wrike systems,\n          AI-assisted development, workflow design, and knowledge systems.'
        ),
        (
            'Spearheaded and led a global Personalized Learning Journey pilot with partners across training, analytics,\n            exam operations, vendors, and readiness.',
            'Led and project managed a global Personalized Learning Journey pilot with partners across training, analytics,\n            exam operations, vendors, and readiness.'
        ),
        (
            '<h2>Daily AI workflow design, not just AI interest</h2>',
            '<h2>Daily AI-assisted workflow design, not just AI interest</h2>'
        ),
        (
            'This is not proprietary LLM infrastructure; it is practical workflow\n            design that makes AI-supported work more repeatable and easier to hand off.',
            'This is not proprietary LLM infrastructure; it is practical workflow\n            design that makes AI-assisted work more repeatable and easier to hand off.'
        ),
    ],
}

for filename, pairs in replacements.items():
    path = Path(filename)
    text = path.read_text(encoding='utf-8')
    for old, new in pairs:
        if old not in text:
            raise SystemExit(f'Missing expected text in {filename}: {old[:80]!r}')
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')
