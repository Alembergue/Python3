"""Generally useful functions."""

# native
from typing import Any
from typing import cast
from typing import Dict
from typing import List
from typing import Mapping
from typing import Optional
from typing import Protocol
from typing import runtime_checkable
from typing import Sequence
from typing import Type
from typing import Union

AnyList = List[Any]
"""Generic `list`."""

AnyDict = Dict[Any, Any]
"""Generic `dict`."""

OnlyReadDict = Mapping[Any, Any]
"""`dict` that will only be read."""

AnyListDict = Union[AnyList, AnyDict]
"""Generic `list` or `dict`."""

AnyIndex = Union[str, int, Sequence[Union[str, int]]]
"""Index into a `list` or `dict`."""


@runtime_checkable
class SupportsItem(Protocol):  # pragma: no cover
    """Protocol for `k in x`, `x[k]`, and `x[k] = v`."""

    def __contains__(self, key: Any) -> bool:
        """Return `True` if `key` exists, `False` otherwise."""

    def __getitem__(self, key: Any) -> Any:
        """Return value of `key`."""

    def __setitem__(self, key: Any, value: Any) -> Optional[Any]:
        """Set `key` to `value`."""


def get_path(src: SupportsItem, path: AnyIndex, default: Optional[Any] = None) -> Any:
    """Get the value indicated by `path` or return `default` if it is not found.

    Args:
        src (SupportsItem): typically a `list` or a `dict`
        path (AnyIndex): path to the value
        default (Any, optional): value to return if `path` is not found.
            Defaults to `None`.

    Returns:
        Any: path value or `default` if it is not found.

    Examples:
        >>> get_path({'a': 1}, 'a')
        1
        >>> get_path({'a': [1, {'b': 2}]}, ['a', 1, 'b'])
        2
    """
    if isinstance(path, str) or not isinstance(path, Sequence):
        path = [path]

    result: Any = default
    try:
        for key in path:
            result = src[key]  # take step
            if isinstance(result, SupportsItem):
                src = result  # preserve context
    except (KeyError, IndexError, TypeError):
        # key doesn't exist, index is unreachable, or item is not indexable
        result = default
    return result


def set_path(
    dest: AnyListDict,
    path: AnyIndex,
    value: Any,
    cls_dict: Type[AnyDict] = dict,
    cls_list: Type[AnyList] = list,
) -> AnyListDict:
    """Set a deeply nested value.

    Args:
        dest (Box): a `list` or `dict`

        path (BoxIndex): index or `Sequence` into `dest`

        value (Any): the value to set

        cls_dict (Type[dict], optional): Constructor for `Mapping` objects.
            Defaults to `dict`.

        cls_list (Type[list], optional): Constructor for `List` objects.
            Defaults to `list`.

    Returns:
        Box: `dest` modified according to the `path`. New `dict` and `list`
            objects will be created if they do not exist.

    Examples:
        >>> item = {'a': [{'b': {'c': 3}}]}
        >>> set_path(item, ['a', 0, 'b', 'c'], 4)
        {'a': [{'b': {'c': 4}}]}
        >>> set_path(item, ['a', 1, 'd'], 5)
        {'a': [{'b': {'c': 4}}, {'d': 5}]}
    """
    if isinstance(path, str) or not isinstance(path, Sequence):
        path = [path]

    last = len(path) - 1
    nested = dest
    for index, key in enumerate(path):
        if isinstance(nested, Mapping) and key not in nested:
            nested[key] = None

        if isinstance(nested, List):
            if isinstance(key, int):
                if key >= len(nested):
                    nested.extend([None] * (key + 1 - len(nested)))
            else:  # trying to index into a list with a str
                nested.append(cls_dict([(key, None)]))
                nested = cast(AnyDict, nested[-1])  # switch to dict context
        # nested[key] exists for dict[str | int] and list[int | str]

        # NOTE: `mypy` can't be sure that we aren't trying to index into
        # a `list` with a `str` down below. But we handled this case, so
        # to avoid much duplication, we just call it an `int` which works
        # for `list` and `dict`.
        key = cast(int, key)

        if index == last:
            nested[key] = value
            break  # done

        curr_val = nested[key]
        next_key = path[index + 1]
        if isinstance(next_key, (int, slice)) and not isinstance(curr_val, List):
            nested[key] = cls_list()
        elif isinstance(next_key, str) and not isinstance(curr_val, Mapping):
            nested[key] = cls_dict()

        nested = nested[key]  # move to next step
    return dest


def dict_merge(
    dest: AnyDict,
    *sources: OnlyReadDict,
    cls_dict: Type[AnyDict] = dict,
) -> AnyDict:
    """Generic recursive merge for dict-like objects.

    NOTE: Every nested `dict` will pass through `cls_dict`.

    Args:
        dest (AnyDict): dict into which `sources` are merged

        *sources (OnlyReadDict): dicts to merge

        cls_dict (Type[AnyDict], optional): constructor for default `dict`.
            Defaults to `dict`.

    Returns:
        AnyDict: `dest` now with merged values

    Examples:
        >>> a = {"b": {"c": 1}, "d": 2}
        >>> b = {"b": {"c": 2, "e": 3}, "d": 2}
        >>> c = {"d": {"e": 5}}
        >>> dict_merge(a, b, c)
        {'b': {'c': 2, 'e': 3}, 'd': {'e': 5}}
    """
    for src in sources:
        for key, value in src.items():
            if not isinstance(value, Mapping):
                # overwrite with simple value
                dest[key] = value
                continue

            value = cls_dict(value)
            prev = dest.get(key, {})
            if isinstance(prev, dict):  # extendable
                if not isinstance(prev, cls_dict):
                    prev = cls_dict(prev)
                dest[key] = dict_merge(prev, value, cls_dict=cls_dict)
            else:  # cannot extend
                dest[key] = value
    return dest
