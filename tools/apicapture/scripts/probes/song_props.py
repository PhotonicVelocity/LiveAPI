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

from Live.Base import IntVector, Vector
from Live.LomObject import LomObject
from Live.Device import Device

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


# ── Listenable properties (for side-effect detection) ─────────────────────────

# Properties excluded from listener subscription — fire too frequently to be useful as listeners.
LISTENER_EXCLUDE: set[str] = {"current_song_time"}  # fires every audio tick (~80/s)

# Non-listenable properties to include in snapshots for restoration between probes.
SNAPSHOT_EXTRA: set[str] = {"name"}


def _discover_listenable(obj: object) -> list[str]:
    """Properties safe to subscribe listeners to (excludes LISTENER_EXCLUDE)."""
    return sorted(
        name[4:-9] for name in dir(obj)
        if name.startswith("add_") and name.endswith("_listener")
        and name[4:-9] not in LISTENER_EXCLUDE
    )
    
    
def _discover_snapshot_props(listenable: list[str]) -> list[str]:
    """Properties to snapshot and restore between probes.

    Includes all listenable properties (even LISTENER_EXCLUDE ones) plus SNAPSHOT_EXTRA
    for non-listenable properties that can drift during probes.
    """
    props = set(SNAPSHOT_EXTRA) | LISTENER_EXCLUDE
    props.update(listenable)
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


