# Python Project Template

A starter template for Python projects with a clean structure and common development tooling preconfigured.

## TODO: mention in this README

- Python versions
    - in CI: see ci.yml
    - minimal version in pyproject.toml -> [project] -> requires-python
    - pyproject.toml -> tool.ruff -> target-version
- Project name currently "pyproj", rename accordingly in:
    - src/pyproj directory
    - pyproject.toml -> [project] -> name
- Define public API in src/pyproj/__init__.py
- line length for python files in
    - .vscode/settings.json -> [python] -> editor.rulers
    - pyproject.toml -> [tool.ruff] -> line-length
- License
    - pyproject.toml -> [project] -> license
- Pyright
    - Installed with "pip install -e ".[dev]". Alternatively install yourself to use from command line
    - Have pylance extension for VSCode installed, set it to use pyright
- Install uv (link to site) for dependency management. I installed it via PowerShell. Then run "uv sync" from repo root
- Install pre-commit via "uv run pre-commit install"
- Rune examples either via console, with task, or with debug launch configuration
- Tests setup to produce artifacts in .artifacts/pytest and .artifacts/pytest-cov. Mention junit.xml and human-readable .html sites. Also integrated into CI pipeline.
- Set Python interpreter
- Copyright in docs/conf.py -> LICENSE
- Docs generated to docs/build/html by both CI and VSCode task. Later integration into readthedocs can be configured to perform automatically.
