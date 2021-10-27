<!-- markdownlint-disable -->

<a href="..\py_to_win_app\py_to_win_app.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `py_to_win_app`






---

<a href="..\py_to_win_app\py_to_win_app.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Project`




<a href="..\py_to_win_app\py_to_win_app.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Project.__init__`

```python
__init__(
    path: Union[str, pathlib.Path] = '',
    name: str = '',
    version: str = '',
    input_dir: str = '',
    main_file: str = '',
    requirements: Union[Iterable[str], str, pathlib.Path] = 'requirements.txt',
    extra_pip_install_args: Iterable[str] = ()
) → None
```

TODO



**Args:**

 - <b>`name`</b> (str, optional):  App's name. If `None` then project's folder name will be used. Defaults to `None`.
 - <b>`version`</b> (str, optional):  App's version. Defaults to `None`.
 - <b>`input_dir`</b> (str):  Directory where your source files are.
 - <b>`main_file`</b> (str):  Path to entry point, e.g. `main.py`


---

#### <kbd>property</kbd> Project.build_path





---

#### <kbd>property</kbd> Project.dist_path





---

#### <kbd>property</kbd> Project.exe_path





---

#### <kbd>property</kbd> Project.full_name

<name>-<version>

---

#### <kbd>property</kbd> Project.input_path





---

#### <kbd>property</kbd> Project.name





---

#### <kbd>property</kbd> Project.path





---

#### <kbd>property</kbd> Project.pydist_path





---

#### <kbd>property</kbd> Project.source_path





---

#### <kbd>property</kbd> Project.version







---

<a href="..\py_to_win_app\py_to_win_app.py#L146"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Project.build`

```python
build(
    python_version: str,
    build_path: Union[str, pathlib.Path] = '',
    source_dir: str = '',
    pydist_dir: str = '',
    download_dir: Union[str, pathlib.Path] = '',
    extract_pythonzip: bool = <class 'tkinter.tix.Tree'>,
    show_console: bool = False,
    exe_file_name: str = None,
    icon_file: Optional[str, pathlib.Path] = None
) → None
```

TODO



**Args:**

 - <b>`python_version`</b> (str):  Embedded python version
 - <b>`requirements_file`</b> (str, optional):  Path to `requirements.txt` file. Defaults to `"requirements.txt"`.
 - <b>`extra_pip_install_args`</b> (Iterable[str], optional):  Arguments to be appended to the `pip install` command during installation of requirements. Defaults to `()`.
 - <b>`build_dir`</b> (str, optional):  Directory to place build to. If `None` then `app_name` attribute will be used. Defaults to `None`.
 - <b>`pydist_dir`</b> (str, optional):  Subdirectory where to place Python embedde interpreter. Defaults to `"pydist"`.
 - <b>`source_dir`</b> (str, optional):  Subdirectory where to place source code. If `None` then `app_nam` attribute will be used. Defaults to `None`.
 - <b>`show_console`</b> (bool, optional):  Show console window or not. Defaults to `False`.
 - <b>`exe_name`</b> (str, optional):  Name of `.exe` file.  If `None` then name will be the same as `main_file`.  Defaults to `None`.  So if there be another paragraph?  * item 1  * item 2  One line.
 - <b>`icon_file`</b> (Union[str, Path, None], optional):  Path to icon file. Defaults to `None`.



**Raises:**

 - <b>`InvalidPythonVersion`</b>:  If incorrect Python version provided.

---

<a href="..\py_to_win_app\py_to_win_app.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `Project.from_pyproject`

```python
from_pyproject(
    pyproject_toml: Union[str, pathlib.Path] = 'pyproject.toml',
    input_dir: str = '',
    main_file: str = '',
    extra_pip_install_args: Iterable[str] = ()
) → Project
```





---

<a href="..\py_to_win_app\py_to_win_app.py#L265"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Project.make_dist`

```python
make_dist(
    file_name: Optional[str] = None,
    delete_build_dir: bool = False
) → Path
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
