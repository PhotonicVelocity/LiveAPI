"""Probe the Scene module.

Uses scene 0 ("Intro") from the demo set.

Usage:
    echo scripts/probes/probe_scene.py > /tmp/apicapture_targeted_probe
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

SCENE_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("color", 42),
    ("color_index", 10),
    ("name", "__probe_test__"),
    ("tempo", 140.0),
    ("tempo_enabled", True),
    ("time_signature_denominator", 8),
    ("time_signature_enabled", True),
    ("time_signature_numerator", 3),
]

SKIP_UNDO: set[str] = set()


# ── Behavioral notes ──────────────────────────────────────────────────────────

NOTES: dict[str, str] = {
    "Scene.fire": (
        "With quantization, the effect is on ``is_triggered``."
    ),
    "Scene.set_fire_button_state": (
        "With quantization, the effect is on ``is_triggered``. "
        "Supports press/release for Gate and Repeat launch modes."
    ),
    "Scene.tempo": (
        "Setting a value auto-enables ``tempo_enabled``. "
        "A value of ``-1`` means 'use song tempo'."
    ),
    "Scene.time_signature_denominator": (
        "Setting a value auto-enables ``time_signature_enabled`` and initializes "
        "``time_signature_numerator`` to ``4`` if unset. "
        "A value of ``-1`` means 'use song time signature'."
    ),
    "Scene.time_signature_numerator": (
        "Setting a value auto-enables ``time_signature_enabled`` and initializes "
        "``time_signature_denominator`` to ``4`` if unset. "
        "A value of ``-1`` means 'use song time signature'."
    ),
}


# ── Module-specific config ────────────────────────────────────────────────────

LISTENER_EXCLUDE: set[str] = {"current_song_time"}

SNAPSHOT_EXTRA: dict[str, set[str]] = {}

CROSS_MODULE_LISTENERS: dict[str, list[str]] = {
    "Song": ["is_playing", "back_to_arranger"],
}


# ── Main probe ────────────────────────────────────────────────────────────────


def run(song: Song, log: Callable) -> Generator[None, None, None]:
    """Probe Scene properties and methods."""
    import time
    from datetime import datetime

    t0 = time.monotonic()
    log("[probe_scene] Starting Scene probes")

    scene = song.scenes[0]  # "Intro" at time 0.0

    results: dict[str, dict[str, dict[str, Any]]] = {
        "Scene": {"properties": {}, "methods": {}},
    }
    fired: list[tuple[str, str, float]] = []
    probe_timing: dict[str, Any] = {"target": None, "set_time": 0.0, "listener_time": None}

    # Set up listeners and snapshot targets
    scene_listenable = discover_listenable(scene, LISTENER_EXCLUDE)
    cross_song_props = CROSS_MODULE_LISTENERS.get("Song", [])
    snapshot_targets = [
        (scene, "Scene", discover_snapshot_props(scene_listenable, "Scene", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
        (song, "Song", cross_song_props),
    ]
    scene_listeners = setup_listeners(scene, "Scene", scene_listenable, fired, probe_timing, log)
    song_listeners = setup_listeners(song, "Song", cross_song_props, fired, probe_timing, log)
    yield

    # Switch to session view
    import Live
    Live.Application.get_application().view.show_view("Session")
    yield
    fired.clear()

    # ── Properties ────────────────────────────────────────────────────────────

    for prop, test_val in SCENE_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, scene, "Scene", prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Scene"]["properties"][prop] = e.value

    # ── Methods ───────────────────────────────────────────────────────────────

    methods = results["Scene"]["methods"]
    orig_quant = song.clip_trigger_quantization

    def _run_method_probe(method, args, check_fn, cleanup_fn=None, *, effect=None, effect_obj=None):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_method(
            song, "Scene", method, args, check_fn, cleanup_fn, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
            obj=scene, effect=effect, effect_obj=effect_obj,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # fire — fires all clips in the scene
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    gen = _run_method_probe(
        "fire", [],
        check_fn=lambda: song.tracks[0].clip_slots[0].is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="ClipSlot.is_playing", effect_obj=song.tracks[0].clip_slots[0],
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

    # fire_as_selected — same as fire but selects next scene
    gen = _run_method_probe(
        "fire_as_selected", [],
        check_fn=lambda: song.tracks[0].clip_slots[0].is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="ClipSlot.is_playing", effect_obj=song.tracks[0].clip_slots[0],
    )
    r = yield from gen
    if r: methods["fire_as_selected"] = r
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
        check_fn=lambda: song.tracks[0].clip_slots[0].is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="ClipSlot.is_playing", effect_obj=song.tracks[0].clip_slots[0],
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

    # Tear down listeners
    teardown_listeners(scene, scene_listeners)
    teardown_listeners(song, song_listeners)

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
    log(f"[probe_scene] Done — {total_props} properties, {total_methods} methods probed in {elapsed}s")
