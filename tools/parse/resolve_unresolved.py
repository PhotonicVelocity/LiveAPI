"""Produce refinements.json from unresolved.json.

Phase 1: Deterministic resolution using hand-curated rules derived from Notes.md.
Phase 2 (future): LLM-assisted resolution for remaining items.

Reads build/{version}/unresolved.json, writes build/{version}/refinements.json.

Usage:
    python tools/parse/resolve_unresolved.py 12.3.6
"""

from __future__ import annotations

import argparse
import json
from os.path import join

# ---------------------------------------------------------------------------
# Hand-curated refinements from Notes.md
# ---------------------------------------------------------------------------

# Arg type overrides: path -> {arg_name: new_type}
_ARG_TYPE_OVERRIDES: dict[str, dict[str, str]] = {
    # Confirmed correct as object — ObjectVector is a generic container for python objects
    "Live.Base.ObjectVector.append": {"arg2": "object"},
    "Live.Base.ObjectVector.extend": {"arg2": "object"},
    # Change to specific type
    "Live.Clip.Clip.add_new_notes": {"arg2": "list[MidiNoteSpecification]"},
    "Live.Clip.Clip.add_warp_marker": {"warp_marker": "WarpMarker"},
    "Live.Clip.Clip.duplicate_notes_by_id": {"note_ids": "list[int]", "destination_time": "float"},
    "Live.Clip.Clip.get_notes_by_id": {"note_ids": "list[int]"},
    "Live.Clip.Clip.remove_notes_by_id": {"arg2": "list[int]"},
    "Live.Clip.Clip.select_notes_by_id": {"arg2": "list[int]"},
    "Live.Song.Song.create_audio_track": {"Index": "int"},
    "Live.Song.Song.create_midi_track": {"Index": "int"},
    # Change to Callable
    "Live.Licensing.PythonLicensingBridge.get_startup_dialog": {
        "authorize_callable": "Callable",
        "authorize_later_callable": "Callable",
    },
    "Live.Licensing.PythonLicensingBridge.set_network_timer": {"callback": "Callable"},
    # Change to Any
    "Live.Song.Song.get_data": {"default_value": "Any"},
    "Live.Song.Song.set_data": {"value": "Any"},
    "Live.Track.Track.get_data": {"default_value": "Any"},
    "Live.Track.Track.set_data": {"value": "Any"},
}

# Return type overrides: path -> new_type
_RETURN_TYPE_OVERRIDES: dict[str, str] = {
    "Live.Song.Song.get_data": "Any",
    "Live.Track.Track.get_data": "Any",
}

# Property type overrides: path -> probed_type
# Inferred from MaxForLive docs, raw_doc descriptions, and sibling probed_type patterns
_PROPERTY_TYPE_OVERRIDES: dict[str, str] = {
    # ControlSurfaceProxy — control_descriptions confirmed via decompiled _MxDCore/ControlSurfaceWrapper.py
    "Live.Application.ControlSurfaceProxy.control_descriptions": "ControlDescriptionVector",
    # ControlSurfaceProxy — pad_layout is "symbol" in M4L docs = str; type_name is clearly str
    "Live.Application.ControlSurfaceProxy.pad_layout": "str",
    "Live.Application.ControlSurfaceProxy.type_name": "str",
    # Text.text — immutable string content
    "Live.Base.Text.text": "str",
    # PythonLicensingBridge — types inferred from raw_doc descriptions
    "Live.Licensing.PythonLicensingBridge.base_product_id": "str",
    "Live.Licensing.PythonLicensingBridge.in_sassafras_mode": "bool",
    "Live.Licensing.PythonLicensingBridge.license_must_match_variant": "bool",
    "Live.Licensing.PythonLicensingBridge.random_number_for_trial_authorization": "int",
    "Live.Licensing.PythonLicensingBridge.set_has_unsaved_changes": "bool",
    # ListenerHandle — types inferred from raw_doc
    "Live.Listener.ListenerHandle.listener_func": "Callable",
    "Live.Listener.ListenerHandle.listener_self": "Any",
    "Live.Listener.ListenerHandle.name": "str",
    # _live_ptr — all other instances probed as int; these just weren't probed
    "Live.LomObject.LomObject._live_ptr": "int",
    "Live.Track.DeviceContainer._live_ptr": "int",
    # is_using_compare_preset_b — all other device subclasses probed as bool
    "Live.MaxDevice.MaxDevice.is_using_compare_preset_b": "bool",
    "Live.PluginDevice.PluginDevice.is_using_compare_preset_b": "bool",
    "Live.RackDevice.RackDevice.is_using_compare_preset_b": "bool",
}

