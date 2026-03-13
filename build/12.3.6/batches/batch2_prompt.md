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

## API Type Skeleton

This is the complete type hierarchy of the Live API — all modules, classes, enums, and properties. Use it to identify valid type names and understand class relationships.

```json
{
  "name": "Live",
  "type": "module",
  "children": [
    {
      "name": "Application",
      "type": "module",
      "children": [
        {
          "name": "Application",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class",
              "children": [
                {
                  "name": "NavDirection",
                  "type": "enum"
                },
                {
                  "name": "_live_ptr",
                  "probed_type": "int"
                },
                {
                  "name": "browse_mode",
                  "probed_type": "bool"
                },
                {
                  "name": "canonical_parent",
                  "probed_type": "Application"
                },
                {
                  "name": "focused_document_view",
                  "probed_type": "str"
                }
              ]
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "average_process_usage",
              "probed_type": "float"
            },
            {
              "name": "browser",
              "probed_type": "Browser"
            },
            {
              "name": "canonical_parent",
              "probed_type": "NoneType"
            },
            {
              "name": "control_surfaces",
              "probed_type": "ObjectVector"
            },
            {
              "name": "current_dialog_button_count",
              "probed_type": "int"
            },
            {
              "name": "current_dialog_message",
              "probed_type": "str"
            },
            {
              "name": "number_of_push_apps_running",
              "probed_type": "int"
            },
            {
              "name": "open_dialog_count",
              "probed_type": "int"
            },
            {
              "name": "peak_process_usage",
              "probed_type": "float"
            },
            {
              "name": "unavailable_features",
              "probed_type": "UnavailableFeatureVector"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        },
        {
          "name": "ControlDescription",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "id",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            }
          ]
        },
        {
          "name": "ControlDescriptionVector",
          "type": "class"
        },
        {
          "name": "ControlSurfaceProxy",
          "type": "class",
          "children": [
            {
              "name": "control_descriptions"
            },
            {
              "name": "pad_layout"
            },
            {
              "name": "type_name"
            }
          ]
        },
        {
          "name": "MessageButtons",
          "type": "enum"
        },
        {
          "name": "PushDialogType",
          "type": "enum"
        },
        {
          "name": "UnavailableFeature",
          "type": "enum"
        },
        {
          "name": "UnavailableFeatureVector",
          "type": "class"
        },
        {
          "name": "Variants",
          "type": "class",
          "children": [
            {
              "name": "BETA",
              "type": "str",
              "value": "'Beta'"
            },
            {
              "name": "INTRO",
              "type": "str",
              "value": "'Intro'"
            },
            {
              "name": "LITE",
              "type": "str",
              "value": "'Lite'"
            },
            {
              "name": "STANDARD",
              "type": "str",
              "value": "'Standard'"
            },
            {
              "name": "SUITE",
              "type": "str",
              "value": "'Suite'"
            },
            {
              "name": "TRIAL",
              "type": "str",
              "value": "'Trial'"
            }
          ]
        }
      ]
    },
    {
      "name": "Base",
      "type": "module",
      "children": [
        {
          "name": "FloatVector",
          "type": "class"
        },
        {
          "name": "IntU64Vector",
          "type": "class"
        },
        {
          "name": "IntVector",
          "type": "class"
        },
        {
          "name": "LimitationError",
          "type": "exception"
        },
        {
          "name": "ObjectVector",
          "type": "class"
        },
        {
          "name": "StringVector",
          "type": "class"
        },
        {
          "name": "Text",
          "type": "class",
          "children": [
            {
              "name": "text"
            }
          ]
        },
        {
          "name": "Timer",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "running",
              "probed_type": "bool"
            }
          ]
        },
        {
          "name": "Vector",
          "type": "class"
        }
      ]
    },
    {
      "name": "Browser",
      "type": "module",
      "children": [
        {
          "name": "Browser",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "audio_effects",
              "probed_type": "BrowserItem"
            },
            {
              "name": "clips",
              "probed_type": "BrowserItem"
            },
            {
              "name": "colors",
              "probed_type": "BrowserItemVector"
            },
            {
              "name": "current_project",
              "probed_type": "BrowserItem"
            },
            {
              "name": "drums",
              "probed_type": "BrowserItem"
            },
            {
              "name": "filter_type",
              "probed_type": "int"
            },
            {
              "name": "hotswap_target",
              "probed_type": "NoneType"
            },
            {
              "name": "instruments",
              "probed_type": "BrowserItem"
            },
            {
              "name": "legacy_libraries",
              "probed_type": "BrowserItemVector"
            },
            {
              "name": "max_for_live",
              "probed_type": "BrowserItem"
            },
            {
              "name": "midi_effects",
              "probed_type": "BrowserItem"
            },
            {
              "name": "packs",
              "probed_type": "BrowserItem"
            },
            {
              "name": "plugins",
              "probed_type": "BrowserItem"
            },
            {
              "name": "samples",
              "probed_type": "BrowserItem"
            },
            {
              "name": "sounds",
              "probed_type": "BrowserItem"
            },
            {
              "name": "user_folders",
              "probed_type": "BrowserItemVector"
            },
            {
              "name": "user_library",
              "probed_type": "BrowserItem"
            }
          ]
        },
        {
          "name": "BrowserItem",
          "type": "class",
          "children": [
            {
              "name": "children",
              "probed_type": "BrowserItemVector"
            },
            {
              "name": "is_device",
              "probed_type": "bool"
            },
            {
              "name": "is_folder",
              "probed_type": "bool"
            },
            {
              "name": "is_loadable",
              "probed_type": "bool"
            },
            {
              "name": "is_selected",
              "probed_type": "bool"
            },
            {
              "name": "iter_children",
              "probed_type": "BrowserItemIterator"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "source",
              "probed_type": "str"
            },
            {
              "name": "uri",
              "probed_type": "str"
            }
          ]
        },
        {
          "name": "BrowserItemIterator",
          "type": "class"
        },
        {
          "name": "BrowserItemVector",
          "type": "class"
        },
        {
          "name": "FilterType",
          "type": "enum"
        },
        {
          "name": "Relation",
          "type": "enum"
        }
      ]
    },
    {
      "name": "CcControlDevice",
      "type": "module",
      "children": [
        {
          "name": "CcControlDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "custom_bool_target",
              "probed_type": "int"
            },
            {
              "name": "custom_bool_target_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_0",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_0_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_1",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_10",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_10_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_11",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_11_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_1_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_2",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_2_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_3",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_3_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_4",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_4_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_5",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_5_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_6",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_6_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_7",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_7_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_8",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_8_list",
              "probed_type": "StringVector"
            },
            {
              "name": "custom_float_target_9",
              "probed_type": "int"
            },
            {
              "name": "custom_float_target_9_list",
              "probed_type": "StringVector"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "Chain",
      "type": "module",
      "children": [
        {
          "name": "Chain",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "RackDevice"
            },
            {
              "name": "color",
              "probed_type": "int"
            },
            {
              "name": "color_index",
              "probed_type": "int"
            },
            {
              "name": "devices",
              "probed_type": "Vector"
            },
            {
              "name": "has_audio_input",
              "probed_type": "bool"
            },
            {
              "name": "has_audio_output",
              "probed_type": "bool"
            },
            {
              "name": "has_midi_input",
              "probed_type": "bool"
            },
            {
              "name": "has_midi_output",
              "probed_type": "bool"
            },
            {
              "name": "is_auto_colored",
              "probed_type": "bool"
            },
            {
              "name": "mixer_device",
              "probed_type": "ChainMixerDevice"
            },
            {
              "name": "mute",
              "probed_type": "bool"
            },
            {
              "name": "muted_via_solo",
              "probed_type": "bool"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "solo",
              "probed_type": "bool"
            }
          ]
        }
      ]
    },
    {
      "name": "ChainMixerDevice",
      "type": "module",
      "children": [
        {
          "name": "ChainMixerDevice",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Chain"
            },
            {
              "name": "chain_activator",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "panning",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "sends",
              "probed_type": "Vector"
            },
            {
              "name": "volume",
              "probed_type": "DeviceParameter"
            }
          ]
        }
      ]
    },
    {
      "name": "Clip",
      "type": "module",
      "children": [
        {
          "name": "Clip",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class",
              "children": [
                {
                  "name": "_live_ptr",
                  "probed_type": "int"
                },
                {
                  "name": "canonical_parent",
                  "probed_type": "Clip"
                },
                {
                  "name": "grid_is_triplet",
                  "probed_type": "bool"
                },
                {
                  "name": "grid_quantization",
                  "probed_type": "GridQuantization"
                }
              ]
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "automation_envelopes",
              "probed_type": "Vector"
            },
            {
              "name": "available_warp_modes",
              "probed_type": "IntVector"
            },
            {
              "name": "canonical_parent",
              "probed_type": "ClipSlot"
            },
            {
              "name": "color",
              "probed_type": "int"
            },
            {
              "name": "color_index",
              "probed_type": "int"
            },
            {
              "name": "end_marker",
              "probed_type": "float"
            },
            {
              "name": "end_time",
              "probed_type": "float"
            },
            {
              "name": "file_path",
              "probed_type": "str"
            },
            {
              "name": "gain",
              "probed_type": "float"
            },
            {
              "name": "gain_display_string",
              "probed_type": "str"
            },
            {
              "name": "groove",
              "probed_type": "NoneType"
            },
            {
              "name": "has_envelopes",
              "probed_type": "bool"
            },
            {
              "name": "has_groove",
              "probed_type": "bool"
            },
            {
              "name": "is_arrangement_clip",
              "probed_type": "bool"
            },
            {
              "name": "is_audio_clip",
              "probed_type": "bool"
            },
            {
              "name": "is_midi_clip",
              "probed_type": "bool"
            },
            {
              "name": "is_overdubbing",
              "probed_type": "bool"
            },
            {
              "name": "is_playing",
              "probed_type": "bool"
            },
            {
              "name": "is_recording",
              "probed_type": "bool"
            },
            {
              "name": "is_session_clip",
              "probed_type": "bool"
            },
            {
              "name": "is_take_lane_clip",
              "probed_type": "bool"
            },
            {
              "name": "is_triggered",
              "probed_type": "bool"
            },
            {
              "name": "launch_mode",
              "probed_type": "int"
            },
            {
              "name": "launch_quantization",
              "probed_type": "int"
            },
            {
              "name": "legato",
              "probed_type": "bool"
            },
            {
              "name": "length",
              "probed_type": "float"
            },
            {
              "name": "loop_end",
              "probed_type": "float"
            },
            {
              "name": "loop_start",
              "probed_type": "float"
            },
            {
              "name": "looping",
              "probed_type": "bool"
            },
            {
              "name": "muted",
              "probed_type": "bool"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "pitch_coarse",
              "probed_type": "int"
            },
            {
              "name": "pitch_fine",
              "probed_type": "float"
            },
            {
              "name": "playing_position",
              "probed_type": "float"
            },
            {
              "name": "position",
              "probed_type": "float"
            },
            {
              "name": "ram_mode",
              "probed_type": "bool"
            },
            {
              "name": "sample_length",
              "probed_type": "int"
            },
            {
              "name": "sample_rate",
              "probed_type": "float"
            },
            {
              "name": "signature_denominator",
              "probed_type": "int"
            },
            {
              "name": "signature_numerator",
              "probed_type": "int"
            },
            {
              "name": "start_marker",
              "probed_type": "float"
            },
            {
              "name": "start_time",
              "probed_type": "float"
            },
            {
              "name": "velocity_amount",
              "probed_type": "float"
            },
            {
              "name": "view",
              "probed_type": "View"
            },
            {
              "name": "warp_markers",
              "probed_type": "WarpMarkerVector"
            },
            {
              "name": "warp_mode",
              "probed_type": "int"
            },
            {
              "name": "warping",
              "probed_type": "bool"
            },
            {
              "name": "will_record_on_start",
              "probed_type": "bool"
            }
          ]
        },
        {
          "name": "ClipLaunchQuantization",
          "type": "enum"
        },
        {
          "name": "GridQuantization",
          "type": "enum"
        },
        {
          "name": "LaunchMode",
          "type": "enum"
        },
        {
          "name": "MidiNote",
          "type": "class",
          "children": [
            {
              "name": "duration",
              "probed_type": "float"
            },
            {
              "name": "mute",
              "probed_type": "bool"
            },
            {
              "name": "note_id",
              "probed_type": "int"
            },
            {
              "name": "pitch",
              "probed_type": "int"
            },
            {
              "name": "probability",
              "probed_type": "float"
            },
            {
              "name": "release_velocity",
              "probed_type": "float"
            },
            {
              "name": "start_time",
              "probed_type": "float"
            },
            {
              "name": "velocity",
              "probed_type": "float"
            },
            {
              "name": "velocity_deviation",
              "probed_type": "float"
            }
          ]
        },
        {
          "name": "MidiNoteSpecification",
          "type": "class",
          "constructable": true
        },
        {
          "name": "MidiNoteVector",
          "type": "class"
        },
        {
          "name": "WarpMarker",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "beat_time",
              "probed_type": "float"
            },
            {
              "name": "sample_time",
              "probed_type": "float"
            }
          ]
        },
        {
          "name": "WarpMarkerVector",
          "type": "class"
        },
        {
          "name": "WarpMode",
          "type": "enum"
        }
      ]
    },
    {
      "name": "ClipSlot",
      "type": "module",
      "children": [
        {
          "name": "ClipSlot",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "clip",
              "probed_type": "Clip"
            },
            {
              "name": "color",
              "probed_type": "int"
            },
            {
              "name": "color_index",
              "probed_type": "int"
            },
            {
              "name": "controls_other_clips",
              "probed_type": "bool"
            },
            {
              "name": "has_clip",
              "probed_type": "bool"
            },
            {
              "name": "has_stop_button",
              "probed_type": "bool"
            },
            {
              "name": "is_group_slot",
              "probed_type": "bool"
            },
            {
              "name": "is_playing",
              "probed_type": "bool"
            },
            {
              "name": "is_recording",
              "probed_type": "bool"
            },
            {
              "name": "is_triggered",
              "probed_type": "bool"
            },
            {
              "name": "playing_status",
              "probed_type": "ClipSlotPlayingState"
            },
            {
              "name": "will_record_on_start",
              "probed_type": "bool"
            }
          ]
        },
        {
          "name": "ClipSlotPlayingState",
          "type": "enum"
        }
      ]
    },
    {
      "name": "CompressorDevice",
      "type": "module",
      "children": [
        {
          "name": "CompressorDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "available_input_routing_channels",
              "probed_type": "RoutingChannelVector"
            },
            {
              "name": "available_input_routing_types",
              "probed_type": "RoutingTypeVector"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "input_routing_channel",
              "probed_type": "RoutingChannel"
            },
            {
              "name": "input_routing_type",
              "probed_type": "RoutingType"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "Conversions",
      "type": "module",
      "children": [
        {
          "name": "AudioToMidiType",
          "type": "enum"
        }
      ]
    },
    {
      "name": "Device",
      "type": "module",
      "children": [
        {
          "name": "ATimeableValueVector",
          "type": "class"
        },
        {
          "name": "Device",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class",
              "children": [
                {
                  "name": "_live_ptr",
                  "probed_type": "int"
                },
                {
                  "name": "canonical_parent",
                  "probed_type": "Device"
                },
                {
                  "name": "is_collapsed",
                  "probed_type": "bool"
                }
              ]
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        },
        {
          "name": "DeviceType",
          "type": "enum"
        }
      ]
    },
    {
      "name": "DeviceIO",
      "type": "module",
      "children": [
        {
          "name": "DeviceIO",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "available_routing_channels",
              "probed_type": "RoutingChannelVector"
            },
            {
              "name": "available_routing_types",
              "probed_type": "RoutingTypeVector"
            },
            {
              "name": "canonical_parent",
              "probed_type": "MaxDevice"
            },
            {
              "name": "default_external_routing_channel_is_none",
              "probed_type": "bool"
            },
            {
              "name": "routing_channel",
              "probed_type": "RoutingChannel"
            },
            {
              "name": "routing_type",
              "probed_type": "RoutingType"
            }
          ]
        }
      ]
    },
    {
      "name": "DeviceParameter",
      "type": "module",
      "children": [
        {
          "name": "AutomationState",
          "type": "enum"
        },
        {
          "name": "DeviceParameter",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "automation_state",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Device"
            },
            {
              "name": "default_value",
              "probed_type": "float"
            },
            {
              "name": "display_value",
              "probed_type": "float"
            },
            {
              "name": "is_enabled",
              "probed_type": "bool"
            },
            {
              "name": "is_quantized",
              "probed_type": "bool"
            },
            {
              "name": "max",
              "probed_type": "float"
            },
            {
              "name": "min",
              "probed_type": "float"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "original_name",
              "probed_type": "str"
            },
            {
              "name": "short_value_items",
              "probed_type": "StringVector"
            },
            {
              "name": "state",
              "probed_type": "int"
            },
            {
              "name": "value",
              "probed_type": "float"
            },
            {
              "name": "value_items",
              "probed_type": "StringVector"
            }
          ]
        },
        {
          "name": "ParameterState",
          "type": "enum"
        }
      ]
    },
    {
      "name": "DriftDevice",
      "type": "module",
      "children": [
        {
          "name": "DriftDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_filter_source_1_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_filter_source_1_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_filter_source_2_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_filter_source_2_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_lfo_source_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_lfo_source_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_pitch_source_1_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_pitch_source_1_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_pitch_source_2_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_pitch_source_2_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_shape_source_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_shape_source_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_source_1_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_source_1_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_source_2_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_source_2_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_source_3_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_source_3_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_target_1_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_target_1_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_target_2_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_target_2_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_matrix_target_3_index",
              "probed_type": "int"
            },
            {
              "name": "mod_matrix_target_3_list",
              "probed_type": "StringVector"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "pitch_bend_range",
              "probed_type": "int"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            },
            {
              "name": "voice_count_index",
              "probed_type": "int"
            },
            {
              "name": "voice_count_list",
              "probed_type": "StringVector"
            },
            {
              "name": "voice_mode_index",
              "probed_type": "int"
            },
            {
              "name": "voice_mode_list",
              "probed_type": "StringVector"
            }
          ]
        }
      ]
    },
    {
      "name": "DrumCellDevice",
      "type": "module",
      "children": [
        {
          "name": "DrumCellDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "gain",
              "probed_type": "float"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "DrumChain",
      "type": "module",
      "children": [
        {
          "name": "DrumChain",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "RackDevice"
            },
            {
              "name": "choke_group",
              "probed_type": "int"
            },
            {
              "name": "color",
              "probed_type": "int"
            },
            {
              "name": "color_index",
              "probed_type": "int"
            },
            {
              "name": "devices",
              "probed_type": "Vector"
            },
            {
              "name": "has_audio_input",
              "probed_type": "bool"
            },
            {
              "name": "has_audio_output",
              "probed_type": "bool"
            },
            {
              "name": "has_midi_input",
              "probed_type": "bool"
            },
            {
              "name": "has_midi_output",
              "probed_type": "bool"
            },
            {
              "name": "in_note",
              "probed_type": "int"
            },
            {
              "name": "is_auto_colored",
              "probed_type": "bool"
            },
            {
              "name": "mixer_device",
              "probed_type": "ChainMixerDevice"
            },
            {
              "name": "mute",
              "probed_type": "bool"
            },
            {
              "name": "muted_via_solo",
              "probed_type": "bool"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "out_note",
              "probed_type": "int"
            },
            {
              "name": "solo",
              "probed_type": "bool"
            }
          ]
        }
      ]
    },
    {
      "name": "DrumPad",
      "type": "module",
      "children": [
        {
          "name": "DrumPad",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "RackDevice"
            },
            {
              "name": "chains",
              "probed_type": "Vector"
            },
            {
              "name": "mute",
              "probed_type": "bool"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "note",
              "probed_type": "int"
            },
            {
              "name": "solo",
              "probed_type": "bool"
            }
          ]
        }
      ]
    },
    {
      "name": "Envelope",
      "type": "module",
      "children": [
        {
          "name": "Envelope",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Clip"
            }
          ]
        },
        {
          "name": "EnvelopeEvent",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "control_coefficients",
              "probed_type": "EnvelopeEventControlCoefficients"
            },
            {
              "name": "time",
              "probed_type": "float"
            },
            {
              "name": "value",
              "probed_type": "float"
            }
          ]
        },
        {
          "name": "EnvelopeEventControlCoefficients",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "x1",
              "probed_type": "float"
            },
            {
              "name": "x2",
              "probed_type": "float"
            },
            {
              "name": "y1",
              "probed_type": "float"
            },
            {
              "name": "y2",
              "probed_type": "float"
            }
          ]
        },
        {
          "name": "EnvelopeEventVector",
          "type": "class"
        }
      ]
    },
    {
      "name": "Eq8Device",
      "type": "module",
      "children": [
        {
          "name": "EditMode",
          "type": "enum"
        },
        {
          "name": "Eq8Device",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class",
              "children": [
                {
                  "name": "_live_ptr",
                  "probed_type": "int"
                },
                {
                  "name": "canonical_parent",
                  "probed_type": "Eq8Device"
                },
                {
                  "name": "is_collapsed",
                  "probed_type": "bool"
                },
                {
                  "name": "selected_band",
                  "probed_type": "int"
                }
              ]
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "edit_mode",
              "probed_type": "bool"
            },
            {
              "name": "global_mode",
              "probed_type": "int"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "oversample",
              "probed_type": "bool"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        },
        {
          "name": "GlobalMode",
          "type": "enum"
        }
      ]
    },
    {
      "name": "Groove",
      "type": "module",
      "children": [
        {
          "name": "Base",
          "type": "enum"
        },
        {
          "name": "Groove",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "base",
              "probed_type": "Base"
            },
            {
              "name": "canonical_parent",
              "probed_type": "GroovePool"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "quantization_amount",
              "probed_type": "float"
            },
            {
              "name": "random_amount",
              "probed_type": "float"
            },
            {
              "name": "timing_amount",
              "probed_type": "float"
            },
            {
              "name": "velocity_amount",
              "probed_type": "float"
            }
          ]
        }
      ]
    },
    {
      "name": "GroovePool",
      "type": "module",
      "children": [
        {
          "name": "GroovePool",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Song"
            },
            {
              "name": "grooves",
              "probed_type": "Vector"
            }
          ]
        }
      ]
    },
    {
      "name": "HybridReverbDevice",
      "type": "module",
      "children": [
        {
          "name": "HybridReverbDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "ir_attack_time",
              "probed_type": "float"
            },
            {
              "name": "ir_category_index",
              "probed_type": "int"
            },
            {
              "name": "ir_category_list",
              "probed_type": "StringVector"
            },
            {
              "name": "ir_decay_time",
              "probed_type": "float"
            },
            {
              "name": "ir_file_index",
              "probed_type": "int"
            },
            {
              "name": "ir_file_list",
              "probed_type": "StringVector"
            },
            {
              "name": "ir_size_factor",
              "probed_type": "float"
            },
            {
              "name": "ir_time_shaping_on",
              "probed_type": "bool"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "Licensing",
      "type": "module",
      "children": [
        {
          "name": "ProgressDialog",
          "type": "class"
        },
        {
          "name": "PythonLicensingBridge",
          "type": "class",
          "children": [
            {
              "name": "base_product_id"
            },
            {
              "name": "in_sassafras_mode"
            },
            {
              "name": "license_must_match_variant"
            },
            {
              "name": "random_number_for_trial_authorization"
            },
            {
              "name": "set_has_unsaved_changes"
            }
          ]
        },
        {
          "name": "StartupDialog",
          "type": "class"
        },
        {
          "name": "TrialContext",
          "type": "enum"
        },
        {
          "name": "UnlockStatus",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "authorization_deactivated",
              "probed_type": "bool"
            },
            {
              "name": "authorization_expired",
              "probed_type": "bool"
            },
            {
              "name": "has_max_unlock_products",
              "probed_type": "bool"
            },
            {
              "name": "temp_demo_mode",
              "probed_type": "bool"
            },
            {
              "name": "time_limited",
              "probed_type": "bool"
            },
            {
              "name": "unlock_error",
              "probed_type": "bool"
            },
            {
              "name": "unlocked",
              "probed_type": "bool"
            }
          ]
        }
      ]
    },
    {
      "name": "Listener",
      "type": "module",
      "children": [
        {
          "name": "ListenerHandle",
          "type": "class",
          "children": [
            {
              "name": "listener_func"
            },
            {
              "name": "listener_self"
            },
            {
              "name": "name"
            }
          ]
        },
        {
          "name": "ListenerVector",
          "type": "class"
        }
      ]
    },
    {
      "name": "LomObject",
      "type": "module",
      "children": [
        {
          "name": "LomObject",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr"
            }
          ]
        }
      ]
    },
    {
      "name": "LooperDevice",
      "type": "module",
      "children": [
        {
          "name": "LooperDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "loop_length",
              "probed_type": "float"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "overdub_after_record",
              "probed_type": "bool"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "record_length_index",
              "probed_type": "int"
            },
            {
              "name": "record_length_list",
              "probed_type": "StringVector"
            },
            {
              "name": "tempo",
              "probed_type": "float"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "MaxDevice",
      "type": "module",
      "children": [
        {
          "name": "MaxDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "audio_inputs",
              "probed_type": "Vector"
            },
            {
              "name": "audio_outputs",
              "probed_type": "Vector"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "midi_inputs",
              "probed_type": "Vector"
            },
            {
              "name": "midi_outputs",
              "probed_type": "Vector"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "MeldDevice",
      "type": "module",
      "children": [
        {
          "name": "MeldDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "mono_poly",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "poly_voices",
              "probed_type": "int"
            },
            {
              "name": "selected_engine",
              "probed_type": "bool"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "unison_voices",
              "probed_type": "int"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "MidiMap",
      "type": "module",
      "children": [
        {
          "name": "CCFeedbackRule",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "cc_no",
              "probed_type": "int"
            },
            {
              "name": "cc_value_map",
              "probed_type": "tuple"
            },
            {
              "name": "channel",
              "probed_type": "int"
            },
            {
              "name": "delay_in_ms",
              "probed_type": "float"
            },
            {
              "name": "enabled",
              "probed_type": "bool"
            }
          ]
        },
        {
          "name": "MapMode",
          "type": "enum"
        },
        {
          "name": "NoteFeedbackRule",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "channel",
              "probed_type": "int"
            },
            {
              "name": "delay_in_ms",
              "probed_type": "float"
            },
            {
              "name": "enabled",
              "probed_type": "bool"
            },
            {
              "name": "note_no",
              "probed_type": "int"
            },
            {
              "name": "vel_map",
              "probed_type": "tuple"
            }
          ]
        },
        {
          "name": "PitchBendFeedbackRule",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "channel",
              "probed_type": "int"
            },
            {
              "name": "delay_in_ms",
              "probed_type": "float"
            },
            {
              "name": "enabled",
              "probed_type": "bool"
            },
            {
              "name": "value_pair_map",
              "probed_type": "tuple"
            }
          ]
        }
      ]
    },
    {
      "name": "MixerDevice",
      "type": "module",
      "children": [
        {
          "name": "MixerDevice",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "crossfade_assign",
              "probed_type": "int"
            },
            {
              "name": "crossfade_assignments",
              "type": "enum"
            },
            {
              "name": "crossfader",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "cue_volume",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "left_split_stereo",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "panning",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "panning_mode",
              "probed_type": "int"
            },
            {
              "name": "panning_modes",
              "type": "enum"
            },
            {
              "name": "right_split_stereo",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "sends",
              "probed_type": "Vector"
            },
            {
              "name": "song_tempo",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "track_activator",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "volume",
              "probed_type": "DeviceParameter"
            }
          ]
        }
      ]
    },
    {
      "name": "PluginDevice",
      "type": "module",
      "children": [
        {
          "name": "PluginDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "presets",
              "probed_type": "StringVector"
            },
            {
              "name": "selected_preset_index",
              "probed_type": "int"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "RackDevice",
      "type": "module",
      "children": [
        {
          "name": "RackDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class",
              "children": [
                {
                  "name": "_live_ptr",
                  "probed_type": "int"
                },
                {
                  "name": "canonical_parent",
                  "probed_type": "RackDevice"
                },
                {
                  "name": "drum_pads_scroll_position",
                  "probed_type": "int"
                },
                {
                  "name": "is_collapsed",
                  "probed_type": "bool"
                },
                {
                  "name": "is_showing_chain_devices",
                  "probed_type": "bool"
                },
                {
                  "name": "selected_chain",
                  "probed_type": "NoneType"
                },
                {
                  "name": "selected_drum_pad",
                  "probed_type": "DrumPad"
                }
              ]
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "can_show_chains",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "chain_selector",
              "probed_type": "DeviceParameter"
            },
            {
              "name": "chains",
              "probed_type": "Vector"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "drum_pads",
              "probed_type": "Vector"
            },
            {
              "name": "has_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "has_macro_mappings",
              "probed_type": "bool"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_showing_chains",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "macros_mapped",
              "probed_type": "tuple"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "return_chains",
              "probed_type": "Vector"
            },
            {
              "name": "selected_variation_index",
              "probed_type": "int"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "variation_count",
              "probed_type": "int"
            },
            {
              "name": "view",
              "probed_type": "View"
            },
            {
              "name": "visible_drum_pads",
              "probed_type": "Vector"
            },
            {
              "name": "visible_macro_count",
              "probed_type": "int"
            }
          ]
        }
      ]
    },
    {
      "name": "RoarDevice",
      "type": "module",
      "children": [
        {
          "name": "RoarDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "env_listen",
              "probed_type": "bool"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "routing_mode_index",
              "probed_type": "int"
            },
            {
              "name": "routing_mode_list",
              "probed_type": "StringVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "Sample",
      "type": "module",
      "children": [
        {
          "name": "Sample",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "beats_granulation_resolution",
              "probed_type": "int"
            },
            {
              "name": "beats_transient_envelope",
              "probed_type": "float"
            },
            {
              "name": "beats_transient_loop_mode",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "SimplerDevice"
            },
            {
              "name": "complex_pro_envelope",
              "probed_type": "float"
            },
            {
              "name": "complex_pro_formants",
              "probed_type": "float"
            },
            {
              "name": "end_marker",
              "probed_type": "int"
            },
            {
              "name": "file_path",
              "probed_type": "str"
            },
            {
              "name": "gain",
              "probed_type": "float"
            },
            {
              "name": "length",
              "probed_type": "int"
            },
            {
              "name": "sample_rate",
              "probed_type": "float"
            },
            {
              "name": "slices",
              "probed_type": "tuple"
            },
            {
              "name": "slicing_beat_division",
              "probed_type": "int"
            },
            {
              "name": "slicing_region_count",
              "probed_type": "int"
            },
            {
              "name": "slicing_sensitivity",
              "probed_type": "float"
            },
            {
              "name": "slicing_style",
              "probed_type": "int"
            },
            {
              "name": "start_marker",
              "probed_type": "int"
            },
            {
              "name": "texture_flux",
              "probed_type": "float"
            },
            {
              "name": "texture_grain_size",
              "probed_type": "float"
            },
            {
              "name": "tones_grain_size",
              "probed_type": "float"
            },
            {
              "name": "warp_markers",
              "probed_type": "WarpMarkerVector"
            },
            {
              "name": "warp_mode",
              "probed_type": "int"
            },
            {
              "name": "warping",
              "probed_type": "bool"
            }
          ]
        },
        {
          "name": "SlicingBeatDivision",
          "type": "enum"
        },
        {
          "name": "SlicingStyle",
          "type": "enum"
        },
        {
          "name": "TransientLoopMode",
          "type": "enum"
        }
      ]
    },
    {
      "name": "Scene",
      "type": "module",
      "children": [
        {
          "name": "Scene",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Song"
            },
            {
              "name": "clip_slots",
              "probed_type": "Vector"
            },
            {
              "name": "color",
              "probed_type": "int"
            },
            {
              "name": "color_index",
              "probed_type": "NoneType"
            },
            {
              "name": "is_empty",
              "probed_type": "bool"
            },
            {
              "name": "is_triggered",
              "probed_type": "bool"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "tempo",
              "probed_type": "float"
            },
            {
              "name": "tempo_enabled",
              "probed_type": "bool"
            },
            {
              "name": "time_signature_denominator",
              "probed_type": "int"
            },
            {
              "name": "time_signature_enabled",
              "probed_type": "bool"
            },
            {
              "name": "time_signature_numerator",
              "probed_type": "int"
            }
          ]
        }
      ]
    },
    {
      "name": "ShifterDevice",
      "type": "module",
      "children": [
        {
          "name": "ShifterDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "pitch_bend_range",
              "probed_type": "int"
            },
            {
              "name": "pitch_mode_index",
              "probed_type": "int"
            },
            {
              "name": "pitch_mode_list",
              "probed_type": "StringVector"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "SimplerDevice",
      "type": "module",
      "children": [
        {
          "name": "PlaybackMode",
          "type": "enum"
        },
        {
          "name": "SimplerDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class",
              "children": [
                {
                  "name": "_live_ptr",
                  "probed_type": "int"
                },
                {
                  "name": "canonical_parent",
                  "probed_type": "SimplerDevice"
                },
                {
                  "name": "is_collapsed",
                  "probed_type": "bool"
                },
                {
                  "name": "sample_end",
                  "probed_type": "int"
                },
                {
                  "name": "sample_env_fade_in",
                  "probed_type": "int"
                },
                {
                  "name": "sample_env_fade_out",
                  "probed_type": "int"
                },
                {
                  "name": "sample_loop_end",
                  "probed_type": "int"
                },
                {
                  "name": "sample_loop_fade",
                  "probed_type": "int"
                },
                {
                  "name": "sample_loop_start",
                  "probed_type": "int"
                },
                {
                  "name": "sample_start",
                  "probed_type": "int"
                },
                {
                  "name": "selected_slice",
                  "probed_type": "int"
                }
              ]
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "can_warp_as",
              "probed_type": "bool"
            },
            {
              "name": "can_warp_double",
              "probed_type": "bool"
            },
            {
              "name": "can_warp_half",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "multi_sample_mode",
              "probed_type": "bool"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "note_pitch_bend_range",
              "probed_type": "int"
            },
            {
              "name": "pad_slicing",
              "probed_type": "bool"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "pitch_bend_range",
              "probed_type": "int"
            },
            {
              "name": "playback_mode",
              "probed_type": "int"
            },
            {
              "name": "playing_position",
              "probed_type": "float"
            },
            {
              "name": "playing_position_enabled",
              "probed_type": "bool"
            },
            {
              "name": "retrigger",
              "probed_type": "bool"
            },
            {
              "name": "sample",
              "probed_type": "Sample"
            },
            {
              "name": "slicing_playback_mode",
              "probed_type": "int"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            },
            {
              "name": "voices",
              "probed_type": "int"
            }
          ]
        },
        {
          "name": "SlicingPlaybackMode",
          "type": "enum"
        }
      ]
    },
    {
      "name": "Song",
      "type": "module",
      "children": [
        {
          "name": "BeatTime",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "bars",
              "probed_type": "int"
            },
            {
              "name": "beats",
              "probed_type": "int"
            },
            {
              "name": "sub_division",
              "probed_type": "int"
            },
            {
              "name": "ticks",
              "probed_type": "int"
            }
          ]
        },
        {
          "name": "CaptureDestination",
          "type": "enum"
        },
        {
          "name": "CaptureMode",
          "type": "enum"
        },
        {
          "name": "CuePoint",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Song"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "time",
              "probed_type": "float"
            }
          ]
        },
        {
          "name": "Quantization",
          "type": "enum"
        },
        {
          "name": "RecordingQuantization",
          "type": "enum"
        },
        {
          "name": "SessionRecordStatus",
          "type": "enum"
        },
        {
          "name": "SmptTime",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "frames",
              "probed_type": "int"
            },
            {
              "name": "hours",
              "probed_type": "int"
            },
            {
              "name": "minutes",
              "probed_type": "int"
            },
            {
              "name": "seconds",
              "probed_type": "int"
            }
          ]
        },
        {
          "name": "Song",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class",
              "children": [
                {
                  "name": "_live_ptr",
                  "probed_type": "int"
                },
                {
                  "name": "canonical_parent",
                  "probed_type": "Song"
                },
                {
                  "name": "detail_clip",
                  "probed_type": "Clip"
                },
                {
                  "name": "draw_mode",
                  "probed_type": "bool"
                },
                {
                  "name": "follow_song",
                  "probed_type": "bool"
                },
                {
                  "name": "highlighted_clip_slot",
                  "probed_type": "ClipSlot"
                },
                {
                  "name": "selected_chain",
                  "probed_type": "NoneType"
                },
                {
                  "name": "selected_parameter",
                  "probed_type": "NoneType"
                },
                {
                  "name": "selected_scene",
                  "probed_type": "Scene"
                },
                {
                  "name": "selected_track",
                  "probed_type": "Track"
                }
              ]
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "appointed_device",
              "probed_type": "NoneType"
            },
            {
              "name": "arrangement_overdub",
              "probed_type": "bool"
            },
            {
              "name": "back_to_arranger",
              "probed_type": "bool"
            },
            {
              "name": "can_capture_midi",
              "probed_type": "bool"
            },
            {
              "name": "can_jump_to_next_cue",
              "probed_type": "bool"
            },
            {
              "name": "can_jump_to_prev_cue",
              "probed_type": "bool"
            },
            {
              "name": "can_redo",
              "probed_type": "bool"
            },
            {
              "name": "can_undo",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "NoneType"
            },
            {
              "name": "clip_trigger_quantization",
              "probed_type": "Quantization"
            },
            {
              "name": "count_in_duration",
              "probed_type": "int"
            },
            {
              "name": "cue_points",
              "probed_type": "Vector"
            },
            {
              "name": "current_song_time",
              "probed_type": "float"
            },
            {
              "name": "exclusive_arm",
              "probed_type": "bool"
            },
            {
              "name": "exclusive_solo",
              "probed_type": "bool"
            },
            {
              "name": "file_path",
              "probed_type": "str"
            },
            {
              "name": "groove_amount",
              "probed_type": "float"
            },
            {
              "name": "groove_pool",
              "probed_type": "GroovePool"
            },
            {
              "name": "is_ableton_link_enabled",
              "probed_type": "bool"
            },
            {
              "name": "is_ableton_link_start_stop_sync_enabled",
              "probed_type": "bool"
            },
            {
              "name": "is_counting_in",
              "probed_type": "bool"
            },
            {
              "name": "is_playing",
              "probed_type": "bool"
            },
            {
              "name": "last_event_time",
              "probed_type": "float"
            },
            {
              "name": "loop",
              "probed_type": "bool"
            },
            {
              "name": "loop_length",
              "probed_type": "float"
            },
            {
              "name": "loop_start",
              "probed_type": "float"
            },
            {
              "name": "master_track",
              "probed_type": "Track"
            },
            {
              "name": "metronome",
              "probed_type": "bool"
            },
            {
              "name": "midi_recording_quantization",
              "probed_type": "RecordingQuantization"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "nudge_down",
              "probed_type": "bool"
            },
            {
              "name": "nudge_up",
              "probed_type": "bool"
            },
            {
              "name": "overdub",
              "probed_type": "bool"
            },
            {
              "name": "punch_in",
              "probed_type": "bool"
            },
            {
              "name": "punch_out",
              "probed_type": "bool"
            },
            {
              "name": "re_enable_automation_enabled",
              "probed_type": "bool"
            },
            {
              "name": "record_mode",
              "probed_type": "bool"
            },
            {
              "name": "return_tracks",
              "probed_type": "Vector"
            },
            {
              "name": "root_note",
              "probed_type": "int"
            },
            {
              "name": "scale_intervals",
              "probed_type": "IntVector"
            },
            {
              "name": "scale_mode",
              "probed_type": "bool"
            },
            {
              "name": "scale_name",
              "probed_type": "str"
            },
            {
              "name": "scenes",
              "probed_type": "Vector"
            },
            {
              "name": "select_on_launch",
              "probed_type": "bool"
            },
            {
              "name": "session_automation_record",
              "probed_type": "bool"
            },
            {
              "name": "session_record",
              "probed_type": "bool"
            },
            {
              "name": "session_record_status",
              "probed_type": "int"
            },
            {
              "name": "signature_denominator",
              "probed_type": "int"
            },
            {
              "name": "signature_numerator",
              "probed_type": "int"
            },
            {
              "name": "song_length",
              "probed_type": "float"
            },
            {
              "name": "start_time",
              "probed_type": "float"
            },
            {
              "name": "swing_amount",
              "probed_type": "float"
            },
            {
              "name": "tempo",
              "probed_type": "float"
            },
            {
              "name": "tempo_follower_enabled",
              "probed_type": "bool"
            },
            {
              "name": "tracks",
              "probed_type": "Vector"
            },
            {
              "name": "tuning_system",
              "probed_type": "TuningSystem"
            },
            {
              "name": "view",
              "probed_type": "View"
            },
            {
              "name": "visible_tracks",
              "probed_type": "Vector"
            }
          ]
        },
        {
          "name": "TimeFormat",
          "type": "enum"
        }
      ]
    },
    {
      "name": "SpectralResonatorDevice",
      "type": "module",
      "children": [
        {
          "name": "SpectralResonatorDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "frequency_dial_mode",
              "probed_type": "int"
            },
            {
              "name": "frequency_dial_mode_list",
              "probed_type": "StringVector"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "midi_gate",
              "probed_type": "int"
            },
            {
              "name": "midi_gate_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mod_mode",
              "probed_type": "int"
            },
            {
              "name": "mod_mode_list",
              "probed_type": "StringVector"
            },
            {
              "name": "mono_poly",
              "probed_type": "int"
            },
            {
              "name": "mono_poly_list",
              "probed_type": "StringVector"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "pitch_bend_range",
              "probed_type": "int"
            },
            {
              "name": "pitch_mode",
              "probed_type": "int"
            },
            {
              "name": "pitch_mode_list",
              "probed_type": "StringVector"
            },
            {
              "name": "polyphony",
              "probed_type": "int"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "TakeLane",
      "type": "module",
      "children": [
        {
          "name": "TakeLane",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "arrangement_clips",
              "probed_type": "Vector"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "name",
              "probed_type": "str"
            }
          ]
        }
      ]
    },
    {
      "name": "Track",
      "type": "module",
      "children": [
        {
          "name": "DeviceContainer",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr"
            }
          ]
        },
        {
          "name": "DeviceInsertMode",
          "type": "enum"
        },
        {
          "name": "RoutingChannel",
          "type": "class",
          "children": [
            {
              "name": "display_name",
              "probed_type": "str"
            },
            {
              "name": "layout",
              "probed_type": "RoutingChannelLayout"
            }
          ]
        },
        {
          "name": "RoutingChannelLayout",
          "type": "enum"
        },
        {
          "name": "RoutingChannelVector",
          "type": "class"
        },
        {
          "name": "RoutingType",
          "type": "class",
          "children": [
            {
              "name": "attached_object",
              "probed_type": "Track"
            },
            {
              "name": "category",
              "probed_type": "int"
            },
            {
              "name": "display_name",
              "probed_type": "str"
            }
          ]
        },
        {
          "name": "RoutingTypeCategory",
          "type": "enum"
        },
        {
          "name": "RoutingTypeVector",
          "type": "class"
        },
        {
          "name": "Track",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class",
              "children": [
                {
                  "name": "_live_ptr",
                  "probed_type": "int"
                },
                {
                  "name": "canonical_parent",
                  "probed_type": "Track"
                },
                {
                  "name": "device_insert_mode",
                  "probed_type": "bool"
                },
                {
                  "name": "is_collapsed",
                  "probed_type": "bool"
                },
                {
                  "name": "selected_device",
                  "probed_type": "Device"
                }
              ]
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "arm",
              "probed_type": "bool"
            },
            {
              "name": "arrangement_clips",
              "probed_type": "Vector"
            },
            {
              "name": "available_input_routing_channels",
              "probed_type": "RoutingChannelVector"
            },
            {
              "name": "available_input_routing_types",
              "probed_type": "RoutingTypeVector"
            },
            {
              "name": "available_output_routing_channels",
              "probed_type": "RoutingChannelVector"
            },
            {
              "name": "available_output_routing_types",
              "probed_type": "RoutingTypeVector"
            },
            {
              "name": "back_to_arranger",
              "probed_type": "bool"
            },
            {
              "name": "can_be_armed",
              "probed_type": "bool"
            },
            {
              "name": "can_be_frozen",
              "probed_type": "bool"
            },
            {
              "name": "can_show_chains",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Song"
            },
            {
              "name": "clip_slots",
              "probed_type": "Vector"
            },
            {
              "name": "color",
              "probed_type": "int"
            },
            {
              "name": "color_index",
              "probed_type": "int"
            },
            {
              "name": "current_input_routing",
              "probed_type": "str"
            },
            {
              "name": "current_input_sub_routing",
              "probed_type": "str"
            },
            {
              "name": "current_monitoring_state",
              "probed_type": "int"
            },
            {
              "name": "current_output_routing",
              "probed_type": "str"
            },
            {
              "name": "current_output_sub_routing",
              "probed_type": "str"
            },
            {
              "name": "devices",
              "probed_type": "Vector"
            },
            {
              "name": "fired_slot_index",
              "probed_type": "int"
            },
            {
              "name": "fold_state",
              "probed_type": "bool"
            },
            {
              "name": "group_track",
              "probed_type": "Track"
            },
            {
              "name": "has_audio_input",
              "probed_type": "bool"
            },
            {
              "name": "has_audio_output",
              "probed_type": "bool"
            },
            {
              "name": "has_midi_input",
              "probed_type": "bool"
            },
            {
              "name": "has_midi_output",
              "probed_type": "bool"
            },
            {
              "name": "implicit_arm",
              "probed_type": "bool"
            },
            {
              "name": "input_meter_left",
              "probed_type": "float"
            },
            {
              "name": "input_meter_level",
              "probed_type": "float"
            },
            {
              "name": "input_meter_right",
              "probed_type": "float"
            },
            {
              "name": "input_routing_channel",
              "probed_type": "RoutingChannel"
            },
            {
              "name": "input_routing_type",
              "probed_type": "RoutingType"
            },
            {
              "name": "input_routings",
              "probed_type": "StringVector"
            },
            {
              "name": "input_sub_routings",
              "probed_type": "StringVector"
            },
            {
              "name": "is_foldable",
              "probed_type": "bool"
            },
            {
              "name": "is_frozen",
              "probed_type": "bool"
            },
            {
              "name": "is_grouped",
              "probed_type": "bool"
            },
            {
              "name": "is_part_of_selection",
              "probed_type": "bool"
            },
            {
              "name": "is_showing_chains",
              "probed_type": "bool"
            },
            {
              "name": "is_visible",
              "probed_type": "bool"
            },
            {
              "name": "mixer_device",
              "probed_type": "MixerDevice"
            },
            {
              "name": "monitoring_states",
              "type": "enum"
            },
            {
              "name": "mute",
              "probed_type": "bool"
            },
            {
              "name": "muted_via_solo",
              "probed_type": "bool"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "output_meter_left",
              "probed_type": "float"
            },
            {
              "name": "output_meter_level",
              "probed_type": "float"
            },
            {
              "name": "output_meter_right",
              "probed_type": "float"
            },
            {
              "name": "output_routing_channel",
              "probed_type": "RoutingChannel"
            },
            {
              "name": "output_routing_type",
              "probed_type": "RoutingType"
            },
            {
              "name": "output_routings",
              "probed_type": "StringVector"
            },
            {
              "name": "output_sub_routings",
              "probed_type": "StringVector"
            },
            {
              "name": "performance_impact",
              "probed_type": "float"
            },
            {
              "name": "playing_slot_index",
              "probed_type": "int"
            },
            {
              "name": "solo",
              "probed_type": "bool"
            },
            {
              "name": "take_lanes",
              "probed_type": "Vector"
            },
            {
              "name": "view",
              "probed_type": "View"
            }
          ]
        }
      ]
    },
    {
      "name": "TuningSystem",
      "type": "module",
      "children": [
        {
          "name": "PitchClassAndOctave",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "index_in_octave",
              "probed_type": "int"
            },
            {
              "name": "octave",
              "probed_type": "int"
            }
          ]
        },
        {
          "name": "ReferencePitch",
          "type": "class",
          "constructable": true,
          "children": [
            {
              "name": "frequency",
              "probed_type": "float"
            },
            {
              "name": "index_in_octave",
              "probed_type": "int"
            },
            {
              "name": "octave",
              "probed_type": "int"
            }
          ]
        },
        {
          "name": "TuningSystem",
          "type": "class",
          "children": [
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Song"
            },
            {
              "name": "highest_note",
              "probed_type": "PitchClassAndOctave"
            },
            {
              "name": "lowest_note",
              "probed_type": "PitchClassAndOctave"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "note_tunings",
              "probed_type": "list"
            },
            {
              "name": "number_of_notes_in_pseudo_octave",
              "probed_type": "int"
            },
            {
              "name": "pseudo_octave_in_cents",
              "probed_type": "float"
            },
            {
              "name": "reference_pitch",
              "probed_type": "ReferencePitch"
            }
          ]
        }
      ]
    },
    {
      "name": "WavetableDevice",
      "type": "module",
      "children": [
        {
          "name": "EffectMode",
          "type": "enum"
        },
        {
          "name": "FilterRouting",
          "type": "enum"
        },
        {
          "name": "ModulationSource",
          "type": "enum"
        },
        {
          "name": "UnisonMode",
          "type": "enum"
        },
        {
          "name": "VoiceCount",
          "type": "enum"
        },
        {
          "name": "Voicing",
          "type": "enum"
        },
        {
          "name": "WavetableDevice",
          "type": "class",
          "children": [
            {
              "name": "View",
              "type": "class"
            },
            {
              "name": "_live_ptr",
              "probed_type": "int"
            },
            {
              "name": "can_compare_ab",
              "probed_type": "bool"
            },
            {
              "name": "can_have_chains",
              "probed_type": "bool"
            },
            {
              "name": "can_have_drum_pads",
              "probed_type": "bool"
            },
            {
              "name": "canonical_parent",
              "probed_type": "Track"
            },
            {
              "name": "class_display_name",
              "probed_type": "str"
            },
            {
              "name": "class_name",
              "probed_type": "str"
            },
            {
              "name": "filter_routing",
              "probed_type": "int"
            },
            {
              "name": "is_active",
              "probed_type": "bool"
            },
            {
              "name": "is_using_compare_preset_b",
              "probed_type": "bool"
            },
            {
              "name": "latency_in_ms",
              "probed_type": "float"
            },
            {
              "name": "latency_in_samples",
              "probed_type": "int"
            },
            {
              "name": "mono_poly",
              "probed_type": "int"
            },
            {
              "name": "name",
              "probed_type": "str"
            },
            {
              "name": "oscillator_1_effect_mode",
              "probed_type": "int"
            },
            {
              "name": "oscillator_1_wavetable_category",
              "probed_type": "int"
            },
            {
              "name": "oscillator_1_wavetable_index",
              "probed_type": "int"
            },
            {
              "name": "oscillator_1_wavetables",
              "probed_type": "StringVector"
            },
            {
              "name": "oscillator_2_effect_mode",
              "probed_type": "int"
            },
            {
              "name": "oscillator_2_wavetable_category",
              "probed_type": "int"
            },
            {
              "name": "oscillator_2_wavetable_index",
              "probed_type": "int"
            },
            {
              "name": "oscillator_2_wavetables",
              "probed_type": "StringVector"
            },
            {
              "name": "oscillator_wavetable_categories",
              "probed_type": "StringVector"
            },
            {
              "name": "parameters",
              "probed_type": "ATimeableValueVector"
            },
            {
              "name": "poly_voices",
              "probed_type": "int"
            },
            {
              "name": "type",
              "probed_type": "DeviceType"
            },
            {
              "name": "unison_mode",
              "probed_type": "int"
            },
            {
              "name": "unison_voice_count",
              "probed_type": "int"
            },
            {
              "name": "view",
              "probed_type": "View"
            },
            {
              "name": "visible_modulation_target_names",
              "probed_type": "StringVector"
            }
          ]
        }
      ]
    }
  ]
}
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


## Reference Documentation

These are curated API reference docs with probed function signatures, parameter names, and types. When these docs show explicit parameter names in function signatures (e.g. `load_item(item)`, `insert_step(start, length, value)`), use those names directly.

### reference/devices/CcControlDevice.md

# CcControlDevice

> `Live.CcControlDevice.CcControlDevice`

This class represents a CC Control device in Live. CcControlDevice is a Device subclass that sends MIDI CC
(Continuous Controller) messages. It exposes 12 continuous CC target slots (`custom_float_target_0` through
`_11`) and 1 toggle CC target slot (`custom_bool_target`), each with a corresponding options list. All 13
targets select from the same 120-item MIDI CC name list. A `resend()` method retransmits all current CC
values.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"CcControlDevice"`.
    - **`class_name`:** `"MidiCcControl"`. **`class_display_name`:** `"CC Control"`.
    - **`type`:** 4 (`MIDI_EFFECT`).
    - **Insert name:** `"CC Control"` (matches `class_display_name`).
    - **All 13 target properties** are `int` (index into the CC name list). Default: `0` for float targets,
      `64` for bool target. All settable, all listenable.
    - **All 13 list properties** return identical `list[str]` of 120 MIDI CC names:
      `["None", "1: Modulation Wheel", "2: Breath Controller", ..., "119: Undefined"]`.
    - **`resend()`** returns `None`, executes without error.
    - **ChoiceProperty pattern:** Each target + list pair is a natural fit for `ChoiceProperty`.

