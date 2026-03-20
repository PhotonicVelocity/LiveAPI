"""Probe the Track module — Track and Track.View classes.

Probes undo tracking, async visibility, side effects, and behavioral metadata
for settable properties and state-changing methods on Track objects.

Uses track 0 (Coffee Leaf) from the demo set as the primary probe target.

Usage:
    echo scripts/probes/probe_track.py > /tmp/apicapture_targeted_probe

Skipped members:
    - fold_state, is_showing_chains — need a group track (demo set has none)
    - current_input/output_routing, current_input/output_sub_routing — string-based API deprecated
    - get_data — read-only
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

TRACK_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("arm", True),
    ("color", 42),
    ("color_index", 10),
    ("current_monitoring_state", 2),  # 0=in, 1=auto, 2=off
    ("implicit_arm", True),
    ("mute", True),
    ("name", "__probe_test__"),
    ("solo", True),
]

VIEW_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("device_insert_mode", True),
    ("is_collapsed", True),
]

# Properties skipped from undo probing.
SKIP_UNDO: set[str] = set()


# ── Behavioral notes ──────────────────────────────────────────────────────────

NOTES: dict[str, str] = {}


# ── Module-specific config ────────────────────────────────────────────────────

LISTENER_EXCLUDE: set[str] = {"current_song_time"}

SNAPSHOT_EXTRA: dict[str, set[str]] = {
    "Track": {"name"},
}

# Cross-module listenable properties to subscribe to for side effect detection.
CROSS_MODULE_LISTENERS: dict[str, list[str]] = {
    "Song": ["is_playing", "back_to_arranger"],
    "Song.View": ["detail_clip"],
}


# ── Main probe ────────────────────────────────────────────────────────────────


def run(song: Song, log: Callable) -> Generator[None, None, None]:
    """Probe Track and Track.View properties and methods."""
    import time
    from datetime import datetime

    t0 = time.monotonic()
    log("[probe_track] Starting Track probes")

    # Use track 0 (Coffee Leaf) as probe target
    track = song.tracks[0]
    track_view = track.view
    results: dict[str, dict[str, dict[str, Any]]] = {
        "Track": {"properties": {}},
        "Track.View": {"properties": {}},
    }
    fired: list[tuple[str, str, float]] = []
    probe_timing: dict[str, Any] = {"target": None, "set_time": 0.0, "listener_time": None}

    # Set up listeners and snapshot targets
    track_listenable = discover_listenable(track, LISTENER_EXCLUDE)
    view_listenable = discover_listenable(track_view, LISTENER_EXCLUDE)
    cross_song_props = CROSS_MODULE_LISTENERS.get("Song", [])
    cross_view_props = CROSS_MODULE_LISTENERS.get("Song.View", [])
    snapshot_targets = [
        (track, "Track", discover_snapshot_props(track_listenable, "Track", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
        (track_view, "Track.View", discover_snapshot_props(view_listenable, "Track.View", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
        (song, "Song", cross_song_props),
        (song.view, "Song.View", cross_view_props),
    ]
    track_listeners = setup_listeners(track, "Track", track_listenable, fired, probe_timing, log)
    view_listeners = setup_listeners(track_view, "Track.View", view_listenable, fired, probe_timing, log)
    # Cross-module listeners for side effect detection
    song_listeners = setup_listeners(song, "Song", cross_song_props, fired, probe_timing, log)
    song_view_listeners = setup_listeners(song.view, "Song.View", cross_view_props, fired, probe_timing, log)
    yield  # let listener setup settle

    # Track properties
    for prop, test_val in TRACK_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, track, "Track", prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Track"]["properties"][prop] = e.value

    # Track.View properties
    for prop, test_val in VIEW_SETTABLE_PROPS:
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, track_view, "Track.View", prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Track.View"]["properties"][prop] = e.value

    # ── Special-case property probes ─────────────────────────────────────────

    def _run_prop_probe(obj, cls, prop, test_val):
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

    # Track.back_to_arranger — same as Song, engine sets True on session clip trigger
    if not track.back_to_arranger:
        song.scenes[0].fire()
        yield
    r = yield from _run_prop_probe(track, "Track", "back_to_arranger", False)
    if r:
        results["Track"]["properties"]["back_to_arranger"] = r
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    if track.back_to_arranger:
        track.back_to_arranger = False
        yield
    song.current_song_time = 0.0
    yield

    # ── Routing property probes ─────────────────────────────────────────────
    log("[probe_track] Starting routing property probes")

    # input_routing_type — pick a different type from available list
    avail_in_types = track.available_input_routing_types
    current_in_type = track.input_routing_type
    target_in_type = None
    for rt in avail_in_types:
        if rt.display_name != current_in_type.display_name:
            target_in_type = rt
            break
    if target_in_type is not None:
        r = yield from _run_prop_probe(track, "Track", "input_routing_type", target_in_type)
        if r:
            results["Track"]["properties"]["input_routing_type"] = r

    # output_routing_type — pick a different type from available list
    avail_out_types = track.available_output_routing_types
    current_out_type = track.output_routing_type
    target_out_type = None
    for rt in avail_out_types:
        if rt.display_name != current_out_type.display_name:
            target_out_type = rt
            break
    if target_out_type is not None:
        r = yield from _run_prop_probe(track, "Track", "output_routing_type", target_out_type)
        if r:
            results["Track"]["properties"]["output_routing_type"] = r

    # input_routing_channel — pick a different channel from available list
    avail_in_channels = track.available_input_routing_channels
    current_in_channel = track.input_routing_channel
    target_in_channel = None
    for rc in avail_in_channels:
        if rc.display_name != current_in_channel.display_name:
            target_in_channel = rc
            break
    if target_in_channel is not None:
        r = yield from _run_prop_probe(track, "Track", "input_routing_channel", target_in_channel)
        if r:
            results["Track"]["properties"]["input_routing_channel"] = r

    # output_routing_channel — "Main" only has one empty channel, so switch to "Ext. Out" first
    orig_out_type = track.output_routing_type
    ext_out = next((rt for rt in track.available_output_routing_types if rt.display_name == "Ext. Out"), None)
    if ext_out is not None:
        track.output_routing_type = ext_out
        yield
        avail_out_channels = track.available_output_routing_channels
        current_out_channel = track.output_routing_channel
        target_out_channel = None
        for rc in avail_out_channels:
            if rc.display_name != current_out_channel.display_name:
                target_out_channel = rc
                break
        if target_out_channel is not None:
            r = yield from _run_prop_probe(track, "Track", "output_routing_channel", target_out_channel)
            if r:
                results["Track"]["properties"]["output_routing_channel"] = r
        # Restore original output routing
        track.output_routing_type = orig_out_type
        yield

    # String-based routing (current_input_routing, etc.) — skipped.
    # The getter returns a prefixed format ("Ext: All Ins") that doesn't match the
    # available names from input_routings ("All Ins"). Setting with available names
    # silently fails (no_change). Use the object-based API (input_routing_type, etc.) instead.

    # ── Method probes ──────────────────────────────────────────────────────────
    log("[probe_track] Starting method probes")

    methods = results["Track"].setdefault("methods", {})

    def _run_method_probe(method, args, check_fn, cleanup_fn=None, *, obj=None, effect=None, effect_obj=None):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_method(
            song, "Track" if obj is None else "Track.View", method, args, check_fn, cleanup_fn,
            fired, probe_timing, snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
            obj=obj if obj is not None else track, effect=effect, effect_obj=effect_obj,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # create_midi_clip — creates an arrangement clip at a given position
    # Track 0 is a MIDI track (Coffee Leaf / Drift synth)
    gen = _run_method_probe(
        "create_midi_clip", [500.0, 4.0],  # position 500 (past existing clips), length 4 beats
        check_fn=lambda: any(
            c.start_time == 500.0 for c in track.arrangement_clips
        ),
        effect="Track.arrangement_clips",
    )
    r = yield from gen
    if r: methods["create_midi_clip"] = r

    # delete_clip — delete session clip at slot 0, undo restores it
    clip_to_delete = track.clip_slots[0].clip
    gen = _run_method_probe(
        "delete_clip", [clip_to_delete],
        check_fn=lambda: not track.clip_slots[0].has_clip,
        effect="ClipSlot.has_clip", effect_obj=track.clip_slots[0],
    )
    r = yield from gen
    if r: methods["delete_clip"] = r

    # duplicate_clip_slot — duplicate slot 0 into next free slot (lands in slot 1)
    gen = _run_method_probe(
        "duplicate_clip_slot", [0],
        check_fn=lambda: track.clip_slots[1].has_clip,
        effect="ClipSlot.has_clip", effect_obj=track.clip_slots[1],
    )
    r = yield from gen
    if r: methods["duplicate_clip_slot"] = r

    # duplicate_clip_to_arrangement — duplicate session clip to arrangement
    clip_to_dup = track.clip_slots[0].clip
    num_arr_before = len(track.arrangement_clips)
    gen = _run_method_probe(
        "duplicate_clip_to_arrangement", [clip_to_dup, 600.0],  # far position to avoid overlap
        check_fn=lambda: len(track.arrangement_clips) > num_arr_before,
        effect="Track.arrangement_clips",
    )
    r = yield from gen
    if r: methods["duplicate_clip_to_arrangement"] = r

    # duplicate_device — duplicate device 1 (Utility) on track 0
    num_devs_before = len(track.devices)
    gen = _run_method_probe(
        "duplicate_device", [1],
        check_fn=lambda: len(track.devices) > num_devs_before,
        effect="Track.devices",
    )
    r = yield from gen
    if r: methods["duplicate_device"] = r

    # delete_device — delete last device (should be safe with undo)
    num_devs = len(track.devices)
    gen = _run_method_probe(
        "delete_device", [num_devs - 1],
        check_fn=lambda: len(track.devices) < num_devs,
        effect="Track.devices",
    )
    r = yield from gen
    if r: methods["delete_device"] = r

    # stop_all_clips — track-level stop
    # Fire a clip first so there's something to stop
    orig_quant = song.clip_trigger_quantization
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    track.clip_slots[0].fire()
    yield
    song.clip_trigger_quantization = orig_quant
    yield
    gen = _run_method_probe(
        "stop_all_clips", [False],
        check_fn=lambda: not track.clip_slots[0].clip.is_playing,
        effect="Track.playing_slot_index",
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
    song.current_song_time = 0.0
    yield

    # set_data
    test_key = "__probe_track_test"
    gen = _run_method_probe(
        "set_data", [test_key, "probe_value"],
        check_fn=lambda: track.get_data(test_key, None) == "probe_value",
        cleanup_fn=lambda: track.set_data(test_key, None),
        effect="Track.data",
    )
    r = yield from gen
    if r: methods["set_data"] = r
    track.set_data(test_key, None)
    yield

    # create_take_lane
    num_lanes_before = len(track.take_lanes)  # type: ignore[attr-defined]
    gen = _run_method_probe(
        "create_take_lane", [],
        check_fn=lambda: len(track.take_lanes) > num_lanes_before,  # type: ignore[attr-defined]
        effect="Track.take_lanes",
    )
    r = yield from gen
    if r: methods["create_take_lane"] = r

    # create_audio_clip — use an audio track (track 10, Vocal Main) and silence.wav
    audio_track = song.tracks[10]
    wav_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "silence.wav")
    num_arr_before = len(audio_track.arrangement_clips)
    snap, snap_json = snapshot_properties(snapshot_targets)
    gen = probe_method(
        song, "Track", "create_audio_clip", [wav_path, 500.0],
        check_fn=lambda: len(audio_track.arrangement_clips) > num_arr_before,
        cleanup_fn=None, fired=fired, probe_timing=probe_timing,
        snapshot=snap, snap_json=snap_json, snapshot_targets=snapshot_targets,
        snapshot_extra=SNAPSHOT_EXTRA, log=log, obj=audio_track,
        effect="Track.arrangement_clips", effect_obj=audio_track,
    )
    try:
        while True:
            next(gen)
            yield
    except StopIteration as e:
        if e.value is not None:
            methods["create_audio_clip"] = e.value

    # insert_device — insert a Compressor at end of track 0
    num_devs_before = len(track.devices)
    gen = _run_method_probe(
        "insert_device", ["Compressor", -1],
        check_fn=lambda: len(track.devices) > num_devs_before,
        effect="Track.devices",
    )
    r = yield from gen
    if r: methods["insert_device"] = r

    # jump_in_running_session_clip — fire a clip, then jump
    orig_quant = song.clip_trigger_quantization
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    track.clip_slots[0].fire()
    yield
    song.clip_trigger_quantization = orig_quant
    yield
    running_clip = track.clip_slots[0].clip
    gen = _run_method_probe(
        "jump_in_running_session_clip", [4.0],
        check_fn=lambda: False,
        effect="Clip.playing_position", effect_obj=running_clip,
    )
    r = yield from gen
    if r: methods["jump_in_running_session_clip"] = r
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

    # ── Track.View method probes ──────────────────────────────────────────────
    log("[probe_track] Starting Track.View method probes")

    view_methods = results["Track.View"].setdefault("methods", {})

    # select_instrument — select a non-instrument device first, then probe select_instrument
    # Track 0 device 1 is Utility (not the instrument), device 0 is Drift (the instrument)
    song.view.select_device(track.devices[1])
    yield
    yield
    gen = _run_method_probe(
        "select_instrument", [],
        check_fn=lambda: False,
        obj=track_view,
        effect="Track.View.selected_device", effect_obj=track_view,
    )
    r = yield from gen
    if r: view_methods["select_instrument"] = r

    # Tear down listeners
    teardown_listeners(track, track_listeners)
    teardown_listeners(track_view, view_listeners)
    teardown_listeners(song, song_listeners)
    teardown_listeners(song.view, song_view_listeners)

    # Write results
    import Live

    app: Live.Application.Application = Live.Application.get_application()
    version = f"{app.get_major_version()}.{app.get_minor_version()}.{app.get_bugfix_version()}"
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "stubs")
    outpath = os.path.join(outdir, version, "pipeline", "ProbeResults.json")

    # Merge with existing results
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
    log(f"[probe_track] Done — {total_props} properties, {total_methods} methods probed in {elapsed}s, wrote {outpath}")
