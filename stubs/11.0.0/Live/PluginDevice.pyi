from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import StringVector
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import Track
    from Live.WavetableDevice import WavetableDevice



class PluginDevice(Device):
    """This class represents a plugin device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_presets_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "presets" has changed.
        """
        ...

    def add_selected_preset_index_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "selected_preset_index" has changed.
        """
        ...

    @property
    def can_have_chains(self) -> bool:
        """Returns true if the device is a rack."""
        ...

    @property
    def can_have_drum_pads(self) -> bool:
        """Returns true if the device is a drum rack."""
        ...

    @property
    def canonical_parent(self) -> Track:
        """Get the canonical parent of the Device."""
        ...

    @property
    def class_display_name(self) -> str:
        """Return const access to the name of the device's class name as displayed in Live's browser and device chain"""
        ...

    @property
    def class_name(self) -> str:
        """Return const access to the name of the device's class."""
        ...

    def get_parameter_names(self, begin: int = 0, end: int = -1, /) -> StringVector:
        """
        Get the range of plugin parameter names, bound by begin and end.
        If end is smaller than 0 it is interpreted as the parameter count.
        """
        ...

    @property
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    @property
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def parameters(self) -> ATimeableValueVector:
        """Const access to the list of available automatable parameters for this device."""
        ...

    @property
    def presets(self) -> StringVector:
        """Get the list of presets the plugin offers."""
        ...

    def presets_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "presets".
        """
        ...

    def remove_presets_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "presets".
        """
        ...

    def remove_selected_preset_index_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "selected_preset_index".
        """
        ...

    @property
    def selected_preset_index(self) -> int:
        """Access to the index of the currently selected preset."""
        ...

    @selected_preset_index.setter
    def selected_preset_index(self, value: int) -> None: ...

    def selected_preset_index_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "selected_preset_index".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def view(self) -> WavetableDevice.View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['PluginDevice']
