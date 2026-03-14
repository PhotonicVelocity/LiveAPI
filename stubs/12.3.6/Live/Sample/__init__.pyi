from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable
from .Sample import Sample


class SlicingBeatDivision:
    sixteenth: int = 0
    sixteenth_triplett: int = 1
    eighth: int = 2
    eighth_triplett: int = 3
    quarter: int = 4
    quarter_triplett: int = 5
    half: int = 6
    half_triplett: int = 7
    one_bar: int = 8
    two_bars: int = 9
    four_bars: int = 10

class SlicingStyle:
    transient: int = 0
    beat: int = 1
    region: int = 2
    manual: int = 3

class TransientLoopMode:
    off: int = 0
    forward: int = 1
    alternate: int = 2

__all__ = ['Sample', 'SlicingBeatDivision', 'SlicingStyle', 'TransientLoopMode']
