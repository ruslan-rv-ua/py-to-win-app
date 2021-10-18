# py-to-win-app

## Make runnable apps from your python scripts!

TODO: description

## Usage

In the root directory of your project:

1. Install:

    `pip install py-to-win-app`

    Using `poetry`:

    `poetry add --dev py-to-win-app`

1. Make `requirements.txt` file:

    `pip freeze > requirements.txt`

    Using `poetry`:

    `poetry export -f requirements.txt -o requirements.txt --without-hashes`

1. Create fiel `build.py` with following content:

    ```python
    from py_to_win_app import Project

    project = Project(
        input_dir="my-project",  # directory where your source files are
        main_file="main.py"
    )

    project.build(python_version="3.9.7")
    project.make_dist()
    ```

1. Run `build.py`:

    `python build.py`

## Documentation

- [API documentation](http://ruslan.rv.ua/py-to-win-app/)

## Examples

1. Clone this repo:

    `git clone https://github.com/ruslan-rv-ua/py2winapp`

1. Execute any of `example-*.py`:

    ```
    python example-flask-desktop.py
    ```

    You can find runnable windows application in `build/flask-desktop` directory.
    Distribution `flask-desktop.zip`

More examples:

- [telecode](https://github.com/ruslan-rv-ua/telecode) — desktop wxPython application

## Credits

- inspired by [ClimenteA/pyvan](https://github.com/ClimenteA/pyvan#readme)
- some examples from [ClimenteA/flaskwebgui](https://github.com/ClimenteA/flaskwebgui)
