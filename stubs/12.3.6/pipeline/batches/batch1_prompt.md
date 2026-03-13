## Unresolved Items

```json
{
  "Live.Application.Application.View.add_is_view_visible_listener": {
    "description": "Add a listener function or method, which will be called as soon as the\nproperty \"is_view_visible\" has changed.",
    "signature": "add_is_view_visible_listener( (View)arg1, (object)arg2, (object)arg3) -> None :",
    "cpp_signature": "void add_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs_name": true
      }
    }
  },
  "Live.Application.Application.View.hide_view": {
    "description": "Hide one through the identifier string specified view.",
    "signature": "hide_view( (View)arg1, (object)arg2) -> None :",
    "cpp_signature": "void hide_view(TPyViewData<ASongApp>,TString)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs_name": true
      }
    }
  },
  "Live.Application.Application.View.is_view_visible_has_listener": {
    "description": "Returns true, if the given listener function or method is connected\nto the property \"is_view_visible\".",
    "signature": "is_view_visible_has_listener( (View)arg1, (object)arg2, (object)arg3) -> bool :",
    "cpp_signature": "bool is_view_visible_has_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs_name": true
      }
    }
  },
  "Live.Application.Application.View.remove_is_view_visible_listener": {
    "description": "Remove a previously set listener function or method from\nproperty \"is_view_visible\".",
    "signature": "remove_is_view_visible_listener( (View)arg1, (object)arg2, (object)arg3) -> None :",
    "cpp_signature": "void remove_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs_name": true
      }
    }
  },
  "Live.Application.Application.View.scroll_view": {
    "description": "Scroll through the identifier string specified view into the given\ndirection, if possible. Will silently return if the specified view\ncan not perform the requested action.",
    "signature": "scroll_view( (View)arg1, (int)arg2, (object)arg3, (bool)arg4) -> None :",
    "cpp_signature": "void scroll_view(TPyViewData<ASongApp>,int,TString,bool)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      },
      "arg3": {
        "current_type": "str",
        "needs_name": true
      },
      "arg4": {
        "current_type": "bool",
        "needs_name": true
      }
    }
  },
  "Live.Application.Application.View.zoom_view": {
    "description": "Zoom through the identifier string specified view into the given\ndirection, if possible. Will silently return if the specified view\ncan not perform the requested action.",
    "signature": "zoom_view( (View)arg1, (int)arg2, (object)arg3, (bool)arg4) -> None :",
    "cpp_signature": "void zoom_view(TPyViewData<ASongApp>,int,TString,bool)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      },
      "arg3": {
        "current_type": "str",
        "needs_name": true
      },
      "arg4": {
        "current_type": "bool",
        "needs_name": true
      }
    }
  },
  "Live.Application.Application.has_option": {
    "description": "Returns True if the given entry exists in Options.txt, False otherwise.",
    "signature": "has_option( (Application)arg1, (object)arg2) -> bool :",
    "cpp_signature": "bool has_option(TPyHandle<ASongApp>,TString)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs_name": true
      }
    }
  },
  "Live.Application.Application.press_current_dialog_button": {
    "description": "Press a button, by index, on the current message box.",
    "signature": "press_current_dialog_button( (Application)arg1, (int)arg2) -> None :",
    "cpp_signature": "void press_current_dialog_button(TPyHandle<ASongApp>,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Application.ControlSurfaceProxy.control_descriptions": {
    "probed_type": null
  },
  "Live.Application.ControlSurfaceProxy.enable_receive_midi": {
    "signature": "enable_receive_midi( (ControlSurfaceProxy)arg1, (bool)arg2) -> None :",
    "cpp_signature": "void enable_receive_midi(APythonControlSurfaceProxy {lvalue},bool)",
    "args": {
      "arg2": {
        "current_type": "bool",
        "needs_name": true
      }
    }
  },
  "Live.Application.ControlSurfaceProxy.grab_control": {
    "signature": "grab_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :",
    "cpp_signature": "void grab_control(APythonControlSurfaceProxy {lvalue},int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Application.ControlSurfaceProxy.pad_layout": {
    "probed_type": null,
    "raw_doc": "The layout of pads on Push."
  },
  "Live.Application.ControlSurfaceProxy.subscribe_to_control": {
    "signature": "subscribe_to_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :",
    "cpp_signature": "void subscribe_to_control(APythonControlSurfaceProxy {lvalue},int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Application.ControlSurfaceProxy.type_name": {
    "probed_type": null
  },
  "Live.Application.ControlSurfaceProxy.unsubscribe_from_control": {
    "signature": "unsubscribe_from_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :",
    "cpp_signature": "void unsubscribe_from_control(APythonControlSurfaceProxy {lvalue},int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Application.encrypt_challenge2": {
    "description": "Returns the UMAC hash for the given challenge.",
    "signature": "encrypt_challenge2( (int)arg1) -> int :",
    "cpp_signature": "int encrypt_challenge2(int)",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Application.get_random_int": {
    "description": "Returns a random integer from the given range.",
    "signature": "get_random_int( (int)arg1, (int)arg2) -> int :",
    "cpp_signature": "int get_random_int(int,int)",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs_name": true
      },
      "arg2": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Base.ObjectVector.append": {
    "signature": "append( (ObjectVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<boost::python::api::object, std::__1::allocator<boost::python::api::object>> {lvalue},boost::python::api::object)",
    "args": {
      "value": {
        "current_type": "object"
      }
    }
  },
  "Live.Base.ObjectVector.extend": {
    "signature": "extend( (ObjectVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<boost::python::api::object, std::__1::allocator<boost::python::api::object>> {lvalue},boost::python::api::object)",
    "args": {
      "values": {
        "current_type": "object"
      }
    }
  },
  "Live.Base.Text.text": {
    "probed_type": null
  },
  "Live.Base.subst_args": {
    "signature": "subst_args( (Text)text [, (str)arg1='' [, (str)arg2='' [, (str)arg3='' [, (str)arg4='' [, (str)arg5='']]]]]) -> str :",
    "cpp_signature": "std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> subst_args(TText [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='']]]]])",
    "args": {
      "arg1": {
        "current_type": "str",
        "needs_name": true
      },
      "arg2": {
        "current_type": "str",
        "needs_name": true
      },
      "arg3": {
        "current_type": "str",
        "needs_name": true
      },
      "arg4": {
        "current_type": "str",
        "needs_name": true
      },
      "arg5": {
        "current_type": "str",
        "needs_name": true
      }
    }
  },
  "Live.Browser.Browser.load_item": {
    "description": "Loads the provided browser item.",
    "signature": "load_item( (Browser)arg1, (BrowserItem)arg2) -> None :",
    "cpp_signature": "void load_item(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)",
    "args": {
      "arg2": {
        "current_type": "BrowserItem",
        "needs_name": true
      }
    }
  },
  "Live.Browser.Browser.preview_item": {
    "description": "Previews the provided browser item.",
    "signature": "preview_item( (Browser)arg1, (BrowserItem)arg2) -> None :",
    "cpp_signature": "void preview_item(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)",
    "args": {
      "arg2": {
        "current_type": "BrowserItem",
        "needs_name": true
      }
    }
  },
  "Live.Browser.Browser.relation_to_hotswap_target": {
    "description": "Returns the relation between the given browser item and the current hotswap target",
    "signature": "relation_to_hotswap_target( (Browser)arg1, (BrowserItem)arg2) -> Relation :",
    "cpp_signature": "ableton::live_library::Relation relation_to_hotswap_target(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)",
    "args": {
      "arg2": {
        "current_type": "BrowserItem",
        "needs_name": true
      }
    }
  },
  "Live.Chain.Chain.duplicate_device": {
    "description": "Duplicate the device at the given index in the chain.",
    "signature": "duplicate_device( (Chain)arg1, (int)arg2) -> None :",
    "cpp_signature": "void duplicate_device(TChainPyHandle,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.View.select_envelope_parameter": {
    "description": "Select the given device parameter in the envelope view.",
    "signature": "select_envelope_parameter( (View)arg1, (DeviceParameter)arg2) -> None :",
    "cpp_signature": "void select_envelope_parameter(TPyViewData<AClip>,TPyHandle<ATimeableValue>)",
    "args": {
      "arg2": {
        "current_type": "DeviceParameter",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.add_new_notes": {
    "description": "Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification\nobjects. The objects will be used to construct new notes in the clip.",
    "signature": "add_new_notes( (Clip)arg1, (object)arg2) -> IntU64Vector :",
    "cpp_signature": "std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> add_new_notes(TPyHandle<AClip>,boost::python::api::object)",
    "args": {
      "arg2": {
        "current_type": "object",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.add_warp_marker": {
    "description": "Available for AudioClips only.\nAdds the specified warp marker, if possible.",
    "signature": "add_warp_marker( (Clip)self, (object)warp_marker) -> None :",
    "cpp_signature": "void add_warp_marker(TPyHandle<AClip>,boost::python::api::object)",
    "args": {
      "warp_marker": {
        "current_type": "object"
      }
    }
  },
  "Live.Clip.Clip.apply_note_modifications": {
    "description": "Expects a list of notes as returned from get_notes_extended. The content\nof the list will be used to modify existing notes in the clip, based on\nmatching note IDs.\nThis function should be used when modifying existing notes, e.g. changing the\nvelocity or start time. The function ensures that per-note events attached to\nthe modified notes are preserved. This is NOT the case when replacing notes\nvia a combination of remove_notes_extended and add_new_notes.\nThe given list can be a subset of the notes in the clip, but it must not\ncontain any notes that are not present in the clip.",
    "signature": "apply_note_modifications( (Clip)arg1, (MidiNoteVector)arg2) -> None :",
    "cpp_signature": "void apply_note_modifications(TPyHandle<AClip>,std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>>)",
    "args": {
      "arg2": {
        "current_type": "MidiNoteVector",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.automation_envelope": {
    "description": "Return the envelope for the given parameter.Returns None if the envelope doesn't exist.Returns None for Arrangement clips.Returns None for parameters from a different track.",
    "signature": "automation_envelope( (Clip)arg1, (DeviceParameter)arg2) -> Envelope :",
    "cpp_signature": "TWeakPtr<TPyHandle<AAutomation>> automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)",
    "args": {
      "arg2": {
        "current_type": "DeviceParameter",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.clear_envelope": {
    "description": "Clears the envelope of this clips given parameter.",
    "signature": "clear_envelope( (Clip)arg1, (DeviceParameter)arg2) -> None :",
    "cpp_signature": "void clear_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)",
    "args": {
      "arg2": {
        "current_type": "DeviceParameter",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.create_automation_envelope": {
    "description": "Creates an envelope for a given parameter and returns it.This should only be used if the envelope doesn't exist.Raises an error if the envelope can't be created.",
    "signature": "create_automation_envelope( (Clip)arg1, (DeviceParameter)arg2) -> Envelope :",
    "cpp_signature": "TWeakPtr<TPyHandle<AAutomation>> create_automation_envelope(TPyHandle<AClip>,TPyHandle<ATimeableValue>)",
    "args": {
      "arg2": {
        "current_type": "DeviceParameter",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.duplicate_notes_by_id": {
    "description": "Duplicate all notes matching the given note IDs.\nIf the optional destination_time is not provided, new notes will be inserted\nafter the last selected note. This behavior can be observed when duplicating\nnotes in the Live GUI.\nIf the transposition_amount is specified, the notes in the region will be\ntransposed by the number of semitones.\nRaises an error on audio clips.",
    "signature": "duplicate_notes_by_id( (Clip)self, (object)note_ids [, (object)destination_time=None [, (int)transposition_amount=0]]) -> IntU64Vector :",
    "cpp_signature": "std::__1::vector<unsigned long long, std::__1::allocator<unsigned long long>> duplicate_notes_by_id(TPyHandle<AClip>,boost::python::api::object [,boost::python::api::object=None [,int=0]])",
    "args": {
      "note_ids": {
        "current_type": "object"
      },
      "destination_time": {
        "current_type": "object"
      }
    }
  },
  "Live.Clip.Clip.get_notes_by_id": {
    "description": "Return a list of MIDI notes matching the given note IDs.",
    "signature": "get_notes_by_id( (Clip)arg1, (object)note_ids) -> MidiNoteVector :",
    "cpp_signature": "std::__1::vector<NClipApi::TNoteInfo, std::__1::allocator<NClipApi::TNoteInfo>> get_notes_by_id(TPyHandle<AClip>,boost::python::api::object)",
    "args": {
      "note_ids": {
        "current_type": "object"
      }
    }
  },
  "Live.Clip.Clip.move_playing_pos": {
    "description": "Jump forward or backward by the specified relative amount in beats.\nWill do nothing, if the Clip is not playing.",
    "signature": "move_playing_pos( (Clip)arg1, (float)arg2) -> None :",
    "cpp_signature": "void move_playing_pos(TPyHandle<AClip>,double)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.quantize": {
    "description": "Quantize all notes in a clip or align warp markers.",
    "signature": "quantize( (Clip)arg1, (int)arg2, (float)arg3) -> None :",
    "cpp_signature": "void quantize(TPyHandle<AClip>,int,float)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      },
      "arg3": {
        "current_type": "float",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.quantize_pitch": {
    "description": "Quantize all the notes of a given pitch. Raises an error on audio clips.",
    "signature": "quantize_pitch( (Clip)arg1, (int)arg2, (int)arg3, (float)arg4) -> None :",
    "cpp_signature": "void quantize_pitch(TPyHandle<AClip>,int,int,float)",
    "args": {
      "arg4": {
        "current_type": "float",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.remove_notes": {
    "description": "Delete all notes starting in the given pitch- and time range.",
    "signature": "remove_notes( (Clip)arg1, (float)arg2, (int)arg3, (float)arg4, (int)arg5) -> None :",
    "cpp_signature": "void remove_notes(TPyHandle<AClip>,double,int,double,int)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs_name": true
      },
      "arg3": {
        "current_type": "int",
        "needs_name": true
      },
      "arg4": {
        "current_type": "float",
        "needs_name": true
      },
      "arg5": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.remove_notes_by_id": {
    "description": "Delete all notes matching the given note IDs.\nThis function should NOT be used to implement modification of existing notes\n(i.e. in combination with add_new_notes), as that leads to loss of per-note\nevents. apply_note_modifications must be used instead for modifying existing\nnotes.",
    "signature": "remove_notes_by_id( (Clip)arg1, (object)arg2) -> None :",
    "cpp_signature": "void remove_notes_by_id(TPyHandle<AClip>,boost::python::api::object)",
    "args": {
      "arg2": {
        "current_type": "object",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.replace_selected_notes": {
    "description": "Called with a tuple of tuples where each inner tuple represents\na note in the same format as returned by get_selected_notes. The\nnotes described that way will then be used to replace the old selection.",
    "signature": "replace_selected_notes( (Clip)arg1, (tuple)arg2) -> None :",
    "cpp_signature": "void replace_selected_notes(TPyHandle<AClip>,boost::python::tuple)",
    "args": {
      "arg2": {
        "current_type": "tuple",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.select_notes_by_id": {
    "description": "Selects all notes matching the given note IDs.",
    "signature": "select_notes_by_id( (Clip)arg1, (object)arg2) -> None :",
    "cpp_signature": "void select_notes_by_id(TPyHandle<AClip>,boost::python::api::object)",
    "args": {
      "arg2": {
        "current_type": "object",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.set_fire_button_state": {
    "description": "Set the clip's fire button state directly. Supports all launch modes.",
    "signature": "set_fire_button_state( (Clip)arg1, (bool)arg2) -> None :",
    "cpp_signature": "void set_fire_button_state(TPyHandle<AClip>,bool)",
    "args": {
      "arg2": {
        "current_type": "bool",
        "needs_name": true
      }
    }
  },
  "Live.Clip.Clip.set_notes": {
    "description": "Called with a tuple of tuples where each inner tuple represents\na note in the same format as returned by get_notes. The\nnotes described that way will then be added to the clip.",
    "signature": "set_notes( (Clip)arg1, (tuple)arg2) -> None :",
    "cpp_signature": "void set_notes(TPyHandle<AClip>,boost::python::tuple)",
    "args": {
      "arg2": {
        "current_type": "tuple",
        "needs_name": true
      }
    }
  },
  "Live.ClipSlot.ClipSlot.create_audio_clip": {
    "description": "Creates an audio clip referencing the file at the given absolute path in the slot.\nThrows an error when called on non-empty slots or slots in non-audio or frozen tracks, or when the path doesn't point at a valid audio file.",
    "signature": "create_audio_clip( (ClipSlot)arg1, (object)arg2) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TPyHandle<AGroupAndClipSlotBase>,TString)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs_name": true
      }
    }
  },
  "Live.ClipSlot.ClipSlot.duplicate_clip_to": {
    "description": "Duplicates the slot's clip to the passed in target slot.\nOverrides the target's clip if it's not empty.\nRaises an exception if the (source) slot itself is empty, or if source and\ntarget have different track types (audio vs. MIDI). Also raises if the source\nor target slot is in a group track (so called group slot).",
    "signature": "duplicate_clip_to( (ClipSlot)arg1, (ClipSlot)arg2) -> None :",
    "cpp_signature": "void duplicate_clip_to(TPyHandle<AGroupAndClipSlotBase>,TPyHandle<AGroupAndClipSlotBase>)",
    "args": {
      "arg2": {
        "current_type": "ClipSlot",
        "needs_name": true
      }
    }
  },
  "Live.ClipSlot.ClipSlot.set_fire_button_state": {
    "description": "Set the clipslot's fire button state directly. Supports all launch modes.",
    "signature": "set_fire_button_state( (ClipSlot)arg1, (bool)arg2) -> None :",
    "cpp_signature": "void set_fire_button_state(TPyHandle<AGroupAndClipSlotBase>,bool)",
    "args": {
      "arg2": {
        "current_type": "bool",
        "needs_name": true
      }
    }
  },
  "Live.Device.Device.store_chosen_bank": {
    "description": "Set the selected bank in the device for persistency.",
    "signature": "store_chosen_bank( (Device)arg1, (int)arg2, (int)arg3) -> None :",
    "cpp_signature": "void store_chosen_bank(TPyHandle<ADevice>,int,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs_name": true
      },
      "arg3": {
        "current_type": "int",
        "needs_name": true
      }
    }
  },
  "Live.DeviceParameter.DeviceParameter.str_for_value": {
    "description": "Return a string representation of the given value. To be used\nfor display purposes only. This value can include characters like 'db' or\n'hz', depending on the type of the parameter.",
    "signature": "str_for_value( (DeviceParameter)arg1, (float)arg2) -> str :",
    "cpp_signature": "TString str_for_value(TPyHandle<ATimeableValue>,float)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs_name": true
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
  "Live.Application.Application.View.hide_view": {
    "args": {
      "arg2": {
        "call_site_names": [
          "view_name"
        ],
        "_votes": {
          "view_name": 1
        },
        "_total_sites": 12
      }
    }
  },
  "Live.Application.Application.View.scroll_view": {
    "args": {
      "arg2": {
        "call_site_names": [
          "direction",
          "up",
          "down",
          "left",
          "right"
        ],
        "_votes": {
          "direction": 14,
          "up": 2,
          "down": 2,
          "left": 2,
          "right": 2
        },
        "_total_sites": 22
      },
      "arg4": {
        "call_site_names": [
          "alt_is_pressed"
        ],
        "_votes": {
          "alt_is_pressed": 8
        },
        "_total_sites": 22
      }
    }
  },
  "Live.Application.Application.View.zoom_view": {
    "args": {
      "arg2": {
        "call_site_names": [
          "up",
          "down",
          "left",
          "right"
        ],
        "_votes": {
          "up": 2,
          "down": 2,
          "left": 2,
          "right": 2
        },
        "_total_sites": 8
      },
      "arg4": {
        "call_site_names": [
          "alt_is_pressed"
        ],
        "_votes": {
          "alt_is_pressed": 8
        },
        "_total_sites": 8
      }
    }
  },
  "Live.Application.Application.has_option": {
    "args": {
      "arg2": {
        "call_site_names": [
          "section_name"
        ],
        "_votes": {
          "section_name": 2
        },
        "_total_sites": 7
      }
    }
  },
  "Live.Application.ControlSurfaceProxy.grab_control": {
    "args": {
      "arg2": {
        "call_site_names": [
          "control"
        ],
        "_votes": {
          "control": 1
        },
        "_total_sites": 1
      }
    }
  },
  "Live.Browser.Browser.load_item": {
    "args": {
      "arg2": {
        "call_site_names": [
          "content"
        ],
        "_votes": {
          "content": 1
        },
        "_total_sites": 1
      }
    }
  },
  "Live.Browser.Browser.preview_item": {
    "args": {
      "arg2": {
        "call_site_names": [
          "content"
        ],
        "_votes": {
          "content": 1
        },
        "_total_sites": 1
      }
    }
  },
  "Live.Clip.Clip.add_new_notes": {
    "args": {
      "arg2": {
        "call_site_names": [
          "notes"
        ],
        "_votes": {
          "notes": 1
        },
        "_total_sites": 3
      }
    }
  },
  "Live.Clip.Clip.clear_envelope": {
    "args": {
      "arg2": {
        "call_site_names": [
          "parameter"
        ],
        "_votes": {
          "parameter": 2
        },
        "_total_sites": 2
      }
    }
  },
  "Live.Clip.Clip.quantize": {
    "args": {
      "arg2": {
        "call_site_names": [
          "quantize_to",
          "quantization_setting"
        ],
        "_votes": {
          "quantize_to": 2,
          "quantization_setting": 1
        },
        "_total_sites": 7
      },
      "arg3": {
        "call_site_names": [
          "quantize_amount"
        ],
        "_votes": {
          "quantize_amount": 1
        },
        "_total_sites": 7
      }
    }
  },
  "Live.Clip.Clip.quantize_pitch": {
    "args": {
      "arg4": {
        "call_site_names": [
          "quantize_amount"
        ],
        "_votes": {
          "quantize_amount": 1
        },
        "_total_sites": 1
      }
    }
  },
  "Live.Clip.Clip.set_fire_button_state": {
    "args": {
      "arg2": {
        "call_site_names": [
          "fire_state",
          "button_state"
        ],
        "_votes": {
          "fire_state": 1,
          "button_state": 1
        },
        "_total_sites": 3
      }
    }
  },
  "Live.ClipSlot.ClipSlot.set_fire_button_state": {
    "args": {
      "arg2": {
        "call_site_names": [
          "fire_state",
          "button_state"
        ],
        "_votes": {
          "fire_state": 1,
          "button_state": 1
        },
        "_total_sites": 3
      }
    }
  },
  "Live.ClipSlot.ClipSlot.duplicate_clip_to": {
    "args": {
      "arg2": {
        "call_site_names": [
          "obj"
        ],
        "_votes": {
          "obj": 1
        },
        "_total_sites": 1
      }
    }
  },
  "Live.DeviceParameter.DeviceParameter.str_for_value": {
    "args": {
      "arg2": {
        "call_site_names": [
          "value"
        ],
        "_votes": {
          "value": 1
        },
        "_total_sites": 1
      }
    }
  }
}
```

