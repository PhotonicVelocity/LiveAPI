"""Shared probe infrastructure for targeted probing scripts.

Provides the core functions for probing properties and methods: snapshot capture,
comparison, side effect detection, undo tracking, and state restoration.
"""

from __future__ import annotations

import time as _time_module
from typing import TYPE_CHECKING, Any

from Live.Base import IntVector, Vector
from Live.LomObject import LomObject

if TYPE_CHECKING:
    from collections.abc import Callable, Generator

    from Live.Song import Song


# ── Comparison and serialization ──────────────────────────────────────────────


def fuzzy_eq(a: Any, b: Any) -> bool:
    """Compare with tolerance for floats, and by _live_ptr for Live API objects."""
    if isinstance(a, float) and isinstance(b, float):
        return abs(a - b) < 0.01
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) < 0.01
    if isinstance(a, LomObject) and isinstance(b, LomObject):
        return a._live_ptr == b._live_ptr
    if isinstance(a, (Vector, IntVector)) and isinstance(b, (Vector, IntVector)):
        return _seq_key(a) == _seq_key(b)
    # Generic iterable comparison (RoutingTypeVector, StringVector, etc.)
    # Only if both have __len__ and __iter__ (duck-typed containers).
    if hasattr(a, "__len__") and hasattr(b, "__len__") and not isinstance(a, (str, bytes)):
        try:
            return _seq_key(a) == _seq_key(b)
        except (TypeError, RuntimeError):
            pass
    return a == b


def _seq_key(seq: Any) -> list:
    """Convert a sequence to a comparable list — ptrs for LomObjects, values for primitives."""
    return [item._live_ptr if isinstance(item, LomObject) else item for item in seq]


def json_safe(val: Any) -> Any:
    """Return val as-is if JSON-serializable, otherwise use _live_ptr or repr().

    Handles Live API objects by type:
    - LomObject → "ptr:<id>"
    - Vector/IntVector → list of ptr or primitive values
    - Objects with display_name (RoutingType, RoutingChannel) → display_name string
    - Iterables of JSON-safe items (StringVector, etc.) → list
    """
    if val is None or isinstance(val, (bool, int, float, str)):
        return val
    if isinstance(val, LomObject):
        return f"ptr:{val._live_ptr}"
    if isinstance(val, (Vector, IntVector)):
        return [f"ptr:{item._live_ptr}" if isinstance(item, LomObject) else item for item in val]
    # Objects with display_name (RoutingType, RoutingChannel, etc.)
    display_name = getattr(val, "display_name", None)
    if display_name is not None:
        return display_name
    # Iterable containers (StringVector, RoutingTypeVector, RoutingChannelVector, etc.)
    try:
        items = list(val)
        if items and all(isinstance(item, (bool, int, float, str)) for item in items):
            return items
        return [json_safe(item) for item in items]
    except (TypeError, RuntimeError):
        pass
    return repr(val)


# ── Discovery ────────────────────────────────────────────────────────────────


def discover_listenable(obj: object, exclude: set[str]) -> list[str]:
    """Discover properties safe to subscribe listeners to (excludes the given set)."""
    return sorted(
        name[4:-9] for name in dir(obj)
        if name.startswith("add_") and name.endswith("_listener")
        and name[4:-9] not in exclude
    )


def discover_snapshot_props(
    listenable: list[str], cls: str, exclude: set[str], extras: dict[str, set[str]],
) -> list[str]:
    """Build the list of properties to snapshot and restore between probes.

    Includes all listenable properties (even excluded ones) plus per-class extras.
    """
    props = set(extras.get(cls, set())) | exclude
    props.update(listenable)
    return sorted(props)


# ── Listener infrastructure ──────────────────────────────────────────────────