### Children

| Child        | Returns                     | Shape    | Listenable | Summary                                        |
| ------------ | --------------------------- | -------- | ---------- | ---------------------------------------------- |
| `parameters` | `Sequence[DeviceParameter]` | `list`   | yes        | Automatable parameters exposed by this device. |
| `view`       | `CcControlDevice.View`      | `single` | no         | View aspects of the device (collapse state).   |

### Properties

| Property                      | Type        | Settable | Listenable | Summary                        |
| ----------------------------- | ----------- | -------- | ---------- | ------------------------------ |
| `custom_float_target_0`       | `int`       | yes      | yes        | CC target slot 0 (index).      |
| `custom_float_target_0_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 0.  |
| `custom_float_target_1`       | `int`       | yes      | yes        | CC target slot 1 (index).      |
| `custom_float_target_1_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 1.  |
| `custom_float_target_2`       | `int`       | yes      | yes        | CC target slot 2.              |
| `custom_float_target_2_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 2.  |
| `custom_float_target_3`       | `int`       | yes      | yes        | CC target slot 3.              |
| `custom_float_target_3_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 3.  |
| `custom_float_target_4`       | `int`       | yes      | yes        | CC target slot 4.              |
| `custom_float_target_4_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 4.  |
| `custom_float_target_5`       | `int`       | yes      | yes        | CC target slot 5.              |
| `custom_float_target_5_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 5.  |
| `custom_float_target_6`       | `int`       | yes      | yes        | CC target slot 6.              |
| `custom_float_target_6_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 6.  |
| `custom_float_target_7`       | `int`       | yes      | yes        | CC target slot 7.              |
| `custom_float_target_7_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 7.  |
| `custom_float_target_8`       | `int`       | yes      | yes        | CC target slot 8.              |
| `custom_float_target_8_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 8.  |
| `custom_float_target_9`       | `int`       | yes      | yes        | CC target slot 9.              |
| `custom_float_target_9_list`  | `list[str]` | no       | no         | 120 MIDI CC names for slot 9.  |
| `custom_float_target_10`      | `int`       | yes      | yes        | CC target slot 10.             |
| `custom_float_target_10_list` | `list[str]` | no       | no         | 120 MIDI CC names for slot 10. |
| `custom_float_target_11`      | `int`       | yes      | yes        | CC target slot 11.             |
| `custom_float_target_11_list` | `list[str]` | no       | no         | 120 MIDI CC names for slot 11. |
| `custom_bool_target`          | `int`       | yes      | yes        | Toggle CC target (index).      |
| `custom_bool_target_list`     | `list[str]` | no       | no         | 120 MIDI CC names for toggle.  |

All 13 lists are identical — 120 entries from `"None"` through `"119: Undefined"`, covering standard MIDI CC
assignments (Modulation Wheel, Breath Controller, Volume, Pan, Sustain, etc.).

### Methods

| Method     | Returns | Summary                           |
| ---------- | ------- | --------------------------------- |
| `resend()` | `None`  | Retransmit all current CC values. |

---

## CcControlDevice.View

Represents the view aspects of a CcControlDevice. Identical to `Device.View`.

### Properties

| Property       | Type   | Settable | Listenable | Summary                                             |
| -------------- | ------ | -------- | ---------- | --------------------------------------------------- |
| `is_collapsed` | `bool` | yes      | yes        | Whether the device is shown collapsed in the chain. |


### reference/devices/CompressorDevice.md

# CompressorDevice

> `Live.CompressorDevice.CompressorDevice`

This class represents a Compressor device in Live. A CompressorDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for sidechain input routing.

The sidechain routing properties let you select the audio source feeding the compressor's
sidechain detector. The available routing options mirror those shown in Live's sidechain
section of the Compressor UI.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"CompressorDevice"`.
    - **class_name:** `"Compressor2"`.
    - **class_display_name:** `"Compressor"`.
    - **Device type:** Audio Effect.
    - Routing properties use the same `RoutingType`/`RoutingChannel` serialization as track routing
      (bridge encodes with `_pfl_type` markers, `display_name`, `category`/`layout`, `attached_object`).
    - Default `input_routing_type`: `"No Input"` (category 6, no attached object).
    - Default `input_routing_channel`: `""` (layout 2).
    - `available_input_routing_types` in a fresh 4-track set: `["3-Audio", "4-Audio", "A-Reverb",
      "B-Delay", "Main", "No Input"]` — same routing type categories as track routing.
    - Setting `input_routing_type` to a value from `available_input_routing_types` works; read-back
      matches the set value.
    - All 4 properties are listenable (confirmed via `listen`/`unlisten` round-trip).
    - In a default set, all routing types show a single channel with `display_name=""`, `layout=2`.
      Multi-channel routing (e.g., L/R sub-channels) would appear with multi-output tracks.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), CompressorDevice adds:

| Property                           | Type                   | Settable | Listenable | Summary                                                |
| ---------------------------------- | ---------------------- | -------- | ---------- | ------------------------------------------------------ |
| `available_input_routing_channels` | `list[RoutingChannel]` | no       | `yes`      | Available source channels for sidechain input routing. |
| `available_input_routing_types`    | `list[RoutingType]`    | no       | `yes`      | Available source types for sidechain input routing.    |
| `input_routing_channel`            | `RoutingChannel`       | yes      | `yes`      | Currently selected sidechain source channel.           |
| `input_routing_type`               | `RoutingType`          | yes      | `yes`      | Currently selected sidechain source type.              |

#### `available_input_routing_channels`

- **Type:** `list[RoutingChannel]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available source channels for input routing in the compressor's sidechain.
Each entry is a `RoutingChannel` with `display_name` and `layout` fields. The list updates
when the available routing options change (e.g., tracks are added or removed, or the routing
type changes). The listener fires when the list contents change.

#### `available_input_routing_types`

- **Type:** `list[RoutingType]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available source types for input routing in the compressor's sidechain. Each
entry is a `RoutingType` with `display_name`, `category`, and `attached_object` fields.
The list updates when available routing options change (e.g., tracks added/removed). The
listener fires when the list contents change.

#### `input_routing_channel`

- **Type:** `RoutingChannel` (get) · `RoutingChannel` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected source channel for the compressor's sidechain input routing. The
value is a `RoutingChannel` object with `display_name` and `layout` fields. Can be set to
any value found in `available_input_routing_channels`. Default: `RoutingChannel("", layout=2)`.

#### `input_routing_type`

- **Type:** `RoutingType` (get) · `RoutingType` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected source type for the compressor's sidechain input routing. The value
is a `RoutingType` object with `display_name`, `category`, and `attached_object` fields.
Can be set to any value found in `available_input_routing_types`. Default:
`RoutingType("No Input", category=6, attached_object=None)`.

### Methods

