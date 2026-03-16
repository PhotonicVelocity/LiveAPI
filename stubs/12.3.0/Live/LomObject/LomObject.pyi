from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable


class LomObject:
    """this is the base class for an object that is accessible via the LOM"""

    @property
    def _live_ptr(self) -> int:
        ...

__all__ = ['LomObject']
