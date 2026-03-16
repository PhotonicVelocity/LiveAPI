from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable
from .ClipSlot import ClipSlot


class ClipSlotPlayingState(int):
    stopped: int = 0
    started: int = 1
    recording: int = 2

__all__ = ['ClipSlot', 'ClipSlotPlayingState']
