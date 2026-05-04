"""Device traversal: top-level devices and into RackDevice chains.

Common idioms from gluon/AbletonLive12_MIDIRemoteScripts @ 810ef77 — iterating
`track.devices` and inspecting class type and parameter counts. The corpus uses this
pattern across many controllers; representative example:
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/LV2_LX2_LC2_LD2/FaderfoxDeviceController.py
"""

from __future__ import annotations

from Live.Track import Track


def collect_top_level_device_names(track: Track) -> list[str]:
    return [device.name for device in track.devices]


def first_device_class_name(track: Track) -> str | None:
    if len(track.devices) == 0:
        return None
    first = track.devices[0]
    return type(first).__name__


def parameter_count_total(track: Track) -> int:
    total = 0
    for device in track.devices:
        total += len(device.parameters)
    return total
