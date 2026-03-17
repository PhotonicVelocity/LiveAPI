"""Song probes — undo tracking, async visibility, value ranges, and error behavior."""

from __future__ import annotations

from typing import Any

from tools.probe.base import ProbeContext

CLASS_NAME = "Song"


# ── Listenable properties (from stubs/12.3.6/Live/Song/Song.pyi) ─────────────

SONG_LISTENABLE: list[str] = [
    "appointed_device",
    "arrangement_overdub",
    "back_to_arranger",
    "can_capture_midi",
    "can_jump_to_next_cue",
    "can_jump_to_prev_cue",
    "clip_trigger_quantization",
    "count_in_duration",
    "cue_points",
    "current_song_time",
    "data",
    "exclusive_arm",
    "groove_amount",
    "is_ableton_link_enabled",
    "is_ableton_link_start_stop_sync_enabled",
    "is_counting_in",
    "is_playing",
    "loop",
    "loop_length",
    "loop_start",
    "metronome",
    "midi_recording_quantization",
    "nudge_down",
    "nudge_up",
    "overdub",
    "punch_in",
    "punch_out",
    "re_enable_automation_enabled",
    "record_mode",
    "return_tracks",
    "root_note",
    "scale_information",
    "scale_intervals",
    "scale_mode",
    "scale_name",
    "scenes",
    "session_automation_record",
    "session_record",
    "session_record_status",
    "signature_denominator",
    "signature_numerator",
    "song_length",
    "start_time",
    "swing_amount",
    "tempo",
    "tempo_follower_enabled",
    "tracks",
    "tuning_system",
    "visible_tracks",
]

VIEW_LISTENABLE: list[str] = [
    "detail_clip",
    "draw_mode",
    "follow_song",
    "selected_chain",
    "selected_parameter",
    "selected_scene",
    "selected_track",
]


# ── Helpers ────────────────────────────────────────────────────────────────────

# Cached OIDs and snapshot, populated by _setup()
_state: dict[str, Any] = {}


def _setup(ctx: ProbeContext) -> None:
    """Subscribe to all listenable properties and take initial snapshot."""
    if _state.get("ready"):
        return

    song_oid = ctx.song_oid
    view_oid = ctx.resolve_child(song_oid, "view")
    if not view_oid:
        raise RuntimeError("Could not resolve Song.View")

    _state["song_oid"] = song_oid
    _state["view_oid"] = view_oid

    snapshot = ctx.subscribe_all({
        "Song": (song_oid, SONG_LISTENABLE),
        "Song.View": (view_oid, VIEW_LISTENABLE),
    })
    _state["snapshot"] = snapshot
    _state["ready"] = True

    print(f"  Initial Song snapshot: {len(snapshot.get('Song', {}))} values")
    print(f"  Initial Song.View snapshot: {len(snapshot.get('Song.View', {}))} values")


def _teardown(ctx: ProbeContext) -> None:
    """Unsubscribe all listeners."""
    ctx.unsubscribe_all()
    _state.clear()


def _song_oid(ctx: ProbeContext) -> str:
    return ctx.song_oid


def _view_oid(ctx: ProbeContext) -> str:
    _setup(ctx)
    return _state["view_oid"]


def _first_track_oid(ctx: ProbeContext) -> str:
    tracks = ctx.resolve_children(ctx.song_oid, "tracks")
    if not tracks:
        raise RuntimeError("No tracks in set")
    return tracks[0]["oid"]


def _first_scene_oid(ctx: ProbeContext) -> str:
    scenes = ctx.resolve_children(ctx.song_oid, "scenes")
    if not scenes:
        raise RuntimeError("No scenes in set")
    return scenes[0]["oid"]


# ── Song settable properties with safe test values ─────────────────────────────