# Arg name overrides: path -> {current_name: new_name}
_ARG_NAME_OVERRIDES: dict[str, dict[str, str]] = {
    # Vector append/extend — arg2 -> value
    "Live.Application.ControlDescriptionVector.append": {"arg2": "value"},
    "Live.Application.ControlDescriptionVector.extend": {"arg2": "value"},
    "Live.Application.UnavailableFeatureVector.append": {"arg2": "value"},
    "Live.Application.UnavailableFeatureVector.extend": {"arg2": "value"},
    "Live.Base.FloatVector.append": {"arg2": "value"},
    "Live.Base.FloatVector.extend": {"arg2": "value"},
    "Live.Base.IntU64Vector.append": {"arg2": "value"},
    "Live.Base.IntU64Vector.extend": {"arg2": "value"},
    "Live.Base.IntVector.append": {"arg2": "value"},
    "Live.Base.IntVector.extend": {"arg2": "value"},
    "Live.Base.ObjectVector.append": {"arg2": "value"},
    "Live.Base.ObjectVector.extend": {"arg2": "value"},
    "Live.Base.StringVector.append": {"arg2": "value"},
    "Live.Base.StringVector.extend": {"arg2": "value"},
    "Live.Base.Vector.append": {"arg2": "value"},
    "Live.Base.Vector.extend": {"arg2": "value"},
    "Live.Browser.BrowserItemVector.append": {"arg2": "value"},
    "Live.Browser.BrowserItemVector.extend": {"arg2": "value"},
    "Live.Clip.MidiNoteVector.append": {"arg2": "value"},
    "Live.Clip.MidiNoteVector.extend": {"arg2": "value"},
    "Live.Clip.WarpMarkerVector.append": {"arg2": "value"},
    "Live.Clip.WarpMarkerVector.extend": {"arg2": "value"},
    "Live.Device.ATimeableValueVector.append": {"arg2": "value"},
    "Live.Device.ATimeableValueVector.extend": {"arg2": "value"},
    "Live.Envelope.EnvelopeEventVector.append": {"arg2": "value"},
    "Live.Envelope.EnvelopeEventVector.extend": {"arg2": "value"},
    "Live.Listener.ListenerVector.append": {"arg2": "value"},
    "Live.Listener.ListenerVector.extend": {"arg2": "value"},
    "Live.Track.RoutingChannelVector.append": {"arg2": "value"},
    "Live.Track.RoutingChannelVector.extend": {"arg2": "value"},
    "Live.Track.RoutingTypeVector.append": {"arg2": "value"},
    "Live.Track.RoutingTypeVector.extend": {"arg2": "value"},
    # Module-level functions
    "Live.Application.encrypt_challenge2": {"arg1": "challenge"},
    "Live.Application.get_random_int": {"arg1": "start", "arg2": "stop"},
    "Live.MidiMap.forward_midi_cc": {
        "arg1": "midi_map_handle",
        "arg2": "midi_channel",
        "arg3": "controller_number",
        "arg4": "controller_value",
    },
    "Live.MidiMap.forward_midi_note": {
        "arg1": "midi_map_handle",
        "arg2": "midi_channel",
        "arg3": "note_number",
        "arg4": "note_velocity",
    },
    "Live.MidiMap.forward_midi_pitchbend": {
        "arg1": "midi_map_handle",
        "arg2": "midi_channel",
        "arg3": "pitchbend_value",
    },
    "Live.MidiMap.map_midi_note": {
        "arg1": "midi_map_handle",
        "arg2": "parameter",
        "arg3": "midi_channel",
        "arg4": "note_number",
    },
    "Live.MidiMap.map_midi_note_with_feedback_map": {
        "arg1": "midi_map_handle",
        "arg2": "parameter",
        "arg3": "midi_channel",
        "arg4": "note_number",
        "arg5": "feedback_rule",
    },
    "Live.MidiMap.map_midi_pitchbend": {
        "arg1": "midi_map_handle",
        "arg2": "parameter",
        "arg3": "midi_channel",
        "arg4": "avoid_takeover",
    },
    "Live.MidiMap.map_midi_pitchbend_with_feedback_map": {
        "arg1": "midi_map_handle",
        "arg2": "parameter",
        "arg3": "midi_channel",
        "arg4": "feedback_rule",
        "arg5": "avoid_takeover",
    },
    "Live.MidiMap.send_feedback_for_parameter": {"arg1": "midi_map_handle", "arg2": "parameter"},
    # Application.View identifier methods
    "Live.Application.Application.View.focus_view": {"arg2": "identifier"},
    "Live.Application.Application.View.hide_view": {"arg2": "identifier"},
    "Live.Application.Application.View.show_view": {"arg2": "identifier"},
    "Live.Application.Application.View.is_view_visible": {"arg2": "identifier"},
    "Live.Application.Application.View.add_is_view_visible_listener": {"arg2": "identifier"},
    "Live.Application.Application.View.is_view_visible_has_listener": {"arg2": "identifier"},
    "Live.Application.Application.View.remove_is_view_visible_listener": {"arg2": "identifier"},
    "Live.Application.Application.View.scroll_view": {"arg2": "direction", "arg3": "identifier", "arg4": "modifier_pressed"},
    "Live.Application.Application.View.zoom_view": {"arg2": "direction", "arg3": "identifier", "arg4": "modifier_pressed"},
    # Fire button state
    "Live.Clip.Clip.set_fire_button_state": {"arg2": "state"},
    "Live.ClipSlot.ClipSlot.set_fire_button_state": {"arg2": "state"},
    "Live.Scene.Scene.set_fire_button_state": {"arg2": "state"},
    # Index-based operations
    "Live.Chain.Chain.delete_device": {"arg2": "index"},
    "Live.Chain.Chain.duplicate_device": {"arg2": "index"},
    "Live.Song.Song.create_scene": {"arg2": "index"},
    "Live.Song.Song.delete_return_track": {"arg2": "index"},
    "Live.Song.Song.delete_scene": {"arg2": "index"},
    "Live.Song.Song.delete_track": {"arg2": "index"},
    "Live.Song.Song.duplicate_scene": {"arg2": "index"},
    "Live.Song.Song.duplicate_track": {"arg2": "index"},
    "Live.Track.Track.delete_device": {"arg2": "index"},
    "Live.Track.Track.duplicate_clip_slot": {"arg2": "index"},
    "Live.Track.Track.duplicate_device": {"arg2": "index"},
    "Live.Application.Application.press_current_dialog_button": {"arg2": "index"},
    "Live.MaxDevice.MaxDevice.get_bank_name": {"arg2": "index"},
    "Live.MaxDevice.MaxDevice.get_bank_parameters": {"arg2": "index"},
    # Clip note operations
    "Live.Clip.Clip.add_new_notes": {"arg2": "notes"},
    "Live.Clip.Clip.remove_notes_by_id": {"arg2": "note_ids"},
    "Live.Clip.Clip.select_notes_by_id": {"arg2": "note_ids"},
    "Live.Clip.Clip.apply_note_modifications": {"arg2": "notes"},
    "Live.Clip.Clip.replace_selected_notes": {"arg2": "notes"},
    "Live.Clip.Clip.set_notes": {"arg2": "notes"},
    "Live.Clip.Clip.remove_notes": {"arg2": "from_time", "arg3": "from_pitch", "arg4": "time_span", "arg5": "pitch_span"},
    "Live.Clip.Clip.quantize": {"arg2": "grid", "arg3": "amount"},
    "Live.Clip.Clip.quantize_pitch": {"arg2": "pitch", "arg3": "grid", "arg4": "amount"},
    # Other methods
    "Live.Application.Application.has_option": {"arg2": "option"},
    "Live.Song.Song.get_current_smpte_song_time": {"arg2": "format"},
    "Live.Application.ControlSurfaceProxy.enable_receive_midi": {"arg2": "enabled"},
    "Live.Application.ControlSurfaceProxy.grab_control": {"arg2": "control_id"},
    "Live.Application.ControlSurfaceProxy.release_control": {"arg2": "control_id"},
    "Live.Application.ControlSurfaceProxy.send_midi": {"arg2": "midi_bytes"},
    "Live.Application.ControlSurfaceProxy.send_value": {"arg2": "values"},
    "Live.Application.ControlSurfaceProxy.subscribe_to_control": {"arg2": "control_id"},
    "Live.Application.ControlSurfaceProxy.unsubscribe_from_control": {"arg2": "control_id"},
    "Live.Browser.Browser.load_item": {"arg2": "item"},
    "Live.Browser.Browser.preview_item": {"arg2": "item"},
    "Live.Browser.Browser.relation_to_hotswap_target": {"arg2": "item"},
    "Live.Clip.Clip.View.select_envelope_parameter": {"arg2": "parameter"},
    "Live.Clip.Clip.automation_envelope": {"arg2": "parameter"},
    "Live.Clip.Clip.clear_envelope": {"arg2": "parameter"},
    "Live.Clip.Clip.create_automation_envelope": {"arg2": "parameter"},
    "Live.Clip.Clip.move_playing_pos": {"arg2": "beats"},
    "Live.ClipSlot.ClipSlot.create_audio_clip": {"arg2": "file_path"},
    "Live.ClipSlot.ClipSlot.create_clip": {"arg2": "length"},
    "Live.ClipSlot.ClipSlot.duplicate_clip_to": {"arg2": "target"},
    "Live.Device.Device.store_chosen_bank": {"arg2": "script_index", "arg3": "bank_index"},
    "Live.DeviceParameter.DeviceParameter.str_for_value": {"arg2": "value"},
    "Live.Envelope.Envelope.delete_events_in_range": {"arg2": "start", "arg3": "end"},
    "Live.Envelope.Envelope.events_in_range": {"arg2": "start", "arg3": "end"},
    "Live.Envelope.Envelope.insert_step": {"arg2": "start", "arg3": "length", "arg4": "value"},
    "Live.Envelope.Envelope.value_at_time": {"arg2": "time"},
    "Live.LooperDevice.LooperDevice.export_to_clip_slot": {"arg2": "target"},
    "Live.MaxDevice.MaxDevice.get_value_item_icons": {"arg2": "parameter"},
    "Live.RackDevice.RackDevice.copy_pad": {"arg2": "source_index", "arg3": "destination_index"},
    "Live.Song.Song.View.select_device": {"arg2": "device"},
    "Live.Song.Song.jump_by": {"arg2": "beats"},
    "Live.Song.Song.scrub_by": {"arg2": "beats"},
    "Live.TakeLane.TakeLane.create_audio_clip": {"arg2": "file_path", "arg3": "start_time"},
    "Live.TakeLane.TakeLane.create_midi_clip": {"arg2": "start_time", "arg3": "length"},
    "Live.Track.Track.create_audio_clip": {"arg2": "file_path", "arg3": "start_time"},
    "Live.Track.Track.create_midi_clip": {"arg2": "start_time", "arg3": "length"},
    "Live.Track.Track.delete_clip": {"arg2": "clip"},
    "Live.Track.Track.jump_in_running_session_clip": {"arg2": "beats"},
    # Base module functions (limited info available, keep arg names as-is where unknown)
    "Live.Base.log": {"arg1": "message"},
    "Live.Base.subst_args": {"arg1": "arg1", "arg2": "arg2", "arg3": "arg3", "arg4": "arg4", "arg5": "arg5"},
}


