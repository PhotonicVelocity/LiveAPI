from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable
from .SimplerDevice import SimplerDevice

if TYPE_CHECKING:
    from Live.Base import IntVector



class PlaybackMode(int):
    classic: int = 0
    one_shot: int = 1
    slicing: int = 2

class SlicingPlaybackMode(int):
    mono: int = 0
    poly: int = 1
    thru: int = 2

def get_available_voice_numbers() -> IntVector:
    """Get a vector of valid Simpler voice numbers."""
    ...

__all__ = ['SimplerDevice', 'PlaybackMode', 'SlicingPlaybackMode', 'get_available_voice_numbers']
