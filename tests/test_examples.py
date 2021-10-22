from pathlib import Path


def test_flask():
    from py_to_win_app import Project

    app_name = "flask-desktop"
    dist_path = Path().cwd() / "dist"
    dist_zip_file = dist_path / f"{app_name}.zip"

    if dist_zip_file.is_file():
        dist_zip_file.unlink()

    p = Project(path=f"examples/{app_name}", input_dir=".")
    p.build(python_version="3.9.7")
    p.make_dist(delete_build_dir=True)

    assert dist_zip_file.exists()


def test_fastapi():
    from py_to_win_app import Project

    app_name = "fastapi-desktop"
    dist_path = Path().cwd() / "dist"
    dist_zip_file = dist_path / f"{app_name}.zip"

    if dist_zip_file.is_file():
        dist_zip_file.unlink()

    p = Project(path=f"examples/{app_name}", input_dir=".")
    p.build(python_version="3.9.7")
    p.make_dist(delete_build_dir=True)

    assert dist_zip_file.exists()