No additional methods beyond those inherited from Device (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`).

### Open Questions

- Does setting `input_routing_channel` or `input_routing_type` to an invalid value raise
  `ValueError` immediately, or is the error deferred? (Untested -- would require constructing
  an invalid routing object.)


### reference/devices/Device.md

# Device

> `Live.Device.Device`

This class represents a MIDI or audio DSP device in Live. A device lives in a track's
device chain (or inside a rack chain). All native Live instruments, audio effects, MIDI
effects, Max for Live devices, and third-party plug-ins are represented as Device objects.
Rack devices (`can_have_chains=True`) contain chains which themselves contain devices.

??? note "Raw probe notes (temporary)"
    - **`name` IS settable** -- `set name='Probe_Test'` succeeded with correct readback. Confirmed
      writable via the API. Restore also works.
    - **`type` values confirmed** -- Drift returns `1` (instrument), Audio Effect Rack returns `2`
      (audio_effect).
    - **`class_name` examples** -- Drift: `'Drift'`, Audio Effect Rack: `'AudioEffectGroupDevice'`.
    - **`can_compare_ab`** -- Drift: `True`, Audio Effect Rack: `False`.

### Open Questions

- What does `type` return for Max for Live devices vs third-party plug-ins?
- Does `is_active` reflect the device's own on/off state, the enclosing rack's state, or both? The stub
  says "false both when the device is off and when it's inside a rack device which is off" -- but does
  toggling the device's own activator from off to on fire the `is_active` listener even when the
  enclosing rack is off?
- What happens when calling `save_preset_to_compare_ab_slot()` on a device where `can_compare_ab`
  is `False`?

### Children

| Child        | Returns                     | Shape    | Listenable | Summary                                        |
| ------------ | --------------------------- | -------- | ---------- | ---------------------------------------------- |
| `parameters` | `Sequence[DeviceParameter]` | `list`   | `yes`      | Automatable parameters exposed by this device. |
| `view`       | `Device.View`               | `single` | `no`       | View aspects of the device (collapse state).   |

#### `parameters`

- **Type:** `Sequence[DeviceParameter]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of automatable parameters for this device. Only automatable parameters are accessible --
not all internal device state is exposed. The listener fires when the parameter list changes
(e.g., when a rack macro configuration changes). Index 0 is conventionally the device's on/off
toggle parameter.

#### `view`

- **Type:** `Device.View`
- **Listenable:** `no`
- **Since:** `<11`

View aspects of the device. Currently exposes only `is_collapsed`.

### Properties

| Property                    | Type    | Settable | Listenable | Summary                                                                     |
| --------------------------- | ------- | -------- | ---------- | --------------------------------------------------------------------------- |
| `can_compare_ab`            | `bool`  | no       | `no`       | Whether the device supports AB comparison.                                  |
| `can_have_chains`           | `bool`  | no       | `no`       | `True` for rack devices.                                                    |
| `can_have_drum_pads`        | `bool`  | no       | `no`       | `True` for Drum Racks.                                                      |
| `class_display_name`        | `str`   | no       | `no`       | Original device name as shown in browser (e.g. `"Operator"`).               |
| `class_name`                | `str`   | no       | `no`       | Internal class name (e.g. `"Operator"`, `"PluginDevice"`).                  |
| `is_active`                 | `bool`  | no       | `yes`      | `False` when device is off or enclosing rack is off.                        |
| `is_using_compare_preset_b` | `bool`  | no       | `yes`      | Whether preset B is loaded. Only valid if `can_compare_ab`.                 |
| `latency_in_ms`             | `float` | no       | `yes`      | Device latency in milliseconds.                                             |
| `latency_in_samples`        | `int`   | no       | `yes`      | Device latency in samples.                                                  |
| `name`                      | `str`   | `str`    | `yes`      | Device name as shown in title bar. Settable.                                |
| `type`                      | `int`   | no       | `no`       | Device type enum: 0=undefined, 1=instrument, 2=audio_effect, 4=midi_effect. |

#### `can_compare_ab`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `12.3`

`True` if the device supports the AB Compare feature. `False` for rack devices and devices
that don't have this capability (third-party plug-ins, Max for Live devices). Accessing
`is_using_compare_preset_b` or calling `save_preset_to_compare_ab_slot()` on a device where
this is `False` raises an error.

#### `can_have_chains`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for rack devices (Instrument Rack, Audio Effect Rack, MIDI Effect Rack, Drum Rack).
`False` for single devices (Operator, Compressor, plug-ins, etc.). When `True`, the device
has `chains` and/or `return_chains` children (accessible on the RackDevice subclass).

#### `can_have_drum_pads`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` only for Drum Racks. Drum Racks have `drum_pads` children in addition to chains.

#### `class_display_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

The original display name of the device class as shown in Live's browser and device header
(e.g. `"Operator"`, `"Auto Filter"`, `"Compressor"`). Does not change when the user renames
the device -- use `name` for the user-visible name.

#### `class_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

The internal Live class name for this device type. Examples: `"Drift"`, `"Operator"`,
`"Limiter"`, `"AudioEffectGroupDevice"` (Audio Effect Rack), `"MxDeviceAudioEffect"` (Max for
Live audio effect), `"PluginDevice"` (third-party VST/AU plug-in). Useful for programmatically
identifying device types.

#### `is_active`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`False` when the device is turned off (device activator) **or** when it's inside a rack
device that is turned off. This means a device can have `is_active=False` even if its own
activator is on -- because the parent rack is off. The Max docs note: "0 = either the device
itself or its enclosing Rack device is off."

#### `is_using_compare_preset_b`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `12.3`

`True` if the device has loaded the preset from compare slot B. Only relevant when
`can_compare_ab` is `True` -- accessing this property on a device that doesn't support
AB comparison raises an error.

#### `latency_in_ms`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.2`

The latency introduced by this device in milliseconds. Changes when the device's latency
compensation changes (e.g., oversampling, look-ahead settings).

#### `latency_in_samples`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `11.2`

The latency introduced by this device in samples. Sample-accurate companion to
`latency_in_ms`.

#### `name`

- **Type:** `str` (get) · `str` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The name of the device as shown in the device title bar. For unmodified devices, this
matches `class_display_name`. Users can rename devices in the Live UI, and this property
can also be set programmatically to rename a device.

#### `type`

- **Type:** `int` (`Device.DeviceType`)
- **Listenable:** `no`
- **Since:** `<11`

The type of the device as a `DeviceType` enum value:

- `0` = undefined
- `1` = instrument
- `2` = audio_effect
- `4` = midi_effect

Note the gap: there is no value `3`. The Max docs confirm these values.

### Methods

| Method                                        | Returns | Summary                                                 |
| --------------------------------------------- | ------- | ------------------------------------------------------- |
| `save_preset_to_compare_ab_slot()`            | `None`  | Save current state to the AB compare slot.              |
| `store_chosen_bank(script_index, bank_index)` | `None`  | Set selected bank for hardware control surface mapping. |

#### `save_preset_to_compare_ab_slot()`

- **Returns:** `None`
- **Raises:** Error if `can_compare_ab` is `False`.
- **Since:** `12.3`

Saves the device's current parameter state to the AB compare slot. After calling this, the
user can switch between preset A and preset B using the AB Compare button. Only works on
devices where `can_compare_ab` is `True`.

#### `store_chosen_bank(script_index, bank_index)`

- **Returns:** `None`
- **Args:**
    - `script_index: int`
    - `bank_index: int`
- **Since:** `<11`

Sets the selected bank in the device for persistency with a hardware control surface. The
Max docs note this is "usually not relevant" for general use. `script_index` identifies the
control surface script and `bank_index` identifies the bank within that script's mapping.

---

## Device.View

> `Live.Device.Device.View`

Represents the view aspects of a device.

### Properties

| Property       | Type   | Settable | Listenable | Summary                                             |
| -------------- | ------ | -------- | ---------- | --------------------------------------------------- |
| `is_collapsed` | `bool` | `bool`   | `yes`      | Whether the device is shown collapsed in the chain. |

#### `is_collapsed`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Controls whether the device is shown collapsed (minimized) in the device chain. `True` means
the device is collapsed to a narrow strip showing only its title bar; `False` means the full
device UI is visible.


### reference/devices/DeviceIO.md

# DeviceIO

> `Live.DeviceIO.DeviceIO`

This class represents a specific input or output bus of a device. DeviceIO objects expose
the routing configuration for a device endpoint -- the routing type (e.g., which track or
external input to use) and the routing channel within that type. DeviceIO is a standalone
class, not a Device subclass.

??? note "Raw probe notes (temporary)"
    Probed with Live 12.3.5 using a Max Audio Effect device inserted on a MIDI track.

    - Bridge returns `type: "DeviceIO"` for I/O bus objects. Each DeviceIO has its own OID.
    - `routing_type` and `routing_channel` use the **same** `RoutingType` / `RoutingChannel`
      serialization as Track routing -- `_pfl_type` markers with `display_name`, `category`/`layout`,
      and `attached_object`.
    - `available_routing_types` returns a list of `RoutingType` objects. Entries include external
      sources (`"Ext. In"`, `"Ext. Out"`), other tracks (with `attached_object` pointing to the
      Track OID), and `"No Input"` / `"No Output"` (category 6).
    - `available_routing_channels` returns a list of `RoutingChannel` objects. Contents depend on
      the selected routing type.
    - All four routing properties support listeners.
    - `default_external_routing_channel_is_none` is gettable and settable. Default is `False`.
      Setting to `True` round-trips correctly.
    - **Setter caveat:** The bridge's `_decode_routing_type_for_set` /
      `_decode_routing_channel_for_set` only map Track property names (`input_routing_type` ->
      `available_input_routing_types`). DeviceIO uses bare names (`routing_type` ->
      `available_routing_types`). Bridge needs two additional entries in its property-name maps to
      support DeviceIO setters.

### Properties

| Property                                   | Type                   | Settable | Listenable | Summary                                                         |
| ------------------------------------------ | ---------------------- | -------- | ---------- | --------------------------------------------------------------- |
| `available_routing_channels`               | `list[RoutingChannel]` | no       | `yes`      | Available routing channels for this bus.                        |
| `available_routing_types`                  | `list[RoutingType]`    | no       | `yes`      | Available routing types for this bus.                           |
| `default_external_routing_channel_is_none` | `bool`                 | yes      | `no`       | Whether the default channel for External routing types is none. |
| `routing_channel`                          | `RoutingChannel`       | yes      | `yes`      | The currently selected routing channel.                         |
| `routing_type`                             | `RoutingType`          | yes      | `yes`      | The currently selected routing type.                            |

#### `available_routing_channels`

- **Type:** `list[RoutingChannel]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available routing channels for this input/output bus. Each entry uses the same
`RoutingChannel` serialization as Track routing (`display_name`, `layout`). The contents depend on
the currently selected `routing_type`. The listener fires when the available channels change.

#### `available_routing_types`

- **Type:** `list[RoutingType]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available routing types for this input/output bus. Each entry uses the same
`RoutingType` serialization as Track routing (`display_name`, `category`, `attached_object`).
Listener fires when the available types change.

#### `default_external_routing_channel_is_none`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `no`
- **Since:** `11.0`

When `True`, the default routing channel for External routing types is set to none. Default is
`False`.

#### `routing_channel`

- **Type:** `RoutingChannel` (get) · `RoutingChannel` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected routing channel for this input/output bus. Uses the same `RoutingChannel`
serialization as Track routing. Can be set to any value found in `available_routing_channels`.

#### `routing_type`

- **Type:** `RoutingType` (get) · `RoutingType` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected routing type for this input/output bus. Uses the same `RoutingType`
serialization as Track routing. Can be set to any value found in `available_routing_types`.
Changing the routing type may cause `available_routing_channels` to update.

### Open Questions

- ~~What is the actual return type of `available_routing_channels` and `available_routing_types`?~~
  **Resolved:** Same `RoutingType`/`RoutingChannel` objects as Track routing, serialized identically.
- ~~What is the return type of `routing_channel` and `routing_type`?~~
  **Resolved:** Same serialization as Track routing with `_pfl_type` markers.
- ~~What does `default_external_routing_channel_is_none` do when set?~~
  **Resolved:** Settable, round-trips correctly, default `False`.
- ~~Does setting `routing_channel` or `routing_type` to an invalid value raise `ValueError`
  immediately, or is it deferred?~~ **Partially resolved:** Setter currently fails because bridge
  doesn't map DeviceIO property names. Once bridge is updated, error behavior should match Track
  routing (immediate `ValueError` from bridge's scan-and-match logic).


### reference/devices/DeviceParameter.md

# DeviceParameter

> `Live.DeviceParameter.DeviceParameter`

This class represents an automatable parameter within a MIDI or audio device. Each device
exposes a list of parameters that can be read, set, automated, and observed. Parameters
have a value range (`min`/`max`), a display representation, and metadata about whether they
are quantized (boolean/enum) or continuous (float).

To modify a parameter, set its `value` property. Use `begin_gesture()`/`end_gesture()` to
group rapid value changes into a single undo step (e.g., when recording automation from a
physical knob).

??? note "Raw probe notes (temporary)"
    - **`value` outside range raises** -- setting a value above `max` or below `min` raises
      `InternalError: "Invalid value. Check the parameters range with min/max"`. It does NOT clamp.
    - **`display_value` is read-only** -- attempting to set it raises a signature mismatch error
      (the API expects float, not str). Despite the stub's "Get/Set" docstring, this property is
      effectively read-only. Use `value` to change the parameter.
    - **`default_value` only for continuous** -- works on non-quantized params (e.g. returned `1.0`
      for Drift LP Freq). On quantized params, raises `InternalError: "There is no default value
      available for this type of parameter"`.
    - **`short_value_items` works** -- returned `['Off', 'On']` for a boolean parameter (same as
      `value_items` in this case). May differ for params with longer display names.
    - **`str_for_value()` works** -- `str_for_value(1.0)` returned `'20.0 kHz'` for Drift LP Freq.
    - **`automation_state`** confirmed: returns `0` (none) for a parameter with no automation.

### Open Questions

- What `original_name` returns for non-macro parameters (the stub says "the original name,
  unaffected of any renamings" -- but Max docs say "the name of a Macro parameter before its
  assignment"). Are these descriptions for different use cases?

### Properties

| Property            | Type            | Settable | Listenable | Summary                                                                |
| ------------------- | --------------- | -------- | ---------- | ---------------------------------------------------------------------- |
| `automation_state`  | `int`           | no       | `yes`      | 0=none, 1=active, 2=overridden.                                        |
| `default_value`     | `float`         | no       | `no`       | Default value. Only for non-quantized parameters; raises on quantized. |
| `display_value`     | `str`           | no       | `yes`      | Value as shown in the GUI (e.g. `"-12 dB"`, `"On"`). Read-only.        |
| `is_enabled`        | `bool`          | no       | `no`       | `False` if macro-mapped or disabled by Max.                            |
| `is_quantized`      | `bool`          | no       | `no`       | `True` for booleans and enums; `False` for continuous float.           |
| `max`               | `float`         | no       | `no`       | Upper bound of the allowed value range.                                |
| `min`               | `float`         | no       | `no`       | Lower bound of the allowed value range.                                |
| `name`              | `str`           | no       | `yes`      | Short parameter name as shown in automation chooser.                   |
| `original_name`     | `str`           | no       | `no`       | Original name before any renaming (e.g. macro assignment).             |
| `short_value_items` | `Sequence[str]` | no       | `no`       | Short names for quantized values. Only if `is_quantized`.              |
| `state`             | `int`           | no       | `yes`      | 0=enabled, 1=irrelevant, 2=disabled.                                   |
| `value`             | `float`         | `float`  | `yes`      | Internal value between `min` and `max`.                                |
| `value_items`       | `Sequence[str]` | no       | `no`       | Display names for quantized values. Only if `is_quantized`.            |

#### `automation_state`

- **Type:** `int` (`DeviceParameter.AutomationState`)
- **Listenable:** `yes`
- **Since:** `<11`

The automation state of this parameter:

- `0` = no automation (no automation lane exists or it's empty)
- `1` = automation active (automation is playing back)
- `2` = automation overridden (user has manually moved the parameter, overriding automation)

Use `re_enable_automation()` to clear the override state (transition from 2 back to 1).

#### `default_value`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `<11`

The default value for this parameter. Only available for non-quantized parameters
(`is_quantized=False`). Accessing this on a quantized parameter raises
`InternalError: "There is no default value available for this type of parameter"`.

#### `display_value`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `12.2`

The parameter value formatted for display, as shown in the Live GUI. Includes unit suffixes
where applicable (e.g. `"-12.0 dB"`, `"440 Hz"`, `"On"`, `"1/16"`). Read-only despite the
stub's "Get/Set" docstring -- attempting to set raises a type error. The Max docs list this
as observable. Use `str_for_value()` to format an arbitrary value without changing the
parameter.

#### `is_enabled`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` when the parameter's value can be modified directly by the user, automation, or MIDI
mapping. `False` when the parameter is macro-controlled, controlled by a `live.remote~`
object, or when Live has disabled it for other reasons. When `False`, setting `value` may
silently fail or raise -- needs probing.

#### `is_quantized`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for boolean toggles and enum/menu parameters. `False` for continuous float parameters
(knobs, sliders). When `True`, use `value_items` to get the display names for each possible
value. Note: some parameters that appear quantized in the UI (e.g., MIDI pitch) actually
report `is_quantized=False` because their internal representation is continuous.

#### `max`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `<11`

The upper bound of the allowed value range. `value` must be set within `[min, max]`.

#### `min`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `<11`

The lower bound of the allowed value range. `value` must be set within `[min, max]`.

#### `name`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

The short parameter name as shown in the automation chooser and device parameter list.
For macro parameters, this is the user-assigned name. The listener fires when the name
changes (e.g., when a macro is reassigned).

#### `original_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

The original name of the parameter, unaffected by user renaming. For macro parameters, this
is the name before the macro was assigned to a target parameter. For non-macro parameters,
likely the same as `name`.

#### `short_value_items`

- **Type:** `Sequence[str]`
- **Listenable:** `no`
- **Since:** `11.1`

Like `value_items`, but prefers short value names when available. Only valid when
`is_quantized=True` -- raises an error otherwise. For simple boolean parameters, returns the
same values as `value_items`. May differ for parameters with longer display names. Not
documented in the Max for Live docs; appears only in the stub.

#### `state`

- **Type:** `int` (`DeviceParameter.ParameterState`)
- **Listenable:** `yes`
- **Since:** `<11`

The active state of the parameter:

- `0` = enabled -- the parameter is active and can be changed.
- `1` = irrelevant -- the parameter can be changed but isn't active, so changes won't have
  an audible effect (e.g., a parameter for a disabled feature within the device).
- `2` = disabled -- the parameter cannot be changed.

#### `value`

- **Type:** `float` (get) · `float` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The internal value of the parameter, between `min` and `max`. Setting a value outside this
range raises `InternalError: "Invalid value. Check the parameters range with min/max"` -- it
does **not** clamp. For quantized parameters, the value is an integer cast to float (e.g.,
`0.0` for off, `1.0` for on). For continuous parameters, the value is a float in the device's
internal scale (not the display scale). Use `display_value` or `str_for_value()` for the
human-readable representation.

#### `value_items`

- **Type:** `Sequence[str]`
- **Listenable:** `no`
- **Since:** `<11`

The list of display names for each possible value of a quantized parameter. Indexed by the
parameter's integer value. Only valid when `is_quantized=True` -- raises an error otherwise.
For example, a filter type parameter might return `["LP12", "LP24", "BP6", "HP12", ...]`.

### Methods

| Method                        | Returns | Summary                                         |
| ----------------------------- | ------- | ----------------------------------------------- |
| `begin_gesture()`             | `None`  | Begin a modification gesture for undo grouping. |
| `end_gesture()`               | `None`  | End a modification gesture.                     |
| `re_enable_automation()`      | `None`  | Clear automation override for this parameter.   |
| `str_for_value(value: float)` | `str`   | Format a value as a display string with units.  |

#### `begin_gesture()`

- **Returns:** `None`
- **Since:** `<11`

Notifies Live that a sequence of `value` modifications should be treated as a single gesture
(one undo step). Call this before rapidly setting `value` multiple times (e.g., when recording
automation from a physical knob or MIDI controller). Must be paired with `end_gesture()`.

#### `end_gesture()`

- **Returns:** `None`
- **Since:** `<11`

Ends a parameter modification gesture started by `begin_gesture()`. All value changes between
`begin_gesture()` and `end_gesture()` are grouped into a single undo step.

#### `re_enable_automation()`

- **Returns:** `None`
- **Since:** `<11`

Re-enables automation playback for this parameter after it has been manually overridden.
Transitions `automation_state` from `2` (overridden) back to `1` (active). No effect if
automation is not overridden. This is the per-parameter equivalent of
`Song.re_enable_automation()` which re-enables all overridden parameters.

#### `str_for_value(value: float)`

- **Returns:** `str`
- **Args:**
    - `value: float` -- a value in the parameter's `[min, max]` range
- **Since:** `<11`

Returns a string representation of the given value, formatted the same way Live displays it.
The returned string can include unit suffixes like `"dB"`, `"Hz"`, `"%"`, etc. Use this for
display purposes -- to format an arbitrary value without actually changing the parameter.


### reference/devices/DriftDevice.md

# DriftDevice

> `Live.DriftDevice.DriftDevice`

This class represents a Drift synthesizer device in Live. DriftDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for accessing the modulation matrix, voice settings, and pitch bend range.

Drift's modulation matrix is exposed through a set of index/list property pairs. Each
pair lets you read or change which modulation source or target is selected in a given
slot. The `*_list` properties return the available option names; the `*_index` properties
return or set the currently selected index into that list.

??? note "Raw probe notes (temporary)"
    - Bridge type name: `"DriftDevice"`.
    - `class_name` = `"Drift"`, `class_display_name` = `"Drift"` (names match).
    - Device type = 1 (Instrument).
    - All `*_index` properties are **settable** (get+set+listen) -- confirmed by probe.
    - All `*_list` properties serialize as plain `list[str]` through the bridge
      (StringVector -> list).
    - `pitch_bend_range` valid range: 0-12. Setting 13+ throws `"Invalid Pitch Bend Range"`.
      Settable within range.
    - `voice_count_list` = `['4', '8', '16', '24', '32']` (5 entries).
    - `voice_mode_list` = `['Poly', 'Mono', 'Stereo', 'Unison']` (4 entries).
    - All mod matrix source lists share the same 8 entries: `['Env 1', 'Env 2', 'LFO', 'Key',
      'Vel', 'Mod', 'Press', 'Slide']`.
    - Target lists have 12 entries: `['None', 'Osc 1 Gain', 'Osc 1 Shape', 'Osc 2 Gain',
      'Osc 2 Detune', 'Noise Gain', 'LP Frequency', 'LP Resonance', 'HP Frequency', 'LFO Rate',
      'Cyc Env Rate', 'Main Volume']`.
    - Default `voice_count_index` = 4 (= 32 voices), `voice_mode_index` = 0 (Poly),
      `pitch_bend_range` = 2.
    - Default mod matrix index values: filter_source_1=1, filter_source_2=6, lfo_source=5,
      pitch_source_1=1, pitch_source_2=2, shape_source=7, source_1=5, source_2=4, source_3=6,
      target_1=8, target_2=0, target_3=0.

### Open Questions

None -- all questions resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
DriftDevice adds:

| Property                           | Type        | Settable | Listenable | Summary                                                 |
| ---------------------------------- | ----------- | -------- | ---------- | ------------------------------------------------------- |
| `mod_matrix_filter_source_1_index` | `int`       | `int`    | `yes`      | Selected source index for filter frequency mod slot 1.  |
| `mod_matrix_filter_source_1_list`  | `list[str]` | no       | `no`       | Available source names for filter frequency mod slot 1. |
| `mod_matrix_filter_source_2_index` | `int`       | `int`    | `yes`      | Selected source index for filter frequency mod slot 2.  |
| `mod_matrix_filter_source_2_list`  | `list[str]` | no       | `no`       | Available source names for filter frequency mod slot 2. |
| `mod_matrix_lfo_source_index`      | `int`       | `int`    | `yes`      | Selected source index for LFO amount modulation.        |
| `mod_matrix_lfo_source_list`       | `list[str]` | no       | `no`       | Available source names for LFO amount modulation.       |
| `mod_matrix_pitch_source_1_index`  | `int`       | `int`    | `yes`      | Selected source index for pitch mod slot 1.             |
| `mod_matrix_pitch_source_1_list`   | `list[str]` | no       | `no`       | Available source names for pitch mod slot 1.            |
| `mod_matrix_pitch_source_2_index`  | `int`       | `int`    | `yes`      | Selected source index for pitch mod slot 2.             |
| `mod_matrix_pitch_source_2_list`   | `list[str]` | no       | `no`       | Available source names for pitch mod slot 2.            |
| `mod_matrix_shape_source_index`    | `int`       | `int`    | `yes`      | Selected source index for shape modulation.             |
| `mod_matrix_shape_source_list`     | `list[str]` | no       | `no`       | Available source names for shape modulation.            |
| `mod_matrix_source_1_index`        | `int`       | `int`    | `yes`      | Selected source index for custom mod slot 1.            |
| `mod_matrix_source_1_list`         | `list[str]` | no       | `no`       | Available source names for custom mod slot 1.           |
| `mod_matrix_source_2_index`        | `int`       | `int`    | `yes`      | Selected source index for custom mod slot 2.            |
| `mod_matrix_source_2_list`         | `list[str]` | no       | `no`       | Available source names for custom mod slot 2.           |
| `mod_matrix_source_3_index`        | `int`       | `int`    | `yes`      | Selected source index for custom mod slot 3.            |
| `mod_matrix_source_3_list`         | `list[str]` | no       | `no`       | Available source names for custom mod slot 3.           |
| `mod_matrix_target_1_index`        | `int`       | `int`    | `yes`      | Selected target index for custom mod slot 1.            |
| `mod_matrix_target_1_list`         | `list[str]` | no       | `no`       | Available target names for custom mod slot 1.           |
| `mod_matrix_target_2_index`        | `int`       | `int`    | `yes`      | Selected target index for custom mod slot 2.            |
| `mod_matrix_target_2_list`         | `list[str]` | no       | `no`       | Available target names for custom mod slot 2.           |
| `mod_matrix_target_3_index`        | `int`       | `int`    | `yes`      | Selected target index for custom mod slot 3.            |
| `mod_matrix_target_3_list`         | `list[str]` | no       | `no`       | Available target names for custom mod slot 3.           |
| `pitch_bend_range`                 | `int`       | `int`    | `yes`      | MIDI pitch bend range in semitones (0-12). Settable.    |
| `voice_count_index`                | `int`       | `int`    | `yes`      | Index of the selected voice count setting.              |
| `voice_count_list`                 | `list[str]` | no       | `no`       | Available voice count setting names.                    |
| `voice_mode_index`                 | `int`       | `int`    | `yes`      | Index of the selected voice mode.                       |
| `voice_mode_list`                  | `list[str]` | no       | `no`       | Available voice mode names.                             |

#### `mod_matrix_filter_source_1_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_filter_source_1_list` for the currently selected modulation
source in filter frequency mod slot 1. Default: 1 (Env 2). Settable.

#### `mod_matrix_filter_source_1_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for filter frequency mod slot 1.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_filter_source_2_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_filter_source_2_list` for the currently selected modulation
source in filter frequency mod slot 2. Default: 6 (Press). Settable.

#### `mod_matrix_filter_source_2_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for filter frequency mod slot 2.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_lfo_source_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_lfo_source_list` for the currently selected modulation source
for the LFO amount. Default: 5 (Mod). Settable.

#### `mod_matrix_lfo_source_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for the LFO amount.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_pitch_source_1_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_pitch_source_1_list` for the currently selected modulation
source in pitch mod slot 1. Default: 1 (Env 2). Settable.

#### `mod_matrix_pitch_source_1_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for pitch mod slot 1.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_pitch_source_2_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_pitch_source_2_list` for the currently selected modulation
source in pitch mod slot 2. Default: 2 (LFO). Settable.

#### `mod_matrix_pitch_source_2_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for pitch mod slot 2.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_shape_source_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_shape_source_list` for the currently selected modulation
source for shape. Default: 7 (Slide). Settable.

#### `mod_matrix_shape_source_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for shape.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_source_1_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_source_1_list` for the currently selected source in custom
mod slot 1. Default: 5 (Mod). Settable -- confirmed by probe.

#### `mod_matrix_source_1_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for custom mod slot 1.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_source_2_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_source_2_list` for the currently selected source in custom
mod slot 2. Default: 4 (Vel). Settable.

#### `mod_matrix_source_2_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for custom mod slot 2.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_source_3_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_source_3_list` for the currently selected source in custom
mod slot 3. Default: 6 (Press). Settable.

#### `mod_matrix_source_3_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation source names for custom mod slot 3.
Values: `['Env 1', 'Env 2', 'LFO', 'Key', 'Vel', 'Mod', 'Press', 'Slide']`.

#### `mod_matrix_target_1_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_target_1_list` for the currently selected target in custom
mod slot 1. Default: 8 (HP Frequency). Settable -- confirmed by probe.

#### `mod_matrix_target_1_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation target names for custom mod slot 1.
Values: `['None', 'Osc 1 Gain', 'Osc 1 Shape', 'Osc 2 Gain', 'Osc 2 Detune',
'Noise Gain', 'LP Frequency', 'LP Resonance', 'HP Frequency', 'LFO Rate',
'Cyc Env Rate', 'Main Volume']`.

#### `mod_matrix_target_2_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_target_2_list` for the currently selected target in custom
mod slot 2. Default: 0 (None). Settable.

#### `mod_matrix_target_2_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation target names for custom mod slot 2.
Values: same as `mod_matrix_target_1_list`.

#### `mod_matrix_target_3_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `mod_matrix_target_3_list` for the currently selected target in custom
mod slot 3. Default: 0 (None). Settable.

#### `mod_matrix_target_3_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available modulation target names for custom mod slot 3.
Values: same as `mod_matrix_target_1_list`.

#### `pitch_bend_range`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The MIDI pitch bend range in semitones. Valid range: 0-12. Setting values >= 13 throws
`"Invalid Pitch Bend Range"`. Default: 2. Settable within valid range.

#### `voice_count_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `voice_count_list` for the currently selected voice count setting.
Default: 4 (= 32 voices). Settable -- confirmed by probe.

#### `voice_count_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available voice count setting names.
Values: `['4', '8', '16', '24', '32']`.

#### `voice_mode_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The index into `voice_mode_list` for the currently selected voice mode.
Default: 0 (Poly). Settable -- confirmed by probe.

#### `voice_mode_list`

- **Type:** `list[str]`
- **Listenable:** `no`
- **Since:** `11.3`

The list of available voice mode names.
Values: `['Poly', 'Mono', 'Stereo', 'Unison']`.


### reference/devices/DrumCellDevice.md

# DrumCellDevice

> `Live.DrumCellDevice.DrumCellDevice`

This class represents a Drum Cell (Drum Sampler) device in Live. DrumCellDevice is a subclass of Device -- it
has all the children, properties, and methods of Device plus one additional property for the sample gain level.

A DrumCellDevice appears as the built-in sampler inside each Drum Rack pad cell. It is not directly
insertable — it is automatically created when a sample is loaded into a Drum Rack pad.

??? note "Raw probe notes (temporary)"
    - Bridge type: `"DrumCellDevice"` (inferred from `type(obj).__name__` pattern; not directly probed
      because DrumCellDevice requires a sample loaded in a Drum Rack pad, which cannot be done
      programmatically via the current API).
    - The stub confirms `gain` has no setter — it is read-only with a listener.
    - DrumCellDevice is not insertable via `insert_device`. It appears automatically inside a Drum Rack
      pad chain when a sample is loaded into that pad.
    - Empty Drum Rack pads have no chains and no devices.

### Open Questions

- Exact range of `gain` not probed (requires a loaded sample). Presumed 0.0–1.0 based on Max docs.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), DrumCellDevice adds:

| Property | Type    | Settable | Listenable | Summary                       |
| -------- | ------- | -------- | ---------- | ----------------------------- |
| `gain`   | `float` | no       | yes        | The sample gain (normalized). |

#### `gain`

- **Type:** `float`
- **Listenable:** yes
- **Since:** `12.1`

The sample gain level as a normalized value (presumably 0.0 to 1.0). The listener fires when the gain value
changes. Read-only — the value reflects the current gain setting in the Drum Cell UI but cannot be changed
programmatically.


### reference/devices/Eq8Device.md

# Eq8Device

> `Live.Eq8Device.Eq8Device`

This class represents an EQ Eight device in Live. An Eq8Device is a subclass of Device --
it has all the children, properties, and methods of Device plus additional members for
controlling the EQ's global mode, edit mode, and oversampling.

EQ Eight can operate in three global modes (Stereo, L/R, M/S), each of which provides two
edit channels. The `edit_mode` and `global_mode` properties expose these settings
programmatically.

??? note "Raw probe notes (temporary)"
    - Bridge type: `"Eq8Device"`. `class_name`: `"Eq8"`.
    - `edit_mode` returns `bool` through the bridge (not `int`), despite the stub declaring it as
      `EditMode`. Setting `1` reads back as `True`, setting `0`/`False` reads back as `False`.
    - `global_mode` returns `int` (0, 1, 2). Settable and round-trips correctly.
    - `oversample` returns `bool`. Settable, round-trips correctly.
    - `view.selected_band` returns `int` (default 2 on fresh device). Settable (0-7), round-trips
      correctly.
    - All properties are listenable.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), Eq8Device adds:

| Property      | Type   | Settable | Listenable | Summary                                                         |
| ------------- | ------ | -------- | ---------- | --------------------------------------------------------------- |
| `edit_mode`   | `bool` | yes      | `yes`      | Which channel is selected for editing (depends on global mode). |
| `global_mode` | `int`  | yes      | `yes`      | The EQ's stereo processing mode (Stereo, L/R, or M/S).         |
| `oversample`  | `bool` | yes      | `yes`      | Whether oversampling is enabled.                                |

#### `edit_mode`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Controls which channel is currently available for editing. The meaning of the value depends
on the current `global_mode`:

- In L/R mode: `False` = Left, `True` = Right
- In M/S mode: `False` = Mid, `True` = Side
- In Stereo mode: `False` = channel A, `True` = channel B (inactive)

- **Quirks:**
    - Despite the stub declaring this as `EditMode`, the bridge serializes it as `bool`.

#### `global_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The EQ's stereo processing mode. The modes are encoded as:

- `0` = Stereo
- `1` = L/R
- `2` = M/S

Changing the global mode affects the available edit modes (see `edit_mode`).

#### `oversample`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Whether oversampling is enabled for the EQ. When on, the EQ processes at a higher internal
sample rate for improved accuracy at the cost of increased CPU usage.

### Methods

No additional methods beyond those inherited from Device (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`).

---

## Eq8Device.View

Represents the view aspects of an EQ Eight device. Extends Device.View with an additional
property for the selected filter band.

### Properties

In addition to `is_collapsed` (inherited from Device.View):

| Property        | Type  | Settable | Listenable | Summary                                          |
| --------------- | ----- | -------- | ---------- | ------------------------------------------------ |
| `selected_band` | `int` | yes      | `yes`      | The index of the currently selected filter band. |

#### `selected_band`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The index of the currently selected filter band in the EQ Eight UI. EQ Eight has 8 bands
(indices 0-7). The listener fires when the user selects a different band in the device UI.
Default value on a fresh device is 2.

### Open Questions

None -- all resolved by probing.


### reference/devices/HybridReverbDevice.md

# HybridReverbDevice

> `Live.HybridReverbDevice.HybridReverbDevice`

This class represents a Hybrid Reverb device in Live. HybridReverbDevice is a subclass
of Device -- it has all the children, properties, and methods of Device plus additional
members for managing the convolution impulse response (IR) selection and time-shaping
parameters.

Hybrid Reverb combines a convolution engine with an algorithmic reverb. The API exposes
properties for browsing and selecting IR files by category, adjusting the IR envelope
(attack, decay, size), and toggling time-shaping.

??? note "Raw probe notes (temporary)"
    - Bridge type name: `"HybridReverbDevice"`.
    - `class_name` = `"Hybrid"`, `class_display_name` = `"Hybrid Reverb"`.
    - Device type = 2 (Audio Effect).
    - All 8 properties are **settable** (get+set+listen), contrary to earlier docs that showed
      "-" for Set.
    - `ir_category_list` and `ir_file_list` serialize as plain `list[str]` through the bridge
      (StringVector -> list).
    - Changing `ir_category_index` dynamically updates `ir_file_list` (confirmed -- file list
      changed after category switch).
    - `ir_file_list` is listenable and fires when the category changes.
    - Float precision: `ir_decay_time` shows float32 artifacts (e.g. set 0.3 -> readback
      0.30000001192092896).
    - `ir_category_list` default = `['Early_Reflections', 'Real_Places',
      'Chambers_and_Large_Rooms', 'Made_for_Drums', 'Halls', 'Plates', 'Springs',
      'Bigger_Spaces', 'Textures', 'User']` (10 categories).

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
HybridReverbDevice adds:

| Property             | Type           | Settable | Listenable | Summary                                                      |
| -------------------- | -------------- | -------- | ---------- | ------------------------------------------------------------ |
| `ir_attack_time`     | `float`        | yes      | `yes`      | Attack time of the IR amplitude envelope, in seconds.        |
| `ir_category_index`  | `int`          | yes      | `yes`      | Index of the selected IR category.                           |
| `ir_category_list`   | `StringVector` | no       | `no`       | List of available IR category names.                         |
| `ir_decay_time`      | `float`        | yes      | `yes`      | Decay time of the IR amplitude envelope, in seconds.         |
| `ir_file_index`      | `int`          | yes      | `yes`      | Index of the selected IR file within the current category.   |
| `ir_file_list`       | `StringVector` | no       | `yes`      | List of IR file names in the selected category.              |
| `ir_size_factor`     | `float`        | yes      | `yes`      | Relative size of the IR, 0.0 to 1.0.                        |
| `ir_time_shaping_on` | `bool`         | yes      | `yes`      | Whether time-shaping (envelope + size) is applied to the IR. |

#### `ir_attack_time`

- **Type:** `float` (get) · `float` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The attack time of the amplitude envelope applied to the impulse response, in seconds.
Default: 0.0.

#### `ir_category_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The index of the currently selected impulse response category. Changing this value
selects a different category and updates `ir_file_list` accordingly. Default: 0.

#### `ir_category_list`

- **Type:** `StringVector` (serializes as `list[str]`)
- **Listenable:** `no`
- **Since:** `<11`

The list of available impulse response category names. Read-only.
Default: `['Early_Reflections', 'Real_Places', 'Chambers_and_Large_Rooms', 'Made_for_Drums',
'Halls', 'Plates', 'Springs', 'Bigger_Spaces', 'Textures', 'User']` (10 categories).

#### `ir_decay_time`

- **Type:** `float` (get) · `float` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The decay time of the amplitude envelope applied to the impulse response, in seconds.
Default: 20.0.

- **Quirks:**
    - Float32 precision artifacts may appear in readback (e.g. set 0.3 reads back as
      0.30000001192092896).

#### `ir_file_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The index of the currently selected impulse response file within the current category.
Default: 0.

#### `ir_file_list`

- **Type:** `StringVector` (serializes as `list[str]`)
- **Listenable:** `yes`
- **Since:** `<11`

The list of impulse response file names available in the currently selected category.
The listener fires when the category changes, causing the file list to update.
Read-only -- the list updates automatically when `ir_category_index` changes.

#### `ir_size_factor`

- **Type:** `float` (get) · `float` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The relative size of the impulse response, ranging from 0.0 to 1.0. Only effective when
`ir_time_shaping_on` is enabled. Default: 1.0.

#### `ir_time_shaping_on`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

When enabled (`True`), the selected impulse response is transformed by the amplitude
envelope (attack/decay) and size parameter. When disabled, the raw IR is used.
Default: True.

### Methods

No additional methods beyond those inherited from Device (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`).

### Open Questions

None -- all questions resolved by probing.


### reference/devices/LooperDevice.md

# LooperDevice

> `Live.LooperDevice.LooperDevice`

This class represents an instance of the Looper audio effect device in Live. A
LooperDevice is a subclass of Device -- it has all the children, properties, and methods
of Device plus additional members for controlling Looper's transport, buffer, and
recording behavior.

Looper is an audio effect that records incoming audio into a buffer and plays it back
in a loop. It supports overdubbing, speed/length manipulation, and exporting its
content to a clip slot.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"LooperDevice"`.
    - **class_name:** `"Looper"`.
    - **class_display_name:** `"Looper"`.
    - **Device type:** Audio Effect.
    - `loop_length` with no content: `0.0`. `tempo` with no content: `0.0`.
    - `overdub_after_record` default: `True`. Settable, round-trips.
    - `record_length_index` default: `10` (variable length). Range: 0-10.
    - `record_length_list`: 11 entries: `[' 1 bar', ' 2 bars', ..., '16 bars',
      ' x bars (variable length)']`. Note leading spaces in entry strings.
    - All 4 properties with listeners confirmed working (loop_length, overdub_after_record,
      record_length_index, tempo). `record_length_list` is NOT listenable.
    - All 11 methods return `None` and succeed (even on empty buffer for most).
    - `export_to_clip_slot`: raises `InternalError` if Looper has no audio content or audio
      engine is off. Takes a ClipSlot OID reference as argument.

### Children

None beyond those inherited from Device (`parameters`, `view`).

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
LooperDevice adds:

| Property               | Type           | Settable | Listenable | Summary                                             |
| ---------------------- | -------------- | -------- | ---------- | --------------------------------------------------- |
| `loop_length`          | `float`        | no       | `yes`      | Length of Looper's recorded buffer. 0.0 when empty. |
| `overdub_after_record` | `bool`         | yes      | `yes`      | Whether Looper enters overdub mode after recording. |
| `record_length_index`  | `int`          | yes      | `yes`      | Selected index in the Record Length chooser (0-10). |
| `record_length_list`   | `StringVector` | no       | `no`       | Available Record Length chooser entries (11 items).  |
| `tempo`                | `float`        | no       | `yes`      | Tempo of Looper's recorded buffer. 0.0 when empty.  |

#### `loop_length`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `12.0`

The length of Looper's recorded buffer. Read-only. Returns `0.0` when empty. The listener
fires when the buffer length changes (e.g., after recording, or after calling
`double_length()` or `half_length()`).

#### `overdub_after_record`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `12.0`

When `True`, Looper switches to overdub mode after finishing a fixed-length recording.
When `False`, Looper switches to playback without overdubbing after recording completes.
Default: `True`. Can be set at any time.

#### `record_length_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `12.0`

The currently selected index in the Record Length chooser (0-10). Corresponds to the
entries in `record_length_list`. Default: `10` (variable length). Controls how many bars
Looper will record before automatically stopping or switching to overdub/playback.

#### `record_length_list`

- **Type:** `StringVector` (serializes as `list[str]`)
- **Listenable:** `no`
- **Since:** `12.0`

Read-only list of the available Record Length chooser entry strings. Static 11 entries:
`[' 1 bar', ' 2 bars', ' 3 bars', ' 4 bars', ' 5 bars', ' 6 bars', ' 7 bars', ' 8 bars',
'12 bars', '16 bars', ' x bars (variable length)']`.
Note: entries have leading spaces for UI formatting alignment.

#### `tempo`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `12.0`

The tempo of Looper's recorded buffer. Read-only. Returns `0.0` when empty. The listener
fires when the buffer tempo changes (e.g., after calling `double_speed()` or
`half_speed()`).

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`), LooperDevice adds:

| Method                                     | Returns | Summary                                       |
| ------------------------------------------ | ------- | --------------------------------------------- |
| `clear()`                                  | `None`  | Erase all recorded content.                   |
| `double_length()`                          | `None`  | Double the buffer length.                     |
| `double_speed()`                           | `None`  | Double the playback speed.                    |
| `export_to_clip_slot(clip_slot: ClipSlot)` | `None`  | Export buffer content to a session clip slot.  |
| `half_length()`                            | `None`  | Halve the buffer length.                      |
| `half_speed()`                             | `None`  | Halve the playback speed.                     |
| `overdub()`                                | `None`  | Switch to overdub mode.                       |
| `play()`                                   | `None`  | Switch to playback mode.                      |
| `record()`                                 | `None`  | Start recording incoming audio.               |
| `stop()`                                   | `None`  | Stop playback.                                |
| `undo()`                                   | `None`  | Undo or redo the last overdub layer.          |

#### `clear()`

- **Returns:** `None`
- **Since:** `12.0`

Erase all recorded content from Looper's buffer.

#### `double_length()`

- **Returns:** `None`
- **Since:** `12.0`

Double the buffer length by duplicating the current content.

#### `double_speed()`

- **Returns:** `None`
- **Since:** `12.0`

Double the playback speed of the loop.

#### `export_to_clip_slot(clip_slot: ClipSlot)`

- **Returns:** `None`
- **Args:**
  - `clip_slot: ClipSlot` -- the session clip slot to export the buffer into
- **Raises:** `InternalError` if Looper has no audio content or audio engine is off.
- **Since:** `12.1`

Export the contents of Looper's buffer to the specified session clip slot.

#### `half_length()`

- **Returns:** `None`
- **Since:** `12.0`

Halve the buffer length by truncating.

#### `half_speed()`

- **Returns:** `None`
- **Since:** `12.0`

Halve the playback speed of the loop.

#### `overdub()`

- **Returns:** `None`
- **Since:** `12.0`

Switch Looper to overdub mode. Incoming audio is layered on top of the existing buffer content.

#### `play()`

- **Returns:** `None`
- **Since:** `12.0`

Switch Looper to playback mode.

#### `record()`

- **Returns:** `None`
- **Since:** `12.0`

Start recording incoming audio into the buffer.

#### `stop()`

- **Returns:** `None`
- **Since:** `12.0`

Stop playback.

#### `undo()`

- **Returns:** `None`
- **Since:** `12.0`

Undo or redo the last overdub layer. Acts as an undo/redo toggle on successive calls.

### Open Questions

- Does `undo()` toggle on successive calls? -- Confirmed per Max docs: acts as undo/redo toggle.


### reference/devices/MaxDevice.md

# MaxDevice

> `Live.MaxDevice.MaxDevice`

This class represents a Max for Live device in Live. A MaxDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for accessing the device's audio and MIDI I/O routing and parameter bank
configuration.

Max for Live devices can expose audio and MIDI inputs and outputs that are accessible
through the API, unlike standard Live devices.

??? note "Raw probe notes (temporary)"
    Probed with Live 12.3.5 using "Max Audio Effect", "Max Instrument", and "Max MIDI Effect".

    - Bridge returns `type: "MaxDevice"` for all M4L device types.
    - `class_name` is always `"MxDeviceAudioEffect"` regardless of M4L device kind (audio effect,
      instrument, or MIDI effect). The standard `Device.type` property distinguishes them.
    - All M4L devices expose `audio_inputs` and `audio_outputs` (at least one `DeviceIO` each for a
      blank device). `midi_inputs` and `midi_outputs` are empty for blank M4L devices -- they only
      appear when the Max patch exposes MIDI I/O objects.
    - All four I/O list properties are listenable (listener fires when the I/O configuration changes).
    - Each I/O list item is a `DeviceIO` object with its own OID and full routing capabilities.
    - `bank_parameters_changed` listener fires successfully (event-only, no readable property).
    - `get_bank_count()` returns `0` for blank M4L devices. `get_bank_name(0)` and
      `get_bank_parameters(0)` raise `InternalError` when bank count is 0.
      `get_bank_parameters(-1)` raises `"this device has no best-of bank"` for devices without
      configured banks.

### Open Questions

- ~~What type do the `audio_inputs` / `audio_outputs` / `midi_inputs` / `midi_outputs`
  lists contain?~~ **Resolved:** `DeviceIO` objects with their own OIDs and routing properties.
- ~~What triggers the `bank_parameters_changed` event?~~ **Partially resolved:** Listener registers
  successfully. Trigger condition not tested (would require editing a Max patch's bank configuration).
- ~~Does `get_value_item_icons()` work for all parameter types?~~ **Unprobed.** Needs an M4L device
  with list-style parameters.
- Bank methods (`get_bank_name`, `get_bank_parameters`) fail with `InternalError` when called with
  invalid indices or on devices with no banks. Need to test with an M4L device that has configured
  parameter banks.

### Children

None beyond those inherited from Device (`parameters`, `view`).

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
MaxDevice adds:

| Property        | Type             | Settable | Listenable | Summary                                   |
| --------------- | ---------------- | -------- | ---------- | ----------------------------------------- |
| `audio_inputs`  | `list[DeviceIO]` | no       | `yes`      | Audio inputs exposed by this M4L device.  |
| `audio_outputs` | `list[DeviceIO]` | no       | `yes`      | Audio outputs exposed by this M4L device. |
| `midi_inputs`   | `list[DeviceIO]` | no       | `yes`      | MIDI inputs exposed by this M4L device.   |
| `midi_outputs`  | `list[DeviceIO]` | no       | `yes`      | MIDI outputs exposed by this M4L device.  |

#### `audio_inputs`

- **Type:** `list[DeviceIO]`
- **Listenable:** `yes`
- **Since:** `<11`

Read-only list of all audio inputs that this Max for Live device offers. Each item is a
`DeviceIO` object with its own OID and routing properties. Blank M4L devices have at least one
audio input. Listener fires when the set of audio inputs changes.

#### `audio_outputs`

- **Type:** `list[DeviceIO]`
- **Listenable:** `yes`
- **Since:** `<11`

Read-only list of all audio outputs that this Max for Live device offers. Each item is a
`DeviceIO` object. Blank M4L devices have at least one audio output. Listener fires when the
set of audio outputs changes.

#### `midi_inputs`

- **Type:** `list[DeviceIO]`
- **Listenable:** `yes`
- **Since:** `11.0`

Read-only list of all MIDI inputs that this Max for Live device offers. Empty for blank M4L
devices -- only populated when the Max patch exposes MIDI I/O objects. Listener fires when the
set of MIDI inputs changes.

#### `midi_outputs`

- **Type:** `list[DeviceIO]`
- **Listenable:** `yes`
- **Since:** `11.0`

Read-only list of all MIDI outputs that this Max for Live device offers. Empty for blank M4L
devices -- only populated when the Max patch exposes MIDI I/O objects. Listener fires when the
set of MIDI outputs changes.

### Events

| Event                     | Listenable | Summary                                                |
| ------------------------- | ---------- | ------------------------------------------------------ |
| `bank_parameters_changed` | `yes`      | Fires when the device's parameter bank layout changes. |

#### `bank_parameters_changed`

- **Listenable:** `yes`
- **Since:** `<11`

An event-only listenable with no corresponding readable property. The listener fires
when the parameter bank configuration changes. There is no property to read -- only
add/remove/has listener methods exist.

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`,
`store_chosen_bank()`), MaxDevice adds:

| Method                                             | Returns | Summary                                         |
| -------------------------------------------------- | ------- | ----------------------------------------------- |
| `get_bank_count()`                                 | `int`   | Number of parameter banks.                      |
| `get_bank_name(bank_index: int)`                   | `str`   | Name of a parameter bank by index.              |
| `get_bank_parameters(bank_index: int)`             | `list`  | Parameter indices for a given bank.             |
| `get_value_item_icons(parameter: DeviceParameter)` | `list`  | Icon identifiers for a list parameter's values. |

#### `get_bank_count()`

- **Returns:** `int`
- **Since:** `<11`

Returns the number of parameter banks for this device. Returns `0` for blank M4L devices
(no configured banks). Related to hardware control surface integration.

#### `get_bank_name(bank_index: int)`

- **Returns:** `str`
- **Args:**
    - `bank_index: int` -- index of the bank to query
- **Raises:** `InternalError` if index is out of range or device has no banks.
- **Since:** `<11`

Returns the name of the parameter bank at the given index. Raises `InternalError` when called
on a device with zero banks.

#### `get_bank_parameters(bank_index: int)`

- **Returns:** `list[int]`
- **Args:**
    - `bank_index: int` -- index of the bank to query; `-1` refers to the "Best of" bank
- **Raises:** `InternalError` if index is out of range. `"this device has no best-of bank"` for `-1` on
  devices without configured banks.
- **Since:** `<11`

Returns the parameter indices for the bank at the given index. Empty slots are marked
as `-1`. Passing `-1` as the bank index returns the "Best of" bank.

#### `get_value_item_icons(parameter: DeviceParameter)`

- **Returns:** `list[str]`
- **Args:**
    - `parameter: DeviceParameter` -- the parameter to query for icons
- **Since:** `<11`

Returns a list of icon identifier strings for a list-style parameter's values. An empty
string indicates no icon should be displayed for that value. An empty list means no icons
should be displayed at all. Related to hardware control surface integration.


### reference/devices/MeldDevice.md

# MeldDevice

> `Live.MeldDevice.MeldDevice`

This class represents a Meld synthesizer device in Live. MeldDevice is a subclass of Device -- it has all the
children, properties, and methods of Device plus additional members for selecting the oscillator engine,
polyphony mode, voice count, and unison settings.

??? note "Raw probe notes (temporary)"
    - Bridge type: `"MeldDevice"`. `class_name`: `"InstrumentMeld"`.
    - `selected_engine` returns `bool` through the bridge (not `int`), despite conceptually being
      a 0/1 selector. Setting `1` reads back as `True`, setting `0`/`False` reads back as `False`.
    - `mono_poly` returns `int`. Default is 1 (Poly). Settable, round-trips correctly.
    - `poly_voices` returns `int`. Default is 5. Settable (set to 2, read back 2), round-trips.
    - `unison_voices` returns `int`. Default is 0 (Off). Settable (set to 2, read back 2), round-trips.
    - All four properties are listenable and settable.

### Open Questions

None — all resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), MeldDevice adds:

| Property          | Type   | Settable | Listenable | Summary                                                           |
| ----------------- | ------ | -------- | ---------- | ----------------------------------------------------------------- |
| `mono_poly`       | `int`  | yes      | yes        | Polyphony mode: 0 = Mono, 1 = Poly.                              |
| `poly_voices`     | `int`  | yes      | yes        | Polyphony voice count index (0-based).                            |
| `selected_engine` | `bool` | yes      | yes        | Oscillator engine selector: False = Engine A, True = Engine B.    |
| `unison_voices`   | `int`  | yes      | yes        | Unison voice count index: 0 = Off, 1 = Two, 2 = Three, 3 = Four. |

#### `mono_poly`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.0`

Selects the polyphony mode. Values: 0 = Mono, 1 = Poly.

#### `poly_voices`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.0`

Selects the polyphony voice count. The index maps to voice counts as follows:
0 = 2, 1 = 3, 2 = 4, 3 = 5, 4 = 6, 5 = 8, 6 = 12.

#### `selected_engine`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** yes
- **Since:** `12.0`

Selects which oscillator engine is active. Values: `False` = Engine A, `True` = Engine B.

**Quirks:**

- Despite conceptually being a 0/1 index, the bridge serializes this as `bool`.

#### `unison_voices`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.0`

Selects the unison voice count. Values: 0 = Off, 1 = Two, 2 = Three, 3 = Four.


### reference/devices/PluginDevice.md

# PluginDevice

> `Live.PluginDevice.PluginDevice`

This class represents a third-party plug-in device (VST or Audio Unit) in Live. A
PluginDevice is a subclass of Device -- it has all the children, properties, and methods
of Device plus additional members for accessing plug-in presets and parameter names.

Plug-in devices wrap external instrument or effect plug-ins. Their parameters are
exposed through the standard `parameters` list (inherited from Device), but PluginDevice
adds methods to query plug-in-specific parameter names and a preset system that is
separate from Live's native preset browser.

??? note "Raw probe notes (temporary)"
    - Bridge type name: `"PluginDevice"` (generic for all VST/AU plug-ins).
    - `class_name` = `"PluginDevice"` (same for all VST2/VST3 plug-ins -- not plug-in-specific).
    - **AU uses a distinct class name:** `class_name='AuPluginDevice'`. VST2 and VST3 both use
      `'PluginDevice'` (no distinction between VST versions). Both resolve to the same `PluginDevice`
      Python class.
    - `class_display_name` = the plug-in's own name (e.g. `"Raum"`).
    - Device type = 2 (Audio Effect) for effect plug-ins; would be 1 (Instrument) for instrument
      plug-ins.
    - **Cannot be inserted via `insert_device`** -- only native devices are accepted. Plug-ins must
      be loaded via `browser_load` (targeting the `plugins` browser root).
    - **`move_device` works** -- a loaded plug-in device can be moved into an Audio Effect Rack chain
      via `Song.move_device()`. Confirmed with TDR Nova into a rack chain.
    - **Dual preset model** -- two completely separate preset systems coexist:
        - **Runtime presets** (`PluginDevice.presets`): reported by the plug-in to Live via the
          VST/AU protocol. Probed all installed plug-ins (12+ across VST2, VST3, AUv2, third-party,
          and Apple built-ins): **every one returns `['Default']` only**. Plug-in-internal preset
          browsers (e.g. Vital's patch browser) are not accessible through Live's API.
        - **Browser presets** (user-saved): `.aupreset` and `.vstpreset` files that appear as
          children of the plug-in's browser item under the `plugins` root (`source='User Library'`).
          These are format-bound -- `.aupreset` only appears under the AUv2 entry, `.vstpreset` only
          under VST3. User-saved browser presets do **not** appear in the runtime `presets` list.
    - **Hotswap cross-format behavior** (via `browser.hotswap_target` + `browser_load`):
        - Same-format preset (e.g. VST3 `.vstpreset` -> VST3 device): preset applied in-place,
          **same OID**.
        - Cross-format preset (e.g. AU `.aupreset` -> VST3 device): replaced in-place with AU
          version (`AuPluginDevice`), **new OID**, device count unchanged.
        - Cross-device swap (e.g. Raum VST3 -> Ozone AU): completely different plug-in swapped
          in-place, **new OID**.
        - Raw `browser_load` without hotswap always appends a new device (not useful for preset
          application).
    - `presets` serializes as plain `list[str]` through the bridge (StringVector -> list).
    - `selected_preset_index` is **settable** -- confirmed by probe.
    - `get_parameter_names(begin, end)` returns `list[str]`. `end` is **exclusive** (Python slicing
      semantics): `get_parameter_names(0, 3)` returns 3 names (indices 0, 1, 2).
      `get_parameter_names(0, -1)` returns all.
    - Some parameter names may be `"-"` (unnamed/placeholder parameters).

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), PluginDevice adds:

| Property                | Type           | Settable | Listenable | Summary                                          |
| ----------------------- | -------------- | -------- | ---------- | ------------------------------------------------ |
| `presets`               | `StringVector` | no       | `yes`      | The list of preset names exposed by the plug-in. |
| `selected_preset_index` | `int`          | yes      | `yes`      | Index of the currently selected plug-in preset.  |

#### `presets`

- **Type:** `StringVector` (serializes as `list[str]`)
- **Listenable:** `yes`
- **Since:** `<11`

The list of preset names offered by the plug-in. These are the presets reported by the
plug-in itself (not Live's preset browser). The listener fires when the plug-in updates
its preset list (e.g., after scanning or user action inside the plug-in).

- **Limitations:**
    - In practice, most plug-ins only report `['Default']`. Plug-in-internal preset browsers
      (e.g. Vital's patch browser) are not accessible through Live's API.

#### `selected_preset_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The index of the currently selected preset in the plug-in's preset list. Setting this
value selects a different preset. The listener fires when the preset selection changes,
whether from the API or from user interaction inside the plug-in.

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`, `store_chosen_bank()`),
PluginDevice adds:

| Method                                      | Returns        | Summary                                 |
| ------------------------------------------- | -------------- | --------------------------------------- |
| `get_parameter_names(begin: int, end: int)` | `StringVector` | Get a range of plug-in parameter names. |

#### `get_parameter_names(begin: int, end: int)`

- **Returns:** `StringVector` (serializes as `list[str]`)
- **Args:**
  - `begin: int` -- starting index of the parameter range (default `0`)
  - `end: int` -- ending index of the parameter range (exclusive); if less than `0`, returns all
    parameters from `begin` to the end (default `-1`)
- **Raises:** Unknown
- **Since:** `<11`

Returns a list of plug-in parameter names for the given index range. The `end` parameter
is exclusive (Python slicing semantics): `get_parameter_names(0, 3)` returns names at
indices 0, 1, 2. Passing `end=-1` returns all parameters from `begin` onward.
Some parameter names may be `"-"` (unnamed/placeholder slots).

### Open Questions

- Does changing `selected_preset_index` actually load the preset in the plug-in? (Likely yes, but
  not confirmed with a multi-preset plug-in.)
- What happens when setting `selected_preset_index` to an out-of-range value? (Not tested -- only
  1 preset available.)


### reference/devices/RackDevice.md

# RackDevice

> `Live.RackDevice.RackDevice`

This class represents a rack device in Live (Instrument Rack, Audio Effect Rack, MIDI Effect Rack, or Drum Rack).
A RackDevice is a subclass of Device — it has all the children, properties, and methods of Device plus additional
members for managing chains, macros, drum pads, and macro variations.

A rack contains one or more chains, each with its own device list and mixer. It may also contain return chains.
Drum Racks additionally expose drum pads.

??? note "Raw probe notes (temporary)"

    Probed against Live 12.3.5 with self-inserted Instrument Rack and Drum Rack.

    **Parameter layout (fixed-size):**

    - `[0]` = Device On (toggle, quantized)
    - `[1]`–`[16]` = Macro 1–16 (continuous, 0.0–127.0). Always 16, regardless of `visible_macro_count`.
    - `[17]` = Chain Selector (Instrument/Audio/MIDI Effect Racks only; Drum Racks have 17 params total, no
      Chain Selector in the parameter list).
    - `add_macro()` / `remove_macro()` only change `visible_macro_count`, never the parameter list.

    **Macro count limits:**

    - Default: 8 visible macros.
    - Maximum: 16 (`add_macro()` throws `"The maximum number of macro controls is already reached!"`).
    - Minimum: 1 (`remove_macro()` throws `"The minimum number of macro controls is already reached!"`).
    - Increment pattern: 1→2 (delta=1), then 2→4→6→8→10→12→14→16 (delta=2 each).

    **macros_mapped:** Always returns a list of 16 booleans (all macros, not just visible ones).

    **selected_variation_index:** Returns `-1` when no variations exist. `delete_selected_variation()` is a no-op
    when `selected_variation_index = -1`.

    **has_drum_pads:** Throws `"Only drum racks can have pads!"` on non-Drum Racks where `can_have_drum_pads=False`.

    **chain_selector:** Accessible via both `get` (returns handle dict `{oid, type: "DeviceParameter"}`) and
    `children` (returns `kind: 'object'` with single item). Also present as parameter [17] in the parameter list
    (Instrument Rack only).

    **View:** Returned as `kind: 'object'` with type `"View"` (not a Rack-specific type name). `selected_chain`
    returns `None` when the rack has no chains. `selected_drum_pad` works on Drum Racks via both `get` and `children`.

    **insert_chain:** Works on all rack types:

    - Instrument Rack: returns `{oid, type: "Chain"}`.
    - Drum Rack: returns `{oid, type: "DrumChain"}`.

    **DrumPad:** Type name is `"DrumPad"`. Empty pads show musical note names as their `name` (e.g. `"C-2"`,
    `"C♯-2"`, `"D-2"`). `note` = 0–127 (MIDI note number). `mute` and `solo` default to `False`.
    128 drum pads total, 16 visible at a time. Default `drum_pads_scroll_position` = 9.

### Open Questions

- ~~What is the maximum number of macros (`add_macro()` limit)?~~ **Answered: 16.**
- ~~What is the minimum number of macros (`remove_macro()` limit)?~~ **Answered: 1.**
- ~~Does `macros_mapped` include hidden macros, or only visible ones?~~ **Answered: all 16 macros (hidden
  included).**
- ~~What does `selected_variation_index` return when no variations exist?~~ **Answered: `-1`.**
- ~~Can `insert_chain()` be called on non-Drum Racks, or only on Drum Racks?~~ **Answered: works on all rack
  types. Returns `Chain` for non-Drum, `DrumChain` for Drum Rack.**

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `chain_selector` | `DeviceParameter` | `single` | `no` | The chain selector parameter for zone-based chain routing. |
| `chains` | `Sequence[Chain]` | `list` | `yes` | The rack's chains. |
| `drum_pads` | `Sequence[DrumPad]` | `list` | `yes` | All 128 drum pads. Drum Racks only. |
| `return_chains` | `Sequence[Chain]` | `list` | `yes` | The rack's return chains. |
| `visible_drum_pads` | `Sequence[DrumPad]` | `list` | `yes` | The 16 currently visible drum pads. Drum Racks only. |

#### `chain_selector`

- **Returns:** `DeviceParameter`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `11.2`

Convenience accessor for the rack's chain selector parameter. The chain selector controls which chain(s) are
active based on the chain zone mapping. This is a `DeviceParameter` object, so it can be automated and mapped.

- **Quirks:** Accessible via both `get` (returns handle dict) and `children` (`kind: 'object'`). Also present as
  parameter [17] in the parameter list (Instrument Rack only; Drum Racks have no Chain Selector parameter).

#### `chains`

- **Returns:** `Sequence[Chain]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The ordered list of chains in this rack. Throws an exception if `can_have_chains` is `False` (which should never
happen for a RackDevice). The listener fires when chains are added, removed, or reordered.

#### `drum_pads`

- **Returns:** `Sequence[DrumPad]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

All 128 drum pads for the topmost Drum Rack. Inner (nested) Drum Racks return an empty list. Throws an exception
if `can_have_drum_pads` is `False`. The listener fires when pad assignments change.

#### `return_chains`

- **Returns:** `Sequence[Chain]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The list of return chains in this rack. Return chains receive audio from send amounts on the main chains. Throws
an exception if `can_have_chains` is `False`.

#### `visible_drum_pads`

- **Returns:** `Sequence[DrumPad]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The 16 drum pads currently visible in the Drum Rack pad grid. Only applies to the topmost Drum Rack — inner Drum
Racks return an empty list. Throws an exception if `can_have_drum_pads` is `False`. The visible range is
controlled by `view.drum_pads_scroll_position`.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), RackDevice adds:

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `can_show_chains` | `bool` | `no` | `no` | `True` if the rack instrument can show chains in Session View. |
| `has_drum_pads` | `bool` | `no` | `yes` | `True` for top-level Drum Racks with pads. |
| `has_macro_mappings` | `bool` | `no` | `yes` | `True` if any macro is mapped to a parameter. |
| `is_showing_chains` | `bool` | `no` | `yes` | `True` if chains are shown in Session View. |
| `macros_mapped` | `Sequence[bool]` | `no` | `yes` | Per-macro boolean list: `True` if that macro is mapped. |
| `selected_variation_index` | `int` | `yes` | `no` | Index of the currently selected macro variation. |
| `variation_count` | `int` | `no` | `yes` | Number of stored macro variations. |
| `visible_macro_count` | `int` | `no` | `yes` | Number of currently visible macros. |

#### `can_show_chains`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this rack contains an instrument device that is capable of showing its chains in Session View (e.g., an
Instrument Rack where chains can appear as rows in the Session View grid for individual clip launching).

#### `has_drum_pads`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the device is a Drum Rack that has pads. A nested (inner) Drum Rack returns `False` because only the
topmost Drum Rack owns the pad grid.

- **Quirks:** Throws if `can_have_drum_pads` is `False` — accessing on an Instrument Rack throws `"Only drum
  racks can have pads!"`. Guard with `can_have_drum_pads` check first.

#### `has_macro_mappings`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if any of the rack's macro knobs are mapped to a parameter inside the rack.

#### `is_showing_chains`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the rack is currently showing its chains in Session View. Only meaningful when `can_show_chains` is
`True`.

#### `macros_mapped`

- **Type:** `Sequence[bool]`
- **Listenable:** `yes`
- **Since:** `<11`

A list of booleans, one per macro parameter, where `True` indicates that the corresponding macro is mapped to a
device parameter inside the rack.

- **Quirks:** Always returns 16 booleans (all macros, not just visible ones). Length is fixed at 16 regardless
  of `visible_macro_count`.

#### `selected_variation_index`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `11.0`

The index of the currently selected macro variation. Setting an out-of-range index throws an exception.

- **Quirks:** Returns `-1` when no variations exist.

#### `variation_count`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `11.0`

The number of macro variations currently stored for this rack. Use `store_variation()` to add variations and
`delete_selected_variation()` to remove them.

#### `visible_macro_count`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `11.2`

The number of macro knobs currently visible in the rack UI. Use `add_macro()` and `remove_macro()` to change
this count. Default = 8. Range: 1–16.

- **Quirks:** `add_macro()` increments: 1→2 (+1), then +2 each step (2→4→6→...→16).

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`, `store_chosen_bank()`), RackDevice adds:

| Method | Returns | Summary |
| --- | --- | --- |
| `add_macro()` | `None` | Increase visible macro count by one. |
| `copy_pad(source_index: int, dest_index: int)` | `None` | Copy all contents from one drum pad to another. |
| `delete_selected_variation()` | `None` | Delete the currently selected macro variation. |
| `insert_chain(index: int = -1)` | `Chain` | Insert a new empty chain at the given index. |
| `randomize_macros()` | `None` | Randomize all eligible macro values. |
| `recall_last_used_variation()` | `None` | Recall the most recently used macro variation. |
| `recall_selected_variation()` | `None` | Recall the currently selected macro variation. |
| `remove_macro()` | `None` | Decrease visible macro count by one. |
| `store_variation()` | `None` | Store a new macro variation from current values. |

#### `add_macro()`

- **Returns:** `None`
- **Args:** None
- **Raises:** Throws `"The maximum number of macro controls is already reached!"` at 16.
- **Since:** `11.0`

Increases the number of visible macro controls in the rack. Does **not** change the parameter list.

- **Quirks:** Increment is +1 from 1→2, then +2 for all subsequent steps (2→4→6→8→10→12→14→16). Maximum is 16.

#### `copy_pad(source_index: int, dest_index: int)`

- **Returns:** `None`
- **Args:**
  - `source_index: int` — note number (0–127) of the source pad
  - `dest_index: int` — note number (0–127) of the destination pad
- **Raises:** Throws if the source pad is empty, or if either index is outside 0–127.
- **Since:** `<11`

Copies all contents of a Drum Rack pad from a source pad into a destination pad. The indices correspond to MIDI
note numbers (0–127). Only applicable to Drum Racks.

#### `delete_selected_variation()`

- **Returns:** `None`
- **Args:** None
- **Since:** `11.0`

Deletes the currently selected macro variation. No-op when `selected_variation_index` is `-1` (no variations or
none selected).

#### `insert_chain(index: int = -1)`

- **Returns:** `Chain` (the newly inserted chain)
- **Args:**
  - `index: int = -1` — position in the chain list; `-1` means end
- **Raises:** Throws if insertion is not possible.
- **Since:** `12.3`

Inserts a new chain at the specified index in the rack's chain list, or at the end if no index is provided.
Works on all rack types. Returns `Chain` for Instrument Racks and `DrumChain` for Drum Racks.

- **Quirks:** For Drum Racks, the newly inserted chain will have an initial MIDI In Note setting of "All Notes" —
  you likely want to set `DrumChain.in_note` to the note value that corresponds to the target pad.

#### `randomize_macros()`

- **Returns:** `None`
- **Args:** None
- **Since:** `11.0`

Randomizes the values for all macro controls that are eligible for randomization. Macros excluded from
randomization (via the rack UI) are not affected.

#### `recall_last_used_variation()`

- **Returns:** `None`
- **Args:** None
- **Since:** `11.0`

Recalls the macro variation that was recalled most recently. Does nothing if no variation has been recalled yet
during this session.

#### `recall_selected_variation()`

- **Returns:** `None`
- **Args:** None
- **Since:** `11.0`

Recalls the currently selected macro variation, setting all mapped macro parameters to their stored values. Does
nothing if there are no variations.

#### `remove_macro()`

- **Returns:** `None`
- **Args:** None
- **Raises:** Throws `"The minimum number of macro controls is already reached!"` at 1.
- **Since:** `11.0`

Decreases the number of visible macro controls in the rack. Does **not** change the parameter list.

- **Quirks:** Decrement is -2 for most steps (16→14→12→...→2), then -1 from 2→1. Minimum is 1.

#### `store_variation()`

- **Returns:** `None`
- **Args:** None
- **Since:** `11.0`

Stores a new variation of the current values of all mapped macro parameters. The new variation is appended to
the variation list and `variation_count` increases by one.

- **Quirks:** `selected_variation_index` stays at `-1` after store (does not auto-select).

---

## RackDevice.View

> `Live.RackDevice.RackDevice.View`

Represents the view aspects of a rack device. Extends Device.View with rack-specific view properties.

### Properties

In addition to `is_collapsed` (inherited from Device.View):

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `drum_pads_scroll_position` | `int` | `yes` | `yes` | Index of the lowest visible row of drum pads. |
| `is_showing_chain_devices` | `bool` | `no` | `yes` | Whether the selected chain's devices are visible. |
| `selected_chain` | `Chain` | `no` | `yes` | The currently selected chain in the rack. |
| `selected_drum_pad` | `DrumPad` | `no` | `yes` | The currently selected drum pad. Drum Racks only. |

#### `drum_pads_scroll_position`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The index of the lowest visible row of drum pads in the Drum Rack pad grid. Controls which 16 pads are shown in
`visible_drum_pads`. Throws an exception if `can_have_drum_pads` is `False`. Default value is 9 on a fresh
Drum Rack.

#### `is_showing_chain_devices`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` when the devices in the currently selected chain are visible in the rack's expanded view. Throws an
exception if `can_have_chains` is `False`.

#### `selected_chain`

- **Type:** `Chain`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected chain in the rack. The listener fires when the selection changes. Returns `None` when the
rack has no chains.

#### `selected_drum_pad`

- **Type:** `DrumPad`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected drum pad in the Drum Rack. Throws an exception if `can_have_drum_pads` is `False`.


### reference/devices/RoarDevice.md

# RoarDevice

> `Live.RoarDevice.RoarDevice`

This class represents a Roar distortion device in Live. RoarDevice is a subclass of Device -- it has all the
children, properties, and methods of Device plus additional members for selecting the routing mode and
toggling envelope input listening.

??? note "Raw probe notes (temporary)"
    - Bridge type: `"RoarDevice"`. `class_name`: `"Roar"`.
    - `routing_mode_index` returns `int`. Default is 3 ("Multi Band"). Settable, round-trips correctly.
    - `routing_mode_list` returns `list[str]` (StringVector serializes as plain list through bridge).
      Values: `["Single", "Serial", "Parallel", "Multi Band", "Mid Side", "Feedback", "Delay"]`.
      Not listenable (static list).
    - `env_listen` returns `bool`. Settable, round-trips correctly.
    - All properties except `routing_mode_list` are listenable.

### Open Questions

None — all resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), RoarDevice adds:

| Property             | Type        | Settable | Listenable | Summary                               |
| -------------------- | ----------- | -------- | ---------- | ------------------------------------- |
| `env_listen`         | `bool`      | yes      | yes        | Envelope Input Listen toggle state.   |
| `routing_mode_index` | `int`       | yes      | yes        | Index of the selected routing mode.   |
| `routing_mode_list`  | `list[str]` | no       | no         | List of available routing mode names. |

#### `env_listen`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** yes
- **Since:** `12.0`

The state of the Envelope Input Listen toggle. When enabled, the envelope follower listens to the input
signal.

#### `routing_mode_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.0`

The index into `routing_mode_list` for the currently selected routing mode. Default is 3 ("Multi Band").

#### `routing_mode_list`

- **Type:** `list[str]`
- **Listenable:** no
- **Since:** `12.0`

The list of available routing mode names for the Roar device. Static list, not listenable.
Values: `["Single", "Serial", "Parallel", "Multi Band", "Mid Side", "Feedback", "Delay"]`.


### reference/devices/ShifterDevice.md

# ShifterDevice

> `Live.ShifterDevice.ShifterDevice`

This class represents a Shifter audio effect device in Live. ShifterDevice is a subclass of Device -- it has
all the children, properties, and methods of Device plus additional members for selecting the pitch mode and
adjusting the MIDI pitch bend range.

Shifter is a pitch-shifting and frequency-shifting audio effect. The pitch mode determines whether pitch is
controlled internally or via MIDI input.

??? note "Raw probe notes (temporary)"
    - Bridge type: `"ShifterDevice"`. `class_name`: `"Shifter"`.
    - `pitch_mode_index` returns `int`. Default is 0 ("Internal"). Settable, round-trips correctly.
    - `pitch_mode_list` returns `list[str]` (StringVector serializes as plain list through bridge).
      Values: `["Internal", "MIDI"]`. Not listenable (static list).
    - `pitch_bend_range` returns `int`. Default is 2. Settable (set to 24, read back 24), round-trips.
    - All properties except `pitch_mode_list` are listenable.

### Open Questions

None — all resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), ShifterDevice adds:

| Property           | Type       | Settable | Listenable | Summary                                                    |
| ------------------ | ---------- | -------- | ---------- | ---------------------------------------------------------- |
| `pitch_bend_range` | `int`      | yes      | yes        | MIDI pitch bend range used in MIDI pitch mode.             |
| `pitch_mode_index` | `int`      | yes      | yes        | Index of the current pitch mode (0 = Internal, 1 = MIDI).  |
| `pitch_mode_list`  | `list[str]`| no       | no         | List of available pitch mode names.                        |

#### `pitch_bend_range`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `11.1`

The pitch bend range in semitones, used when the pitch mode is set to MIDI. Default is 2.

#### `pitch_mode_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `11.1`

The index of the current pitch mode. Values: 0 = Internal, 1 = MIDI.

#### `pitch_mode_list`

- **Type:** `list[str]`
- **Listenable:** no
- **Since:** `11.1`

The list of available pitch mode names. Static list, not listenable.
Values: `["Internal", "MIDI"]`.


### reference/devices/SimplerDevice.md

# SimplerDevice

> `Live.SimplerDevice.SimplerDevice`

This class represents an instance of Simpler in Live. A SimplerDevice is a subclass of
Device -- it has all the children, properties, and methods of Device plus additional
members for sample playback, warping, slicing, and voice management.

Simpler has three playback modes: Classic, One-Shot, and Slicing. The available properties
and methods vary depending on the active mode.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"SimplerDevice"`.
    - **`class_name`:** `"OriginalSimpler"`. **`class_display_name`:** `"Simpler"`.
    - **`type`:** 1 (`INSTRUMENT`).
    - **Insert name:** `"Simpler"` (matches `class_display_name`).
    - **7 settable properties** round-trip confirmed: `note_pitch_bend_range` (default 48),
      `pad_slicing` (default False), `pitch_bend_range` (default 5), `playback_mode` (default 0,
      range 0–2), `retrigger` (default True), `slicing_playback_mode` (default 0, range 0–2),
      `voices` (default 6, valid: 1,2,3,4,6,8,12,16,24,32).
    - **6 read-only properties:** `can_warp_as` (False), `can_warp_double` (False), `can_warp_half`
      (False), `multi_sample_mode` (False), `playing_position` (0.0), `playing_position_enabled`
      (False). All return defaults when no sample is loaded.
    - **All 13 properties are listenable.**
    - **`sample` child:** Returns `None` when no sample is loaded (confirmed — does not throw).
    - **All 6 methods** raise `InternalError` when no sample is loaded. This is expected — they
      require an active sample.
    - **`playback_mode`:** 0=Classic, 1=One-Shot, 2=Slicing. Plain `int`, not an enum.
    - **`slicing_playback_mode`:** 0=Mono, 1=Poly, 2=Thru. Plain `int`, not an enum.
    - **`voices`:** Valid values are 1,2,3,4,6,8,12,16,24,32 (not arbitrary). Invalid values throw.
    - **View:** 8 read-only listenable `int` properties. All return `-1` when no sample is loaded.
      `selected_slice` throws `AttributeError` when no sample is loaded and Simpler is not in
      Slicing mode.

### Children

In addition to Device children (`parameters`, `view`), SimplerDevice adds:

| Child    | Returns  | Shape    | Listenable | Summary                                 |
| -------- | -------- | -------- | ---------- | --------------------------------------- |
| `sample` | `Sample` | `single` | `yes`      | The sample currently loaded in Simpler. |

#### `sample`

- **Type:** `Sample` or `None`
- **Listenable:** `yes`
- **Since:** `<11`

The sample currently loaded into Simpler. The listener fires when a new sample is loaded
or the sample is replaced. Returns `None` if no sample is loaded.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), SimplerDevice adds:

| Property                   | Type    | Settable | Listenable | Summary                                                     |
| -------------------------- | ------- | -------- | ---------- | ----------------------------------------------------------- |
| `can_warp_as`              | `bool`  | no       | `yes`      | Whether `warp_as` is currently available.                   |
| `can_warp_double`          | `bool`  | no       | `yes`      | Whether `warp_double` is currently available.               |
| `can_warp_half`            | `bool`  | no       | `yes`      | Whether `warp_half` is currently available.                 |
| `multi_sample_mode`        | `bool`  | no       | `yes`      | Whether Simpler is in multi-sample mode.                    |
| `note_pitch_bend_range`    | `int`   | yes      | `yes`      | The per-note pitch bend range in semitones. Default 48.     |
| `pad_slicing`              | `bool`  | yes      | `yes`      | Whether slices can be added by playing unassigned notes.    |
| `pitch_bend_range`         | `int`   | yes      | `yes`      | The global pitch bend range in semitones. Default 5.        |
| `playback_mode`            | `int`   | yes      | `yes`      | 0=Classic, 1=One-Shot, 2=Slicing. Default 0.               |
| `playing_position`         | `float` | no       | `yes`      | Normalized playback position between start and end markers. |
| `playing_position_enabled` | `bool`  | no       | `yes`      | Whether Simpler is currently playing back the sample.       |
| `retrigger`                | `bool`  | yes      | `yes`      | Whether retrigger mode is enabled. Default True.            |
| `slicing_playback_mode`    | `int`   | yes      | `yes`      | 0=Mono, 1=Poly, 2=Thru. Default 0.                         |
| `voices`                   | `int`   | yes      | `yes`      | Polyphony voice count. Valid: 1,2,3,4,6,8,12,16,24,32.     |

#### `can_warp_as`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether `warp_as` is currently available. Returns `False` when no sample is loaded.

#### `can_warp_double`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether `warp_double` is currently available. Returns `False` when no sample is loaded.

#### `can_warp_half`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether `warp_half` is currently available. Returns `False` when no sample is loaded.

#### `multi_sample_mode`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether Simpler is in multi-sample mode. Returns `False` when no sample is loaded.

#### `note_pitch_bend_range`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The per-note pitch bend range in semitones. Default 48.

#### `pad_slicing`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Whether slices can be added by playing unassigned notes on the MIDI controller.

#### `pitch_bend_range`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `11.3`

The global pitch bend range in semitones. Default 5.

#### `playback_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

0=Classic, 1=One-Shot, 2=Slicing. Default 0. Plain `int`, not an enum.

#### `playing_position`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Normalized playback position between start and end markers. Returns `0.0` when no sample is loaded.

#### `playing_position_enabled`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Whether Simpler is currently playing back the sample. Returns `False` when no sample is loaded.

#### `retrigger`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Whether retrigger mode is enabled. Default True.

#### `slicing_playback_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

0=Mono, 1=Poly, 2=Thru. Default 0. Plain `int`, not an enum.

#### `voices`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Polyphony voice count. Valid values are 1, 2, 3, 4, 6, 8, 12, 16, 24, 32 (not arbitrary). Invalid values throw.

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot()`, `store_chosen_bank()`),
SimplerDevice adds:

| Method                      | Returns | Summary                                                      |
| --------------------------- | ------- | ------------------------------------------------------------ |
| `crop()`                    | `None`  | Crop the sample to the region between start and end markers. |
| `guess_playback_length()`   | `float` | Estimate the playback length in beats between the markers.   |
| `reverse()`                 | `None`  | Reverse the loaded sample.                                   |
| `warp_as(beat_time: float)` | `None`  | Warp the active region to fit the given beat length.         |
| `warp_double()`             | `None`  | Double the playback tempo of the active region.              |
| `warp_half()`               | `None`  | Halve the playback tempo of the active region.               |

All methods raise `InternalError` when no sample is loaded.

#### `crop()`

- **Returns:** `None`
- **Since:** `<11`

Crop the sample to the region between start and end markers.

#### `guess_playback_length()`

- **Returns:** `float`
- **Since:** `<11`

Estimate the playback length in beats between the markers.

#### `reverse()`

- **Returns:** `None`
- **Since:** `<11`

Reverse the loaded sample.

#### `warp_as(beat_time: float)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` -- the target beat length for the active region
- **Since:** `<11`

Warp the active region to fit the given beat length.

#### `warp_double()`

- **Returns:** `None`
- **Since:** `<11`

Double the playback tempo of the active region.

#### `warp_half()`

- **Returns:** `None`
- **Since:** `<11`

Halve the playback tempo of the active region.

---

## SimplerDevice.View

Represents the view aspects of a Simpler device. Extends Device.View with sample display
properties for visualizing the waveform, loop region, and slices.

### Properties

In addition to `is_collapsed` (inherited from Device.View):

| Property              | Type  | Settable | Listenable | Summary                                                      |
| --------------------- | ----- | -------- | ---------- | ------------------------------------------------------------ |
| `sample_end`          | `int` | no       | `yes`      | Modulated sample end position in samples. -1 if no sample.   |
| `sample_env_fade_in`  | `int` | no       | `yes`      | Envelope fade-in time in samples. -1 if no sample.           |
| `sample_env_fade_out` | `int` | no       | `yes`      | Envelope fade-out time in samples. -1 if no sample.          |
| `sample_loop_end`     | `int` | no       | `yes`      | Modulated loop end position in samples. -1 if no sample.     |
| `sample_loop_fade`    | `int` | no       | `yes`      | Modulated loop crossfade length in samples. -1 if no sample. |
| `sample_loop_start`   | `int` | no       | `yes`      | Modulated loop start position in samples. -1 if no sample.   |
| `sample_start`        | `int` | no       | `yes`      | Modulated sample start position in samples. -1 if no sample. |
| `selected_slice`      | `int` | no       | `yes`      | Currently selected slice time. Errors if no sample.          |

#### `sample_end`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated sample end position in samples. Returns `-1` if no sample is loaded.

#### `sample_env_fade_in`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Envelope fade-in time in samples. Returns `-1` if no sample is loaded.

#### `sample_env_fade_out`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Envelope fade-out time in samples. Returns `-1` if no sample is loaded.

#### `sample_loop_end`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated loop end position in samples. Returns `-1` if no sample is loaded.

#### `sample_loop_fade`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated loop crossfade length in samples. Returns `-1` if no sample is loaded.

#### `sample_loop_start`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated loop start position in samples. Returns `-1` if no sample is loaded.

#### `sample_start`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Modulated sample start position in samples. Returns `-1` if no sample is loaded.

#### `selected_slice`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Currently selected slice time.

- **Quirks:**
    - Throws `AttributeError` when no sample is loaded and Simpler is not in Slicing mode.


### reference/devices/SpectralResonatorDevice.md

# SpectralResonatorDevice

> `Live.SpectralResonatorDevice.SpectralResonatorDevice`

This class represents a Spectral Resonator device in Live. SpectralResonatorDevice is a
subclass of Device -- it has all the children, properties, and methods of Device plus
additional members for controlling frequency dial mode, MIDI gate, modulation mode,
mono/poly mode, pitch mode, pitch bend range, and polyphony voice count.

Spectral Resonator is a spectral audio effect that tunes incoming audio to pitched
resonances. It can be driven by MIDI for pitch control.

??? note "Raw probe notes (temporary)"
    - Bridge type name: `"SpectralResonatorDevice"`.
    - `class_name` = `"Transmute"` (shares implementation base with Spectral Time -- the stub uses
      `TTransmuteDevicePyHandle`).
    - `class_display_name` = `"Spectral Resonator"`.
    - Device type = 2 (Audio Effect).
    - All 7 index properties are **settable** (get+set+listen).
    - All 5 `*_list` properties serialize as plain `list[str]` through the bridge
      (StringVector -> list).
    - The `*_list` properties are marked listenable in the stub but appear static in practice.
    - `pitch_bend_range` valid range: 0-24 (clamped; setting 48 -> readback 24). Settable.
    - `frequency_dial_mode_list` = `['ModulationHertz', 'ModulationBeat8th']` (internal names,
      not UI labels).
    - `midi_gate_list` = `['Off', 'On']`.
    - `mod_mode_list` = `['None', 'Chorus', 'Wander', 'Granular']`.
    - `mono_poly_list` = `['Mono', 'Poly']`.
    - `pitch_mode_list` = `['Internal', 'MIDI']`.
    - Default values: `frequency_dial_mode` = 0, `midi_gate` = 0, `mod_mode` = 0, `mono_poly` = 0,
      `pitch_mode` = 0, `polyphony` = 2, `pitch_bend_range` = 2.

### Open Questions

None -- all questions resolved by probing.

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`,
`can_have_drum_pads`, `class_display_name`, `class_name`, `is_active`,
`is_using_compare_preset_b`, `latency_in_ms`, `latency_in_samples`, `name`, `type`),
SpectralResonatorDevice adds:

| Property                   | Type           | Settable | Listenable | Summary                                                          |
| -------------------------- | -------------- | -------- | ---------- | ---------------------------------------------------------------- |
| `frequency_dial_mode`      | `int`          | `int`    | `yes`      | Freq dial mode: 0 = Hertz, 1 = MIDI note.                        |
| `frequency_dial_mode_list` | `list[str]`    | no       | `yes`      | List of available frequency dial mode names.                     |
| `midi_gate`                | `int`          | `int`    | `yes`      | MIDI gate switch: 0 = Off, 1 = On.                               |
| `midi_gate_list`           | `list[str]`    | no       | `yes`      | List of available MIDI gate options.                             |
| `mod_mode`                 | `int`          | `int`    | `yes`      | Modulation mode: 0 = None, 1 = Chorus, 2 = Wander, 3 = Granular. |
| `mod_mode_list`            | `list[str]`    | no       | `yes`      | List of available modulation mode names.                         |
| `mono_poly`                | `int`          | `int`    | `yes`      | Mono/Poly switch: 0 = Mono, 1 = Poly.                            |
| `mono_poly_list`           | `list[str]`    | no       | `yes`      | List of available mono/poly options.                             |
| `pitch_bend_range`         | `int`          | `int`    | `yes`      | Pitch bend range in semitones (0-24). Settable.                  |
| `pitch_mode`               | `int`          | `int`    | `yes`      | Pitch mode: 0 = Internal, 1 = MIDI.                              |
| `pitch_mode_list`          | `list[str]`    | no       | `yes`      | List of available pitch mode names.                              |
| `polyphony`                | `int`          | `int`    | `yes`      | Polyphony voice count index.                                     |

#### `frequency_dial_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The mode of the frequency dial control. Values: 0 = Hertz, 1 = MIDI note values.
Default: 0. Settable -- confirmed by probe.

#### `frequency_dial_mode_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available frequency dial mode names. The stub includes a listener for this
property, suggesting the list can change dynamically.
Values: `['ModulationHertz', 'ModulationBeat8th']` (internal names).

#### `midi_gate`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The state of the MIDI gate switch. Values: 0 = Off, 1 = On.
Default: 0. Settable -- confirmed by probe.

#### `midi_gate_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available MIDI gate options. Values: `['Off', 'On']`.

#### `mod_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The modulation mode. Values: 0 = None, 1 = Chorus, 2 = Wander, 3 = Granular.
Default: 0. Settable -- confirmed by probe.

#### `mod_mode_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available modulation mode names. Values: `['None', 'Chorus', 'Wander', 'Granular']`.

#### `mono_poly`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The mono/poly switch state. Values: 0 = Mono, 1 = Poly.
Default: 0. Settable -- confirmed by probe.

#### `mono_poly_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available mono/poly option names. Values: `['Mono', 'Poly']`.

#### `pitch_bend_range`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The pitch bend range in semitones. Valid range: 0-24 (values above 24 are clamped).
Default: 2. Settable -- confirmed by probe.

#### `pitch_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The pitch mode. Values: 0 = Internal, 1 = MIDI.
Default: 0. Settable -- confirmed by probe.

#### `pitch_mode_list`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available pitch mode names. Values: `['Internal', 'MIDI']`.

#### `polyphony`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The polyphony voice count index. Maps to voice counts as follows:
0 = 2, 1 = 4, 2 = 8, 3 = 16 voices.
Default: 2 (= 8 voices). Settable -- confirmed by probe.


### reference/devices/WavetableDevice.md

# WavetableDevice

> `Live.WavetableDevice.WavetableDevice`

This class represents a Wavetable synthesizer device in Live. WavetableDevice is a subclass of Device -- it
has all the children, properties, and methods of Device plus additional members for controlling the
oscillators, filter routing, voice settings, unison mode, and the modulation matrix.

Wavetable's modulation matrix is exposed through a set of methods that let you add parameters to the matrix,
query modulation amounts, and set modulation amounts by target and source index. The
`visible_modulation_target_names` property lists the currently visible targets, and
`modulation_matrix_changed` fires a listener when the matrix is modified.

??? note "Raw probe notes (temporary)"
    - **Bridge type:** `"WavetableDevice"`.
    - **`class_name`:** `"InstrumentVector"`. **`class_display_name`:** `"Wavetable"`.
    - **`type`:** 1 (`INSTRUMENT`).
    - **Insert name:** `"Wavetable"` (matches `class_display_name`).
    - **All 11 int properties** are settable and listenable. Round-trip confirmed.
    - **`filter_routing`:** 0–2 (0=Serial, 1=Parallel, 2=Split). 3+ throws.
    - **`mono_poly`:** 0=Mono, 1=Poly. Default 1.
    - **`oscillator_N_effect_mode`:** 0–3 (0=None, 1=Fm, 2=Classic, 3=Modern). 4+ throws.
    - **`oscillator_N_wavetable_category`:** Index into `oscillator_wavetable_categories`.
      Changing category updates `oscillator_N_wavetables`.
    - **`oscillator_N_wavetable_index`:** Index within current category's wavetable list.
    - **`oscillator_N_wavetables`:** Dynamic `list[str]` — updates on category change.
      Default category 0 ("Basics") has 29 wavetables.
    - **`oscillator_wavetable_categories`:** Static `list[str]` of 12 categories:
      `["Basics", "Collection", "Complex", "Distortion", "Filter", "Formant", "Harmonics",
      "Instrument", "Noise", "Retro", "Vintage", "User"]`.
    - **`poly_voices`:** 0–6 (7 valid values). 7+ throws "Invalid poly voice count".
    - **`unison_mode`:** 0–6 (0=None, 1=Classic, 2=Shimmer, 3=Noise, 4=Phase Sync,
      5=Position Spread, 6=Random Note). 7+ throws.
    - **`unison_voice_count`:** 2–8 (7 valid values). <2 or >8 throws.
    - **`visible_modulation_target_names`:** Read-only `list[str]`. Listenable.
      Default: `["Amp", "Pitch", "Osc 1 Pos", "Osc 1 Warp"]`.
    - **`modulation_matrix_changed`:** Listenable (no readable value, fire-only).
    - **Modulation sources:** 13 sources (indices 0–12). Source 13+ throws "invalid index".
    - **`is_parameter_modulatable(param)`:** Returns `bool`. `Device On` and `Osc 1 On`
      return `False`; `Osc 1 Transp`, `Osc 1 Detune`, `Osc 1 Pos` return `True`.
    - **`add_parameter_to_modulation_matrix(param)`:** Returns `int` (new target index).
    - **`get_modulation_target_parameter_name(target_idx)`:** Returns `str`.
    - **`get_modulation_value(target_idx, source)`:** Returns `float`.
    - **`set_modulation_value(target_idx, source, value)`:** Returns `None`. Round-trip confirmed.

### Children

| Child        | Returns                     | Shape    | Listenable | Summary                                        |
| ------------ | --------------------------- | -------- | ---------- | ---------------------------------------------- |
| `parameters` | `Sequence[DeviceParameter]` | `list`   | yes        | Automatable parameters exposed by this device. |
| `view`       | `WavetableDevice.View`      | `single` | no         | View aspects of the device (collapse state).   |

### Properties

In addition to all Device properties (`can_compare_ab`, `can_have_chains`, `can_have_drum_pads`,
`class_display_name`, `class_name`, `is_active`, `is_using_compare_preset_b`, `latency_in_ms`,
`latency_in_samples`, `name`, `type`), WavetableDevice adds:

| Property                          | Type        | Settable | Listenable | Summary                                                       |
| --------------------------------- | ----------- | -------- | ---------- | ------------------------------------------------------------- |
| `filter_routing`                  | `int`       | yes      | yes        | Filter routing mode: 0=Serial, 1=Parallel, 2=Split.          |
| `mono_poly`                       | `int`       | yes      | yes        | Voice mode: 0=Mono, 1=Poly.                                  |
| `oscillator_1_effect_mode`        | `int`       | yes      | yes        | Osc 1 effect mode: 0=None, 1=Fm, 2=Classic, 3=Modern.        |
| `oscillator_1_wavetable_category` | `int`       | yes      | yes        | Oscillator 1 wavetable category index.                        |
| `oscillator_1_wavetable_index`    | `int`       | yes      | yes        | Osc 1 wavetable index within the current category.            |
| `oscillator_1_wavetables`         | `list[str]` | no       | yes        | Wavetable names available for oscillator 1.                   |
| `oscillator_2_effect_mode`        | `int`       | yes      | yes        | Osc 2 effect mode (same values as osc 1).                     |
| `oscillator_2_wavetable_category` | `int`       | yes      | yes        | Oscillator 2 wavetable category index.                        |
| `oscillator_2_wavetable_index`    | `int`       | yes      | yes        | Osc 2 wavetable index within the current category.            |
| `oscillator_2_wavetables`         | `list[str]` | no       | yes        | Wavetable names available for oscillator 2.                   |
| `oscillator_wavetable_categories` | `list[str]` | no       | no         | Names of all available wavetable categories.                  |
| `poly_voices`                     | `int`       | yes      | yes        | Number of polyphonic voices (0–6).                            |
| `unison_mode`                     | `int`       | yes      | yes        | Unison mode (0–6, see values below).                          |
| `unison_voice_count`              | `int`       | yes      | yes        | Number of unison voices (2–8).                                |
| `visible_modulation_target_names` | `list[str]` | no       | yes        | Names of modulation targets visible in the matrix.            |

### Methods

In addition to all Device methods (`save_preset_to_compare_ab_slot`, `store_chosen_bank`), WavetableDevice
adds:

| Method                                               | Returns | Summary                                                  |
| ---------------------------------------------------- | ------- | -------------------------------------------------------- |
| `add_parameter_to_modulation_matrix(parameter)`      | `int`   | Add a parameter to the modulation matrix.                |
| `get_modulation_target_parameter_name(target_index)` | `str`   | Get the parameter name for a modulation target by index. |
| `get_modulation_value(target_index, source)`         | `float` | Get the modulation amount for a target-source pair.      |
| `is_parameter_modulatable(parameter)`                | `bool`  | Check whether a parameter can be modulated.              |
| `set_modulation_value(target_index, source, value)`  | `None`  | Set the modulation amount for a target-source pair.      |


### reference/tracks/Clip.md

# Clip

> `Live.Clip.Clip`

Represents a clip in Live — either audio or MIDI, in either Session View or Arrangement View. The full
property/method surface is available on all clips, but many members are only meaningful for one clip type (audio vs
MIDI) or one context (session vs arrangement). Those are marked in each detail entry.

??? note "Raw probe notes (temporary)"

    **Color behavior (probed 2026-02-17):**

    - Setting `color` to `None` raises an `InternalError` (C++ type mismatch: expected `int`). Matches Track and
      Scene behavior.
    - Setting `color_index` to `None` raises an `InternalError`. Clips always have a color in the Live UI — there
      is no "no color" option — so `None` is not a valid value.

    **Arrangement clip playback (probed 2026-02-17):**

    All playback state properties and playback control methods are session-only. On arrangement clips they don't
    error, but they silently no-op:

    - Properties always `False`/`0.0`: `is_playing`, `is_triggered`, `is_recording`, `is_overdubbing`,
      `playing_position` — even while the transport plays through the clip's time range.
    - Methods no-op: `fire()`, `stop()`, `move_playing_pos()`, `scrub()`, `stop_scrub()`.

    **move_playing_pos / scrub / stop_scrub behavior (probed 2026-02-17):**

    - `move_playing_pos(beats)`: relative unquantized jump within the clip's local playhead. While playing,
      `move_playing_pos(2.0)` jumps ~2 beats forward; negative values jump backwards. While stopped: no-op.
    - `scrub(beat_time)`: auditions a looping snippet at an absolute position. While playing, clip transitions to
      `is_triggered=True`. While stopped, starts playback.
    - `stop_scrub()`: ends a scrub session. Clip remains in `is_triggered=True` state.

    **will_record_on_start (probed 2026-02-17):**

    Always returns `False` through the Python API regardless of conditions tested. Same non-functional behavior as
    `ClipSlot.will_record_on_start`. Skipped from the public API spec.

### Open Questions

- `warping`: stub notes that setting this property is internally deferred. What does this mean for listeners —
  does the listener fire before or after the deferred apply?
- ~~`start_time` on session clips: can it be negative when playback was offset?~~
  **Answered:** Session `start_time` is the song time (beat position) when the clip was fired. Updates on each
  launch.
- ~~`position` vs `loop_start`: Max docs say `position` always equals `loop_start` on get, but setting `position`
  preserves loop length whereas setting `loop_start` does not.~~
  **Answered:** Confirmed. `position` always equals `loop_start` on get. Setting `position` slides the loop
  window (preserves length); setting `loop_start` changes only the start (length changes).
- `loop_jump`: fires when the playhead crosses the loop start. Is this a real observable property in the PFL
  bridge, or does it require a listener-only approach?
- `notes`: fires when the note list changes. Does the bridge surface this as a listenable?
- `sample_rate` / `sample_length`: are these available on arrangement audio clips, or session audio clips only?
- ~~What is the sentinel for `playing_position` on a stopped clip?~~
  **Answered:** `0.0` for stopped session clips. Arrangement clips always return `0.0`.

### Mental Model For Live API Clip Properties

**API Parameters:** loop_start, loop_end, start_marker, end_marker, start_time, end_time, length
**UI Handles:** Start Marker, End Marker, Loop Start, Loop End, Loop Brace (the bar between start and end)
**UI Parameter Boxes:** Start, End, Loop Position, Loop Length

#### UI Behavior

The UI parameter boxes are the source-of-truth for all values. The handles and boxes are always in sync with the
following mapping:

**Handle to Box Mapping**

| Dragging Handle | Changes Parameter Box |
| --- | --- |
| Loop Start | Loop Position, Loop Length |
| Loop End | Loop Length |
| Loop Brace | Loop Position |
| Start Marker | Start |
| End Marker | End |

**Box to Handle Mapping**

| Changing Box Value | Moves Handle |
| --- | --- |
| Start | Start Marker |
| End | End Marker |
| Loop Position | Loop Brace (Start and End) |
| Loop Length | Loop End |

**Other Behavior:**

- When looping is on, dragging a Loop Handle will also move the Start/End Marker Handle if they are at the same
  position. This coupling breaks once they are separated.
- When looping is turned off, the end marker and timeline extent are reconciled: if the clip length in the
  timeline is shorter than the marker span, the end marker is clamped to fit within the timeline; if longer, it
  is shortened to match the end marker. The resulting timeline extent equals the marker span, and the clip will
  never grow larger on the timeline.

#### Clean API model

**When Looping is On:**

Both handle sets may be controlled.

| API name | Mental Name | Description |
| --- | --- | --- |
| loop_start | Loop Start | Controls the Loop Start Handle. |
| loop_end | Loop End | Controls the Loop End Handle. |
| start_marker | Start Marker | Controls where clip playback will start from, followed by normal loop range. |
| end_marker | End Marker | Has no effect during loop playback, but will move the inactive handle. |

**When Looping is Off:**

Only the start/end marker handles may be controlled.

| API name | Mental Name | Description |
| --- | --- | --- |
| loop_start | Start Marker | Controls the Start Marker Handle. |
| loop_end | End Marker | Controls the End Marker Handle. |
| start_marker | N/A | Invalid when looping off. |
| end_marker | N/A | Invalid when looping off. |

**At All Times:**

| API name | Mental Name | Description |
| --- | --- | --- |
| looping | Looping Toggle | Enable (or Disable) the looping mode. |
| length | Loop Length | The length of the looping region, whether active or not. |

**In Arrangements:**

| API name | Mental Name | Description |
| --- | --- | --- |
| start_time | Clip Start Time | When the clip starts in the Timeline. |
| end_time | Clip End Time | When the clip ends in the Timeline. |

**In Sessions:**

| API name | Mental Name | Description |
| --- | --- | --- |
| start_time | Fired At | Song time when the clip was fired. |
| end_time | N/A | Not super useful. |

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `view` | `Clip.View` | `single` | `no` | View aspects of this clip. |

#### `view`

- **Returns:** `Clip.View`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

Provides access to view-related state: grid quantization settings and envelope visibility controls. See the
`Clip.View` section at the bottom of this file.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `automation_envelopes` | `list` | `no` | `no` | Read-only list of all automation envelopes. |
| `available_warp_modes` | `list[int]` | `no` | `no` | Audio only. Available warp mode indexes. |
| `canonical_parent` | `object` | `no` | `no` | The clip's parent object (ClipSlot or Track). |
| `color` | `int` | `yes` | `yes` | Clip color as packed RGB `0x00rrggbb`. |
| `color_index` | `int` | `yes` | `yes` | Clip color palette index. |
| `end_marker` | `float` | `yes` | `yes` | End marker position in beats. Only functional when looping is ON. |
| `end_time` | `float` | `no` | `yes` | Arrangement: timeline end. Session: derived, not very useful. |
| `file_path` | `str` | `no` | `no` | Audio only. Absolute path to the referenced audio file. |
| `gain` | `float` | `yes` | `yes` | Audio only. Clip gain, range `0.0` to `1.0`. |
| `gain_display_string` | `str` | `no` | `no` | Audio only. Gain as a human-readable string. |
| `groove` | `Groove\|None` | `yes` | `yes` | Groove object associated with this clip, or `None`. |
| `has_envelopes` | `bool` | `no` | `yes` | `True` if the clip has any automation envelopes. |
| `has_groove` | `bool` | `no` | `no` | `True` if a groove is associated with this clip. |
| `is_arrangement_clip` | `bool` | `no` | `no` | `True` for clips in Arrangement View. |
| `is_audio_clip` | `bool` | `no` | `no` | `True` for audio clips. |
| `is_midi_clip` | `bool` | `no` | `no` | `True` for MIDI clips. Opposite of `is_audio_clip`. |
| `is_overdubbing` | `bool` | `no` | `yes` | Session only. `True` while overdubbing. |
| `is_playing` | `bool` | `no` | `no` | Session only. `True` if playing or recording. |
| `is_recording` | `bool` | `no` | `yes` | Session only. `True` if recording. |
| `is_session_clip` | `bool` | `no` | `no` | `True` for clips in Session View. |
| `is_take_lane_clip` | `bool` | `no` | `no` | `True` for Take Lane clips (also arrangement clips). |
| `is_triggered` | `bool` | `no` | `no` | Session only. `True` while the launch button is blinking. |
| `launch_mode` | `int` | `yes` | `yes` | Launch mode (0=Trigger, 1=Gate, 2=Toggle, 3=Repeat). |
| `launch_quantization` | `int` | `yes` | `yes` | Per-clip launch quantization override. |
| `legato` | `bool` | `yes` | `yes` | `True` if the Legato switch is on. |
| `length` | `float` | `no` | `no` | Always `loop_end - loop_start`, regardless of loop state. |
| `loop_end` | `float` | `yes` | `yes` | Loop region end (loop ON), or end marker alias (loop OFF). |
| `loop_jump` | `bang` | `no` | `yes` | Fires when the playhead crosses the loop start. |
| `loop_start` | `float` | `yes` | `yes` | Loop region start (loop ON), or start marker alias (loop OFF). |
| `looping` | `bool` | `yes` | `yes` | `True` if looping is enabled. |
| `muted` | `bool` | `yes` | `yes` | `True` if the clip's Clip Activator is off (muted). |
| `name` | `str` | `yes` | `yes` | Clip display name. |
| `notes` | `bang` | `no` | `yes` | MIDI only. Fires when the note list changes. |
| `pitch_coarse` | `int` | `yes` | `yes` | Audio only. Transpose in semitones, `-48` to `48`. |
| `pitch_fine` | `float` | `yes` | `yes` | Audio only. Detune in cents, `-50` to `49`. |
| `playing_position` | `float` | `no` | `yes` | Session only. Current playhead position. |
| `playing_status` | `bang` | `no` | `yes` | Fires when playing/trigger status changes. |
| `position` | `float` | `yes` | `yes` | Always equals `loop_start` on get; set slides loop window. |
| `ram_mode` | `bool` | `yes` | `yes` | Audio only. `True` if RAM switch is enabled. |
| `sample_length` | `int` | `no` | `no` | Audio only. Sample length in samples. |
| `sample_rate` | `float` | `no` | `no` | Audio only. Sample rate of the clip's audio file. |
| `signature_denominator` | `int` | `yes` | `yes` | Clip time signature denominator. |
| `signature_numerator` | `int` | `yes` | `yes` | Clip time signature numerator. |
| `start_marker` | `float` | `yes` | `yes` | Start marker position in beats. Setter ignored when loop OFF. |
| `start_time` | `float` | `no` | `yes` | Arrangement: timeline start. Session: song time when fired. |
| `velocity_amount` | `float` | `yes` | `yes` | How much trigger velocity affects clip volume, `0.0` to `1.0`. |
| `warp_markers` | `list[WarpMarker]` | `no` | `yes` | Audio only. Warp markers; observable fires bang on change. |
| `warp_mode` | `int` | `yes` | `yes` | Audio only. Warp mode index. |
| `warping` | `bool` | `yes` | `yes` | Audio only. `True` if warping is enabled. Setting is deferred. |
| `will_record_on_start` | `bool` | `no` | `no` | Always returns `False` via Python API (non-functional). |

#### `automation_envelopes`

- **Type:** `list`
- **Listenable:** `no`
- **Since:** `12.2`

Read-only list of all automation envelopes on this clip. Returns `Envelope` objects. Use
`automation_envelope(parameter)` to get the envelope for a specific parameter, or
`create_automation_envelope(parameter)` to create one.

#### `available_warp_modes`

- **Type:** `list[int]`
- **Listenable:** `no`
- **Since:** `<11`

Audio only. List of integer indexes of warp modes available for this clip. Cross-reference with `warp_mode`.

- **Quirks:** Returns `[0, 1, 2, 3, 4, 6]` for a standard audio clip — REX mode (5) is not available.

#### `canonical_parent`

- **Type:** `object`
- **Listenable:** `no`
- **Since:** `<11`

The clip's canonical parent. For session clips this is the `ClipSlot`; for arrangement clips this is the `Track`.

#### `color`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Clip color as a packed RGB value `0x00rrggbb`. When setting, Live snaps to the nearest color in the clip color
chooser.

- **Quirks:** Setting to `None` raises an `InternalError` (C++ type mismatch).

#### `color_index`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Palette-based color index. Clips always have a color in the Live UI.

- **Quirks:** Setting to `None` raises an `InternalError`.

#### `end_marker`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

**When loop is ON:** Position of the clip's end marker in beats. The end marker has no effect on loop playback but
its handle position is maintained.
**When loop is OFF:** Invalid parameter. The setter is accepted (value changes on readback) but the UI handle does
not move, and the API value is overwritten when looping is toggled back on. Use `loop_end` to control the end
bound when looping is off.

#### `end_time`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Context-dependent read-only value:

- **Arrangement:** timeline end position in beats.
- **Session:** a derived value that is not particularly useful. Equals
  `max(loop_end - start_marker, loop_end - loop_start)` when looping is on; equals
  `end_marker - start_marker` when looping is off. Not recommended for direct use.

#### `file_path`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Audio only. Absolute path to the audio file referenced by this clip.

#### `gain`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. Clip gain, range `0.0` to `1.0`.

#### `gain_display_string`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Audio only. Gain as a human-readable display string (e.g. `"1.3 dB"`). Read-only.

#### `groove`

- **Type:** `Groove | None`
- **Listenable:** `yes`
- **Since:** `11.0`

The Groove object applied to this clip. Groove objects are accessed via `Song.groove_pool`.

- **Limitations:** Setting to `None` to remove the groove is not possible via the Python API — the C++ setter
  requires `TPyHandle<AAbstractGroove>` and rejects `NoneType`. The UI's "Commit Groove" button is also not
  exposed.

#### `has_envelopes`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the clip contains any automation envelopes. Fires listener when envelopes are added or removed.

#### `has_groove`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `11.0`

`True` if a groove is associated with this clip.

#### `is_arrangement_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for clips in Arrangement View. Take Lane clips are also arrangement clips (`is_take_lane_clip` and
`is_arrangement_clip` can both be `True`).

