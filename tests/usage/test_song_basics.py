"""Song-level basics: tempo, transport, tracks/scenes iteration.

Patterns drawn from gluon/AbletonLive12_MIDIRemoteScripts @ 810ef77:
  - _Axiom/Transport.py
  - Launchpad_Pro/SpecialSessionRecordingComponent.py
  - Axiom_49_61_Classic/Axiom.py
  - LV2_LX2_LC2_LD2/FaderfoxHelper.py

These functions are never executed; they exist for pyright to type-check against the stubs.
"""

from __future__ import annotations

import Live
from Live.Song import Song


def transport_toggle(song: Song) -> None:
    # https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/_Axiom/Transport.py#L27-L30
    if song.is_playing:
        song.is_playing = False
    else:
        song.is_playing = True


def tempo_read_write(song: Song) -> None:
    current: float = song.tempo
    song.tempo = current + 0.5


def application_access() -> None:
    # https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/Axiom_49_61_Classic/Axiom.py#L32
    app = Live.Application.get_application()
    major: int = app.get_major_version()
    minor: int = app.get_minor_version()
    _ = (major, minor)


def iterate_tracks(song: Song) -> None:
    # Common idiom — `for track in song.tracks:` appears throughout the corpus,
    # e.g. https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/LV2_LX2_LC2_LD2/LV2TransportController.py#L113
    for track in song.tracks:
        _ = track.name


def master_track_access(song: Song) -> None:
    # https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/LV2_LX2_LC2_LD2/FaderfoxHelper.py#L131-L141
    master = song.master_track
    _ = master.name
