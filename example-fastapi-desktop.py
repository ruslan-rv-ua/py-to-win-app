from py_to_win_app import Project

app_name = "fastapi-desktop"

p = Project(path=f"examples/{app_name}", input_dir='.')

p.build(
    python_version="3.9.7",
    exe_name=app_name,
)
p.make_dist()
