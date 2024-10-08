"""`dict` with attribute access, deep selectors, and merging."""

# native
from __future__ import annotations
from typing import Any
from typing import Dict
from typing import Mapping
from typing import Optional
from typing import TypeVar

# pkg
from .fn import AnyIndex
from .fn import dict_merge
from .fn import get_path
from .fn import set_path

__all__ = ["AttrDict"]


Self = TypeVar("Self", bound="AttrDict")
"""`AttrDict` instance."""

NOT_FOUND = object()
"""Sentinel for a missing object."""


class AttrDict(Dict[str, Any]):
    """Like a `dict`, but with attribute syntax.

    NOTE: We do not throw `AttributeError` or `KeyError` because accessing
    a non-existent key or attribute returns `None`.

    Examples:
        >>> AttrDict({"a": 1}).a
        1
    """

    def copy(self: Self) -> Self:
        """Return a shallow copy.

        Examples:
            >>> items = AttrDict(a=1)
            >>> clone = items.copy()
            >>> items == clone # same contents
            True
            >>> items is not clone # different pointers
            True
            >>> clone.a = 5
            >>> items != clone
            True
        """
        return self.__class__(super().copy())

    def __contains__(self, name: Any) -> bool:
        """Return `True` if `name` is a key.

        Args:
            name (Any): typically a `AnyIndex`. If it's a string,
                the check proceeds as usual. If it's a `Sequence`, the
                checks are performed using `.get()`.

        Returns:
            bool: `True` if the `name` is a valid key, `False` otherwise.

        Examples:
            Normal checking works as expected:
            >>> items = AttrDict(a=1, b=2)
            >>> 'a' in items
            True
            >>> 'x' in items
            False

            Nested checks are also possible:
            >>> items = AttrDict(a=[{"b": 2}, {"b": 3}])
            >>> ['a', 0, 'b'] in items
            True
            >>> ['a', 1, 'x'] in items
            False
        """
        return self.get(name, NOT_FOUND) is not NOT_FOUND

    def __getattr__(self, name: str) -> Optional[Any]:
        """Return the value of the attribute or `None`.

        Args:
            name (str): attribute name

        Returns:
            Any: attribute value or `None` if the attribute is missing

        Examples:
            Typically, attributes are the same as key/values:
            >>> item = AttrDict(a=1)
            >>> item.a
            1
            >>> item['a']
            1

            However, instance attributes supersede key/values:
            >>> item = AttrDict(b=1)
            >>> object.__setattr__(item, 'b', 2)
            >>> item.b
            2
            >>> item['b']
            1

            Missing attributes return `None`:
            >>> item = AttrDict(a=1)
            >>> item.b is None
            True
        """
        # NOTE: This method is only called when the attribute cannot be found.
        return self[name]

    def __setattr__(self, name: str, value: Any) -> None:
        """Set the value of an attribute.

        Args:
            name (str): attribute name
            value (Any): value to set

        Examples:
            Setting an attribute is usually the same as a key/value:
            >>> item = AttrDict()
            >>> item.a = 1
            >>> item.a
            1
            >>> item['a']
            1

            However, instance attributes supersede key/values:
            >>> item = AttrDict()
            >>> object.__setattr__(item, 'b', 2)
            >>> item.b
            2
            >>> item.b = 3  # instance attribute updated
            >>> item.b
            3
            >>> item['b'] is None
            True
        """
        try:
            super().__getattribute__(name)  # is real?
            super().__setattr__(name, value)
        except AttributeError:  # use key/value
            self[name] = value

    def __delattr__(self, name: str) -> None:
        """Delete an attribute.

        Args:
            name (str): attribute name

        Examples:
            Deleting an attribute usually deletes the underlying key/value:
            >>> item = AttrDict(a=1)
            >>> del item.a
            >>> item
            {}

            However, instance attributes supersede key/values:
            >>> item = AttrDict(b=1)
            >>> object.__setattr__(item, 'b', 2)
            >>> item.b  # real attribute supersedes key/value
            2
            >>> del item.b  # deletes real attribute
            >>> object.__getattribute__(item, 'b') # instance attribute gone
            Traceback (most recent call last):
             ...
            AttributeError: 'AttrDict' object has no attribute 'b'
            >>> item
            {'b': 1}
        """
        try:
            super().__getattribute__(name)  # is real?
            super().__delattr__(name)
        except AttributeError:  # use key/value
            del self[name]

    def __getitem__(self, name: AnyIndex) -> Optional[Any]:
        """Return the value of the key.

        Args:
            name (AnyIndex): key name or Sequence of the path to a key

        Returns:
            Any: value of the key or `None` if it cannot be found

        Examples:
            >>> item = AttrDict(a=1)
            >>> item['a']
            1
            >>> item['b'] is None
            True
        """
        return self.get(name)

    def __setitem__(self, name: AnyIndex, value: Any) -> None:
        """Set the value of a key.

        Args:
            name (BoxIndex): key name
            value (Any): key value

        Examples:
            >>> item = AttrDict(a=1)
            >>> item['a'] = 5
            >>> item['a']
            5

            >>> item[['a', 'b']] = 10
            >>> item.a.b
            10
        """
        self.set(name, value)

    def __delitem__(self, name: str) -> None:
        """Delete a key.

        Args:
            name (str): key name

        Examples:
            >>> item = AttrDict(a=1)
            >>> del item['a']
            >>> item
            {}

            Deleting missing keys has no effect:
            >>> item = AttrDict(a=1)
            >>> del item['b']
            >>> item
            {'a': 1}
        """
        try:
            super().__delitem__(name)
        except KeyError:
            pass

    def get(self, path: AnyIndex, default: Optional[Any] = None, /) -> Optional[Any]:
        """Return the value at `path` or `default` if it cannot be found.

        Args:
            path (AnyIndex): path to the value
            default (Any, optional): value to return if `name` is not found.
                Defaults to `None`.

        Returns:
            Optional[Any]: key value or `default` if the key is not found

        Examples:
            Normal `.get` functions work:
            >>> items = AttrDict(a=dict(b=[{"c": 3}, {"c": -10}]), d=4)
            >>> items.get('d') == 4
            True
            >>> items.get('e') is None
            True
            >>> items.get('e', 5) == 5
            True

            But you can also indexing into nested `list` and `dict`:
            >>> items.get(['a', 'b', 1, 'c']) == -10
            True

            Bad indexing will just return the default:
            >>> items.get(['e']) is None # key doesn't exist
            True
            >>> items.get(['a', 'b', 5]) is None  # index unreachable
            True
            >>> items.get(['d', 'e']) is None # int is not indexable
            True
        """
        if isinstance(path, str):
            return super().get(path, default)
        return get_path(self, path, default)

    def set(self: Self, path: AnyIndex, value: Optional[Any] = None, /) -> Self:
        """Set key at `path` to `value`.

        Args:
            path (AnyIndex): path to the key to set.
            value (Any, optional): value to set. Defaults to `None`.

        Returns:
            Self: for chaining

        Examples:
            >>> items = AttrDict({"a": 1})
            >>> items.set("b", 2)
            {'a': 1, 'b': 2}

            You can set values deeper:
            >>> items.set(["b", "c", "d"], 5)
            {'a': 1, 'b': {'c': {'d': 5}}}

            You can also use a `tuple` (or other Sequence):
            >>> items.set(("b", "c", "d"), 10)
            {'a': 1, 'b': {'c': {'d': 10}}}

            An empty `Sequence` performs no action:
            >>> items.set((), 20)
            {'a': 1, 'b': {'c': {'d': 10}}}
        """
        if isinstance(path, str):
            super().__setitem__(path, value)
            return self

        set_path(self, path, value, self.__class__)
        return self

    def __lshift__(self: Self, other: Mapping[str, Any]) -> Self:
        """Merge `other` into `self`.

        NOTE: Any nested dictionaries will be converted to `AttrDict` objects.

        Args:
            other (Mapping[str, Any]): other dictionary to merge

        Returns:
            AttrDict: merged dictionary

        Examples:
            >>> item = AttrDict(a=1, b=2)
            >>> item <<= {"b": 3}
            >>> item.b
            3

            >>> item << {"b": 2, "c": {"d": 4}} << {"c": {"d": {"e": 5}}}
            {'a': 1, 'b': 2, 'c': {'d': {'e': 5}}}
            >>> item.c.d.e
            5
        """
        dict_merge(self, other, cls_dict=self.__class__)
        return self


__pdoc__ = {
    "AttrDict.__contains__": True,
    "AttrDict.__getattr__": True,
    "AttrDict.__setattr__": True,
    "AttrDict.__delattr__": True,
    "AttrDict.__getitem__": True,
    "AttrDict.__setitem__": True,
    "AttrDict.__delitem__": True,
    "AttrDict.__lshift__": True,
}
