#!/usr/bin/env python
# coding: utf-8
"""Standard JSON responses."""

# native
from __future__ import annotations
from typing import Any, Dict, Optional

# pkg
from .attrdict import AttrDict

# Response status
STATUS_SUCCESS = "success"
STATUS_FAIL = "fail"
STATUS_ERROR = "error"

Msg = Optional[str]


class JSend(AttrDict):
    """Service response object.

    This object loosely conforms to the
    [JSend specification](https://labs.omniti.com/labs/jsend).
    """

    def __init__(self, *args: Any, **kwargs: Dict[str, Any]):
        """Construct a JSend object.

        Examples:
            >>> result = JSend()
            >>> result.ok
            True
            >>> result.status == 'success'
            True
            >>> result.data is None
            True
            >>> result == {'ok': True, 'status': 'success', 'data': None}
            True
        """
        self.update(ok=True, status=STATUS_SUCCESS, data=None)
        super().__init__(*args, **kwargs)

    def fail(self, message: Msg = None) -> JSend:
        """Indicate a controlled failure.

        Args:
            message (str): human-readable explanation of the failure

        Returns:
            JSend: self for chaining

        Examples:
            >>> result = JSend()
            >>> msg = 'Missing a phone number.'
            >>> result.fail(msg) is result
            True
            >>> result.ok is False
            True
            >>> result.status == 'fail'
            True
            >>> result.message == msg
            True
        """
        self.update(ok=False, status=STATUS_FAIL, message=message)
        return self

    def error(self, message: Msg = None, code: Optional[Any] = None) -> JSend:
        """Indicate an uncontrolled error.

        Args:
            message (str): human-readable explanation of the error
            code (Any, optional): technical indication of the error

        Returns:
            JSend: self for chaining

        Examples:
            >>> result = JSend()
            >>> msg = 'No such file [file.text].'
            >>> code = 13
            >>> result.error(msg, code) is result
            True
            >>> result.ok is False
            True
            >>> result.status == 'error'
            True
            >>> result.message == msg
            True
            >>> result.code == code
            True
        """
        self.update(ok=False, status=STATUS_ERROR, message=message, code=code)
        return self

    def success(self, data: Optional[Any] = None) -> JSend:
        """Indicate a successful response.

        Args:
            data (Any, optional): response payload

        Returns:
            JSend: self for chaining

        Examples:
            >>> data = "Works"
            >>> result = JSend()
            >>> result.success(data) is result
            True
            >>> result.data == data
            True
        """
        self.update(ok=True, status=STATUS_SUCCESS, data=data)
        return self