def resolve(unresolved: dict) -> dict:
    """Apply hand-curated rules to produce refinements."""
    refinements: dict[str, dict] = {}

    for item in unresolved.get("unresolved", []):
        path = item["path"]
        kind = item["kind"]

        if kind == "arg_type":
            arg_name = item["arg_name"]
            overrides = _ARG_TYPE_OVERRIDES.get(path, {})
            if arg_name in overrides:
                ref = refinements.setdefault(path, {})
                args = ref.setdefault("args", {})
                args.setdefault(arg_name, {})["type"] = overrides[arg_name]

        elif kind == "arg_name":
            arg_name = item["arg_name"]
            overrides = _ARG_NAME_OVERRIDES.get(path, {})
            if arg_name in overrides:
                new_name = overrides[arg_name]
                ref = refinements.setdefault(path, {})
                args = ref.setdefault("args", {})
                args.setdefault(arg_name, {})["name"] = new_name

        elif kind == "return_type":
            if path in _RETURN_TYPE_OVERRIDES:
                ref = refinements.setdefault(path, {})
                ref["returns"] = {"type": _RETURN_TYPE_OVERRIDES[path]}

        elif kind == "property_type":
            if path in _PROPERTY_TYPE_OVERRIDES:
                ref = refinements.setdefault(path, {})
                ref["probed_type"] = _PROPERTY_TYPE_OVERRIDES[path]

    return {"version": unresolved.get("version", ""), "refinements": refinements}


