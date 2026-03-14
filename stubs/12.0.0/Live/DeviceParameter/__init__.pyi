from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable
from .DeviceParameter import DeviceParameter


class AutomationState:
    none: int = 0
    playing: int = 1
    overridden: int = 2

class ParameterState:
    enabled: int = 0
    irrelevant: int = 1
    disabled: int = 2

__all__ = ['DeviceParameter', 'AutomationState', 'ParameterState']
