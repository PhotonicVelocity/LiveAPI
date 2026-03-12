# Future

## Object args and returns

### Genuinely object — no change needed

- Live.Base.ObjectVector.append (arg2: object)
- Live.Base.ObjectVector.extend (arg2: object)

### Change to specific type

- Live.Clip.Clip.add_new_notes (arg2: object → list[MidiNoteSpecification])
  desc: Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification objects. The objects will be used to construct new notes in the clip.
- Live.Clip.Clip.add_warp_marker (warp_marker: object → WarpMarker)
  desc: Available for AudioClips only. Adds the specified warp marker, if possible.
- Live.Clip.Clip.duplicate_notes_by_id (note_ids: object → list[int], destination_time: object → float)
  desc: Duplicate all notes matching the given note IDs. If the optional destination_time is not provided, new notes will be inserted after the last selected note.
- Live.Clip.Clip.get_notes_by_id (note_ids: object → list[int])
  desc: Return a list of MIDI notes matching the given note IDs.
- Live.Clip.Clip.remove_notes_by_id (arg2: object → list[int])
  desc: Delete all notes matching the given note IDs.
- Live.Clip.Clip.select_notes_by_id (arg2: object → list[int])
  desc: Selects all notes matching the given note IDs.
- Live.Song.Song.create_audio_track (Index: object → int)
  desc: Create a new audio track at the optional given index and return it.
- Live.Song.Song.create_midi_track (Index: object → int)
  desc: Create a new midi track at the optional given index and return it.

### Change to Callable

- Live.Licensing.PythonLicensingBridge.get_startup_dialog (authorize_callable: object → Callable, authorize_later_callable: object → Callable)
  desc: Retrieves an instance of the startup dialog with the passed callables connected to its buttons.
- Live.Licensing.PythonLicensingBridge.set_network_timer (callback: object → Callable)
  desc: Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer.

### Change to Any

- Live.Song.Song.get_data (default_value: object → Any, return: object → Any)
  desc: Get data for the given key, that was previously stored using set_data.
- Live.Song.Song.set_data (value: object → Any)
  desc: Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.
- Live.Track.Track.get_data (default_value: object → Any, return: object → Any)
  desc: Get data for the given key, that was previously stored using set_data.
- Live.Track.Track.set_data (value: object → Any)
  desc: Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.

## Unnamed args (argX)

### 1. Vector append/extend — rename arg2 → value

All vector classes use `arg2` for the element param. Use `value` as this is standard for Python list method signature.

- Live.Application.ControlDescriptionVector.append/extend (arg2 -> value: ControlDescription)
- Live.Application.UnavailableFeatureVector.append/extend (arg2 -> value: UnavailableFeature)
- Live.Base.FloatVector.append/extend (arg2 -> value: float)
- Live.Base.IntU64Vector.append/extend (arg2 -> value: int)
- Live.Base.IntVector.append/extend (arg2 -> value: int)
- Live.Base.ObjectVector.append/extend (arg2 -> value: object)
- Live.Base.StringVector.append/extend (arg2 -> value: str)
- Live.Base.Vector.append/extend (arg2 -> value: LomObject)
- Live.Browser.BrowserItemVector.append/extend (arg2 -> value: BrowserItem)
- Live.Clip.MidiNoteVector.append/extend (arg2 -> value: MidiNote)
- Live.Clip.WarpMarkerVector.append/extend (arg2 -> value: WarpMarker)
- Live.Device.ATimeableValueVector.append/extend (arg2 -> value: DeviceParameter)
- Live.Envelope.EnvelopeEventVector.append/extend (arg2 -> value: EnvelopeEvent)
- Live.Listener.ListenerVector.append/extend (arg2 -> value: ListenerHandle)
- Live.Track.RoutingChannelVector.append/extend (arg2 -> value: RoutingChannel)
- Live.Track.RoutingTypeVector.append/extend (arg2 -> value: RoutingType)

### 2. Module-level functions — args start at arg1 (no self)

- Live.Application.encrypt_challenge2 (arg1 -> challenge: int)
  desc: Returns the UMAC hash for the given challenge.
- Live.Application.get_random_int (arg1 -> start: int, arg2 -> stop: int)
  desc: Returns a random integer from the given range.
