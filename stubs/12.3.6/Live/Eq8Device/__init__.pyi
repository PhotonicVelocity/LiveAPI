from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable
from .Eq8Device import Eq8Device


class EditMode(int):
    a: int = 0
    b: int = 1

class GlobalMode(int):
    stereo: int = 0
    left_right: int = 1
    mid_side: int = 2

__all__ = ['Eq8Device', 'EditMode', 'GlobalMode']
