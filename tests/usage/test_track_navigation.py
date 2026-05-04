"""Track navigation: clip_slots, devices, master/return distinctions.

Patterns drawn from gluon/AbletonLive12_MIDIRemoteScripts @ 810ef77:
  - LV2_LX2_LC2_LD2/FaderfoxMixerController.py
  - LV2_LX2_LC2_LD2/FaderfoxHelper.py
  - LV2_LX2_LC2_LD2/FaderfoxDeviceController.py
"""

from __future__ import annotations

from Live.Song import Song
from Live.Track import Track


def select_master_via_view(song: Song) -> None:
    # https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/LV2_LX2_LC2_LD2/FaderfoxMixerController.py#L84
    master: Track = song.master_track
    song.view.selected_track = master


def is_selected_master(song: Song) -> bool:
    # https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/LV2_LX2_LC2_LD2/FaderfoxHelper.py#L131
    return song.view.selected_track is song.master_track


def find_first_eq(track: Track) -> object | None:
    # FaderfoxDeviceController pattern: iterate devices on a track —
    # https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/LV2_LX2_LC2_LD2/FaderfoxDeviceController.py
    for device in track.devices:
        cls_name = type(device).__name__
        if "Eq" in cls_name:
            return device
    return None


def selected_track_name(song: Song) -> str:
    selected = song.view.selected_track
    return selected.name
