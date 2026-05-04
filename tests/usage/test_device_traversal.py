"""Device traversal: top-level devices and into RackDevice chains.

Patterns drawn from common Remote Script idioms (FaderfoxDeviceController, Push2 device
selection). Walks the device tree under a track and into rack chains.
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
