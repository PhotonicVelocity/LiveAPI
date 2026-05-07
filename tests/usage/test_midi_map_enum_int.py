"""MIDI map functions accepting int for enum-typed parameters.

Boost.Python enum bindings accept either the enum value or the underlying int at
runtime. The Step 10 generator fix widens enum-typed args to `EnumName | int` so
shipped Remote Scripts that pass raw int (Axiom, MackieControl, RemoteSL family)
type-check cleanly.

References:
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/Axiom_49_61_Classic/SliderSection.py#L26
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/MackieControl/ChannelStrip.py#L214

Note: feedback_rule on map_midi_*_with_feedback_map was previously widened to
`T | None`, but a re-audit showed the corpus initializes `feedback_rule = None`
then reassigns to a concrete subtype before every dispatch — None is never
actually passed. The widening was removed; if a probe confirms the binding
accepts None, re-add it as a `type_override` on the arg in lom/MidiMap.yaml.
"""

from __future__ import annotations

import Live
from Live.DeviceParameter import DeviceParameter
from Live.MidiMap import map_midi_cc


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
