"""Listening to visible_tracks changes.

Pattern from gluon/AbletonLive12_MIDIRemoteScripts @ 810ef77:
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/Axiom_49_61_Classic/Axiom.py#L21-L39
"""

from __future__ import annotations

from collections.abc import Callable

from Live.Song import Song


def attach_visible_tracks_listener(song: Song, callback: Callable[[], None]) -> None:
    song.add_visible_tracks_listener(callback)


def detach_visible_tracks_listener(song: Song, callback: Callable[[], None]) -> None:
    song.remove_visible_tracks_listener(callback)


def initial_selection(song: Song) -> str:
    selected = song.view.selected_track
    return selected.name