# (property_name, test_value) — test_value must differ from typical defaults
SONG_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("arrangement_overdub", True),
    ("back_to_arranger", True),
    ("clip_trigger_quantization", 2),  # Quantization enum — 0=none, 1=8bars, 2=4bars, ...
    ("current_song_time", 4.0),
    ("groove_amount", 0.5),
    ("is_playing", True),
    ("loop", True),
    ("loop_length", 8.0),
    ("loop_start", 4.0),
    ("metronome", True),
    ("midi_recording_quantization", 1),  # RecordingQuantization enum
    ("nudge_down", True),
    ("nudge_up", True),
    ("overdub", True),
    ("punch_in", True),
    ("punch_out", True),
    ("record_mode", True),
    ("root_note", 2),  # 0=C, 2=D
    ("scale_mode", True),
    ("scale_name", "Minor"),
    ("session_automation_record", True),
    ("session_record", True),
    ("signature_denominator", 8),
    ("signature_numerator", 3),
    ("start_time", 4.0),
    ("swing_amount", 0.5),
    ("tempo", 130.0),
    ("tempo_follower_enabled", True),
    ("is_ableton_link_enabled", True),
    ("is_ableton_link_start_stop_sync_enabled", True),
]

# Properties that need special handling (skipped from generic undo/async probing)
SONG_SKIP_UNDO = {
    "is_playing",  # transport state, not undoable
    "nudge_down",  # momentary, not undoable
    "nudge_up",  # momentary, not undoable
    "record_mode",  # requires armed track
    "session_record",  # requires armed track
    "session_automation_record",  # requires armed track
    "current_song_time",  # transport position, not undoable
    "start_time",  # arrangement start, undo behavior unclear without playing
}

# Song.View settable properties — these need the view OID
VIEW_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("draw_mode", True),
    ("follow_song", True),
]

# View properties that need object references (handled separately)
# detail_clip, highlighted_clip_slot, selected_chain, selected_scene, selected_track


# ── Undo + Async Probes ───────────────────────────────────────────────────────


def probe_undo(ctx: ProbeContext) -> None:
    """Probe undo tracking and async visibility for every settable Song property."""
    _setup(ctx)
    song = _song_oid(ctx)

    for prop, test_val in SONG_SETTABLE_PROPS:
        if prop in SONG_SKIP_UNDO:
            continue
        ctx.probe_property_undo_async(song, "Song", prop, test_val)

    # Song.View properties
    view = _view_oid(ctx)
    for prop, test_val in VIEW_SETTABLE_PROPS:
        ctx.probe_property_undo_async(view, "Song.View", prop, test_val)

    # Object-reference properties
    _probe_appointed_device_undo(ctx)

    # Object-reference properties on Song.View
    _probe_view_selected_scene_undo(ctx, view)
    _probe_view_selected_track_undo(ctx, view)

    # Method undo probes
    _probe_method_undo_create_scene(ctx)
    _probe_method_undo_create_midi_track(ctx)
    _probe_method_undo_create_audio_track(ctx)
    _probe_method_undo_create_return_track(ctx)
    _probe_method_undo_duplicate_scene(ctx)
    _probe_method_undo_duplicate_track(ctx)
    _probe_method_undo_set_or_delete_cue(ctx)
    _probe_method_undo_capture_and_insert_scene(ctx)


def _probe_appointed_device_undo(ctx: ProbeContext) -> None:
    """Probe Song.appointed_device undo by appointing a device from the first track."""
    tracks = ctx.resolve_children(ctx.song_oid, "tracks")
    if not tracks:
        print("  [skip] Song.appointed_device — no tracks")
        return

    devices = ctx.resolve_children(tracks[0]["oid"], "devices")
    if not devices:
        print("  [skip] Song.appointed_device — first track has no devices")
        return

    song = ctx.song_oid
    # get returns {"oid": "...", "type": "..."} for object-reference properties
    orig = ctx.get(song, "appointed_device")
    orig_oid = orig["oid"] if isinstance(orig, dict) else orig
    target_oid = devices[0]["oid"]

    if orig_oid == target_oid and len(devices) > 1:
        target_oid = devices[1]["oid"]
    elif orig_oid == target_oid:
        print("  [skip] Song.appointed_device — only one device, matches current")
        return

    result = ctx._record("Song", "appointed_device", "property")
    try:
        ctx.call(song, "begin_undo_step")
        ctx.set(song, "appointed_device", {"oid": target_oid})
        immediate = ctx.get(song, "appointed_device")
        imm_oid = immediate["oid"] if isinstance(immediate, dict) else immediate
        ctx.call(song, "end_undo_step")

        result.set("async_visibility", "immediate" if imm_oid == target_oid else "next_tick")

        ctx.wait()
        ctx.call(song, "undo")
        ctx.wait()

        after_undo = ctx.get(song, "appointed_device")
        after_oid = after_undo["oid"] if isinstance(after_undo, dict) else after_undo
        result.set("undo_tracked", after_oid == orig_oid)

        # Redo to neutralize undo, then restore
        ctx.call(song, "redo")
        ctx.wait()
        current = ctx.get(song, "appointed_device")
        current_oid = current["oid"] if isinstance(current, dict) else current
        if current_oid != orig_oid:
            ctx.set(song, "appointed_device", {"oid": orig_oid})
            ctx.wait()
    except Exception as e:
        result.set("error", str(e)[:200])

    ctx._log("Song", "appointed_device", "property", result)


