"""Probe undo tracking and async visibility for settable Song properties.

Runs inside Live via the targeted probe trigger. Uses yield to cross tick boundaries,
which is essential for accurately classifying async visibility — a property is "immediate"
if the new value is readable on the same tick as the set, "next_tick" if it only appears
after yielding.

Usage:
    echo scripts/probes/song_props.py > /tmp/apicapture_targeted_probe
"""

from __future__ import annotations

import json
import os
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

    import Live
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
    ("scale_name", "Minor"),
    ("signature_denominator", 8),
    ("signature_numerator", 3),
    ("swing_amount", 0.6),
    ("tempo", 130.0),
    ("tempo_follower_enabled", True),
    ("is_ableton_link_enabled", True),
    ("is_ableton_link_start_stop_sync_enabled", True),
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
    "record_mode",
    "session_record",
    "session_automation_record",
    "current_song_time",
    "start_time",
}


# ── Listenable properties (for side-effect detection) ─────────────────────────

# Excluded from listening
LISTENER_EXCLUDE: set[str] = {"current_song_time"} # fires every audio tick (~80/s)


def _discover_listenable(obj: object) -> list[str]:
    """Discover listenable properties by finding add_*_listener methods on the object."""
    props = []
    for name in dir(obj):
        if name.startswith("add_") and name.endswith("_listener"):
            prop = name[4:-9]  # strip "add_" prefix and "_listener" suffix
            if prop not in LISTENER_EXCLUDE:
                props.append(prop)
    return sorted(props)


# ── Listener infrastructure ───────────────────────────────────────────────────


def setup_listeners(
    obj: Song | Song.View, cls: str, props: list[str], fired: list, probe_timing: dict, log: Callable,
) -> list[tuple[str, Any]]:
    """Add listeners for all listenable properties. Returns [(prop, callback)] for teardown.

    probe_timing is a shared dict with:
      - "target": (cls, prop) currently being probed, or None
      - "set_time": monotonic time when the property was set
      - "listener_time": monotonic time when the self-listener fired
    """
    import time

    listeners: list[tuple[str, Any]] = []
    for prop in props:
        add_fn = getattr(obj, f"add_{prop}_listener", None)
        if add_fn is None:
            continue

        def make_cb(c: str, p: str):
            def callback():
                now = time.monotonic()
                set_time = probe_timing.get("set_time", 0.0)
                dt = now - set_time
                fired.append((c, p, dt))
                target = probe_timing.get("target")
                if target == (c, p):
                    probe_timing["listener_time"] = now
                log(f"    [listener] {c}.{p} fired ({dt*1000:.1f}ms)")
            return callback

        cb = make_cb(cls, prop)
        try:
            add_fn(cb)
            listeners.append((prop, cb))
        except Exception:
            pass
    log(f"  Subscribed to {len(listeners)}/{len(props)} listeners on {cls}")
    return listeners


def teardown_listeners(obj: Song | Song.View, listeners: list[tuple[str, Any]]) -> None:
    """Remove all listeners added by setup_listeners."""
    for prop, cb in listeners:
        remove_fn = getattr(obj, f"remove_{prop}_listener", None)
        if remove_fn:
            try:
                remove_fn(cb)
            except Exception:
                pass


# ── Helpers ────────────────────────────────────────────────────────────────────


def snapshot_listenables(objects: list[tuple[Any, str, list[str]]]) -> dict[tuple[str, str], Any]:
    """Read current values of all listenable properties.

    Args:
        objects: [(obj, cls_name, prop_list), ...] — e.g. [(song, "Song", SONG_LISTENABLE), ...]

    Returns:
        {(cls, prop): value, ...} for every readable property.
    """
    snap: dict[tuple[str, str], Any] = {}
    for obj, cls, props in objects:
        for prop in props:
            try:
                snap[(cls, prop)] = getattr(obj, prop)
            except Exception:
                pass
    return snap


def fuzzy_eq(a: Any, b: Any) -> bool:
    """Compare with tolerance for float precision."""
    if isinstance(a, float) and isinstance(b, float):
        return abs(a - b) < 0.01
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) < 0.01
    return a == b


