from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import Track



class MeldDevice(Device):
    """This class represents a Meld device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_mono_poly_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mono_poly" has changed.
        """
        ...

    def add_poly_voices_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "poly_voices" has changed.
        """
        ...

    def add_selected_engine_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "selected_engine" has changed.
        """
        ...

    def add_unison_voices_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "unison_voices" has changed.
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

    @property
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    @property
    def latency_in_ms(self) -> float:
        """Returns the latency of the device in ms."""
        ...

    @property
    def latency_in_samples(self) -> int:
        """Returns the latency of the device in samples."""
        ...

    @property
    def mono_poly(self) -> int:
        """Returns the mode of Polyphony"""
        ...

    @mono_poly.setter
    def mono_poly(self, value: int) -> None: ...

    def mono_poly_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "mono_poly".
        """
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
    def poly_voices(self) -> int:
        """Return the Poly Voice count"""
        ...

    @poly_voices.setter
    def poly_voices(self, value: int) -> None: ...

    def poly_voices_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "poly_voices".
        """
        ...

    def remove_mono_poly_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "mono_poly".
        """
        ...

    def remove_poly_voices_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "poly_voices".
        """
        ...

    def remove_selected_engine_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "selected_engine".
        """
        ...

    def remove_unison_voices_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "unison_voices".
        """
        ...

    @property
    def selected_engine(self) -> bool:
        """Return what Voice Engine is selected"""
        ...

    @selected_engine.setter
    def selected_engine(self, value: bool) -> None: ...

    def selected_engine_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "selected_engine".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def unison_voices(self) -> int:
        """Return the Unison Voice count"""
        ...

    @unison_voices.setter
    def unison_voices(self, value: int) -> None: ...

    def unison_voices_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "unison_voices".
        """
        ...

    @property
    def view(self) -> Device.View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['MeldDevice']
