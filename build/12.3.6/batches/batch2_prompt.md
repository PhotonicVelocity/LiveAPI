## Unresolved Items

```json
[
  {
    "path": "Live.Clip.Clip.View.select_envelope_parameter",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "DeviceParameter",
    "description": "Select the given device parameter in the envelope view.",
    "signature": "select_envelope_parameter( (View)arg1, (DeviceParameter)arg2) -> None :",
    "cpp_signature": "void select_envelope_parameter(TPyViewData<AClip>,TPyHandle<ATimeableValue>)"
  },
  {
    "path": "Live.Clip.Clip.add_new_notes",
    "kind": "arg_type",
    "arg_name": "arg2",
    "current_type": "object",
    "description": "Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification\nobjects. The objects will be used to construct new notes in the clip.",
    "signature": "add_new_notes( (Clip)arg1, (object)arg2) -> IntU64Vector :",
    "cpp_signature": "std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> add_new_notes(TPyHandle<AClip>,boost::python::api::object)"
  },
  {
    "path": "Live.Clip.Clip.add_new_notes",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "object",
    "description": "Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification\nobjects. The objects will be used to construct new notes in the clip.",
    "signature": "add_new_notes( (Clip)arg1, (object)arg2) -> IntU64Vector :",
    "cpp_signature": "std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> add_new_notes(TPyHandle<AClip>,boost::python::api::object)"
  },
  {
    "path": "Live.Clip.Clip.add_warp_marker",
    "kind": "arg_type",
    "arg_name": "warp_marker",
    "current_type": "object",
    "description": "Available for AudioClips only.\nAdds the specified warp marker, if possible.",
    "signature": "add_warp_marker( (Clip)self, (object)warp_marker) -> None :",
    "cpp_signature": "void add_warp_marker(TPyHandle<AClip>,boost::python::api::object)"
  },
  {
    "path": "Live.Clip.Clip.apply_note_modifications",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "MidiNoteVector",
    "description": "Expects a list of notes as returned from get_notes_extended. The content\nof the list will be used to modify existing notes in the clip, based on\nmatching note IDs.\nThis function should be used when modifying existing notes, e.g. changing the\nvelocity or start time. The function ensures that per-note events attached to\nthe modified notes are preserved. This is NOT the case when replacing notes\nvia a combination of remove_notes_extended and add_new_notes.\nThe given list can be a subset of the notes in the clip, but it must not\ncontain any notes that are not present in the clip.",
    "signature": "apply_note_modifications( (Clip)arg1, (MidiNoteVector)arg2) -> None :",
    "cpp_signature": "void apply_note_modifications(TPyHandle<AClip>,std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>>)"
  },
  {
    "path": "Live.Clip.Clip.automation_envelope",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "DeviceParameter",
    "description": "Return the envelope for the given parameter.Returns None if the envelope doesn't exist.Returns None for Arrangement clips.Returns None for parameters from a different track.",
    "signature": "automation_envelope( (Clip)arg1, (DeviceParameter)arg2) -> Envelope :",
    "cpp_signature": "TWeakPtr<TPyHandle<AAutomation>> automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)"
  },
  {
    "path": "Live.Clip.Clip.clear_envelope",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "DeviceParameter",
    "description": "Clears the envelope of this clips given parameter.",
    "signature": "clear_envelope( (Clip)arg1, (DeviceParameter)arg2) -> None :",
    "cpp_signature": "void clear_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)"
  },
  {
    "path": "Live.Clip.Clip.create_automation_envelope",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "DeviceParameter",
    "description": "Creates an envelope for a given parameter and returns it.This should only be used if the envelope doesn't exist.Raises an error if the envelope can't be created.",
    "signature": "create_automation_envelope( (Clip)arg1, (DeviceParameter)arg2) -> Envelope :",
    "cpp_signature": "TWeakPtr<TPyHandle<AAutomation>> create_automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)"
  },
  {
    "path": "Live.Clip.Clip.duplicate_notes_by_id",
    "kind": "arg_type",
    "arg_name": "note_ids",
    "current_type": "object",
    "description": "Duplicate all notes matching the given note IDs.\nIf the optional destination_time is not provided, new notes will be inserted\nafter the last selected note. This behavior can be observed when duplicating\nnotes in the Live GUI.\nIf the transposition_amount is specified, the notes in the region will be\ntransposed by the number of semitones.\nRaises an error on audio clips.",
    "signature": "duplicate_notes_by_id( (Clip)self, (object)note_ids [, (object)destination_time=None [, (int)transposition_amount=0]]) -> IntU64Vector :",
    "cpp_signature": "std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> duplicate_notes_by_id(TPyHandle<AClip>,boost::python::api::object [,boost::python::api::object=None [,int=0]])"
  },
  {
    "path": "Live.Clip.Clip.duplicate_notes_by_id",
    "kind": "arg_type",
    "arg_name": "destination_time",
    "current_type": "object",
    "description": "Duplicate all notes matching the given note IDs.\nIf the optional destination_time is not provided, new notes will be inserted\nafter the last selected note. This behavior can be observed when duplicating\nnotes in the Live GUI.\nIf the transposition_amount is specified, the notes in the region will be\ntransposed by the number of semitones.\nRaises an error on audio clips.",
    "signature": "duplicate_notes_by_id( (Clip)self, (object)note_ids [, (object)destination_time=None [, (int)transposition_amount=0]]) -> IntU64Vector :",
    "cpp_signature": "std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> duplicate_notes_by_id(TPyHandle<AClip>,boost::python::api::object [,boost::python::api::object=None [,int=0]])"
  },
  {
    "path": "Live.Clip.Clip.get_notes_by_id",
    "kind": "arg_type",
    "arg_name": "note_ids",
    "current_type": "object",
    "description": "Return a list of MIDI notes matching the given note IDs.",
    "signature": "get_notes_by_id( (Clip)arg1, (object)note_ids) -> MidiNoteVector :",
    "cpp_signature": "std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_notes_by_id(TPyHandle<AClip>,boost::python::api::object)"
  },
  {
    "path": "Live.Clip.Clip.move_playing_pos",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Jump forward or backward by the specified relative amount in beats.\nWill do nothing, if the Clip is not playing.",
    "signature": "move_playing_pos( (Clip)arg1, (float)arg2) -> None :",
    "cpp_signature": "void move_playing_pos(TPyHandle<AClip>,double)"
  },
  {
    "path": "Live.Clip.Clip.quantize",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Quantize all notes in a clip or align warp markers.",
    "signature": "quantize( (Clip)arg1, (int)arg2, (float)arg3) -> None :",
    "cpp_signature": "void quantize(TPyHandle<AClip>,int,float)"
  },
  {
    "path": "Live.Clip.Clip.quantize",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "float",
    "description": "Quantize all notes in a clip or align warp markers.",
    "signature": "quantize( (Clip)arg1, (int)arg2, (float)arg3) -> None :",
    "cpp_signature": "void quantize(TPyHandle<AClip>,int,float)"
  },
  {
    "path": "Live.Clip.Clip.quantize_pitch",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Quantize all the notes of a given pitch. Raises an error on audio clips.",
    "signature": "quantize_pitch( (Clip)arg1, (int)arg2, (int)arg3, (float)arg4) -> None :",
    "cpp_signature": "void quantize_pitch(TPyHandle<AClip>,int,int,float)"
  },
  {
    "path": "Live.Clip.Clip.quantize_pitch",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "int",
    "description": "Quantize all the notes of a given pitch. Raises an error on audio clips.",
    "signature": "quantize_pitch( (Clip)arg1, (int)arg2, (int)arg3, (float)arg4) -> None :",
    "cpp_signature": "void quantize_pitch(TPyHandle<AClip>,int,int,float)"
  },
  {
    "path": "Live.Clip.Clip.quantize_pitch",
    "kind": "arg_name",
    "arg_name": "arg4",
    "current_type": "float",
    "description": "Quantize all the notes of a given pitch. Raises an error on audio clips.",
    "signature": "quantize_pitch( (Clip)arg1, (int)arg2, (int)arg3, (float)arg4) -> None :",
    "cpp_signature": "void quantize_pitch(TPyHandle<AClip>,int,int,float)"
  },
  {
    "path": "Live.Clip.Clip.remove_notes",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Delete all notes starting in the given pitch- and time range.",
    "signature": "remove_notes( (Clip)arg1, (float)arg2, (int)arg3, (float)arg4, (int)arg5) -> None :",
    "cpp_signature": "void remove_notes(TPyHandle<AClip>,double,int,double,int)"
  },
  {
    "path": "Live.Clip.Clip.remove_notes",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "int",
    "description": "Delete all notes starting in the given pitch- and time range.",
    "signature": "remove_notes( (Clip)arg1, (float)arg2, (int)arg3, (float)arg4, (int)arg5) -> None :",
    "cpp_signature": "void remove_notes(TPyHandle<AClip>,double,int,double,int)"
  },
  {
    "path": "Live.Clip.Clip.remove_notes",
    "kind": "arg_name",
    "arg_name": "arg4",
    "current_type": "float",
    "description": "Delete all notes starting in the given pitch- and time range.",
    "signature": "remove_notes( (Clip)arg1, (float)arg2, (int)arg3, (float)arg4, (int)arg5) -> None :",
    "cpp_signature": "void remove_notes(TPyHandle<AClip>,double,int,double,int)"
  },
  {
    "path": "Live.Clip.Clip.remove_notes",
    "kind": "arg_name",
    "arg_name": "arg5",
    "current_type": "int",
    "description": "Delete all notes starting in the given pitch- and time range.",
    "signature": "remove_notes( (Clip)arg1, (float)arg2, (int)arg3, (float)arg4, (int)arg5) -> None :",
    "cpp_signature": "void remove_notes(TPyHandle<AClip>,double,int,double,int)"
  },
  {
    "path": "Live.Clip.Clip.remove_notes_by_id",
    "kind": "arg_type",
    "arg_name": "arg2",
    "current_type": "object",
    "description": "Delete all notes matching the given note IDs.\nThis function should NOT be used to implement modification of existing notes\n(i.e. in combination with add_new_notes), as that leads to loss of per-note\nevents. apply_note_modifications must be used instead for modifying existing\nnotes.",
    "signature": "remove_notes_by_id( (Clip)arg1, (object)arg2) -> None :",
    "cpp_signature": "void remove_notes_by_id(TPyHandle<AClip>,boost::python::api::object)"
  },
  {
    "path": "Live.Clip.Clip.remove_notes_by_id",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "object",
    "description": "Delete all notes matching the given note IDs.\nThis function should NOT be used to implement modification of existing notes\n(i.e. in combination with add_new_notes), as that leads to loss of per-note\nevents. apply_note_modifications must be used instead for modifying existing\nnotes.",
    "signature": "remove_notes_by_id( (Clip)arg1, (object)arg2) -> None :",
    "cpp_signature": "void remove_notes_by_id(TPyHandle<AClip>,boost::python::api::object)"
  },
  {
    "path": "Live.Clip.Clip.replace_selected_notes",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "tuple",
    "description": "Called with a tuple of tuples where each inner tuple represents\na note in the same format as returned by get_selected_notes. The\nnotes described that way will then be used to replace the old selection.",
    "signature": "replace_selected_notes( (Clip)arg1, (tuple)arg2) -> None :",
    "cpp_signature": "void replace_selected_notes(TPyHandle<AClip>,boost::python::tuple)"
  },
  {
    "path": "Live.Clip.Clip.select_notes_by_id",
    "kind": "arg_type",
    "arg_name": "arg2",
    "current_type": "object",
    "description": "Selects all notes matching the given note IDs.",
    "signature": "select_notes_by_id( (Clip)arg1, (object)arg2) -> None :",
    "cpp_signature": "void select_notes_by_id(TPyHandle<AClip>,boost::python::api::object)"
  },
  {
    "path": "Live.Clip.Clip.select_notes_by_id",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "object",
    "description": "Selects all notes matching the given note IDs.",
    "signature": "select_notes_by_id( (Clip)arg1, (object)arg2) -> None :",
    "cpp_signature": "void select_notes_by_id(TPyHandle<AClip>,boost::python::api::object)"
  },
  {
    "path": "Live.Clip.Clip.set_fire_button_state",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "bool",
    "description": "Set the clip's fire button state directly. Supports all launch modes.",
    "signature": "set_fire_button_state( (Clip)arg1, (bool)arg2) -> None :",
    "cpp_signature": "void set_fire_button_state(TPyHandle<AClip>,bool)"
  },
  {
    "path": "Live.Clip.Clip.set_notes",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "tuple",
    "description": "Called with a tuple of tuples where each inner tuple represents\na note in the same format as returned by get_notes. The\nnotes described that way will then be added to the clip.",
    "signature": "set_notes( (Clip)arg1, (tuple)arg2) -> None :",
    "cpp_signature": "void set_notes(TPyHandle<AClip>,boost::python::tuple)"
  },
  {
    "path": "Live.Clip.MidiNoteVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "MidiNote",
    "signature": "append( (MidiNoteVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Clip.MidiNoteVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "MidiNote",
    "signature": "extend( (MidiNoteVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Clip.WarpMarkerVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "WarpMarker",
    "signature": "append( (WarpMarkerVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<NApiHelpers::TWarpMarker, std::__1::allocator<NApiHelpers::TWarpMarker>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Clip.WarpMarkerVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "WarpMarker",
    "signature": "extend( (WarpMarkerVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<NApiHelpers::TWarpMarker, std::__1::allocator<NApiHelpers::TWarpMarker>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.ClipSlot.ClipSlot.create_audio_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "str",
    "description": "Creates an audio clip referencing the file at the given absolute path in the slot.\nThrows an error when called on non-empty slots or slots in non-audio or frozen tracks, or when the path doesn't point at a valid audio file.",
    "signature": "create_audio_clip( (ClipSlot)arg1, (object)arg2) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TPyHandle<AGroupAndClipSlotBase>,TString)"
  },
  {
    "path": "Live.ClipSlot.ClipSlot.create_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Creates an empty clip with the given length in the slot.\nThrows an error when called on non-empty slots or slots in non-MIDI tracks.",
    "signature": "create_clip( (ClipSlot)arg1, (float)arg2) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_clip(TPyHandle<AGroupAndClipSlotBase>,double)"
  },
  {
    "path": "Live.ClipSlot.ClipSlot.duplicate_clip_to",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "ClipSlot",
    "description": "Duplicates the slot's clip to the passed in target slot.\nOverrides the target's clip if it's not empty.\nRaises an exception if the (source) slot itself is empty, or if source and\ntarget have different track types (audio vs. MIDI). Also raises if the source\nor target slot is in a group track (so called group slot).",
    "signature": "duplicate_clip_to( (ClipSlot)arg1, (ClipSlot)arg2) -> None :",
    "cpp_signature": "void duplicate_clip_to(TPyHandle<AGroupAndClipSlotBase>,TPyHandle<AGroupAndClipSlotBase>)"
  },
  {
    "path": "Live.ClipSlot.ClipSlot.set_fire_button_state",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "bool",
    "description": "Set the clipslot's fire button state directly. Supports all launch modes.",
    "signature": "set_fire_button_state( (ClipSlot)arg1, (bool)arg2) -> None :",
    "cpp_signature": "void set_fire_button_state(TPyHandle<AGroupAndClipSlotBase>,bool)"
  },
  {
    "path": "Live.Device.ATimeableValueVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "DeviceParameter",
    "signature": "append( (ATimeableValueVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<TWeakPtr<ATimeableValue>, std::__1::allocator<TWeakPtr<ATimeableValue>>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Device.ATimeableValueVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "DeviceParameter",
    "signature": "extend( (ATimeableValueVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<TWeakPtr<ATimeableValue>, std::__1::allocator<TWeakPtr<ATimeableValue>>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Device.Device.store_chosen_bank",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Set the selected bank in the device for persistency.",
    "signature": "store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :",
    "cpp_signature": "void store_chosen_bank(TPyHandle<ADevice>,int,int)"
  },
  {
    "path": "Live.Device.Device.store_chosen_bank",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "int",
    "description": "Set the selected bank in the device for persistency.",
    "signature": "store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :",
    "cpp_signature": "void store_chosen_bank(TPyHandle<ADevice>,int,int)"
  },
  {
    "path": "Live.DeviceParameter.DeviceParameter.str_for_value",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Return a string representation of the given value. To be used\nfor display purposes only. This value can include characters like 'db' or\n'hz', depending on the type of the parameter.",
    "signature": "str_for_value( (DeviceParameter)arg1, (float)arg2) -> str :",
    "cpp_signature": "TString str_for_value(TPyHandle<ATimeableValue>,float)"
  },
  {
    "path": "Live.Envelope.Envelope.delete_events_in_range",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Deletes the events in the specified time range.",
    "signature": "delete_events_in_range( (Envelope)arg1, (float)arg2, (float)arg3) -> None :",
    "cpp_signature": "void delete_events_in_range(TPyHandle<AAutomation> {lvalue},double,double)"
  },
  {
    "path": "Live.Envelope.Envelope.delete_events_in_range",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "float",
    "description": "Deletes the events in the specified time range.",
    "signature": "delete_events_in_range( (Envelope)arg1, (float)arg2, (float)arg3) -> None :",
    "cpp_signature": "void delete_events_in_range(TPyHandle<AAutomation> {lvalue},double,double)"
  },
  {
    "path": "Live.Envelope.Envelope.events_in_range",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Returns the events in the specified time range.",
    "signature": "events_in_range( (Envelope)arg1, (float)arg2, (float)arg3) -> EnvelopeEventVector :",
    "cpp_signature": "std::__1::vector<NApiHelpers::TEnvelopeEvent, std::__1::allocator<NApiHelpers::TEnvelopeEvent>> events_in_range(TPyHandle<AAutomation> {lvalue},double,double)"
  },
  {
    "path": "Live.Envelope.Envelope.events_in_range",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "float",
    "description": "Returns the events in the specified time range.",
    "signature": "events_in_range( (Envelope)arg1, (float)arg2, (float)arg3) -> EnvelopeEventVector :",
    "cpp_signature": "std::__1::vector<NApiHelpers::TEnvelopeEvent, std::__1::allocator<NApiHelpers::TEnvelopeEvent>> events_in_range(TPyHandle<AAutomation> {lvalue},double,double)"
  },
  {
    "path": "Live.Envelope.Envelope.insert_step",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Given a start time, a step length and a value, creates a step in the envelope.",
    "signature": "insert_step( (Envelope)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :",
    "cpp_signature": "void insert_step(TPyHandle<AAutomation> {lvalue},double,double,double)"
  },
  {
    "path": "Live.Envelope.Envelope.insert_step",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "float",
    "description": "Given a start time, a step length and a value, creates a step in the envelope.",
    "signature": "insert_step( (Envelope)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :",
    "cpp_signature": "void insert_step(TPyHandle<AAutomation> {lvalue},double,double,double)"
  },
  {
    "path": "Live.Envelope.Envelope.insert_step",
    "kind": "arg_name",
    "arg_name": "arg4",
    "current_type": "float",
    "description": "Given a start time, a step length and a value, creates a step in the envelope.",
    "signature": "insert_step( (Envelope)arg1, (float)arg2, (float)arg3, (float)arg4) -> None :",
    "cpp_signature": "void insert_step(TPyHandle<AAutomation> {lvalue},double,double,double)"
  },
  {
    "path": "Live.Envelope.Envelope.value_at_time",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Returns the parameter value at the specified time.",
    "signature": "value_at_time( (Envelope)arg1, (float)arg2) -> float :",
    "cpp_signature": "double value_at_time(TPyHandle<AAutomation> {lvalue},double)"
  },
  {
    "path": "Live.Envelope.EnvelopeEventVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "EnvelopeEvent",
    "signature": "append( (EnvelopeEventVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<NApiHelpers::TEnvelopeEvent, std::__1::allocator<NApiHelpers::TEnvelopeEvent>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Envelope.EnvelopeEventVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "EnvelopeEvent",
    "signature": "extend( (EnvelopeEventVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<NApiHelpers::TEnvelopeEvent, std::__1::allocator<NApiHelpers::TEnvelopeEvent>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Licensing.PythonLicensingBridge.base_product_id",
    "kind": "property_type",
    "current_type": null,
    "raw_doc": "Returns Live's current base product ID."
  },
  {
    "path": "Live.Licensing.PythonLicensingBridge.get_startup_dialog",
    "kind": "arg_type",
    "arg_name": "authorize_callable",
    "current_type": "object",
    "description": "Retrieves an instance of the startup dialog with the passed callables connected to its buttons.",
    "signature": "get_startup_dialog( (PythonLicensingBridge)arg1, (object)authorize_callable, (object)authorize_later_callable) -> StartupDialog :",
    "cpp_signature": "TWeakPtr<AStartupDialog> get_startup_dialog(APythonLicensingBridge {lvalue},boost::python::api::object,boost::python::api::object)"
  },
  {
    "path": "Live.Licensing.PythonLicensingBridge.get_startup_dialog",
    "kind": "arg_type",
    "arg_name": "authorize_later_callable",
    "current_type": "object",
    "description": "Retrieves an instance of the startup dialog with the passed callables connected to its buttons.",
    "signature": "get_startup_dialog( (PythonLicensingBridge)arg1, (object)authorize_callable, (object)authorize_later_callable) -> StartupDialog :",
    "cpp_signature": "TWeakPtr<AStartupDialog> get_startup_dialog(APythonLicensingBridge {lvalue},boost::python::api::object,boost::python::api::object)"
  },
  {
    "path": "Live.Licensing.PythonLicensingBridge.in_sassafras_mode",
    "kind": "property_type",
    "current_type": null
  },
  {
    "path": "Live.Licensing.PythonLicensingBridge.license_must_match_variant",
    "kind": "property_type",
    "current_type": null,
    "raw_doc": "Returns a bool indicating if we require the license information returned by the server to match the variant of Live."
  },
  {
    "path": "Live.Licensing.PythonLicensingBridge.random_number_for_trial_authorization",
    "kind": "property_type",
    "current_type": null,
    "raw_doc": "Returns the integer to send along with the Trial authorization request. This same integer will be checked for in `process_trial_response` (and then changed)."
  },
  {
    "path": "Live.Licensing.PythonLicensingBridge.set_has_unsaved_changes",
    "kind": "property_type",
    "current_type": null,
    "raw_doc": "Returns true if the set has unsaved changes."
  },
  {
    "path": "Live.Licensing.PythonLicensingBridge.set_network_timer",
    "kind": "arg_type",
    "arg_name": "callback",
    "current_type": "object",
    "description": "Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer. If any callback invocation raises an exception, the timer is stopped.",
    "signature": "set_network_timer( (PythonLicensingBridge)arg1, (object)callback, (int)interval_in_ms) -> None :",
    "cpp_signature": "void set_network_timer(APythonLicensingBridge {lvalue},boost::python::api::object,int)"
  },
  {
    "path": "Live.Listener.ListenerHandle.listener_func",
    "kind": "property_type",
    "current_type": null,
    "raw_doc": "Returns the original function"
  },
  {
    "path": "Live.Listener.ListenerHandle.listener_self",
    "kind": "property_type",
    "current_type": null,
    "raw_doc": "Returns the weak reference to original self, if it was a bound method"
  },
  {
    "path": "Live.Listener.ListenerHandle.name",
    "kind": "property_type",
    "current_type": null,
    "raw_doc": "Prints the name of the property that this listener is connected to"
  },
  {
    "path": "Live.Listener.ListenerVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "ListenerHandle",
    "signature": "append( (ListenerVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<TWeakPtr<LPythonRemote>, std::__1::allocator<TWeakPtr<LPythonRemote>>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Listener.ListenerVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "ListenerHandle",
    "signature": "extend( (ListenerVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<TWeakPtr<LPythonRemote>, std::__1::allocator<TWeakPtr<LPythonRemote>>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.LomObject.LomObject._live_ptr",
    "kind": "property_type",
    "current_type": null
  },
  {
    "path": "Live.LooperDevice.LooperDevice.export_to_clip_slot",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "ClipSlot",
    "description": "Export Looper's content to a Session Clip Slot.",
    "signature": "export_to_clip_slot( (LooperDevice)arg1, (ClipSlot)arg2) -> None :",
    "cpp_signature": "void export_to_clip_slot(TLooperDevicePyHandle,TPyHandle<AGroupAndClipSlotBase>)"
  },
  {
    "path": "Live.MaxDevice.MaxDevice.get_bank_name",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Get the name of a parameter bank given by index. This is related to hardware control surfaces.",
    "signature": "get_bank_name( (MaxDevice)arg1, (int)arg2) -> str :",
    "cpp_signature": "TString get_bank_name(TMaxDevicePyHandle,int)"
  },
  {
    "path": "Live.MaxDevice.MaxDevice.get_bank_parameters",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces.",
    "signature": "get_bank_parameters( (MaxDevice)arg1, (int)arg2) -> list :",
    "cpp_signature": "boost::python::list get_bank_parameters(TMaxDevicePyHandle,int)"
  },
  {
    "path": "Live.MaxDevice.MaxDevice.get_value_item_icons",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "DeviceParameter",
    "description": "Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.",
    "signature": "get_value_item_icons( (MaxDevice)arg1, (DeviceParameter)arg2) -> list :",
    "cpp_signature": "boost::python::list get_value_item_icons(TMaxDevicePyHandle,TPyHandle<ATimeableValue>)"
  },
  {
    "path": "Live.MaxDevice.MaxDevice.is_using_compare_preset_b",
    "kind": "property_type",
    "current_type": null,
    "raw_doc": "Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors."
  }
]
```

