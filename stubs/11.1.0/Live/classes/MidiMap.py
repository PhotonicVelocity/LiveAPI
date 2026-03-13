from types import ModuleType
from typing import Callable


class MidiMap(ModuleType):

    @staticmethod
    def forward_midi_cc(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool=True) -> bool:
        ...

    @staticmethod
    def forward_midi_note(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool=True) -> bool:
        ...

    @staticmethod
    def forward_midi_pitchbend(arg1: int, arg2: int, arg3: int) -> bool:
        ...

    @staticmethod
    def map_midi_cc(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, avoid_takeover: bool, sensitivity: float=1.0) -> bool:
        ...

    @staticmethod
    def map_midi_cc_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, feedback_rule: CCFeedbackRule, avoid_takeover: bool, sensitivity: float=1.0) -> bool:
        ...

    @staticmethod
    def map_midi_note(arg1: int, arg2: DeviceParameter, arg3: int, arg4: int) -> bool:
        ...

    @staticmethod
    def map_midi_note_with_feedback_map(arg1: int, arg2: DeviceParameter, arg3: int, arg4: int, arg5: NoteFeedbackRule) -> bool:
        ...

    @staticmethod
    def map_midi_pitchbend(arg1: int, arg2: DeviceParameter, arg3: int, arg4: bool) -> bool:
        ...

    @staticmethod
    def map_midi_pitchbend_with_feedback_map(arg1: int, arg2: DeviceParameter, arg3: int, arg4: PitchBendFeedbackRule, arg5: bool) -> bool:
        ...

    @staticmethod
    def send_feedback_for_parameter(arg1: int, arg2: DeviceParameter) -> None:
        ...

    class CCFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            ...

        @property
        def cc_no(self) -> int:
            ...

        @cc_no.setter
        def cc_no(self, value) -> None:
            ...

        @property
        def cc_value_map(self) -> tuple:
            ...

        @cc_value_map.setter
        def cc_value_map(self, value) -> None:
            ...

        @property
        def channel(self) -> int:
            ...

        @channel.setter
        def channel(self, value) -> None:
            ...

        @property
        def delay_in_ms(self) -> float:
            ...

        @delay_in_ms.setter
        def delay_in_ms(self, value) -> None:
            ...

    class MapMode:
        absolute: int = 0
        relative_signed_bit: int = 1
        relative_binary_offset: int = 2
        relative_two_compliment: int = 3
        relative_signed_bit2: int = 4
        absolute_14_bit: int = 5
        relative_smooth_signed_bit: int = 6
        relative_smooth_binary_offset: int = 7
        relative_smooth_two_compliment: int = 8
        relative_smooth_signed_bit2: int = 9

    class NoteFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            ...

        @property
        def channel(self) -> int:
            ...

        @channel.setter
        def channel(self, value) -> None:
            ...

        @property
        def delay_in_ms(self) -> float:
            ...

        @delay_in_ms.setter
        def delay_in_ms(self, value) -> None:
            ...

        @property
        def note_no(self) -> int:
            ...

        @note_no.setter
        def note_no(self, value) -> None:
            ...

        @property
        def vel_map(self) -> tuple:
            ...

        @vel_map.setter
        def vel_map(self, value) -> None:
            ...

    class PitchBendFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            ...

        @property
        def channel(self) -> int:
            ...

        @channel.setter
        def channel(self, value) -> None:
            ...

        @property
        def delay_in_ms(self) -> float:
            ...

        @delay_in_ms.setter
        def delay_in_ms(self, value) -> None:
            ...

        @property
        def value_pair_map(self) -> tuple:
            ...

        @value_pair_map.setter
        def value_pair_map(self, value) -> None:
            ...
