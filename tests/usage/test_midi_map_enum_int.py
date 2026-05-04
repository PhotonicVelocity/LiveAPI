"""MIDI map functions accepting int for enum-typed parameters.

Boost.Python enum bindings accept either the enum value or the underlying int at
runtime. The Step 10 generator fix widens enum-typed args to `EnumName | int` so
shipped Remote Scripts that pass raw int (Axiom, MackieControl, RemoteSL family)
type-check cleanly.

The Step 12 refinements also widened the feedback_rule parameters to `T | None`
because Ableton's own _Framework/ControlSurface.py passes None for them.

References:
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/Axiom_49_61_Classic/SliderSection.py#L26
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/MackieControl/ChannelStrip.py#L214
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/_Framework/ControlSurface.py#L485-L491
"""

from __future__ import annotations

import Live
from Live.DeviceParameter import DeviceParameter
from Live.MidiMap import (
    map_midi_cc,
    map_midi_cc_with_feedback_map,
    map_midi_note_with_feedback_map,
    map_midi_pitchbend_with_feedback_map,
)


def map_cc_with_int_mode(
    handle: int, parameter: DeviceParameter, channel: int, controller: int
) -> bool:
    # Axiom_49_61_Classic/SliderSection.py:26 pattern — int literal for map_mode.
    MAP_MODE_ABSOLUTE = 0  # corresponds to Live.MidiMap.MapMode.absolute
    return map_midi_cc(handle, parameter, channel, controller, MAP_MODE_ABSOLUTE, False)


def map_cc_with_enum_mode(
    handle: int, parameter: DeviceParameter, channel: int, controller: int
) -> bool:
    # Same call, using the enum form — both should type-check.
    return map_midi_cc(
        handle, parameter, channel, controller, Live.MidiMap.MapMode.absolute, False
    )


def map_cc_feedback_with_none(
    handle: int, parameter: DeviceParameter, channel: int, controller: int
) -> bool:
    # _Framework/ControlSurface.py:488 pattern — None passed for feedback_rule.
    MAP_MODE_ABSOLUTE = 0
    return map_midi_cc_with_feedback_map(
        handle, parameter, channel, controller, MAP_MODE_ABSOLUTE, None, False
    )


def map_note_feedback_with_none(
    handle: int, parameter: DeviceParameter, channel: int, note: int
) -> bool:
    # _Framework/ControlSurface.py:485 pattern — None passed for arg5 (NoteFeedbackRule).
    return map_midi_note_with_feedback_map(handle, parameter, channel, note, None)


def map_pitchbend_feedback_with_none(
    handle: int, parameter: DeviceParameter, channel: int
) -> bool:
    # _Framework/ControlSurface.py:491 pattern — None passed for arg4 (PitchBendFeedbackRule).
    return map_midi_pitchbend_with_feedback_map(handle, parameter, channel, None, False)