## MaxForLive Documentation

These are the official Ableton MaxForLive docs for the Live Object Model. Use them to find parameter names, types, and descriptions.

### chainmixerdevice.md

# ChainMixerDevice

This class represents a chain's mixer device in Live.

## Canonical Paths

```
live_set tracks N devices M chains L mixer_device
```

```
live_set tracks N devices M return_chains L mixer_device
```

## Children

### sends list of [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve

[in Audio Effect Racks and Instrument Racks only]   
For Drum Racks, otherwise empty.

### chain_activator [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

### panning [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in Audio Effect Racks and Instrument Racks only]

### volume [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in Audio Effect Racks and Instrument Racks only]


### clip.md

# Clip

This class represents a clip in Live. It can be either an audio clip or a MIDI clip in the Arrangement or Session View, depending on the track / slot it lives in.

## Canonical Paths

```
live_set tracks N clip_slots M clip
```

```
live_set tracks N arrangement_clips M
```

## Children

### view [Clip.View](/apiref/lom/clip_view/ "Clip.View") read-only

## Properties

### available_warp_modes list read-only

Returns the list of indexes of the Warp Modes available for the clip. Only valid for audio clips.

### color int observe

The RGB value of the clip's color in the form `0x00rrggbb` or (2^16 * red) + (2^8) * green + blue, where red, green and blue are values from 0 (dark) to 255 (light).   
  
