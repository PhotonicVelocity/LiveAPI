from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable


class LomObject:
    """this is the base class for an object that is accessible via the LOM"""

    @property
    def _live_ptr(self) -> int:
        ...

    @property
    def canonical_parent(self) -> LomObject | None:
        """Get the canonical parent — the structural owner one step up the LOM tree."""
        ...

__all__ = ['LomObject']
