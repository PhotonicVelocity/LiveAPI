from types import ModuleType
from typing import Callable


class Track(ModuleType):

    class DeviceContainer(object):
        def __init__(self, *a, **k):
            """
            This class is a common super class of Track and Chain
            """
            ...

        @property
        def _live_ptr(self):
            ...

    class DeviceInsertMode:
        default: int = 0
        selected_left: int = 1
        selected_right: int = 2
        count: int = 3

    class RoutingChannel(object):
        def __init__(self, *a, **k):
            """
            This class represents a routing channel.
            """
            ...

        @property
        def display_name(self) -> str:
            """
            Display name of routing channel.
            """
            ...

        @property
        def layout(self) -> RoutingChannelLayout:
            """
            The routing channel's Layout, e.g., mono or stereo.
            """
            ...

    class RoutingChannelLayout:
        midi: int = 0
        mono: int = 1
        stereo: int = 2

    class RoutingChannelVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning routing channels from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class RoutingType(object):
        def __init__(self, *a, **k):
            """
            This class represents a routing type.
            """
            ...

        @property
        def attached_object(self) -> None:
            """
            Live object associated with the routing type.
            """
            ...

        @property
        def category(self) -> int:
            """
            Category of the routing type.
            """
            ...

        @property
        def display_name(self) -> str:
            """
            Display name of routing type.
            """
            ...

    class RoutingTypeCategory:
        external: int = 0
        rewire: int = 1
        resampling: int = 2
        master: int = 3
        track: int = 4
        parent_group_track: int = 5
        none: int = 6
        invalid: int = 7

    class RoutingTypeVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning routing types from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class Track(object):
        def __init__(self, *a, **k):
            """
            This class represents a track in Live. It can be either an Audio track, a MIDI Track, a Return Track or the Master track. The Master Track and at least one Audio or MIDI track will be always present.Return Tracks are optional.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def arm(self) -> bool:
            """
            Arm the track for recording. Not available for Master- and Send Tracks.
            """
            ...

        @arm.setter
        def arm(self, value) -> None:
            ...

        @property
        def arrangement_clips(self) -> tuple:
            """
            const access to the list of clips in arrangement viewThe list will be empty for the master, send and group tracks.
            """
            ...

        @property
        def available_input_routing_channels(self) -> tuple[RoutingChannel, ...]:
            """
            Return a list of source channels for input routing.
            """
            ...

        @property
        def available_input_routing_types(self) -> tuple[RoutingType, ...]:
            """
            Return a list of source types for input routing.
            """
            ...

        @property
        def available_output_routing_channels(self) -> tuple[RoutingChannel, ...]:
            """
            Return a list of destination channels for output routing.
            """
            ...

        @property
        def available_output_routing_types(self) -> tuple[RoutingType, ...]:
            """
            Return a list of destination types for output routing.
            """
            ...

        @property
        def can_be_armed(self) -> bool:
            """
            return True, if this Track has a valid arm property. Not all trackscan be armed (for example return Tracks or the Master Tracks).
            """
            ...

        @property
        def can_be_frozen(self) -> bool:
            """
            return True, if this Track can be frozen.
            """
            ...

        @property
        def can_show_chains(self) -> bool:
            """
            return True, if this Track contains a rack instrument device that is capable of showing its chains in session view.
            """
            ...

        @property
        def canonical_parent(self) -> Song:
            """
            Get the canonical parent of the track.
            """
            ...

        @property
        def clip_slots(self) -> tuple:
            """
            const access to the list of clipslots (see class AClipSlot) for this track.The list will be empty for the master and sendtracks.
            """
            ...

        @property
        def color(self) -> int:
            """
            Get/set access to the color of the Track (RGB).
            """
            ...

        @color.setter
        def color(self, value) -> None:
            ...

        @property
        def color_index(self) -> int:
            """
            Get/Set access to the color index of the track. Can be None for no color.
            """
            ...

        @color_index.setter
        def color_index(self, value) -> None:
            ...

        @property
        def current_input_routing(self) -> str:
            """
            Get/Set the name of the current active input routing.When setting a new routing, the new routing must be one of the available ones.
            """
            ...

        @current_input_routing.setter
        def current_input_routing(self, value) -> None:
            ...

        @property
        def current_input_sub_routing(self) -> str:
            """
            Get/Set the current active input sub routing.When setting a new routing, the new routing must be one of the available ones.
            """
            ...

        @current_input_sub_routing.setter
        def current_input_sub_routing(self, value) -> None:
            ...

        @property
        def current_monitoring_state(self) -> int:
            """
            Get/Set the track's current monitoring state.
            """
            ...

        @current_monitoring_state.setter
        def current_monitoring_state(self, value) -> None:
            ...

        @property
        def current_output_routing(self) -> str:
            """
            Get/Set the current active output routing.When setting a new routing, the new routing must be one of the available ones.
            """
            ...

        @current_output_routing.setter
        def current_output_routing(self, value) -> None:
            ...

        @property
        def current_output_sub_routing(self) -> str:
            """
            Get/Set the current active output sub routing.When setting a new routing, the new routing must be one of the available ones.
            """
            ...

        @current_output_sub_routing.setter
        def current_output_sub_routing(self, value) -> None:
            ...

        @property
        def devices(self) -> tuple:
            """
            Return const access to all available Devices that are present in the TracksDevicechain. This tuple will also include the 'mixer_device' that every Trackalways has.
            """
            ...

        @property
        def fired_slot_index(self) -> int:
            """
            const access to the index of the fired (and thus blinking) clipslot in this track.This index is -1 if no slot is fired and -2 if the track's stop button has been fired.
            """
            ...

        @property
        def fold_state(self) -> bool:
            """
            Get/Set whether the track is folded or not. Only available if is_foldable is True.
            """
            ...

        @fold_state.setter
        def fold_state(self, value) -> None:
            ...

        @property
        def group_track(self) -> Track:
            """
            return the group track if is_grouped.
            """
            ...

        @property
        def has_audio_input(self) -> bool:
            """
            return True, if this Track can be feed with an Audio signal. This istrue for all Audio Tracks.
            """
            ...

        @property
        def has_audio_output(self) -> bool:
            """
            return True, if this Track sends out an Audio signal. This istrue for all Audio Tracks, and MIDI tracks with an Instrument.
            """
            ...

        @property
        def has_midi_input(self) -> bool:
            """
            return True, if this Track can be feed with an Audio signal. This istrue for all MIDI Tracks.
            """
            ...

        @property
        def has_midi_output(self) -> bool:
            """
            return True, if this Track sends out MIDI events. This istrue for all MIDI Tracks with no Instruments.
            """
            ...

        @property
        def implicit_arm(self) -> bool:
            """
            Arm the track for recording. When The track is implicitly armed, it showsin a weaker color in the live GUI and is not saved in the set.
            """
            ...

        @implicit_arm.setter
        def implicit_arm(self, value) -> None:
            ...

        @property
        def input_meter_left(self) -> float:
            """
            Momentary value of left input channel meter, 0.0 to 1.0. For Audio Tracks only.
            """
            ...

        @property
        def input_meter_level(self) -> float:
            """
            Return the MIDI or Audio meter value of the Tracks input, depending on thetype of the Track input. Meter values (MIDI or Audio) are always scaledfrom 0.0 to 1.0.
            """
            ...

        @property
        def input_meter_right(self) -> float:
            """
            Momentary value of right input channel meter, 0.0 to 1.0. For Audio Tracks only.
            """
            ...

        @property
        def input_routing_channel(self) -> RoutingChannel:
            """
            Get and set the current source channel for input routing.Raises ValueError if the type isn't one of the current values inavailable_input_routing_channels.
            """
            ...

        @input_routing_channel.setter
        def input_routing_channel(self, value) -> None:
            ...

        @property
        def input_routing_type(self) -> RoutingType:
            """
            Get and set the current source type for input routing.Raises ValueError if the type isn't one of the current values inavailable_input_routing_types.
            """
            ...

        @input_routing_type.setter
        def input_routing_type(self, value) -> None:
            ...

        @property
        def input_routings(self) -> tuple[str, ...]:
            """
            Const access to the list of available input routings.
            """
            ...

        @property
        def input_sub_routings(self) -> tuple[str, ...]:
            """
            Return a list of all available input sub routings.
            """
            ...

        @property
        def is_foldable(self) -> bool:
            """
            return True if the track can be (un)folded to hide/reveal contained tracks.
            """
            ...

        @property
        def is_frozen(self) -> bool:
            """
            return True if this Track is currently frozen. No changes should be applied to the track's devices or clips while it is frozen.
            """
            ...

        @property
        def is_grouped(self) -> bool:
            """
            return True if this Track is current part of a group track.
            """
            ...

        @property
        def is_part_of_selection(self) -> bool:
            """
            return False if the track is not selected.
            """
            ...

        @property
        def is_showing_chains(self) -> bool:
            """
            Get/Set whether a track with a rack device is showing its chains in session view.
            """
            ...

        @is_showing_chains.setter
        def is_showing_chains(self, value) -> None:
            ...

        @property
        def is_visible(self) -> bool:
            """
            return False if the track is hidden within a folded group track.
            """
            ...

        @property
        def mixer_device(self) -> MixerDevice:
            """
            Return access to the special Device that every Track has: This Device containsthe Volume, Pan, Sendamounts, and Crossfade assignment parameters.
            """
            ...

        @property
        def mute(self) -> bool:
            """
            Mute/unmute the track.
            """
            ...

        @mute.setter
        def mute(self, value) -> None:
            ...

        @property
        def muted_via_solo(self) -> bool:
            """
            Returns true if the track is muted because another track is soloed.
            """
            ...

        @property
        def name(self) -> str:
            """
            Read/write access to the name of the Track, as visible in the track header.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def output_meter_left(self) -> float:
            """
            Momentary value of left output channel meter, 0.0 to 1.0.For tracks with audio output only.
            """
            ...

        @property
        def output_meter_level(self) -> float:
            """
            Return the MIDI or Audio meter value of the Track output (behind themixer_device), depending on the type of the Track input, this can be a MIDIor Audio meter. Meter values (MIDI or Audio) are always scaled from 0.0 to 1.0.
            """
            ...

        @property
        def output_meter_right(self) -> float:
            """
            Momentary value of right output channel meter, 0.0 to 1.0.For tracks with audio output only.
            """
            ...

        @property
        def output_routing_channel(self) -> RoutingChannel:
            """
            Get and set the current destination channel for output routing.Raises ValueError if the channel isn't one of the current values inavailable_output_routing_channels.
            """
            ...

        @output_routing_channel.setter
        def output_routing_channel(self, value) -> None:
            ...

        @property
        def output_routing_type(self) -> RoutingType:
            """
            Get and set the current destination type for output routing.Raises ValueError if the type isn't one of the current values inavailable_output_routing_types.
            """
            ...

        @output_routing_type.setter
        def output_routing_type(self, value) -> None:
            ...

        @property
        def output_routings(self) -> tuple[str, ...]:
            """
            Const access to the list of all available output routings.
            """
            ...

        @property
        def output_sub_routings(self) -> tuple[str, ...]:
            """
            Return a list of all available output sub routings.
            """
            ...

        @property
        def performance_impact(self) -> float:
            """
            Reports the performance impact of this track.
            """
            ...

        @property
        def playing_slot_index(self) -> int:
            """
            const access to the index of the currently playing clip in the track.Will be -1 when no clip is playing.
            """
            ...

        @property
        def solo(self) -> bool:
            """
            Get/Set the solo status of the track. Note that this will not disable thesolo state of any other track. If you want exclusive solo, you have to disable the solo state of the other Tracks manually.
            """
            ...

        @solo.setter
        def solo(self, value) -> None:
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a Track.
            """
            ...

        def add_arm_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "arm" has changed.
            """
            ...

        def add_arrangement_clips_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "arrangement_clips" has changed.
            """
            ...

        def add_available_input_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_input_routing_channels" has changed.
            """
            ...

        def add_available_input_routing_types_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_input_routing_types" has changed.
            """
            ...

        def add_available_output_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_output_routing_channels" has changed.
            """
            ...

        def add_available_output_routing_types_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_output_routing_types" has changed.
            """
            ...

        def add_clip_slots_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "clip_slots" has changed.
            """
            ...

        def add_color_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "color_index" has changed.
            """
            ...

        def add_color_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "color" has changed.
            """
            ...

        def add_current_input_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_input_routing" has changed.
            """
            ...

        def add_current_input_sub_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_input_sub_routing" has changed.
            """
            ...

        def add_current_monitoring_state_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_monitoring_state" has changed.
            """
            ...

        def add_current_output_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_output_routing" has changed.
            """
            ...

        def add_current_output_sub_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_output_sub_routing" has changed.
            """
            ...

        def add_data_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "data" has changed.
            """
            ...

        def add_devices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "devices" has changed.
            """
            ...

        def add_fired_slot_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "fired_slot_index" has changed.
            """
            ...

        def add_has_audio_input_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_audio_input" has changed.
            """
            ...

        def add_has_audio_output_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_audio_output" has changed.
            """
            ...

        def add_has_midi_input_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_midi_input" has changed.
            """
            ...

        def add_has_midi_output_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_midi_output" has changed.
            """
            ...

        def add_implicit_arm_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "implicit_arm" has changed.
            """
            ...

        def add_input_meter_left_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_meter_left" has changed.
            """
            ...

        def add_input_meter_level_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_meter_level" has changed.
            """
            ...

        def add_input_meter_right_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_meter_right" has changed.
            """
            ...

        def add_input_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routing_channel" has changed.
            """
            ...

        def add_input_routing_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routing_type" has changed.
            """
            ...

        def add_input_routings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routings" has changed.
            """
            ...

        def add_input_sub_routings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_sub_routings" has changed.
            """
            ...

        def add_is_frozen_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_frozen" has changed.
            """
            ...

        def add_is_showing_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_showing_chains" has changed.
            """
            ...

        def add_mute_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mute" has changed.
            """
            ...

        def add_muted_via_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "muted_via_solo" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_output_meter_left_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_meter_left" has changed.
            """
            ...

        def add_output_meter_level_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_meter_level" has changed.
            """
            ...

        def add_output_meter_right_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_meter_right" has changed.
            """
            ...

        def add_output_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_routing_channel" has changed.
            """
            ...

        def add_output_routing_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_routing_type" has changed.
            """
            ...

        def add_output_routings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_routings" has changed.
            """
            ...

        def add_output_sub_routings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_sub_routings" has changed.
            """
            ...

        def add_performance_impact_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "performance_impact" has changed.
            """
            ...

        def add_playing_slot_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_slot_index" has changed.
            """
            ...

        def add_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "solo" has changed.
            """
            ...

        def arm_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "arm".
            """
            ...

        def arrangement_clips_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "arrangement_clips".
            """
            ...

        def available_input_routing_channels_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_input_routing_channels".
            """
            ...

        def available_input_routing_types_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_input_routing_types".
            """
            ...

        def available_output_routing_channels_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_output_routing_channels".
            """
            ...

        def available_output_routing_types_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_output_routing_types".
            """
            ...

        def clip_slots_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "clip_slots".
            """
            ...

        def color_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "color".
            """
            ...

        def color_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "color_index".
            """
            ...

        def create_audio_clip(self, arg2: object, arg3: float) -> None:
            """
            Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time. Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.
            """
            ...

        def current_input_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_input_routing".
            """
            ...

        def current_input_sub_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_input_sub_routing".
            """
            ...

        def current_monitoring_state_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_monitoring_state".
            """
            ...

        def current_output_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_output_routing".
            """
            ...

        def current_output_sub_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_output_sub_routing".
            """
            ...

        def data_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "data".
            """
            ...

        def delete_clip(self, arg2: Clip) -> None:
            """
            Delete the given clip. Raises a runtime error when the clip belongs to another track.
            """
            ...

        def delete_device(self, arg2: int) -> None:
            """
            Delete a device identified by the index in the 'devices' list.
            """
            ...

        def devices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "devices".
            """
            ...

        def duplicate_clip_slot(self, arg2: int) -> int:
            """
            Duplicate a clip and put it into the next free slot and return the index of the destination slot. A new scene is created if no free slot is available. If creating the new scene would exceed the limitations, a runtime error is raised.
            """
            ...

        def duplicate_clip_to_arrangement(self, clip: Clip, destination_time: float) -> Clip:
            """
            Duplicate the given clip into the arrangement of this track at the provided destination time and return it. When the type of the clip and the type of the track are incompatible, a runtime error is raised.
            """
            ...

        def fired_slot_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "fired_slot_index".
            """
            ...

        def get_data(self, key: object, default_value: object) -> object:
            """
            Get data for the given key, that was previously stored using set_data.
            """
            ...

        def has_audio_input_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_audio_input".
            """
            ...

        def has_audio_output_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_audio_output".
            """
            ...

        def has_midi_input_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_midi_input".
            """
            ...

        def has_midi_output_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_midi_output".
            """
            ...

        def implicit_arm_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "implicit_arm".
            """
            ...

        def input_meter_left_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_meter_left".
            """
            ...

        def input_meter_level_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_meter_level".
            """
            ...

        def input_meter_right_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_meter_right".
            """
            ...

        def input_routing_channel_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routing_channel".
            """
            ...

        def input_routing_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routing_type".
            """
            ...

        def input_routings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routings".
            """
            ...

        def input_sub_routings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_sub_routings".
            """
            ...

        def is_frozen_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_frozen".
            """
            ...

        def is_showing_chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_showing_chains".
            """
            ...

        def jump_in_running_session_clip(self, arg2: float) -> None:
            """
            Jump forward or backward in the currently running Sessionclip (if any) by the specified relative amount in beats. Does nothing if no Session Clip is currently running.
            """
            ...

        def mute_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mute".
            """
            ...

        def muted_via_solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "muted_via_solo".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def output_meter_left_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_meter_left".
            """
            ...

        def output_meter_level_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_meter_level".
            """
            ...

        def output_meter_right_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_meter_right".
            """
            ...

        def output_routing_channel_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_routing_channel".
            """
            ...

        def output_routing_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_routing_type".
            """
            ...

        def output_routings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_routings".
            """
            ...

        def output_sub_routings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_sub_routings".
            """
            ...

        def performance_impact_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "performance_impact".
            """
            ...

        def playing_slot_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_slot_index".
            """
            ...

        def remove_arm_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "arm".
            """
            ...

        def remove_arrangement_clips_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "arrangement_clips".
            """
            ...

        def remove_available_input_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_input_routing_channels".
            """
            ...

        def remove_available_input_routing_types_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_input_routing_types".
            """
            ...

        def remove_available_output_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_output_routing_channels".
            """
            ...

        def remove_available_output_routing_types_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_output_routing_types".
            """
            ...

        def remove_clip_slots_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "clip_slots".
            """
            ...

        def remove_color_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "color_index".
            """
            ...

        def remove_color_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "color".
            """
            ...

        def remove_current_input_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_input_routing".
            """
            ...

        def remove_current_input_sub_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_input_sub_routing".
            """
            ...

        def remove_current_monitoring_state_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_monitoring_state".
            """
            ...

        def remove_current_output_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_output_routing".
            """
            ...

        def remove_current_output_sub_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_output_sub_routing".
            """
            ...

        def remove_data_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "data".
            """
            ...

        def remove_devices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "devices".
            """
            ...

        def remove_fired_slot_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "fired_slot_index".
            """
            ...

        def remove_has_audio_input_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_audio_input".
            """
            ...

        def remove_has_audio_output_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_audio_output".
            """
            ...

        def remove_has_midi_input_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_midi_input".
            """
            ...

        def remove_has_midi_output_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_midi_output".
            """
            ...

        def remove_implicit_arm_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "implicit_arm".
            """
            ...

        def remove_input_meter_left_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_meter_left".
            """
            ...

        def remove_input_meter_level_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_meter_level".
            """
            ...

        def remove_input_meter_right_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_meter_right".
            """
            ...

        def remove_input_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routing_channel".
            """
            ...

        def remove_input_routing_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routing_type".
            """
            ...

        def remove_input_routings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routings".
            """
            ...

        def remove_input_sub_routings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_sub_routings".
            """
            ...

        def remove_is_frozen_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_frozen".
            """
            ...

        def remove_is_showing_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_showing_chains".
            """
            ...

        def remove_mute_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mute".
            """
            ...

        def remove_muted_via_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "muted_via_solo".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_output_meter_left_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_meter_left".
            """
            ...

        def remove_output_meter_level_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_meter_level".
            """
            ...

        def remove_output_meter_right_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_meter_right".
            """
            ...

        def remove_output_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_routing_channel".
            """
            ...

        def remove_output_routing_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_routing_type".
            """
            ...

        def remove_output_routings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_routings".
            """
            ...

        def remove_output_sub_routings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_sub_routings".
            """
            ...

        def remove_performance_impact_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "performance_impact".
            """
            ...

        def remove_playing_slot_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_slot_index".
            """
            ...

        def remove_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "solo".
            """
            ...

        def set_data(self, key: object, value: object) -> None:
            """
            Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.
            """
            ...

        def solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "solo".
            """
            ...

        def stop_all_clips(self, Quantized: bool=True) -> None:
            """
            Stop running and triggered clip and slots on this track.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a Track.
                """
                ...

            @property
            def _live_ptr(self):
                ...

            @property
            def canonical_parent(self):
                """
                Get the canonical parent of the track view.
                """
                ...

            @property
            def device_insert_mode(self):
                """
                Get/Listen the device insertion mode of the track.  By default, it will insert devices at the end, but it can be changed to make it relative to current selection.
                """
                ...

            @property
            def is_collapsed(self):
                """
                Get/Set/Listen if the track is shown collapsed in the arranger view.
                """
                ...

            @property
            def selected_device(self):
                """
                Get/Set/Listen the insertion mode of the device.  While in insertion mode, loading new devices from the browser will place devices at the selected position.
                """
                ...

            def add_device_insert_mode_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "device_insert_mode" has changed.
                """
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def add_selected_device_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_device" has changed.
                """
                ...

            def device_insert_mode_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "device_insert_mode".
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_device_insert_mode_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "device_insert_mode".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...

            def remove_selected_device_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_device".
                """
                ...

            def select_instrument(self) -> bool:
                """
                Selects the track's instrument if it has one.
                """
                ...

            def selected_device_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_device".
                """
                ...

        class monitoring_states:
            IN: int = 0
            AUTO: int = 1
            OFF: int = 2
