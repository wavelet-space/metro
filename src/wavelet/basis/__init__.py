# Helpers for date, time, and calendar.


from typing import Self

# Helpers to work with JSON.

# Package helpers.


def create_and_activate_virtual_evironment(path):
    import venv
    venv.create()    

def check_package_structure(requirements: str):
    """Check the project structure against some requirements."""

class Project:
    def __init__(self, path, package_name: str, package_version="0.1.0") -> None:
        self.path = path
        self.package_name = package_name
        self.package_version = package_version 

    # builder pattern

    def with_repository(self) -> Self:
        ...

    def with_environment(self) -> Self:
         ...

    @classmethod
    def build(cls) -> Self:
        return cls(None, None, None)


def create_package_(template: str, with_enviroment: bool, with_repository: bool):
    # [required] Create the project directory.
    #   The project and package directory can and often are the same. 
    # [optional] Creare and activate virtual environment
    #    It is often desired that virtual environment is created inside the package.

    ...    
    
    
def main():
    # The command line interaface to create package structure etc.
    print(__name__)


if __name__ == "__main__":
        main()