When setting the RGB value, the nearest color from the clip color chooser is taken.

### color_index int observe

The clip's color index.

### end_marker float observe

The end marker of the clip in beats, independent of the loop state. Cannot be set before the start marker.

### end_time float read-onlyobserve

The end time of the clip. For Session View clips, if Loop is on, this is the Loop End, otherwise it's the End Marker. For Arrangement View clips, this is always the position of the clip's rightmost edge in the Arrangement.

### gain float observe

The gain of the clip (range is 0.0 to 1.0). Only valid for audio clips.

### gain_display_string symbol read-only

Get the gain display value of the clip as a string (e.g. "1.3 dB"). Can only be called on audio clips.

### file_path symbol read-only

Get the location of the audio file represented by the clip. Only available for audio clips.

### groove [Groove](/apiref/lom/groove/ "Groove") observe

Get/set/observe access to the groove associated with this clip.   
  
*Available since Live 11.0.*

### has_envelopes bool read-onlyobserve

Get/observe whether the clip has any automation.

### has_groove bool read-only

Returns true if a groove is associated with this clip.   
  
*Available since Live 11.0.*

### is_session_clip bool read-only

1 = The clip is a Session clip.   
A clip can be either an Arrangement or a Session clip.

### is_arrangement_clip bool read-only

1 = The clip is an Arrangement clip.   
A clip can be either an Arrangement or a Session clip.

### is_take_lane_clip bool read-only

1 = The clip is a Take Lane clip.   
Returns true if the clip is on a Take Lane. Take Lane clips are also Arrangement clips.

### is_audio_clip bool read-only

0 = MIDI clip, 1 = audio clip

### is_midi_clip bool read-only

The opposite of `is_audio_clip`.

### is_overdubbing bool read-onlyobserve

1 = clip is overdubbing.

### is_playing bool

1 = clip is playing or recording.

### is_recording bool read-onlyobserve

1 = clip is recording.

### is_triggered bool read-only

1 = Clip Launch button is blinking.

### launch_mode int observe

The Launch Mode of the Clip as an integer index. Available Launch Modes are:   
0 = Trigger (default)   
1 = Gate   
2 = Toggle   
3 = Repeat   
  
*Available since Live 11.0.*

### launch_quantization int observe

The Launch Quantization of the Clip as an integer index. Available Launch Quantization values are:   
0 = Global (default)   
1 = None   
2 = 8 Bars   
3 = 4 Bars   
4 = 2 Bars   
5 = 1 Bar   
6 = 1/2   
7 = 1/2T   
8 = 1/4   
9 = 1/4T   
10 = 1/8   
11 = 1/8T   
12 = 1/16   
13 = 1/16T   
14 = 1/32   
  
*Available since Live 11.0.*

### legato bool observe

1 = Legato Mode switch in the Clip's Launch settings is on.   
  
*Available since Live 11.0.*

### length float read-only

For looped clips: loop length in beats. Otherwise it's the distance in beats from start to end marker. Makes no sense for unwarped audio clips.

### loop_end float observe

For looped clips: loop end.   
For unlooped clips: clip end.

### loop_jump bang observe

Bangs when the clip play position is crossing the loop start marker (possibly projected into the loop).

### loop_start float observe

For looped clips: loop start.   
For unlooped clips: clip start.   
  
loop_start and loop_end are in absolute clip beat time if clip is MIDI or warped. The 1.1.1 position has beat time 0. If the clip is unwarped audio, they are given in seconds, 0 is the time of the first sample in the audio material.

### looping bool observe

1 = clip is looped. Unwarped audio cannot be looped.

### muted bool observe

1 = muted (i.e. the Clip Activator button of the clip is off).

### name symbol observe

### notes bang observe

Observer sends bang when the list of notes changes.   
Available for MIDI clips only.

### warp_markers dict/bang read-onlyobserve

The Clip's Warp Markers as a dict. Observing this property bangs when the warp_markers change.  
  
The last Warp Marker in the dict is not visible in the Live interface. This hidden marker is used to calculate the BPM of the last segment.   
  
Available for audio clips only.   
  
*Getting is available since Live 11.0.*

### pitch_coarse int observe

Pitch shift in semitones ("Transpose"), -48 ... 48.   
Available for audio clips only.

### pitch_fine float observe

Extra pitch shift in cents ("Detune"), -50 ... 49.   
Available for audio clips only.

### playing_position float read-onlyobserve

Current playing position of the clip.   
  
For MIDI and warped audio clips, the value is given in beats of absolute clip time. The clip's beat time of 0 is where 1 is shown in the bar/beat/16th time scale at the top of the clip view.   
  
For unwarped audio clips, the position is given in seconds, according to the time scale shown at the bottom of the clip view.   
  
Stopped clips have a playing position of 0.

### playing_status bang observe

Observer sends bang when playing/trigger status changes.

### position float read-onlyobserve

