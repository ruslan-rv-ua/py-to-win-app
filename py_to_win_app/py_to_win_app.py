from pathlib import Path


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
