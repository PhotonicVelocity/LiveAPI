from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.LomObject import LomObject



class FloatVector:
    """A simple container for returning floats from Live."""

    def append(self, value: float, /) -> None:
        ...

    def extend(self, values: Iterable[float], /) -> None:
        ...

class IntU64Vector:
    """A simple container for returning unsigned long integers from Live."""

    def append(self, value: int, /) -> None:
        ...

    def extend(self, values: Iterable[int], /) -> None:
        ...

class IntVector:
    """A simple container for returning integers from Live."""

    def append(self, value: int, /) -> None:
        ...

    def extend(self, values: Iterable[int], /) -> None:
        ...

class LimitationError(Exception):
    ...

class ObjectVector:
    """A simple read only container for returning python objects."""

    def append(self, value: object, /) -> None:
        ...

    def extend(self, values: object, /) -> None:
        ...

class StringVector:
    """A simple container for returning strings from Live."""

    def append(self, value: str, /) -> None:
        ...

    def extend(self, values: Iterable[str], /) -> None:
        ...

class Text:
    """A translatable, immutable string."""

    ...

class Timer:
    """A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback every interval. Errors in the callback will stop the timer."""

    def restart(self) -> None:
        ...

    @property
    def running(self) -> bool:
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

class Vector:
    """A simple read only container for returning objects from Live."""

    def append(self, value: LomObject, /) -> None:
        ...

    def extend(self, values: Iterable[LomObject], /) -> None:
        ...

def get_text(classname: str, textname: str, /) -> Text:
    """Retrieves the (translated) Text identified by `classname` and `textname`."""
    ...

def log(arg1: str, /) -> None:
    ...

def subst_args(text: Text, arg1: str = '', arg2: str = '', arg3: str = '', arg4: str = '', arg5: str = '', /) -> str:
    ...
__all__ = ['FloatVector', 'IntU64Vector', 'IntVector', 'LimitationError', 'ObjectVector', 'StringVector', 'Text', 'Timer', 'Vector', 'get_text', 'log', 'subst_args']
