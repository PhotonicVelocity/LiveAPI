from types import ModuleType
from typing import Callable


class MixerDevice(ModuleType):

    class MixerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Mixer Device in Live, which gives youaccess to the Volume and Panning properties of a Track.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the mixer device.
            """
            ...

        @property
        def crossfade_assign(self) -> int:
            """
            Player- and ReturnTracks only: Access to the Track's Crossfade Assign State.
            """
            ...

        @crossfade_assign.setter
        def crossfade_assign(self, value) -> None:
            ...

        @property
        def crossfader(self) -> DeviceParameter:
            """
            MasterTrack only: Const access to the Crossfader.
            """
            ...

        @property
        def cue_volume(self) -> DeviceParameter:
            """
            MasterTrack only: Const access to the Cue Volume Parameter.
            """
            ...

        @property
        def left_split_stereo(self) -> DeviceParameter:
            """
            Const access to the Track's Left Split Stereo Panning Device Parameter.
            """
            ...

        @property
        def panning(self) -> DeviceParameter:
            """
            Const access to the Tracks Panning Device Parameter.
            """
            ...

        @property
        def panning_mode(self) -> int:
            """
            Access to the Track's Panning Mode.
            """
            ...

        @panning_mode.setter
        def panning_mode(self, value) -> None:
            ...

        @property
        def right_split_stereo(self) -> DeviceParameter:
            """
            Const access to the Track's Right Split Stereo Panning Device Parameter.
            """
            ...

        @property
        def sends(self) -> tuple:
            """
            Const access to the Tracks list of Send Amount Device Parameters.
            """
            ...

        @property
        def song_tempo(self) -> DeviceParameter:
            """
            MasterTrack only: Const access to the Song's Tempo.
            """
            ...

        @property
        def track_activator(self) -> DeviceParameter:
            """
            Const access to the Tracks Activator Device Parameter.
            """
            ...

        @property
        def volume(self) -> DeviceParameter:
            """
            Const access to the Tracks Volume Device Parameter.
            """
            ...

        def add_crossfade_assign_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "crossfade_assign" has changed.
            """
            ...

        def add_panning_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "panning_mode" has changed.
            """
            ...

        def add_sends_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "sends" has changed.
            """
            ...

        def crossfade_assign_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "crossfade_assign".
            """
            ...

        def panning_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "panning_mode".
            """
            ...

        def remove_crossfade_assign_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "crossfade_assign".
            """
            ...

        def remove_panning_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "panning_mode".
            """
            ...

        def remove_sends_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "sends".
            """
            ...

        def sends_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sends".
            """
            ...

        class crossfade_assignments:
            A: int = 0
            NONE: int = 1
            B: int = 2

        class panning_modes:
            stereo: int = 0
            stereo_split: int = 1
