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

from Live.Base import IntVector, Vector
from Live.LomObject import LomObject

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


# ── Listenable properties (for side-effect detection) ─────────────────────────

# Properties excluded from listener subscription — fire too frequently to be useful as listeners.
LISTENER_EXCLUDE: set[str] = {"current_song_time"}  # fires every audio tick (~80/s)

# Non-listenable properties to include in snapshots, keyed by class name.
# When probing other modules, add entries here for cross-module properties to track.
SNAPSHOT_EXTRA: dict[str, set[str]] = {
    "Song": {"name"},
    "Song.View": {"highlighted_clip_slot"},
}


def _discover_listenable(obj: object) -> list[str]:
    """Properties safe to subscribe listeners to (excludes LISTENER_EXCLUDE)."""
    return sorted(
        name[4:-9] for name in dir(obj)
        if name.startswith("add_") and name.endswith("_listener")
        and name[4:-9] not in LISTENER_EXCLUDE
    )
    
    
def _discover_snapshot_props(listenable: list[str], cls: str) -> list[str]:
    """Properties to snapshot and restore between probes.

    Includes all listenable properties (even LISTENER_EXCLUDE ones) plus SNAPSHOT_EXTRA
    for non-listenable properties that can drift during probes.
    """
    props = set(SNAPSHOT_EXTRA.get(cls, set())) | LISTENER_EXCLUDE
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


def snapshot_properties(
    objects: list[tuple[Any, str, list[str]]],
) -> tuple[dict[tuple[str, str], Any], dict[tuple[str, str], Any]]:
    """Read current values of properties for pre/post-probe comparison and restoration.

    Args:
        objects: [(obj, cls_name, prop_list), ...] — e.g. [(song, "Song", song_snapshot_props), ...]

    Returns:
        (raw, serialized) — raw holds live objects for comparison/restore,
        serialized holds _json_safe values captured eagerly for output.
    """
    raw: dict[tuple[str, str], Any] = {}
    serialized: dict[tuple[str, str], Any] = {}
    for obj, cls, props in objects:
        for prop in props:
            try:
                val = getattr(obj, prop)
                raw[(cls, prop)] = val
                serialized[(cls, prop)] = _json_safe(val)
            except Exception:
                pass
    return raw, serialized


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