def _probe_view_selected_scene_undo(ctx: ProbeContext, view_oid: str) -> None:
    """Probe Song.View.selected_scene undo by switching scenes."""
    scenes = ctx.resolve_children(ctx.song_oid, "scenes")
    if len(scenes) < 2:
        print("  [skip] Song.View.selected_scene — need ≥2 scenes")
        return

    orig = ctx.get(view_oid, "selected_scene")
    orig_oid = orig["oid"] if isinstance(orig, dict) else orig
    target_oid = scenes[1]["oid"] if scenes[0]["oid"] == orig_oid else scenes[0]["oid"]

    result = ctx._record("Song.View", "selected_scene", "property")
    try:
        ctx.call(ctx.song_oid, "begin_undo_step")
        ctx.set(view_oid, "selected_scene", {"oid": target_oid})
        immediate = ctx.get(view_oid, "selected_scene")
        imm_oid = immediate["oid"] if isinstance(immediate, dict) else immediate
        ctx.call(ctx.song_oid, "end_undo_step")

        result.set("async_visibility", "immediate" if imm_oid == target_oid else "next_tick")

        ctx.wait()
        ctx.call(ctx.song_oid, "undo")
        ctx.wait()

        after_undo = ctx.get(view_oid, "selected_scene")
        after_oid = after_undo["oid"] if isinstance(after_undo, dict) else after_undo
        result.set("undo_tracked", after_oid == orig_oid)

        # Redo to neutralize undo, then restore
        ctx.call(ctx.song_oid, "redo")
        ctx.wait()
        current = ctx.get(view_oid, "selected_scene")
        current_oid = current["oid"] if isinstance(current, dict) else current
        if current_oid != orig_oid:
            ctx.set(view_oid, "selected_scene", {"oid": orig_oid})
            ctx.wait()
    except Exception as e:
        result.set("error", str(e)[:200])

    ctx._log("Song.View", "selected_scene", "property", result)


def _probe_view_selected_track_undo(ctx: ProbeContext, view_oid: str) -> None:
    """Probe Song.View.selected_track undo by switching tracks."""
    tracks = ctx.resolve_children(ctx.song_oid, "tracks")
    if len(tracks) < 2:
        print("  [skip] Song.View.selected_track — need ≥2 tracks")
        return

    orig = ctx.get(view_oid, "selected_track")
    orig_oid = orig["oid"] if isinstance(orig, dict) else orig
    target_oid = tracks[1]["oid"] if tracks[0]["oid"] == orig_oid else tracks[0]["oid"]

    result = ctx._record("Song.View", "selected_track", "property")
    try:
        ctx.call(ctx.song_oid, "begin_undo_step")
        ctx.set(view_oid, "selected_track", {"oid": target_oid})
        immediate = ctx.get(view_oid, "selected_track")
        imm_oid = immediate["oid"] if isinstance(immediate, dict) else immediate
        ctx.call(ctx.song_oid, "end_undo_step")

        result.set("async_visibility", "immediate" if imm_oid == target_oid else "next_tick")

        ctx.wait()
        ctx.call(ctx.song_oid, "undo")
        ctx.wait()

        after_undo = ctx.get(view_oid, "selected_track")
        after_oid = after_undo["oid"] if isinstance(after_undo, dict) else after_undo
        result.set("undo_tracked", after_oid == orig_oid)

        # Redo to neutralize undo, then restore
        ctx.call(ctx.song_oid, "redo")
        ctx.wait()
        current = ctx.get(view_oid, "selected_track")
        current_oid = current["oid"] if isinstance(current, dict) else current
        if current_oid != orig_oid:
            ctx.set(view_oid, "selected_track", {"oid": orig_oid})
            ctx.wait()
    except Exception as e:
        result.set("error", str(e)[:200])

    ctx._log("Song.View", "selected_track", "property", result)


