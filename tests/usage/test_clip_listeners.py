"""Clip and ClipSlot listener registration patterns.

Patterns drawn from:
  doc/decompiled/AbletonLive12_MIDIRemoteScripts/LV2_LX2_LC2_LD2/LV2TransportController.py:99-148

The listener API is one of the most-used Live API surfaces by Remote Scripts.
"""

from __future__ import annotations

from collections.abc import Callable

from Live.Clip import Clip
from Live.ClipSlot import ClipSlot
from Live.Song import Song


def add_clip_listeners(song: Song, on_playing_changed: Callable[[], None]) -> None:
    # LV2TransportController.py:111-123
    for track in song.tracks:
        for slot in track.clip_slots:
            if slot.has_clip:
                slot.add_has_clip_listener(on_playing_changed)
                clip = slot.clip
                if clip is not None:
                    clip.add_playing_status_listener(on_playing_changed)


def remove_clip_listener_safely(clip: Clip, callback: Callable[[], None]) -> None:
    # LV2TransportController.py:138-148 — guarded removal.
    try:
        if clip.playing_status_has_listener(callback):
            clip.remove_playing_status_listener(callback)
    except Exception:
        pass


def remove_slot_listener_safely(slot: ClipSlot, callback: Callable[[], None]) -> None:
    # LV2TransportController.py:125-136
    try:
        if slot.has_clip_has_listener(callback):
            slot.remove_has_clip_listener(callback)
    except Exception:
        pass
