from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable
from .DeviceParameter import DeviceParameter


class AutomationState(int):
    none: int = 0
    playing: int = 1
    overridden: int = 2

class ParameterState(int):
    enabled: int = 0
    irrelevant: int = 1
    disabled: int = 2

__all__ = ['DeviceParameter', 'AutomationState', 'ParameterState']
