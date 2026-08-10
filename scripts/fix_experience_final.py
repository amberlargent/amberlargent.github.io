from pathlib import Path

p = Path('experience.html')
text = p.read_text(encoding='utf-8')
text = text.replace(
    '<h2>Daily AI workflow design, not just AI interest</h2>',
    '<h2>AI-supported workflow design, not AI theater</h2>'
)
text = text.replace(
'''        Two direct-manager recommendation letters are available and speak to my integrity, follow-through,
        curiosity, problem identification, process improvement, and willingness to step into complex work.''',
'''        Two direct-manager recommendation letters are available and speak to my integrity, follow-through,
        curiosity, problem identification, process improvement, and willingness to step into complex work.
        Exact excerpts can be added here once the public-safe quote text is selected.'''
)
p.write_text(text, encoding='utf-8')