#### `is_audio_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for audio clips. Use to gate audio-only members before accessing them.

#### `is_midi_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for MIDI clips. Exact opposite of `is_audio_clip`.

#### `is_overdubbing`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Session only. `True` while the clip is overdubbing. Always `False` on arrangement clips.

#### `is_playing`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Session only. `True` if the clip is currently playing or recording. Always `False` on arrangement clips, even
while the transport plays through the clip's time range. Use `fire()` and `stop()` to control playback.

#### `is_recording`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Session only. `True` if the clip is currently recording. Always `False` on arrangement clips.

#### `is_session_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `12.2`

`True` for clips in Session View.

#### `is_take_lane_clip`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `12.2`

`True` for Take Lane clips. These are a subtype of arrangement clips; `is_arrangement_clip` is also `True`.

#### `is_triggered`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Session only. `True` while the Clip Launch button is blinking (launch queued, waiting on quantization). Always
`False` on arrangement clips.

#### `launch_mode`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `11.0`

Launch mode: `0` = Trigger (default), `1` = Gate, `2` = Toggle, `3` = Repeat.

#### `launch_quantization`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `11.0`

Per-clip launch quantization, overrides the song's global quantization when set. Values: `0`=Global (default),
`1`=None, `2`=8 Bars, `3`=4 Bars, `4`=2 Bars, `5`=1 Bar, `6`=1/2, `7`=1/2T, `8`=1/4, `9`=1/4T, `10`=1/8,
`11`=1/8T, `12`=1/16, `13`=1/16T, `14`=1/32.