- Live.Base.log (arg1: str)
- Live.Base.subst_args (arg1: str, arg2: str, arg3: str, arg4: str, arg5: str)
- Live.MidiMap.forward_midi_cc (arg1: int, arg2: int, arg3: int, arg4: int)
- Live.MidiMap.forward_midi_note (arg1: int, arg2: int, arg3: int, arg4: int)
- Live.MidiMap.forward_midi_pitchbend (arg1: int, arg2: int, arg3: int)
- Live.MidiMap.map_midi_note (arg1: int, arg2: DeviceParameter, arg3: int, arg4: int)
- Live.MidiMap.map_midi_note_with_feedback_map (arg1: int, arg2: DeviceParameter, arg3: int, arg4: int, arg5: NoteFeedbackRule)
- Live.MidiMap.map_midi_pitchbend (arg1: int, arg2: DeviceParameter, arg3: int, arg4: bool)
- Live.MidiMap.map_midi_pitchbend_with_feedback_map (arg1: int, arg2: DeviceParameter, arg3: int, arg4: PitchBendFeedbackRule, arg5: bool)
- Live.MidiMap.send_feedback_for_parameter (arg1: int, arg2: DeviceParameter)

### 3. Application.View identifier methods — rename arg2 → identifier

All Application "view" related methods take an identifier string. Use `identifier` for clarity.

- Live.Application.Application.View.focus_view (arg2 -> identifier: str)
  desc: Show and focus one through the identifier string specified view.
- Live.Application.Application.View.hide_view (arg2 -> identifier: str)
  desc: Hide one through the identifier string specified view.
- Live.Application.Application.View.show_view (arg2 -> identifier: str)
  desc: Show one through the identifier string specified view. Will throw a runtime error if this is called in Live's initialization scope.
- Live.Application.Application.View.add_is_view_visible_listener (arg2 -> identifier: str)
  desc: Add a listener function or method, which will be called as soon as the property "is_view_visible" has changed.
- Live.Application.Application.View.is_view_visible_has_listener (arg2 -> identifier: str)
  desc: Returns true, if the given listener function or method is connected to the property "is_view_visible".
- Live.Application.Application.View.remove_is_view_visible_listener (arg2 -> identifier: str)
  desc: Remove a previously set listener function or method from property "is_view_visible".
- Live.Application.Application.View.scroll_view (arg2: int, arg3 -> identifier: str, arg4: bool)
  desc: Scroll through the identifier string specified view into the given direction, if possible. Will silently return if the specified view can not perform the requested action.
- Live.Application.Application.View.zoom_view (arg2: int, arg3 -> identifier: str, arg4: bool)
  desc: Zoom through the identifier string specified view into the given direction, if possible. Will silently return if the specified view can not perform the requested action.

### 4. set_fire_button_state — rename arg2 → state

Fire button state methods take a boolean for the new state. Use `state` for clarity.

- Live.Clip.Clip.set_fire_button_state (arg2 -> state: bool)
  desc: Set the clip's fire button state directly. Supports all launch modes.
- Live.ClipSlot.ClipSlot.set_fire_button_state (arg2 -> state: bool)
  desc: Set the clipslot's fire button state directly. Supports all launch modes.
- Live.Scene.Scene.set_fire_button_state (arg2 -> state: bool)
  desc: Set the scene's fire button state directly. Supports all launch modes.

### 5. Index-based operations — rename arg2 → index

Index-based methods take an integer index for the item to operate on. Use `index` for clarity.

- Live.Chain.Chain.delete_device (arg2 -> index: int)
  desc: Remove a device identified by its index from the chain. Throws runtime error if bad index.
- Live.Chain.Chain.duplicate_device (arg2 -> index: int)
  desc: Duplicate the device at the given index in the chain.
- Live.Song.Song.create_scene (arg2 -> index: int)
  desc: Create a new scene at the given index. If the index is -1, the new scene is added at the end. If the index is invalid or the new scene would exceed the limitations, a limitation error is raised.
- Live.Song.Song.delete_return_track (arg2 -> index: int)
  desc: Delete the return track with the given index. If no track with this index exists, an exception will be raised.
- Live.Song.Song.delete_scene (arg2 -> index: int)
  desc: Delete the scene with the given index. If no scene with this index exists, an exception will be raised.
- Live.Song.Song.delete_track (arg2 -> index: int)
  desc: Delete the track with the given index. If no track with this index exists, an exception will be raised.
- Live.Song.Song.duplicate_scene (arg2 -> index: int)
  desc: Duplicates a scene and selects the new one. Raises a limitation error if creating a new scene would exceed the limitations.