### Type Usage Context

Code snippets showing how members with unresolved types are used in practice. Use these to infer types from usage patterns (e.g. compared to strings → str, iterated → sequence, etc.).

```json
{
  "Live.Application.ControlSurfaceProxy.control_descriptions": {
    "usage_snippets": [
      "return tuple((c.name for c in self._proxy.control_descriptions))"
    ],
    "unresolved_property_type": true
  },
  "Live.Application.ControlSurfaceProxy.type_name": {
    "usage_snippets": [
      "def type_name(self):",
      "return obj.type_name",
      "return self._proxy.type_name"
    ],
    "unresolved_property_type": true
  },
  "Live.Base.ObjectVector.append": {
    "usage_snippets": [
      "bank_buttons_raw.append(DeviceButton(channel, cc, name=name))",
      "clip_launch_buttons.append(self._control_factory.create_clip_launch_button(index))",
      "clip_stop_buttons.append(self._control_factory.create_clip_stop_button(index))",
      "parameter_encoders_raw.append(EncoderElement(MIDI_CC_TYPE,",
      "self._ProjectMixIO__components.append(self._ProjectMixIO__main_display)",
      "self._modes_buttons.append(button)",
      "self._sliders.append(make_slider(41 + index, \"Volume_Control_%d\" % index))",
      "self._strip_buttons.append(make_button(51 + index, \"Mute_Button_%d\" % index))",
      "send_controls_raw.append(make_mixer_encoder(cc,",
      "send_info.append(mixer_options[\"SEND{}\".format(send + 1)])"
    ],
    "unresolved_arg_types": {
      "value": "object"
    }
  },
  "Live.Base.ObjectVector.extend": {
    "usage_snippets": [
      "chains.extend(nested_chains)",
      "data_to_send.extend(as_ascii(adjust_string(scene.name, NAME_LENGTH).strip()))",
      "data_to_send.extend(as_ascii(adjust_string(track.name, NAME_LENGTH).strip()))",
      "notes_to_render.extend(wrap_note(note_on, note_off, clip_length))",
      "self._additional_parameters.extend([self.zoom, self.envelope])",
      "self._clip_data[\"notes\"].extend([create_note(payload[i[:i + BYTES_PER_NOTE]], group_offset) for i in range(0, payload_length, BYTES_PER_NOTE)])",
      "self._items.extend(list(map(self._item_wrapper, next_slice)))",
      "self._mixer_sections.extend([",
      "self._note_off_events.extend(note_offs)",
      "self._note_on_events.extend(note_ons)"
    ],
    "unresolved_arg_types": {
      "values": "object"
    }
  },
  "Live.Base.Text.text": {
    "usage_snippets": [
      "def text(self):",
      "def text(self, text):",
      "from .text import Text",
      "self._message_box.text = consts.MessageBoxText.EMPTY_DEVICE_CHAIN",
      "self._message_box.text = message",
      "self._message_box.text = text",
      "text = self._adaptee.text"
    ],
    "unresolved_property_type": true
  },
  "Live.Clip.Clip.get_notes_by_id": {
    "usage_snippets": [
      "midi_notes = lom_object.get_notes_by_id(id_to_note_mapping.keys())"
    ],
    "unresolved_arg_types": {
      "note_ids": "object"
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

### application.md

#### Application

This class represents the Live application. It is reachable by the root path `live_app`.

##### Canonical Path

```
live_app
```

##### Children

###### press_current_dialog_button

Parameter: `index`  
Press the button with the given index in the current dialog box.

### application_view.md

#### Application.View

This class represents the aspects of the Live application related to viewing the application.

##### Canonical Path

```
live_app view
```

##### Properties

###### hide_view

Parameter: `view_name`  
Hides the named view. You can also pass an empty view_name “ ", which refers to the Arrangement or Session View (whichever is visible in the main window).

###### scroll_view

Parameters: `direction view_name modifier_pressed`  
`direction` [int] is 0 = up, 1 = down, 2 = left, 3 = right   
`modifier_pressed` [bool] If view_name is "Arranger" and modifier_pressed is 1 and direction is left or right, then the size of the selected time region is modified, otherwise the position of the playback cursor is moved.   
Not all views are scrollable, and not in all directions. Currently, only the `Arranger`, `Browser`, `Session`, and `Detail/DeviceChain` views can be scrolled.   
You can also pass an empty view_name `" "`, which refers to the Arrangement or Session View (whichever view is visible).

###### zoom_view

Parameter: `direction view_name modifier_pressed`  
`direction` [int] - 0 = up, 1 = down, 2 = left, 3 = right   
`modifier_pressed` [bool] If `view_name` is 'Arrangement', `modifier_pressed` is 1, and `direction` is left or right, then the size of the selected time region is modified, otherwise the position of the playback cursor is moved. If `view_name` is Arrangement and `modifier_pressed` is 1 and `direction` is up or down, then only the height of the highlighted track is changed, otherwise the height of all tracks is changed.   
Only the Arrangement and Session Views can be zoomed. For Session View, the behaviour of zoom_view is identical to scroll_view. You can also pass an empty view_name “ ", which refers to the Arrangement or Session View (whichever is visible in the main window).

### clip.md

#### Clip

This class represents a clip in Live. It can be either an audio clip or a MIDI clip in the Arrangement or Session View, depending on the track / slot it lives in.

##### Canonical Paths

```
live_set tracks N clip_slots M clip
```

```
live_set tracks N arrangement_clips M
```

##### Children

###### add_new_notes

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

###### add_warp_marker

Only available for warped Audio Clips. Adds the specified warp marker, if possible.   
  
The warp marker is specified as a dict which can have a `beat_time` and a `sample_time` key, both associated with float values.   
The `sample_time` key may be omitted; in this case, Live will calculate the appropriate sample time to create a warp marker at the specified beat time without changing the Clip's playback timing, similar to what would happen if you were to double-click in the upper half of the Sample Display in Clip View.   
  
If `sample_time` is specified, certain limitations must be taken into account: \

* The sample time must lie within the range *[0, s]*, where *s* is the sample's length. The `sample_length` Clip property helps with this.
* The sample time must lie between the left and right adjacents markers' respective sample times (this is a logical constraint).
* Within these constraints, there are limitations on the resulting segments' BPM. The allowed BPM range is *[5, 999]*.

###### apply_note_modifications

Parameter:   
`dictionary`  
Key: `"notes"` [list of note dictionaries] as returned from `get_notes_extended`.   
The list of note dictionaries passed to the function can be a subset of notes in the clip, but will be ignored if it contains any notes that are not present in the clip.   
  
For MIDI clips only.   
  
*Available since Live 11.0. Replaces modifying notes with remove_notes followed by set_notes.*

###### clear_envelope

Parameter:   
`device_parameter` [id]   
Removes the automation of the clip for the given parameter.

###### duplicate_notes_by_id

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

###### get_notes_by_id

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

###### move_playing_pos

Parameter: `beats`  
`beats` [float] relative jump distance in beats. Negative beats jump backwards.   
Jumps by given amount, unquantized.   
Unwarped audio clips, recording audio clips and recording non-overdub MIDI clips cannot jump.

###### quantize

Parameter:   
`quantization_grid` [int]   
`amount` [float]   
Quantizes all notes in the clip to the quantization_grid taking the song's swing_amount into account.

###### quantize_pitch

Parameter:   
`pitch` [int]   
`quantization_grid` [int]   
`amount` [float]   
Same as *quantize*, but only for notes in the given pitch.

###### remove_notes_by_id

Parameter:   
`list` of note IDs.   
Deletes all notes associated with the provided IDs.   
Provided note IDs must be associated with existing notes in the clip. Existing notes can be queried with `get_notes_extended`.   
  
*Available since Live 11.0.*

###### select_notes_by_id

Parameter:   
`list` of note IDs.   
Selects all notes associated with the provided IDs.   
  
Note that this function will *not* print a warning or error if the list contains nonexistent IDs.   
  
*Available since Live 11.0.6*

###### set_fire_button_state

Parameter: `state` [bool]   
If the state is set to 1, Live simulates pressing the clip start button until the state is set to 0, or until the clip is otherwise stopped.

### clip_view.md

#### Clip.View

Representing the view aspects of a Clip.

##### Canonical Path

```
live_set tracks N clip_slots M clip view
```

##### Properties

###### select_envelope_parameter

Parameter: [DeviceParameter]   
Select the specified device parameter in the Envelopes box.

### clipslot.md

#### ClipSlot

This class represents an entry in Live's Session View matrix.   
  
The properties `playing_status`, `is_playing` and `is_recording` are useful for clip slots of Group Tracks. These are always empty and represent the state of the clips in the tracks within the Group Track.

##### Canonical Path

```
live_set tracks N clip_slots M
```

##### Children

###### create_audio_clip

Parameter: `path`  
Given an absolute path to a valid audio file in a supported format, creates an audio clip that references the file in the clip slot. Throws an error if the clip slot doesn't belong to an audio track or if the track is frozen.

###### duplicate_clip_to

Parameter: `target_clip_slot` [ClipSlot]   
Duplicates the slot's clip to the given clip slot, overriding the target clip slot's clip if it's not empty.

###### set_fire_button_state

Parameter: `state` [bool]   
1 = Live simulates pressing of Clip Launch button until the state is set to 0 or until the slot is stopped otherwise.

### controlsurface.md

#### ControlSurface

A ControlSurface can be reached either directly by the root path `control_surfaces N` or by getting a list of active control surface IDs, via calling *get control_surfaces* on an Application object.   
The latter list is in the same order in which control surfaces appear in Live's Link/MIDI Preferences. Note the same order is not guaranteed when getting a control surface via the `control_surfaces N` path.   
  
A control surface can be thought of as a software layer between the Live API and, in this case, Max for Live. Individiual controls on the surface are represented by objects that can be grabbed and released via Max for Live, to obtain and give back exclusive control (see *grab_control* and *release_control*). In this way, parts of the hardware can be controlled via Max for Live while other parts can retain their default functionality.   
  
Additionally, Live offers a special `MaxForLive` control surface that has a *register_midi_control* function. Using this, Max for Live developers can set up entirely custom control surfaces by adding and grabbing arbitrary controls.

##### Canonical Path

```
control_surfaces N
```

##### Properties

###### pad_layout symbol read-onlyobserve

The active pad layout.  
  
On Push 2 and 3, the layout can be changed with the Note and Session buttons and depends on the loaded instrument. Layout variants can be selected by pressing the Layout button.  
  
Available layouts are:\

* Melodic mode - the device chain is empty or an Instrument is loaded  
  `note.melodic.64_notes` - Melodic: 64 Notes  
  `note.melodic.64_notes_and_macro_variations` - Melodic: 64 Notes + Macro Variations  
  `note.melodic.sequencer` - Melodic: Sequencer  
  `note.melodic.sequencer_and_32_notes` - Melodic: Sequencer + 32 Notes
* Drums mode - a Drum Rack is loaded  
  `note.drums.macro_variations` - Drums: Macro Variations  
  `note.drums.64_pads` - Drums: 64 Pads  
  `note.drums.loop_selector` - Drums: Loop Selector  
  `note.drums.16_velocities` - Drums: 16 Velocities  
  `note.drums.16_pitches` - Drums: 16 Pitches
* Session mode - the Session button was pressed  
  `session` - Session is active

##### Functions

###### grab_control

Parameter: `control`  
Take ownership of the *control*. This releases all standard functionality of the control, so that it can be used exclusively via Max for Live.

### device.md

#### Device

This class represents a MIDI or audio device in Live.

##### Canonical Paths

```
live_set tracks N devices M
```

```
live_set tracks N devices M chains L devices K
```

```
live_set tracks N devices M return_chains L devices K
```

##### Children

###### store_chosen_bank

Parameters:   
`script_index` [int]   
`bank_index` [int]   
(This is related to hardware control surfaces and is usually not relevant.)

### deviceparameter.md

#### DeviceParameter

This class represents an (automatable) parameter within a MIDI or audio device. To modify a device parameter, set its `value` property or send its object ID to [live.remote~](/reference/live.remote~ "live.remote~").

##### Canonical Path

```
live_set tracks N devices M parameters L
```

##### Properties

###### str_for_value

Parameter: `value` [float] Returns: [symbol] String representation of the specified value.
