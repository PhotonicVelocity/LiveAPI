from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import StringVector
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import Track



class HybridReverbDevice(Device):
    """This class represents a Hybrid Reverb device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_ir_attack_time_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "ir_attack_time" has changed.
        """
        ...

    def add_ir_category_index_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "ir_category_index" has changed.
        """
        ...

    def add_ir_decay_time_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "ir_decay_time" has changed.
        """
        ...

    def add_ir_file_index_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "ir_file_index" has changed.
        """
        ...

    def add_ir_file_list_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "ir_file_list" has changed.
        """
        ...

    def add_ir_size_factor_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "ir_size_factor" has changed.
        """
        ...

    def add_ir_time_shaping_on_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "ir_time_shaping_on" has changed.
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
    def ir_attack_time(self) -> float:
        """Return the current IrAttackTime"""
        ...

    @ir_attack_time.setter
    def ir_attack_time(self, value: float) -> None: ...

    def ir_attack_time_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "ir_attack_time".
        """
        ...

    @property
    def ir_category_index(self) -> int:
        """Return the current IR category index"""
        ...

    @ir_category_index.setter
    def ir_category_index(self, value: int) -> None: ...

    def ir_category_index_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "ir_category_index".
        """
        ...

    @property
    def ir_category_list(self) -> StringVector:
        """Return the current IR categories list"""
        ...

    @property
    def ir_decay_time(self) -> float:
        """Return the current IrDecayTime"""
        ...

    @ir_decay_time.setter
    def ir_decay_time(self, value: float) -> None: ...

    def ir_decay_time_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "ir_decay_time".
        """
        ...

    @property
    def ir_file_index(self) -> int:
        """Return the current IR file index"""
        ...

    @ir_file_index.setter
    def ir_file_index(self, value: int) -> None: ...

    def ir_file_index_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "ir_file_index".
        """
        ...

    @property
    def ir_file_list(self) -> StringVector:
        """Return the current IR file list"""
        ...

    def ir_file_list_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "ir_file_list".
        """
        ...

    @property
    def ir_size_factor(self) -> float:
        """Return the current IrSizeFactor"""
        ...

    @ir_size_factor.setter
    def ir_size_factor(self, value: float) -> None: ...

    def ir_size_factor_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "ir_size_factor".
        """
        ...

    @property
    def ir_time_shaping_on(self) -> bool:
        """Return the current IrTimeShapingOn"""
        ...

    @ir_time_shaping_on.setter
    def ir_time_shaping_on(self, value: bool) -> None: ...

    def ir_time_shaping_on_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "ir_time_shaping_on".
        """
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
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def parameters(self) -> ATimeableValueVector:
        """Const access to the list of available automatable parameters for this device."""
        ...

    def remove_ir_attack_time_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "ir_attack_time".
        """
        ...

    def remove_ir_category_index_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "ir_category_index".
        """
        ...

    def remove_ir_decay_time_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "ir_decay_time".
        """
        ...

    def remove_ir_file_index_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "ir_file_index".
        """
        ...

    def remove_ir_file_list_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "ir_file_list".
        """
        ...

    def remove_ir_size_factor_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "ir_size_factor".
        """
        ...

    def remove_ir_time_shaping_on_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "ir_time_shaping_on".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    @property
    def view(self) -> Track.View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['HybridReverbDevice']
