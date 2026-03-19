"""Probe the Track module — Track and Track.View classes.

Probes undo tracking, async visibility, side effects, and behavioral metadata
for settable properties and state-changing methods on Track objects.

Uses track 0 (Coffee Leaf) from the demo set as the primary probe target.

Usage:
    echo scripts/probes/probe_track.py > /tmp/apicapture_targeted_probe

Skipped members:
    - fold_state, is_showing_chains — need a group track (demo set has none)
    - get_data — read-only
    - jump_in_running_session_clip — needs a running session clip
    - insert_device — needs a device URI/browser item
    - create_audio_clip — needs a valid audio file path
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
SKIP_UNDO: set[str] = {
    "back_to_arranger",  # engine-driven, same as Song.back_to_arranger
}


# ── Behavioral notes ──────────────────────────────────────────────────────────

NOTES: dict[str, str] = {}


# ── Module-specific config ────────────────────────────────────────────────────

LISTENER_EXCLUDE: set[str] = {"current_song_time"}

SNAPSHOT_EXTRA: dict[str, set[str]] = {
    "Track": {"name"},
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
    snapshot_targets = [
        (track, "Track", discover_snapshot_props(track_listenable, "Track", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
        (track_view, "Track.View", discover_snapshot_props(view_listenable, "Track.View", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
    ]
    track_listeners = setup_listeners(track, "Track", track_listenable, fired, probe_timing, log)
    view_listeners = setup_listeners(track_view, "Track.View", view_listenable, fired, probe_timing, log)
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

    # ── Routing property probes ─────────────────────────────────────────────
    log("[probe_track] Starting routing property probes")

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

    # output_routing_channel — pick a different channel from available list
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

    # current_input_routing — string-based routing (pick different from available)
    avail_in_names = list(track.input_routings)
    current_in_name = track.current_input_routing
    target_in_name = next((n for n in avail_in_names if n != current_in_name), None)
    if target_in_name is not None:
        r = yield from _run_prop_probe(track, "Track", "current_input_routing", target_in_name)
        if r:
            results["Track"]["properties"]["current_input_routing"] = r

    # current_output_routing — string-based routing
    avail_out_names = list(track.output_routings)
    current_out_name = track.current_output_routing
    target_out_name = next((n for n in avail_out_names if n != current_out_name), None)
    if target_out_name is not None:
        r = yield from _run_prop_probe(track, "Track", "current_output_routing", target_out_name)
        if r:
            results["Track"]["properties"]["current_output_routing"] = r

    # current_input_sub_routing — string-based sub-routing
    avail_in_sub = list(track.input_sub_routings)
    current_in_sub = track.current_input_sub_routing
    target_in_sub = next((n for n in avail_in_sub if n != current_in_sub), None)
    if target_in_sub is not None:
        r = yield from _run_prop_probe(track, "Track", "current_input_sub_routing", target_in_sub)
        if r:
            results["Track"]["properties"]["current_input_sub_routing"] = r

    # current_output_sub_routing — string-based sub-routing
    avail_out_sub = list(track.output_sub_routings)
    current_out_sub = track.current_output_sub_routing
    target_out_sub = next((n for n in avail_out_sub if n != current_out_sub), None)
    if target_out_sub is not None:
        r = yield from _run_prop_probe(track, "Track", "current_output_sub_routing", target_out_sub)
        if r:
            results["Track"]["properties"]["current_output_sub_routing"] = r

    # ── Method probes ──────────────────────────────────────────────────────────
    log("[probe_track] Starting method probes")

    methods = results["Track"].setdefault("methods", {})

    def _run_method_probe(method, args, check_fn, cleanup_fn=None, *, obj=None):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_method(
            song, "Track" if obj is None else "Track.View", method, args, check_fn, cleanup_fn,
            fired, probe_timing, snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
            obj=obj if obj is not None else track,
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
    )
    r = yield from gen
    if r: methods["create_midi_clip"] = r

    # delete_clip — delete session clip at slot 0, undo restores it
    clip_to_delete = track.clip_slots[0].clip
    gen = _run_method_probe(
        "delete_clip", [clip_to_delete],
        check_fn=lambda: not track.clip_slots[0].has_clip,
    )
    r = yield from gen
    if r: methods["delete_clip"] = r

    # duplicate_clip_slot — duplicate slot 0 into next free slot
    num_clips_before = sum(1 for cs in track.clip_slots if cs.has_clip)
    gen = _run_method_probe(
        "duplicate_clip_slot", [0],
        check_fn=lambda: sum(1 for cs in track.clip_slots if cs.has_clip) > num_clips_before,
    )
    r = yield from gen
    if r: methods["duplicate_clip_slot"] = r

    # duplicate_clip_to_arrangement — duplicate session clip to arrangement
    clip_to_dup = track.clip_slots[0].clip
    num_arr_before = len(track.arrangement_clips)
    gen = _run_method_probe(
        "duplicate_clip_to_arrangement", [clip_to_dup, 600.0],  # far position to avoid overlap
        check_fn=lambda: len(track.arrangement_clips) > num_arr_before,
    )
    r = yield from gen
    if r: methods["duplicate_clip_to_arrangement"] = r

    # duplicate_device — duplicate device 1 (Utility) on track 0
    num_devs_before = len(track.devices)
    gen = _run_method_probe(
        "duplicate_device", [1],
        check_fn=lambda: len(track.devices) > num_devs_before,
    )
    r = yield from gen
    if r: methods["duplicate_device"] = r

    # delete_device — delete last device (should be safe with undo)
    num_devs = len(track.devices)
    gen = _run_method_probe(
        "delete_device", [num_devs - 1],
        check_fn=lambda: len(track.devices) < num_devs,
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

    # set_data
    test_key = "__probe_track_test"
    gen = _run_method_probe(
        "set_data", [test_key, "probe_value"],
        check_fn=lambda: track.get_data(test_key, None) == "probe_value",
        cleanup_fn=lambda: track.set_data(test_key, None),
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
    )
    r = yield from gen
    if r: methods["create_take_lane"] = r

    # ── Track.View method probes ──────────────────────────────────────────────
    log("[probe_track] Starting Track.View method probes")

    view_methods = results["Track.View"].setdefault("methods", {})

    # select_instrument — selects the track's instrument device, returns bool
    gen = _run_method_probe(
        "select_instrument", [],
        check_fn=lambda: False,  # returns bool, no observable state change to check
        obj=track_view,
    )
    r = yield from gen
    if r: view_methods["select_instrument"] = r

    # Tear down listeners
    teardown_listeners(track, track_listeners)
    teardown_listeners(track_view, view_listeners)

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
