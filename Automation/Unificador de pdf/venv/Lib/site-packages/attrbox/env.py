"""Load configuration from environment files.

The file format is similar to a Bash file, but it is not as complete as
[python-dotenv](https://github.com/theskumar/python-dotenv#file-format).

Supported:

- unquoted and single-quoted key
- unquoted, single- and double-quoted value
- spaces before and after key, equal sign, and value are ignored
- `export` at the start of the line is ignored
- `#` comment at the start of the line
- value expansion for values in the environment
- value expansion for values only in the file (e.g., when `update_env=False`)

Unsupported:

- key without a value
- multiline value
- `#` comment after value
- escape sequences in value

Examples:
    >>> loads('''
    ... # a comment
    ... normal=value
    ... ' quoted '=" space "
    ... export expanded="expanded-${normal}"
    ... ''')
    {'normal': 'value', ' quoted ': ' space ', 'expanded': 'expanded-value'}
"""

# native
from os import environ as ENV
from pathlib import Path
from typing import Dict
from typing import Optional
from typing import Mapping
from typing import Protocol
from typing import Union
from typing import Match
import re

# pkg
from .attrdict import AttrDict

PathStr = Union[Path, str]
"""Type representing a `Path` or a string to a path."""

_RE_EXPAND = re.compile(r"\$(\w+|\{[^}]*\})", re.ASCII)
"""Regex for finding variable expansions."""


class SupportsRead(Protocol):  # pylint: disable=too-few-public-methods
    """Protocol for a class that implements a `.read()` method."""

    def read(self) -> str:
        """Read the contents of the file-like object."""


def expand(
    value: str,
    store: Optional[Mapping[str, str]] = None,
    *,
    dotted_keys: bool = False,
) -> str:
    """Expand variables of the form `$var` and `${var}`.

    A simplified form of `os.path.expandvars`.

    Args:
        value (str): value to expand

        store (Mapping[str, str], optional): valid substitutions.
            If `None`, `os.environ` is used. Defaults to `None`.

        dotted_keys (bool): if `True` allow `${dotted.name}` to map
            to nested values `{"dotted": {"name": "value"}}`.
            Defaults to `False`.

    Returns:
        str: expanded value. Unknown variables are left unchanged.

    Examples:
        Regular expansion works as expected:
        >>> expand("$a ${b}", {'a': 'hello', 'b': 'world'})
        'hello world'

        Unknown variables are left unchanged:
        >>> expand("$a is $b", {'a': 'this'})
        'this is $b'
        >>> expand("no vars", {})
        'no vars'

        Values are passed to `str`:
        >>> expand("$a", {'a': 5})
        '5'

        Dotted names are optionally possible:
        >>> expand("${a.b}", {"a": {"b": "works"}}, dotted_keys=True)
        'works'
    """
    if "$" not in value:
        return value

    values = store or ENV

    if dotted_keys and not isinstance(values, AttrDict):
        values = AttrDict(values)

    def _repl(match: Match[str]) -> str:
        value = match.group(0)
        name = match.group(1)
        if name.startswith("{") and name.endswith("}"):
            name = name[1:-1]

        if dotted_keys:
            name = name.split(".")

        if name in values:
            value = str(values[name])
        return value

    return _RE_EXPAND.sub(_repl, value)


def load(
    file: SupportsRead,
    /,
    *,
    update_env: bool = True,
    dotted_keys: bool = True,
) -> Dict[str, str]:
    """Load an environment `file`.

    Args:
        file (SupportsRead): file-like (has `.read()`).

        update_env (bool, optional): If `True`, update the `os.path.environ` as
            values are read in. Defaults to `True`.

        dotted_keys (bool, optional): If `True`, split the key by `.` and use that
            to create a nested `dict`. Defaults to `True`.

    Returns:
        Dict[str, str]: configuration values

    Examples:
        >>> root = Path(__file__).parent.parent.parent
        >>> load((root / "test/config_3.env").open())
        {'section': {'key': 'value3', 'env': 'loaded'}}
    """
    return loads(file.read(), update_env=update_env, dotted_keys=dotted_keys)


