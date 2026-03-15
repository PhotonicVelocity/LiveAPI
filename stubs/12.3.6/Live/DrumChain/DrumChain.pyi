from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from Live.Base import Vector
    from Live.Chain import Chain
    from Live.ChainMixerDevice import ChainMixerDevice
    from Live.RackDevice import RackDevice
    from Live.Track import Track



class DrumChain:
    """This class represents a drum group device chain in Live."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_choke_group_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "choke_group" has changed.
        """
        ...

    def add_in_note_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "in_note" has changed.
        """
        ...

    def add_out_note_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "out_note" has changed.
        """
        ...

    @property
    def canonical_parent(self) -> RackDevice:
        """Get the canonical parent of the chain."""
        ...

    @property
    def choke_group(self) -> int:
        """Access to the chain's choke group setting."""
        ...

    @choke_group.setter
    def choke_group(self, value: int) -> None: ...

    def choke_group_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "choke_group".
        """
        ...

    @property
    def color(self) -> int:
        """Access the color index of the Chain."""
        ...

    @color.setter
    def color(self, value: int) -> None: ...

    @property
    def color_index(self) -> int:
        """Access the color index of the Chain."""
        ...

    @color_index.setter
    def color_index(self, value: int) -> None: ...

    @property
    def devices(self) -> Vector[RackDevice]:
        """Return const access to all available Devices that are present in the chains"""
        ...

    @property
    def has_audio_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This is
        true for all Audio Chains.
        """
        ...

    @property
    def has_audio_output(self) -> bool:
        """
        return True, if this Chain sends out an Audio signal. This is
        true for all Audio Chains, and MIDI chains with an Instrument.
        """
        ...

    @property
    def has_midi_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This is
        true for all MIDI Chains.
        """
        ...

    @property
    def has_midi_output(self) -> bool:
        """
        return True, if this Chain sends out MIDI events. This is
        true for all MIDI Chains with no Instruments.
        """
        ...

    @property
    def in_note(self) -> int:
        """Access to the incoming MIDI note that will trigger this chain."""
        ...

    @in_note.setter
    def in_note(self, value: int) -> None: ...

    def in_note_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "in_note".
        """
        ...

    @property
    def is_auto_colored(self) -> bool:
        """
        Get/set access to the auto color flag of the Chain.
        If True, the Chain will always have the same color as the containing
        Track or Chain.
        """
        ...

    @is_auto_colored.setter
    def is_auto_colored(self, value: bool) -> None: ...

    @property
    def mixer_device(self) -> ChainMixerDevice:
        """
        Return access to the mixer device that holds the chain's mixer parameters:
        the Volume, Pan, and Sendamounts.
        """
        ...

    @property
    def mute(self) -> bool:
        """Mute/unmute the chain."""
        ...

    @mute.setter
    def mute(self, value: bool) -> None: ...

    @property
    def muted_via_solo(self) -> bool:
        """
        Return const access to whether this chain is muted due to some other chain
        being soloed.
        """
        ...

    @property
    def name(self) -> str:
        """Read/write access to the name of the Chain, as visible in the track header."""
        ...

    @name.setter
    def name(self, value: str) -> None: ...

    @property
    def out_note(self) -> int:
        """Access to the MIDI note sent to the devices in the chain."""
        ...

    @out_note.setter
    def out_note(self, value: int) -> None: ...

    def out_note_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "out_note".
        """
        ...

    def remove_choke_group_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "choke_group".
        """
        ...

    def remove_in_note_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "in_note".
        """
        ...

    def remove_out_note_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "out_note".
        """
        ...

    @property
    def solo(self) -> bool:
        """
        Get/Set the solo status of the chain. Note that this will not disable the
        solo state of any other Chain in the same rack. If you want exclusive solo,
        you have to disable the solo state of the other Chains manually.
        """
        ...

    @solo.setter
    def solo(self, value: bool) -> None: ...

__all__ = ['DrumChain']