- Live.Song.Song.duplicate_track (arg2 -> index: int)
  desc: Duplicates a track and selects the new one. If the track is inside a folded group track, the group track is unfolded. Raises a limitation error if creating a new track would exceed the limitations.
- Live.Track.Track.delete_device (arg2 -> index: int)
  desc: Delete a device identified by the index in the 'devices' list.
- Live.Track.Track.duplicate_clip_slot (arg2 -> index: int)
  desc: Duplicate a clip and put it into the next free slot and return the index of the destination slot. A new scene is created if no free slot is available. If creating the new scene would exceed the limitations, a runtime error is raised.
- Live.Track.Track.duplicate_device (arg2 -> index: int)
  desc: Duplicate a device at a given index in the 'devices' list.
- Live.Application.Application.press_current_dialog_button (arg2 -> index: int)
  desc: Press a button, by index, on the current message box.
- Live.MaxDevice.MaxDevice.get_bank_name (arg2 -> index: int)
  desc: Get the name of a parameter bank given by index. This is related to hardware control surfaces.
- Live.MaxDevice.MaxDevice.get_bank_parameters (arg2 -> index: int)
  desc: Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces.

### 6. Clip note operations

- Live.Clip.Clip.add_new_notes (arg2: object)
  desc: Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification objects. The objects will be used to construct new notes in the clip.
- Live.Clip.Clip.remove_notes_by_id (arg2: object)
  desc: Delete all notes matching the given note IDs. This function should NOT be used to implement modification of existing notes (i.e. in combination with add_new_notes), as that leads to loss of per-note events. apply_note_modifications must be used instead for modifying existing notes.
- Live.Clip.Clip.select_notes_by_id (arg2: object)
  desc: Selects all notes matching the given note IDs.
- Live.Clip.Clip.apply_note_modifications (arg2: MidiNoteVector)
  desc: Expects a list of notes as returned from get_notes_extended. The content of the list will be used to modify existing notes in the clip, based on matching note IDs. This function should be used when modifying existing notes, e.g. changing the velocity or start time. The function ensures that per-note events attached to the modified notes are preserved. This is NOT the case when replacing notes via a combination of remove_notes_extended and add_new_notes. The given list can be a subset of the notes in the clip, but it must not contain any notes that are not present in the clip.
- Live.Clip.Clip.replace_selected_notes (arg2: tuple)
  desc: Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_selected_notes. The notes described that way will then be used to replace the old selection.
- Live.Clip.Clip.set_notes (arg2: tuple)
  desc: Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_notes. The notes described that way will then be added to the clip.
- Live.Clip.Clip.remove_notes (arg2: float, arg3: int, arg4: float, arg5: int)
- Live.Clip.Clip.quantize (arg2: int, arg3: float)
  desc: Quantize all notes in a clip or align warp markers.
- Live.Clip.Clip.quantize_pitch (arg2: int, arg3: int, arg4: float)
  desc: Quantize all the notes of a given pitch. Raises an error on audio clips.

### 7. Other methods

- Live.Application.Application.has_option (arg2 -> option: str)
  desc: Returns True if the given entry exists in Options.txt, False otherwise.
- Live.Song.Song.get_current_smpte_song_time (arg2 -> format: int -> SmpteFormat)
  desc: Get const access to the songs current playing position, by specifying the SMPTE format in which you would like to receive the time.
- Live.Application.ControlSurfaceProxy.enable_receive_midi (arg2: bool)
- Live.Application.ControlSurfaceProxy.grab_control (arg2: int)
- Live.Application.ControlSurfaceProxy.release_control (arg2: int)
- Live.Application.ControlSurfaceProxy.send_midi (arg2: tuple)
- Live.Application.ControlSurfaceProxy.send_value (arg2: tuple)
- Live.Application.ControlSurfaceProxy.subscribe_to_control (arg2: int)
- Live.Application.ControlSurfaceProxy.unsubscribe_from_control (arg2: int)
- Live.Browser.Browser.load_item (arg2: BrowserItem)
  desc: Loads the provided browser item.
- Live.Browser.Browser.preview_item (arg2: BrowserItem)
  desc: Previews the provided browser item.
- Live.Browser.Browser.relation_to_hotswap_target (arg2: BrowserItem)
  desc: Returns the relation between the given browser item and the current hotswap target