def loads(
    text: str,
    /,
    *,
    update_env: bool = True,
    dotted_keys: bool = True,
) -> Dict[str, str]:
    """Parse an environment file from a string.

    Args:
        text (str): text to parse.

        update_env (bool, optional): If `True`, update the `os.path.environ` as
            values are read in. Defaults to `True`.

        dotted_keys (bool, optional): If `True`, split the key by `.` and use that
            to create a nested `dict`. Defaults to `True`.

    Returns:
        Dict[str, str]: configuration values

    Examples:
        If you don't want to update the environment:
        >>> 'fake' in ENV
        False
        >>> loads('''export 'fake'=ignored
        ... works=not $fake''', update_env=False)
        {'fake': 'ignored', 'works': 'not ignored'}
        >>> 'fake' in ENV
        False

        Keys with dots in them create nested dicts, but are optional:
        >>> loads('section.key=value', update_env=False, dotted_keys=True)
        {'section': {'key': 'value'}}
        >>> loads('section.key=value', update_env=False, dotted_keys=False)
        {'section.key': 'value'}
    """
    result = AttrDict()
    for line in text.replace("\r\n", "\n").split("\n"):
        line = line.strip()
        if not line or line.startswith("#"):
            continue  # skip blank lines and comments

        if line.startswith("export "):
            line = line[len("export ") :]

        key, value = line.split("=", 1)

        key = key.strip()
        if len(key) >= 2 and key.startswith("'") and key.endswith("'"):
            key = key[1:-1]  # unquote key

        # We expand the value with the current values which may have
        # nested structure and then with the environment values (which do not).
        value = expand(value, result, dotted_keys=dotted_keys)
        value = expand(value)

        value = value.strip()
        if len(value) >= 2 and (
            (value.startswith("'") and value.endswith("'"))
            or (value.startswith('"') and value.endswith('"'))
        ):
            value = value[1:-1]  # unquote value

        if update_env:
            ENV[key] = value
        if dotted_keys:
            result[key.split(".")] = value
        else:
            result[key] = value
    return result


def find_env(path: Optional[PathStr] = None, name: str = ".env") -> Optional[Path]:
    """Find the `.env` file in the ancestors of the current path.

    Args:
        path (PathLike, optional): A starting path to check. If `None`, starts with
            the current working directory. Defaults to `None`.
        name (str, optional): file name to search for. Defaults to `".env"`.

    Returns:
        Optional[Path]: path to environment file or `None` if it is not found.

    Examples:
        Search from the current working directory:
        >>> str(find_env())
        '.../.env'

        Search from a specific directory:
        >>> str(find_env("."))
        '.../.env'

        Pass a `Path` object:
        >>> str(find_env(Path(__file__)))
        '.../.env'

        Point directly to the `.env` file:
        >>> str(find_env(Path(__file__).parent.parent.parent / ".env"))
        '.../.env'
    """
    if not path:
        path = Path.cwd()
    elif isinstance(path, str):
        path = Path(path).resolve()

    if path.name == name and path.exists():
        return path

    for parent in [path] + list(path.parents):
        path = parent / name
        if path.exists():
            return path
    return None


def load_env(path: Optional[PathStr] = None) -> Dict[str, str]:
    """Load an environment file.

    We recursively search for a `.env` file from the path given or the current
    working directory, if omitted.

    Args:
        path (PathStr, optional): starting path. If `None`, start from the
            current working directory. Defaults to `None`.

    Raises:
        FileNotFoundError: If not `.env` file is found.

    Returns:
        Dict[str, str]: configuration values

    Examples:
        >>> load_env() # our .env doesn't have any values
        {}

        If no `.env` can be found, a `FileNotFoundError` is raised:
        >>> load_env("/")
        Traceback (most recent call last):
            ...
        FileNotFoundError: Cannot find .env file to load.
    """
    path = find_env(path)
    if not path or not path.exists():
        raise FileNotFoundError("Cannot find .env file to load.")
    return loads(path.read_text(encoding="utf-8"), update_env=True, dotted_keys=True)
