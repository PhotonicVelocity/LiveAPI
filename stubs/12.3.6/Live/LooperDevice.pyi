from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from Live.Base import StringVector
    from Live.Clip import Clip
    from Live.ClipSlot import ClipSlot
    from Live.Device import ATimeableValueVector, Device, DeviceType
    from Live.Track import Track



class LooperDevice(Device):
    """This class represents a Looper device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_loop_length_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "loop_length" has changed.
        """
        ...

    def add_overdub_after_record_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "overdub_after_record" has changed.
        """
        ...

    def add_record_length_index_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "record_length_index" has changed.
        """
        ...

    def add_tempo_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "tempo" has changed.
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

    def clear(self) -> None:
        """Erase Looper's recorded content."""
        ...

    def double_length(self) -> None:
        """Double the length of Looper's buffer."""
        ...

    def double_speed(self) -> None:
        """Double the speed of Looper's playback."""
        ...

    def export_to_clip_slot(self, clip_slot: ClipSlot | None, /) -> None:
        """Export Looper's content to a Session Clip Slot."""
        ...

    def half_length(self) -> None:
        """Halve the length of Looper's buffer."""
        ...

    def half_speed(self) -> None:
        """Halve the speed of Looper's playback."""
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
    def loop_length(self) -> float:
        """The length of Looper's buffer."""
        ...

    def loop_length_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "loop_length".
        """
        ...

    @property
    def name(self) -> str:
        """Return access to the name of the device."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    def overdub(self) -> None:
        """Play back while adding additional layers of incoming audio."""
        ...

    @property
    def overdub_after_record(self) -> bool:
        """If true, Looper will switch to overdub after recording, when recording a fixed number of bars. Otherwise, the switch will be to playback without overdubbing."""
        ...

    @overdub_after_record.setter
    def overdub_after_record(self, value: bool) -> None: ...

    def overdub_after_record_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "overdub_after_record".
        """
        ...

    @property
    def parameters(self) -> ATimeableValueVector:
        """Const access to the list of available automatable parameters for this device."""
        ...

    def play(self) -> None:
        """Play back without overdubbing."""
        ...

    def record(self) -> None:
        """Record incoming audio."""
        ...

    @property
    def record_length_index(self) -> int:
        """Access to the Record Length chooser entry index."""
        ...

    @record_length_index.setter
    def record_length_index(self, value: int) -> None: ...

    def record_length_index_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "record_length_index".
        """
        ...

    @property
    def record_length_list(self) -> StringVector:
        """Read-only access to the list of Record Length chooser entry strings."""
        ...

    def remove_loop_length_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "loop_length".
        """
        ...

    def remove_overdub_after_record_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "overdub_after_record".
        """
        ...

    def remove_record_length_index_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "record_length_index".
        """
        ...

    def remove_tempo_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "tempo".
        """
        ...

    def stop(self) -> None:
        """Stop Looper's playback."""
        ...

    @property
    def tempo(self) -> float:
        """The tempo of Looper's buffer."""
        ...

    def tempo_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "tempo".
        """
        ...

    @property
    def type(self) -> DeviceType:
        """Return the type of the device."""
        ...

    def undo(self) -> None:
        """Erase everything that was recorded since the last time Overdub was enabled. Calling a second time will restore the material erased by the previous undooperation."""
        ...

    @property
    def view(self) -> Device.View:
        """Representing the view aspects of a device."""
        ...

__all__ = ['LooperDevice']