def setup_listeners(
    obj: Any, cls: str, props: list[str], fired: list, probe_timing: dict, log: Callable,
) -> list[tuple[str, Any]]:
    """Add listeners for all listenable properties. Returns [(prop, callback)] for teardown.

    probe_timing is a shared dict with:
      - "target": (cls, prop) currently being probed, or None
      - "set_time": monotonic time when the property was set
      - "listener_time": monotonic time when the self-listener fired
    """
    listeners: list[tuple[str, Any]] = []
    for prop in props:
        add_fn = getattr(obj, f"add_{prop}_listener", None)
        if add_fn is None:
            continue

        def make_cb(c: str, p: str):
            def callback():
                now = _time_module.monotonic()
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


def teardown_listeners(obj: Any, listeners: list[tuple[str, Any]]) -> None:
    """Remove all listeners added by setup_listeners."""
    for prop, cb in listeners:
        remove_fn = getattr(obj, f"remove_{prop}_listener", None)
        if remove_fn:
            try:
                remove_fn(cb)
            except Exception:
                pass


# ── Snapshot and restore ─────────────────────────────────────────────────────


def snapshot_properties(
    objects: list[tuple[Any, str, list[str]]],
) -> tuple[dict[tuple[str, str], Any], dict[tuple[str, str], Any]]:
    """Read current values of properties for pre/post-probe comparison and restoration.

    Returns:
        (raw, serialized) — raw holds live objects for comparison/restore,
        serialized holds json_safe values captured eagerly for output.
    """
    raw: dict[tuple[str, str], Any] = {}
    serialized: dict[tuple[str, str], Any] = {}
    for obj, cls, props in objects:
        for prop in props:
            try:
                val = getattr(obj, prop)
                raw[(cls, prop)] = val
                serialized[(cls, prop)] = json_safe(val)
            except Exception:
                pass
    return raw, serialized


