
from setuptools import setup, find_namespace_packages

setup(
    name="wavelet-basis",
    version="0.1.0",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[],
     entry_points = {
        'console_scripts': ['basis=wavelet.basis:main'],
    }
)