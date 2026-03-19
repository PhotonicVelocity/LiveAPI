"""Probe the Song module — Song, Song.View, and CuePoint classes.

Probes undo tracking, async visibility, side effects, and behavioral metadata
for all settable properties and state-changing methods. Runs inside Live via
the targeted probe trigger.

Uses yield to cross tick boundaries, which is essential for accurately classifying
async visibility — a property is "immediate" if the new value is readable on the
same tick as the set, "next_tick" if it only appears after yielding.

Note: async_visibility describes when the LOM property is readable, not when the
underlying action takes effect. Transport methods like stop_all_clips act on the
audio engine immediately but the Python-visible property updates on the next tick.

Usage:
    echo scripts/probes/probe_song.py > /tmp/apicapture_targeted_probe

Skipped members:
    - begin_undo_step, end_undo_step, undo, redo — undo infrastructure used by the probe itself
    - get_data, find_device_position, get_beats_*, get_current_*, is_cue_point_selected — read-only
    - tap_tempo — pass-through to Live's internal tap averaging, no behavioral metadata to capture
    - capture_midi — requires external MIDI input
    - force_link_beat_time — no observable effect without Link peers
    - re_enable_automation — can't trigger programmatically (UI-driven flag)
"""

from __future__ import annotations

import json
import os
from typing import TYPE_CHECKING, Any

from _probe_base import (
    discover_listenable,
    discover_snapshot_props,
    find_new_index,
    probe_method,
    probe_property,
    ptr_set,
    setup_listeners,
    snapshot_properties,
    teardown_listeners,
)

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

    from Live.Song import Song


# ── Settable properties with safe test values ──────────────────────────────────

# (property_name, test_value) — test_value must differ from typical defaults.
# For booleans, test_value is ignored — we always flip the current value.
SONG_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("arrangement_overdub", True),
    # back_to_arranger excluded — engine-driven status flag, set may be ignored
    ("clip_trigger_quantization", 2),  # Quantization enum — 0=none, 1=8bars, 2=4bars, ...
    ("groove_amount", 0.5),
    ("loop", True),
    ("loop_length", 8.0),
    ("loop_start", 4.0),
    ("metronome", True),
    ("midi_recording_quantization", 1),  # RecordingQuantization enum
    ("overdub", True),
    ("punch_in", True),
    ("punch_out", True),
    ("root_note", 2),  # 0=C, 2=D
    ("scale_mode", True),
    ("scale_name", "Dorian"),
    ("signature_denominator", 8),
    ("signature_numerator", 3),
    ("swing_amount", 0.6),
    ("tempo", 130.0),
    ("tempo_follower_enabled", True),
    ("is_ableton_link_enabled", True),
    ("is_ableton_link_start_stop_sync_enabled", True),
    ("record_mode", True),
    ("session_record", True),
    ("session_automation_record", True),
]

VIEW_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("draw_mode", True),
    ("follow_song", True),
]

# Properties skipped from undo probing (transport/momentary state).
SKIP_UNDO: set[str] = {
    "is_playing",
    "nudge_down",
    "nudge_up",
    "current_song_time",
    "start_time",
}


# ── Behavioral notes (merged into results for downstream enrichment) ──────────

NOTES: dict[str, str] = {
    "Song.appointed_device": (
        "The ``appointed_device`` listener does not fire on programmatic changes "
        "(``setattr`` or ``select_device``). It appears to be UI-driven only."
    ),
    "Song.back_to_arranger": (
        "Can only be set to ``False``. The engine sets it to ``True`` when session "
        "clips are triggered (e.g. via ``Scene.fire()``)."
    ),
    "Song.record_mode": (
        "The ``is_playing`` side effect depends on the 'Record Starts Playback' preference."
    ),
    "Song.re_enable_automation": (
        "``re_enable_automation_enabled`` is only set by physical UI interaction "
        "(e.g. moving a mapped knob), not by programmatic ``param.value`` changes."
    ),
    "Song.session_record": (
        "The ``is_playing`` side effect depends on the 'Record Starts Playback' preference."
    ),
    "Song.set_data": (
        "The stored value is immediately readable via ``get_data`` on the same tick."
    ),
    "Song.stop_all_clips": (
        "Does not stop the song transport — only stops clip playback."
    ),
    "Song.View.select_device": (
        "Does not fire the ``appointed_device`` listener even when "
        "``should_appoint_device`` is ``True``."
    ),
}


# ── Module-specific config ────────────────────────────────────────────────────

