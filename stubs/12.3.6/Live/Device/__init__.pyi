from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable
from .Device import Device

if TYPE_CHECKING:
    from Live.DeviceParameter import DeviceParameter



class ATimeableValueVector:

    def append(self, value: DeviceParameter | None) -> None:
        ...

    def extend(self, values: DeviceParameter | None) -> None:
        ...

class DeviceType:
    """The type of the device."""
    undefined: int = 0
    instrument: int = 1
    audio_effect: int = 2
    midi_effect: int = 4

__all__ = ['Device', 'ATimeableValueVector', 'DeviceType']