- Live.Clip.Clip.View.select_envelope_parameter (arg2: DeviceParameter)
  desc: Select the given device parameter in the envelope view.
- Live.Clip.Clip.automation_envelope (arg2: DeviceParameter)
  desc: Return the envelope for the given parameter. Returns None if the envelope doesn't exist. Returns None for Arrangement clips. Returns None for parameters from a different track.
- Live.Clip.Clip.clear_envelope (arg2: DeviceParameter)
  desc: Clears the envelope of this clips given parameter.
- Live.Clip.Clip.create_automation_envelope (arg2: DeviceParameter)
  desc: Creates an envelope for a given parameter and returns it. This should only be used if the envelope doesn't exist. Raises an error if the envelope can't be created.
- Live.Clip.Clip.move_playing_pos (arg2: float)
  desc: Jump forward or backward by the specified relative amount in beats. Will do nothing, if the Clip is not playing.
- Live.ClipSlot.ClipSlot.create_audio_clip (arg2: str)
  desc: Creates an audio clip referencing the file at the given absolute path in the slot. Throws an error when called on non-empty slots or slots in non-audio or frozen tracks, or when the path doesn't point at a valid audio file.
- Live.ClipSlot.ClipSlot.create_clip (arg2: float)
  desc: Creates an empty clip with the given length in the slot. Throws an error when called on non-empty slots or slots in non-MIDI tracks.
- Live.ClipSlot.ClipSlot.duplicate_clip_to (arg2: ClipSlot)
  desc: Duplicates the slot's clip to the passed in target slot. Overrides the target's clip if it's not empty. Raises an exception if the (source) slot itself is empty, or if source and target have different track types (audio vs. MIDI). Also raises if the source or target slot is in a group track (so called group slot).
- Live.Device.Device.store_chosen_bank (arg2: int, arg3: int)
  desc: Set the selected bank in the device for persistency.
- Live.DeviceParameter.DeviceParameter.str_for_value (arg2: float)
  desc: Return a string representation of the given value. To be used for display purposes only. This value can include characters like 'db' or 'hz', depending on the type of the parameter.
- Live.Envelope.Envelope.delete_events_in_range (arg2: float, arg3: float)
  desc: Deletes the events in the specified time range.
- Live.Envelope.Envelope.events_in_range (arg2: float, arg3: float)
  desc: Returns the events in the specified time range.
- Live.Envelope.Envelope.insert_step (arg2: float, arg3: float, arg4: float)
  desc: Given a start time, a step length and a value, creates a step in the envelope.
- Live.Envelope.Envelope.value_at_time (arg2: float)
  desc: Returns the parameter value at the specified time.
- Live.LooperDevice.LooperDevice.export_to_clip_slot (arg2: ClipSlot)
  desc: Export Looper's content to a Session Clip Slot.
- Live.MaxDevice.MaxDevice.get_value_item_icons (arg2: DeviceParameter)
  desc: Get a list of icon identifier strings for a list parameter's values. An empty string is given where no icon should be displayed. An empty list is given when no icons should be displayed. This is related to hardware control surfaces.
- Live.RackDevice.RackDevice.copy_pad (arg2: int, arg3: int)
  desc: Copies all contents of a drum pad from a source pad into a destination pad. copy_pad(source_index, destination_index) where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack. Throws an exception when the source pad is empty, or when the source or destination indices are not between 0 - 127.
- Live.Song.Song.View.select_device (arg2: Device)
  desc: Select the given device.
- Live.Song.Song.jump_by (arg2: float)
  desc: Set a new playing pos, relative to the current one.
- Live.Song.Song.scrub_by (arg2: float)
  desc: Same as jump_by, but does not stop playback.
- Live.TakeLane.TakeLane.create_audio_clip (arg2: str, arg3: float)
  desc: Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time. Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.
- Live.TakeLane.TakeLane.create_midi_clip (arg2: float, arg3: float)
  desc: Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.
- Live.Track.Track.create_audio_clip (arg2: str, arg3: float)
  desc: Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time. Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.
- Live.Track.Track.create_midi_clip (arg2: float, arg3: float)
  desc: Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.
- Live.Track.Track.delete_clip (arg2: Clip)
  desc: Delete the given clip. Raises a runtime error when the clip belongs to another track.
- Live.Track.Track.jump_in_running_session_clip (arg2: float)
  desc: Jump forward or backward in the currently running Sessionclip (if any) by the specified relative amount in beats. Does nothing if no Session Clip is currently running.