def _check_unlistened_side_effects(
    snapshot: dict, snap_json: dict, obj_by_cls: dict[str, Any],
    already_seen: set[tuple[str, str]], skip: tuple[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Check SNAPSHOT_EXTRA properties for changes not caught by listeners.

    Returns side effect dicts for any that changed, excluding already_seen keys.
    """
    effects = []
    for cls_name, extras in SNAPSHOT_EXTRA.items():
        obj = obj_by_cls.get(cls_name)
        if obj is None:
            continue
        for prop in extras:
            key = (cls_name, prop)
            if key in already_seen or key == skip or key not in snapshot:
                continue
            try:
                current = getattr(obj, prop)
                if not fuzzy_eq(current, snapshot[key]):
                    effects.append({
                        "label": cls_name,
                        "prop": prop,
                        "from": snap_json[key],
                        "to": _json_safe(current),
                        "_raw_after": current,
                        "unlistened": True,
                    })
            except Exception:
                pass
    return effects


def restore_side_effects(
    snapshot: dict[tuple[str, str], Any], obj_by_cls: dict[str, Any], log: Callable,
    skip: tuple[str, str] | None = None,
) -> bool:
    """Restore any properties that drifted from their pre-probe snapshot values.

    Stops playback first so current_song_time doesn't keep advancing between ticks.

    Args:
        skip: optional (cls, prop) to skip — the main probed property, handled separately.

    Returns:
        True if any property was restored.
    """
    changed = False

    # Stop playback first — otherwise current_song_time keeps advancing between ticks.
    is_playing_key = ("Song", "is_playing")
    if is_playing_key in snapshot and is_playing_key != skip:
        playing_obj = obj_by_cls.get("Song")
        if playing_obj is not None:
            try:
                if getattr(playing_obj, "is_playing") and not snapshot[is_playing_key]:
                    setattr(playing_obj, "is_playing", False)
                    log("    [restore] Song.is_playing: True → False")
                    changed = True
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
                changed = True
        except Exception:
            pass

    return changed


def probe_property(
    song: Song, obj: Any, cls: str, prop: str, test_value: Any, fired: list, probe_timing: dict,
    snapshot: dict, snap_json: dict, snapshot_targets: list[tuple[Any, str, list[str]]], log: Callable,
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
        seen_keys: set[tuple[str, str]] = set()
        for c, p, dt in fired:
            if c == cls and p == prop:
                continue
            effect: dict[str, Any] = {"label": c, "prop": p, "listener_latency_ms": round(dt * 1000, 1)}
            key = (c, p)
            seen_keys.add(key)
            if key in snapshot:
                try:
                    after = getattr(obj_by_cls[c], p)
                    effect["from"] = snap_json[key]
                    effect["to"] = _json_safe(after)
                    effect["_raw_after"] = after  # stashed for undo comparison
                except Exception:
                    pass
            side_effects.append(effect)
        # Check SNAPSHOT_EXTRA for unlistened side effects.
        side_effects.extend(_check_unlistened_side_effects(
            snapshot, snap_json, obj_by_cls, seen_keys, skip=(cls, prop),
        ))

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
                    if fuzzy_eq(current, snapshot[key]):
                        effect["undo_result"] = "restored"
                    elif "_raw_after" in effect and fuzzy_eq(current, effect["_raw_after"]):
                        effect["undo_result"] = "unchanged"
                    else:
                        effect["undo_result"] = "changed"
                        effect["undo_value"] = _json_safe(current)
                except Exception:
                    pass
            effect.pop("_raw_after", None)
        if side_effects:
            result["side_effects"] = side_effects

        # 12. Restore any side effects not cleaned up by undo.
        #     Loop because restoring one property (e.g. is_playing) can cause
        #     next_tick side effects on others (e.g. detail_clip).
        for _ in range(3):
            if not restore_side_effects(snapshot, obj_by_cls, log, skip=(cls, prop)):
                break
            yield  # let restorations settle, then check again

        # 14. Restore main property if undo didn't work.
        if not undo_worked:
            try:
                setattr(obj, prop, orig)
            except Exception:
                pass  # some properties reject None or stale objects
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
    cleanup_fn: Callable[[], None] | None, fired: list, probe_timing: dict, snapshot: dict, snap_json: dict,
    snapshot_targets: list[tuple[Any, str, list[str]]], log: Callable,
    *, obj: Any = None,
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
        target = obj if obj is not None else song
        song.begin_undo_step()
        getattr(target, method)(*args)
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
        seen_keys: set[tuple[str, str]] = set()
        for c, p, dt in fired:
            effect: dict[str, Any] = {"label": c, "prop": p, "listener_latency_ms": round(dt * 1000, 1)}
            key = (c, p)
            seen_keys.add(key)
            if key in snapshot:
                try:
                    after = getattr(obj_by_cls[c], p)
                    effect["from"] = snap_json[key]
                    effect["to"] = _json_safe(after)
                    effect["_raw_after"] = after
                except Exception:
                    pass
            side_effects.append(effect)
        # Check SNAPSHOT_EXTRA for unlistened side effects.
        side_effects.extend(_check_unlistened_side_effects(
            snapshot, snap_json, obj_by_cls, seen_keys,
        ))

        # 7. Clear fired and undo.
        fired.clear()
        song.undo()

        # 8. Yield to next tick.
        yield

        # 9. Check effect gone → undo_tracked.
        if result.get("async_visibility") == "no_effect":
            result["undo_tracked"] = "n/a"
        else:
            result["undo_tracked"] = not check_fn()

        # 10. Check which side effects fired during undo and whether values restored.
        undo_fired = {(c, p) for c, p, _ in fired}
        for effect in side_effects:
            key = (effect["label"], effect["prop"])
            effect["undo_fires_listener"] = key in undo_fired
            if key in snapshot:
                try:
                    current = getattr(obj_by_cls[effect["label"]], effect["prop"])
                    if fuzzy_eq(current, snapshot[key]):
                        effect["undo_result"] = "restored"
                    elif "_raw_after" in effect and fuzzy_eq(current, effect["_raw_after"]):
                        effect["undo_result"] = "unchanged"
                    else:
                        effect["undo_result"] = "changed"
                        effect["undo_value"] = _json_safe(current)
                except Exception:
                    pass
            effect.pop("_raw_after", None)
        if side_effects:
            result["side_effects"] = side_effects

        # 11. Restore any side effects not cleaned up by undo.
        #     Loop because restoring one property can cause next_tick side effects on others.
        for _ in range(3):
            if not restore_side_effects(snapshot, obj_by_cls, log):
                break
            yield  # let restorations settle, then check again

        # 13. If undo didn't work, run cleanup.
        if result["undo_tracked"] is not True and cleanup_fn:
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
        (song, "Song", _discover_snapshot_props(song_listenable, "Song")),
        (view, "Song.View", _discover_snapshot_props(view_listenable, "Song.View")),
    ]
    song_listeners = setup_listeners(song, "Song", song_listenable, fired, probe_timing, log)
    view_listeners = setup_listeners(view, "Song.View", view_listenable, fired, probe_timing, log)
    yield  # let listener setup settle

    # Switch to session view and set a known starting state.
    # The demo set opens in arrangement view with a stale detail_clip reference;
    # switching to session and setting highlighted_clip_slot establishes a stable
    # session context so all probes start from consistent state.
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
        gen = probe_property(song, song, "Song", prop, test_val, fired, probe_timing, snap, snap_json, snapshot_targets, log)
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
        gen = probe_property(song, view, "Song.View", prop, test_val, fired, probe_timing, snap, snap_json, snapshot_targets, log)
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
        gen = probe_property(song, obj, cls, prop, test_val, fired, probe_timing, snap, snap_json, snapshot_targets, log)
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

    # Song.View.detail_clip — set to a clip; ensure we pick one that differs from current
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
    log("[song_props] Starting method probes")

    if "Song" not in results:
        results["Song"] = {"properties": {}, "methods": {}}
    methods = results["Song"].setdefault("methods", {})

    def _run_method_probe(method, args, check_fn, cleanup_fn=None):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_method(song, "Song", method, args, check_fn, cleanup_fn, fired, probe_timing, snap, snap_json,
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

    # delete_scene (middle index — undo restores it)
    num_scenes = len(song.scenes)
    ids_before = _ptr_set(song.scenes)
    gen = _run_method_probe(
        "delete_scene", [num_scenes // 2],
        check_fn=lambda: len(song.scenes) < num_scenes,
    )
    r = yield from gen
    if r: methods["delete_scene"] = r

    # delete_track (middle index — undo restores it)
    num_tracks = len(song.tracks)
    ids_before = _ptr_set(song.tracks)
    gen = _run_method_probe(
        "delete_track", [num_tracks // 2],
        check_fn=lambda: len(song.tracks) < num_tracks,
    )
    r = yield from gen
    if r: methods["delete_track"] = r

    # delete_return_track (middle index — undo restores it)
    num_rt = len(song.return_tracks)
    ids_before = _ptr_set(song.return_tracks)
    gen = _run_method_probe(
        "delete_return_track", [num_rt // 2],
        check_fn=lambda: len(song.return_tracks) < num_rt,
    )
    r = yield from gen
    if r: methods["delete_return_track"] = r

    # ── Transport / position method probes ───────────────────────────────────
    log("[song_props] Starting transport/position method probes")

    # start_playing
    gen = _run_method_probe(
        "start_playing", [],
        check_fn=lambda: song.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
    )
    r = yield from gen
    if r: methods["start_playing"] = r

    # stop_playing — start first so we can test stopping
    song.start_playing()
    yield
    gen = _run_method_probe(
        "stop_playing", [],
        check_fn=lambda: not song.is_playing,
    )
    r = yield from gen
    if r: methods["stop_playing"] = r
    # Ensure stopped
    if song.is_playing:
        song.stop_playing()
        yield

    # continue_playing
    gen = _run_method_probe(
        "continue_playing", [],
        check_fn=lambda: song.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
    )
    r = yield from gen
    if r: methods["continue_playing"] = r

    # play_selection
    gen = _run_method_probe(
        "play_selection", [],
        check_fn=lambda: song.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
    )
    r = yield from gen
    if r: methods["play_selection"] = r

    # stop_all_clips — fire track 0 slot 0 clip, then probe stopping it
    clip_slot = song.tracks[0].clip_slots[0]
    orig_quant = song.clip_trigger_quantization
    song.clip_trigger_quantization = 0  # type: ignore[assignment]  # Quantization enum accepts int at runtime
    yield
    clip_slot.fire()
    yield
    # Restore quantization before probe so snapshot captures original value
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
    # Firing the clip sets back_to_arranger (next_tick, so restore can't catch it)
    song.stop_all_clips(False)
    yield
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield

    # jump_by — move song position forward
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

    # scrub_by — similar to jump_by
    gen = _run_method_probe(
        "scrub_by", [4.0],
        check_fn=lambda: song.current_song_time >= 4.0,
    )
    r = yield from gen
    if r: methods["scrub_by"] = r
    song.current_song_time = 0.0
    yield

    # jump_to_prev_cue — position past all cue points so we can jump back
    song.current_song_time = song.song_length
    yield
    gen = _run_method_probe(
        "jump_to_prev_cue", [],
        check_fn=lambda: song.current_song_time < song.song_length,
    )
    r = yield from gen
    if r: methods["jump_to_prev_cue"] = r

    # jump_to_next_cue — position at start so we can jump forward
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
    log("[song_props] Starting data store method probes")

    # set_data — store a test value, check it persists
    test_key = "__liverelay_probe_test"
    gen = _run_method_probe(
        "set_data", [test_key, "probe_value"],
        check_fn=lambda: song.get_data(test_key, None) == "probe_value",
        cleanup_fn=lambda: song.set_data(test_key, None),
    )
    r = yield from gen
    if r: methods["set_data"] = r
    # Clean up test key
    song.set_data(test_key, None)
    yield


    # ── State-changing methods with preconditions ───────────────────────────
    log("[song_props] Starting precondition method probes")

    # move_device — move Auto Filter from track 1 to end of track 0
    track0 = song.tracks[0]
    track1 = song.tracks[1]
    num_devs_t0 = len(track0.devices)
    # Track 1 device 1 is Auto Filter (a simple audio effect, movable between tracks)
    device_to_move = track1.devices[1]
    gen = _run_method_probe(
        "move_device", [device_to_move, track0, num_devs_t0],
        check_fn=lambda: len(track0.devices) > num_devs_t0,
    )
    r = yield from gen
    if r: methods["move_device"] = r

    # trigger_session_record — starts session recording
    gen = _run_method_probe(
        "trigger_session_record", [],
        check_fn=lambda: song.session_record,
        cleanup_fn=lambda: song.stop_playing(),
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
    log("[song_props] Starting Song.View method probes")

    view_methods = results["Song.View"].setdefault("methods", {})

    # select_device — use track 1 device 0 (Strum-o-Matic)
    target_device = song.tracks[1].devices[0]
    snap, snap_json = snapshot_properties(snapshot_targets)
    gen = probe_method(
        song, "Song.View", "select_device", [target_device, True],
        check_fn=lambda: (song.appointed_device is not None
                          and song.appointed_device._live_ptr == target_device._live_ptr),
        cleanup_fn=None, fired=fired, probe_timing=probe_timing,
        snapshot=snap, snap_json=snap_json, snapshot_targets=snapshot_targets, log=log,
        obj=view,
    )
    try:
        while True:
            next(gen)
            yield
    except StopIteration as e:
        if e.value is not None:
            view_methods["select_device"] = e.value

    # ── CuePoint probes ─────────────────────────────────────────────────────
    log("[song_props] Starting CuePoint probes")

    results["CuePoint"] = {"properties": {}, "methods": {}}

    # CuePoint.name (settable, listenable) — cue 0 is "Intro" at time 0.0
    cue = song.cue_points[0]
    snap, snap_json = snapshot_properties(snapshot_targets)
    gen = probe_property(
        song, cue, "CuePoint", "name", "__probe_test__", fired, probe_timing,
        snap, snap_json, snapshot_targets, log,
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
        snapshot=snap, snap_json=snap_json, snapshot_targets=snapshot_targets, log=log,
        obj=cue1,
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

    # Merge behavioral notes into results (probed members get inline notes,
    # unprobed members go into a top-level "notes" dict for downstream enrichment)
    orphan_notes: dict[str, str] = {}
    for key, note in NOTES.items():
        # Keys like "Song.View.select_device" — class name may contain dots
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
    log(f"[song_props] Done — {total_props} properties, {total_methods} methods probed in {elapsed}s, wrote {outpath}")
