from lazydocs import generate_docs
from pathlib import Path
import markdown2

generate_docs(["py_to_win_app.Project"], output_path="./docs")

md_file = Path("./docs/py_to_win_app.Project.md")
md_text = md_file.read_text(encoding="utf8")
docs_html = markdown2.markdown(md_text, extras=['fenced-code-blocks'])

html_file = Path("./docs/templates/bootstrap.html")
html_template = html_file.read_text(encoding="utf8")
html = html_template.format(html=docs_html)

Path("./docs/index.html").write_text(html, encoding="utf8")
