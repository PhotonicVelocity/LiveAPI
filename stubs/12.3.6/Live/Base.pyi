from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, Self, TypeVar, overload

T = TypeVar('T', covariant=True)

if TYPE_CHECKING:
    from Live.Base import Vector



class FloatVector(Vector[float]):
    """A simple container for returning floats from Live."""

    def append(self, value: float, /) -> None: ...

    def extend(self, values: Iterable[float], /) -> None: ...

class IntU64Vector(Vector[int]):
    """A simple container for returning unsigned long integers from Live."""

    def append(self, value: int, /) -> None: ...

    def extend(self, values: Iterable[int], /) -> None: ...

class IntVector(Vector[int]):
    """A simple container for returning integers from Live."""

    def append(self, value: int, /) -> None: ...

    def extend(self, values: Iterable[int], /) -> None: ...

class LimitationError(Exception): ...

class ObjectVector(Vector[object]):
    """A simple read only container for returning python objects."""

    def append(self, value: object, /) -> None: ...

    def extend(self, values: Iterable[object], /) -> None: ...

class StringVector(Vector[str]):
    """A simple container for returning strings from Live."""

    def append(self, value: str, /) -> None: ...

    def extend(self, values: Iterable[str], /) -> None: ...

class Text:
    """A translatable, immutable string."""

    @property
    def text(self) -> str:
        ...

class Timer:
    """A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback every interval. Errors in the callback will stop the timer."""

    def __init__(self, callback: object, interval: int, repeat: bool = False, start: bool = False) -> None: ...

    def restart(self) -> None:
        ...

    @property
    def running(self) -> bool:
        ...

    def start(self) -> None:
        ...

    def stop(self) -> None:
        ...

class Vector(Generic[T]):
    """A simple read only container for returning objects from Live."""

    def __iter__(self) -> Iterator[T]: ...

    @overload
    def __getitem__(self, index: int) -> T: ...

    @overload
    def __getitem__(self, index: slice) -> Self: ...

    def __getitem__(self, index: int | slice) -> T | Self: ...

    def __len__(self) -> int: ...

    def __contains__(self, value: object) -> bool: ...

    def __bool__(self) -> bool: ...

def get_text(classname: str, textname: str, /) -> Text:
    """Retrieves the (translated) Text identified by `classname` and `textname`."""
    ...

def log(string: str, /) -> None:
    ...

def subst_args(text: Text, arg1: str = '', arg2: str = '', arg3: str = '', arg4: str = '', arg5: str = '', /) -> str:
    ...

__all__ = ['FloatVector', 'IntU64Vector', 'IntVector', 'LimitationError', 'ObjectVector', 'StringVector', 'Text', 'Timer', 'Vector', 'get_text', 'log', 'subst_args']
