import re

from jinja2.ext import Extension


def to_slug(value: str, separator: str = "-") -> str:
    value = value.lower()
    value = re.sub(r"[^\w\s_-]", "", value)
    value = re.sub(r"[\s_-]+", separator, value)
    return value


class SlugExtension(Extension):
    def __init__(self, environment):
        super().__init__(environment)
        environment.filters["to_slug"] = to_slug