def snapshot_properties(objects: list[tuple[Any, str, list[str]]]) -> dict[tuple[str, str], Any]:
    """Read current values of properties for pre/post-probe comparison and restoration.

    Args:
        objects: [(obj, cls_name, prop_list), ...] — e.g. [(song, "Song", song_snapshot_props), ...]

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
    """Compare with tolerance for floats, and by _live_ptr for Live API objects."""
    if isinstance(a, float) and isinstance(b, float):
        return abs(a - b) < 0.01
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) < 0.01
    # Single Live API objects — compare by ptr
    if isinstance(a, LomObject) and isinstance(b, LomObject):
        return a._live_ptr == b._live_ptr
    # Vectors — compare element-wise (by ptr for LomObjects, by value for primitives)
    if isinstance(a, (Vector, IntVector)) and isinstance(b, (Vector, IntVector)):
        return _vector_key(a) == _vector_key(b)
    return a == b


def _vector_key(vec: Vector | IntVector) -> list:  # type: ignore[type-arg]
    """Convert a Vector to a comparable list — ptrs for LomObjects, values for primitives."""
    return [item._live_ptr if isinstance(item, LomObject) else item for item in vec]


def _json_safe(val: Any) -> Any:
    """Return val as-is if JSON-serializable, otherwise use _live_ptr or repr()."""
    if val is None or isinstance(val, (bool, int, float, str)):
        return val
    if isinstance(val, LomObject):
        return f"ptr:{val._live_ptr}"
    if isinstance(val, (Vector, IntVector)):
        return [f"ptr:{item._live_ptr}" if isinstance(item, LomObject) else item for item in val]
    return repr(val)


def restore_side_effects(
    snapshot: dict[tuple[str, str], Any], obj_by_cls: dict[str, Any], log: Callable,
    skip: tuple[str, str] | None = None,
) -> None:
    """Restore any properties that drifted from their pre-probe snapshot values.

    Stops playback first so current_song_time doesn't keep advancing between ticks.

    Args:
        skip: optional (cls, prop) to skip — the main probed property, handled separately.
    """
    # Stop playback first — otherwise current_song_time keeps advancing between ticks.
    is_playing_key = ("Song", "is_playing")
    if is_playing_key in snapshot and is_playing_key != skip:
        playing_obj = obj_by_cls.get("Song")
        if playing_obj is not None:
            try:
                if getattr(playing_obj, "is_playing") and not snapshot[is_playing_key]:
                    setattr(playing_obj, "is_playing", False)
                    log("    [restore] Song.is_playing: True → False")
            except Exception:
                pass

    for (snap_cls, snap_prop), snap_val in snapshot.items():
        if (snap_cls, snap_prop) == is_playing_key:
            continue  # already handled above
        if skip and (snap_cls, snap_prop) == skip:
            continue
        snap_obj = obj_by_cls.get(snap_cls)
        if snap_obj is None:
            continue
        try:
            current = getattr(snap_obj, snap_prop)
            if not fuzzy_eq(current, snap_val):
                setattr(snap_obj, snap_prop, snap_val)
                log(f"    [restore] {snap_cls}.{snap_prop}: {current!r} → {snap_val!r}")
        except Exception:
            pass


def probe_property(
    song: Song, obj: Song | Song.View, cls: str, prop: str, test_value: Any, fired: list, probe_timing: dict,
    snapshot: dict, snapshot_targets: list[tuple[Any, str, list[str]]], log: Callable,
) -> Generator[None, None, dict[str, Any]]:
    """Probe a single property for undo tracking, async visibility, and side effects.

    This is a generator — each yield crosses a tick boundary.

    Steps:
        1.  Read original value; skip if test_value matches.
        2.  Clear fired listeners, set timing target.
        3.  begin_undo_step → set property → end_undo_step.
        4.  Read back immediately → classify "immediate" if value changed.
        5.  Yield (tick boundary).
        6.  Read back again → classify "next_tick" or "no_change".
        7.  Collect side effects and listener timing from fired list.
        8.  Clear fired list, call undo().
        9.  Yield (tick boundary).
        10. Read back → determine undo_tracked.
        11. Check which side-effect listeners fired during undo and whether values restored.
        12. Restore any side effects not cleaned up by undo (setattr from snapshot).
        13. Yield (tick boundary — let restorations settle).
        14. Restore main property if undo didn't work.
        15. Yield (tick boundary).

    Args:
        snapshot: {(cls, prop): value} — pre-probe snapshot of all snapshotted properties,
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

        result["from"] = _json_safe(orig)
        result["to"] = _json_safe(test_value)

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
        obj_by_cls = {c: o for o, c, _ in snapshot_targets}
        side_effects = []
        for c, p, dt in fired:
            if c == cls and p == prop:
                continue
            effect: dict[str, Any] = {"label": c, "prop": p, "listener_latency_ms": round(dt * 1000, 1)}
            key = (c, p)
            if key in snapshot:
                try:
                    after = getattr(obj_by_cls[c], p)
                    effect["from"] = _json_safe(snapshot[key])
                    effect["to"] = _json_safe(after)
                except Exception:
                    pass
            side_effects.append(effect)

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
        undo_fired = {(c, p) for c, p, _ in fired}
        result["undo_fires_listener"] = (cls, prop) in undo_fired
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

        # 12. Restore any side effects not cleaned up by undo.
        restore_side_effects(snapshot, obj_by_cls, log, skip=(cls, prop))

        # 13. Yield to let restorations settle.
        yield

        # 14. Restore main property if undo didn't work.
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
    snapshot_targets: list[tuple[Any, str, list[str]]], log: Callable,
) -> Generator[None, None, dict[str, Any]]:
    """Probe a method for undo tracking, async visibility, and side effects.

    This is a generator — each yield crosses a tick boundary.

    Args:
        check_fn: () -> bool — returns True if the method's effect is present.
        cleanup_fn: () -> None — restores state if undo didn't work. Can be None.
        snapshot: {(cls, prop): value} — pre-probe snapshot of all snapshotted properties.
        snapshot_targets: [(obj, cls, props), ...] — for resolving side effect objects.
    """
    import time as _time

    result: dict[str, Any] = {}
    if args:
        result["args"] = [_json_safe(a) for a in args]

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
        obj_by_cls = {c: o for o, c, _ in snapshot_targets}
        side_effects = []
        for c, p, dt in fired:
            effect: dict[str, Any] = {"label": c, "prop": p, "listener_latency_ms": round(dt * 1000, 1)}
            key = (c, p)
            if key in snapshot:
                try:
                    after = getattr(obj_by_cls[c], p)
                    effect["from"] = _json_safe(snapshot[key])
                    effect["to"] = _json_safe(after)
                except Exception:
                    pass
            side_effects.append(effect)

        # 7. Clear fired and undo.
        fired.clear()
        song.undo()

        # 8. Yield to next tick.
        yield

        # 9. Check effect gone → undo_tracked.
        result["undo_tracked"] = not check_fn()

        # 10. Check which side effects fired during undo and whether values restored.
        undo_fired = {(c, p) for c, p, _ in fired}
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

        # 11. Restore any side effects not cleaned up by undo.
        restore_side_effects(snapshot, obj_by_cls, log)

        # 12. Yield to let restorations settle.
        yield

        # 13. If undo didn't work, run cleanup.
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

    # Set up listeners and snapshot targets
    view = song.view
    song_listenable = _discover_listenable(song)
    view_listenable = _discover_listenable(view)
    snapshot_targets = [
        (song, "Song", _discover_snapshot_props(song_listenable)),
        (view, "Song.View", _discover_snapshot_props(view_listenable)),
    ]
    song_listeners = setup_listeners(song, "Song", song_listenable, fired, probe_timing, log)
    view_listeners = setup_listeners(view, "Song.View", view_listenable, fired, probe_timing, log)
    yield  # let listener setup settle

    # Song properties
    for prop, test_val in SONG_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        snap = snapshot_properties(snapshot_targets)
        gen = probe_property(song, song, "Song", prop, test_val, fired, probe_timing, snap, snapshot_targets, log)
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Song"]["properties"][prop] = e.value

    # Song.View properties
    for prop, test_val in VIEW_SETTABLE_PROPS:
        snap = snapshot_properties(snapshot_targets)
        gen = probe_property(song, view, "Song.View", prop, test_val, fired, probe_timing, snap, snapshot_targets, log)
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Song.View"]["properties"][prop] = e.value

    # ── Object-reference property probes ─────────────────────────────────────
    # These can't go in the static lists — test values are runtime objects.

    def _run_obj_prop_probe(obj, cls, prop, test_val):
        snap = snapshot_properties(snapshot_targets)
        gen = probe_property(song, obj, cls, prop, test_val, fired, probe_timing, snap, snapshot_targets, log)
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # Song.View.selected_scene — pick a different scene (middle index)
    scenes = song.scenes
    if len(scenes) >= 2:
        current_scene = view.selected_scene
        mid = len(scenes) // 2
        target_scene = scenes[mid] if scenes[mid]._live_ptr != current_scene._live_ptr else scenes[mid - 1]
        r = yield from _run_obj_prop_probe(view, "Song.View", "selected_scene", target_scene)
        if r:
            results["Song.View"]["properties"]["selected_scene"] = r
    else:
        log("  [skip] Song.View.selected_scene — need ≥2 scenes")

    # Song.View.selected_track — pick a different track (middle index)
    tracks = song.tracks
    if len(tracks) >= 2:
        current_track = view.selected_track
        mid = len(tracks) // 2
        target_track = tracks[mid] if tracks[mid]._live_ptr != current_track._live_ptr else tracks[mid - 1]
        r = yield from _run_obj_prop_probe(view, "Song.View", "selected_track", target_track)
        if r:
            results["Song.View"]["properties"]["selected_track"] = r
    else:
        log("  [skip] Song.View.selected_track — need ≥2 tracks")

    # Song.appointed_device — use devices from return tracks (present in minimal sets)
    return_tracks = song.return_tracks
    all_devices: list[Device] = []
    for rt in return_tracks:
        all_devices.extend(rt.devices)
    if len(all_devices) >= 2:
        current_device = song.appointed_device
        if current_device is not None:
            target_device = all_devices[1] if all_devices[0]._live_ptr == current_device._live_ptr else all_devices[0]
        else:
            target_device = all_devices[0]
        r = yield from _run_obj_prop_probe(song, "Song", "appointed_device", target_device)
        if r:
            results["Song"]["properties"]["appointed_device"] = r
    else:
        log(f"  [skip] Song.appointed_device — need ≥2 devices on return tracks (found {len(all_devices)})")

    # ── Method probes ──────────────────────────────────────────────────────────
    log("[song_props] Starting method probes")

    if "Song" not in results:
        results["Song"] = {"properties": {}, "methods": {}}
    methods = results["Song"].setdefault("methods", {})

    def _run_method_probe(method, args, check_fn, cleanup_fn=None):
        snap = snapshot_properties(snapshot_targets)
        gen = probe_method(song, "Song", method, args, check_fn, cleanup_fn, fired, probe_timing, snap,
                           snapshot_targets, log)
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # create_scene (middle index to avoid end-of-list selection edge case)
    ids_before = _ptr_set(song.scenes)
    gen = _run_method_probe(
        "create_scene", [len(song.scenes) // 2],
        check_fn=lambda: bool(_ptr_set(song.scenes) - ids_before),
        cleanup_fn=lambda: song.delete_scene(_find_new_index(song.scenes, ids_before)),
    )
    r = yield from gen
    if r: methods["create_scene"] = r

    # create_midi_track (middle index to avoid end-of-list selection edge case)
    ids_before = _ptr_set(song.tracks)
    gen = _run_method_probe(
        "create_midi_track", [len(song.tracks) // 2],
        check_fn=lambda: bool(_ptr_set(song.tracks) - ids_before),
        cleanup_fn=lambda: song.delete_track(_find_new_index(song.tracks, ids_before)),
    )
    r = yield from gen
    if r: methods["create_midi_track"] = r

    # create_audio_track (middle index to avoid end-of-list selection edge case)
    ids_before = _ptr_set(song.tracks)
    gen = _run_method_probe(
        "create_audio_track", [len(song.tracks) // 2],
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

    # duplicate_scene (middle index to avoid edge cases)
    ids_before = _ptr_set(song.scenes)
    gen = _run_method_probe(
        "duplicate_scene", [len(song.scenes) // 2],
        check_fn=lambda: bool(_ptr_set(song.scenes) - ids_before),
        cleanup_fn=lambda: song.delete_scene(_find_new_index(song.scenes, ids_before)),
    )
    r = yield from gen
    if r: methods["duplicate_scene"] = r

    # duplicate_track (middle index to avoid edge cases)
    ids_before = _ptr_set(song.tracks)
    gen = _run_method_probe(
        "duplicate_track", [len(song.tracks) // 2],
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

    # capture_and_insert_scene (middle index to avoid edge cases)
    ids_before = _ptr_set(song.scenes)
    gen = _run_method_probe(
        "capture_and_insert_scene", [len(song.scenes) // 2],
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
