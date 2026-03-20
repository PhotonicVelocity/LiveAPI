"""Probe the Clip module.

Uses track 0 slot 0 (MIDI clip, "Coffee Lead") from the demo set.
Audio-specific properties tested on track 10 slot 0 if available.

Usage:
    echo scripts/probes/probe_clip.py > /tmp/apicapture_targeted_probe

Skipped members:
    - Note methods (get_notes*, set_notes, select_*, apply_note_modifications, etc.) — read/write, not behavioral
    - Envelope methods (automation_envelope, clear_*_envelopes, create_automation_envelope) — need automation data
    - beat_to_sample_time, sample_to_beat_time, seconds_to_sample_time — conversion functions, read-only
    - note_number_to_name — utility, read-only
    - move_warp_marker — needs warp markers
    - replace_selected_notes — needs selected notes
    - groove — needs a Groove object (demo set has none)
    - position — only meaningful while clip is playing
    - is_playing (settable) — transport control, deferred
    - quantize, quantize_pitch, duplicate_region, duplicate_notes_by_id — MIDI-only
"""

from __future__ import annotations

import json
import os
from typing import TYPE_CHECKING, Any

from _probe_base import (
    discover_listenable,
    discover_snapshot_props,
    probe_method,
    probe_property,
    setup_listeners,
    snapshot_properties,
    teardown_listeners,
)

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

    from Live.Song import Song


# ── Settable properties — universal (work on both MIDI and audio clips) ───────

CLIP_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("color", 12243060),  # RGB int — 0xBAD074 (pale green)
    ("color_index", 10),
    ("end_marker", 16.0),
    ("launch_mode", 1),  # 0=trigger, 1=gate, 2=toggle, 3=repeat
    ("launch_quantization", 2),  # Quantization enum
    ("legato", True),
    ("loop_end", 16.0),
    ("loop_start", 4.0),
    ("looping", True),
    ("muted", True),
    ("name", "__probe_test__"),
    ("signature_denominator", 8),
    ("signature_numerator", 3),
    ("start_marker", 4.0),
    ("velocity_amount", 0.5),
]

# Audio-only settable properties
AUDIO_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("gain", 0.5),
    ("pitch_coarse", 3),
    ("pitch_fine", 0.5),
    ("ram_mode", True),
    ("warp_mode", 1),  # WarpMode enum
    ("warping", True),
]

SKIP_UNDO: set[str] = set()


# ── Behavioral notes ──────────────────────────────────────────────────────────

NOTES: dict[str, str] = {
    "Clip.fire": (
        "With quantization, the effect is on ``is_triggered``."
    ),
    "Clip.set_fire_button_state": (
        "With quantization, the effect is on ``is_triggered``. "
        "Supports press/release for Gate and Repeat launch modes."
    ),
}


# ── Module-specific config ────────────────────────────────────────────────────

LISTENER_EXCLUDE: set[str] = {"current_song_time", "playing_position"}  # fires every audio tick while playing

SNAPSHOT_EXTRA: dict[str, set[str]] = {}

CROSS_MODULE_LISTENERS: dict[str, list[str]] = {
    "Song": ["is_playing", "back_to_arranger"],
    "ClipSlot": ["playing_status", "is_triggered"],
}


# ── Main probe ────────────────────────────────────────────────────────────────