# ── Method undo probes ─────────────────────────────────────────────────────────


def _probe_method_undo_create_scene(ctx: ProbeContext) -> None:
    """Probe Song.create_scene undo — create a scene at the end, undo, check count."""
    scenes_before = ctx.resolve_children(ctx.song_oid, "scenes")
    count_before = len(scenes_before)

    def check_fn() -> bool:
        return len(ctx.resolve_children(ctx.song_oid, "scenes")) > count_before

    ctx.probe_method_undo(
        "Song",
        "create_scene",
        ctx.song_oid,
        [count_before],
        check_fn=check_fn,
        cleanup_fn=lambda: _delete_last_scene(ctx, count_before),
    )


def _delete_last_scene(ctx: ProbeContext, expected_count: int) -> None:
    scenes = ctx.resolve_children(ctx.song_oid, "scenes")
    if len(scenes) > expected_count:
        ctx.call(ctx.song_oid, "delete_scene", [len(scenes) - 1])
        ctx.wait()


def _probe_method_undo_create_midi_track(ctx: ProbeContext) -> None:
    tracks_before = ctx.resolve_children(ctx.song_oid, "tracks")
    count_before = len(tracks_before)

    def check_fn() -> bool:
        return len(ctx.resolve_children(ctx.song_oid, "tracks")) > count_before

    ctx.probe_method_undo(
        "Song",
        "create_midi_track",
        ctx.song_oid,
        [count_before],
        check_fn=check_fn,
        cleanup_fn=lambda: _delete_last_track(ctx, count_before),
    )


def _probe_method_undo_create_audio_track(ctx: ProbeContext) -> None:
    tracks_before = ctx.resolve_children(ctx.song_oid, "tracks")
    count_before = len(tracks_before)

    def check_fn() -> bool:
        return len(ctx.resolve_children(ctx.song_oid, "tracks")) > count_before

    ctx.probe_method_undo(
        "Song",
        "create_audio_track",
        ctx.song_oid,
        [count_before],
        check_fn=check_fn,
        cleanup_fn=lambda: _delete_last_track(ctx, count_before),
    )


def _probe_method_undo_create_return_track(ctx: ProbeContext) -> None:
    returns_before = ctx.resolve_children(ctx.song_oid, "return_tracks")
    count_before = len(returns_before)

    def check_fn() -> bool:
        return len(ctx.resolve_children(ctx.song_oid, "return_tracks")) > count_before

    def cleanup() -> None:
        returns = ctx.resolve_children(ctx.song_oid, "return_tracks")
        if len(returns) > count_before:
            ctx.call(ctx.song_oid, "delete_return_track", [len(returns) - 1])
            ctx.wait()

    ctx.probe_method_undo(
        "Song",
        "create_return_track",
        ctx.song_oid,
        [],
        check_fn=check_fn,
        cleanup_fn=cleanup,
    )


def _delete_last_track(ctx: ProbeContext, expected_count: int) -> None:
    tracks = ctx.resolve_children(ctx.song_oid, "tracks")
    if len(tracks) > expected_count:
        ctx.call(ctx.song_oid, "delete_track", [len(tracks) - 1])
        ctx.wait()


def _probe_method_undo_duplicate_scene(ctx: ProbeContext) -> None:
    scenes_before = ctx.resolve_children(ctx.song_oid, "scenes")
    count_before = len(scenes_before)

    def check_fn() -> bool:
        return len(ctx.resolve_children(ctx.song_oid, "scenes")) > count_before

    ctx.probe_method_undo(
        "Song",
        "duplicate_scene",
        ctx.song_oid,
        [0],
        check_fn=check_fn,
        cleanup_fn=lambda: _delete_last_scene(ctx, count_before),
    )


def _probe_method_undo_duplicate_track(ctx: ProbeContext) -> None:
    tracks_before = ctx.resolve_children(ctx.song_oid, "tracks")
    count_before = len(tracks_before)

    def check_fn() -> bool:
        return len(ctx.resolve_children(ctx.song_oid, "tracks")) > count_before

    ctx.probe_method_undo(
        "Song",
        "duplicate_track",
        ctx.song_oid,
        [0],
        check_fn=check_fn,
        cleanup_fn=lambda: _delete_last_track(ctx, count_before),
    )