Get and set the clip's loop position. The value will always equal loop_start, however setting this property, unlike setting loop_start, preserves the loop length.

### ram_mode bool observe

1 = an audio clip’s RAM switch is enabled.

### sample_length int read-only

Length of the Clip's sample, in samples.

### sample_rate float read-only

Get the Clip's sample rate.

### signature_denominator int observe

### signature_numerator int observe

### start_marker float observe

The start marker of the clip in beats, independent of the loop state. Cannot be set behind the end marker.

### start_time float read-onlyobserve

The start time of the clip, relative to the global song time. The value is in beats.   
  
For Arrangement View clips, this is the offset within the arrangement. For Session View clips, this is the time the clip was started. Note that what is reported is the start_time of the currently playing clip on the track, regardless of which clip.   
  
When a Session View clip's playback position was offset by clicking in its time ruler in the Clip Detail View or moving its start marker, its start_time may be negative. This allows using the start_time as an offset when calculating the clip's current playback position based on the global song time.

### velocity_amount float observe

How much the velocity of the note that triggers the clip affects its volume, 0 = no effect, 1 = full effect.   
  
*Available since Live 11.0.*

### warp_mode int observe

The Warp Mode of the clip as an integer index. Available Warp Modes are:   
0 = Beats Mode   
1 = Tones Mode   
2 = Texture Mode   
3 = Re-Pitch Mode   
4 = Complex Mode   
5 = REX Mode   
6 = Complex Pro Mode   
Available for audio clips only.

### warping bool observe

1 = Warp switch is on.   
Available for audio clips only.   
  
Technical note: Internally, Live will defer the setting of this property. This has the consequence that if you are sequencing API calls from a single event, the actual order of operations may differ from what you'd intuitively expect. Most of the time this should be transparent to you, but if you run into issues, please report them.

### will_record_on_start bool read-only

1 for MIDI clips which are in triggered state, with the track armed and MIDI Arrangement Overdub on.

## Functions

### add_new_notes

Parameter:   
`dictionary`  
Key: `"notes"` [list of note specification dictionaries]   
Note specification dictionaries have the following keys:   
`pitch` : [int] the MIDI note number, 0...127, 60 is C3.   
`start_time` : [float] the note start time in beats of absolute clip time.   
`duration` : [float] the note length in beats.   
`velocity (optional)` : [float] the note velocity, 0 ... 127 *(100 by default)*.   
`mute (optional)` : [bool] 1 = the note is deactivated *(0 by default)*.   
`probability (optional)` : [float] the chance that the note will be played:   
1.0 = the note is always played   
0.0 = the note is never played   
*(1.0 by default)*.   
`velocity_deviation (optional)` : [float] the range of velocity values at which the note can be played:   
0.0 = no deviation; the note will always play at the velocity specified by the *velocity* property   
-127.0 to 127.0 = the note will be assigned a velocity value between *velocity* and *velocity + velocity_deviation*, inclusive; if the resulting range exceeds the limits of MIDI velocity (0 to 127), then it will be clamped within those limits   
*(0.0 by default)*.   
`release_velocity (optional)` : [float] the note release velocity *(64 by default)*.   
Returns a list of note IDs of the added notes.   
  
For MIDI clips only.   
  
*Available since Live 11.0.*

### add_warp_marker

Only available for warped Audio Clips. Adds the specified warp marker, if possible.   
  
The warp marker is specified as a dict which can have a `beat_time` and a `sample_time` key, both associated with float values.   
The `sample_time` key may be omitted; in this case, Live will calculate the appropriate sample time to create a warp marker at the specified beat time without changing the Clip's playback timing, similar to what would happen if you were to double-click in the upper half of the Sample Display in Clip View.   
  
If `sample_time` is specified, certain limitations must be taken into account: \

* The sample time must lie within the range *[0, s]*, where *s* is the sample's length. The `sample_length` Clip property helps with this.
* The sample time must lie between the left and right adjacents markers' respective sample times (this is a logical constraint).
* Within these constraints, there are limitations on the resulting segments' BPM. The allowed BPM range is *[5, 999]*.

### apply_note_modifications

Parameter:   
`dictionary`  
Key: `"notes"` [list of note dictionaries] as returned from `get_notes_extended`.   
The list of note dictionaries passed to the function can be a subset of notes in the clip, but will be ignored if it contains any notes that are not present in the clip.   
  
For MIDI clips only.   
  
*Available since Live 11.0. Replaces modifying notes with remove_notes followed by set_notes.*

### clear_all_envelopes

Removes all automation in the clip.

### clear_envelope

Parameter:   
`device_parameter` [id]   
Removes the automation of the clip for the given parameter.

### crop

Crops the clip: if the clip is looped, the region outside the loop is removed; if it isn't, the region outside the start and end markers.

### deselect_all_notes

Call this before replace_selected_notes if you just want to add some notes.   
Output:   
`deselect_all_notes id 0`  
  
For MIDI clips only.

### duplicate_loop

Makes the loop two times longer by moving loop_end to the right, and duplicates both the notes and the envelopes. If the clip is not looped, the clip start/end range is duplicated. Available for MIDI clips only.

### duplicate_notes_by_id

Parameter:   
`list` of note IDs.   
Or `dictionary`  
Keys:   
`note_ids` [list of note IDs] as returned from `get_notes_extended`  
`destination_time (optional)` [float/int]   
`transposition_amount (optional)` [int]   
Duplicates all notes matching the given note IDs.   
Provided note IDs must be associated with existing notes in the clip. Existing notes can be queried with `get_notes_extended`.   
The selection of notes will be duplicated to *destination_time*, if provided. Otherwise the new notes will be inserted after the last selected note. This behavior can be observed when duplicating notes in the Live GUI.   
If the *transposition_amount* is specified, the duplicated notes will be transposed by the number of semitones.   
Available for MIDI clips only.   
  
*Available since Live 11.1.2*

### duplicate_region

Parameter:   
`region_start` [float/int]   
`region_length` [float/int]   
`destination_time` [float/int]   
`pitch (optional)` [int]   
`transposition_amount (optional)` [int]   
Duplicate the notes in the specified region to the *destination_time*. Only notes of the specified pitch are duplicated or all if *pitch* is -1. If the *transposition_amount* is not 0, the notes in the region will be transposed by the *transpose_amount* of semitones. Available for MIDI clips only.

### fire

Same effect as pressing the Clip Launch button.

### get_all_notes_extended

Parameter:   
`dict (optional)` [dict]   
(See below for a discussion of this argument).   
  
Returns a dictionary of all of the notes in the clip, regardless of where they are positioned with respect to the start/end markers and the loop start/loop end, as a list of note dictionaries. Each note dictionary consists of the following key-value pairs:   
`note_id` : [int] the unique note identifier.   
`pitch` : [int] the MIDI note number, 0...127, 60 is C3.   
`start_time` : [float] the note start time in beats of absolute clip time.   
`duration` : [float] the note length in beats.   
`velocity` : [float] the note velocity, 0 ... 127.   
`mute` : [bool] 1 = the note is deactivated.   
`probability` : [float] the chance that the note will be played:   
1.0 = the note is always played;   
0.0 = the note is never played.   
`velocity_deviation` : [float] the range of velocity values at which the note can be played:   
0.0 = no deviation; the note will always play at the velocity specified by the *velocity* property   
-127.0 to 127.0 = the note will be assigned a velocity value between *velocity* and *velocity + velocity_deviation*, inclusive; if the resulting range exceeds the limits of MIDI velocity (0 to 127), then it will be clamped within those limits.   
`release_velocity` : [float] the note release velocity.   
  
It is possible to optionally provide a single [dict] argument to this function, containing a single key-value pair: the key is "return" and the associated value is a list of the note properties as listed above in the discussion of the returned note dictionaries, e.g. ["note_id", "pitch", "velocity"]. The effect of this will be that the returned note dictionaries will only contain the key-value pairs for the specified properties, which can be useful to improve patch performance when processing large notes dictionaries.   
  
For MIDI clips only.   
  
*Available since Live 11.1*

### get_notes_by_id

Parameter:   
`list` of note IDs.   
  
Provided note IDs must be associated with existing notes in the clip. Existing notes can be queried with `get_notes_extended`.   
  
Returns a dictionary of notes associated with the provided IDs, as a list of note dictionaries. Each note dictionary consists of the following key-value pairs:   
`note_id` : [int] the unique note identifier.   
`pitch` : [int] the MIDI note number, 0...127, 60 is C3.   
`start_time` : [float] the note start time in beats of absolute clip time.   
`duration` : [float] the note length in beats.   
`velocity` : [float] the note velocity, 0 ... 127.   
`mute` : [bool] 1 = the note is deactivated.   
`probability` : [float] the chance that the note will be played:   
1.0 = the note is always played;   
0.0 = the note is never played.   
`velocity_deviation` : [float] the range of velocity values at which the note can be played:   
0.0 = no deviation; the note will always play at the velocity specified by the *velocity* property   
-127.0 to 127.0 = the note will be assigned a velocity value between *velocity* and *velocity + velocity_deviation*, inclusive; if the resulting range exceeds the limits of MIDI velocity (0 to 127), then it will be clamped within those limits.   
`release_velocity` : [float] the note release velocity.   
  
It is possible to optionally provide the argument to this function in the form of a dictionary instead. The dictionary must include the "note_ids" key associated with a list of [int]s, which are the ID values you would like to pass to the function.   
  
If you use this method, you can optionally provide an additional key-value pair: the key is "return" and the associated value is a list of the note properties as listed above in the discussion of the returned note dictionaries, e.g. ["note_id", "pitch", "velocity"]. The effect of this will be that the returned note dictionaries will only contain the key-value pairs for the specified properties, which can be useful to improve patch performance when processing large notes dictionaries.   
  
For MIDI clips only.   
  
*Available since Live 11.0.*

### get_notes_extended

Parameters:   
`from_pitch` [int]   
`pitch_span` [int]   
`from_time` [float]   
`time_span` [float]   
  
`from_time` and `time_span` are given in beats.   
  
Returns a dictionary of notes that have their start times in the given area, as a list of note dictionaries. Each note dictionary consists of the following key-value pairs:   
`note_id` : [int] the unique note identifier.   
`pitch` : [int] the MIDI note number, 0...127, 60 is C3.   
`start_time` : [float] the note start time in beats of absolute clip time.   
`duration` : [float] the note length in beats.   
`velocity` : [float] the note velocity, 0 ... 127.   
`mute` : [bool] 1 = the note is deactivated.   
`probability` : [float] the chance that the note will be played:   
1.0 = the note is always played;   
0.0 = the note is never played.   
`velocity_deviation` : [float] the range of velocity values at which the note can be played:   
0.0 = no deviation; the note will always play at the velocity specified by the *velocity* property   
-127.0 to 127.0 = the note will be assigned a velocity value between *velocity* and *velocity + velocity_deviation*, inclusive; if the resulting range exceeds the limits of MIDI velocity (0 to 127), then it will be clamped within those limits.   
`release_velocity` : [float] the note release velocity.   
  
