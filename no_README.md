# py-to-win-app

## Make runnable apps from your python scripts!

TODO: description

## Installation

Install as dev dependency:

    poetry add --dev py-to-win-app

Or using pip:

    pip install py-to-win-app

## Usage

1. Make `requirements.txt` file:

    `pip freeze > requirements.txt`

    Using `poetry`:

    `poetry export -f requirements.txt -o requirements.txt --without-hashes`

1. In root directory of your project create file `build.py` with following content:

    ```python
    from py_to_win_app import Project

    project = Project(
        input_dir="my_project",  # directory where your source files are
        main_file="main.py"
    )

    project.build(python_version="3.9.7")
    project.make_dist()
    ```

1. Run `build.py`:

    `python build.py`

## Documentation

- [API documentation](https://github.com/ruslan-rv-ua/py-to-win-app/blob/markdown-docs/docs/py_to_win_app.md)

## Examples

1. Clone this repo:

    `git clone https://github.com/ruslan-rv-ua/py2winapp`

1. Execute any of `example-*.py`:

    ```
    python example-flask-desktop.py
    ```

    You can find runnable windows application in `build/flask-desktop` directory.
    Distribution `flask-desktop.zip`

#### More examples:

- [telecode](https://github.com/ruslan-rv-ua/telecode) — desktop wxPython application

## Credits

- inspired by [ClimenteA/pyvan](https://github.com/ClimenteA/pyvan#readme)
- some examples from [ClimenteA/flaskwebgui](https://github.com/ClimenteA/flaskwebgui)
