from py_to_win_app import Project

app_name = "fastapi-desktop"

p = Project(
    input_dir=f"examples/{app_name}", main_file="main.py", app_name=app_name
)

p.build(
    python_version="3.9.7",
    requirements_file=f"examples/{app_name}/requirements.txt",
)
print(">>>")
