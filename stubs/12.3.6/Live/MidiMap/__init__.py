from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from Live.DeviceParameter import DeviceParameter



class CCFeedbackRule:
    """Structure to define feedback properties of MIDI mappings."""

    def __init__(self) -> None: ...

    @property
    def cc_no(self) -> int:
        ...

    @cc_no.setter
    def cc_no(self, value: int) -> None: ...

    @property
    def cc_value_map(self) -> tuple:
        ...

    @cc_value_map.setter
    def cc_value_map(self, value: tuple) -> None: ...

    @property
    def channel(self) -> int:
        ...

    @channel.setter
    def channel(self, value: int) -> None: ...

    @property
    def delay_in_ms(self) -> float:
        ...

    @delay_in_ms.setter
    def delay_in_ms(self, value: float) -> None: ...

    @property
    def enabled(self) -> bool:
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None: ...

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

class NoteFeedbackRule:
    """Structure to define feedback properties of MIDI mappings."""

    def __init__(self) -> None: ...

    @property
    def channel(self) -> int:
        ...

    @channel.setter
    def channel(self, value: int) -> None: ...

    @property
    def delay_in_ms(self) -> float:
        ...

    @delay_in_ms.setter
    def delay_in_ms(self, value: float) -> None: ...

    @property
    def enabled(self) -> bool:
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None: ...

    @property
    def note_no(self) -> int:
        ...

    @note_no.setter
    def note_no(self, value: int) -> None: ...

    @property
    def vel_map(self) -> tuple:
        ...

    @vel_map.setter
    def vel_map(self, value: tuple) -> None: ...

class PitchBendFeedbackRule:
    """Structure to define feedback properties of MIDI mappings."""

    def __init__(self) -> None: ...

    @property
    def channel(self) -> int:
        ...

    @channel.setter
    def channel(self, value: int) -> None: ...

    @property
    def delay_in_ms(self) -> float:
        ...

    @delay_in_ms.setter
    def delay_in_ms(self, value: float) -> None: ...

    @property
    def enabled(self) -> bool:
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None: ...

    @property
    def value_pair_map(self) -> tuple:
        ...

    @value_pair_map.setter
    def value_pair_map(self, value: tuple) -> None: ...

def forward_midi_cc(midi_map_handle: int, midi_channel: int, controller_number: int, controller_value: int, ShouldConsumeEvent: bool = True) -> bool:
    ...

def forward_midi_note(midi_map_handle: int, midi_channel: int, note_number: int, note_velocity: int, ShouldConsumeEvent: bool = True) -> bool:
    ...

def forward_midi_pitchbend(midi_map_handle: int, midi_channel: int, pitchbend_value: int) -> bool:
    ...

def map_midi_cc(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, avoid_takeover: bool, sensitivity: float = 1.0) -> bool:
    ...

def map_midi_cc_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, feedback_rule: CCFeedbackRule, avoid_takeover: bool, sensitivity: float = 1.0) -> bool:
    ...

def map_midi_note(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, note_number: int) -> bool:
    ...

def map_midi_note_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, note_number: int, feedback_rule: NoteFeedbackRule) -> bool:
    ...

def map_midi_pitchbend(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, avoid_takeover: bool) -> bool:
    ...

def map_midi_pitchbend_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, feedback_rule: PitchBendFeedbackRule, avoid_takeover: bool) -> bool:
    ...

def send_feedback_for_parameter(midi_map_handle: int, parameter: DeviceParameter) -> None:
    ...

__all__ = ['CCFeedbackRule', 'MapMode', 'NoteFeedbackRule', 'PitchBendFeedbackRule', 'forward_midi_cc', 'forward_midi_note', 'forward_midi_pitchbend', 'map_midi_cc', 'map_midi_cc_with_feedback_map', 'map_midi_note', 'map_midi_note_with_feedback_map', 'map_midi_pitchbend', 'map_midi_pitchbend_with_feedback_map', 'send_feedback_for_parameter']