def probe_property(
    song: Song, obj: Song | Song.View, cls: str, prop: str, test_value: Any, fired: list, probe_timing: dict,
    snapshot: dict, listenables: list[tuple[Any, str, list[str]]], log: Callable,
) -> Generator[None, None, dict[str, Any]]:
    """Probe a single property for undo tracking, async visibility, and side effects.

    This is a generator — each yield crosses a tick boundary.

    Args:
        snapshot: {(cls, prop): value} — pre-probe snapshot of all listenable properties,
            used to check whether side effects are restored after undo.
    """
    result: dict[str, Any] = {}

    try:
        # 1. Read original value.
        orig = getattr(obj, prop)
        if isinstance(orig, bool):
            test_value = not orig
        if fuzzy_eq(orig, test_value):
            result["async_visibility"] = "skip"
            result["undo_tracked"] = "skip"
            result["notes"] = f"test_value matches original ({orig!r})"
            log(f"  [prop] {cls}.{prop}: skip — test_value matches original ({orig!r})")
            return result

        # 2. Clear fired listeners and set timing target.
        import time as _time

        fired.clear()
        probe_timing["target"] = (cls, prop)
        probe_timing["listener_time"] = None

        # 3. begin_undo_step, set, end_undo_step.
        song.begin_undo_step()
        probe_timing["set_time"] = _time.monotonic()
        setattr(obj, prop, test_value)
        song.end_undo_step()

        # 4. Read back immediately.
        readback = getattr(obj, prop)
        is_immediate = fuzzy_eq(readback, test_value)

        # 5. Yield to next tick.
        yield

        # 6. If not immediate, check again.
        if is_immediate:
            result["async_visibility"] = "immediate"
        else:
            readback_next = getattr(obj, prop)
            if fuzzy_eq(readback_next, test_value):
                result["async_visibility"] = "next_tick"
            else:
                result["async_visibility"] = "no_change"

        # 7. Collect side effects and listener timing.
        side_effects = [
            {"label": c, "prop": p, "listener_latency_ms": round(dt * 1000, 1)}
            for c, p, dt in fired
            if not (c == cls and p == prop)
        ]
        if probe_timing["listener_time"] is not None:
            dt = probe_timing["listener_time"] - probe_timing["set_time"]
            result["listener_latency_ms"] = round(dt * 1000, 1)

        probe_timing["target"] = None

        # 8. Clear fired and undo.
        fired.clear()
        song.undo()

        # 9. Yield to next tick.
        yield

        # 10. Read back → undo tracking.
        after_undo = getattr(obj, prop)
        undo_worked = fuzzy_eq(after_undo, orig)
        result["undo_tracked"] = undo_worked

        # 11. Check which side effects fired during undo and whether values restored.
        undo_fired = {(c, p) for c, p, dt in fired}
        obj_by_cls = {c: o for o, c, _ in listenables}
        for effect in side_effects:
            key = (effect["label"], effect["prop"])
            effect["undo_fires_listener"] = key in undo_fired
            if key in snapshot:
                try:
                    current = getattr(obj_by_cls[effect["label"]], effect["prop"])
                    effect["undo_restores_value"] = fuzzy_eq(current, snapshot[key])
                except Exception:
                    pass
        if side_effects:
            result["side_effects"] = side_effects

        # 12. Restore if undo didn't work.
        if not undo_worked:
            setattr(obj, prop, orig)
            yield

    except Exception as e:
        result["async_visibility"] = result.get("async_visibility", "error")
        result["undo_tracked"] = result.get("undo_tracked", "error")
        result["error"] = str(e)[:200]

    tag = result.get("async_visibility", "?")
    undo = result.get("undo_tracked", "?")
    effects = result.get("side_effects", [])
    effect_str = f", side_effects={[e['prop'] for e in effects]}" if effects else ""
    log(f"  [prop] {cls}.{prop}: async={tag}, undo={undo}{effect_str}")
    return result


