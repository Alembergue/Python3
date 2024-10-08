"""Attribute-based data structures.

.. include:: ../../README.md
   :start-line: 4
"""

# pkg
from .attrdict import __pdoc__ as doc1
from .attrdict import AttrDict
from .attrlist import __pdoc__ as doc2
from .attrlist import AttrList

from .jsend import JSend

from .env import load_env
from .config import load_config
from .config import parse_docopt


__version__ = "0.1.5"
__all__ = (
    "__version__",
    "AttrDict",
    "AttrList",
    "JSend",
    "load_env",
    "load_config",
    "parse_docopt",
)

# Update pdoc at all levels.
__pdoc__ = {}
for doc in [doc1, doc2]:
    __pdoc__.update(doc)
