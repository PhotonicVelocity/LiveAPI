from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from Live.Chain import Chain
    from Live.ChainMixerDevice import ChainMixerDevice
    from Live.LomObject import LomObject
    from Live.RackDevice import RackDevice



class DrumChain:
    """
    This class represents a drum group device chain in Live.
    """

    @property
    def _live_ptr(self) -> int:
        ...

    @property
    def canonical_parent(self) -> RackDevice:
        """
        Get the canonical parent of the chain.
        """
        ...

    @property
    def choke_group(self) -> int:
        """
        Access to the chain's choke group setting.
        """
        ...

    @choke_group.setter
    def choke_group(self, value) -> None:
        ...

    @property
    def color(self) -> int:
        """
        Access the color index of the Chain.
        """
        ...

    @color.setter
    def color(self, value) -> None:
        ...

    @property
    def color_index(self) -> int:
        """
        Access the color index of the Chain.
        """
        ...

    @color_index.setter
    def color_index(self, value) -> None:
        ...

    @property
    def devices(self) -> tuple:
        """
        Return const access to all available Devices that are present in the chains
        """
        ...

    @property
    def has_audio_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This istrue for all Audio Chains.
        """
        ...

    @property
    def has_audio_output(self) -> bool:
        """
        return True, if this Chain sends out an Audio signal. This istrue for all Audio Chains, and MIDI chains with an Instrument.
        """
        ...

    @property
    def has_midi_input(self) -> bool:
        """
        return True, if this Chain can be feed with an Audio signal. This istrue for all MIDI Chains.
        """
        ...

    @property
    def has_midi_output(self) -> bool:
        """
        return True, if this Chain sends out MIDI events. This istrue for all MIDI Chains with no Instruments.
        """
        ...

    @property
    def in_note(self) -> int:
        """
        Access to the incoming MIDI note that will trigger this chain.
        """
        ...

    @in_note.setter
    def in_note(self, value) -> None:
        ...

    @property
    def is_auto_colored(self) -> bool:
        """
        Get/set access to the auto color flag of the Chain.If True, the Chain will always have the same color as the containingTrack or Chain.
        """
        ...

    @is_auto_colored.setter
    def is_auto_colored(self, value) -> None:
        ...

    @property
    def mixer_device(self) -> ChainMixerDevice:
        """
        Return access to the mixer device that holds the chain's mixer parameters:the Volume, Pan, and Sendamounts.
        """
        ...

    @property
    def mute(self) -> bool:
        """
        Mute/unmute the chain.
        """
        ...

    @mute.setter
    def mute(self, value) -> None:
        ...

    @property
    def muted_via_solo(self) -> bool:
        """
        Return const access to whether this chain is muted due to some other chainbeing soloed.
        """
        ...

    @property
    def name(self) -> str:
        """
        Read/write access to the name of the Chain, as visible in the track header.
        """
        ...

    @name.setter
    def name(self, value) -> None:
        ...

    @property
    def out_note(self) -> int:
        """
        Access to the MIDI note sent to the devices in the chain.
        """
        ...

    @out_note.setter
    def out_note(self, value) -> None:
        ...

    @property
    def solo(self) -> bool:
        """
        Get/Set the solo status of the chain. Note that this will not disable thesolo state of any other Chain in the same rack. If you want exclusive solo, you have to disable the solo state of the other Chains manually.
        """
        ...

    @solo.setter
    def solo(self, value) -> None:
        ...

    def add_choke_group_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "choke_group" has changed.
        """
        ...

    def add_color_index_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "color_index" has changed.
        """
        ...

    def add_color_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "color" has changed.
        """
        ...

    def add_devices_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "devices" has changed.
        """
        ...

    def add_in_note_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "in_note" has changed.
        """
        ...

    def add_is_auto_colored_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "is_auto_colored" has changed.
        """
        ...

    def add_mute_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "mute" has changed.
        """
        ...

    def add_muted_via_solo_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "muted_via_solo" has changed.
        """
        ...

    def add_name_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        ...

    def add_out_note_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "out_note" has changed.
        """
        ...

    def add_solo_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "solo" has changed.
        """
        ...

    def choke_group_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "choke_group".
        """
        ...

    def color_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "color".
        """
        ...

    def color_index_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "color_index".
        """
        ...

    def delete_device(self, arg2: int) -> None:
        """
        Remove a device identified by its index from the chain. Throws runtime error if bad index.
        """
        ...

    def devices_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "devices".
        """
        ...

    def duplicate_device(self, arg2: int) -> None:
        """
        Duplicate the device at the given index in the chain.
        """
        ...

    def in_note_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "in_note".
        """
        ...

    def insert_device(self, DeviceName: str, DeviceIndex: int=-1) -> LomObject:
        """
        Add a device at a given index in the chain. At end if -1.
        """
        ...

    def is_auto_colored_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_auto_colored".
        """
        ...

    def mute_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "mute".
        """
        ...

    def muted_via_solo_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "muted_via_solo".
        """
        ...

    def name_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        ...

    def out_note_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "out_note".
        """
        ...

    def remove_choke_group_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "choke_group".
        """
        ...

    def remove_color_index_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "color_index".
        """
        ...

    def remove_color_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "color".
        """
        ...

    def remove_devices_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "devices".
        """
        ...

    def remove_in_note_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "in_note".
        """
        ...

    def remove_is_auto_colored_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "is_auto_colored".
        """
        ...

    def remove_mute_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "mute".
        """
        ...

    def remove_muted_via_solo_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "muted_via_solo".
        """
        ...

    def remove_name_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "name".
        """
        ...

    def remove_out_note_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "out_note".
        """
        ...

    def remove_solo_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "solo".
        """
        ...

    def solo_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "solo".
        """
        ...


__all__ = ['DrumChain']