def probe_method(
    song: Song, cls: str, method: str, args: list, check_fn: Callable[[], bool],
    cleanup_fn: Callable[[], None] | None, fired: list, probe_timing: dict, snapshot: dict,
    listenables: list[tuple[Any, str, list[str]]], log: Callable,
) -> Generator[None, None, dict[str, Any]]:
    """Probe a method for undo tracking, async visibility, and side effects.

    This is a generator — each yield crosses a tick boundary.

    Args:
        check_fn: () -> bool — returns True if the method's effect is present.
        cleanup_fn: () -> None — restores state if undo didn't work. Can be None.
        snapshot: {(cls, prop): value} — pre-probe snapshot of all listenable properties.
        listenables: [(obj, cls, props), ...] — for resolving side effect objects.
    """
    import time as _time

    result: dict[str, Any] = {}

    try:
        # 1. Clear fired listeners.
        fired.clear()
        probe_timing["target"] = None
        probe_timing["set_time"] = _time.monotonic()

        # 2. begin_undo_step, call method, end_undo_step.
        song.begin_undo_step()
        getattr(song, method)(*args)
        song.end_undo_step()

        # 3. Check effect immediately.
        is_immediate = check_fn()

        # 4. Yield to next tick.
        yield

        # 5. If not immediate, check again.
        if is_immediate:
            result["async_visibility"] = "immediate"
        else:
            if check_fn():
                result["async_visibility"] = "next_tick"
            else:
                result["async_visibility"] = "no_effect"

        # 6. Collect side effects.
        side_effects = [
            {"label": c, "prop": p, "listener_latency_ms": round(dt * 1000, 1)}
            for c, p, dt in fired
        ]

        # 7. Clear fired and undo.
        fired.clear()
        song.undo()

        # 8. Yield to next tick.
        yield

        # 9. Check effect gone → undo_tracked.
        result["undo_tracked"] = not check_fn()

        # 10. Check which side effects fired during undo and whether values restored.
        undo_fired = {(c, p) for c, p, dt in fired}
        obj_by_cls = {c: o for o, c, _ in listenables}
        for effect in side_effects:
            key = (effect["label"], effect["prop"])
            effect["undo_fires_listener"] = key in undo_fired
            if key in snapshot:
                try:
                    current = getattr(obj_by_cls[effect["label"]], effect["prop"])
                    effect["undo_restores_value"] = fuzzy_eq(current, snapshot[key])
                except Exception:
                    pass
        if side_effects:
            result["side_effects"] = side_effects

        # 11. If undo didn't work, run cleanup.
        if not result["undo_tracked"] and cleanup_fn:
            cleanup_fn()
            yield

    except Exception as e:
        result["async_visibility"] = result.get("async_visibility", "error")
        result["undo_tracked"] = result.get("undo_tracked", "error")
        result["error"] = str(e)[:200]

    effects = result.get("side_effects", [])
    effect_str = f", side_effects={[e['prop'] for e in effects]}" if effects else ""
    tag = result.get("async_visibility", "?")
    undo = result.get("undo_tracked", "?")
    log(f"  [meth] {cls}.{method}: async={tag}, undo={undo}{effect_str}")
    return result


def _ptr_set(items) -> set[int]:
    """Extract stable _live_ptr values from a list of Live API objects."""
    return {item._live_ptr for item in items}


def _find_new_index(items, before_ptrs: set[int]) -> int | None:
    """Find the index of the first item whose _live_ptr wasn't in before_ptrs."""
    for i, item in enumerate(items):
        if item._live_ptr not in before_ptrs:
            return i
    return None


