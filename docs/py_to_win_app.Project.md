<!-- markdownlint-disable -->

<a href="..\py_to_win_app\py_to_win_app\Project#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>class</kbd> `Project`




<a href="..\py_to_win_app\py_to_win_app\__init__#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `Project.__init__`

```python
__init__(input_dir: str, main_file: str, app_name: str = None) → None
```






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

<a href="..\py_to_win_app\py_to_win_app\build#L357"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.build`

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
    icon_file: Optional[str, pathlib.Path] = None
) → None
```





---

<a href="..\py_to_win_app\py_to_win_app\delete_build#L447"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.delete_build`

```python
delete_build() → None
```





---

<a href="..\py_to_win_app\py_to_win_app\download_file#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.download_file`

```python
download_file(
    url: str,
    local_file_path: pathlib.Path,
    chunk_size: int = 128
) → None
```

Download streaming a file url to `local_file_path`

---

<a href="..\py_to_win_app\py_to_win_app\extract_embedded#L186"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.extract_embedded`

```python
extract_embedded(embedded_file_path: pathlib.Path) → None
```





---

<a href="..\py_to_win_app\py_to_win_app\make_dist#L432"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.make_dist`

```python
make_dist(file_name: str = None) → Path
```





---

<a href="..\py_to_win_app\py_to_win_app\unzip#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>method</kbd> `Project.unzip`

```python
unzip(zip_file_path: pathlib.Path, destination_dir_path: pathlib.Path) → None
```







---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
