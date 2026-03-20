"""Probe the ClipSlot module.

Uses track 0 slot 0 (has clip) and slot 1 (empty) from the demo set.

Usage:
    echo scripts/probes/probe_clipslot.py > /tmp/apicapture_targeted_probe

Skipped members:
    - create_audio_clip — needs audio track, already probed in probe_track
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


# ── Settable properties ───────────────────────────────────────────────────────

CLIPSLOT_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("has_stop_button", True),
]

SKIP_UNDO: set[str] = set()


# ── Behavioral notes ──────────────────────────────────────────────────────────

NOTES: dict[str, str] = {}


# ── Module-specific config ────────────────────────────────────────────────────

LISTENER_EXCLUDE: set[str] = {"current_song_time"}

SNAPSHOT_EXTRA: dict[str, set[str]] = {}

# Cross-module listeners for side effect detection.
CROSS_MODULE_LISTENERS: dict[str, list[str]] = {
    "Song": ["is_playing", "back_to_arranger"],
}


# ── Main probe ────────────────────────────────────────────────────────────────


def run(song: Song, log: Callable) -> Generator[None, None, None]:
    """Probe ClipSlot properties and methods."""
    import time
    from datetime import datetime

    t0 = time.monotonic()
    log("[probe_clipslot] Starting ClipSlot probes")

    # Use track 0 slot 0 (has clip) and slot 1 (empty)
    track = song.tracks[0]
    slot_with_clip = track.clip_slots[0]
    slot_empty = track.clip_slots[1]

    results: dict[str, dict[str, dict[str, Any]]] = {
        "ClipSlot": {"properties": {}, "methods": {}},
    }
    fired: list[tuple[str, str, float]] = []
    probe_timing: dict[str, Any] = {"target": None, "set_time": 0.0, "listener_time": None}

    # Set up listeners and snapshot targets on the slot with a clip
    slot_listenable = discover_listenable(slot_with_clip, LISTENER_EXCLUDE)
    cross_song_props = CROSS_MODULE_LISTENERS.get("Song", [])
    snapshot_targets = [
        (slot_with_clip, "ClipSlot", discover_snapshot_props(
            slot_listenable, "ClipSlot", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
        (song, "Song", cross_song_props),
    ]
    slot_listeners = setup_listeners(slot_with_clip, "ClipSlot", slot_listenable, fired, probe_timing, log)
    song_listeners = setup_listeners(song, "Song", cross_song_props, fired, probe_timing, log)
    yield

    # Switch to session view for consistent clip slot behavior
    import Live
    Live.Application.get_application().view.show_view("Session")
    song.view.highlighted_clip_slot = slot_with_clip
    yield
    fired.clear()

    # ── Properties ────────────────────────────────────────────────────────────

    for prop, test_val in CLIPSLOT_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, slot_with_clip, "ClipSlot", prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["ClipSlot"]["properties"][prop] = e.value

    # ── Methods ───────────────────────────────────────────────────────────────

    methods = results["ClipSlot"]["methods"]

    def _run_method_probe(method, args, check_fn, cleanup_fn=None, *, effect=None, effect_obj=None,
                          obj=None):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_method(
            song, "ClipSlot", method, args, check_fn, cleanup_fn, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
            obj=obj if obj is not None else slot_with_clip,
            effect=effect, effect_obj=effect_obj,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # fire — fire the clip in slot 0
    orig_quant = song.clip_trigger_quantization
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    gen = _run_method_probe(
        "fire", [],
        check_fn=lambda: slot_with_clip.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="ClipSlot.is_playing", effect_obj=slot_with_clip,
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
    song.clip_trigger_quantization = orig_quant
    song.current_song_time = 0.0
    yield

    # stop — fire first, then stop
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    slot_with_clip.fire()
    yield
    song.clip_trigger_quantization = orig_quant
    yield
    gen = _run_method_probe(
        "stop", [],
        check_fn=lambda: not slot_with_clip.is_playing,
        effect="ClipSlot.is_playing", effect_obj=slot_with_clip,
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

    # create_clip — create a MIDI clip in empty slot 1
    gen = _run_method_probe(
        "create_clip", [4.0],
        check_fn=lambda: slot_empty.has_clip,
        obj=slot_empty,
        effect="ClipSlot.has_clip", effect_obj=slot_empty,
    )
    r = yield from gen
    if r: methods["create_clip"] = r

    # delete_clip — delete the clip in slot 0 (undo restores it)
    gen = _run_method_probe(
        "delete_clip", [],
        check_fn=lambda: not slot_with_clip.has_clip,
        effect="ClipSlot.has_clip", effect_obj=slot_with_clip,
    )
    r = yield from gen
    if r: methods["delete_clip"] = r

    # duplicate_clip_to — duplicate slot 0's clip to slot 1
    # Ensure slot 1 is empty first (undo from create_clip should have cleared it)
    gen = _run_method_probe(
        "duplicate_clip_to", [slot_empty],
        check_fn=lambda: slot_empty.has_clip,
        effect="ClipSlot.has_clip", effect_obj=slot_empty,
    )
    r = yield from gen
    if r: methods["duplicate_clip_to"] = r

    # set_fire_button_state — set to True then undo
    gen = _run_method_probe(
        "set_fire_button_state", [True],
        check_fn=lambda: slot_with_clip.is_triggered,
        effect="ClipSlot.is_triggered", effect_obj=slot_with_clip,
    )
    r = yield from gen
    if r: methods["set_fire_button_state"] = r
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

    # Tear down listeners
    teardown_listeners(slot_with_clip, slot_listeners)
    teardown_listeners(song, song_listeners)

    # Write results
    import Live

    app: Live.Application.Application = Live.Application.get_application()
    version = f"{app.get_major_version()}.{app.get_minor_version()}.{app.get_bugfix_version()}"
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "..", "stubs")
    outpath = os.path.join(outdir, version, "pipeline", "ProbeResults.json")

    # Merge — replace classes this probe covers, keep others
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
    log(f"[probe_clipslot] Done — {total_props} properties, {total_methods} methods probed in {elapsed}s")
