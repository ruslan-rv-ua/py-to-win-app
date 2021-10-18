<!-- markdownlint-disable -->

<a href="..\py_to_win_app#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `py_to_win_app`






---

<a href="..\py_to_win_app\Project#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Project`




<a href="..\py_to_win_app\__init__#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(input_dir: str, main_file: str, app_name: str = None) → None
```






---

#### <kbd>property</kbd> app_name





---

#### <kbd>property</kbd> build_path





---

#### <kbd>property</kbd> dist_path





---

#### <kbd>property</kbd> exe_path





---

#### <kbd>property</kbd> input_path





---

#### <kbd>property</kbd> path





---

#### <kbd>property</kbd> pydist_path





---

#### <kbd>property</kbd> requirements_path





---

#### <kbd>property</kbd> source_path







---

<a href="..\py_to_win_app\build#L356"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `build`

```python
build(
    python_version: str,
    pydist_dir: str = 'pydist',
    requirements_file: str = 'requirements.txt',
    extra_pip_install_args: Iterable[str] = (),
    build_dir: str = None,
    source_dir: str = None,
    show_console: bool = False,
    exe_name: str = None,
    icon_file: Optional[str, Path] = None
) → None
```





---

<a href="..\py_to_win_app\delete_build#L446"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `delete_build`

```python
delete_build() → None
```





---

<a href="..\py_to_win_app\make_dist#L431"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `make_dist`

```python
make_dist(file_name: str = None) → Path
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
