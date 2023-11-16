# Helpers for date, time, and calendar.


from typing import Self
from pathlib import Path

# Helpers to work with JSON.

# Package helpers.


# ###########################################################################
## Create project
# ###########################################################################

def create_and_activate_virtual_evironment(path):
    import venv

    venv.create()


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
    
    def create(self):
        root = Path(self.path)
        root.mkdir(parents=True, exist_ok=True)

        (self.path / "README.md").write_text("# README", encoding="utf8")

# ###########################################################################
## Manage project
# ###########################################################################


def check_package_structure(requirements: str):
    """Check the project structure against some requirements."""



# ###########################################################################
# use case
# ###########################################################################
def create_package(template: str, with_enviroment: bool, with_repository: bool):
    # [required] Create the project directory.
    #   The project and package directory can and often are the same.
    # [optional] Creare and activate virtual environment
    #    It is often desired that virtual environment is created inside the package.

    project = Project(Path("./project"), "package")
    project.create()


# ###########################################################################
def main():
    # The command line interaface to create package structure etc.
    print(__name__)
    create_package(None, False, False)

    from yaml import load, dump, Loader
    temp = load(open("./template/simple/project.yaml"), Loader=Loader)
    print(dump(temp))
    print(temp)

    from jinja2 import Template
    with open('template/simple/README.md') as file_:
        template = Template(file_.read())
        result = template.render(project_name=temp["package"]["name"])
        print(result)

if __name__ == "__main__":
    main()
