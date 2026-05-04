"""Session recording state and transport controls.

Patterns drawn from gluon/AbletonLive12_MIDIRemoteScripts @ 810ef77:
  https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/Launchpad_Pro/SpecialSessionRecordingComponent.py
"""

from __future__ import annotations

from Live.Song import Song


def maybe_start_playback(song: Song) -> None:
    # https://github.com/gluon/AbletonLive12_MIDIRemoteScripts/blob/810ef77/Launchpad_Pro/SpecialSessionRecordingComponent.py#L44
    if not song.is_playing:
        song.start_playing()


def metronome_toggle(song: Song) -> None:
    song.metronome = not song.metronome


def stop_all_clips(song: Song) -> None:
    song.stop_all_clips()


def begin_undo_step(song: Song) -> None:
    song.begin_undo_step()
    song.tempo = 100.0
    song.end_undo_step()
