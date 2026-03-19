"""Probe the Track module — Track and Track.View classes.

Probes undo tracking, async visibility, side effects, and behavioral metadata
for settable properties and state-changing methods on Track objects.

Uses track 0 (Coffee Leaf) from the demo set as the primary probe target.

Usage:
    echo scripts/probes/probe_track.py > /tmp/apicapture_targeted_probe

Skipped members:
    - fold_state, is_showing_chains — need a group track (demo set has none)
    - input_routing_channel, input_routing_type — RoutingType objects, special-case
    - output_routing_channel, output_routing_type — RoutingType objects, special-case
    - current_input_routing, current_input_sub_routing — need available routing names
    - current_output_routing, current_output_sub_routing — need available routing names
    - get_data — read-only
    - jump_in_running_session_clip — needs a running clip
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
