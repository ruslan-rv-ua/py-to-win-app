import os
import re
import shutil
import subprocess
import sys
from tkinter.tix import Tree
import zipfile
from contextlib import contextmanager
from pathlib import Path
from typing import Iterable, Optional, Union

import requests
import tomli
from genexe.generate_exe import generate_exe
from txtoml.txtoml import constrain


__all__ = ["Project"]

_PYTHON_VERSION_REGEX = re.compile(r"^(\d+|x)\.(\d+|x)\.(\d+|x)$")
_GET_PIP_URL = "https://bootstrap.pypa.io/get-pip.py"
_PYTHON_URL = "https://www.python.org/ftp/python"
_HEADER_NO_CONSOLE = (
    """import sys, os"""
    + """\nif sys.executable.endswith('pythonw.exe'):"""
    + """\n    sys.stdout = open(os.devnull, 'w')"""
    + """\n    sys.stderr = open(os.path.join(os.getenv(\'TEMP\'), """
    + """\'stderr-{}\'.format(os.path.basename(sys.argv[0]))), "w")"""
    + """\n\n"""
)
_DEFAULT_IGNORE_PATTERNS = [
    "__pycache__",
    "*.pyc",
    "build.py",
]


@contextmanager
def _log(message: str, exit_message: str = "Done.") -> None:
    print(message)
    yield
    if exit_message:
        print(exit_message, end="\n\n")


