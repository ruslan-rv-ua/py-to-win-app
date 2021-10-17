from pathlib import Path
from typing import Iterable, Union
import re

PYTHON_VERSION_REGEX = re.compile(r"^(\d+|x)\.(\d+|x)\.(\d+|x)$")


class Project:
    def __init__(
        self, input_dir: str, main_file: str, app_name: str = None
    ) -> None:
        self._path = Path().cwd()
        self._input_path = self._path / input_dir
        self._app_name = app_name if app_name is not None else self._path.name

        (self._path / "build").mkdir(exist_ok=True)
        self._build_path: Path = None
        self._source_path: Path = None
        self._exe_path: Path = None
        self._pydist_path: Path = None
        self._requirements_path: Path = None

        (self._path / "dist").mkdir(exist_ok=True)
        self._dist_path: Path = None

    @property
    def path(self) -> Path:
        return self._path

    @property
    def input_path(self) -> None:
        return self._input_path

    @property
    def app_name(self) -> str:
        return self._app_name

    @property
    def build_path(self) -> Path:
        return self._build_path

    @property
    def source_path(self) -> Path:
        return self._source_path

    @property
    def exe_path(self) -> Path:
        return self._exe_path

    @property
    def pydist_path(self) -> Path:
        return self._pydist_path

    @property
    def requirements_path(self) -> Path:
        return self._requirements_path

    @property
    def dist_path(self) -> Path:
        return self._dist_path

    @staticmethod
    def _is_correct_version(python_version) -> bool:
        return re.match(PYTHON_VERSION_REGEX, python_version)

    def build(
        self,
        python_version: str,
        pydist_dir: str = "pydist",
        requirements_file: str = "requirements.txt",
        extra_pip_install_args: Iterable[str] = (),
        build_dir: str = None,
        source_dir: str = None,
        # TODO ignore_input: Iterable[str] = (),
        show_console: bool = False,
        icon_file: Union[str, Path, None] = None,
        # TODO: download_dir: Union[str, Path] = None,
    ) -> None:
        if not self._is_correct_version(python_version):
            raise ValueError(
                f"Specified python version `{python_version}` "
                "does not have the correct format, it should be of format: "
                "`x.x.x` where `x` is a positive number."
            )

        self._pydist_path = self._path / pydist_dir
        self._requirements_path = self._path / requirements_file
        self._build_path = (
            self._path / "build" / build_dir
            if build_dir is not None
            else self._path / "build" / self._app_name
        )
        self._source_path = (
            self._path / source_dir
            if source_dir is not None
            else self._path / self._app_name
        )
