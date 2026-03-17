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
from typing import Any


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


# ── Helpers ────────────────────────────────────────────────────────────────────


def fuzzy_eq(a: Any, b: Any) -> bool:
    """Compare with tolerance for float precision."""
    if isinstance(a, float) and isinstance(b, float):
        return abs(a - b) < 0.01
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(float(a) - float(b)) < 0.01
    return a == b


def probe_property(song, obj, cls: str, prop: str, test_value: Any, log):
    """Probe a single property for undo tracking and async visibility.

    This is a generator — each yield crosses a tick boundary.

    Steps:
      1. Read original value. Flip booleans automatically.
      2. begin_undo_step, set, end_undo_step.
      3. Read back immediately (same tick) → async_visibility = "immediate" if changed.
      4. Yield to next tick.
      5. If not immediate, read again → "next_tick" if changed, "no_change" otherwise.
      6. Undo.
      7. Yield to next tick (always — undo may also be async).
      8. Read back → undo_tracked = True if original value restored.
      9. If undo didn't work, redo to restore previous stack entry, then fix our property.
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

        # 2. begin_undo_step, set, end_undo_step.
        song.begin_undo_step()
        setattr(obj, prop, test_value)
        song.end_undo_step()

        # 3. Read back immediately.
        readback = getattr(obj, prop)
        is_immediate = fuzzy_eq(readback, test_value)

        # 4. Yield to next tick.
        yield

        # 5. If not immediate, check again.
        if is_immediate:
            result["async_visibility"] = "immediate"
        else:
            readback_next = getattr(obj, prop)
            if fuzzy_eq(readback_next, test_value):
                result["async_visibility"] = "next_tick"
            else:
                result["async_visibility"] = "no_change"

        # 6. Undo.
        song.undo()

        # 7. Yield to next tick.
        yield

        # 8. Read back → undo tracking.
        after_undo = getattr(obj, prop)
        undo_worked = fuzzy_eq(after_undo, orig)
        result["undo_tracked"] = undo_worked

        # 9. Restore if undo didn't work.
        if not undo_worked:
            setattr(obj, prop, orig)
            yield

    except Exception as e:
        result["async_visibility"] = result.get("async_visibility", "error")
        result["undo_tracked"] = result.get("undo_tracked", "error")
        result["error"] = str(e)[:200]

    tag = result.get("async_visibility", "?")
    undo = result.get("undo_tracked", "?")
    log(f"  [prop] {cls}.{prop}: async={tag}, undo={undo}")
    return result


def run(song, log):
    """Probe all settable Song and Song.View properties."""
    import time
    from datetime import datetime

    t0 = time.monotonic()
    log("[song_props] Starting property probes")
    results: dict[str, dict[str, dict[str, Any]]] = {
        "Song": {"properties": {}},
        "Song.View": {"properties": {}},
    }

    # Song properties
    for prop, test_val in SONG_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        gen = probe_property(song, song, "Song", prop, test_val, log)
        # Drive the generator across ticks
        try:
            while True:
                next(gen)
                yield  # cross tick boundary
        except StopIteration as e:
            if e.value is not None:
                results["Song"]["properties"][prop] = e.value

    # Song.View properties
    view = song.view
    for prop, test_val in VIEW_SETTABLE_PROPS:
        gen = probe_property(song, view, "Song.View", prop, test_val, log)
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Song.View"]["properties"][prop] = e.value

    # Write results
    import Live  # type: ignore

    app = Live.Application.get_application()
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
        existing_classes[cls]["properties"].update(data["properties"])

    elapsed = round(time.monotonic() - t0, 1)
    output = {
        "version": version,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "elapsed_seconds": elapsed,
        "classes": existing_classes,
    }

    with open(outpath, "w") as f:
        json.dump(output, f, indent=2)

    total = sum(len(d["properties"]) for d in results.values())
    log(f"[song_props] Done — {total} properties probed in {elapsed}s, wrote {outpath}")