class Project:
    def __init__(
        self,
        *,
        path: Union[str, Path] = "",
        name: str = "",
        version: str = "",
        input_dir: str = "",
        main_file: str = "",
        requirements: Union[Iterable[str], str, Path] = "requirements.txt",
        extra_pip_install_args: Iterable[str] = (),
    ) -> None:
        """TODO

        Args:
            name (str, optional): App's name. If `None` then project's folder name will be used. Defaults to `None`.
            version (str, optional): App's version. Defaults to `None`.
            input_dir (str): Directory where your source files are.
            main_file (str): Path to entry point, e.g. `main.py`
        """  # noqa

        self._path = Project._make_absolute_path(path)

        # make folders for build and dist
        self._build_subdir_path = Path.cwd() / "build"
        self._build_subdir_path.mkdir(exist_ok=True)
        self._dist_subdir_path = Path.cwd() / "dist"
        self._dist_subdir_path.mkdir(exist_ok=True)
        self._download_subdir_path = Path.cwd() / 'downloads'
        self._download_subdir_path.mkdir(exist_ok=True)

        self._name = name
        self._version = version

        self._input_path = Project._make_absolute_path(
            input_dir,
            default_path=self._discover_input_dir(self.path),
            base_path=self.path,
        )
        if not self._input_path.exists():
            raise FileNotFoundError(
                f"Input dir  does not exists: `{self.input_path}`"
            )
        print(f"Input dir: {self.input_path}")

        self._main_file_path = Project._make_absolute_path(
            main_file,
            default_path=self._discover_main_file(self.input_path),
            base_path=self.input_path,
        )
        if not (
            self._main_file_path.is_file() and self._main_file_path.exists()
        ):
            raise FileNotFoundError(
                f"Main file does not exists: `{self._main_file_path}` "
            )
        print(f"Main file: {self._main_file_path}")
        self._main_file_name = self._main_file_path.name

        self._requirements = requirements
        self._extra_pip_install_args = extra_pip_install_args

        self._build_path: Path = None
        self._source_path: Path = None
        self._exe_path: Path = None
        self._pydist_path: Path = None
        self._dist_path: Path = None

    @classmethod
    def from_pyproject(
        cls,
        pyproject_toml: Union[str, Path] = "pyproject.toml",
        input_dir: str = "",
        main_file: str = "",
        extra_pip_install_args: Iterable[str] = (),
    ) -> "Project":
        toml_file_path = Path(pyproject_toml)
        if not toml_file_path.is_absolute():
            toml_file_path = Path.cwd() / toml_file_path
        toml_content = toml_file_path.read_text()
        toml_data = tomli.loads(toml_content)
        name = toml_data["tool"]["poetry"]["name"]
        version = toml_data["tool"]["poetry"]["version"]
        toml_dependencies: dict = toml_data["tool"]["poetry"]["dependencies"]

        requirements = [
            f'"{package}{version}"'
            for package, version in constrain(toml_dependencies).items()
        ]

        return cls(
            path=toml_file_path.parent,
            name=name,
            version=version,
            input_dir=input_dir,
            main_file=main_file,
            requirements=requirements,
            extra_pip_install_args=extra_pip_install_args,
        )

    def build(
        self,
        *,
        python_version: str,
        build_path: Union[str, Path] = "",
        source_dir: str = "",
        pydist_dir: str = "",
        download_dir: Union[str, Path] = "",
        extract_pythonzip: bool = Tree,
        # TODO ignore_input: Iterable[str] = (),
        show_console: bool = False,
        exe_file_name: str = None,
        icon_file: Optional[Union[str, Path]] = None,
    ) -> None:
        """TODO

        Args:
            python_version (str): Embedded python version
            requirements_file (str, optional): Path to `requirements.txt` file. Defaults to `"requirements.txt"`.
            extra_pip_install_args (Iterable[str], optional): Arguments to be appended to the `pip install` command during installation of requirements. Defaults to `()`.
            build_dir (str, optional): Directory to place build to. If `None` then `app_name` attribute will be used. Defaults to `None`.
            pydist_dir (str, optional): Subdirectory where to place Python embedde interpreter. Defaults to `"pydist"`.
            source_dir (str, optional): Subdirectory where to place source code. If `None` then `app_nam` attribute will be used. Defaults to `None`.
            show_console (bool, optional): Show console window or not. Defaults to `False`.
            exe_name (str, optional): Name of `.exe` file.
                If `None` then name will be the same as `main_file`.
                Defaults to `None`.
            icon_file (Union[str, Path, None], optional): Path to icon file. Defaults to `None`.

        Raises:
            InvalidPythonVersion: If incorrect Python version provided.
        """  # noqa

        if not self._is_correct_version(python_version):
            raise ValueError(
                f"Specified python version `{python_version}` "
                + "does not have the correct format, it should be of format: "
                + "`x.x.x` where `x` is a positive number."
            )

        self._build_path = Project._make_absolute_path(
            build_path,
            default_path=self.full_name,
            base_path=self._build_subdir_path,
        )
        self._pydist_path = Project._make_absolute_path(
            pydist_dir, default_path="pydist", base_path=self.build_path
        )
        self._scripts_path = self.pydist_path / "Scripts"
        self._source_path = Project._make_absolute_path(
            source_dir, default_path=self.name, base_path=self.build_path
        )
        download_path = Project._make_absolute_path(
            download_dir, default_path=self._download_subdir_path, base_path=self.path
        )
        if not download_path.exists():
            raise FileNotFoundError(
                f'Download directory does not exists: `{download_path}`'
            )

        ##################################################
        # do the magic!
        ##################################################
        self._make_empty_build_dir()
        self._copy_source_files()

        # download embedded python and extract it to build directory
        pydist_file_path = self._download_python_dist(
            download_path=download_path, python_version=python_version
        )
        self._extract_pydist_file(pydist_file_path)

        self._patch_pth_file(python_version=python_version)
        if extract_pythonzip:
            self._extract_pythonzip(python_version=python_version)

        # Get and install `pip`. Install requirements
        getpippy_file_path = self._download_getpippy(
            download_path=download_path
        )
        with _log(
            f"Coping `{getpippy_file_path}` file to `{self._pydist_path}`"
        ):
            copied_getpippy_file_path = Path(
                shutil.copy2(getpippy_file_path, self.pydist_path)
            )
        self._install_pip()
        self._install_requirements(
            extra_pip_install_args=self._extra_pip_install_args
        )
        with _log(f"Removeing `{copied_getpippy_file_path}`"):
            copied_getpippy_file_path.unlink()

        # make exe
        if exe_file_name is None:
            exe_file_name = self.name
        else:
            if exe_file_name.lower().endswith(".exe"):
                # other_name.exe -> other_name
                exe_file_name = exe_file_name.lower().rstrip(".exe")
        icon_file_path = Path(icon_file) if icon_file is not None else None
        self._make_startup_exe(
            show_console=show_console,
            exe_file_name=exe_file_name,
            icon_file_path=icon_file_path,
        )

        _log(
            f"\nBuild done! Folder `{self._build_path}` "
            "contains your runnable application!\n",
            exit_message=None,
        )

    def make_dist(
        self,
        *,
        file_name: Optional[str] = None,
        delete_build_dir: bool = False,
    ) -> Path:
        if file_name is None:
            file_name = self.full_name
        zip_file_path = self._dist_subdir_path / file_name
        with _log(f"Making zip archive {zip_file_path}"):
            shutil.make_archive(
                base_name=str(zip_file_path),
                format="zip",
                root_dir=str(self._build_subdir_path),
                base_dir=str(
                    self.build_path.relative_to(self._build_subdir_path)
                ),
            )
        self._dist_path = zip_file_path

        if delete_build_dir:
            self._delete_build_dir()

        return zip_file_path

    @property
    def path(self) -> Path:
        return self._path

    @property
    def name(self) -> str:
        return self._name if self._name else self.path.name

    @property
    def version(self) -> str:
        return self._version

    @property
    def full_name(self) -> str:
        """<name>-<version>"""
        return self.name + (f"-{self.version}" if self.version else "")

    @property
    def input_path(self) -> Path:
        return self._input_path

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
    def dist_path(self) -> Path:
        return self._dist_path

    @staticmethod
    def _make_absolute_path(
        path: Union[str, Path] = "",
        default_path: Union[str, Path] = "",
        base_path: Union[str, Path] = Path().cwd(),
    ) -> Path:
        path = Path(path or default_path)
        if path.is_absolute():
            return path
        return Path(base_path).absolute().resolve() / path

    def _discover_input_dir(self, path: Path) -> str:
        with _log(f"Input dir not specified.\nDiscovering in `{path}`"):
            names = [
                f"{self.name}",
                f"{self.name.replace('-', '_')}",
                f"{self.name.replace('-', '')}",
                "src",
                "source",
                "sources",
            ]
            for name in names:
                input_path = path / name
                print(f"Trying `{input_path}`...")
                if input_path.exists():
                    return name
            print("Nothing discovered.")
            return ""

    def _discover_main_file(self, path: Path) -> str:
        with _log(f"Main file not specified.\nDiscovering in `{path}`"):
            names = (
                f"{self.name}.py",
                f"{self.name.replace('-', '_')}.py",
                f"{self.name.replace('-', '')}.py",
                "main.py",
            )
            for name in names:
                main_file_path = path / name
                print(f"Trying `{main_file_path}`...")
                if main_file_path.is_file():
                    return name
            print("Nothing discovered.")
            return ""

    @staticmethod
    def _is_correct_version(python_version) -> bool:
        return re.match(_PYTHON_VERSION_REGEX, python_version)

    @staticmethod
    def _get_short_version(python_version: str) -> str:
        return "".join(python_version.split(".")[:2])  # 3.9.7 -> 39

    @staticmethod
    def _execute_os_command(command: str, cwd: str = None) -> str:
        """Execute terminal command"""

        with _log(f"Running command: {command}", exit_message=None):
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                cwd=os.getcwd() if cwd is None else cwd,
            )

            # Poll process for new output until finished
            while True:
                nextline = process.stdout.readline().decode("UTF-8")
                if nextline == "" and process.poll() is not None:
                    break
                sys.stdout.write(nextline)
                sys.stdout.flush()

            output = process.communicate()[0]
            exit_code = process.returncode

            if exit_code == 0:
                return output
            else:
                raise Exception(command, exit_code, output)

    @staticmethod
    def _download_file(
        url: str, local_file_path: Path, chunk_size: int = 128
    ) -> None:
        """Download streaming a file url to `local_file_path`"""
        r = requests.get(url, stream=True)
        with open(local_file_path, "wb") as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    @staticmethod
    def _unzip(zip_file_path: Path, destination_dir_path: Path) -> None:
        with zipfile.ZipFile(zip_file_path, "r") as zip_file:
            zip_file.extractall(destination_dir_path)

    @staticmethod
    def _download_python_dist(download_path: Path, python_version: str):
        embedded_file_name = f"python-{python_version}-embed-amd64.zip"
        embedded_file_path = download_path / embedded_file_name
        with _log("Downloading embedde python."):
            if embedded_file_path.is_file():
                return embedded_file_path
            Project._download_file(
                url=f"{_PYTHON_URL}/{python_version}/{embedded_file_name}",
                local_file_path=embedded_file_path,
            )
            if not embedded_file_path.is_file():
                raise RuntimeError("Download failed!")
        return embedded_file_path

    @staticmethod
    def _download_getpippy(download_path: Path) -> Path:
        getpippy_file_path = download_path / "get-pip.py"
        with _log("Downloading `get-pip.py`."):
            if getpippy_file_path.exists():
                return getpippy_file_path
            Project._download_file(
                url=_GET_PIP_URL, local_file_path=getpippy_file_path
            )
            if not getpippy_file_path.exists():
                raise RuntimeError("Download failed!")
        return getpippy_file_path

    def _make_empty_build_dir(self) -> None:
        # Delete build folder if it exists
        if self._build_path.is_dir():
            with _log(
                f"Existing build directory found, "
                f"removing contents from `{self._build_path}`"
            ):
                shutil.rmtree(self._build_path)
        self._build_path.mkdir()

    def _extract_pydist_file(self, pydist_file_path: Path) -> None:
        with _log(
            f"Extracting `{pydist_file_path}` to `{self._pydist_path}`"
        ):
            self._unzip(
                zip_file_path=pydist_file_path,
                destination_dir_path=self._pydist_path,
            )

    def _copy_source_files(self) -> None:
        ignore_patterns = []
        ignore_patterns.append(self._build_path.name)
        ignore_patterns += _DEFAULT_IGNORE_PATTERNS
        if not self._source_path.is_dir():
            self._source_path.mkdir()
        with _log(
            f"Copying files from `{self._input_path}` "
            + f"to `{self._source_path}`."
        ):
            shutil.copytree(
                src=self._input_path,
                dst=self._source_path,
                ignore=shutil.ignore_patterns(*ignore_patterns),
                dirs_exist_ok=True,
            )

    def _patch_pth_file(self, python_version: str) -> None:
        short_version = Project._get_short_version(python_version)
        pth_file_name = f"python{short_version}._pth"  # python39._pth
        pth_file_path = self._pydist_path / pth_file_name
        pythonzip_file_name = f"python{short_version}.zip"  # python39.zip
        with _log(
            f"Generating `{pth_file_path}` with uncommented `import site` line"
        ):
            if self._pydist_path == self._build_path:
                relative_path_to_source = "."
            else:
                relative_path_to_source = ".."
            relative_path_to_source += f"\\{self._source_path.name}"

            pth_file_content = (
                f"{pythonzip_file_name}\n"
                + f"{relative_path_to_source}\n\n"
                + "# Uncomment to run site.main() automatically\n"
                + "import site\n"
            )
            pth_file_path.write_text(pth_file_content, encoding="utf8")

    def _extract_pythonzip(self, python_version: str) -> None:
        """Extract pythonXX.zip zip file to pythonXX.zip folder
        and delete pythonXX.zip zip file
        """
        short_version = Project._get_short_version(python_version)
        pythonzip_file_name = f"python{short_version}.zip"  # python39.zip
        pythonzip_file_path = self._pydist_path / pythonzip_file_name
        pythonzip_dir_path = Path(pythonzip_file_path)
        with _log(
            f"Extracting `{pythonzip_file_path}` to `{pythonzip_dir_path}`"
        ):
            pythonzip_file_path = pythonzip_file_path.rename(
                pythonzip_file_path.with_suffix(".temp_zip")
            )
            Project._unzip(pythonzip_file_path, pythonzip_dir_path)
            pythonzip_file_path.unlink()

    def _install_pip(self) -> None:
        with _log("Installing `pip`"):
            Project._execute_os_command(
                command="python.exe get-pip.py --no-warn-script-location",
                cwd=str(self.pydist_path),
            )
            if not self._scripts_path.exists():
                raise RuntimeError("Error installing `pip` with `get-pip.py`")

    def _install_requirements(self, extra_pip_install_args: Iterable):
        if isinstance(self._requirements, (str, Path)):
            # load from `requirements.txt`
            requirements_txt_path = Path(self._requirements)
            if not requirements_txt_path.is_absolute():
                requirements_txt_path = self.path / requirements_txt_path
            modules = requirements_txt_path.read_text().splitlines()
        else:  # is Iterable
            modules = self._requirements

        if extra_pip_install_args:
            extra_pip_install_args_str = " " + " ".join(extra_pip_install_args)
        else:
            extra_pip_install_args_str = ""

        for module in modules:
            with _log(f"Installing {module}:"):
                cmd = (
                    "pip3.exe install --no-cache-dir "
                    + "--no-warn-script-location "
                    + f"{module}{extra_pip_install_args_str}"
                )
                try:
                    Project._execute_os_command(
                        command=cmd, cwd=str(self._scripts_path)
                    )
                except Exception:
                    print("FAILED TO INSTALL ", module)
                    with (
                        self.build_path / "FAILED_TO_INSTALL_MODULES.txt"
                    ).open(mode="a") as f:
                        f.write(module + "\n")

    def _make_startup_exe(
        self,
        show_console: bool,
        exe_file_name: str,
        icon_file_path: Optional[Path] = None,
    ) -> Path:
        """Make the startup exe file needed to run the script"""

        if not show_console:
            main_file_copy_path = self._source_path / self._main_file_name
            with _log(f"No console. Patching `{main_file_copy_path}`"):
                main_file_content = main_file_copy_path.read_text(
                    encoding="utf8", errors="surrogateescape"
                )
                if _HEADER_NO_CONSOLE not in main_file_content:
                    main_file_copy_path.write_text(
                        str(_HEADER_NO_CONSOLE + main_file_content),
                        encoding="utf8",
                        errors="surrogateescape",
                    )

        relative_pydist_dir = self.pydist_path.relative_to(self.build_path)
        relative_source_dir = self.source_path.relative_to(self.build_path)
        exe_file_path = self.build_path / f"{exe_file_name}.exe"
        python_entrypoint = "python.exe"
        command_str = (
            f"{{EXE_DIR}}\\{relative_pydist_dir}\\{python_entrypoint} "
            + f"{{EXE_DIR}}\\{relative_source_dir}\\{self._main_file_name}"
        )

        with _log(
            f"Making startup exe file `{exe_file_path}`", exit_message=None
        ):
            generate_exe(
                target=exe_file_path,
                command=command_str,
                icon_file=icon_file_path,
                show_console=show_console,
            )

            self._exe_path = exe_file_path
            return exe_file_path

    def _delete_build_dir(self) -> None:
        with _log(f"Removing build folder {self._build_path}!"):
            shutil.rmtree(self.build_path)
            self._build_path = self._source_path = self._pydist_path = None
