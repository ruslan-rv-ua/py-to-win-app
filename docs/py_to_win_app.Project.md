<!-- markdownlint-disable -->

<a href="..\py_to_win_app\py_to_win_app\Project#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>class</kbd> `Project`




<a href="..\py_to_win_app\py_to_win_app\__init__#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Project.__init__`

```python
__init__(input_dir: str, main_file: str, app_name: str = None) → None
```

TODO



**Args:**

 - <b>`input_dir`</b> (str):  Directory where your source files are.
 - <b>`main_file`</b> (str):  Path to entry point, e.g. `main.py`
 - <b>`app_name`</b> (str, optional):  App's name. If `None` then project's directory name will be used. Defaults to `None`.


---

### <kbd>property</kbd> Project.app_name





---

### <kbd>property</kbd> Project.build_path





---

### <kbd>property</kbd> Project.dist_path





---

### <kbd>property</kbd> Project.exe_path





---

### <kbd>property</kbd> Project.input_path





---

### <kbd>property</kbd> Project.path





---

### <kbd>property</kbd> Project.pydist_path





---

### <kbd>property</kbd> Project.requirements_path





---

### <kbd>property</kbd> Project.source_path







---

<a href="..\py_to_win_app\py_to_win_app\build#L363"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.build`

```python
build(
    python_version: str,
    requirements_file: str = 'requirements.txt',
    extra_pip_install_args: Iterable[str] = (),
    build_dir: str = None,
    pydist_dir: str = 'pydist',
    source_dir: str = None,
    show_console: bool = False,
    exe_name: str = None,
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
 - <b>`exe_name`</b> (str, optional):  Name of `.exe` file. If `None` then name will be the same as `main_file`. Defaults to `None`.
 - <b>`icon_file`</b> (Union[str, Path, None], optional):  Path to icon file. Defaults to `None`.



**Raises:**

 - <b>`ValueError`</b>:  If wrong Python version provided.

---

<a href="..\py_to_win_app\py_to_win_app\delete_build#L469"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.delete_build`

```python
delete_build() → None
```





---

<a href="..\py_to_win_app\py_to_win_app\make_dist#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.make_dist`

```python
make_dist(file_name: str = None) → Path
```







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