#### `legato`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `11.0`

`True` when the Legato switch in the clip's Launch settings is on.

#### `length`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `<11`

Always equals `loop_end - loop_start`, regardless of whether looping is enabled and regardless of marker
positions. This is NOT `end_marker - start_marker`. Units are beats for MIDI and warped audio; seconds for
unwarped audio.

#### `loop_end`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

**When loop is ON:** controls the Loop End Handle (right edge of the loop brace). Independent of `end_marker`.
**When loop is OFF:** aliases the End Marker Handle — setting `loop_end` moves the end marker and adjusts the
clip's timeline extent. This is the **only** way to control the end bound when looping is off. Units are beats
for MIDI and warped audio; seconds for unwarped audio.

#### `loop_jump`

- **Type:** `bang` (no value)
- **Listenable:** `yes`
- **Since:** `<11`

Observable that fires when the clip playhead crosses the loop start marker. Used to detect loop cycles.

#### `loop_start`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

**When loop is ON:** controls the Loop Start Handle (left edge of the loop brace). Independent of `start_marker`.
**When loop is OFF:** aliases the Start Marker Handle — setting `loop_start` moves the start marker. This is the
**only** way to control the start bound when looping is off; `start_marker` writes are silently ignored. Units
are beats for MIDI and warped audio; seconds for unwarped audio. Beat time `0` corresponds to position `1.1.1`
in the clip view ruler.

