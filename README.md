# metro

Tool for Advanced Packaging (Python and C/C++).

## Features

This is a kinda monolith,&hellip; can be splitted to several packages in the future.

- [ ] Generate project from JSON/YAML templates.
- [ ] Create and activate virtual environment.
- manage and audit
  - [ ] Verify package structures: use <https://github.com/wavelet-space/pmt>?
  - [ ] Change package name

- Don't overgeneralize, make it work for us!
- Using jinja and extensions for templating.


Motivation
A large number of projects have almost no or inadequate documentation. When we want to expand or contribute to the project in any way, it is useful if you can quickly navigate its structure. The simplest solution is to draw a dependency graph between modules (Python) or header files (C++), e.g. using GraphViz (SVG, PNG). Graph nodes represent modules and arrows of dependencies between them.

Installation
Features and Usage
 Get module dependencies (graph)
Search modules …
 Run as service/server
References
http://pymotw.com/2/inspect/
https://docs.python.org/3/library/inspect.html
https://www.geeksforgeeks.org/how-to-import-a-python-module-given-the-full-path/