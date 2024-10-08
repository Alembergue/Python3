"""`list` that broadcasts attribute access to its elements."""

# native
from __future__ import annotations
from typing import Any
from typing import List
from typing import SupportsIndex
from typing import TypeVar
from typing import Union

Self = TypeVar("Self", bound="AttrList")
"""`AttrList` instance."""

AttrListKey = Union[SupportsIndex, slice, str]
"""`AttrList` key type."""


def str2index(index: str) -> AttrListKey:
    """Return a slice or numeric index.

    Args:
        index (str): string index to parse

    Returns:
        (slice | int): parsed index

    Examples:
        >>> str2index("-1")
        -1
        >>> str2index("3:5")
        slice(3, 5, None)
        >>> str2index("5:3:-1")
        slice(5, 3, -1)
        >>> str2index("bar")
        'bar'
    """
    if ":" in index:
        return slice(*[int(x) for x in index.split(":")])
    try:
        return int(index, 10)
    except ValueError:
        return index


class AttrList(List[Any]):
    """Collection that broadcasts attribute, index, and function calls to its members.

    Attribute access (`.`) is broadcast to all members. An exception
    is an attribute that exists on the list instance itself.

    >>> nums = AttrList([complex(1, 2), complex(3, 4), complex(5, 6)])
    >>> nums.real
    [1.0, 3.0, 5.0]

    Array access (`[]`) with `int` and `slice` indexes works as usual by returning
    a portion of the list. `string` indexes, however, are broadcast to each member.

    >>> items = AttrList(["Apple", "Bat", "Cat"])
    >>> items[0]
    'Apple'
    >>> items["0"]
    ['A', 'B', 'C']

    Calling the list (`()`) broadcasts the call to all members. Usually, this is
    combined with attribute access:

    >>> items = AttrList(["Apple", "Bat", "Cat"])
    >>> items.lower()
    ['apple', 'bat', 'cat']
    """

    def __getattr__(self, name: str) -> AttrList:
        """Return an attribute from all members.

        Args:
            name (str): attribute name

        Returns:
            (list[any]): value of attribute for each member or `None` if missing

        Examples:
            >>> from . import AttrDict
            >>> items = AttrList([AttrDict(a=1), AttrDict(a=2), AttrDict(a=3, b=4)])
            >>> items.a
            [1, 2, 3]
            >>> items.b
            [None, None, 4]

            Note that instance attributes supersede member attributes:
            >>> object.__setattr__(items, "b", 5)
            >>> items.b
            5
        """
        # NOTE: This method is only called when the attribute cannot be found.
        # We delegate this call to every member.
        result = self.__class__()
        for member in self:
            # if isinstance(member, AttrDict):  # check if name is defined
            #     result.append(member[name] if name in member else None)
            # else:
            result.append(getattr(member, name, None))
        return result

    def __setattr__(self, name: str, value: Any) -> None:
        """Set an attribute on all members (or the list itself).

        Args:
            name (str): attribute name
            value (any): attribute value

        Examples:
            >>> from . import AttrDict
            >>> items = AttrList([AttrDict(a=1), AttrDict(b=2)])
            >>> items.a = 5
            >>> items
            [{'a': 5}, {'b': 2, 'a': 5}]

            Note that instance attributes supersede member attributes:
            >>> object.__setattr__(items, "b", 5)
            >>> items.b = 7
            >>> items.b
            7
        """
        try:
            super().__getattribute__(name)  # is real?
            super().__setattr__(name, value)
        except AttributeError:  # use members
            for member in self:
                setattr(member, name, value)

    def __delattr__(self, name: str) -> None:
        """Delete an attribute from all members (or the list itself).

        Args:
            name (str): attribute name

        Examples:
            >>> from . import AttrDict
            >>> items = AttrList([AttrDict(a=1, b=2), AttrDict(a=2, c=3), dict(d=4)])
            >>> del items.a
            >>> items
            [{'b': 2}, {'c': 3}, {'d': 4}]

            Deleting an instance attribute works:
            >>> object.__setattr__(items, 'b', 5)
            >>> items.b = 7
            >>> items.b
            7
            >>> del items.b # deletes instance attribute
            >>> items
            [{'b': 2}, {'c': 3}, {'d': 4}]
        """
        try:
            super().__getattribute__(name)  # is real?
            super().__delattr__(name)
        except AttributeError:  # use members
            for member in self:
                try:
                    delattr(member, name)
                except AttributeError:
                    pass

    def __getitem__(self: Self, index: AttrListKey) -> Union[Self, Any]:
        """Return an item from all members (or the list itself).

        Args:
            index (int|slice|str): item index

        Returns:
            (any): the item at the index in each member (`str` index) or the
            member at the given index (`int` or `slice`)

        Examples:
            A string index is applied to all members:
            >>> items = AttrList([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> items["-1"]
            [3, 6, 9]

            Normal indexing works as expected:
            >>> items = AttrList([1, 2, 3])
            >>> items[1]
            2
            >>> items[0:2]
            [1, 2]

            Weird indexing throws a `TypeError`:
            >>> items = AttrList([1, 2, 3])
            >>> items[{"a": 1}]
            Traceback (most recent call last):
             ...
            TypeError: list indices must be integers or slices, not dict
        """
        result = self
        if isinstance(index, str):
            index = str2index(index)
            result = self.__class__(item[index] for item in self)
        elif isinstance(index, slice):
            result = self.__class__(super().__getitem__(index))
        else:
            result = super().__getitem__(index)
        return result

    def __setitem__(self, index: AttrListKey, value: Any) -> None:
        """Set an item in all members (or the list itself).

        Args:
            index (int|slice|str): item index
            value (any): item value

        Examples:
            A string index is applied to all members:
            >>> items = AttrList([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> items["0"] = 100
            >>> items
            [[100, 2, 3], [100, 5, 6], [100, 8, 9]]

            Immutable members are untouched:
            >>> items = AttrList(["Cat", [1, 2, 3]])
            >>> items["0"] = "A"
            >>> items
            ['Cat', ['A', 2, 3]]

            Normal indexing works as expected:
            >>> items = AttrList([1, 2, 3])
            >>> items[1] = 5
            >>> items
            [1, 5, 3]

            Weird indexing throws a `TypeError`:
            >>> items = AttrList([1, 2, 3])
            >>> items[{"a": 1}] = 100
            Traceback (most recent call last):
             ...
            TypeError: list indices must be integers or slices, not dict
        """
        if isinstance(index, str):
            index = str2index(index)
            for member in self:
                if hasattr(member, "__setitem__"):
                    member.__setitem__(index, value)
        else:
            super().__setitem__(index, value)

    def __delitem__(self, index: AttrListKey) -> None:
        """Delete an item from all members (or the list itself).

        Args:
            index (int|slice|str): item index

        Examples:
            A string index is applied to all members:
            >>> items = AttrList([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
            >>> del items["0"]
            >>> items
            [[2, 3], [5, 6], [8, 9]]

            Immutable members are untouched:
            >>> items = AttrList(["Cat", [1, 2, 3]])
            >>> del items["-1"]
            >>> items
            ['Cat', [1, 2]]

            Normal indexing works as expected:
            >>> items = AttrList([1, 2, 3])
            >>> del items[1]
            >>> items
            [1, 3]

            Weird indexing throws a `TypeError`:
            >>> items = AttrList([1, 2, 3])
            >>> del items[{"a": 1}]
            Traceback (most recent call last):
             ...
            TypeError: list indices must be integers or slices, not dict
        """
        if isinstance(index, str):
            index = str2index(index)
            for member in self:
                if hasattr(member, "__delitem__"):
                    member.__delitem__(index)
        else:
            super().__delitem__(index)

    def __call__(self: Self, *args: Any, **kwargs: Any) -> Self:
        """Return a new list with the result of calling all callables in the list.

        Args:
            args (*any): arguments to the callable
            kwargs (**any): keyword arguments to the callable

        Returns:
            (Self): new list with results of the callable

        Examples:
            >>> items = AttrList(["a", "b", "c"])
            >>> items.upper()
            ['A', 'B', 'C']

            >>> items = AttrList([lambda x: x + 2, lambda y: y + 5, "Z"])
            >>> items(1)
            [3, 6, 'Z']
        """
        return self.__class__(
            item(*args, **kwargs) if callable(item) else item for item in self
        )


__pdoc__ = {
    "AttrList.__getattr__": True,
    "AttrList.__setattr__": True,
    "AttrList.__delattr__": True,
    "AttrList.__getitem__": True,
    "AttrList.__setitem__": True,
    "AttrList.__delitem__": True,
    "AttrList.__call__": True,
}