#### `looping`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if clip looping is enabled. Toggling this switches which marker system is active — with loop ON,
`loop_start`/`loop_end` control the loop brace independently of the markers; with loop OFF, they alias the
start/end markers.

- **Quirks:** **Toggle ON -> OFF (arrangement):** The end marker and timeline extent are reconciled — if the
  timeline is shorter than the marker span, the end marker is clamped; if longer, the timeline shrinks. The clip
  never grows on toggle. **Toggle OFF -> ON:** the UI's saved loop marker positions are restored. Unwarped audio
  clips cannot be looped.

#### `muted`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` when the clip's Clip Activator button is off (clip is deactivated/muted).

#### `name`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Display name of the clip.

#### `notes`

- **Type:** `bang` (no value)
- **Listenable:** `yes`
- **Since:** `<11`

MIDI only. Observable that fires when the clip's note list changes. Use `get_notes_extended()` or
`get_all_notes_extended()` to retrieve current notes after receiving this notification.

#### `pitch_coarse`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. Pitch transposition in semitones (Transpose knob). Range: `-48` to `48`.

#### `pitch_fine`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. Fine pitch adjustment in cents (Detune knob). Range: `-50` to `49`.

#### `playing_position`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Session only. Current playhead position. For MIDI and warped audio: beats of absolute clip time (beat `0` =
position `1` in the clip ruler). For unwarped audio: seconds from clip start. Stopped clips return `0.0`. Always
`0.0` on arrangement clips.

#### `playing_status`

- **Type:** `bang` (no value)
- **Listenable:** `yes`
- **Since:** `<11`

Observable that fires when the clip's playing or trigger status changes. Has no readable value; use `is_playing`,
`is_recording`, `is_triggered` to read current state after receiving the notification.

#### `position`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Loop position / window slide control. On get, always equals `loop_start`. On set, moves `loop_start` to the
specified position and adjusts `loop_end` to preserve `length` (unlike setting `loop_start` directly, which
changes `length`). Works in both loop ON and OFF modes.

- **Quirks:** When the new loop window extends past `start_marker` or `end_marker`, those markers are auto-pushed
  to stay within/at the loop bounds.

#### `ram_mode`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. `True` when the clip's RAM mode switch is enabled.

#### `sample_length`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Audio only. Length of the clip's audio sample in samples (not beats).

#### `sample_rate`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `11.0`

Audio only. Sample rate of the clip's audio file in Hz.

#### `signature_denominator`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Clip time signature denominator.

#### `signature_numerator`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Clip time signature numerator.

#### `start_marker`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

**When loop is ON:** Position of the clip's start marker in beats. Fully independent of `loop_start`. Playback
starts here and goes until `loop_end` before looping back to `loop_start` — can define an "intro" or shorter
first loop.
**When loop is OFF:** setter is **silently ignored** — the API value does not change. Use `loop_start` to control
the start bound in this state.

#### `start_time`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Context-dependent start time in beats (read-only):

- **Arrangement clips:** start position within the arrangement timeline.
- **Session clips:** song time (beat position) when the clip was fired. Updates each time the clip is launched.

#### `velocity_amount`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.0`

Controls how much the velocity of the MIDI note triggering the clip affects the clip's volume. `0.0` = no effect;
`1.0` = full effect.

#### `warp_markers`

- **Type:** `list[WarpMarker]` (WarpMarkerVector)
- **Listenable:** `yes`
- **Since:** `11.0`

Audio only. The clip's warp markers as a list. Returns `WarpMarker` objects, each with `beat_time: float` and
`sample_time: float`. The observable fires a bang when markers change.

- **Quirks:** The last marker in the list is a phantom marker (1/32 beat after the last visible marker) used
  internally to derive the final-segment BPM — it is not shown in the Live UI. `WarpMarker.sample_time` is in
  **seconds**, not samples, despite the field name. This differs from `beat_to_sample_time()` which returns
  samples.

#### `warp_mode`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. Warp mode as an integer. Must be one of the values in `available_warp_modes`. Values: `0` = Beats,
`1` = Tones, `2` = Texture, `3` = Re-Pitch, `4` = Complex, `5` = REX, `6` = Complex Pro.

#### `warping`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Audio only. `True` when the Warp switch is enabled.

- **Quirks:** Setting this property is internally deferred by Live. In sequences of API calls within a single
  event, the actual order of operations may differ from the call order. Introduce a tick delay between the set
  and any dependent operation.

#### `will_record_on_start`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Documented as `True` when recording will start on armed MIDI tracks. However, probing shows it always returns
`False` through the Python API. Recording state is covered by `is_recording` and `is_overdubbing`.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `add_new_notes(notes: tuple[MidiNoteSpecification, ...])` | `list[int]` | MIDI only. Add new notes; returns assigned note IDs. |
| `add_warp_marker(warp_marker: WarpMarker)` | `None` | Audio only. Add a warp marker. |
| `apply_note_modifications(notes: MidiNoteVector)` | `None` | MIDI only. Modify existing notes in-place by note ID. |
| `automation_envelope(device_parameter)` | `Envelope\|None` | Return the envelope for a parameter, or `None`. |
| `beat_to_sample_time(beat_time: float)` | `float` | Audio only. Convert beat time to sample time (warped). |
| `clear_all_envelopes()` | `None` | Remove all automation envelopes. |
| `clear_envelope(device_parameter)` | `None` | Remove the envelope for a specific parameter. |
| `create_automation_envelope(device_parameter)` | `Envelope` | Create and return an envelope for a parameter. |
| `crop()` | `None` | Crop clip to loop or start/end markers. |
| `deselect_all_notes()` | `None` | MIDI only. Deselect all notes. |
| `duplicate_loop()` | `None` | MIDI only. Double the loop length and duplicate content. |
| `duplicate_notes_by_id(note_ids, destination_time, transposition_amount)` | `list[int]` | MIDI only. Duplicate notes by ID. Returns new IDs. |
| `duplicate_region(region_start, region_length, destination_time, pitch, transposition_amount)` | `None` | MIDI only. Duplicate notes in a region. |
| `fire()` | `None` | Session only. Launch this clip. |
| `get_all_notes_extended(return_fields)` | `MidiNoteVector` | MIDI only. Return all notes. |
| `get_notes(from_time, from_pitch, time_span, pitch_span)` | `tuple` | **Deprecated.** MIDI only. Return notes as tuples. |
| `get_notes_by_id(note_ids, return_fields)` | `MidiNoteVector` | MIDI only. Return notes by ID. |
| `get_notes_extended(from_pitch, pitch_span, from_time, time_span, return_fields)` | `MidiNoteVector` | MIDI only. Return notes in a region. |
| `get_selected_notes()` | `tuple` | **Deprecated.** MIDI only. Return selected notes. |
| `get_selected_notes_extended(return_fields)` | `MidiNoteVector` | MIDI only. Return selected notes. |
| `move_playing_pos(beats: float)` | `None` | Session only. Relative jump of clip playhead. |
| `move_warp_marker(beat_time: float, beat_time_distance: float)` | `None` | Audio only. Move a warp marker. |
| `note_number_to_name(midi_pitch: int)` | `str` | MIDI only. Convert MIDI note number to name. |
| `quantize(quantization_grid: int, amount: float)` | `None` | MIDI only. Quantize all notes. |
| `quantize_pitch(pitch: int, quantization_grid: int, amount: float)` | `None` | MIDI only. Quantize notes of one pitch. |
| `remove_notes(from_time, from_pitch, time_span, pitch_span)` | `None` | **Deprecated.** MIDI only. Delete notes in a region. |
| `remove_notes_by_id(note_ids: list[int])` | `None` | MIDI only. Delete notes by ID. |
| `remove_notes_extended(from_pitch, pitch_span, from_time, time_span)` | `None` | MIDI only. Delete notes in a region. |
| `remove_warp_marker(beat_time: float)` | `None` | Audio only. Remove a warp marker. |
| `replace_selected_notes(notes_tuple)` | `None` | **Deprecated.** MIDI only. Replace selected notes. |
| `sample_to_beat_time(sample_time: float)` | `float` | Audio only. Convert sample time to beat time (warped). |
| `scrub(beat_time: float)` | `None` | Session only. Audition a looping snippet at a position. |
| `seconds_to_sample_time(seconds: float)` | `float` | Audio only. Convert seconds to sample time (unwarped). |
| `select_all_notes()` | `None` | MIDI only. Select all notes. |
| `select_notes_by_id(note_ids: list[int])` | `None` | MIDI only. Select specific notes by ID. |
| `set_fire_button_state(state: bool)` | `None` | Simulate holding/releasing the clip launch button. |
| `set_notes(notes_tuple)` | `None` | **Deprecated.** MIDI only. Add notes from tuple data. |
| `stop()` | `None` | Session only. Stop this clip. |
| `stop_scrub()` | `None` | Session only. End an active scrub session. |

#### `add_new_notes(notes)`

- **Returns:** `list[int]` -- list of note IDs for the added notes
- **Args:**
  - `notes: tuple[MidiNoteSpecification, ...]` -- a **tuple** of `Live.Clip.MidiNoteSpecification` objects
- **Raises:** `InternalError` if passed dicts or a list instead of a tuple of `MidiNoteSpecification`
- **Since:** `11.0`

Adds notes to the clip. The argument must be a **tuple** of `Live.Clip.MidiNoteSpecification` objects — **not** a
list of dicts.

`MidiNoteSpecification` is constructed with keyword args:

```python
import Live
spec = Live.Clip.MidiNoteSpecification(
    pitch=60,          # int, required: MIDI note number 0-127
    start_time=0.0,    # float, required: start in beats of absolute clip time
    duration=0.5,      # float, required: note length in beats
    velocity=100.0,    # float, optional, default 100
    release_velocity=64.0,  # float, optional, default 64
    velocity_deviation=0.0, # float, optional, default 0.0
    mute=False,        # bool, optional, default False
    probability=1.0,   # float, optional, default 1.0
)
clip.add_new_notes((spec,))  # must be a tuple
```

Returns the list of integer note IDs assigned to the new notes.

#### `add_warp_marker(warp_marker)`

- **Returns:** `None`
- **Args:**
  - `warp_marker: Live.Clip.WarpMarker` -- native C++ `TWarpMarker` type
- **Raises:** `Segment length out of range` if resulting segment BPM exceeds `[5, 999]` or a marker already
  exists at the same `beat_time` with a different `sample_time`; `Warp marker sample time is out of range` if
  `sample_time` exceeds clip duration.
- **Since:** `11.0.5`

Adds a warp marker. The argument is a `Live.Clip.WarpMarker` object, **not** a dict. Constructor:
`Live.Clip.WarpMarker(sample_time, beat_time)` — note `sample_time` comes **first**. Does **not** accept keyword
arguments.

- **Quirks:** `sample_time` is in **seconds** (not samples). Adding a duplicate marker with the same `beat_time`
  and `sample_time` as an existing marker is a silent no-op.

#### `apply_note_modifications(notes)`

- **Returns:** `None`
- **Args:**
  - `notes: MidiNoteVector` -- the **original vector** returned by `get_all_notes_extended`, with attributes
    modified in-place
- **Raises:** `InternalError` if passed a Python `list` instead of the native `MidiNoteVector`
- **Since:** `11.0`

In-place modification of existing notes. The intended workflow is:

1. `notes = clip.get_all_notes_extended()` -- returns a `MidiNoteVector`
2. Modify note attributes in-place: `notes[0].velocity = 50`
3. `clip.apply_note_modifications(notes)` -- pass the **same vector** back

The argument must be the original `MidiNoteVector` object (Boost.Python-wrapped `std::vector`). Passing a plain
Python `list` raises `InternalError`.

#### `automation_envelope(device_parameter)`

- **Returns:** `Envelope | None`
- **Args:**
  - `device_parameter: DeviceParameter`
- **Since:** `<11`

Returns the automation envelope for the given device parameter, or `None` if no envelope exists. Always returns
`None` for Arrangement clips and for parameters on a different track.

#### `beat_to_sample_time(beat_time)`

- **Returns:** `float` -- sample time in **samples** (not seconds)
- **Args:**
  - `beat_time: float`
- **Raises:** Error if clip is not warped.
- **Since:** `<11`

Audio only. Converts beat time to sample time for warped clips. Returns the value in **samples** (not seconds).

- **Quirks:** The return unit (samples) differs from `WarpMarker.sample_time` which is in seconds. Divide by
  `sample_rate` to convert.

#### `clear_all_envelopes()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Deletes all clip-level automation envelopes.

#### `clear_envelope(device_parameter)`

- **Returns:** `None`
- **Args:**
  - `device_parameter: DeviceParameter`
- **Since:** `<11`

Removes the clip's automation envelope for a specific device parameter.

#### `create_automation_envelope(device_parameter)`

- **Returns:** `Envelope`
- **Args:**
  - `device_parameter: DeviceParameter`
- **Since:** `<11`

Creates and returns an automation envelope for the given device parameter. Use `automation_envelope(parameter)`
first to check if one already exists.

#### `crop()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

If the clip is looped, removes content outside the loop. If not looped, removes content outside the start/end
markers.

#### `deselect_all_notes()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

MIDI only. Deselects all notes in the clip.

#### `duplicate_loop()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

MIDI only. Doubles the loop by moving `loop_end` to the right and duplicating all notes and envelopes into the new
region. If not looped, doubles the start/end range instead.

#### `duplicate_notes_by_id(note_ids, destination_time=None, transposition_amount=0)`

- **Returns:** `list[int]` -- note IDs of the newly created duplicate notes
- **Args:**
  - `note_ids: list[int]` -- IDs of notes to duplicate
  - `destination_time: float (optional)` -- beat time to place duplicates
  - `transposition_amount: int (optional)` -- semitones to transpose duplicates
- **Since:** `11.1.2`

MIDI only. Duplicates notes matching the given IDs. Preserves per-note expression envelopes (MDE) on the copies.

#### `duplicate_region(region_start, region_length, destination_time, pitch=-1, transposition_amount=0)`

- **Returns:** `None`
- **Args:**
  - `region_start: float` -- start of the region in beats
  - `region_length: float` -- length in beats
  - `destination_time: float` -- beat time to place the duplicated notes
  - `pitch: int (optional)` -- only duplicate this pitch; `-1` = all pitches (default)
  - `transposition_amount: int (optional)` -- semitones to transpose
- **Since:** `<11`

MIDI only. Duplicates all notes in the specified time region. Preserves per-note expression envelopes (MDE).

#### `fire()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Session only. Launches this clip. Equivalent to pressing the Clip Launch button. No-op on arrangement clips.

#### `get_all_notes_extended(return_fields=None)`

- **Returns:** `MidiNoteVector` -- native C++ vector of `MidiNote` objects
- **Args:**
  - `return_fields: dict (optional)` -- `{"return": [field_names]}` to limit returned fields
- **Since:** `11.1`

MIDI only. Returns all notes in the clip regardless of marker positions. Each element is a `MidiNote` object with
writable attributes: `note_id`, `pitch`, `start_time`, `duration`, `velocity`, `mute`, `probability`,
`velocity_deviation`, `release_velocity`. The returned vector is the same type expected by
`apply_note_modifications()`.

#### `get_notes(from_time, from_pitch, time_span, pitch_span)`

- **Returns:** `tuple` -- tuple of tuples `(pitch, time, duration, velocity, mute)`
- **Args:**
  - `from_time: float`, `from_pitch: int`, `time_span: float`, `pitch_span: int`
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `get_notes_extended()`.

#### `get_notes_by_id(note_ids, return_fields=None)`

- **Returns:** `MidiNoteVector`
- **Args:**
  - `note_ids: object` -- list of note IDs
  - `return_fields: dict (optional)`
- **Since:** `11.0`

MIDI only. Returns notes matching the given IDs.

#### `get_notes_extended(from_pitch, pitch_span, from_time, time_span, return_fields=None)`

- **Returns:** `MidiNoteVector`
- **Args:**
  - `from_pitch: int`, `pitch_span: int`, `from_time: float`, `time_span: float`
  - `return_fields: dict (optional)`
- **Since:** `11.0`

MIDI only. Returns notes whose start times fall within the given region. Replaces the deprecated `get_notes`.

#### `get_selected_notes()`

- **Returns:** `tuple` -- tuple of tuples `(pitch, time, duration, velocity, mute)`
- **Args:** None
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `get_selected_notes_extended()`.

#### `get_selected_notes_extended(return_fields=None)`

- **Returns:** `MidiNoteVector`
- **Args:**
  - `return_fields: dict (optional)`
- **Since:** `11.0`

MIDI only. Returns the currently selected notes.

#### `move_playing_pos(beats)`

- **Returns:** `None`
- **Args:**
  - `beats: float` -- relative jump in beats; negative = backwards
- **Since:** `<11`

Session only. Relative unquantized jump from the current playhead position within the clip's local timeline. Does
not affect the global song playhead. No-op when stopped or on arrangement clips.

#### `move_warp_marker(beat_time, beat_time_distance)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` -- beat time of the marker to move
  - `beat_time_distance: float` -- relative distance to move it
- **Since:** `11.0`

Audio only. Moves the warp marker at `beat_time` by `beat_time_distance`.

#### `note_number_to_name(midi_pitch)`

- **Returns:** `str`
- **Args:**
  - `midi_pitch: int` -- MIDI note number `0-127`
- **Since:** `12.1`

MIDI only. Returns a human-readable name for the given MIDI note number (e.g. `"C3"`, `"F#4"`). Takes into account
the clip's scale, tonal spelling settings, and current tuning system.

#### `quantize(quantization_grid, amount)`

- **Returns:** `None`
- **Args:**
  - `quantization_grid: int` -- `GridQuantization` enum value **1-8**
  - `amount: float` -- quantization strength `0.0-1.0`
- **Raises:** `InternalError: Invalid quantization.` for values outside 1-8
- **Since:** `<11`

MIDI only. Quantizes all notes to the given grid using the song's current swing setting. Values: `1`=8 Bars,
`2`=4 Bars, `3`=2 Bars, `4`=1 Bar, `5`=1/2, `6`=1/4, `7`=1/8, `8`=1/16.

#### `quantize_pitch(pitch, quantization_grid, amount)`

- **Returns:** `None`
- **Args:**
  - `pitch: int` -- MIDI pitch to quantize (0-127)
  - `quantization_grid: int` -- `GridQuantization` enum value **1-8**
  - `amount: float` -- quantization strength `0.0-1.0`
- **Since:** `<11`

MIDI only. Same as `quantize` but restricted to notes of a single pitch.

#### `remove_notes(from_time, from_pitch, time_span, pitch_span)`

- **Returns:** `None`
- **Args:**
  - `from_time: float`, `from_pitch: int`, `time_span: float`, `pitch_span: int`
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `remove_notes_extended()` and `remove_notes_by_id()`.

#### `remove_notes_by_id(note_ids)`

- **Returns:** `None`
- **Args:**
  - `note_ids: list[int]`
- **Since:** `11.0`

MIDI only. Deletes all notes matching the given IDs.

#### `remove_notes_extended(from_pitch, pitch_span, from_time, time_span)`

- **Returns:** `None`
- **Args:**
  - `from_pitch: int`, `pitch_span: int`, `from_time: float`, `time_span: float`
- **Since:** `11.0`

MIDI only. Deletes all notes whose start times fall in the given region.

#### `remove_warp_marker(beat_time)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` -- beat time of the marker to remove
- **Since:** `11.0`

Audio only. Removes the warp marker at `beat_time`.

#### `replace_selected_notes(notes_tuple)`

- **Returns:** `None`
- **Args:**
  - `notes_tuple: tuple`
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `apply_note_modifications()` or `remove_notes_extended()` +
`add_new_notes()`.

#### `sample_to_beat_time(sample_time)`

- **Returns:** `float`
- **Args:**
  - `sample_time: float` -- sample time in **samples** (not seconds)
- **Raises:** Error if clip is not warped.
- **Since:** `<11`

Audio only. Converts sample time to beat time for warped clips. Inverse of `beat_to_sample_time`.

#### `scrub(beat_time)`

- **Returns:** `None`
- **Args:**
  - `beat_time: float` -- absolute clip beat time to scrub to
- **Since:** `<11`

Session only. Auditions a looping snippet at an absolute beat position. The snippet size is determined by the
global `clip_trigger_quantization` setting. No-op on arrangement clips.

#### `seconds_to_sample_time(seconds)`

- **Returns:** `float`
- **Args:**
  - `seconds: float`
- **Raises:** Error if clip is warped.
- **Since:** `<11`

Audio only. Converts seconds to sample time for **unwarped** clips. Note: this is the opposite requirement from
`beat_to_sample_time`/`sample_to_beat_time` which require warped clips.

#### `select_all_notes()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

MIDI only. Selects all notes in the clip.

#### `select_notes_by_id(note_ids)`

- **Returns:** `None`
- **Args:**
  - `note_ids: list[int]`
- **Since:** `11.0.6`

MIDI only. Selects notes matching the given IDs.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:**
  - `state: bool`
- **Since:** `<11`

Simulates pressing and holding the clip launch button until `state=False` or the clip is otherwise stopped.

#### `set_notes(notes_tuple)`

- **Returns:** `None`
- **Args:**
  - `notes_tuple: tuple`
- **Since:** `<11`

**Deprecated.** MIDI only. Superseded by `add_new_notes()`.

#### `stop()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Session only. Stops the clip if it is currently playing or recording. No-op on arrangement clips.

#### `stop_scrub()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Session only. Ends a scrub initiated with `scrub()`. No-op on arrangement clips.

---

## Clip.View

> `Live.Clip.Clip.View`

Provides access to view aspects of a clip: grid display settings and envelope visibility controls in the Clip
Detail View.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `grid_is_triplet` | `bool` | `yes` | `no` | Whether the clip displays a triplet grid. |
| `grid_quantization` | `int` | `yes` | `no` | Grid quantization resolution (`GridQuantization` enum). |

#### `grid_is_triplet`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Controls whether the clip's detail view displays a triplet grid. Works on any clip regardless of whether it is the
detail clip.

#### `grid_quantization`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

Grid quantization resolution for the clip's detail view. Uses the `Clip.GridQuantization` enum (not
`Song.Quantization`). Values: `0`=No grid (off), `1`=8 Bars, `2`=4 Bars, `3`=2 Bars, `4`=1 Bar, `5`=1/2,
`6`=1/4, `7`=1/8, `8`=1/16, `9`=1/32. Triplet variants are controlled separately by `grid_is_triplet`.

- **Quirks:** `Clip.quantize()` and `Clip.quantize_pitch()` use the same enum but only accept values **1-8**
  (0 and 9 raise `Invalid quantization`). The value is an int enum; passing a float raises a type mismatch error.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `hide_envelope()` | `None` | Hide the Envelopes box in Clip Detail View. |
| `select_envelope_parameter(parameter: DeviceParameter)` | `None` | Select a parameter for envelope display. |
| `show_envelope()` | `None` | Show the Envelopes box in Clip Detail View. |
| `show_loop()` | `None` | Scroll the Detail View to show the loop region. |

#### `hide_envelope()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Switches the clip detail view away from the Envelopes tab. Only has an effect when the clip is the detail clip;
silently no-ops otherwise.

#### `select_envelope_parameter(parameter)`

- **Returns:** `None`
- **Args:**
  - `parameter: DeviceParameter`
- **Since:** `<11`

Selects the specified device parameter in the Envelopes box for display/editing. Only has an effect when the clip
is the detail clip; silently no-ops otherwise.

#### `show_envelope()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Switches the clip detail view to the Envelopes tab. Only has an effect when the clip is the detail clip.

