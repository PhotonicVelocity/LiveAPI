from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable
from .Groove import Groove


class Base(int):
    gb_four: int = 0
    gb_eight: int = 1
    gb_eight_triplet: int = 2
    gb_sixteen: int = 3
    gb_sixteen_triplet: int = 4
    gb_thirtytwo: int = 5
    count: int = 6

__all__ = ['Groove', 'Base']