def main():
    parser = argparse.ArgumentParser(description="Resolve unresolved types/names into refinements.json")
    parser.add_argument("version", help="Live version (e.g. 12.3.6)")
    parser.add_argument("--input", help="Path to unresolved.json")
    parser.add_argument("--output", help="Path to output refinements.json")
    args = parser.parse_args()

    input_path = args.input or join("build", args.version, "unresolved.json")
    output_path = args.output or join("build", args.version, "refinements.json")

    with open(input_path) as f:
        unresolved = json.load(f)

    result = resolve(unresolved)

    with open(output_path, "w") as f:
        json.dump(result, f, indent=2)

    n = len(result["refinements"])
    print(f"Wrote {n} refinements to {output_path}")

    # Count what was resolved vs left unresolved
    resolved_paths = set()
    for item in unresolved.get("unresolved", []):
        path = item["path"]
        kind = item["kind"]
        if kind == "arg_type" and item["arg_name"] in _ARG_TYPE_OVERRIDES.get(path, {}):
            resolved_paths.add((path, kind, item["arg_name"]))
        elif kind == "arg_name" and item["arg_name"] in _ARG_NAME_OVERRIDES.get(path, {}):
            resolved_paths.add((path, kind, item["arg_name"]))
        elif kind == "return_type" and path in _RETURN_TYPE_OVERRIDES:
            resolved_paths.add((path, kind, ""))
        elif kind == "property_type" and path in _PROPERTY_TYPE_OVERRIDES:
            resolved_paths.add((path, kind, ""))

    total = len(unresolved.get("unresolved", []))
    print(f"Resolved {len(resolved_paths)} of {total} unresolved items")


if __name__ == "__main__":
    main()
