from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')

if TYPE_CHECKING:
    from Live.LomObject import LomObject



class FloatVector(Vector[float]):
    """A simple container for returning floats from Live."""

    def append(self, value: float | None, /) -> None:
        ...

    def extend(self, values: Iterable[float] | None, /) -> None:
        ...

class IntVector(Vector[int]):
    """A simple container for returning integers from Live."""

    def append(self, value: int | None, /) -> None:
        ...

    def extend(self, values: Iterable[int] | None, /) -> None:
        ...

class LimitationError(Exception): ...

class ObjectVector(Vector[object]):
    """A simple read only container for returning python objects."""

    def append(self, value: Any | None, /) -> None:
        ...

    def extend(self, values: Iterable[object] | None, /) -> None:
        ...

class StringVector(Vector[str]):
    """A simple container for returning strings from Live."""

    def append(self, value: str | None, /) -> None:
        ...

    def extend(self, values: Iterable[str] | None, /) -> None:
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
    def __getitem__(self, index: slice) -> Vector[T]: ...

    def __getitem__(self, index: int | slice) -> T | Vector[T]: ...

    def __len__(self) -> int: ...

    def __contains__(self, value: object) -> bool: ...

    def __bool__(self) -> bool: ...

    def append(self, value: LomObject | None, /) -> None:
        ...

    def extend(self, values: Iterable[LomObject] | None, /) -> None:
        ...

def log(string: str | None, /) -> None:
    ...

__all__ = ['FloatVector', 'IntVector', 'LimitationError', 'ObjectVector', 'StringVector', 'Timer', 'Vector', 'log']
