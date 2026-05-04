"""Track navigation: clip_slots, devices, master/return distinctions.

Patterns drawn from:
  - doc/decompiled/AbletonLive12_MIDIRemoteScripts/LV2_LX2_LC2_LD2/FaderfoxMixerController.py
  - doc/decompiled/AbletonLive12_MIDIRemoteScripts/LV2_LX2_LC2_LD2/FaderfoxHelper.py
  - doc/decompiled/AbletonLive12_MIDIRemoteScripts/LV2_LX2_LC2_LD2/FaderfoxDeviceController.py
"""

from __future__ import annotations

from Live.Song import Song
from Live.Track import Track


def select_master_via_view(song: Song) -> None:
    # FaderfoxMixerController.py:84 — set view's selected_track to master.
    master: Track = song.master_track
    song.view.selected_track = master


def is_selected_master(song: Song) -> bool:
    # FaderfoxHelper.py:131 — comparison against master_track.
    return song.view.selected_track is song.master_track


def find_first_eq(track: Track) -> object | None:
    # FaderfoxDeviceController pattern — iterate devices on a track.
    for device in track.devices:
        cls_name = type(device).__name__
        if "Eq" in cls_name:
            return device
    return None


def selected_track_name(song: Song) -> str:
    selected = song.view.selected_track
    return selected.name
