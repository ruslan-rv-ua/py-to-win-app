from py_to_win_app import Project

app_name = "pb-ccy-rates"

Project.from_pyproject(
    pyproject_toml=f"examples/{app_name}/pyproject.toml", input_dir="."
).build(
    python_version="3.9.7",
    pydist_dir="code",
    source_dir="code",
    show_console=True,
    exe_file_name="rates",
)
