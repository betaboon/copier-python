# Copier Python Template

A [Copier](https://github.com/copier-org/copier) template for Python projects managed by [PDM](https://github.com/pdm-project/pdm).

## Features

| | |
|-|-|
| Package management | [![pdm](https://img.shields.io/badge/pdm-7e56c2?style=for-the-badge&logo=pdm&logoColor=white)](https://pdm-project.org) |
| Linting and Formatting | [![ruff](https://img.shields.io/badge/ruff-d7ff64?style=for-the-badge&logo=ruff&logoColor=black)](https://astral.sh/ruff) [![gitlint](https://img.shields.io/badge/gitlint-blue?style=for-the-badge&logo=conventionalcommits&logoColor=white)](https://jorisroovers.com/gitlint/latest/)|
| Testing | [![pytest](https://img.shields.io/badge/pytest-009fe3?style=for-the-badge&logo=pytest&logoColor=white)](https://pytest.org) |
| Git hooks | [![precommit](https://img.shields.io/badge/pre_commit-fab040?style=for-the-badge&logo=precommit&logoColor=black)](https://pre-commit.com/) |
| Documenting | [![sphinx](https://img.shields.io/badge/sphinx-blue?style=for-the-badge&logo=sphinx&logoColor=white)](https://www.sphinx-doc.org) |
| Documentation hosting | [![githubpages](https://img.shields.io/badge/pages-black?style=for-the-badge&logo=github&logoColor=white)](https://pages.github.com) |
| CI/CD | [![githubactions](https://img.shields.io/badge/actions-black?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/actions) |
| Releasing | [![pypi](https://img.shields.io/badge/pypi-0073b7?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org) [![semanticrelease](https://img.shields.io/badge/semantic_release-blue?style=for-the-badge&logo=semanticrelease&logoColor=white)](https://github.com/python-semantic-release/python-semantic-release)|
| Container image | [![docker](https://img.shields.io/badge/docker-1d63ed?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)|


## Installation

To install Copier use [`pipx`](https://pipx.pypa.io):
```
pip install --user pipx
pipx install copier
```

As this template uses custom extensions you have to install [`copier-templates-extensions`](https://github.com/copier-org/copier-templates-extensions):
```
pip inject copier copier-templates-extensions
```

## Usage

To create a project from this template:
```
copier copy --trust "gh:betaboon/copier-python" /path/to/project
```

## PDM scripts

This template provides some [pdm scripts](https://pdm-project.org/latest/usage/scripts/)

Get a full list with `pdm run --list`:

| Name              | Description              |
|-------------------|--------------------------|
| test              | Run tests                |
| lint              | Run pre-commit           |
| docs-build        | Build docs               |
| docs-serve        | Build and serve docs     |
| install-git-hooks | Install pre-commit hooks |

## GitHub configuration

It is suggested to [create a branch-protection rule for `main`](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches).

For GitHub pages publishing, you need to [enable publishing with custom action](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site#publishing-with-a-custom-github-actions-workflow).

## PyPI configuration

For PyPI publishing, you need to [create a pypi project with a trusted publisher](https://docs.pypi.org/trusted-publishers/).
