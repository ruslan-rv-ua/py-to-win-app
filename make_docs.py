from lazydocs import generate_docs
from pathlib import Path
import markdown

generate_docs(["py_to_win_app.Project"], output_path="./docs")

md_file = Path("./docs/py_to_win_app.Project.md")
md_text = md_file.read_text(encoding="utf8")
md = markdown.Markdown(extensions=["codehilite"])
md.set_output_format("html")
docs_html = md.convert(md_text)

html_file = Path("./docs/templates/bootstrap.html")
html_template = html_file.read_text(encoding="utf8")
html = html_template.format(html=docs_html)

Path("./docs/index.html").write_text(html, encoding="utf8")