It is possible to optionally provide the arguments to this function in the form of a single dictionary instead. The dictionary must include all of the parameter names given above as its keys; the associated values are the parameter values you wish to pass to the function.   
  
If you use this method, you can optionally provide an additional key-value pair: the key is "return" and the associated value is a list of the note properties as listed above in the discussion of the returned note dictionaries, e.g. ["note_id", "pitch", "velocity"]. The effect of this will be that the returned note dictionaries will only contain the key-value pairs for the specified properties, which can be useful to improve patch performance when processing large notes dictionaries.   
  
For MIDI clips only.   
  
*Available since Live 11.0. Replaces get_notes.*

### get_selected_notes_extended

Parameter:   
`dict (optional)` [dict]   
(See below for a discussion of this argument).   
  
Returns a dictionary of the selected notes in the clip, as a list of note dictionaries. Each note dictionary consists of the following key-value pairs:   
`note_id` : [int] the unique note identifier.   
`pitch` : [int] the MIDI note number, 0...127, 60 is C3.   
`start_time` : [float] the note start time in beats of absolute clip time.   
`duration` : [float] the note length in beats.   
`velocity` : [float] the note velocity, 0 ... 127.   
`mute` : [bool] 1 = the note is deactivated.   
`probability` : [float] the chance that the note will be played:   
1.0 = the note is always played;   
0.0 = the note is never played.   
`velocity_deviation` : [float] the range of velocity values at which the note can be played:   
0.0 = no deviation; the note will always play at the velocity specified by the *velocity* property   
-127.0 to 127.0 = the note will be assigned a velocity value between *velocity* and *velocity + velocity_deviation*, inclusive; if the resulting range exceeds the limits of MIDI velocity (0 to 127), then it will be clamped within those limits.   
`release_velocity` : [float] the note release velocity.   
  
It is possible to optionally provide a single [dict] argument to this function, containing a single key-value pair: the key is "return" and the associated value is a list of the note properties as listed above in the discussion of the returned note dictionaries, e.g. ["note_id", "pitch", "velocity"]. The effect of this will be that the returned note dictionaries will only contain the key-value pairs for the specified properties, which can be useful to improve patch performance when processing large notes dictionaries.   
  
For MIDI clips only.   
  
*Available since Live 11.0. Replaces get_selected_notes.*

### move_playing_pos

Parameter: `beats`  
`beats` [float] relative jump distance in beats. Negative beats jump backwards.   
Jumps by given amount, unquantized.   
Unwarped audio clips, recording audio clips and recording non-overdub MIDI clips cannot jump.

### move_warp_marker

Parameters: `beat_time` [float]   
`beat_time_distance` [float]   
Moves the warp marker specified by *beat_time* the specified beat time distance.

### quantize

Parameter:   
`quantization_grid` [int]   
`amount` [float]   
Quantizes all notes in the clip to the quantization_grid taking the song's swing_amount into account.

### quantize_pitch

Parameter:   
`pitch` [int]   
`quantization_grid` [int]   
`amount` [float]   
Same as *quantize*, but only for notes in the given pitch.

### remove_notes_by_id

Parameter:   
`list` of note IDs.   
Deletes all notes associated with the provided IDs.   
Provided note IDs must be associated with existing notes in the clip. Existing notes can be queried with `get_notes_extended`.   
  
*Available since Live 11.0.*

### remove_notes_extended

Parameter:   
`from_pitch` [int]   
`pitch_span` [int]   
`from_time` [float]   
`time_span` [float]   
Deletes all notes that start in the given area. `from_time` and `time_span` are given in beats.   
  
*Available since Live 11.0. Replaces remove_notes.*

### remove_warp_marker

Parameter: `beat_time` [float]   
Removes the warp marker at the given beat time.

### scrub

Parameter: `beat_time` [float]   
Scrub the clip to a time, specified in beats. This behaves exactly like scrubbing with the mouse; the scrub will respect Global Quantization, starting and looping in time with the transport. The scrub will continue until stop_scrub() is called.

### select_all_notes

Use this function to process all notes of a clip, independent of the current selection.   
  
Output:   
`select_all_notes id 0`  
  
For MIDI clips only.

### select_notes_by_id

Parameter:   
`list` of note IDs.   
Selects all notes associated with the provided IDs.   
  
Note that this function will *not* print a warning or error if the list contains nonexistent IDs.   
  
*Available since Live 11.0.6*

### set_fire_button_state

Parameter: `state` [bool]   
If the state is set to 1, Live simulates pressing the clip start button until the state is set to 0, or until the clip is otherwise stopped.

### stop

Same effect as pressing the stop button of the track, but only if this clip is actually playing or recording. If this clip is triggered or if another clip in this track is playing, it has no effect.

### stop_scrub

Stops an active scrub on a clip.


### clip_view.md

# Clip.View

Representing the view aspects of a Clip.

## Canonical Path

```
live_set tracks N clip_slots M clip view
```

## Properties

### grid_is_triplet bool

Get/set whether the clip is displayed with a triplet grid.

### grid_quantization int

Get/set the grid quantization.

## Functions

### hide_envelope

Hide the Envelopes box.

### select_envelope_parameter

Parameter: [DeviceParameter]   
Select the specified device parameter in the Envelopes box.

### show_envelope

Show the Envelopes box.

### show_loop

If the clip is visible in Live's Detail View, this function will make the current loop visible there.


### clipslot.md

# ClipSlot

This class represents an entry in Live's Session View matrix.   
  
The properties `playing_status`, `is_playing` and `is_recording` are useful for clip slots of Group Tracks. These are always empty and represent the state of the clips in the tracks within the Group Track.

## Canonical Path

```
live_set tracks N clip_slots M
```

## Children

### clip [Clip](/apiref/lom/clip/ "Clip") read-only

`id 0` if slot is empty

## Properties

### color long read-onlyobserve

The color of the first clip in the Group Track if the clip slot is a Group Track slot.

### color_index long read-onlyobserve

The color index of the first clip in the Group Track if the clip slot is a Group Track slot.

### controls_other_clips bool read-onlyobserve

1 for a Group Track slot that has non-deactivated clips in the tracks within its group.   
Control of empty clip slots doesn't count.

### has_clip bool read-onlyobserve

1 = a clip exists in this clip slot.

### has_stop_button bool observe

1 = this clip stops its track (or tracks within a Group Track).

### is_group_slot bool read-only

1 = this clip slot is a Group Track slot.

### is_playing bool read-only

1 = playing_status != 0, otherwise 0.

### is_recording bool read-only

1 = playing_status == 2, otherwise 0.

### is_triggered bool read-onlyobserve

1 = clip slot button (Clip Launch, Clip Stop or Clip Record) or button of contained clip are blinking.

### playing_status int read-onlyobserve

0 = all clips in tracks within a Group Track stopped or all tracks within a Group Track are empty.   
1 = at least one clip in a track within a Group Track is playing.   
2 = at least one clip in a track within a Group Track is playing or recording.   
Equals 0 if this is not a clip slot of a Group Track.

### will_record_on_start bool read-only

1 = clip slot will record on start.

## Functions

### create_audio_clip

Parameter: `path`  
Given an absolute path to a valid audio file in a supported format, creates an audio clip that references the file in the clip slot. Throws an error if the clip slot doesn't belong to an audio track or if the track is frozen.

### create_clip

Parameter: `length`  
Length is given in beats and must be a greater value than 0.0. Can only be called on empty clip slots in MIDI tracks.

### delete_clip

Deletes the contained clip.

### duplicate_clip_to

Parameter: `target_clip_slot` [ClipSlot]   
Duplicates the slot's clip to the given clip slot, overriding the target clip slot's clip if it's not empty.

### fire

Parameter: `record_length (optional)`  
`launch_quantization (optional)`  
Fires the clip or triggers the Stop Button, if any. Starts recording if slot is empty and track is armed. Starts recording of armed and empty tracks within a Group Track if Preferences->Launch->Start Recording on Scene Launch is ON. If *record_length* is provided, the slot will record for the given length in beats. *launch_quantization* overrides the global quantization if provided.

### set_fire_button_state

Parameter: `state` [bool]   
1 = Live simulates pressing of Clip Launch button until the state is set to 0 or until the slot is stopped otherwise.

### stop

Stops playing or recording clips in this track or the tracks within the group, if any. It doesn't matter on which slot of the track you call this function.


### compressordevice.md

# CompressorDevice

This class represents a Compressor device in Live.   
A CompressorDevice shares all of the children, functions and properties of a Device; listed below are the members unique to it.

## Properties

### available_input_routing_channels dict read-onlyobserve

The list of available source channels for the compressor's input routing in the sidechain. It's represented as a dictionary with the following key:   
`available_input_routing_channels` [list]   
The list contains dictionaries as described in *input_routing_channel*.

### available_input_routing_types dict read-onlyobserve

The list of available source types for the compressor's input routing in the sidechain. It's represented as a dictionary with the following key:   
`available_input_routing_types` [list]   
The list contains dictionaries as described in *input_routing_type*.

### input_routing_channel dict observe

The currently selected source channel for the compressor's input routing in the sidechain. It's represented as a dictionary with the following keys:   
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the compressor's *available_input_routing_channels*.

### input_routing_type dict observe

The currently selected source type for the compressor's input routing in the sidechain. It's represented as a dictionary with the following keys:   
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_input_routing_types*.


### device.md

# Device

This class represents a MIDI or audio device in Live.

## Canonical Paths

```
live_set tracks N devices M
```

```
live_set tracks N devices M chains L devices K
```

```
live_set tracks N devices M return_chains L devices K
```

## Children

### parameters list of [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve

