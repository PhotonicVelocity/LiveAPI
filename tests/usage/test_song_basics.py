"""Song-level basics: tempo, transport, tracks/scenes iteration.

Patterns drawn from:
  - doc/decompiled/AbletonLive12_MIDIRemoteScripts/_Axiom/Transport.py
  - doc/decompiled/AbletonLive12_MIDIRemoteScripts/Launchpad_Pro/SpecialSessionRecordingComponent.py
  - doc/decompiled/AbletonLive12_MIDIRemoteScripts/Axiom_49_61_Classic/Axiom.py

These functions are never executed; they exist for pyright to type-check against the stubs.
"""

from __future__ import annotations

import Live
from Live.Song import Song


def transport_toggle(song: Song) -> None:
    # _Axiom/Transport.py:27,30 — direct boolean assignment to is_playing.
    if song.is_playing:
        song.is_playing = False
    else:
        song.is_playing = True


def tempo_read_write(song: Song) -> None:
    current: float = song.tempo
    song.tempo = current + 0.5


def application_access() -> None:
    # Axiom_49_61_Classic/Axiom.py:32 — module-level entry point.
    app = Live.Application.get_application()
    major: int = app.get_major_version()
    minor: int = app.get_minor_version()
    _ = (major, minor)


def iterate_tracks(song: Song) -> None:
    # FaderfoxScript pattern — for-loop over song.tracks.
    for track in song.tracks:
        _ = track.name


def master_track_access(song: Song) -> None:
    # FaderfoxHelper.py:131,141 — master_track read.
    master = song.master_track
    _ = master.name
