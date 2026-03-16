from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import Track



class Eq8Device:
    """This class represents an Eq8 device."""

    class View:
        """Representing the view aspects of an Eq8 device."""

        @property
        def _live_ptr(self) -> int:
            ...

        def add_selected_band_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "selected_band" has changed.
            """
            ...

        @property
        def canonical_parent(self) -> Eq8Device:
            """Get the canonical parent of the View."""
            ...

        @property
        def is_collapsed(self) -> bool:
            """Get/Set/Listen if the device is shown collapsed in the device chain."""
            ...

        @is_collapsed.setter
        def is_collapsed(self, value: bool) -> None: ...

        def remove_selected_band_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "selected_band".
            """
            ...

        @property
        def selected_band(self) -> int:
            """Access to the selected filter band."""
            ...

        @selected_band.setter
        def selected_band(self, value: int) -> None: ...

        def selected_band_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "selected_band".
            """
            ...

    @property
    def _live_ptr(self) -> int:
        ...

    def add_edit_mode_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "edit_mode" has changed.
        """
        ...

    def add_global_mode_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "global_mode" has changed.
        """
        ...

    def add_oversample_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oversample" has changed.
        """
        ...

    @property
    def can_compare_ab(self) -> bool:
        """Returns true if the Device has the capability to AB compare."""
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

    @property
    def edit_mode(self) -> bool:
        """Access to Eq8's edit mode."""
        ...

    @edit_mode.setter
    def edit_mode(self, value: bool) -> None: ...

    def edit_mode_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "edit_mode".
        """
        ...

    @property
    def global_mode(self) -> int:
        """Access to Eq8's global mode."""
        ...

    @global_mode.setter
    def global_mode(self, value: int) -> None: ...

    def global_mode_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "global_mode".
        """
        ...

    @property
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    @property
    def is_using_compare_preset_b(self) -> bool:
        """Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors."""
        ...

    @is_using_compare_preset_b.setter
    def is_using_compare_preset_b(self, value: bool) -> None: ...

    @property
    def latency_in_ms(self) -> float:
        """Returns the latency of the device in ms."""
        ...

    @property
    def latency_in_samples(self) -> int:
        """Returns the latency of the device in samples."""
        ...

    @property
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def oversample(self) -> bool:
        """Access to Eq8's oversample value."""
        ...

    @oversample.setter
    def oversample(self, value: bool) -> None: ...

    def oversample_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oversample".
        """
        ...

    @property
    def parameters(self) -> ATimeableValueVector:
        """Const access to the list of available automatable parameters for this device."""
        ...

    def remove_edit_mode_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "edit_mode".
        """
        ...

    def remove_global_mode_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "global_mode".
        """
        ...

    def remove_oversample_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "oversample".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def view(self) -> View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['Eq8Device']
