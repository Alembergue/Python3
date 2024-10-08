"""Configuration loading and parsing."""

# native
from inspect import cleandoc
from pathlib import Path
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Sequence
from typing import Union
import json

# lib
from docopt import docopt
import tomli as tomllib  # TODO 2026-10-04 [3.10 EOL]: switch to native tomllib

# pkg
from .attrdict import AttrDict
from . import env

PYTHON_KEYWORDS: List[
    str
] = """\
    False      await      else       import     pass
    None       break      except     in         raise
    True       class      finally    is         return
    and        continue   for        lambda     try
    as         def        from       nonlocal   while
    assert     del        global     not        with
    async      elif       if         or         yield
""".lower().split()
"""[All Python keywords](https://docs.python.org/3/reference/lexical_analysis.html#keywords)."""

LoaderFunc = Callable[[str], Any]
"""Function signature to load configuration from a string."""

LOADERS: Dict[str, LoaderFunc] = {}
"""Mapping of file extensions to configuration loaders."""


def set_loader(suffix: str, loader: LoaderFunc) -> None:
    """Register a configuration `loader` for a given file `suffix`.

    NOTE: This will overwrite any previously registered loader for `suffix`.

    Args:
        suffix (str): file suffix with the leading period (e.g., `".json"`)

        loader (LoaderFunc): function that takes a string and returns
            an object, typically a `Dict[str, Any]` of key/value pairs.
    """
    LOADERS[suffix] = loader


set_loader(".json", json.loads)
set_loader(".toml", tomllib.loads)
set_loader(".env", env.loads)
# loaders registered


def load_config(
    path: Path,
    /,
    *,
    load_imports: bool = True,
    loaders: Optional[Mapping[str, LoaderFunc]] = None,
    done: Optional[List[Path]] = None,
) -> Dict[str, Any]:
    """Load a configuration file from `path` using configuration `loaders`.

    Args:
        path (Path): file to load.

        load_imports (bool, optional): If `True`, recursively load any files
            located at the `imports` key. Defaults to `True`.

        loaders (Mapping[str, LoaderFunc], optional): mapping of file suffixes
            to to loader functions. If `None`, uses the global `LOADERS`.
            Defaults to `None`.

        done (List[Path], optional): If provided, a list of paths to ignore when
            doing recursive loading. Defaults to `None`.

    Returns:
        Dict[str, Any]: keys/values from the configuration file

    Examples:
        >>> root = Path(__file__).parent.parent.parent
        >>> expected = {'section': {'key': 'value1', "env": "loaded",
        ... "json": "loaded", "toml": "loaded"}}
        >>> load_config(root / "test/config_1.toml") == expected
        True
    """
    result = AttrDict()
    path = path.resolve()
    done = done or []

    loader = (loaders or LOADERS)[path.suffix]
    data = loader(path.read_text())
    if load_imports and "imports" in data:
        imports = [(path.parent / p).resolve() for p in data.pop("imports")]
        for file in imports:
            if file in done:
                continue

            result <<= load_config(
                file,
                load_imports=True,
                loaders=loaders,
                done=done + imports,
            )
    result <<= data
    return result


def optvar(
    name: str,
    /,
    *,
    shadow_keywords: bool = False,
    shadow_builtins: bool = False,
) -> str:
    """Return a valid python variable name from a docopt flag.

    Args:
        name (str): docopt option name.

        shadow_keywords (bool, optional): If `True`, allow `name` to be a
            python keyword. Otherwise, add an underscore. Defaults to `False`.

        shadow_builtins (bool, optional): If `True` allow `name` to be a name
            of a python `builtins` (globally available names). Otherwise, add an
            underscore. Defaults to `False`.

    Returns:
        str: option name converted to a valid python variable name

    Examples:
        Special cases:
        >>> optvar("-") == "stdin"
        True
        >>> optvar("--") == "__"
        True

        Leading dashes removed:
        >>> optvar("--example") == "example"
        True
        >>> optvar("-v") == "v"
        True

        Hyphens become underscores:
        >>> optvar("--two-words") == "two_words"
        True

        Angle brackets removed:
        >>> optvar("<file>") == "file"
        True

        By default, we don't shadow keywords or builtins:
        >>> optvar("--continue") == "continue_"
        True
        >>> optvar("--help") == "help_"
        True

        Shadow builtins if you want:
        >>> optvar("--list", shadow_builtins=True) == "list"
        True

        Shadow keywords at your own risk:
        >>> optvar("--continue", shadow_keywords=True) == "continue"
        True
    """
    result = name.lower()
    special = {"-": "stdin", "--": "__"}
    if result in special:
        return special[result]
    # special cases handled

    result = result.replace("--", "")
    if result[0] == "-":
        result = result[1:]
    # leading hyphens removed

    trans: Dict[str, Union[str, int, None]] = {"-": "_", "<": "", ">": ""}
    result = result.translate(str.maketrans(trans))
    # hyphens become underscores; angle brackets removed

    if not shadow_keywords and result in PYTHON_KEYWORDS:
        result += "_"
        # don't shadow keywords

    if not shadow_builtins:
        built_in = [s.lower() for s in globals()["__builtins__"]]
        if result in built_in:
            result += "_"
        # don't shadow builtins

    return result


def parse_docopt(
    doc: str,
    /,
    argv: Optional[Sequence[str]] = None,
    *,
    version: str = "1.0.0",
    options_first: bool = False,
    read_config: bool = True,
) -> AttrDict:
    """Parse docopt args and load config.

    Args:
        doc (str): docstring with description of command

        argv (Sequence[str], optional): arguments to parse against the
            doc. If `None`, will default to `sys.argv[1:]`. Defaults to `None`.

        version (str, optional): program version. Defaults to `"1.0.0"`.

        options_first (bool): If `True`, options must come before positional
            arguments. Defaults to `False`.

        read_config (bool): If `True`, a `<config>` argument or `--config` option
            will be automatically loaded before args are parsed. Defaults to `True`.

    Returns:
        AttrDict[str, Any]: mapping of options to values

    Examples:
        >>> usage = "Usage: test.py [--debug]"
        >>> parse_docopt(usage, argv=["--debug"])
        {'debug': True}

        >>> root = Path(__file__).parent.parent.parent
        >>> path = str(root / "test/config_1.toml")
        >>> usage = "Usage: test.py <config> [--section.key=VAL]"
        >>> argv = [path, "--section.key=overwrite"]
        >>> expected = {"section": {
        ...     "key": "overwrite", # overwritten by argv
        ...     "env": "loaded", "json": "loaded", "toml": "loaded"
        ... }, "config": path}
        >>> parse_docopt(usage, argv=argv) == expected
        True
    """
    result = AttrDict()
    args = {
        optvar(k, shadow_builtins=True): v
        for k, v in docopt(
            cleandoc(doc),
            argv=argv,
            help=True,
            version=version,
            options_first=options_first,
        ).items()
    }

    if read_config and "config" in args:
        result <<= load_config(Path(args["config"]))

    for key, val in args.items():
        key = optvar(key, shadow_builtins=True)
        result[key.split(".")] = val
    return result
