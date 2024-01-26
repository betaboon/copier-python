from jinja2.ext import Extension
from packaging import version

PYTHON_VERSIONS = ["3.8", "3.9", "3.10", "3.11", "3.12"]


def to_python_version(value: list[str] = []) -> str:
    available_versions = sorted([version.parse(v) for v in PYTHON_VERSIONS])
    selected_versions = sorted([version.parse(v) for v in value])
    deselected_versions = sorted(set(available_versions) - set(selected_versions))

    min_version = selected_versions[0]
    max_version = selected_versions[-1]
    gap_versions = [v for v in deselected_versions if min_version < v < max_version]

    version_string = f">={min_version},<{max_version.major}.{max_version.minor + 1}"
    for v in gap_versions:
        version_string += f",!={v}.*"

    return version_string


class PythonExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["to_python_version"] = to_python_version
