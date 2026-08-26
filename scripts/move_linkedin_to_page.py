from pathlib import Path
import re

path = Path("index.html")
text = path.read_text(encoding="utf-8")

text = text.replace('<a href="#linkedin">LinkedIn</a>', '<a href="linkedin.html">LinkedIn</a>')

pattern = r'\n\s*<section id="linkedin">.*?</section>\s*\n(?=\s*<section id="service">)'
text, removed = re.subn(pattern, "\n\n", text, count=1, flags=re.DOTALL)

if removed != 1:
    raise SystemExit("Expected one embedded LinkedIn section in index.html")

path.write_text(text, encoding="utf-8")