# Properties excluded from listener subscription — fire too frequently to be useful as listeners.
LISTENER_EXCLUDE: set[str] = {"current_song_time"}  # fires every audio tick (~80/s)

# Non-listenable properties to include in snapshots, keyed by class name.
SNAPSHOT_EXTRA: dict[str, set[str]] = {
    "Song": {"name"},
    "Song.View": {"highlighted_clip_slot"},
}


# ── Main probe ────────────────────────────────────────────────────────────────


def run(song: Song, log: Callable) -> Generator[None, None, None]:
    """Probe all settable Song and Song.View properties."""
    import time
    from datetime import datetime

    t0 = time.monotonic()
    log("[probe_song] Starting property probes")
    results: dict[str, dict[str, dict[str, Any]]] = {
        "Song": {"properties": {}},
        "Song.View": {"properties": {}},
    }
    fired: list[tuple[str, str, float]] = []
    probe_timing: dict[str, Any] = {"target": None, "set_time": 0.0, "listener_time": None}

    # Set up listeners and snapshot targets
    view = song.view
    song_listenable = discover_listenable(song, LISTENER_EXCLUDE)
    view_listenable = discover_listenable(view, LISTENER_EXCLUDE)
    snapshot_targets = [
        (song, "Song", discover_snapshot_props(song_listenable, "Song", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
        (view, "Song.View", discover_snapshot_props(view_listenable, "Song.View", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
    ]
    song_listeners = setup_listeners(song, "Song", song_listenable, fired, probe_timing, log)
    view_listeners = setup_listeners(view, "Song.View", view_listenable, fired, probe_timing, log)
    yield  # let listener setup settle

    # Switch to session view and set a known starting state.
    import Live
    Live.Application.get_application().view.show_view("Session")
    view.highlighted_clip_slot = song.tracks[0].clip_slots[0]
    yield
    fired.clear()  # discard listeners fired by the view switch

    # Song properties
    for prop, test_val in SONG_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, song, "Song", prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Song"]["properties"][prop] = e.value

    # Song.View properties
    for prop, test_val in VIEW_SETTABLE_PROPS:
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, view, "Song.View", prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Song.View"]["properties"][prop] = e.value

    # ── Special-case property probes ─────────────────────────────────────────
    # These need runtime preconditions or object values and can't go in the static lists.

    def _run_obj_prop_probe(obj, cls, prop, test_val):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, obj, cls, prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # Song.back_to_arranger — Live sets it True (e.g. on scene fire), user can only clear to False
    if not song.back_to_arranger:
        song.scenes[0].fire()
        yield
    r = yield from _run_obj_prop_probe(song, "Song", "back_to_arranger", False)
    if r:
        results["Song"]["properties"]["back_to_arranger"] = r
    # Clean up — scene fire starts playback and sets back_to_arranger True
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)  # immediate stop, no quantization
    yield
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield

    # Song.View.selected_scene
    r = yield from _run_obj_prop_probe(view, "Song.View", "selected_scene", song.scenes[6])
    if r:
        results["Song.View"]["properties"]["selected_scene"] = r

    # Song.View.selected_track
    r = yield from _run_obj_prop_probe(view, "Song.View", "selected_track", song.tracks[7])
    if r:
        results["Song.View"]["properties"]["selected_track"] = r

    # Song.appointed_device — track 0 device 1 (Utility)
    r = yield from _run_obj_prop_probe(song, "Song", "appointed_device", song.tracks[0].devices[1])
    if r:
        results["Song"]["properties"]["appointed_device"] = r

    # Song.View.detail_clip — track 1 slot 1 clip (Strum-o-Matic)
    target_clip = song.tracks[1].clip_slots[1].clip
    r = yield from _run_obj_prop_probe(view, "Song.View", "detail_clip", target_clip)
    if r:
        results["Song.View"]["properties"]["detail_clip"] = r
    else:
        log("  [skip] Song.View.detail_clip — no different clip found on track 0")

    # Song.View.highlighted_clip_slot — track 7, scene 6
    r = yield from _run_obj_prop_probe(view, "Song.View", "highlighted_clip_slot", song.tracks[7].clip_slots[6])
    if r:
        results["Song.View"]["properties"]["highlighted_clip_slot"] = r

    # Song.View.selected_chain — drum rack on track 2, chain 5
    orig_track = view.selected_track
    orig_scene = view.selected_scene
    orig_detail = view.detail_clip
    view.selected_track = song.tracks[2]
    yield
    drum_rack = song.tracks[2].devices[0]
    target_chain = drum_rack.chains[5]  # type: ignore[attr-defined]  # RackDevice at runtime
    r = yield from _run_obj_prop_probe(view, "Song.View", "selected_chain", target_chain)
    if r:
        results["Song.View"]["properties"]["selected_chain"] = r
    # Restore view state
    view.selected_track = orig_track
    view.selected_scene = orig_scene
    if orig_detail is not None:
        view.detail_clip = orig_detail
    yield

    # ── Method probes ──────────────────────────────────────────────────────────
    log("[probe_song] Starting method probes")

    if "Song" not in results:
        results["Song"] = {"properties": {}, "methods": {}}
    methods = results["Song"].setdefault("methods", {})

    def _run_method_probe(method, args, check_fn, cleanup_fn=None, *, effect=None):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_method(
            song, "Song", method, args, check_fn, cleanup_fn, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log, effect=effect,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # create_scene (middle index to avoid end-of-list selection edge case)
    ids_before = ptr_set(song.scenes)
    gen = _run_method_probe(
        "create_scene", [len(song.scenes) // 2],
        check_fn=lambda: bool(ptr_set(song.scenes) - ids_before),
        cleanup_fn=lambda: song.delete_scene(find_new_index(song.scenes, ids_before)),
        effect="Song.scenes",
    )
    r = yield from gen
    if r: methods["create_scene"] = r

    # create_midi_track (middle index to avoid end-of-list selection edge case)
    ids_before = ptr_set(song.tracks)
    gen = _run_method_probe(
        "create_midi_track", [len(song.tracks) // 2],
        check_fn=lambda: bool(ptr_set(song.tracks) - ids_before),
        cleanup_fn=lambda: song.delete_track(find_new_index(song.tracks, ids_before)),
        effect="Song.tracks",
    )
    r = yield from gen
    if r: methods["create_midi_track"] = r

    # create_audio_track (middle index to avoid end-of-list selection edge case)
    ids_before = ptr_set(song.tracks)
    gen = _run_method_probe(
        "create_audio_track", [len(song.tracks) // 2],
        check_fn=lambda: bool(ptr_set(song.tracks) - ids_before),
        cleanup_fn=lambda: song.delete_track(find_new_index(song.tracks, ids_before)),
        effect="Song.tracks",
    )
    r = yield from gen
    if r: methods["create_audio_track"] = r

    # create_return_track
    ids_before = ptr_set(song.return_tracks)
    gen = _run_method_probe(
        "create_return_track", [],
        check_fn=lambda: bool(ptr_set(song.return_tracks) - ids_before),
        cleanup_fn=lambda: song.delete_return_track(find_new_index(song.return_tracks, ids_before)),
        effect="Song.return_tracks",
    )
    r = yield from gen
    if r: methods["create_return_track"] = r

    # duplicate_scene (middle index to avoid edge cases)
    ids_before = ptr_set(song.scenes)
    gen = _run_method_probe(
        "duplicate_scene", [len(song.scenes) // 2],
        check_fn=lambda: bool(ptr_set(song.scenes) - ids_before),
        cleanup_fn=lambda: song.delete_scene(find_new_index(song.scenes, ids_before)),
        effect="Song.scenes",
    )
    r = yield from gen
    if r: methods["duplicate_scene"] = r

    # duplicate_track (middle index to avoid edge cases)
    ids_before = ptr_set(song.tracks)
    gen = _run_method_probe(
        "duplicate_track", [len(song.tracks) // 2],
        check_fn=lambda: bool(ptr_set(song.tracks) - ids_before),
        cleanup_fn=lambda: song.delete_track(find_new_index(song.tracks, ids_before)),
        effect="Song.tracks",
    )
    r = yield from gen
    if r: methods["duplicate_track"] = r

    # set_or_delete_cue
    ids_before = ptr_set(song.cue_points)
    gen = _run_method_probe(
        "set_or_delete_cue", [],
        check_fn=lambda: ptr_set(song.cue_points) != ids_before,
        effect="Song.cue_points",
    )
    r = yield from gen
    if r: methods["set_or_delete_cue"] = r

    # capture_and_insert_scene (middle index to avoid edge cases)
    ids_before = ptr_set(song.scenes)
    gen = _run_method_probe(
        "capture_and_insert_scene", [len(song.scenes) // 2],
        check_fn=lambda: bool(ptr_set(song.scenes) - ids_before),
        cleanup_fn=lambda: song.delete_scene(find_new_index(song.scenes, ids_before)),
        effect="Song.scenes",
    )
    r = yield from gen
    if r: methods["capture_and_insert_scene"] = r

    # delete_scene (middle index — undo restores it)
    num_scenes = len(song.scenes)
    gen = _run_method_probe(
        "delete_scene", [num_scenes // 2],
        check_fn=lambda: len(song.scenes) < num_scenes,
        effect="Song.scenes",
    )
    r = yield from gen
    if r: methods["delete_scene"] = r

    # delete_track (middle index — undo restores it)
    num_tracks = len(song.tracks)
    gen = _run_method_probe(
        "delete_track", [num_tracks // 2],
        check_fn=lambda: len(song.tracks) < num_tracks,
        effect="Song.tracks",
    )
    r = yield from gen
    if r: methods["delete_track"] = r

    # delete_return_track (middle index — undo restores it)
    num_rt = len(song.return_tracks)
    gen = _run_method_probe(
        "delete_return_track", [num_rt // 2],
        check_fn=lambda: len(song.return_tracks) < num_rt,
        effect="Song.return_tracks",
    )
    r = yield from gen
    if r: methods["delete_return_track"] = r

    # ── Transport / position method probes ───────────────────────────────────
    log("[probe_song] Starting transport/position method probes")

    # start_playing
    gen = _run_method_probe(
        "start_playing", [],
        check_fn=lambda: song.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="Song.is_playing",
    )
    r = yield from gen
    if r: methods["start_playing"] = r

    # stop_playing — start first so we can test stopping
    song.start_playing()
    yield
    gen = _run_method_probe(
        "stop_playing", [],
        check_fn=lambda: not song.is_playing,
        effect="Song.is_playing",
    )
    r = yield from gen
    if r: methods["stop_playing"] = r
    if song.is_playing:
        song.stop_playing()
        yield

    # continue_playing
    gen = _run_method_probe(
        "continue_playing", [],
        check_fn=lambda: song.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="Song.is_playing",
    )
    r = yield from gen
    if r: methods["continue_playing"] = r

    # play_selection
    gen = _run_method_probe(
        "play_selection", [],
        check_fn=lambda: song.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="Song.is_playing",
    )
    r = yield from gen
    if r: methods["play_selection"] = r

    # stop_all_clips — fire track 0 slot 0 clip, then probe stopping it
    clip_slot = song.tracks[0].clip_slots[0]
    orig_quant = song.clip_trigger_quantization
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    clip_slot.fire()
    yield
    song.clip_trigger_quantization = orig_quant
    yield
    gen = _run_method_probe(
        "stop_all_clips", [False],
        check_fn=lambda: not clip_slot.clip.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
    )
    r = yield from gen
    if r: methods["stop_all_clips"] = r
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield

    # jump_by
    song.current_song_time = 0.0
    yield
    gen = _run_method_probe(
        "jump_by", [4.0],
        check_fn=lambda: song.current_song_time >= 4.0,
    )
    r = yield from gen
    if r: methods["jump_by"] = r
    song.current_song_time = 0.0
    yield

    # scrub_by
    gen = _run_method_probe(
        "scrub_by", [4.0],
        check_fn=lambda: song.current_song_time >= 4.0,
    )
    r = yield from gen
    if r: methods["scrub_by"] = r
    song.current_song_time = 0.0
    yield

    # jump_to_prev_cue
    song.current_song_time = song.song_length
    yield
    gen = _run_method_probe(
        "jump_to_prev_cue", [],
        check_fn=lambda: song.current_song_time < song.song_length,
    )
    r = yield from gen
    if r: methods["jump_to_prev_cue"] = r

    # jump_to_next_cue
    song.current_song_time = 0.0
    yield
    gen = _run_method_probe(
        "jump_to_next_cue", [],
        check_fn=lambda: song.current_song_time > 0.0,
    )
    r = yield from gen
    if r: methods["jump_to_next_cue"] = r

    # Reset position
    song.current_song_time = 0.0
    yield

    # ── Data store method probes ───────────────────────────────────────────────
    log("[probe_song] Starting data store method probes")

    test_key = "__liverelay_probe_test"
    gen = _run_method_probe(
        "set_data", [test_key, "probe_value"],
        check_fn=lambda: song.get_data(test_key, None) == "probe_value",
        cleanup_fn=lambda: song.set_data(test_key, None),
    )
    r = yield from gen
    if r: methods["set_data"] = r
    song.set_data(test_key, None)
    yield

    # ── State-changing methods with preconditions ───────────────────────────
    log("[probe_song] Starting precondition method probes")

    # move_device — move Auto Filter from track 1 to end of track 0
    track0 = song.tracks[0]
    track1 = song.tracks[1]
    num_devs_t0 = len(track0.devices)
    device_to_move = track1.devices[1]
    gen = _run_method_probe(
        "move_device", [device_to_move, track0, num_devs_t0],
        check_fn=lambda: len(track0.devices) > num_devs_t0,
        effect="Track.devices",
    )
    r = yield from gen
    if r: methods["move_device"] = r

    # trigger_session_record
    gen = _run_method_probe(
        "trigger_session_record", [],
        check_fn=lambda: song.session_record,
        cleanup_fn=lambda: song.stop_playing(),
        effect="Song.session_record",
    )
    r = yield from gen
    if r: methods["trigger_session_record"] = r
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield

    # ── Song.View method probes ────────────────────────────────────────────────
    log("[probe_song] Starting Song.View method probes")

    view_methods = results["Song.View"].setdefault("methods", {})

    # select_device — use track 1 device 0 (Strum-o-Matic)
    target_device = song.tracks[1].devices[0]
    snap, snap_json = snapshot_properties(snapshot_targets)
    gen = probe_method(
        song, "Song.View", "select_device", [target_device, True],
        check_fn=lambda: (song.appointed_device is not None
                          and song.appointed_device._live_ptr == target_device._live_ptr),
        cleanup_fn=None, fired=fired, probe_timing=probe_timing,
        snapshot=snap, snap_json=snap_json, snapshot_targets=snapshot_targets,
        snapshot_extra=SNAPSHOT_EXTRA, log=log, obj=view,
    )
    try:
        while True:
            next(gen)
            yield
    except StopIteration as e:
        if e.value is not None:
            view_methods["select_device"] = e.value

    # ── CuePoint probes ─────────────────────────────────────────────────────
    log("[probe_song] Starting CuePoint probes")

    results["CuePoint"] = {"properties": {}, "methods": {}}

    # CuePoint.name (settable, listenable) — cue 0 is "Intro" at time 0.0
    cue = song.cue_points[0]
    snap, snap_json = snapshot_properties(snapshot_targets)
    gen = probe_property(
        song, cue, "CuePoint", "name", "__probe_test__", fired, probe_timing,
        snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
    )
    try:
        while True:
            next(gen)
            yield
    except StopIteration as e:
        if e.value is not None:
            results["CuePoint"]["properties"]["name"] = e.value

    # CuePoint.jump() — cue 1 is "Verse 1" at time 32.0
    cue1 = song.cue_points[1]
    song.current_song_time = 0.0
    yield
    snap, snap_json = snapshot_properties(snapshot_targets)
    gen = probe_method(
        song, "CuePoint", "jump", [],
        check_fn=lambda: song.current_song_time > 0.0,
        cleanup_fn=None, fired=fired, probe_timing=probe_timing,
        snapshot=snap, snap_json=snap_json, snapshot_targets=snapshot_targets,
        snapshot_extra=SNAPSHOT_EXTRA, log=log, obj=cue1,
    )
    try:
        while True:
            next(gen)
            yield
    except StopIteration as e:
        if e.value is not None:
            results["CuePoint"]["methods"]["jump"] = e.value
    song.current_song_time = 0.0
    yield

    # Tear down listeners
    teardown_listeners(song, song_listeners)
    teardown_listeners(view, view_listeners)

    # Write results
    app: Live.Application.Application = Live.Application.get_application()
    version = f"{app.get_major_version()}.{app.get_minor_version()}.{app.get_bugfix_version()}"
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "stubs")
    outpath = os.path.join(outdir, version, "pipeline", "ProbeResults.json")

    # Merge with existing results if present
    existing_classes: dict[str, Any] = {}
    if os.path.exists(outpath):
        with open(outpath, "r") as f:
            existing_classes = json.load(f).get("classes", {})

    for cls, data in results.items():
        if cls not in existing_classes:
            existing_classes[cls] = {"properties": {}, "methods": {}}
        existing_classes[cls]["properties"].update(data.get("properties", {}))
        existing_classes[cls].setdefault("methods", {}).update(data.get("methods", {}))

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
    log(f"[probe_song] Done — {total_props} properties, {total_methods} methods probed in {elapsed}s, wrote {outpath}")
