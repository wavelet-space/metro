"""
Zjištění a vykreslení závislostí mezi moduly v Python balíku.

"""

import sys
import inspect
import importlib

from dataclasses import dataclass

from typing import Any, List
from types import ModuleType

## Jaké má balík moduly?

def import_package(package_name: str) -> ModuleType:
    package = importlib.import_module(package_name)
    return package


def inspect_module(module: object) -> Any:
    for member in inspect.getmembers(module):
        if member[0] != "__builtins__":
            yield member
            if inspect.ismodule(member[1]):
                inspect_module(member)


@dataclass(frozen=True)
class Module:
    classes: List[str]
    functions: List[str]


@dataclass(frozen=True)
class Package:
    modules: List[str]


def main():

    # Načti balík daný jako název na příkazové řádce.
    if len(sys.argv) > 1:
        this = import_package(sys.argv[1])
    # Nebo načti tento modul
    else:
        this = sys.modules[__name__]

    # doc = inspect.getdoc(this)
    # package = Package(
    #     modules=modules
    # )

    members = [member[1] for member in inspect_module(this)]

    for m in members:
        if inspect.isclass(m):
            print(m.__name__, m.__module__, m.__name__, m.__qualname__)
        elif inspect.isfunction(m):
            print(m.__name__, m.__module__, m.__name__)


if __name__ == "__main__":

    main()