#### `show_loop()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Scrolls the clip detail view to show the current loop region. Only has an effect when the clip is the detail clip.


### reference/tracks/ClipSlot.md

# ClipSlot

> `Live.ClipSlot.ClipSlot`

Represents a single cell in Live's Session View matrix -- the intersection of one track and one
scene row. A slot always exists even when empty; it can contain a clip or be used as a stop
trigger. Group track slots have additional aggregate behavior over the tracks within the group.

??? note "Raw probe notes (temporary)"
    #### Color behavior (probed 2026-02-17)

    - `color` and `color_index` have **no setter** -- `set` raises
      `"property of 'ClipSlot' object has no setter"` on both regular and group slots.
    - **Regular slots** (empty or with clip): both return `None`. Even when `has_clip=True`, the slot's own
      color is `None` -- the clip's color is only accessible via `clip.color`.
    - **Group slots** (empty row): both return `None`.
    - **Group slots** (clips in child tracks): returns the **first** contained clip's color/color_index. In a
      group with children at `color_index=5` (green) and `color_index=22` (blue), the group slot reported
      `color_index=5`.
    - The Live UI allows "setting" a group slot's color, but this is a UI-level composite action that sets
      `Clip.color` on each child clip individually -- it is not exposed through `ClipSlot.color`.

    #### controls_other_clips (probed 2026-02-17)

    - Only meaningful on **group track slots** -- always `False` on regular (non-group) slots.
    - `True` when at least one child track slot at the same scene index contains an **active**
      (non-deactivated) clip. Deactivated clips do not count.
    - Tested scenarios (6-track session: 1-MIDI, 2 Group containing 3 MIDI + 4 Audio, 5 Group containing
      6 Audio):
        - Empty row -> `False`
        - Row with active clip in child track -> `True`
        - Row with deactivated clip in child track -> `False`
    - **Arm state does not affect the value** -- arming a child track does not change the result.
    - **Follow actions do not affect the value** -- clips with "next" follow actions on regular (non-group)
      tracks still report `False`.
    - Visually corresponds to the hatched clip indicator shown on the right side of group slots in the
      Live UI.

    #### will_record_on_start (probed 2026-02-17)

    - Always returns `False` through the Python API regardless of conditions tested:
        - Armed/unarmed track, empty/occupied slots, MIDI and audio tracks
        - Transport playing/stopped
        - `session_record` on/off, `overdub` on/off
        - Group track slots, child track slots, top-level track slots
        - "Start Recording on Scene Launch" preference on/off
    - The property reads without error but never reports `True`. May only function through the Max LOM
      path or within listener callback contexts. **Skipped** from the public API spec.

### Open Questions

- ~~For non-group slots: do `is_playing` and `is_recording` reflect the clip's actual playback
  state, or are they derived from `playing_status` (which would make them always `0` for
  non-group slots)?~~ **Resolved (probed, Live 12.3.5):** `is_playing` and `is_recording`
  reflect the clip's actual state on non-group slots, despite `playing_status` always being `0`
  there. The Max docs' claim that they derive from `playing_status` is incorrect for non-group
  slots -- they appear to have an independent implementation.
- ~~What does `color` / `color_index` return when `has_clip=True` on a non-group slot?~~ **Resolved:**
  returns `None` -- see probe notes.
- What exception type does `delete_clip()` raise when the slot is empty?
- Can `has_stop_button` be set on a group slot, or is it read-only there?

### Children

| Child  | Returns      | Shape    | Listenable | Summary                                          |
| ------ | ------------ | -------- | ---------- | ------------------------------------------------ |
| `clip` | `Clip\|None` | `single` | `yes`      | The clip owned by this slot, or `None` if empty. |

#### `clip`

- **Type:** `Clip | None`
- **Listenable:** `yes` (via `has_clip` listener -- `clip` itself is not directly listenable, but `has_clip`
  fires when a clip is created or deleted)
- **Since:** `<11`

The clip contained in this slot. `None` when the slot is empty (`has_clip=False`). Always
check `has_clip` before accessing `clip` properties. The Max docs note that the Max LOM
returns `id 0` (equivalent to `None`) when the slot is empty.

### Properties

| Property               | Type                   | Settable | Listenable | Summary                                                                                |
| ---------------------- | ---------------------- | -------- | ---------- | -------------------------------------------------------------------------------------- |
| `color`                | `int\|None`            | no       | `yes`      | Color of the first clip in a group slot. `None` for regular empty slots.               |
| `color_index`          | `int\|None`            | no       | `yes`      | Color index of the first clip in a group slot. `None` for regular empty slots.         |
| `controls_other_clips` | `bool`                 | no       | `yes`      | Group slot only: `True` if child tracks have active (non-deactivated) clips.           |
| `has_clip`             | `bool`                 | no       | `yes`      | `True` if a clip exists in this slot.                                                  |
| `has_stop_button`      | `bool`                 | `bool`   | `yes`      | Whether this slot has a stop button. When fired while empty, stops the track.          |
| `is_group_slot`        | `bool`                 | no       | `no`       | `True` if this slot belongs to a group track.                                          |
| `is_playing`           | `bool`                 | no       | `no`       | `True` if the clip in this slot is playing. Works on both group and non-group slots.   |
| `is_recording`         | `bool`                 | no       | `no`       | `True` if the clip in this slot is recording. Works on both group and non-group slots. |
| `is_triggered`         | `bool`                 | no       | `yes`      | `True` while a clip launch, stop, or record button in this slot is blinking.           |
| `playing_status`       | `ClipSlotPlayingState` | no       | `yes`      | Aggregate playback state for group slots only; always `0` for non-group slots.         |
| `will_record_on_start` | `bool`                 | no       | `no`       | `True` if firing this slot will begin recording. Currently always returns `False`.     |

#### `color`

- **Type:** `int | None`
- **Listenable:** `yes`
- **Since:** `<11`

Read-only derived color. Returns `None` on all regular slots -- even when `has_clip=True`.
For group slots: returns the packed RGB color (`0x00rrggbb`) of the first clip in the group;
`None` when no child clips exist in the row. No setter exists on either regular or group
slots -- attempting `set` raises `"property of 'ClipSlot' object has no setter"`. To set a
clip's color, use the clip's own `color` property. Note: the Live UI allows coloring a group
slot (which colors all child clips), but this is an internal composite action not exposed
through the API.

#### `color_index`

- **Type:** `int | None`
- **Listenable:** `yes`
- **Since:** `<11`

Read-only derived color index. Returns `None` on all regular slots -- even when
`has_clip=True`. For group slots: returns the color index of the first clip in the group;
`None` when no child clips exist in the row. No setter exists.

#### `controls_other_clips`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` only for group track slots that have at least one **active** (non-deactivated) clip in
any child track at this scene row. Deactivated clips do not count -- a group slot with only
deactivated child clips reports `False`. When `True`, firing the slot will launch those child
track clips. Always `False` for non-group slots, regardless of follow actions or other
cross-slot relationships. Arm state of child tracks does not affect the value.

#### `has_clip`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` when this slot contains a clip. Use this to gate access to `clip` and clip-specific
operations. Fires its listener when a clip is created or deleted in this slot.

#### `has_stop_button`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

When `True`, firing this empty slot (or pressing the stop button for the track) stops any
currently playing or recording clip on this track. For group slots, stops all clips within
child tracks.

#### `is_group_slot`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this slot belongs to a group track. Group slots aggregate the state of child track
slots at the same scene row and expose `controls_other_clips` and `playing_status`.

#### `is_playing`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the clip in this slot is currently playing. Works on both group and non-group slots.
For non-group slots, reflects the clip's actual playback state (not derived from `playing_status`,
which is always `0` for non-group slots -- contradicting the Max docs). For group slots, `True` if
at least one child clip is playing.

#### `is_recording`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the clip in this slot is currently recording. Works on both group and non-group slots.
For non-group slots, reflects the clip's actual recording state (not derived from `playing_status`,
which is always `0` for non-group slots -- contradicting the Max docs). For group slots, `True` if
at least one child clip is recording.

#### `is_triggered`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` while a clip launch button, clip stop button, or clip record button in this slot is
blinking (queued, waiting on launch quantization). Fires listener on state change. Works on
both group and non-group slots. During session recording with launch quantization, `is_triggered`
is `True` in the target slot while `Song.session_record_status == 2` (triggered phase), then
transitions to `False` when recording actually starts.

#### `playing_status`

- **Type:** `ClipSlotPlayingState` (int)
- **Listenable:** `yes`
- **Since:** `<11`

Aggregate playback state for group track slots. Confirmed always `0` for non-group slots,
regardless of the clip's actual playback or recording state. Note that `is_playing` and
`is_recording` still work correctly on non-group slots despite `playing_status` being `0` --
they have an independent implementation.

**Listener behavior (probed 12.3.5):** The listener fires on group slots when child clip
playback state changes (value = new `ClipSlotPlayingState`). On non-group slots, the listener
does not fire -- subscribe succeeds but no events are delivered.

`ClipSlotPlayingState` enum values:

- `0` = stopped (all child track clips stopped, or not a group slot)
- `1` = playing (at least one child clip is playing)
- `2` = recording (at least one child clip is playing or recording)

#### `will_record_on_start`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Documented as `True` when firing this slot will trigger recording rather than playing back an
existing clip. However, probing shows it **always returns `False`** through the Python API
regardless of arm state, clip presence, transport state, session record/overdub toggles, group
track membership, or the "Start Recording on Scene Launch" preference. May only function
through the Max LOM path or within listener callback contexts. The information it claims to
provide is trivially derivable from `track.arm` and `has_clip`.

### Methods

| Method                                                                   | Returns | Summary                                                     |
| ------------------------------------------------------------------------ | ------- | ----------------------------------------------------------- |
| `create_audio_clip(path: str)`                                           | `Clip`  | Create an audio clip from a file in this slot.              |
| `create_clip(length: float)`                                             | `Clip`  | Create an empty MIDI clip of the given length in beats.     |
| `delete_clip()`                                                          | `None`  | Delete the clip in this slot.                               |
| `duplicate_clip_to(target_slot: ClipSlot)`                               | `None`  | Copy this slot's clip to another slot.                      |
| `fire(record_length=None, launch_quantization=None, force_legato=False)` | `None`  | Fire the clip, trigger the stop button, or begin recording. |
| `set_fire_button_state(state: bool)`                                     | `None`  | Programmatically hold or release the clip launch button.    |
| `stop()`                                                                 | `None`  | Stop the playing or recording clip on this track.           |

#### `create_audio_clip(path: str)`

- **Returns:** `Clip`
- **Args:** `path: str` -- absolute path to a valid audio file
- **Raises:** Error if slot is non-empty, track is not an audio track, track is frozen, or path is not a
  valid audio file.
- **Since:** `11.3`

Creates an audio clip referencing the file at the given absolute path. Raises an error if the
slot already contains a clip, if the track is not an audio track, or if the track is frozen.

#### `create_clip(length: float)`

- **Returns:** `Clip`
- **Args:** `length: float` -- clip length in beats, must be `> 0.0`
- **Raises:** Error if slot is non-empty or track is not a MIDI track.
- **Since:** `<11`

Creates an empty MIDI clip. Can only be called on empty slots in MIDI tracks. Length is in
beats and must be greater than `0.0`.

#### `delete_clip()`

- **Returns:** `None`
- **Raises:** Exception if the slot is empty.
- **Since:** `<11`

Deletes the clip contained in this slot. Raises an exception if called on an empty slot.

#### `duplicate_clip_to(target_slot: ClipSlot)`

- **Returns:** `None`
- **Args:** `target_slot: ClipSlot`
- **Raises:** Exception if this slot is empty; if source and target track types differ (audio vs MIDI); if
  source or target is a group slot.
- **Since:** `<11`

Duplicates this slot's clip to another slot. The target clip is replaced if non-empty. Raises
if the source is empty, if source and target have mismatched track types, or if either slot
is a group slot.

#### `fire(record_length=None, launch_quantization=None, force_legato=False)`

- **Returns:** `None`
- **Args:**
    - `record_length: float = 1.7976931348623157e+308` (effectively infinite; omit to record indefinitely)
    - `launch_quantization: int = -2147483648` (sentinel: use global quantization)
    - `force_legato: bool = False`
- **Raises:** Error if `record_length` is passed but the slot already owns a clip.
- **Since:** `<11`

The primary launch action for a slot. Behavior depends on slot state:

- If the slot has a clip: launches it.
- If the slot is empty and `has_stop_button=True`: triggers the stop button.
- If the slot is empty and the track is armed: starts recording.

`record_length` specifies the recording duration in beats, after which the clip will loop
back and play. Must not be provided if the slot already has a clip. `launch_quantization`
overrides the global quantization setting. `force_legato` causes the clip to start
immediately, moving the playhead to stay in sync.

#### `set_fire_button_state(state: bool)`

- **Returns:** `None`
- **Args:** `state: bool`
- **Since:** `<11`

Simulates pressing and holding the clip launch button. Supports all launch modes (e.g. Gate
mode clips sustain while state is `True`). Set to `False` to release.

#### `stop()`

- **Returns:** `None`
- **Since:** `<11`

Stops any actively playing or recording clip on this track. For group slots, stops clips in
all child tracks. The Max docs note that it does not matter which slot index on the track you
call this from -- the effect is track-wide.


### reference/tracks/Envelope.md

# Envelope

> `Live.Envelope.Envelope`

This class represents an automation or modulation envelope in Live. An envelope contains
breakpoint events that describe how a parameter value changes over time. Envelopes can be
queried for their events, edited by inserting steps or deleting event ranges, and sampled
at arbitrary time positions.

??? note "Raw probe notes (temporary)"
    - `canonical_parent` returns the parent `Clip` handle -- confirmed for session clip envelopes.
    - Time coordinates are in beats (relative to clip start). `insert_step(0.0, 1.0, 0.5)` on a
      4-beat clip created a step from beat 0 to beat 1; `value_at_time(0.5)` returned the inserted
      value `0.5`.
    - `value_at_time` on a fresh envelope (no events) returns the parameter's current value
      (e.g. 0.85 for volume at default).
    - `events_in_range` fails with `ValidationError: Unsupported return type: EnvelopeEvent` --
      EnvelopeEvent is a value object (like MidiNote/WarpMarker), not a handle-based object.
      Returns `[]` successfully when there are no events. Needs bridge-side serialization.
    - `delete_events_in_range` works; after deletion, `events_in_range` returns `[]`.
    - Both `events_in_range` and `delete_events_in_range` reject large `end` values with
      `ValidationError: Range out of bounds.` The max accepted value is approximately `1,576,800`
      beats (~4.5 hours at 120 BPM). `2,147,483,647.0` (max 32-bit int) fails. Values up to
      `1,000,000.0` work reliably.
    - `automation_envelope(param)` accepts a DeviceParameter handle directly. Returns `None` when
      no envelope exists for that parameter, or an Envelope handle when one does.
    - `create_automation_envelope(param)` returns an Envelope handle. Raises
      `InternalError: There is already an envelope for the parameter` if called twice.
    - `automation_envelopes` children list returns Envelope handles via standard `children()` call.
      Empty list when no envelopes exist.
    - `clear_envelope(param)` and `clear_all_envelopes()` both work. `has_envelopes` correctly
      reflects state transitions (False -> True after create, False after clear).
    - Envelope type name in the bridge is `"Envelope"`.

### Open Questions

- ~~Does `insert_step()` overwrite existing events in the step range, or does it merge?~~
  **Resolved:** partial overwrite. The new step overwrites only its range; non-overlapping
  portions of prior steps are preserved. Tested via `value_at_time` on overlapping regions.
- ~~Are the `EnvelopeEvent.control_coefficients` used for curve shaping between breakpoints?
  What do `x1`, `x2`, `y1`, `y2` represent -- Bezier control points?~~
  **Resolved:** Yes, cubic Bezier control points. `(x1, y1)` and `(x2, y2)` define the
  interpolation curve between this event and the next. Default `(0.5, 0.5, 0.5, 0.5)` =
  linear (straight line). Always present (never None). Non-default values only come from
  UI-drawn curves -- `insert_step` has no curve parameter.
- Envelope event values are in the parameter's native internal scale, not the 0-1 linear
  fader range. For volume: `insert_step(value=0.5)` -> event value ~= 0.1995 (dB-scale).
- Each flat step is represented as two events at the same time (discontinuity/jump).
  Boundary events with value 1.0 appear at envelope edges.

### Properties

| Property           | Type     | Settable | Listenable | Summary                                    |
| ------------------ | -------- | -------- | ---------- | ------------------------------------------ |
| `canonical_parent` | `object` | no       | `no`       | The parent object that owns this envelope. |

#### `canonical_parent`

- **Type:** `Clip`
- **Listenable:** `no`
- **Since:** `<11`

Returns the canonical parent of this envelope. For session clip envelopes, this is the parent
`Clip` object. Probing confirmed the returned handle has `type=Clip` and matches the clip OID.

### Methods

| Method                                                   | Returns               | Summary                                         |
| -------------------------------------------------------- | --------------------- | ----------------------------------------------- |
| `delete_events_in_range(start: float, end: float)`       | `None`                | Delete all envelope events within a time range. |
| `events_in_range(start: float, end: float)`              | `EnvelopeEventVector` | Return all envelope events within a time range. |
| `insert_step(start: float, length: float, value: float)` | `None`                | Insert a constant-value step into the envelope. |
| `value_at_time(time: float)`                             | `float`               | Return the parameter value at a specific time.  |

#### `delete_events_in_range(start: float, end: float)`

- **Returns:** `None`
- **Args:**
    - `start: float` -- the start time of the range (beats)
    - `end: float` -- the end time of the range (beats)
- **Raises:** `ValidationError: Range out of bounds.` when `end` exceeds ~1,576,800.
- **Since:** `12.2`

Deletes all envelope events that fall within the specified time range defined by `start`
and `end`. Times are in beats relative to clip start. Probing confirmed deletion works and
subsequent `events_in_range` returns `[]`. The `end` parameter has an upper bound of
approximately 1,576,800 beats; values beyond this (including `2,147,483,647.0`) are rejected.

#### `events_in_range(start: float, end: float)`

- **Returns:** `EnvelopeEventVector` (list of `EnvelopeEvent`)
- **Args:**
    - `start: float` -- the start time of the range (beats)
    - `end: float` -- the end time of the range (beats)
- **Raises:** `ValidationError: Range out of bounds.` when `end` exceeds ~1,576,800.
- **Since:** `12.2`

Returns a vector of `EnvelopeEvent` objects that fall within the specified time range.
Each event has a `time`, `value`, and `control_coefficients` property. Times are in beats
relative to clip start. Values are in the parameter's native internal scale (e.g. dB for
volume). Each flat step creates two events at the same time (a discontinuity). Boundary
events with value 1.0 appear at envelope edges. The `end` parameter has an upper bound of
approximately 1,576,800 beats (~4.5 hours at 120 BPM); values beyond this (including
`2,147,483,647.0`) are rejected with a validation error.

#### `insert_step(start: float, length: float, value: float)`

- **Returns:** `None`
- **Args:**
    - `start: float` -- the start time of the step (beats)
    - `length: float` -- the duration of the step (beats)
    - `value: float` -- the parameter value for the step
- **Since:** `12.2`

Creates a step (flat segment) in the envelope starting at `start`, lasting for `length`,
at the given `value`. Times are in beats relative to clip start. Probing confirmed:
`insert_step(0.0, 1.0, 0.5)` followed by `value_at_time(0.5)` returned `0.5`.

#### `value_at_time(time: float)`

- **Returns:** `float`
- **Args:**
    - `time: float` -- the time position to sample (beats)
- **Since:** `12.2`

Returns the interpolated parameter value of the envelope at the specified time position.
Time is in beats relative to clip start. On a fresh envelope with no events, returns the
parameter's current value (e.g. `0.85` for volume at default). After `insert_step(0.0, 1.0, 0.5)`,
`value_at_time(0.5)` returns `0.5`.

---

## EnvelopeEvent

> `Live.Envelope.EnvelopeEvent`

This class represents a single breakpoint event within an envelope. Each event has a time
position, a value, and control coefficients that define the cubic Bezier curve shape between
this event and the next.

??? note "Raw probe notes (temporary)"
    EnvelopeEvent is a value object (not handle-based), serialized by the bridge following the
    MidiNote/WarpMarker pattern. Probed via `events_in_range` after bridge serialization was added.

    - `control_coefficients` is always present (never None). Default `(0.5, 0.5, 0.5, 0.5)` =
      linear interpolation. Non-default values only come from UI-drawn automation curves.
    - `time` is in beats relative to clip start.
    - `value` is in the parameter's native internal scale (e.g. dB for volume, not 0-1 linear).
    - Each flat step creates two events at the same time (a discontinuity/jump).
    - Boundary events with value 1.0 appear at the start and end of the envelope range.

### Properties

| Property               | Type                               | Settable | Listenable | Summary                                       |
| ---------------------- | ---------------------------------- | -------- | ---------- | --------------------------------------------- |
| `control_coefficients` | `EnvelopeEventControlCoefficients` | no       | `no`       | Curve-shaping coefficients for this event.    |
| `time`                 | `float`                            | no       | `no`       | The time position of this breakpoint (beats). |
| `value`                | `float`                            | no       | `no`       | The parameter value at this breakpoint.       |

#### `control_coefficients`

- **Type:** `EnvelopeEventControlCoefficients`
- **Listenable:** `no`
- **Since:** `12.2`

Cubic Bezier control points defining the interpolation curve between this event and the next.
`(x1, y1)` is the first control point, `(x2, y2)` is the second. Default `(0.5, 0.5, 0.5, 0.5)`
= linear (straight line). Always present (never None). Non-default values only appear from
UI-drawn automation curves -- the `insert_step` API produces flat steps with default coefficients.

#### `time`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

The time position of this breakpoint event in beats relative to clip start. Flat steps
create two events at the same time to represent the value discontinuity (jump).

#### `value`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

The parameter value at this breakpoint, in the parameter's native internal scale. For volume
this is a logarithmic (dB) scale, not 0-1 linear. Boundary events use value 1.0.

---

## EnvelopeEventControlCoefficients

> `Live.Envelope.EnvelopeEventControlCoefficients`

This class represents the cubic Bezier control points of an envelope event, defining the
interpolation curve shape between consecutive breakpoints.

??? note "Raw probe notes (temporary)"
    Probed via `events_in_range` after bridge serialization. All API-created steps produce
    the default `(0.5, 0.5, 0.5, 0.5)` (linear interpolation). The values represent two
    Bezier control points `(x1, y1)` and `(x2, y2)` normalized to the segment between
    consecutive events. Non-default values (curved automation) only appear from UI-drawn
    breakpoints.

### Properties

| Property | Type    | Settable | Listenable | Summary                            |
| -------- | ------- | -------- | ---------- | ---------------------------------- |
| `x1`     | `float` | no       | `no`       | First x-axis control coefficient.  |
| `x2`     | `float` | no       | `no`       | Second x-axis control coefficient. |
| `y1`     | `float` | no       | `no`       | First y-axis control coefficient.  |
| `y2`     | `float` | no       | `no`       | Second y-axis control coefficient. |

#### `x1`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

First Bezier control point x-coordinate. Together with `y1`, defines the departure tangent
from this event toward the next. Default 0.5 = linear interpolation.

#### `x2`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

Second Bezier control point x-coordinate. Together with `y2`, defines the arrival tangent
approaching the next event. Default 0.5 = linear interpolation.

#### `y1`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

First Bezier control point y-coordinate. Together with `x1`, defines the departure tangent
from this event toward the next. Default 0.5 = linear interpolation.

#### `y2`

- **Type:** `float`
- **Listenable:** `no`
- **Since:** `12.2`

Second Bezier control point y-coordinate. Together with `x2`, defines the arrival tangent
approaching the next event. Default 0.5 = linear interpolation.


### reference/tracks/MixerDevice.md

# MixerDevice

> `Live.MixerDevice.MixerDevice`

This class represents a track's mixer device in Live, providing access to volume, panning,
sends, and other mixer-related parameters. Every track has a mixer device. The master track's
mixer device additionally exposes the crossfader, cue volume, and song tempo parameters.

All mixer parameters are exposed as `DeviceParameter` objects, which means they can be
automated, MIDI-mapped, and modified via the API.

??? note "Raw probe notes (temporary)"
    - **Master-only children raise on regular tracks:**
        - `crossfader` -> `InternalError: "Only the main track has a crossfader!"`
        - `cue_volume` -> `InternalError: "Cue volume available on the main track only!"`
        - `song_tempo` -> `InternalError: "Only the main track has the song tempo!"`
    - **`crossfade_assign` raises on master:** `InternalError: "Main track has no crossfader assignment!"`
    - **`panning_mode` IS settable:** set to `1` (Split Stereo), readback=`1`. Confirmed writable.
    - **Master track has 0 sends** -- `sends` returns an empty list on the master track.

### Open Questions

None -- all key questions resolved by probing.

### Children

| Child                | Returns                     | Shape    | Listenable | Summary                                             |
| -------------------- | --------------------------- | -------- | ---------- | --------------------------------------------------- |
| `crossfader`         | `DeviceParameter`           | `single` | `no`       | Crossfader parameter. Master track only.            |
| `cue_volume`         | `DeviceParameter`           | `single` | `no`       | Cue/preview volume. Master track only.              |
| `left_split_stereo`  | `DeviceParameter`           | `single` | `no`       | Left split stereo pan parameter.                    |
| `panning`            | `DeviceParameter`           | `single` | `no`       | Pan parameter.                                      |
| `right_split_stereo` | `DeviceParameter`           | `single` | `no`       | Right split stereo pan parameter.                   |
| `sends`              | `Sequence[DeviceParameter]` | `list`   | `yes`      | Send amount parameters, one per return track.       |
| `song_tempo`         | `DeviceParameter`           | `single` | `no`       | Song tempo as a DeviceParameter. Master track only. |
| `track_activator`    | `DeviceParameter`           | `single` | `no`       | Track on/off toggle parameter.                      |
| `volume`             | `DeviceParameter`           | `single` | `no`       | Volume parameter.                                   |

#### `crossfader`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The crossfader parameter. Only available on the master track's mixer device. Controls the
A/B crossfade position. Accessing on a non-master track raises
`InternalError: "Only the main track has a crossfader!"`.

#### `cue_volume`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The cue (preview/solo) volume parameter. Only available on the master track's mixer device.
Accessing on a non-master track raises
`InternalError: "Cue volume available on the main track only!"`.

#### `left_split_stereo`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The left channel's pan parameter when the track is in split stereo panning mode
(`panning_mode=1`). In standard stereo mode (`panning_mode=0`), this parameter exists but
is not active.

#### `panning`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The track's panning parameter. In standard stereo mode, this controls the stereo position.
In split stereo mode, this parameter exists but may not be the active control -- use
`left_split_stereo` and `right_split_stereo` instead.

#### `right_split_stereo`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The right channel's pan parameter when the track is in split stereo panning mode
(`panning_mode=1`). In standard stereo mode (`panning_mode=0`), this parameter exists but
is not active.

#### `sends`

- **Type:** `Sequence[DeviceParameter]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of send amount parameters, one per return track. The order matches
`Song.return_tracks`. The listener fires when return tracks are added or removed (changing
the send count). The master track's sends list is always empty.

#### `song_tempo`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The song's tempo exposed as a `DeviceParameter` on the master track's mixer. This allows
the tempo to be automated via the same parameter mechanism as other mixer controls. Accessing
on a non-master track raises `InternalError: "Only the main track has the song tempo!"`.

#### `track_activator`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The track's on/off toggle (activator) as a `DeviceParameter`. This is the same toggle
controlled by the track's mute state, exposed here for automation and mapping.

#### `volume`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The track's volume fader as a `DeviceParameter`.

### Properties

| Property           | Type  | Settable | Listenable | Summary                                                   |
| ------------------ | ----- | -------- | ---------- | --------------------------------------------------------- |
| `crossfade_assign` | `int` | `int`    | `yes`      | Crossfade assignment: 0=A, 1=none, 2=B. Raises on master. |
| `panning_mode`     | `int` | `int`    | `yes`      | Panning mode: 0=Stereo, 1=Split Stereo. Settable.         |

#### `crossfade_assign`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The track's crossfade assignment:

- `0` = A (assigned to crossfader side A)
- `1` = none (not crossfade-assigned)
- `2` = B (assigned to crossfader side B)

Accessing on the master track raises
`InternalError: "Main track has no crossfader assignment!"`.

#### `panning_mode`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The track's panning mode:

- `0` = Stereo -- standard single-knob panning
- `1` = Split Stereo -- separate left/right pan controls via `left_split_stereo` and
  `right_split_stereo`

Settable. Setting `panning_mode=1` switches the track to split stereo panning.

