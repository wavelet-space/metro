
from setuptools import setup, find_packages

setup(
    name="metro",
    version="0.2.0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "pyyaml",
        "jinja2", 
        "graphviz",
    ],
     entry_points = {
        'console_scripts': [
            'metro=metro:main',
            'graph=metro._explore:main',
        ],
    }
)