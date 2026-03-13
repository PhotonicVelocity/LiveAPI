## Unresolved Items

```json
{
  "Live.Track.Track.create_audio_clip": {
    "description": "Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.",
    "signature": "create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs_name": true
      },
      "arg3": {
        "current_type": "float",
        "needs_name": true
      }
    }
  },
  "Live.Track.Track.create_midi_clip": {
    "description": "Creates an empty MIDI clip and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.",
    "signature": "create_midi_clip( (Track)arg1, (float)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_midi_clip(TTrackPyHandle,double,double)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs_name": true
      },
      "arg3": {
        "current_type": "float",
        "needs_name": true
      }
    }
  },
  "Live.Track.Track.duplicate_clip_slot": {
    "description": "Duplicate a clip and put it into the next free slot and return the index\nof the destination slot. A new scene is created if no free slot is\navailable. If creating the new scene would exceed the limitations,\na runtime error is raised.",
    "signature": "duplicate_clip_slot( (Track)arg1, (int)arg2) -> int :",
    "cpp_signature": "int duplicate_clip_slot(TTrackPyHandle,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Track.Track.duplicate_device": {
    "description": "Duplicate a device at a given index in the 'devices' list.",
    "signature": "duplicate_device( (Track)arg1, (int)arg2) -> None :",
    "cpp_signature": "void duplicate_device(TTrackPyHandle,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Track.Track.get_data": {
    "description": "Get data for the given key, that was previously stored using set_data.",
    "signature": "get_data( (Track)arg1, (object)key, (object)default_value) -> object :",
    "cpp_signature": "boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object)",
    "args": {
      "default_value": {
        "current_type": "object"
      }
    },
    "returns": {
      "current_type": "object"
    }
  },
  "Live.Track.Track.jump_in_running_session_clip": {
    "description": "Jump forward or backward in the currently running Sessionclip (if any)\nby the specified relative amount in beats. Does nothing if no Session Clip\nis currently running.",
    "signature": "jump_in_running_session_clip( (Track)arg1, (float)arg2) -> None :",
    "cpp_signature": "void jump_in_running_session_clip(TTrackPyHandle,double)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs_name": true
      }
    }
  },
  "Live.Track.Track.set_data": {
    "description": "Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.",
    "signature": "set_data( (Track)arg1, (object)key, (object)value) -> None :",
    "cpp_signature": "void set_data(TTrackPyHandle,TString,boost::python::api::object)",
    "args": {
      "value": {
        "current_type": "object"
      }
    }
  }
}
```

## Decompiled Remote Scripts Evidence

These hints were extracted from Ableton's decompiled Remote Scripts (1200+ Python files that call the Live API). Use them as additional evidence when resolving names and types.

### Call-Site Arg Name Hints

Variable names observed at call sites for each arg position, sorted by frequency. These are the names callers used when passing values — suggestive but not definitive.

```json
{
  "Live.Track.Track.duplicate_clip_slot": {
    "args": {
      "arg2": {
        "call_site_names": [
          "index",
          "target_index",
          "source_index",
          "slot_index"
        ],
        "_votes": {
          "index": 3,
          "target_index": 2,
          "source_index": 1,
          "slot_index": 1
        },
        "_total_sites": 7
      }
    }
  }
}
```

### Type Usage Context

Code snippets showing how members with unresolved types are used in practice. Use these to infer types from usage patterns (e.g. compared to strings → str, iterated → sequence, etc.).

