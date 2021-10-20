from lazydocs import generate_docs
from pathlib import Path
import markdown2

md_file = Path("./docs/py_to_win_app.Project.md")
html_template_file = Path("./docs/templates/bootstrap.html")
index_html_file = Path("./docs/index.html")

generate_docs(["py_to_win_app.Project"], output_path="./docs")

md_text = md_file.read_text(encoding="utf8")
docs_html = markdown2.markdown(md_text, extras=['fenced-code-blocks'])

html_template = html_template_file.read_text(encoding="utf8")
html = html_template.format(html=docs_html)

index_html_file.write_text(html, encoding="utf8")

md_file.unlink()

print('Documentation updated! Now you can add it to commit.')