def _probe_method_undo_set_or_delete_cue(ctx: ProbeContext) -> None:
    """Probe set_or_delete_cue — toggles a cue point at the current position."""
    cues_before = ctx.resolve_children(ctx.song_oid, "cue_points")
    count_before = len(cues_before)

    def check_fn() -> bool:
        return len(ctx.resolve_children(ctx.song_oid, "cue_points")) != count_before

    ctx.probe_method_undo(
        "Song",
        "set_or_delete_cue",
        ctx.song_oid,
        [],
        check_fn=check_fn,
    )


def _probe_method_undo_capture_and_insert_scene(ctx: ProbeContext) -> None:
    """Probe capture_and_insert_scene undo."""
    scenes_before = ctx.resolve_children(ctx.song_oid, "scenes")
    count_before = len(scenes_before)

    def check_fn() -> bool:
        return len(ctx.resolve_children(ctx.song_oid, "scenes")) > count_before

    ctx.probe_method_undo(
        "Song",
        "capture_and_insert_scene",
        ctx.song_oid,
        [0],
        check_fn=check_fn,
        cleanup_fn=lambda: _delete_last_scene(ctx, count_before),
    )


# ── Async-only probes (for props skipped in undo) ─────────────────────────────


def probe_async(ctx: ProbeContext) -> None:
    """Probe async visibility for properties skipped in undo probing."""
    _setup(ctx)
    song = _song_oid(ctx)

    # These are transport/momentary props — still useful to know async visibility
    async_only_props: list[tuple[str, Any]] = [
        ("is_playing", True),
        ("current_song_time", 4.0),
        ("nudge_down", True),
        ("nudge_up", True),
    ]

    for prop, test_val in async_only_props:
        result = ctx._record("Song", prop, "property")
        try:
            orig = ctx.get(song, prop)
            if orig == test_val:
                result.set("async_visibility", "skip")
                result.set("notes", f"test_value matches original ({orig!r})")
                ctx._log("Song", prop, "property", result)
                continue

            ctx.set(song, prop, test_val)
            immediate = ctx.get(song, prop)
            result.set("async_visibility", "immediate" if immediate == test_val else "next_tick")

            # Restore
            ctx.set(song, prop, orig)
            ctx.wait()
        except Exception as e:
            result.set("async_visibility", "error")
            result.set("error", str(e)[:200])

        ctx._log("Song", prop, "property", result)


# ── Value range probes ─────────────────────────────────────────────────────────


def probe_range(ctx: ProbeContext) -> None:
    """Probe value ranges and boundary behavior for Song properties."""
    _setup(ctx)
    song = _song_oid(ctx)

    # tempo: documented as 20.0–999.0
    ctx.probe_value_range(song, "Song", "tempo", [20.0, 60.0, 120.0, 200.0, 500.0, 999.0, 19.99, 999.01, 0.0, -1.0])

    # groove_amount: 0.0–1.0
    ctx.probe_value_range(song, "Song", "groove_amount", [0.0, 0.25, 0.5, 0.75, 1.0, -0.01, 1.01, 2.0])

    # swing_amount: 0.0–1.0
    ctx.probe_value_range(song, "Song", "swing_amount", [0.0, 0.25, 0.5, 0.75, 1.0, -0.01, 1.01])

    # signature_numerator: typical 1–32
    ctx.probe_value_range(song, "Song", "signature_numerator", [1, 2, 3, 4, 5, 6, 7, 8, 12, 16, 32, 0, -1, 64, 99])

    # signature_denominator: powers of 2 typically (1, 2, 4, 8, 16)
    ctx.probe_value_range(
        song, "Song", "signature_denominator", [1, 2, 4, 8, 16, 32, 0, 3, 5, 6, 7, 9, -1]
    )

    # root_note: 0–11
    ctx.probe_value_range(song, "Song", "root_note", [0, 1, 6, 11, 12, -1, 255])

    # clip_trigger_quantization: Quantization enum 0–13
    ctx.probe_value_range(
        song, "Song", "clip_trigger_quantization", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, -1]
    )

    # midi_recording_quantization: RecordingQuantization enum
    ctx.probe_value_range(
        song, "Song", "midi_recording_quantization", [0, 1, 2, 3, 4, 5, 6, 7, 8, -1, 20]
    )

    # loop_start and loop_length: non-negative floats
    ctx.probe_value_range(song, "Song", "loop_start", [0.0, 1.0, 4.0, 100.0, -1.0])
    ctx.probe_value_range(song, "Song", "loop_length", [1.0, 4.0, 8.0, 16.0, 0.0, -1.0])

    # scale_name: known scale names
    ctx.probe_value_range(
        song,
        "Song",
        "scale_name",
        ["Major", "Minor", "Dorian", "Mixolydian", "Lydian", "Phrygian", "Locrian", "NotAScale", ""],
    )