def run(song: Song, log: Callable) -> Generator[None, None, None]:
    """Probe all settable Song and Song.View properties."""
    import time
    from datetime import datetime

    t0 = time.monotonic()
    log("[song_props] Starting property probes")
    results: dict[str, dict[str, dict[str, Any]]] = {
        "Song": {"properties": {}},
        "Song.View": {"properties": {}},
    }
    fired: list[tuple[str, str, float]] = []
    probe_timing: dict[str, Any] = {"target": None, "set_time": 0.0, "listener_time": None}

    # Set up listeners for side-effect detection
    view = song.view
    song_listenable = _discover_listenable(song)
    view_listenable = _discover_listenable(view)
    listenables = [(song, "Song", song_listenable), (view, "Song.View", view_listenable)]
    song_listeners = setup_listeners(song, "Song", song_listenable, fired, probe_timing, log)
    view_listeners = setup_listeners(view, "Song.View", view_listenable, fired, probe_timing, log)
    yield  # let listener setup settle

    # Song properties
    for prop, test_val in SONG_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        snap = snapshot_listenables(listenables)
        gen = probe_property(song, song, "Song", prop, test_val, fired, probe_timing, snap, listenables, log)
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Song"]["properties"][prop] = e.value

    # Song.View properties
    for prop, test_val in VIEW_SETTABLE_PROPS:
        snap = snapshot_listenables(listenables)
        gen = probe_property(song, view, "Song.View", prop, test_val, fired, probe_timing, snap, listenables, log)
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Song.View"]["properties"][prop] = e.value

    # ── Method probes ──────────────────────────────────────────────────────────
    log("[song_props] Starting method probes")

    if "Song" not in results:
        results["Song"] = {"properties": {}, "methods": {}}
    methods = results["Song"].setdefault("methods", {})

    def _run_method_probe(method, args, check_fn, cleanup_fn=None):
        snap = snapshot_listenables(listenables)
        gen = probe_method(song, "Song", method, args, check_fn, cleanup_fn, fired, probe_timing, snap,
                           listenables, log)
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # create_scene
    ids_before = _ptr_set(song.scenes)
    gen = _run_method_probe(
        "create_scene", [len(ids_before)],
        check_fn=lambda: bool(_ptr_set(song.scenes) - ids_before),
        cleanup_fn=lambda: song.delete_scene(_find_new_index(song.scenes, ids_before)),
    )
    r = yield from gen
    if r: methods["create_scene"] = r

    # create_midi_track
    ids_before = _ptr_set(song.tracks)
    gen = _run_method_probe(
        "create_midi_track", [len(ids_before)],
        check_fn=lambda: bool(_ptr_set(song.tracks) - ids_before),
        cleanup_fn=lambda: song.delete_track(_find_new_index(song.tracks, ids_before)),
    )
    r = yield from gen
    if r: methods["create_midi_track"] = r

    # create_audio_track
    ids_before = _ptr_set(song.tracks)
    gen = _run_method_probe(
        "create_audio_track", [len(ids_before)],
        check_fn=lambda: bool(_ptr_set(song.tracks) - ids_before),
        cleanup_fn=lambda: song.delete_track(_find_new_index(song.tracks, ids_before)),
    )
    r = yield from gen
    if r: methods["create_audio_track"] = r

    # create_return_track
    ids_before = _ptr_set(song.return_tracks)
    gen = _run_method_probe(
        "create_return_track", [],
        check_fn=lambda: bool(_ptr_set(song.return_tracks) - ids_before),
        cleanup_fn=lambda: song.delete_return_track(_find_new_index(song.return_tracks, ids_before)),
    )
    r = yield from gen
    if r: methods["create_return_track"] = r

    # duplicate_scene
    ids_before = _ptr_set(song.scenes)
    gen = _run_method_probe(
        "duplicate_scene", [0],
        check_fn=lambda: bool(_ptr_set(song.scenes) - ids_before),
        cleanup_fn=lambda: song.delete_scene(_find_new_index(song.scenes, ids_before)),
    )
    r = yield from gen
    if r: methods["duplicate_scene"] = r

    # duplicate_track
    ids_before = _ptr_set(song.tracks)
    gen = _run_method_probe(
        "duplicate_track", [0],
        check_fn=lambda: bool(_ptr_set(song.tracks) - ids_before),
        cleanup_fn=lambda: song.delete_track(_find_new_index(song.tracks, ids_before)),
    )
    r = yield from gen
    if r: methods["duplicate_track"] = r

    # set_or_delete_cue
    ids_before = _ptr_set(song.cue_points)
    gen = _run_method_probe(
        "set_or_delete_cue", [],
        check_fn=lambda: _ptr_set(song.cue_points) != ids_before,
    )
    r = yield from gen
    if r: methods["set_or_delete_cue"] = r

    # capture_and_insert_scene
    ids_before = _ptr_set(song.scenes)
    gen = _run_method_probe(
        "capture_and_insert_scene", [0],
        check_fn=lambda: bool(_ptr_set(song.scenes) - ids_before),
        cleanup_fn=lambda: song.delete_scene(_find_new_index(song.scenes, ids_before)),
    )
    r = yield from gen
    if r: methods["capture_and_insert_scene"] = r

    # Tear down listeners
    teardown_listeners(song, song_listeners)
    teardown_listeners(view, view_listeners)

    # Write results
    import Live

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

    elapsed = round(time.monotonic() - t0, 1)
    output = {
        "version": version,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "elapsed_seconds": elapsed,
        "classes": existing_classes,
    }

    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)

    total_props = sum(len(d.get("properties", {})) for d in results.values())
    total_methods = sum(len(d.get("methods", {})) for d in results.values())
    log(f"[song_props] Done — {total_props} properties, {total_methods} methods probed in {elapsed}s, wrote {outpath}")
