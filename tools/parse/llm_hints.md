# Manual Hints for LLM Resolution

These are facts about the Live API that cannot be inferred from the type skeleton, decompiled code,
or MaxForLive docs. Use them to guide your resolutions.

## Domain facts

- Song and Application are root objects that have no parent. Their `canonical_parent` is always None.
- Browser.hotswap_target points to the Device that will be hotswapped.

## Pinned parameter names

Use these exact names for the specified parameters. Do not vary them.

- `Application.has_option` arg2 → `option_name` (the option key looked up in Options.txt)
- `Clip.View.select_envelope_parameter` arg2 → `parameter` (not `device_parameter` — type is already DeviceParameter)
- `Clip.automation_envelope` arg2 → `parameter`
- `Clip.clear_envelope` arg2 → `parameter`
- `Clip.create_automation_envelope` arg2 → `parameter`
- `ClipSlot.create_audio_clip` arg2 → `file_path` (absolute path to audio file)
- `Track.create_audio_clip` arg3 → `time` (arrangement insertion point in beats)
- `Envelope.delete_events_in_range` arg2/arg3 → `start_time` / `end_time`
- `Envelope.events_in_range` arg2/arg3 → `start_time` / `end_time`
- `Envelope.insert_step` arg2 → `start_time`
- `Song.get_current_smpte_song_time` arg2 → `smpte_format` (avoids shadowing Python builtin `format`)
- `MidiMap.forward_midi_cc` arg4 → `cc_no` (CC controller number)
- `MidiMap.map_midi_pitchbend` arg4 → `needs_takeover` (bool preventing value jumps)
- `MidiMap.map_midi_pitchbend_with_feedback_map` arg5 → `needs_takeover`
- `ControlSurfaceProxy.enable_receive_midi` arg2 → `enabled` (adjective for bool state)

## Pinned types

Use these exact types. Do not vary them.

- `ControlSurfaceProxy.send_value` arg2 type → `tuple[int, ...]` (MIDI values are always ints)
- `Clip.remove_notes_by_id` / `select_notes_by_id` / `get_notes_by_id` / `duplicate_notes_by_id` note_ids type
  → `list[int]` (M4L docs specify "list of note IDs")
- `Clip.add_new_notes` arg2 type → `Iterable[MidiNoteSpecification]` (description says "Python iterable")
- `Vector.append` arg2 type → `Any` (Vector is generic; accepts any element type)
- `Licensing.PythonLicensingBridge.get_startup_dialog` authorize_callable → `Callable`
- `Licensing.PythonLicensingBridge.get_startup_dialog` authorize_later_callable → `Callable`
- `Licensing.PythonLicensingBridge.set_network_timer` callback → `Callable | None` (docs say "pass None to stop")
- `Listener.ListenerHandle.listener_func` probed_type → `Callable`