```json
{
  "Live.Track.Track.get_data": {
    "usage_snippets": [
      "if self.song.view.selected_track.get_data(\"alternative_mode_locked\", False) and alternative_mode:",
      "return bool(self.song.view.selected_track.get_data(\"alternative_mode_locked\", False))",
      "return self.song.view.selected_track.get_data(\"push-note-repeat-enabled\", False)",
      "return self.song.view.selected_track.get_data(\"push-note-repeat-rate\", DEFAULT_RATE)",
      "saved_mode = track.get_data(\"push-selected-note-mode\", None)",
      "self._interval = self._song.get_data(\"push-note-layout-interval\", 3)",
      "self._is_horizontal = self._song.get_data(\"push-note-layout-horizontal\", True)",
      "self._tuning_system_interval = self._song.get_data(\"push-note-layout-tuning-system-interval\", 5)",
      "self.selected_notes_provider.selected_notes = self.song.view.selected_track.get_data(\"push-instrument-selected-notes\", [DEFAULT_START_NOTE])"
    ],
    "unresolved_arg_types": {
      "default_value": "object"
    },
    "unresolved_return_type": "object"
  },
  "Live.Track.Track.set_data": {
    "usage_snippets": [
      "self._song.set_data(\"push-note-layout-horizontal\", is_horizontal)",
      "self._song.set_data(\"push-note-layout-interval\", interval)",
      "self._song.set_data(\"push-note-layout-tuning-system-interval\", interval)",
      "self.song.view.selected_track.set_data(\"alternative_mode_locked\", False)",
      "self.song.view.selected_track.set_data(\"alternative_mode_locked\", True)",
      "self.song.view.selected_track.set_data(\"push-instrument-selected-notes\", self.selected_notes_provider.selected_notes)",
      "self.song.view.selected_track.set_data(\"push-note-repeat-enabled\", is_enabled)",
      "self.song.view.selected_track.set_data(\"push-note-repeat-rate\", NOTE_REPEAT_RATES[option])",
      "self.song.view.selected_track.set_data(\"push-selected-note-mode\", mode)",
      "track.set_data(\"push-selected-note-mode\", \"sequencer_loop\")"
    ],
    "unresolved_arg_types": {
      "value": "object"
    }
  }
}
```

## API Type Skeleton

This is the complete type hierarchy of the Live API — all modules, classes, enums (with values), and properties (with types where known). Use it to identify valid type names and understand class/module relationships.

Format: containers end with `:` and have indented children, properties use `name -> Type`, enums use `Name = val1, val2, ...`, string constants use `name = 'value'`, exceptions use `!Name`.