# ── Error behavior probes ─────────────────────────────────────────────────────


def probe_error(ctx: ProbeContext) -> None:
    """Probe error conditions and messages for Song properties and methods."""
    _setup(ctx)
    song = _song_oid(ctx)

    # tempo with bad types
    ctx.probe_error(song, "Song", "tempo", [None, "fast", True, [120]])

    # signature with bad values
    ctx.probe_error(song, "Song", "signature_numerator", [None, 0, -1, "4"])
    ctx.probe_error(song, "Song", "signature_denominator", [None, 0, -1, 3, "8"])

    # scale_name with bad values
    ctx.probe_error(song, "Song", "scale_name", [None, 123, True])

    # Method error probes
    _probe_error_delete_track(ctx)
    _probe_error_delete_scene(ctx)
    _probe_error_create_scene(ctx)
    _probe_error_jump_by(ctx)


def _probe_error_delete_track(ctx: ProbeContext) -> None:
    """Probe delete_track with invalid indices."""
    result = ctx._record("Song", "delete_track", "method")
    errors: list[dict[str, str]] = []

    for idx in [-1, 9999, None]:
        try:
            ctx.call(ctx.song_oid, "delete_track", [idx])
            errors.append({"value": repr(idx), "error": "no error (unexpected)"})
            # Undo if it somehow succeeded
            ctx.call(ctx.song_oid, "undo")
            ctx.wait()
        except Exception as e:
            errors.append({"value": repr(idx), "error": str(e)[:200]})

    result.set("error_behavior", errors)
    ctx._log("Song", "delete_track", "method", result)


def _probe_error_delete_scene(ctx: ProbeContext) -> None:
    """Probe delete_scene with invalid indices."""
    result = ctx._record("Song", "delete_scene", "method")
    errors: list[dict[str, str]] = []

    for idx in [-1, 9999, None]:
        try:
            ctx.call(ctx.song_oid, "delete_scene", [idx])
            errors.append({"value": repr(idx), "error": "no error (unexpected)"})
            ctx.call(ctx.song_oid, "undo")
            ctx.wait()
        except Exception as e:
            errors.append({"value": repr(idx), "error": str(e)[:200]})

    result.set("error_behavior", errors)
    ctx._log("Song", "delete_scene", "method", result)


def _probe_error_create_scene(ctx: ProbeContext) -> None:
    """Probe create_scene with invalid indices."""
    result = ctx._record("Song", "create_scene", "method")
    errors: list[dict[str, str]] = []

    for idx in [-1, 9999, None]:
        try:
            ctx.call(ctx.song_oid, "create_scene", [idx])
            errors.append({"value": repr(idx), "error": "no error (unexpected)"})
            ctx.call(ctx.song_oid, "undo")
            ctx.wait()
        except Exception as e:
            errors.append({"value": repr(idx), "error": str(e)[:200]})

    result.set("error_behavior", errors)
    ctx._log("Song", "create_scene", "method", result)


def _probe_error_jump_by(ctx: ProbeContext) -> None:
    """Probe jump_by with extreme values."""
    result = ctx._record("Song", "jump_by", "method")
    errors: list[dict[str, str]] = []

    for val in [None, "1.0", 2147483647.0, float("inf"), float("nan")]:
        try:
            ctx.call(ctx.song_oid, "jump_by", [val])
            errors.append({"value": repr(val), "error": "no error"})
        except Exception as e:
            errors.append({"value": repr(val), "error": str(e)[:200]})

    result.set("error_behavior", errors)
    ctx._log("Song", "jump_by", "method", result)