def check_unlistened_side_effects(
    snapshot: dict, snap_json: dict, obj_by_cls: dict[str, Any],
    already_seen: set[tuple[str, str]], snapshot_extra: dict[str, set[str]],
    skip: tuple[str, str] | None = None,
) -> list[dict[str, Any]]:
    """Check SNAPSHOT_EXTRA properties for changes not caught by listeners.

    Returns side effect dicts for any that changed, excluding already_seen keys.
    """
    effects = []
    for cls_name, extras in snapshot_extra.items():
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
                        "to": json_safe(current),
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

    Returns:
        True if any property was restored.
    """
    changed = False

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
            continue
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


# ── Core probe functions ─────────────────────────────────────────────────────


def probe_property(
    song: Song, obj: Any, cls: str, prop: str, test_value: Any, fired: list, probe_timing: dict,
    snapshot: dict, snap_json: dict, snapshot_targets: list[tuple[Any, str, list[str]]],
    snapshot_extra: dict[str, set[str]], log: Callable,
) -> Generator[None, None, dict[str, Any]]:
    """Probe a single property for undo tracking, async visibility, and side effects.

    This is a generator — each yield crosses a tick boundary.
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

        result["from"] = json_safe(orig)
        result["to"] = json_safe(test_value)

        # 2. Clear fired listeners and set timing target.
        fired.clear()
        probe_timing["target"] = (cls, prop)
        probe_timing["listener_time"] = None

        # 3. begin_undo_step, set, end_undo_step.
        song.begin_undo_step()
        probe_timing["set_time"] = _time_module.monotonic()
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
                    effect["to"] = json_safe(after)
                    effect["_raw_after"] = after
                except Exception:
                    pass
            side_effects.append(effect)
        side_effects.extend(check_unlistened_side_effects(
            snapshot, snap_json, obj_by_cls, seen_keys, snapshot_extra, skip=(cls, prop),
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
                        effect["undo_value"] = json_safe(current)
                except Exception:
                    pass
            effect.pop("_raw_after", None)
        if side_effects:
            result["side_effects"] = side_effects

        # 12. Restore side effects (loop for cascading next_tick effects).
        for _ in range(3):
            if not restore_side_effects(snapshot, obj_by_cls, log, skip=(cls, prop)):
                break
            yield

        # 13. Restore main property if undo didn't work.
        if not undo_worked:
            try:
                setattr(obj, prop, orig)
            except Exception:
                pass
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
    snapshot_targets: list[tuple[Any, str, list[str]]], snapshot_extra: dict[str, set[str]],
    log: Callable, *, obj: Any = None, effect: str | None = None,
) -> Generator[None, None, dict[str, Any]]:
    """Probe a method for undo tracking, async visibility, and side effects.

    This is a generator — each yield crosses a tick boundary.

    Args:
        effect: "Class.prop" string identifying the primary effect (e.g. "Song.tracks").
            The method's async_visibility, undo_tracked, from/to, and listener data are
            measured on this property. It is recorded as the top-level "effect" field and
            excluded from side_effects.
        check_fn: () -> bool — fallback for detecting the effect when the named property
            isn't in the listener/snapshot system. Used for async visibility detection.
    """
    result: dict[str, Any] = {}
    if args:
        result["args"] = [json_safe(a) for a in args]

    try:
        # Resolve the effect property for direct measurement.
        obj_by_cls = {c: o for o, c, _ in snapshot_targets}
        effect_cls = effect_prop = None
        effect_obj = None
        effect_key = None
        effect_orig = None
        if effect:
            effect_cls, effect_prop = effect.split(".", 1)
            effect_obj = obj_by_cls.get(effect_cls)
            effect_key = (effect_cls, effect_prop)
            if effect_obj is not None:
                try:
                    effect_orig = getattr(effect_obj, effect_prop)
                except Exception:
                    pass

        # 1. Clear fired listeners.
        fired.clear()
        probe_timing["target"] = effect_key
        probe_timing["set_time"] = _time_module.monotonic()
        probe_timing["listener_time"] = None

        # 2. begin_undo_step, call method, end_undo_step.
        target = obj if obj is not None else song
        song.begin_undo_step()
        getattr(target, method)(*args)
        song.end_undo_step()

        # 3. Check effect immediately — use the named property if available, else check_fn.
        if effect_obj is not None and effect_orig is not None:
            try:
                readback = getattr(effect_obj, effect_prop)
                is_immediate = not fuzzy_eq(readback, effect_orig)
            except Exception:
                is_immediate = check_fn()
        else:
            is_immediate = check_fn()

        # 4. Yield to next tick.
        yield

        # 5. Classify async visibility.
        if is_immediate:
            async_vis = "immediate"
        else:
            if effect_obj is not None and effect_orig is not None:
                try:
                    readback_next = getattr(effect_obj, effect_prop)
                    has_effect = not fuzzy_eq(readback_next, effect_orig)
                except Exception:
                    has_effect = check_fn()
            else:
                has_effect = check_fn()
            async_vis = "next_tick" if has_effect else "no_effect"

        # 6. Collect side effects from fired listeners.
        side_effects = []
        seen_keys: set[tuple[str, str]] = set()
        for c, p, dt in fired:
            se: dict[str, Any] = {"label": c, "prop": p, "listener_latency_ms": round(dt * 1000, 1)}
            key = (c, p)
            seen_keys.add(key)
            if key in snapshot:
                try:
                    after = getattr(obj_by_cls[c], p)
                    se["from"] = snap_json[key]
                    se["to"] = json_safe(after)
                    se["_raw_after"] = after
                except Exception:
                    pass
            side_effects.append(se)
        side_effects.extend(check_unlistened_side_effects(
            snapshot, snap_json, obj_by_cls, seen_keys, snapshot_extra,
        ))

        # 7. Build the primary effect entry.
        effect_data: dict[str, Any] | None = None
        if effect:
            effect_data = {"label": effect_cls, "prop": effect_prop}
            effect_data["async_visibility"] = async_vis
            # Capture from/to on the effect property.
            if effect_key in snapshot:
                effect_data["from"] = snap_json[effect_key]
            if effect_obj is not None:
                try:
                    after_val = getattr(effect_obj, effect_prop)
                    effect_data["to"] = json_safe(after_val)
                    effect_data["_raw_after"] = after_val
                except Exception:
                    pass
            # Capture listener latency if the effect's listener fired.
            if probe_timing["listener_time"] is not None:
                dt = probe_timing["listener_time"] - probe_timing["set_time"]
                effect_data["listener_latency_ms"] = round(dt * 1000, 1)
            probe_timing["target"] = None

        # 8. Clear fired and undo.
        fired.clear()
        song.undo()

        # 9. Yield to next tick.
        yield

        # 10. Check undo tracking on the effect property.
        if async_vis == "no_effect":
            undo_tracked = "n/a"
        elif effect_obj is not None and effect_orig is not None:
            try:
                after_undo = getattr(effect_obj, effect_prop)
                undo_tracked = fuzzy_eq(after_undo, effect_orig)
            except Exception:
                undo_tracked = not check_fn()
        else:
            undo_tracked = not check_fn()

        # 11. Check undo behavior on side effects and the primary effect.
        undo_fired = {(c, p) for c, p, _ in fired}

        if effect_data is not None:
            effect_data["undo_tracked"] = undo_tracked
            effect_data["undo_fires_listener"] = effect_key in undo_fired
            # Check undo_result on the effect property.
            if effect_key in snapshot and effect_obj is not None:
                try:
                    current = getattr(effect_obj, effect_prop)
                    if fuzzy_eq(current, snapshot[effect_key]):
                        effect_data["undo_result"] = "restored"
                    elif "_raw_after" in effect_data and fuzzy_eq(current, effect_data["_raw_after"]):
                        effect_data["undo_result"] = "unchanged"
                    else:
                        effect_data["undo_result"] = "changed"
                        effect_data["undo_value"] = json_safe(current)
                except Exception:
                    pass
            effect_data.pop("_raw_after", None)

        for se in side_effects:
            key = (se["label"], se["prop"])
            se["undo_fires_listener"] = key in undo_fired
            if key in snapshot:
                try:
                    current = getattr(obj_by_cls[se["label"]], se["prop"])
                    if fuzzy_eq(current, snapshot[key]):
                        se["undo_result"] = "restored"
                    elif "_raw_after" in se and fuzzy_eq(current, se["_raw_after"]):
                        se["undo_result"] = "unchanged"
                    else:
                        se["undo_result"] = "changed"
                        se["undo_value"] = json_safe(current)
                except Exception:
                    pass
            se.pop("_raw_after", None)

        # Remove the primary effect from side_effects (if it was captured there too).
        if effect_key:
            side_effects = [se for se in side_effects
                           if not (se.get("label") == effect_cls and se.get("prop") == effect_prop)]

        # Write results.
        if effect_data is not None:
            result["effect"] = effect_data
        else:
            # No named effect — put async/undo at top level (legacy format).
            result["async_visibility"] = async_vis
            result["undo_tracked"] = undo_tracked

        if side_effects:
            result["side_effects"] = side_effects

        # 11. Restore side effects (loop for cascading next_tick effects).
        for _ in range(3):
            if not restore_side_effects(snapshot, obj_by_cls, log):
                break
            yield

        # 12. If undo didn't work, run cleanup.
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


# ── Utilities ────────────────────────────────────────────────────────────────


def ptr_set(items: Any) -> set[int]:
    """Extract stable _live_ptr values from a list of Live API objects."""
    return {item._live_ptr for item in items}


def find_new_index(items: Any, before_ptrs: set[int]) -> int | None:
    """Find the index of the first item whose _live_ptr wasn't in before_ptrs."""
    for i, item in enumerate(items):
        if item._live_ptr not in before_ptrs:
            return i
    return None