```
Live:
	Application:
		Application:
			View:
				NavDirection = up, down, left, right
				canonical_parent -> Application
			browser -> Browser
			control_surfaces -> ObjectVector
			unavailable_features -> UnavailableFeatureVector
			view -> View
		ControlDescription:
		ControlDescriptionVector:
		ControlSurfaceProxy:
			control_descriptions
			pad_layout
			type_name
		MessageButtons = OK_BUTTON, OK_NEW_SET_BUTTON, OK_RETRY_BUTTON, SAVE_DONT_SAVE_BUTTON, OK_ACCOUNT_BUTTON, OK_PURCHASE_BUTTON
		PushDialogType = MESSAGE_BOX, OUT_OF_UNLOCKS_DIALOG, RENT_TO_OWN_LICENSE_EXPIRED_DIALOG
		UnavailableFeature = note_velocity_ranges_and_probabilities
		UnavailableFeatureVector:
		Variants:
			BETA = "'Beta'"
			INTRO = "'Intro'"
			LITE = "'Lite'"
			STANDARD = "'Standard'"
			SUITE = "'Suite'"
			TRIAL = "'Trial'"
	Base:
		FloatVector:
		IntU64Vector:
		IntVector:
		!LimitationError
		ObjectVector:
		StringVector:
		Text:
			text
		Timer:
		Vector:
	Browser:
		Browser:
			audio_effects -> BrowserItem
			clips -> BrowserItem
			colors -> BrowserItemVector
			current_project -> BrowserItem
			drums -> BrowserItem
			instruments -> BrowserItem
			legacy_libraries -> BrowserItemVector
			max_for_live -> BrowserItem
			midi_effects -> BrowserItem
			packs -> BrowserItem
			plugins -> BrowserItem
			samples -> BrowserItem
			sounds -> BrowserItem
			user_folders -> BrowserItemVector
			user_library -> BrowserItem
		BrowserItem:
			children -> BrowserItemVector
			iter_children -> BrowserItemIterator
		BrowserItemIterator
		BrowserItemVector:
		FilterType = disabled, hotswap_off, instrument_hotswap, audio_effect_hotswap, midi_effect_hotswap, drum_pad_hotswap, midi_track_devices, samples, count
		Relation = ancestor, equal, descendant, none
	CcControlDevice:
		CcControlDevice:
			View
			canonical_parent -> Track
			custom_bool_target_list -> StringVector
			custom_float_target_0_list -> StringVector
			custom_float_target_10_list -> StringVector
			custom_float_target_11_list -> StringVector
			custom_float_target_1_list -> StringVector
			custom_float_target_2_list -> StringVector
			custom_float_target_3_list -> StringVector
			custom_float_target_4_list -> StringVector
			custom_float_target_5_list -> StringVector
			custom_float_target_6_list -> StringVector
			custom_float_target_7_list -> StringVector
			custom_float_target_8_list -> StringVector
			custom_float_target_9_list -> StringVector
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
	Chain:
		Chain:
			canonical_parent -> RackDevice
			devices -> Vector
			mixer_device -> ChainMixerDevice
	ChainMixerDevice:
		ChainMixerDevice:
			canonical_parent -> Chain
			chain_activator -> DeviceParameter
			panning -> DeviceParameter
			sends -> Vector
			volume -> DeviceParameter
	Clip:
		Clip:
			View:
				canonical_parent -> Clip
				grid_quantization -> GridQuantization
			automation_envelopes -> Vector
			available_warp_modes -> IntVector
			canonical_parent -> ClipSlot
			view -> View
			warp_markers -> WarpMarkerVector
		ClipLaunchQuantization = q_global, q_none, q_8_bars, q_4_bars, q_2_bars, q_bar, q_half, q_half_triplet, q_quarter, q_quarter_triplet, q_eighth, q_eighth_triplet, q_sixteenth, q_sixteenth_triplet, q_thirtysecond
		GridQuantization = no_grid, g_8_bars, g_4_bars, g_2_bars, g_bar, g_half, g_quarter, g_eighth, g_sixteenth, g_thirtysecond, count
		LaunchMode = trigger, gate, toggle, repeat
		MidiNote:
		MidiNoteSpecification
		MidiNoteVector:
		WarpMarker:
		WarpMarkerVector:
		WarpMode = beats, complex, complex_pro, repitch, rex, texture, tones, count
	ClipSlot:
		ClipSlot:
			canonical_parent -> Track
			clip -> Clip
			playing_status -> ClipSlotPlayingState
		ClipSlotPlayingState = stopped, started, recording
	CompressorDevice:
		CompressorDevice:
			View
			available_input_routing_channels -> RoutingChannelVector
			available_input_routing_types -> RoutingTypeVector
			canonical_parent -> Track
			input_routing_channel -> RoutingChannel
			input_routing_type -> RoutingType
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
	Conversions:
		AudioToMidiType = harmony_to_midi, melody_to_midi, drums_to_midi
	Device:
		ATimeableValueVector:
		Device:
			View:
				canonical_parent -> Device
			canonical_parent -> Track
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
		DeviceType = undefined, instrument, audio_effect, midi_effect
	DeviceIO:
		DeviceIO:
			available_routing_channels -> RoutingChannelVector
			available_routing_types -> RoutingTypeVector
			canonical_parent -> MaxDevice
			routing_channel -> RoutingChannel
			routing_type -> RoutingType
	DeviceParameter:
		AutomationState = none, playing, overridden
		DeviceParameter:
			canonical_parent -> Device
			short_value_items -> StringVector
			value_items -> StringVector
		ParameterState = enabled, irrelevant, disabled
	DriftDevice:
		DriftDevice:
			View
			canonical_parent -> Track
			mod_matrix_filter_source_1_list -> StringVector
			mod_matrix_filter_source_2_list -> StringVector
			mod_matrix_lfo_source_list -> StringVector
			mod_matrix_pitch_source_1_list -> StringVector
			mod_matrix_pitch_source_2_list -> StringVector
			mod_matrix_shape_source_list -> StringVector
			mod_matrix_source_1_list -> StringVector
			mod_matrix_source_2_list -> StringVector
			mod_matrix_source_3_list -> StringVector
			mod_matrix_target_1_list -> StringVector
			mod_matrix_target_2_list -> StringVector
			mod_matrix_target_3_list -> StringVector
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
			voice_count_list -> StringVector
			voice_mode_list -> StringVector
	DrumCellDevice:
		DrumCellDevice:
			View
			canonical_parent -> Track
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
	DrumChain:
		DrumChain:
			canonical_parent -> RackDevice
			devices -> Vector
			mixer_device -> ChainMixerDevice
	DrumPad:
		DrumPad:
			canonical_parent -> RackDevice
			chains -> Vector
	Envelope:
		Envelope:
			canonical_parent -> Clip
		EnvelopeEvent:
			control_coefficients -> EnvelopeEventControlCoefficients
		EnvelopeEventControlCoefficients:
		EnvelopeEventVector:
	Eq8Device:
		EditMode = a, b
		Eq8Device:
			View:
				canonical_parent -> Eq8Device
			canonical_parent -> Track
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
		GlobalMode = stereo, left_right, mid_side
	Groove:
		Base = gb_four, gb_eight, gb_eight_triplet, gb_sixteen, gb_sixteen_triplet, gb_thirtytwo, count
		Groove:
			base -> Base
			canonical_parent -> GroovePool
	GroovePool:
		GroovePool:
			canonical_parent -> Song
			grooves -> Vector
	HybridReverbDevice:
		HybridReverbDevice:
			View
			canonical_parent -> Track
			ir_category_list -> StringVector
			ir_file_list -> StringVector
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
	Licensing:
		ProgressDialog:
		PythonLicensingBridge:
			base_product_id
			in_sassafras_mode
			license_must_match_variant
			random_number_for_trial_authorization
			set_has_unsaved_changes
		StartupDialog:
		TrialContext = SAVE, FORCE_UPDATE, STARTUP
		UnlockStatus:
	Listener:
		ListenerHandle:
			listener_func
			listener_self
			name
		ListenerVector:
	LomObject:
		LomObject:
	LooperDevice:
		LooperDevice:
			View
			canonical_parent -> Track
			parameters -> ATimeableValueVector
			record_length_list -> StringVector
			type -> DeviceType
			view -> View
	MaxDevice:
		MaxDevice:
			View
			audio_inputs -> Vector
			audio_outputs -> Vector
			canonical_parent -> Track
			is_using_compare_preset_b
			midi_inputs -> Vector
			midi_outputs -> Vector
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
	MeldDevice:
		MeldDevice:
			View
			canonical_parent -> Track
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
	MidiMap:
		CCFeedbackRule:
			cc_value_map -> tuple
		MapMode = absolute, relative_signed_bit, relative_binary_offset, relative_two_compliment, relative_signed_bit2, absolute_14_bit, relative_smooth_signed_bit, relative_smooth_binary_offset, relative_smooth_two_compliment, relative_smooth_signed_bit2
		NoteFeedbackRule:
			vel_map -> tuple
		PitchBendFeedbackRule:
			value_pair_map -> tuple
	MixerDevice:
		MixerDevice:
			canonical_parent -> Track
			crossfade_assignments = A, NONE, B
			crossfader -> DeviceParameter
			cue_volume -> DeviceParameter
			left_split_stereo -> DeviceParameter
			panning -> DeviceParameter
			panning_modes = stereo, stereo_split
			right_split_stereo -> DeviceParameter
			sends -> Vector
			song_tempo -> DeviceParameter
			track_activator -> DeviceParameter
			volume -> DeviceParameter
	PluginDevice:
		PluginDevice:
			View
			canonical_parent -> Track
			is_using_compare_preset_b
			parameters -> ATimeableValueVector
			presets -> StringVector
			type -> DeviceType
			view -> View
	RackDevice:
		RackDevice:
			View:
				canonical_parent -> RackDevice
				selected_drum_pad -> DrumPad
			canonical_parent -> Track
			chain_selector -> DeviceParameter
			chains -> Vector
			drum_pads -> Vector
			is_using_compare_preset_b
			macros_mapped -> tuple
			parameters -> ATimeableValueVector
			return_chains -> Vector
			type -> DeviceType
			view -> View
			visible_drum_pads -> Vector
	RoarDevice:
		RoarDevice:
			View
			canonical_parent -> Track
			parameters -> ATimeableValueVector
			routing_mode_list -> StringVector
			type -> DeviceType
			view -> View
	Sample:
		Sample:
			canonical_parent -> SimplerDevice
			slices -> tuple
			warp_markers -> WarpMarkerVector
		SlicingBeatDivision = sixteenth, sixteenth_triplett, eighth, eighth_triplett, quarter, quarter_triplett, half, half_triplett, one_bar, two_bars, four_bars
		SlicingStyle = transient, beat, region, manual
		TransientLoopMode = off, forward, alternate
	Scene:
		Scene:
			canonical_parent -> Song
			clip_slots -> Vector
	ShifterDevice:
		ShifterDevice:
			View
			canonical_parent -> Track
			parameters -> ATimeableValueVector
			pitch_mode_list -> StringVector
			type -> DeviceType
			view -> View
	SimplerDevice:
		PlaybackMode = classic, one_shot, slicing
		SimplerDevice:
			View:
				canonical_parent -> SimplerDevice
			canonical_parent -> Track
			parameters -> ATimeableValueVector
			sample -> Sample
			type -> DeviceType
			view -> View
		SlicingPlaybackMode = mono, poly, thru
	Song:
		BeatTime:
		CaptureDestination = auto, session, arrangement
		CaptureMode = all, all_except_selected
		CuePoint:
			canonical_parent -> Song
		Quantization = q_no_q, q_8_bars, q_4_bars, q_2_bars, q_bar, q_half, q_half_triplet, q_quarter, q_quarter_triplet, q_eight, q_eight_triplet, q_sixtenth, q_sixtenth_triplet, q_thirtytwoth
		RecordingQuantization = rec_q_no_q, rec_q_quarter, rec_q_eight, rec_q_eight_triplet, rec_q_eight_eight_triplet, rec_q_sixtenth, rec_q_sixtenth_triplet, rec_q_sixtenth_sixtenth_triplet, rec_q_thirtysecond
		SessionRecordStatus = off, transition, on
		SmptTime:
		Song:
			View:
				canonical_parent -> Song
				detail_clip -> Clip
				highlighted_clip_slot -> ClipSlot
				selected_scene -> Scene
				selected_track -> Track
			clip_trigger_quantization -> Quantization
			cue_points -> Vector
			groove_pool -> GroovePool
			master_track -> Track
			midi_recording_quantization -> RecordingQuantization
			return_tracks -> Vector
			scale_intervals -> IntVector
			scenes -> Vector
			tracks -> Vector
			tuning_system -> TuningSystem
			view -> View
			visible_tracks -> Vector
		TimeFormat = ms_time, smpte_24, smpte_25, smpte_30, smpte_30_drop, smpte_29
	SpectralResonatorDevice:
		SpectralResonatorDevice:
			View
			canonical_parent -> Track
			frequency_dial_mode_list -> StringVector
			midi_gate_list -> StringVector
			mod_mode_list -> StringVector
			mono_poly_list -> StringVector
			parameters -> ATimeableValueVector
			pitch_mode_list -> StringVector
			type -> DeviceType
			view -> View
	TakeLane:
		TakeLane:
			arrangement_clips -> Vector
			canonical_parent -> Track
	Track:
		DeviceContainer:
		DeviceInsertMode = default, selected_left, selected_right, count
		RoutingChannel:
			layout -> RoutingChannelLayout
		RoutingChannelLayout = mono, stereo, midi
		RoutingChannelVector:
		RoutingType:
			attached_object -> Track
		RoutingTypeCategory = external, rewire, resampling, master, track, parent_group_track, none, invalid
		RoutingTypeVector:
		Track:
			View:
				canonical_parent -> Track
				selected_device -> Device
			arrangement_clips -> Vector
			available_input_routing_channels -> RoutingChannelVector
			available_input_routing_types -> RoutingTypeVector
			available_output_routing_channels -> RoutingChannelVector
			available_output_routing_types -> RoutingTypeVector
			canonical_parent -> Song
			clip_slots -> Vector
			devices -> Vector
			group_track -> Track
			input_routing_channel -> RoutingChannel
			input_routing_type -> RoutingType
			input_routings -> StringVector
			input_sub_routings -> StringVector
			mixer_device -> MixerDevice
			monitoring_states = IN, AUTO, OFF
			output_routing_channel -> RoutingChannel
			output_routing_type -> RoutingType
			output_routings -> StringVector
			output_sub_routings -> StringVector
			take_lanes -> Vector
			view -> View
	TuningSystem:
		PitchClassAndOctave:
		ReferencePitch:
		TuningSystem:
			canonical_parent -> Song
			highest_note -> PitchClassAndOctave
			lowest_note -> PitchClassAndOctave
			note_tunings -> list
			reference_pitch -> ReferencePitch
	WavetableDevice:
		EffectMode = none, frequency_modulation, sync_and_pulse_width, warp_and_fold
		FilterRouting = serial, parallel, split
		ModulationSource = amp_envelope, envelope_2, envelope_3, lfo_1, lfo_2, midi_velocity, midi_note, midi_pitch_bend, midi_channel_pressure, midi_mod_wheel, midi_random
		UnisonMode = none, classic, slow_shimmer, fast_shimmer, phase_sync, position_spread, random_note
		VoiceCount = two, three, four, five, six, seven, eight
		Voicing = mono, poly
		WavetableDevice:
			View
			canonical_parent -> Track
			oscillator_1_wavetables -> StringVector
			oscillator_2_wavetables -> StringVector
			oscillator_wavetable_categories -> StringVector
			parameters -> ATimeableValueVector
			type -> DeviceType
			view -> View
			visible_modulation_target_names -> StringVector
```

## MaxForLive Documentation

These are the official Ableton MaxForLive docs for the Live Object Model. Use them to find parameter names, types, and descriptions.

### track.md

#### Track

This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.   
  
Not all properties are supported by all types of tracks. The properties are marked accordingly.

##### Canonical Path

```
live_set tracks N
```

##### Children

###### create_audio_clip

Parameters:   
`file_path` [symbol]   
`position` [float]   
Given an absolute path to a valid audio file in a supported format, creates an audio clip that references the file at the specified position in the arrangement view. Prints an error if the track is not an audio track, if the track is frozen, or if the track is being recorded into. The position must be within the range [0., 1576800].   
  
See the `ClipSlot.create_audio_clip` function if you need to create audio clips in session view instead.

###### create_midi_clip

Parameters:   
`start_time` [float]   
`length` [float]   
Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.   
  
See the `ClipSlot.create_clip` function if you need to create audio clips in session view instead.

###### duplicate_clip_slot

Parameter: `index`  
  
Works like 'Duplicate' in a clip's context menu.

###### jump_in_running_session_clip

Parameter: `beats`  
  
`beats` [float] is the amount to jump relatively to the current clip position.   
Modify playback position in running Session clip, if any.
