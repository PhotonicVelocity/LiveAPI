from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Iterable

if TYPE_CHECKING:
    from . import ClipSlotPlayingState
    from Live.Clip import Clip
    from Live.LomObject import LomObject
    from Live.Track import Track



class ClipSlot(LomObject):
    """This class represents an entry in Lives Session view matrix."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_color_index_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "color_index" has changed.
        """
        ...

    def add_color_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "color" has changed.
        """
        ...

    def add_controls_other_clips_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "controls_other_clips" has changed.
        """
        ...

    def add_has_clip_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "has_clip" has changed.
        """
        ...

    def add_has_stop_button_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "has_stop_button" has changed.
        """
        ...

    def add_is_triggered_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_triggered" has changed.
        """
        ...

    def add_playing_status_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "playing_status" has changed.
        """
        ...

    @property
    def canonical_parent(self) -> Track:
        """Get the canonical parent of the ClipSlot."""
        ...

    @property
    def clip(self) -> Clip:
        """Returns the Clip which this clipslots currently owns. Might be None."""
        ...

    @property
    def color(self) -> int:
        """Returns the canonical color for the clip slot or None if it does not exist."""
        ...

    def color_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "color".
        """
        ...

    @property
    def color_index(self) -> int:
        """Returns the canonical color index for the clip slot or None if it does not exist."""
        ...

    def color_index_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "color_index".
        """
        ...

    @property
    def controls_other_clips(self) -> bool:
        """
        Returns true if firing this slot will fire clips in other slots.
        Can only be true for slots in group tracks.
        """
        ...

    def controls_other_clips_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "controls_other_clips".
        """
        ...

    def create_clip(self, pages: float | None, /) -> None:
        """
        Creates an empty clip with the given length in the slot.
        Throws an error when called on non-empty slots or slots in non-MIDI tracks.
        """
        ...

    def delete_clip(self) -> None:
        """
        Removes the clip contained in the slot.
        Raises an exception if the slot was empty.
        """
        ...

    def duplicate_clip_to(self, target_clip_slot: ClipSlot | None, /) -> None:
        """
        Duplicates the slot's clip to the passed in target slot.
        Overrides the target's clip if it's not empty.
        Raises an exception if the (source) slot itself is empty, or if source and
        target have different track types (audio vs. MIDI). Also raises if the source
        or target slot is in a group track (so called group slot).
        """
        ...

    def fire(self) -> None:
        """
        Fire a Clip if this Clipslot owns one, else trigger the stop button,
        if we have one.
        """
        ...

    @property
    def has_clip(self) -> bool:
        """Returns true if this Clipslot owns a Clip."""
        ...

    def has_clip_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "has_clip".
        """
        ...

    @property
    def has_stop_button(self) -> bool:
        """
        Get/Set if this Clip has a stop button, which will, if fired, stop any
        other Clip that is currently playing the Track we do belong to.
        """
        ...

    @has_stop_button.setter
    def has_stop_button(self, value: bool) -> None: ...

    def has_stop_button_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "has_stop_button".
        """
        ...

    @property
    def is_group_slot(self) -> bool:
        """Returns whether this clip slot is a group track slot (group slot)."""
        ...

    @property
    def is_playing(self) -> bool:
        """Returns whether the clip associated with the slot is playing."""
        ...

    @property
    def is_recording(self) -> bool:
        """Returns whether the clip associated with the slot is recording."""
        ...

    @property
    def is_triggered(self) -> bool:
        """Const access to the triggering state of the clip slot."""
        ...

    def is_triggered_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "is_triggered".
        """
        ...

    @property
    def playing_status(self) -> ClipSlotPlayingState:
        """
        Const access to the playing state of the clip slot.
        Can be either stopped, playing, or recording.
        """
        ...

    def playing_status_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "playing_status".
        """
        ...

    def remove_color_index_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "color_index".
        """
        ...

    def remove_color_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "color".
        """
        ...

    def remove_controls_other_clips_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "controls_other_clips".
        """
        ...

    def remove_has_clip_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "has_clip".
        """
        ...

    def remove_has_stop_button_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "has_stop_button".
        """
        ...

    def remove_is_triggered_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "is_triggered".
        """
        ...

    def remove_playing_status_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "playing_status".
        """
        ...

    def set_fire_button_state(self, state: bool | None, /) -> None:
        """Set the clipslot's fire button state directly. Supports all launch modes."""
        ...

    def stop(self) -> None:
        """
        Stop playing the contained Clip, if there is a Clip and its currently
        playing.
        """
        ...

    @property
    def will_record_on_start(self) -> bool:
        """returns true if the clip slot will record on being fired."""
        ...

__all__ = ['ClipSlot']
