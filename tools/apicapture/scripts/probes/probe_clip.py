"""Probe the Clip module.

Uses track 0 slot 0 (MIDI clip, "Coffee Lead") from the demo set.
Audio-specific properties tested on track 10 slot 0 if available.

Usage:
    echo scripts/probes/probe_clip.py > /tmp/apicapture_targeted_probe

Skipped members:
    - Note methods (get_notes*, set_notes, select_*, apply_note_modifications, etc.) — read/write, not behavioral
    - Envelope methods (automation_envelope, clear_*_envelopes, create_automation_envelope) — need automation data
    - beat_to_sample_time, sample_to_beat_time, seconds_to_sample_time — conversion functions, read-only
    - note_number_to_name — utility, read-only
    - move_warp_marker — needs warp markers
    - replace_selected_notes — needs selected notes
    - groove — needs a Groove object (demo set has none)
    - position — only meaningful while clip is playing
    - get_notes*, get_selected_notes* — read-only
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


# ── Settable properties — universal (work on both MIDI and audio clips) ───────

CLIP_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("color", 12243060),  # RGB int — 0xBAD074 (pale green)
    ("color_index", 10),
    ("end_marker", 16.0),
    ("launch_mode", 1),  # 0=trigger, 1=gate, 2=toggle, 3=repeat
    ("launch_quantization", 2),  # Quantization enum
    ("legato", True),
    ("loop_end", 16.0),
    ("loop_start", 4.0),
    ("looping", True),
    ("muted", True),
    ("name", "__probe_test__"),
    ("signature_denominator", 8),
    ("signature_numerator", 3),
    ("start_marker", 4.0),
    ("velocity_amount", 0.5),
]

# Audio-only settable properties
AUDIO_SETTABLE_PROPS: list[tuple[str, Any]] = [
    ("gain", 0.5),
    ("pitch_coarse", 3),
    ("pitch_fine", 0.5),
    ("ram_mode", True),
    ("warp_mode", 1),  # WarpMode enum
    # warping — handled as special case (undo invalidates the clip reference)
]

SKIP_UNDO: set[str] = set()


# ── Behavioral notes ──────────────────────────────────────────────────────────

NOTES: dict[str, str] = {
    "Clip.fire": (
        "With quantization, the effect is on ``is_triggered``."
    ),
    "Clip.set_fire_button_state": (
        "With quantization, the effect is on ``is_triggered``. "
        "Supports press/release for Gate and Repeat launch modes."
    ),
    "Clip.warping": (
        "Undoing a warping change on audio clips invalidates the Python object reference — "
        "re-fetch the clip from its ``ClipSlot`` after undo."
    ),
}


# ── Module-specific config ────────────────────────────────────────────────────

LISTENER_EXCLUDE: set[str] = {"current_song_time", "playing_position"}  # fires every audio tick while playing

SNAPSHOT_EXTRA: dict[str, set[str]] = {}

CROSS_MODULE_LISTENERS: dict[str, list[str]] = {
    "Song": ["is_playing", "back_to_arranger"],
    "ClipSlot": ["playing_status", "is_triggered"],
}


# ── Main probe ────────────────────────────────────────────────────────────────


def run(song: Song, log: Callable) -> Generator[None, None, None]:
    """Probe Clip properties and methods."""
    import time
    from datetime import datetime

    t0 = time.monotonic()
    log("[probe_clip] Starting Clip probes")

    # Use track 0 slot 0 (MIDI clip)
    track = song.tracks[0]
    clip = track.clip_slots[2].clip

    results: dict[str, dict[str, dict[str, Any]]] = {
        "Clip": {"properties": {}, "methods": {}},
    }
    fired: list[tuple[str, str, float]] = []
    probe_timing: dict[str, Any] = {"target": None, "set_time": 0.0, "listener_time": None}

    # Set up listeners and snapshot targets on the clip
    clip_listenable = discover_listenable(clip, LISTENER_EXCLUDE)
    clip_slot = track.clip_slots[0]
    cross_song_props = CROSS_MODULE_LISTENERS.get("Song", [])
    cross_slot_props = CROSS_MODULE_LISTENERS.get("ClipSlot", [])
    snapshot_targets = [
        (clip, "Clip", discover_snapshot_props(clip_listenable, "Clip", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
        (song, "Song", cross_song_props),
        (clip_slot, "ClipSlot", cross_slot_props),
    ]
    clip_listeners = setup_listeners(clip, "Clip", clip_listenable, fired, probe_timing, log)
    song_listeners = setup_listeners(song, "Song", cross_song_props, fired, probe_timing, log)
    slot_listeners = setup_listeners(clip_slot, "ClipSlot", cross_slot_props, fired, probe_timing, log)
    yield

    # Switch to session view
    import Live
    Live.Application.get_application().view.show_view("Session")
    yield
    fired.clear()

    # ── Universal properties ──────────────────────────────────────────────────

    for prop, test_val in CLIP_SETTABLE_PROPS:
        if prop in SKIP_UNDO:
            continue
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_property(
            song, clip, "Clip", prop, test_val, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            if e.value is not None:
                results["Clip"]["properties"][prop] = e.value

    # ── Methods ───────────────────────────────────────────────────────────────

    methods = results["Clip"]["methods"]
    orig_quant = song.clip_trigger_quantization

    def _run_method_probe(method, args, check_fn, cleanup_fn=None, *, effect=None, effect_obj=None,
                          obj=None):
        snap, snap_json = snapshot_properties(snapshot_targets)
        gen = probe_method(
            song, "Clip", method, args, check_fn, cleanup_fn, fired, probe_timing,
            snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
            obj=obj if obj is not None else clip,
            effect=effect, effect_obj=effect_obj,
        )
        try:
            while True:
                next(gen)
                yield
        except StopIteration as e:
            return e.value

    # fire — fire the clip (disable quantization for immediate effect)
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    gen = _run_method_probe(
        "fire", [],
        check_fn=lambda: clip.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="Clip.is_playing", effect_obj=clip,
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

    # stop — keep quantization disabled so stop is immediate
    clip.fire()
    yield
    yield  # fire is next_tick
    gen = _run_method_probe(
        "stop", [],
        check_fn=lambda: not clip.is_playing,
        effect="Clip.is_playing", effect_obj=clip,
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

    # set_fire_button_state
    gen = _run_method_probe(
        "set_fire_button_state", [True],
        check_fn=lambda: clip.is_playing,
        cleanup_fn=lambda: song.stop_playing(),
        effect="Clip.is_playing", effect_obj=clip,
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

    # duplicate_loop — doubles the loop content
    orig_loop_end = clip.loop_end
    gen = _run_method_probe(
        "duplicate_loop", [],
        check_fn=lambda: clip.loop_end > orig_loop_end,
        effect="Clip.loop_end", effect_obj=clip,
    )
    r = yield from gen
    if r: methods["duplicate_loop"] = r

    # crop — removes material outside loop
    gen = _run_method_probe(
        "crop", [],
        check_fn=lambda: False,  # hard to check, crop changes start/end markers
        effect="Clip.end_marker", effect_obj=clip,
    )
    r = yield from gen
    if r: methods["crop"] = r

    # move_playing_pos — move the play position within the clip
    # Need clip to be playing first
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    clip.fire()
    yield
    yield
    gen = _run_method_probe(
        "move_playing_pos", [4.0],
        check_fn=lambda: False,  # position changes within clip, not easily observable
    )
    r = yield from gen
    if r: methods["move_playing_pos"] = r
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

    # scrub — scrub playback to a position
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    clip.fire()
    yield
    yield
    gen = _run_method_probe(
        "scrub", [4.0],
        check_fn=lambda: False,
    )
    r = yield from gen
    if r: methods["scrub"] = r
    if song.is_playing:
        song.stop_playing()
        yield
    song.stop_all_clips(False)
    yield
    song.clip_trigger_quantization = orig_quant
    if song.back_to_arranger:
        song.back_to_arranger = False
        yield
    song.current_song_time = 0.0
    yield

    # stop_scrub
    gen = _run_method_probe(
        "stop_scrub", [],
        check_fn=lambda: False,
    )
    r = yield from gen
    if r: methods["stop_scrub"] = r

    # ── MIDI / session clip specific ─────────────────────────────────────────
    log("[probe_clip] Starting MIDI/session-specific probes")

    # is_playing (settable on session clips — starts/stops clip playback)
    song.clip_trigger_quantization = 0  # type: ignore[assignment]
    yield
    snap, snap_json = snapshot_properties(snapshot_targets)
    gen = probe_property(
        song, clip, "Clip", "is_playing", True, fired, probe_timing,
        snap, snap_json, snapshot_targets, SNAPSHOT_EXTRA, log,
    )
    try:
        while True:
            next(gen)
            yield
    except StopIteration as e:
        if e.value is not None:
            results["Clip"]["properties"]["is_playing"] = e.value
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

    # quantize — quantize all notes to grid, check if note positions changed
    notes_before = [n.start_time for n in clip.get_all_notes_extended()]
    gen = _run_method_probe(
        "quantize", [4, 1.0],  # grid=1/16, amount=100%
        check_fn=lambda: [n.start_time for n in clip.get_all_notes_extended()] != notes_before,
    )
    r = yield from gen
    if r: methods["quantize"] = r

    # duplicate_region — duplicate notes in a region, check note count
    note_count_before = len(clip.get_all_notes_extended())
    gen = _run_method_probe(
        "duplicate_region", [0.0, 4.0, clip.loop_end],  # start, length, dest_time
        check_fn=lambda: len(clip.get_all_notes_extended()) > note_count_before,
    )
    r = yield from gen
    if r: methods["duplicate_region"] = r

    # select_all_notes — check via get_selected_notes_extended count
    gen = _run_method_probe(
        "select_all_notes", [],
        check_fn=lambda: len(clip.get_selected_notes_extended()) > 0,
    )
    r = yield from gen
    if r: methods["select_all_notes"] = r

    # deselect_all_notes — select first then deselect
    clip.select_all_notes()
    yield
    gen = _run_method_probe(
        "deselect_all_notes", [],
        check_fn=lambda: len(clip.get_selected_notes_extended()) == 0,
    )
    r = yield from gen
    if r: methods["deselect_all_notes"] = r

    # quantize_pitch — quantize notes of a specific pitch
    # Find a pitch that exists in the clip
    all_notes_qp = clip.get_all_notes_extended()
    qp_pitch = all_notes_qp[0].pitch if len(all_notes_qp) > 0 else 60
    notes_before_qp = [n.start_time for n in all_notes_qp if n.pitch == qp_pitch]
    gen = _run_method_probe(
        "quantize_pitch", [qp_pitch, 4, 1.0],  # grid=1/16, amount=100%
        check_fn=lambda: [n.start_time for n in clip.get_all_notes_extended() if n.pitch == qp_pitch] != notes_before_qp,
    )
    r = yield from gen
    if r: methods["quantize_pitch"] = r

    # add_new_notes — add a note via MidiNoteSpecification
    import Live.Clip
    note_count_before2 = len(clip.get_all_notes_extended())
    spec = Live.Clip.MidiNoteSpecification(pitch=64, start_time=0.0, duration=0.5, velocity=100.0)
    gen = _run_method_probe(
        "add_new_notes", [[spec]],
        check_fn=lambda: len(clip.get_all_notes_extended()) > note_count_before2,
    )
    r = yield from gen
    if r: methods["add_new_notes"] = r

    # set_notes — add notes via legacy tuple format (pitch, time, duration, velocity, muted)
    note_count_before3 = len(clip.get_all_notes_extended())
    gen = _run_method_probe(
        "set_notes", [((62, 0.0, 0.5, 100, False),)],
        check_fn=lambda: len(clip.get_all_notes_extended()) > note_count_before3,
    )
    r = yield from gen
    if r: methods["set_notes"] = r

    # duplicate_notes_by_id — duplicate existing notes by their IDs
    all_notes = clip.get_all_notes_extended()
    if len(all_notes) > 0:
        note_ids = [all_notes[0].note_id]
        note_count_before4 = len(clip.get_all_notes_extended())
        gen = _run_method_probe(
            "duplicate_notes_by_id", [note_ids],
            check_fn=lambda: len(clip.get_all_notes_extended()) > note_count_before4,
        )
        r = yield from gen
        if r: methods["duplicate_notes_by_id"] = r

    # select_notes_by_id — select specific notes by ID
    all_notes = clip.get_all_notes_extended()
    if len(all_notes) > 0:
        note_ids = [all_notes[0].note_id]
        gen = _run_method_probe(
            "select_notes_by_id", [note_ids],
            check_fn=lambda: len(clip.get_selected_notes_extended()) > 0,
        )
        r = yield from gen
        if r: methods["select_notes_by_id"] = r

    # apply_note_modifications — modify existing notes
    all_notes = clip.get_all_notes_extended()
    if len(all_notes) > 0:
        orig_vel = all_notes[0].velocity
        all_notes[0].velocity = 50.0
        gen = _run_method_probe(
            "apply_note_modifications", [all_notes],
            check_fn=lambda: clip.get_all_notes_extended()[0].velocity != orig_vel,
        )
        r = yield from gen
        if r: methods["apply_note_modifications"] = r

    # ── Audio-specific properties ─────────────────────────────────────────────
    # Use track 10 (Vocal Main) slot 1 which has an audio clip
    audio_track = song.tracks[10]
    audio_slot = audio_track.clip_slots[1]
    if audio_slot.has_clip:
        audio_clip = audio_slot.clip
        log(f"[probe_clip] Probing audio-specific properties on {audio_track.name}")

        # Set up listeners on the audio clip (separate from MIDI clip listeners)
        audio_listenable = discover_listenable(audio_clip, LISTENER_EXCLUDE)
        audio_snapshot_targets = [
            (audio_clip, "Clip", discover_snapshot_props(
                audio_listenable, "Clip", LISTENER_EXCLUDE, SNAPSHOT_EXTRA)),
            (song, "Song", cross_song_props),
        ]
        audio_listeners = setup_listeners(audio_clip, "Clip", audio_listenable, fired, probe_timing, log)
        yield

        for prop, test_val in AUDIO_SETTABLE_PROPS:
            snap, snap_json = snapshot_properties(audio_snapshot_targets)
            gen = probe_property(
                song, audio_clip, "Clip", prop, test_val, fired, probe_timing,
                snap, snap_json, audio_snapshot_targets, SNAPSHOT_EXTRA, log,
            )
            try:
                while True:
                    next(gen)
                    yield
            except StopIteration as e:
                if e.value is not None:
                    # Prefix with "audio:" to distinguish from MIDI clip results
                    results["Clip"]["properties"][prop] = e.value

        # warping — special case: undo invalidates the clip reference, so we
        # manually probe and re-fetch from the slot after undo.
        import time as _time
        orig_warping = audio_clip.warping
        test_warping = not orig_warping
        fired.clear()
        probe_timing["target"] = ("Clip", "warping")
        probe_timing["listener_time"] = None

        song.begin_undo_step()
        probe_timing["set_time"] = _time.monotonic()
        audio_clip.warping = test_warping
        song.end_undo_step()

        readback = audio_clip.warping
        is_immediate = readback == test_warping
        yield

        if is_immediate:
            async_vis = "immediate"
        elif audio_clip.warping == test_warping:
            async_vis = "next_tick"
        else:
            async_vis = "no_change"

        latency = None
        if probe_timing["listener_time"] is not None:
            latency = round((probe_timing["listener_time"] - probe_timing["set_time"]) * 1000, 1)

        fired.clear()
        song.undo()
        yield

        # Re-fetch clip after undo (warping undo invalidates the reference)
        audio_clip_after = audio_slot.clip
        undo_worked = audio_clip_after.warping == orig_warping

        warping_result: dict[str, Any] = {
            "from": orig_warping,
            "to": test_warping,
            "async_visibility": async_vis,
            "undo_tracked": undo_worked,
        }
        if latency is not None:
            warping_result["listener_latency_ms"] = latency
        warping_result["notes"] = NOTES.get("Clip.warping", "")
        results["Clip"]["properties"]["warping"] = warping_result

        # Re-set up listeners on the new clip reference for teardown
        teardown_listeners(audio_clip, audio_listeners)
        audio_clip = audio_clip_after
        audio_listeners = setup_listeners(audio_clip, "Clip", audio_listenable, fired, probe_timing, log)
        yield

        teardown_listeners(audio_clip, audio_listeners)
    else:
        log("[probe_clip] No audio clip at track 10 slot 1, skipping audio properties")

    # Tear down listeners
    teardown_listeners(clip, clip_listeners)
    teardown_listeners(song, song_listeners)
    teardown_listeners(clip_slot, slot_listeners)

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
    log(f"[probe_clip] Done — {total_props} properties, {total_methods} methods probed in {elapsed}s")
