class ProjectException(Exception):
    pass


class InvalidPythonVersion(ProjectException):
    pass


class WrongInputDir(ProjectException):
    pass


class WrongMainFile(ProjectException):
    pass
