class ProjectException(Exception):
    pass


class InvalidPythonVersion(ProjectException):
    pass


class InputDirError(ProjectException):
    pass


class MainFileError(ProjectException):
    pass