Only automatable parameters are accessible. See [DeviceParameter](#DeviceParameter) to learn how to modify them.

### view [Device.View](/apiref/lom/device_view/ "Device.View") read-only

## Properties

### can_have_chains bool read-only

0 for a single device   
1 for a device Rack

### can_have_drum_pads bool read-only

1 for Drum Racks

### class_display_name symbol read-only

Get the original name of the device (e.g. `Operator`, `Auto Filter`).

### class_name symbol read-only

Live device type such as `MidiChord`, `Operator`, `Limiter`, `MxDeviceAudioEffect`, or `PluginDevice`.

### is_active bool read-onlyobserve

0 = either the device itself or its enclosing Rack device is off.

### name symbol observe

This is the string shown in the title bar of the device.

### type int read-only

The type of the device. Possible types are: 0 = undefined, 1 = instrument, 2 = audio_effect, 4 = midi_effect.

### latency_in_samples int read-onlyobserve

Device latency in samples.

### latency_in_ms float read-onlyobserve

Device latency in milliseconds.

### can_compare_ab bool read-only

1 for devices that support the AB Compare feature. 0 otherwise.   
  
*Available since Live 12.3.*

### is_using_compare_preset_b bool observe

1 if the device has compare preset B loaded. 0 otherwise.   
(Only relevant if *can_compare_ab*, otherwise errors.)   
  
*Available since Live 12.3.*

## Functions

### store_chosen_bank

Parameters:   
`script_index` [int]   
`bank_index` [int]   
(This is related to hardware control surfaces and is usually not relevant.)

### save_preset_to_compare_ab_slot

Save the device state to the other compare AB slot.   
(Only relevant if *can_compare_ab*, otherwise errors.)   
  
*Available since Live 12.3.*


### device_view.md

# Device.View

Representing the view aspects of a Device.

## Canonical Paths

```
live_set tracks N devices M view
```

```
live_set tracks N devices M chains L devices K view
```

```
live_set tracks N devices M return_chains L devices K view
```

## Properties

### is_collapsed bool observe

1 = the device is shown collapsed in the device chain.


### deviceio.md

# DeviceIO

This class represents an input or output bus of a Live device.

## Properties

### available_routing_channels dictionary read-onlyobserve

The available channels for this input/output bus. The channels are represented as a *dictionary* with the following key:   
`available_routing_channels` [list]   
The list contains *dictionaries* as described in *routing_channel*.

### available_routing_types dictionary read-onlyobserve

The available types for this input/output bus. The types are represented as a *dictionary* with the following key:   
`available_routing_types` [list]   
The list contains *dictionaries* as described in *routing_type*.

### default_external_routing_channel_is_none bool

1 = the default routing channel for External routing types is none.   
  
*Available since Live 11.0.*

### routing_channel dictionary observe

The current routing channel for this input/output bus. It is represented as a *dictionary* with the following keys:   
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to any of the values found in *available_routing_channels.*

### routing_type dictionary observe

The current routing type for this input/output bus. It is represented as a *dictionary* with the following keys:   
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to any of the values found in *available_routing_types.*


### deviceparameter.md

# DeviceParameter

This class represents an (automatable) parameter within a MIDI or audio device. To modify a device parameter, set its `value` property or send its object ID to [live.remote~](/reference/live.remote~ "live.remote~").

## Canonical Path

```
live_set tracks N devices M parameters L
```

## Properties

### automation_state int read-onlyobserve

Get the automation state of the parameter.   
0 = no automation.   
1 = automation active.   
2 = automation overridden.

### default_value float read-only

Get the default value for this parameter.   
Only available for parameters that aren't quantized (see *is_quantized*).

### is_enabled bool read-only

1 = the parameter value can be modified directly by the user, by sending `set` to a [live.object](/reference/live.object "live.object"), by automation or by an assigned MIDI message or keystroke.   
Parameters can be disabled because they are macro-controlled, or they are controlled by a live-remote~ object, or because Live thinks that they should not be moved.

### is_quantized bool read-only

1 for booleans and enums   
0 for int/float parameters   
Although parameters like MidiPitch.Pitch appear quantized to the user, they actually have an is_quantized value of 0.

### max float read-only

Largest allowed value.

### min float read-only

Lowest allowed value.

### name symbol read-only

The short parameter name as shown in the (closed) automation chooser.

### original_name symbol read-only

The name of a Macro parameter before its assignment.

### state int read-onlyobserve

The active state of the parameter.   
0 = the parameter is active and can be changed.   
1 = the parameter can be changed but isn't active, so changes won't have an audible effect.   
2 = the parameter cannot be changed.

### value float observe

The internal value between min and max. Use display_value for the value as visible in the GUI.

### display_value float observe

The value as visible in the GUI.

### value_items StringVector read-only

Get a list of the possible values for this parameter.   
Only available for parameters that are quantized (see *is_quantized*).

## Functions

### re_enable_automation

Re-enable automation for this parameter.

### str_for_value

Parameter: `value` [float] Returns: [symbol] String representation of the specified value.

### __str__

Returns: [symbol] String representation of the current parameter value.


### driftdevice.md

# DriftDevice

This class represents an instance of a Drift device in Live.   
A DriftDevice has all the properties, functions and children of a Device.

## Properties

### mod_matrix_filter_source_1_index int observe

The index of the available sources for modulating the Filter Frequency for the first modulation slot.

### mod_matrix_filter_source_1_list StringVector read-only

The list of the available sources for modulating the Filter Frequency for the first modulation slot.

### mod_matrix_filter_source_2_index int observe

The index of the available sources for modulating the Filter Frequency for the second modulation slot.

### mod_matrix_filter_source_2_list StringVector read-only

The list of the available sources for modulating the Filter Frequency for the second modulation slot.

### mod_matrix_lfo_source_index int observe

The index of the available sources for modulating the LFO Amount.

### mod_matrix_lfo_source_list StringVector read-only

The list of the available sources for modulating the LFO Amount.

### mod_matrix_pitch_source_1_index int observe

The index of the available sources for modulating the Pitch for the first modulation slot.

### mod_matrix_pitch_source_1_list StringVector read-only

The list of the available sources for modulating the Pitch for the first modulation slot.

### mod_matrix_pitch_source_2_index int observe

The index of the available sources for modulating the Pitch for the second modulation slot.

### mod_matrix_pitch_source_2_list StringVector read-only

The list of the available sources for modulating the Pitch for the second modulation slot.

### mod_matrix_shape_source_index int observe

The index of the available sources for modulating Shape.

### mod_matrix_shape_source_list StringVector read-only

The list of the available sources for modulating Shape.

### mod_matrix_source_1_index int observe

The index of the available sources for the first custom modulation slot.

### mod_matrix_source_1_list StringVector read-only

The list of the available sources for the first custom modulation slot.

### mod_matrix_source_2_index int observe

The index of the available sources for the second custom modulation slot.

### mod_matrix_source_2_list StringVector read-only

The list of the available sources for the second custom modulation slot.

### mod_matrix_source_3_index int observe

The index of the available sources for the third custom modulation slot.

### mod_matrix_source_3_list StringVector read-only

The list of the available sources for the third custom modulation slot.

### mod_matrix_target_1_index int observe

The index of the available targets for the first custom modulation slot.

### mod_matrix_target_1_list StringVector read-only

The list of the available targets for the first custom modulation slot.

### mod_matrix_target_2_index int observe

The index of the available targets for the second custom modulation slot.

### mod_matrix_target_2_list StringVector read-only

The list of the available targets for the second custom modulation slot.

### mod_matrix_target_3_index int observe

The index of the available targets for the third custom modulation slot.

### mod_matrix_target_3_list StringVector read-only

The list of the available targets for the third custom modulation slot.

### pitch_bend_range int observe

The amount for the MIDI Pitch Bend range in semitones.

### voice_count_index int observe

The index of the voice count parameter.

### voice_count_list StringVector read-only

The list of available voice count settings.

### voice_mode_index int observe

The index of the voice mode utilized by Drift.

### voice_mode_list StringVector read-only

The list of available voice modes.


### drumcelldevice.md

# DrumCellDevice

This class represents an instance of a Drum Sampler device in Live.   
A DrumCell has all the properties, functions and children of a Device. Listed below are members unique to DrumCell Device.

## Properties

### gain float observe

The sample gain, as normalized value.


### eq8device.md

# Eq8Device

This class represents an instance of an EQ Eight device in Live.   
An Eq8Device has all the properties, functions and children of a Device. Listed below are members unique to Eq8Device.

## Properties

### edit_mode bool observe

Access to EQ Eight's edit mode, which toggles the channel currently available for editing. The available edit modes depend on the global mode (see `global_mode`) and are encoded as follows:   
  
In L/R mode: 0 = L, 1 = R   
In M/S mode: 0 = M, 1 = S   
In Stereo mode: 0 = A, 1 = B (inactive)

### global_mode int observe

Access to EQ Eight's global mode. The modes are encoded as follows:   
  
0 = Stereo   
1 = L/R   
2 = M/S

### oversample bool observe

Access to EQ Eight's Oversampling parameter. 0 = Off, 1 = On.


### eq8device_view.md

# Eq8Device.View

Represents the view aspects of an Eq8Device.   
An Eq8Device.View has all the children, properties and functions of a Device.View. Listed below are members unique to it.

## Properties

### selected_band int observe

The index of the currently selected filter band.


### hybridreverbdevice.md

# HybridReverbDevice

This class represents an instance of a Hybrid Reverb device in Live.   
A HybridReverbDevice has all the properties, functions and children of a Device. Listed below are members unique to HybridReverbDevice.

## Properties

### ir_attack_time float observe

The attack time of the amplitude envelope for the impulse response, in seconds.

### ir_category_index int observe

The index of the selected impulse response category.

### ir_category_list StringVector read-only

The list of impulse response categories.

### ir_decay_time float observe

The decay time of the amplitude envelope for the impulse response, in seconds.

### ir_file_index int observe

The index of the selected impulse response files from the current category.

### ir_file_list StringVector read-onlyobserve

The list of impulse response files from the selected category.

### ir_size_factor float observe

The relative size of the impulse response, 0.0 to 1.0.

### ir_time_shaping_on bool observe

Enables transforming the current selected impulse response with an amplitude envelope and size parameter.   
1 = enabled.


### lom.md

# LOM - The Live Object Model

*Objects which comprise the Live API described by their structure, properties and functions.*
The Live Object Model lists a number of Live object classes with their properties and functions, as well as their parent-child relations through which a hierarchy is formed. Please refer to the [Live API overview chapter](/userguide/m4l/live_api/)for definitions of the basic Live API terms and a list of the Max objects used to access it.   
  
*This document refers to Ableton Live version 12.3b9*

## Object Model Overview

| *Click on the classes to navigate to their description.* |
| --- |

Expand

## API Objects

| Item | Description |
| --- | --- |
| [Application](/apiref/lom/application/) | This class represents the Live application. It is reachable by the root path live_app ... |
| [Application.View](/apiref/lom/application_view/) | This class represents the aspects of the Live application related to viewing the application.... |
| [Chain](/apiref/lom/chain/) | This class represents a group device chain in Live. |
| [ChainMixerDevice](/apiref/lom/chainmixerdevice/) | This class represents a chain's mixer device in Live. |
| [Clip](/apiref/lom/clip/) | This class represents a clip in Live. It can be either an audio clip or a MIDI clip in the Arr... |
| [Clip.View](/apiref/lom/clip_view/) | Representing the view aspects of a Clip. |
| [ClipSlot](/apiref/lom/clipslot/) | This class represents an entry in Live's Session View matrix. The properties ... |
| [CompressorDevice](/apiref/lom/compressordevice/) | This class represents a Compressor device in Live. A CompressorDevice shares all of the ch... |
| [ControlSurface](/apiref/lom/controlsurface/) | A ControlSurface can be reached either directly by the root path control_surfaces N or by g... |
| [CuePoint](/apiref/lom/cuepoint/) | Represents a locator in the Arrangement View. |
| [Device](/apiref/lom/device/) | This class represents a MIDI or audio device in Live. |
| [Device.View](/apiref/lom/device_view/) | Representing the view aspects of a Device. |
| [DeviceIO](/apiref/lom/deviceio/) | This class represents an input or output bus of a Live device. |
| [DeviceParameter](/apiref/lom/deviceparameter/) | This class represents an (automatable) parameter within a MIDI or audio device. To modify a de... |
| [DriftDevice](/apiref/lom/driftdevice/) | This class represents an instance of a Drift device in Live. A DriftDevice has all the... |
| [DrumCellDevice](/apiref/lom/drumcelldevice/) | This class represents an instance of a Drum Sampler device in Live. A DrumCell has all... |
| [DrumChain](/apiref/lom/drumchain/) | This class represents a Drum Rack device chain in Live. A DrumChain is a type ... |
| [DrumPad](/apiref/lom/drumpad/) | This class represents a Drum Rack pad in Live. |
| [Eq8Device](/apiref/lom/eq8device/) | This class represents an instance of an EQ Eight device in Live. An Eq8Device has all ... |
| [Eq8Device.View](/apiref/lom/eq8device_view/) | Represents the view aspects of an Eq8Device. An Eq8Device.View has all the children, p... |
| [Groove](/apiref/lom/groove/) | This class represents a groove in Live. Available since Live 11.0. ... |
| [GroovePool](/apiref/lom/groovepool/) | This class represents the groove pool in Live. It provides access to the current set's list of groov... |
| [HybridReverbDevice](/apiref/lom/hybridreverbdevice/) | This class represents an instance of a Hybrid Reverb device in Live. A HybridReverbDev... |
| [LooperDevice](/apiref/lom/looperdevice/) | This class represents an instance of a Looper device in Live. An LooperDevice has all ... |
| [MaxDevice](/apiref/lom/maxdevice/) | This class represents a Max for Live device in Live. A MaxDevice is a type of Device... |
| [MeldDevice](/apiref/lom/melddevice/) | This class represents an instance of a Meld device in Live. A MeldDevice has all the p... |
| [MixerDevice](/apiref/lom/mixerdevice/) | This class represents a mixer device in Live. It provides access to volume, panning and other ... |
| [PluginDevice](/apiref/lom/plugindevice/) | This class represents a plug-in device. A PluginDevice is a type of Device, meaning ... |
| [RackDevice](/apiref/lom/rackdevice/) | This class represents a Live Rack Device. A RackDevice is a type of Device, meaning th... |
| [RackDevice.View](/apiref/lom/rackdevice_view/) | Represents the view aspects of a Rack Device. A RackDevice.View is a type of Device.Vi... |
| [RoarDevice](/apiref/lom/roardevice/) | This class represents an instance of a Roar device in Live. A RoarDevice has all the p... |
| [Sample](/apiref/lom/sample/) | This class represents a sample file loaded into Simpler. |
| [Scene](/apiref/lom/scene/) | This class represents a series of clip slots in Live's Session View matrix.... |
| [ShifterDevice](/apiref/lom/shifterdevice/) | This class represents an instance of the Shifter audio effect. A ShifterDevice is a ty... |
| [SimplerDevice](/apiref/lom/simplerdevice/) | This class represents an instance of Simpler. A SimplerDevice is a type of device, mea... |
| [SimplerDevice.View](/apiref/lom/simplerdevice_view/) | Represents the view aspects of a SimplerDevice. A SimplerDevice.View is a type of Device.V... |
| [Song](/apiref/lom/song/) | This class represents a Live Set. The current Live Set is reachable by the root path li... |
| [Song.View](/apiref/lom/song_view/) | This class represents the view aspects of a Live document: the Session and Arrangement Views.... |
| [SpectralResonatorDevice](/apiref/lom/spectralresonatordevice/) | This class represents an instance of a Spectral Resonator device in Live. An SpectralR... |
| [TakeLane](/apiref/lom/takelane/) | This class represents a take lane in Live. Tracks in Live can have take lanes in Arrangement View, w... |
| [this_device](/apiref/lom/this_device/) | This root path represents the device containing the live.path object to which the ... |
| [Track](/apiref/lom/track/) | This class represents a track in Live. It can either be an audio track, a MIDI track, a return... |
| [Track.View](/apiref/lom/track_view/) | Representing the view aspects of a track. |
| [TuningSystem](/apiref/lom/tuningsystem/) | This class represents a tuning system in Live. |
| [WavetableDevice](/apiref/lom/wavetabledevice/) | This class represents a Wavetable instrument. A WavetableDevice shares all of the ch... |


### looperdevice.md

# LooperDevice

This class represents an instance of a Looper device in Live.   
An LooperDevice has all the properties, functions and children of a Device. Listed below are members unique to LooperDevice.

## Properties

### loop_length float read-onlyobserve

The length of Looper's buffer.

### overdub_after_record bool observe

1 = Looper will switch to overdub after recording, when recording a fixed number of bars. 0 = switch to playback without overdubbing.

### record_length_index int observe

Access to the Record Length chooser entry index.

### record_length_list StringVector read-only

Access to the list of Record Length chooser entry strings.

### tempo float read-onlyobserve

The tempo of Looper's buffer.

## Functions

### clear

Erase Looper's recorded content.

### double_speed

Double the speed of Looper's playback.

### half_speed

Halve the speed of Looper's playback.

### double_length

Double the length of Looper's buffer.

### half_length

Halve the length of Looper's buffer.

### record

Record incoming audio.

### overdub

Play back while adding additional layers of incoming audio.

### play

Play back without overdubbing.

### stop

Stop Looper's playback.

### undo

Erase everything that was recorded since the last time Overdub was enabled. Calling a second time will restore the material erased by the previous undo operation.

### export_to_clip_slot

Parameter: `clip_slot` [ClipSlot]   
The target clip slot.   
  
Given a valid LOM ID of an empty clip slot on a non-frozen audio track, will export Looper's content to a clip in that slot. This is similar to using the Drag Me! control on the Looper device, and the same restrictions apply: the audio engine must be turned on, the Looper must actually hold audio content, the content must have a fixed length (i.e. Looper must not be recording), etc.


### maxdevice.md

# MaxDevice

This class represents a Max for Live device in Live.   
  
A MaxDevice is a type of Device, meaning that it has all the children, properties and functions that a Device has. Listed below are the members unique to MaxDevice.

## Properties

### audio_inputs list of [DeviceIO](/apiref/lom/deviceio/ "DeviceIO") read-onlyobserve

List of the audio inputs that the MaxDevice offers.

### audio_outputs list of [DeviceIO](/apiref/lom/deviceio/ "DeviceIO") read-onlyobserve

List of the audio outputs that the MaxDevice offers.

### midi_inputs list of [DeviceIO](/apiref/lom/deviceio/ "DeviceIO") read-onlyobserve

List of the midi inputs that the MaxDevice offers.   
  
*Available since Live 11.0.*

### midi_outputs list of [DeviceIO](/apiref/lom/deviceio/ "DeviceIO") read-onlyobserve

List of the midi outputs that the MaxDevice offers.   
  
*Available since Live 11.0.*

## Functions

### get_bank_count

Returns: [int] the number of parameter banks.

### get_bank_name

Parameters: `bank_index` [int]   
Returns: [list of symbols] The name of the parameter bank specified by bank_index.

### get_bank_parameters

Parameters: `bank_index` [int]   
Returns: [list of ints] The indices of the parameters contained in the bank specified by bank_index. Empty slots are marked as -1. Bank index -1 refers to the "Best of" bank.


### melddevice.md

# MeldDevice

This class represents an instance of a Meld device in Live.   
A MeldDevice has all the properties, functions and children of a Device.

## Properties

### selected_engine int observe

Meld's oscillator engine selector. The modes are encoded as follows:   
0 = Engine A   
1 = Engine B

### unison_voices int observe

Selects the Unison voice count. The modes are encoded as follows:   
  
0 = off   
1 = two   
2 = three   
3 = four

### mono_poly int observe

Selects the polyphony mode. The modes are encoded as follows:   
  
0 = mono   
1 = poly

### poly_voices int observe

Selects the polyphony voice count. The modes are encoded as follows:   
  
0 = two   
1 = three   
2 = four   
3 = five   
4 = six   
5 = eight   
6 = twelve


### mixerdevice.md

# MixerDevice

This class represents a mixer device in Live. It provides access to volume, panning and other [DeviceParameter](#DeviceParameter) objects. See [DeviceParameter](#DeviceParameter) to learn how to modify them.

## Canonical Path

```
live_set tracks N mixer_device
```

## Children

### sends list of [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve

One send per return track.

### cue_volume [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in master track only]

### crossfader [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in master track only]

### left_split_stereo [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

The Track's Left Split Stereo Pan Parameter.

### panning [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

### right_split_stereo [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

The Track's Right Split Stereo Pan Parameter.

### song_tempo [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

[in master track only]

### track_activator [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

### volume [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

## Properties

### crossfade_assign int observe

0 = A, 1 = none, 2 = B [not in master track]

### panning_mode int observe

Access to the Track mixer's pan mode: 0 = Stereo, 1 = Split Stereo.


### plugindevice.md

# PluginDevice

This class represents a plug-in device.   
  
A PluginDevice is a type of Device, meaning that it has all the children, properties and functions that a Device has. Listed below are the members unique to PluginDevice.

## Properties

### presets StringVector read-onlyobserve

Get the list of the plug-in's presets.

### selected_preset_index int observe

Get/set the index of the currently selected preset.


### rackdevice.md

# RackDevice

This class represents a Live Rack Device.   
A RackDevice is a type of Device, meaning that it has all the children, properties and functions that a Device has. Listed below are members unique to RackDevice.

## Children

### chain_selector [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

Convenience accessor for the Rack's chain selector.

### chains list of [Chain](/apiref/lom/chain/ "Chain") read-onlyobserve

The Rack's chains.

### drum_pads list of [DrumPad](/apiref/lom/drumpad/ "DrumPad") read-onlyobserve

All 128 Drum Pads for the topmost Drum Rack. Inner Drum Racks return a list of 0 entries.

### return_chains list of [Chain](/apiref/lom/chain/ "Chain") read-onlyobserve

The Rack's return chains.

### visible_drum_pads list of [DrumPad](/apiref/lom/drumpad/ "DrumPad") read-onlyobserve

All 16 visible DrumPads for the topmost Drum Rack. Inner Drum Racks return a list of 0 entries.

## Properties

### can_show_chains bool read-only

1 = The Rack contains an instrument device that is capable of showing its chains in Session View.

### has_drum_pads bool read-onlyobserve

1 = the device is a Drum Rack with pads. A nested Drum Rack is a Drum Rack without pads.   
Only available for Drum Racks.

### has_macro_mappings bool read-onlyobserve

1 = any of a Rack's Macros are mapped to a parameter.

### is_showing_chains bool observe

1 = The Rack contains an instrument device that is showing its chains in Session View.

### variation_count int read-onlyobserve

The number of currently stored macro variations.   
  
*Available since Live 11.0.*

### selected_variation_index int

Get/set the currently selected variation.   
  
*Available since Live 11.0.*

### visible_macro_count int read-onlyobserve

The number of currently visible macros.

## Functions

### copy_pad

Parameters:   
`source_index` [int]   
`destination_index` [int]   
Copies all content of a Drum Rack pad from a source pad to a destination pad. The source_index and destination_index refer to pad indices inside a Drum Rack.

### add_macro

Increases the number of visible macro controls.   
  
*Available since Live 11.0.*

### insert_chain

Parameters: `index` [int] (optional)   
  
Attempts to insert a new chain at the given index, or at the end of the chain list if no index is provided. Throws an error if insertion is not possible.   
Side note: A chain inserted into a Drum Rack will have an initial MIDI In Note setting of "All Notes" (see `DrumChain.in_note`). You likely want the chain to be triggered when a specific pad is played; the way to achieve this is to set the `in_note` to the note value that corresponds to the pad.   
  
*Available since Live 12.3.*

### remove_macro

Decreases the number of visible macro controls.   
  
*Available since Live 11.0.*

### randomize_macros

Randomizes the values of eligible macro controls.   
  
*Available since Live 11.0.*

### store_variation

Stores a new variation of the values of all currently mapped macros.   
  
*Available since Live 11.0.*

### recall_selected_variation

Recalls the currently selected macro variation.   
  
*Available since Live 11.0.*

### recall_last_used_variation

Recalls the macro variation that was recalled most recently.   
  
*Available since Live 11.0.*

### delete_selected_variation

Deletes the currently selected macro variation. Does nothing if there is no selected variation.   
  
*Available since Live 11.0.*


### rackdevice_view.md

# RackDevice.View

Represents the view aspects of a Rack Device.   
A RackDevice.View is a type of Device.View, meaning that it has all the properties that a Device.View has. Listed below are the members unique to RackDevice.View.

## Children

### selected_drum_pad [DrumPad](/apiref/lom/drumpad/ "DrumPad") observe

Currently selected Drum Rack pad.   
Only available for Drum Racks.

### selected_chain [Chain](/apiref/lom/chain/ "Chain") observe

Currently selected chain.

## Properties

### drum_pads_scroll_position int observe

Lowest row of pads visible, range: 0 - 28.   
Only available for Drum Racks.

### is_showing_chain_devices bool observe

1 = the devices in the currently selected chain are visible.


### roardevice.md

# RoarDevice

This class represents an instance of a Roar device in Live.   
A RoarDevice has all the properties, functions and children of a Roar Device.

## Properties

### routing_mode_index int observe

The index of the routing mode utilized by Roar.

### routing_mode_list StringVector read-only

The list of available routing modes.

### env_listen bool observe

Get, set and observe the Envelope Input Listen toogle.


### shifterdevice.md

# ShifterDevice

This class represents an instance of the Shifter audio effect.   
A ShifterDevice is a type of device, meaning that it has all the children, properties and functions that a device has. Listed below are members unique to ShifterDevice.

## Properties

### pitch_bend_range int observe

The pitch bend range used in MIDI Pitch Mode.

### pitch_mode_index int observe

The current pitch mode index: 0 = Internal, 1 = MIDI


### simplerdevice.md

# SimplerDevice

This class represents an instance of Simpler.   
A SimplerDevice is a type of device, meaning that it has all the children, properties and functions that a device has. Listed below are members unique to SimplerDevice.

## Children

### sample [Sample](/apiref/lom/sample/ "Sample") read-onlyobserve

The sample currently loaded into Simpler.

## Properties

### can_warp_as bool read-onlyobserve

1 = warp_as is available.

### can_warp_double bool read-onlyobserve

1 = warp_double is available.

### can_warp_half bool read-onlyobserve

1 = warp_half is available.

### multi_sample_mode bool read-onlyobserve

1 = Simpler is in multisample mode.

### pad_slicing bool observe

1 = slices can be added in Slicing Mode by playing notes which are not yet assigned to existing slices.

### playback_mode int observe

Get/set Simpler's playback mode.   
0 = Classic Mode   
1 = One-Shot Mode   
2 = Slicing Mode

### playing_position float read-onlyobserve

The current playing position in the sample, expressed as a value between 0. and 1.

### playing_position_enabled bool read-onlyobserve

1 = Simpler is playing back the sample and showing the playing position.

### retrigger bool observe

1 = Retrigger is enabled in Simpler.

### slicing_playback_mode int observe

Get/set Simpler's Slicing Playback Mode.   
0 = Mono   
1 = Poly   
2 = Thru

### voices int observe

Get/set the number of Voices.

## Functions

### crop

Crop the loaded sample to the active region between the start and end markers.

### guess_playback_length

Returns: [float] An estimated beat time for the playback length between the start and end markers.

### reverse

Reverse the loaded sample.

### warp_as

Parameters: `beats` [int]   
Warp the active region between the start and end markers as the specified number of beats.

### warp_double

Double the playback tempo of the active region between the start and end markers.

### warp_half

Halve the playback tempo for the active region between the start and end markers.


### simplerdevice_view.md

# SimplerDevice.View

Represents the view aspects of a SimplerDevice.   
A SimplerDevice.View is a type of Device.View, meaning that it has all the properties that a Device.View has. Listed below are the members unique to SimplerDevice.View.

## Properties

### selected_slice int observe

The currenctly selected slice, identified by its slice time.


### spectralresonatordevice.md

# SpectralResonatorDevice

This class represents an instance of a Spectral Resonator device in Live.   
An SpectralResonatorDevice has all the properties, functions and children of a Device. Listed below are members unique to SpectralResonatorDevice.

## Properties

### frequency_dial_mode int observe

Get, set and observe the Freq control's mode.  
0 = Hertz, 1 = MIDI note values.

### midi_gate int observe

Get, set and observe the MIDI gate switch's state.  
0 = Off, 1 = On.

### mod_mode int observe

Get, set and observe the Modulation Mode.  
0 = None, 1 = Chorus, 2 = Wander, 3 = Granular.

### mono_poly int observe

Get, set and observe the Mono/Poly switch's state.  
0 = Mono, 1 = Poly.

### pitch_mode int observe

Get, set and observe the Pitch Mode.  
0 = Internal, 1 = MIDI.

### pitch_bend_range int observe

Get, set and observe the Pitch Bend Range.\

### polyphony int observe

Get, set and observe the Polyphony.  
0 = 2, 1 = 4, 2 = 8, 3 = 16 voices.


### this_device.md

# this_device

This root path represents the device containing the [live.path](/reference/live.path "live.path") object to which the `goto this_device` message is sent. The class of this object is `Device`.

## Canonical Path

```
live_set tracks N devices M
```


### wavetabledevice.md

# WavetableDevice

This class represents a Wavetable instrument.   
  
A WavetableDevice shares all of the children, functions and properties that a Device has. Listed below are members unique to it.

## Properties

### filter_routing int observe

Access to the current filter routing. 0 = Serial, 1 = Parallel, 2 = Split.

### mono_poly int observe

Access to Wavetable's Poly/Mono switch. 0 = Mono, 1 = Poly.

### oscillator_1_effect_mode int observe

Access to oscillator 1's effect mode. 0 = None, 1 = Fm, 2 = Classic, 3 = Modern.

### oscillator_2_effect_mode int observe

Access to oscillator 2's effect mode.

### oscillator_1_wavetable_category observe

Access to oscillator 1's wavetable category selector.

### oscillator_2_wavetable_category observe

Access to oscillator 2's wavetable category selector.

### oscillator_1_wavetable_index observe

Access to oscillator 1's wavetable index selector.

### oscillator_2_wavetable_index observe

Access to oscillator 2's wavetable index selector.

### oscillator_1_wavetables StringVector read-onlyobserve

List of names of the wavetables currently available for oscillator 1. Depends on the current wavetable category selection (see *oscillator_1_wavetable_category*).

### oscillator_2_wavetables StringVector read-onlyobserve

List of names of the wavetables currently available for oscillator 2. Depends on the current wavetable category selection (see *oscillator_2_wavetable_category*).

### oscillator_wavetable_categories StringVector read-only

List of the names of the available wavetable categories.

### poly_voices int observe

The current number of polyphonic voices.

### unison_mode int observe

Access to Wavetable's unison mode parameter.   
  
0 = None   
1 = Classic   
2 = Shimmer   
3 = Noise   
4 = Phase Sync   
5 = Position Spread   
6 = Random Note

### unison_voice_count int observe

Access to the number of unison voices.

### visible_modulation_target_names StringVector read-onlyobserve

List of the names of modulation targets currently visible in the modulation matrix.

## Functions

### add_parameter_to_modulation_matrix

Parameter: `parameter_to_add` [DeviceParameter]   
Add an instrument parameter to the modulation matrix. Only works for parameters that can be modulated (see *is_parameter_modulatable*).

### get_modulation_target_parameter_name

Parameter: `index` [int]   
Return the modulation target parameter name at *index* in the modulation matrix as a [symbol].

### get_modulation_value

Parameters: `modulation_target_index` [int] `modulation_source_index` [int]   
Return the amount of the modulation of the parameter at `modulation_target_index` by the modulation source at `modulation_source_index` in Wavetable's modulation matrix.

### is_parameter_modulatable

Parameter: `parameter` [DeviceParameter]   
1 = `parameter` can be modulated. Call this before `add_parameter_to_modulation_matrix`.

### set_modulation_value

Parameters: `modulation_target_index` [int] `modulation_source_index` [int]   
Set the amount of the modulation of the parameter at `modulation_target_index` by the modulation source at `modulation_source_index` in Wavetable's modulation matrix.

