from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from . import VoiceCount
    from Live.Base import StringVector
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.DeviceParameter import DeviceParameter
    from Live.Track import Track



class WavetableDevice(Device):
    """This class represents a Wavetable device."""

    class View(Device.View):
        """Representing the view aspects of a Wavetable device."""

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> WavetableDevice:
            """Get the canonical parent of the View."""
            ...

        @property
        def is_collapsed(self) -> bool:
            """Get/Set/Listen if the device is shown collapsed in the device chain."""
            ...

        @is_collapsed.setter
        def is_collapsed(self, value: bool) -> None: ...

    @property
    def _live_ptr(self) -> int:
        ...

    def add_filter_routing_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "filter_routing" has changed.
        """
        ...

    def add_modulation_matrix_changed_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "modulation_matrix_changed" has changed.
        """
        ...

    def add_mono_poly_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "mono_poly" has changed.
        """
        ...

    def add_oscillator_1_effect_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oscillator_1_effect_mode" has changed.
        """
        ...

    def add_oscillator_1_wavetable_category_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oscillator_1_wavetable_category" has changed.
        """
        ...

    def add_oscillator_1_wavetable_index_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oscillator_1_wavetable_index" has changed.
        """
        ...

    def add_oscillator_1_wavetables_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oscillator_1_wavetables" has changed.
        """
        ...

    def add_oscillator_2_effect_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oscillator_2_effect_mode" has changed.
        """
        ...

    def add_oscillator_2_wavetable_category_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oscillator_2_wavetable_category" has changed.
        """
        ...

    def add_oscillator_2_wavetable_index_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oscillator_2_wavetable_index" has changed.
        """
        ...

    def add_oscillator_2_wavetables_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "oscillator_2_wavetables" has changed.
        """
        ...

    def add_parameter_to_modulation_matrix(self, parameter: DeviceParameter | None, /) -> int:
        """Add a non-pitch parameter to the modulation matrix."""
        ...

    def add_poly_voices_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "poly_voices" has changed.
        """
        ...

    def add_unison_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "unison_mode" has changed.
        """
        ...

    def add_unison_voice_count_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "unison_voice_count" has changed.
        """
        ...

    def add_visible_modulation_target_names_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "visible_modulation_target_names" has changed.
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
    def filter_routing(self) -> int:
        """Return the current filter routing."""
        ...

    @filter_routing.setter
    def filter_routing(self, value: int) -> None: ...

    def filter_routing_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "filter_routing".
        """
        ...

    def get_modulation_target_parameter_name(self, target_index: int | None, /) -> str:
        """Get the parameter name of the modulation target at the given index."""
        ...

    def get_modulation_value(self, target_index: int | None, source: int | None, /) -> float:
        """Get the value of a modulation amount for the given target-source connection."""
        ...

    @property
    def is_active(self) -> bool:
        """Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off."""
        ...

    def is_parameter_modulatable(self, parameter: DeviceParameter | None, /) -> bool:
        """Indicate whether the parameter is modulatable. Note that pitch parameters only exist in python and must be handled there."""
        ...

    def modulation_matrix_changed_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "modulation_matrix_changed".
        """
        ...

    @property
    def mono_poly(self) -> int:
        """Return the current voicing mode."""
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
    def oscillator_1_effect_mode(self) -> int:
        """Return the current effect mode of the oscillator 1."""
        ...

    @oscillator_1_effect_mode.setter
    def oscillator_1_effect_mode(self, value: int) -> None: ...

    def oscillator_1_effect_mode_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oscillator_1_effect_mode".
        """
        ...

    @property
    def oscillator_1_wavetable_category(self) -> int:
        """Return the current wavetable category of the oscillator 1."""
        ...

    @oscillator_1_wavetable_category.setter
    def oscillator_1_wavetable_category(self, value: int) -> None: ...

    def oscillator_1_wavetable_category_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oscillator_1_wavetable_category".
        """
        ...

    @property
    def oscillator_1_wavetable_index(self) -> int:
        """Return the current wavetable index of the oscillator 1."""
        ...

    @oscillator_1_wavetable_index.setter
    def oscillator_1_wavetable_index(self, value: int) -> None: ...

    def oscillator_1_wavetable_index_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oscillator_1_wavetable_index".
        """
        ...

    @property
    def oscillator_1_wavetables(self) -> StringVector:
        """Get a vector of oscillator 1's wavetable names."""
        ...

    def oscillator_1_wavetables_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oscillator_1_wavetables".
        """
        ...

    @property
    def oscillator_2_effect_mode(self) -> int:
        """Return the current effect mode of the oscillator 2."""
        ...

    @oscillator_2_effect_mode.setter
    def oscillator_2_effect_mode(self, value: int) -> None: ...

    def oscillator_2_effect_mode_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oscillator_2_effect_mode".
        """
        ...

    @property
    def oscillator_2_wavetable_category(self) -> int:
        """Return the current wavetable category of the oscillator 2."""
        ...

    @oscillator_2_wavetable_category.setter
    def oscillator_2_wavetable_category(self, value: int) -> None: ...

    def oscillator_2_wavetable_category_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oscillator_2_wavetable_category".
        """
        ...

    @property
    def oscillator_2_wavetable_index(self) -> int:
        """Return the current wavetable index of the oscillator 2."""
        ...

    @oscillator_2_wavetable_index.setter
    def oscillator_2_wavetable_index(self, value: int) -> None: ...

    def oscillator_2_wavetable_index_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oscillator_2_wavetable_index".
        """
        ...

    @property
    def oscillator_2_wavetables(self) -> StringVector:
        """Get a vector of oscillator 2's wavetable names."""
        ...

    def oscillator_2_wavetables_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "oscillator_2_wavetables".
        """
        ...

    @property
    def oscillator_wavetable_categories(self) -> StringVector:
        """Get a vector of the available wavetable categories."""
        ...

    @property
    def parameters(self) -> ATimeableValueVector:
        """Const access to the list of available automatable parameters for this device."""
        ...

    @property
    def poly_voices(self) -> int:
        """Return the current number of polyphonic voices. Uses the VoiceCount enumeration."""
        ...

    @poly_voices.setter
    def poly_voices(self, value: int) -> None: ...

    def poly_voices_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "poly_voices".
        """
        ...

    def remove_filter_routing_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "filter_routing".
        """
        ...

    def remove_modulation_matrix_changed_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "modulation_matrix_changed".
        """
        ...

    def remove_mono_poly_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "mono_poly".
        """
        ...

    def remove_oscillator_1_effect_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "oscillator_1_effect_mode".
        """
        ...

    def remove_oscillator_1_wavetable_category_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "oscillator_1_wavetable_category".
        """
        ...

    def remove_oscillator_1_wavetable_index_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "oscillator_1_wavetable_index".
        """
        ...

    def remove_oscillator_1_wavetables_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "oscillator_1_wavetables".
        """
        ...

    def remove_oscillator_2_effect_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "oscillator_2_effect_mode".
        """
        ...

    def remove_oscillator_2_wavetable_category_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "oscillator_2_wavetable_category".
        """
        ...

    def remove_oscillator_2_wavetable_index_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "oscillator_2_wavetable_index".
        """
        ...

    def remove_oscillator_2_wavetables_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "oscillator_2_wavetables".
        """
        ...

    def remove_poly_voices_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "poly_voices".
        """
        ...

    def remove_unison_mode_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "unison_mode".
        """
        ...

    def remove_unison_voice_count_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "unison_voice_count".
        """
        ...

    def remove_visible_modulation_target_names_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "visible_modulation_target_names".
        """
        ...

    def set_modulation_value(self, target_index: int | None, source: int | None, value: float | None, /) -> None:
        """Set the value of a modulation amount for the given target-source connection."""
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def unison_mode(self) -> int:
        """Return the current unison mode."""
        ...

    @unison_mode.setter
    def unison_mode(self, value: int) -> None: ...

    def unison_mode_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "unison_mode".
        """
        ...

    @property
    def unison_voice_count(self) -> int:
        """Return the current number of unison voices."""
        ...

    @unison_voice_count.setter
    def unison_voice_count(self, value: int) -> None: ...

    def unison_voice_count_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "unison_voice_count".
        """
        ...

    @property
    def view(self) -> View:
        """Representing the view aspects of a device."""
        ...

    @property
    def visible_modulation_target_names(self) -> StringVector:
        """Get the names of all the visible modulation targets."""
        ...

    def visible_modulation_target_names_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "visible_modulation_target_names".
        """
        ...

__all__ = ['WavetableDevice']
