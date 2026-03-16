from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from . import AutomationState
    from Live.Base import StringVector
    from Live.Device import Device
    from Live.LomObject import LomObject



class DeviceParameter(LomObject):
    """
    This class represents a (automatable) parameter within a MIDI or
    Audio DSP-Device.
    """

    @property
    def _live_ptr(self) -> int:
        ...

    def add_automation_state_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "automation_state" has changed.
        """
        ...

    def add_name_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "name" has changed.
        """
        ...

    def add_state_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "state" has changed.
        """
        ...

    def add_value_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "value" has changed.
        """
        ...

    @property
    def automation_state(self) -> int:
        """Returns state of type AutomationState."""
        ...

    def automation_state_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "automation_state".
        """
        ...

    def begin_gesture(self) -> None:
        """Notify the begin of a modification of the parameter, when a sequence of modifications have to be consider a consistent group -- for Sexample, when recording automation."""
        ...

    @property
    def canonical_parent(self) -> Device:
        """Get the canonical parent of the device parameter."""
        ...

    @property
    def default_value(self) -> float:
        """
        Return the default value for this parameter.  A Default value is only
        available for non-quantized parameter types (see 'is_quantized').
        """
        ...

    def end_gesture(self) -> None:
        """Notify the end of a modification of the parameter. See begin_gesture."""
        ...

    @property
    def is_enabled(self) -> bool:
        """Returns false if the parameter has been macro mapped or disabled by Max."""
        ...

    @property
    def is_quantized(self) -> bool:
        """
        Returns True, if this value is a boolean or integer like switch.
        Non quantized values are continues float values.
        """
        ...

    @property
    def max(self) -> float:
        """
        Returns const access to the upper value of the allowed range for
        this parameter
        """
        ...

    @property
    def min(self) -> float:
        """
        Returns const access to the lower value of the allowed range for
        this parameter
        """
        ...

    @property
    def name(self) -> str:
        """
        Returns const access the name of this parameter, as visible in Lives
        automation choosers.
        """
        ...

    def name_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "name".
        """
        ...

    @property
    def original_name(self) -> str:
        """
        Returns const access the original name of this parameter, unaffected of
        any renamings.
        """
        ...

    def re_enable_automation(self) -> None:
        """Reenable automation for this parameter."""
        ...

    def remove_automation_state_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "automation_state".
        """
        ...

    def remove_name_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "name".
        """
        ...

    def remove_state_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "state".
        """
        ...

    def remove_value_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "value".
        """
        ...

    @property
    def short_value_items(self) -> StringVector:
        """Return the list of possible values for this parameter. Like value_items, but prefers short value names if available. Raises an error if 'is_quantized' is False."""
        ...

    @property
    def state(self) -> int:
        """
        Returns the state of the parameter:
        - enabled - the parameter's value can be changed,
        - irrelevant - the parameter is enabled, but value changes will not take any effect until it gets enabled,
        - disabled - the parameter's value cannot be changed.
        """
        ...

    def state_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "state".
        """
        ...

    def str_for_value(self, value: float | None, /) -> str:
        """
        Return a string representation of the given value. To be used
        for display purposes only. This value can include characters like 'db' or
        'hz', depending on the type of the parameter.
        """
        ...

    @property
    def value(self) -> float:
        """
        Get/Set the current value (as visible in the GUI) this parameter.
        The value must be inside the min/max properties of this device.
        """
        ...

    @value.setter
    def value(self, value: float) -> None: ...

    def value_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "value".
        """
        ...

    @property
    def value_items(self) -> StringVector:
        """Return the list of possible values for this parameter. Raises an error if 'is_quantized' is False."""
        ...

__all__ = ['DeviceParameter']