def run(song: Song, log: Callable) -> Generator[None, None, None]:
    """Probe Clip properties and methods."""
    import time
    from datetime import datetime

    t0 = time.monotonic()
    log("[probe_clip] Starting Clip probes")

    # Use track 0 slot 0 (MIDI clip)
    track = song.tracks[0]
    clip = track.clip_slots[0].clip

    results: dict[str, dict[str, dict[str, Any]]] = {
        "Clip": {"properties": {}, "methods": {}},
    }
    fired: list[tuple[str, str, float]] = []
    probe_timing: dict[str, Any] = {"target": None, "set_time": 0.0, "listener_time": None}

    # Set up listeners and snapshot targets on the clip
    clip_listenable = discover_listenable(clip, LISTENER_EXCLUDE)
    clip_slot = track.clip_slots[0]
    cross_song_props = CROSS_MODULE_LISTENERS.get("Song", [])
    cross_slot_props = CROSS_MODULE_LISTENERS.get("ClipSlot", [])
    snapshot_targets = [
        (clip, "Clip", discover_snapshot_props(clip_listenable, "Clip", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
        (song, "Song", cross_song_props),
        (clip_slot, "ClipSlot", cross_slot_props),
    ]
    clip_listeners = setup_listeners(clip, "Clip", clip_listenable, fired, probe_timing, log)
    song_listeners = setup_listeners(song, "Song", cross_song_props, fired, probe_timing, log)
    slot_listeners = setup_listeners(clip_slot, "ClipSlot", cross_slot_props, fired, probe_timing, log)
    yield

    # Switch to session view
    import Live
    Live.Application.get_application().view.show_view("Session")
    yield
    fired.clear()

    # ── Universal properties ──────────────────────────────────────────────────

    for prop, test_val in CLIP_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, clip, "Clip", prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Clip"]["properties"][prop] = e.value

    # ── Methods ───────────────────────────────────────────────────────────────

    methods = results["Clip"]["methods"]
    orig_quant = song.clip_trigger_quantization

    def _run_method_probe(method, args, check_fn, cleanup_fn=None, *, effect=None, effect_obj=None,
                          obj=None):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_method(
            song, "Clip", method, args, check_fn, cleanup_fn, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
            obj=obj if obj is not None else clip,
            effect=effect, effect_obj=effect_obj,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # fire — fire the clip (disable quantization for immediate effect)
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    gen = _run_method_probe(
        "fire", [],
        check_fn=lambda: clip.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="Clip.is_playing", effect_obj=clip,
    )
    r = yield from gen
    if r: methods["fire"] = r
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield
    song.current_song_time = 0.0
    yield

    # stop — keep quantization disabled so stop is immediate
    clip.fire()
    yield
    yield  # fire is next_tick
    gen = _run_method_probe(
        "stop", [],
        check_fn=lambda: not clip.is_playing,
        effect="Clip.is_playing", effect_obj=clip,
    )
    r = yield from gen
    if r: methods["stop"] = r
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield
    song.current_song_time = 0.0
    yield

    # set_fire_button_state
    gen = _run_method_probe(
        "set_fire_button_state", [True],
        check_fn=lambda: clip.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="Clip.is_playing", effect_obj=clip,
    )
    r = yield from gen
    if r: methods["set_fire_button_state"] = r
    song.clip_trigger_quantization = orig_quant
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield
    song.current_song_time = 0.0
    yield

    # duplicate_loop — doubles the loop content
    orig_loop_end = clip.loop_end
    gen = _run_method_probe(
        "duplicate_loop", [],
        check_fn=lambda: clip.loop_end > orig_loop_end,
        effect="Clip.loop_end", effect_obj=clip,
    )
    r = yield from gen
    if r: methods["duplicate_loop"] = r

    # crop — removes material outside loop
    gen = _run_method_probe(
        "crop", [],
        check_fn=lambda: False,  # hard to check, crop changes start/end markers
        effect="Clip.end_marker", effect_obj=clip,
    )
    r = yield from gen
    if r: methods["crop"] = r

    # move_playing_pos — move the play position within the clip
    # Need clip to be playing first
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    clip.fire()
    yield
    yield
    gen = _run_method_probe(
        "move_playing_pos", [4.0],
        check_fn=lambda: False,  # position changes within clip, not easily observable
    )
    r = yield from gen
    if r: methods["move_playing_pos"] = r
    song.clip_trigger_quantization = orig_quant
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield
    song.current_song_time = 0.0
    yield

    # scrub — scrub playback to a position
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    clip.fire()
    yield
    yield
    gen = _run_method_probe(
        "scrub", [4.0],
        check_fn=lambda: False,
    )
    r = yield from gen
    if r: methods["scrub"] = r
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    song.clip_trigger_quantization = orig_quant
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield
    song.current_song_time = 0.0
    yield

    # stop_scrub
    gen = _run_method_probe(
        "stop_scrub", [],
        check_fn=lambda: False,
    )
    r = yield from gen
    if r: methods["stop_scrub"] = r

    # ── Audio-specific properties ─────────────────────────────────────────────
    # Use track 10 (Vocal Main) which has audio clips
    audio_track = song.tracks[10]
    audio_slot = audio_track.clip_slots[0]
    if audio_slot.has_clip:
        audio_clip = audio_slot.clip
        log(f"[probe_clip] Probing audio-specific properties on {audio_track.name}")

        # Set up listeners on the audio clip (separate from MIDI clip listeners)
        audio_listenable = discover_listenable(audio_clip, LISTENER_EXCLUDE)
        audio_snapshot_targets = [
            (audio_clip, "Clip", discover_snapshot_props(
                audio_listenable, "Clip", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
            (song, "Song", cross_song_props),
        ]
        audio_listeners = setup_listeners(audio_clip, "Clip", audio_listenable, fired, probe_timing, log)
        yield

        for prop, test_val in AUDIO_SETTABLE_PROPS:
            snap, snap_json = snapshot_properties(audio_snapshot_targets)
            gen = probe_property(
                song, audio_clip, "Clip", prop, test_val, fired, probe_timing,
                snap, snap_json, audio_snapshot_targets, SNAPSHOT_EXTRA, log,
            )
            try:
                while True:
                    next(gen)
                    yield
            except StopIteration as e:
                if e.value is not None:
                    # Prefix with "audio:" to distinguish from MIDI clip results
                    results["Clip"]["properties"][prop] = e.value

        teardown_listeners(audio_clip, audio_listeners)
    else:
        log("[probe_clip] No audio clip at track 10 slot 0, skipping audio properties")

    # Tear down listeners
    teardown_listeners(clip, clip_listeners)
    teardown_listeners(song, song_listeners)
    teardown_listeners(clip_slot, slot_listeners)

    # Write results
    app: Live.Application.Application = Live.Application.get_application()
    version = f"{app.get_major_version()}.{app.get_minor_version()}.{app.get_bugfix_version()}"
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "stubs")
    outpath = os.path.join(outdir, version, "pipeline", "ProbeResults.json")

    existing_classes: dict[str, Any] = {}
    if os.path.exists(outpath):
        with open(outpath, "r") as f:
            existing_classes = json.load(f).get("classes", {})

    for cls, data in results.items():
        existing_classes[cls] = data

    # Merge behavioral notes
    orphan_notes: dict[str, str] = {}
    for key, note in NOTES.items():
        placed = False
        for cls in existing_classes:
            if key.startswith(cls + "."):
                member = key[len(cls) + 1:]
                for section in ("properties", "methods"):
                    if member in existing_classes[cls].get(section, {}):
                        existing_classes[cls][section][member]["notes"] = note
                        placed = True
        if not placed:
            orphan_notes[key] = note

    elapsed = round(time.monotonic() - t0, 1)
    output = {
        "version": version,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "elapsed_seconds": elapsed,
        "classes": existing_classes,
    }
    if orphan_notes:
        output["notes"] = orphan_notes

    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)

    total_props = sum(len(d.get("properties", {})) for d in results.values())
    total_methods = sum(len(d.get("methods", {})) for d in results.values())
    log(f"[probe_clip] Done — {total_props} properties, {total_methods} methods probed in {elapsed}s")
