## Unresolved Items

```json
{
  "Live.Licensing.PythonLicensingBridge.base_product_id": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns Live's current base product ID."
  },
  "Live.Licensing.PythonLicensingBridge.get_startup_dialog": {
    "description": "Retrieves an instance of the startup dialog with the passed callables connected to its buttons.",
    "signature": "get_startup_dialog( (PythonLicensingBridge)arg1, (object)authorize_callable, (object)authorize_later_callable) -> StartupDialog :",
    "cpp_signature": "TWeakPtr<AStartupDialog> get_startup_dialog(APythonLicensingBridge {lvalue},boost::python::api::object,boost::python::api::object)",
    "args": {
      "authorize_callable": {
        "current_type": "object",
        "needs": [
          "type"
        ]
      },
      "authorize_later_callable": {
        "current_type": "object",
        "needs": [
          "type"
        ]
      }
    }
  },
  "Live.Licensing.PythonLicensingBridge.in_sassafras_mode": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ]
  },
  "Live.Licensing.PythonLicensingBridge.license_must_match_variant": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns a bool indicating if we require the license information returned by the server to match the variant of Live."
  },
  "Live.Licensing.PythonLicensingBridge.process_license_response": {
    "description": "Processes a list of strings, each representing a server response to a product authorization.",
    "signature": "process_license_response( (PythonLicensingBridge)arg1, (list)license_response_lines) -> UnlockStatus :",
    "cpp_signature": "TUnlockStatus process_license_response(APythonLicensingBridge {lvalue},boost::python::list)",
    "args": {
      "license_response_lines": {
        "current_type": "list",
        "needs": [
          "type"
        ]
      }
    }
  },
  "Live.Licensing.PythonLicensingBridge.random_number_for_trial_authorization": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns the integer to send along with the Trial authorization request. This same integer will be checked for in `process_trial_response` (and then changed)."
  },
  "Live.Licensing.PythonLicensingBridge.set_has_unsaved_changes": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns true if the set has unsaved changes."
  },
  "Live.Licensing.PythonLicensingBridge.set_network_timer": {
    "description": "Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer. If any callback invocation raises an exception, the timer is stopped.",
    "signature": "set_network_timer( (PythonLicensingBridge)arg1, (object)callback, (int)interval_in_ms) -> None :",
    "cpp_signature": "void set_network_timer(APythonLicensingBridge {lvalue},boost::python::api::object,int)",
    "args": {
      "callback": {
        "current_type": "object",
        "needs": [
          "type"
        ]
      }
    }
  },
  "Live.Licensing.get_unlock_dir": {
    "description": "Returns a tuple containing the unlock file directory and a flag indicating if the unlock file is in the system domain.",
    "signature": "get_unlock_dir() -> tuple :",
    "cpp_signature": "boost::python::tuple get_unlock_dir()",
    "returns": {
      "current_type": "tuple",
      "needs": [
        "type"
      ]
    }
  },
  "Live.Listener.ListenerHandle.listener_func": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns the original function"
  },
  "Live.Listener.ListenerHandle.listener_self": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns the weak reference to original self, if it was a bound method"
  },
  "Live.Listener.ListenerHandle.name": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Prints the name of the property that this listener is connected to"
  },
  "Live.Listener.ListenerVector": {
    "needs": [
      "element_repr"
    ],
    "raw_doc": "A read only container for accessing a list of listeners."
  },
  "Live.LooperDevice.LooperDevice.export_to_clip_slot": {
    "description": "Export Looper's content to a Session Clip Slot.",
    "signature": "export_to_clip_slot( (LooperDevice)arg1, (ClipSlot)arg2) -> None :",
    "cpp_signature": "void export_to_clip_slot(TLooperDevicePyHandle,TPyHandle<AGroupAndClipSlotBase>)",
    "args": {
      "arg2": {
        "current_type": "ClipSlot",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MaxDevice.MaxDevice.get_bank_name": {
    "description": "Get the name of a parameter bank given by index. This is related to hardware control surfaces.",
    "signature": "get_bank_name( (MaxDevice)arg1, (int)arg2) -> str :",
    "cpp_signature": "TString get_bank_name(TMaxDevicePyHandle,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MaxDevice.MaxDevice.get_bank_parameters": {
    "description": "Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces.",
    "signature": "get_bank_parameters( (MaxDevice)arg1, (int)arg2) -> list :",
    "cpp_signature": "boost::python::list get_bank_parameters(TMaxDevicePyHandle,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    },
    "returns": {
      "current_type": "list",
      "needs": [
        "type"
      ]
    }
  },
  "Live.MaxDevice.MaxDevice.get_value_item_icons": {
    "description": "Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.",
    "signature": "get_value_item_icons( (MaxDevice)arg1, (DeviceParameter)arg2) -> list :",
    "cpp_signature": "boost::python::list get_value_item_icons(TMaxDevicePyHandle,TPyHandle<ATimeableValue>)",
    "args": {
      "arg2": {
        "current_type": "DeviceParameter",
        "needs": [
          "name"
        ]
      }
    },
    "returns": {
      "current_type": "list",
      "needs": [
        "type"
      ]
    }
  },
  "Live.MaxDevice.MaxDevice.is_using_compare_preset_b": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors."
  },
  "Live.MidiMap.CCFeedbackRule.cc_value_map": {
    "probed_type": "tuple",
    "needs": [
      "element_repr"
    ]
  },
  "Live.MidiMap.NoteFeedbackRule.vel_map": {
    "probed_type": "tuple",
    "needs": [
      "element_repr"
    ]
  },
  "Live.MidiMap.PitchBendFeedbackRule.value_pair_map": {
    "probed_type": "tuple",
    "needs": [
      "element_repr"
    ]
  },
  "Live.MidiMap.forward_midi_cc": {
    "signature": "forward_midi_cc( (int)arg1, (int)arg2, (int)arg3, (int)arg4 [, (bool)ShouldConsumeEvent=True]) -> bool :",
    "cpp_signature": "bool forward_midi_cc(unsigned int,unsigned int,int,int [,bool=True])",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg4": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MidiMap.forward_midi_note": {
    "signature": "forward_midi_note( (int)arg1, (int)arg2, (int)arg3, (int)arg4 [, (bool)ShouldConsumeEvent=True]) -> bool :",
    "cpp_signature": "bool forward_midi_note(unsigned int,unsigned int,int,int [,bool=True])",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg4": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MidiMap.forward_midi_pitchbend": {
    "signature": "forward_midi_pitchbend( (int)arg1, (int)arg2, (int)arg3) -> bool :",
    "cpp_signature": "bool forward_midi_pitchbend(unsigned int,unsigned int,int)",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MidiMap.map_midi_note": {
    "signature": "map_midi_note( (int)arg1, (DeviceParameter)arg2, (int)arg3, (int)arg4) -> bool :",
    "cpp_signature": "bool map_midi_note(unsigned int,TPyHandle<ATimeableValue>,int,int)",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg2": {
        "current_type": "DeviceParameter",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg4": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MidiMap.map_midi_note_with_feedback_map": {
    "signature": "map_midi_note_with_feedback_map( (int)arg1, (DeviceParameter)arg2, (int)arg3, (int)arg4, (NoteFeedbackRule)arg5) -> bool :",
    "cpp_signature": "bool map_midi_note_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,int,NPythonMidiMap::TNoteFeedbackRule)",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg2": {
        "current_type": "DeviceParameter",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg4": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg5": {
        "current_type": "NoteFeedbackRule",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MidiMap.map_midi_pitchbend": {
    "signature": "map_midi_pitchbend( (int)arg1, (DeviceParameter)arg2, (int)arg3, (bool)arg4) -> bool :",
    "cpp_signature": "bool map_midi_pitchbend(unsigned int,TPyHandle<ATimeableValue>,int,bool)",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg2": {
        "current_type": "DeviceParameter",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg4": {
        "current_type": "bool",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MidiMap.map_midi_pitchbend_with_feedback_map": {
    "signature": "map_midi_pitchbend_with_feedback_map( (int)arg1, (DeviceParameter)arg2, (int)arg3, (PitchBendFeedbackRule)arg4, (bool)arg5) -> bool :",
    "cpp_signature": "bool map_midi_pitchbend_with_feedback_map(unsigned int,TPyHandle<ATimeableValue>,int,NPythonMidiMap::TPitchBendFeedbackRule,bool)",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg2": {
        "current_type": "DeviceParameter",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg4": {
        "current_type": "PitchBendFeedbackRule",
        "needs": [
          "name"
        ]
      },
      "arg5": {
        "current_type": "bool",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.MidiMap.send_feedback_for_parameter": {
    "signature": "send_feedback_for_parameter( (int)arg1, (DeviceParameter)arg2) -> None :",
    "cpp_signature": "void send_feedback_for_parameter(unsigned int,TPyHandle<ATimeableValue>)",
    "args": {
      "arg1": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg2": {
        "current_type": "DeviceParameter",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.PluginDevice.PluginDevice.is_using_compare_preset_b": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors."
  },
  "Live.RackDevice.RackDevice.View.selected_chain": {
    "probed_type": "NoneType",
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Return access to the currently selected chain."
  },
  "Live.RackDevice.RackDevice.copy_pad": {
    "description": "Copies all contents of a drum pad from a source pad into a destination pad. copy_pad(source_index, destination_index) where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack. Throws an exception when the source pad is empty, or when the source or destination indices are not between 0 - 127.",
    "signature": "copy_pad( (RackDevice)arg1, (int)arg2, (int)arg3) -> None :",
    "cpp_signature": "void copy_pad(TRackDevicePyHandle,int,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.RackDevice.RackDevice.insert_chain": {
    "description": "Inserts a new chain, either at the specified index or, if not index was specified, at the end of the chain sequence.",
    "signature": "insert_chain( (RackDevice)arg1 [, (int)Index=-1]) -> LomObject :",
    "cpp_signature": "TWeakPtr<TPyHandleBase> insert_chain(TRackDevicePyHandle [,int=-1])",
    "returns": {
      "current_type": "LomObject",
      "needs": [
        "type"
      ]
    }
  },
  "Live.RackDevice.RackDevice.is_using_compare_preset_b": {
    "probed_type": null,
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors."
  },
  "Live.Sample.Sample.slices": {
    "probed_type": "tuple",
    "needs": [
      "element_repr"
    ],
    "raw_doc": "Access to the list of slice points in sample time in the sample."
  },
  "Live.Scene.Scene.color_index": {
    "probed_type": "NoneType",
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Get/set access to the color index of the scene. Can be None for no color."
  },
  "Live.Scene.Scene.set_fire_button_state": {
    "description": "Set the scene's fire button state directly. Supports all launch modes.",
    "signature": "set_fire_button_state( (Scene)arg1, (bool)arg2) -> None :",
    "cpp_signature": "void set_fire_button_state(TPyHandle<AScene>,bool)",
    "args": {
      "arg2": {
        "current_type": "bool",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.View.detail_clip": {
    "probed_type": "NoneType",
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Get/Set the Clip that is currently visible in Lives Detailview."
  },
  "Live.Song.Song.View.select_device": {
    "description": "Select the given device.",
    "signature": "select_device( (View)arg1, (Device)arg2 [, (bool)ShouldAppointDevice=True]) -> None :",
    "cpp_signature": "void select_device(TPyViewData<ASong>,TPyHandle<ADevice> [,bool=True])",
    "args": {
      "arg2": {
        "current_type": "Device",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.View.selected_chain": {
    "probed_type": "NoneType",
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Get the highlighted chain if available."
  },
  "Live.Song.Song.View.selected_parameter": {
    "probed_type": "NoneType",
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Get the currently selected device parameter."
  },
  "Live.Song.Song.appointed_device": {
    "probed_type": "NoneType",
    "needs": [
      "probed_type"
    ],
    "raw_doc": "Read, write, and listen access to the appointed Device"
  },
  "Live.Song.Song.create_audio_track": {
    "description": "Create a new audio track at the optional given index and return it.If the index is -1,\nthe new track is added at the end. It will create a default audio track if possible.\nIf the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item",
    "signature": "create_audio_track( (Song)arg1 [, (object)Index=None]) -> Track :",
    "cpp_signature": "TWeakPtr<TTrackPyHandle> create_audio_track(TPyHandle<ASong> [,boost::python::api::object=None])",
    "args": {
      "index": {
        "current_type": "object",
        "needs": [
          "type"
        ]
      }
    }
  },
  "Live.Song.Song.create_midi_track": {
    "description": "Create a new midi track at the optional given index and return it.If the index is -1,\nthe new track is added at the end.It will create a default midi track if possible.\nIf the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item",
    "signature": "create_midi_track( (Song)arg1 [, (object)Index=None]) -> Track :",
    "cpp_signature": "TWeakPtr<TTrackPyHandle> create_midi_track(TPyHandle<ASong> [,boost::python::api::object=None])",
    "args": {
      "index": {
        "current_type": "object",
        "needs": [
          "type"
        ]
      }
    }
  },
  "Live.Song.Song.create_scene": {
    "description": "Create a new scene at the given index. If the index is -1,\nthe new scene is added at the end. If the index is invalid or\nthe new scene would exceed the limitations, a limitation error is raised.",
    "signature": "create_scene( (Song)arg1, (int)arg2) -> Scene :",
    "cpp_signature": "TWeakPtr<TPyHandle<AScene>> create_scene(TPyHandle<ASong>,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.delete_return_track": {
    "description": "Delete the return track with the given index. If no track with this index\nexists, an exception will be raised.",
    "signature": "delete_return_track( (Song)arg1, (int)arg2) -> None :",
    "cpp_signature": "void delete_return_track(TPyHandle<ASong>,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.delete_scene": {
    "description": "Delete the scene with the given index. If no scene with this index\nexists, an exception will be raised.",
    "signature": "delete_scene( (Song)arg1, (int)arg2) -> None :",
    "cpp_signature": "void delete_scene(TPyHandle<ASong>,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.delete_track": {
    "description": "Delete the track with the given index. If no track with this index\nexists, an exception will be raised.",
    "signature": "delete_track( (Song)arg1, (int)arg2) -> None :",
    "cpp_signature": "void delete_track(TPyHandle<ASong>,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.duplicate_scene": {
    "description": "Duplicates a scene and selects the new one.\nRaises a limitation error if creating a new scene would exceed the limitations.",
    "signature": "duplicate_scene( (Song)arg1, (int)arg2) -> None :",
    "cpp_signature": "void duplicate_scene(TPyHandle<ASong>,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.duplicate_track": {
    "description": "Duplicates a track and selects the new one.\nIf the track is inside a folded group track, the group track is unfolded.\nRaises a limitation error if creating a new track would exceed the limitations.",
    "signature": "duplicate_track( (Song)arg1, (int)arg2) -> None :",
    "cpp_signature": "void duplicate_track(TPyHandle<ASong>,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.find_device_position": {
    "description": "Returns the closest possible position to the given target, where the\ndevice can be inserted. If inserting is not possible at all (i.e. if\nthe device type is wrong), -1 is returned.",
    "signature": "find_device_position( (Song)arg1, (Device)device, (LomObject)target, (int)target_position) -> int :",
    "cpp_signature": "int find_device_position(TPyHandle<ASong>,TPyHandle<ADevice>,TPyHandleBase,int)",
    "args": {
      "target": {
        "current_type": "LomObject",
        "needs": [
          "type"
        ]
      }
    }
  },
  "Live.Song.Song.get_current_smpte_song_time": {
    "description": "Get const access to the songs current playing position, by specifying\nthe SMPTE format in which you would like to receive the time.",
    "signature": "get_current_smpte_song_time( (Song)arg1, (int)arg2) -> SmptTime :",
    "cpp_signature": "NSongApi::TSmptTime get_current_smpte_song_time(TPyHandle<ASong>,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.get_data": {
    "description": "Get data for the given key, that was previously stored using set_data.",
    "signature": "get_data( (Song)arg1, (object)key, (object)default_value) -> object :",
    "cpp_signature": "boost::python::api::object get_data(TPyHandle<ASong>,TString,boost::python::api::object)",
    "args": {
      "default_value": {
        "current_type": "object",
        "needs": [
          "type"
        ]
      }
    },
    "returns": {
      "current_type": "object",
      "needs": [
        "type"
      ]
    }
  },
  "Live.Song.Song.jump_by": {
    "description": "Set a new playing pos, relative to the current one.",
    "signature": "jump_by( (Song)arg1, (float)arg2) -> None :",
    "cpp_signature": "void jump_by(TPyHandle<ASong>,double)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.move_device": {
    "description": "Move a device into the target at the given position, where 0 moves it before the first device and len(devices) moves it to the end of the device chain.If the device cannot be moved to this position, the nearest possible position is chosen. If the device type is not valid, a runtime error is raised.Returns the index, where the device was moved to.",
    "signature": "move_device( (Song)arg1, (Device)device, (LomObject)target, (int)target_position) -> int :",
    "cpp_signature": "int move_device(TPyHandle<ASong>,TPyHandle<ADevice>,TPyHandleBase,int)",
    "args": {
      "target": {
        "current_type": "LomObject",
        "needs": [
          "type"
        ]
      }
    }
  },
  "Live.Song.Song.scrub_by": {
    "description": "Same as jump_by, but does not stop playback.",
    "signature": "scrub_by( (Song)arg1, (float)arg2) -> None :",
    "cpp_signature": "void scrub_by(TPyHandle<ASong>,double)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Song.Song.set_data": {
    "description": "Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.",
    "signature": "set_data( (Song)arg1, (object)key, (object)value) -> None :",
    "cpp_signature": "void set_data(TPyHandle<ASong>,TString,boost::python::api::object)",
    "args": {
      "value": {
        "current_type": "object",
        "needs": [
          "type"
        ]
      }
    }
  },
  "Live.Song.get_all_scales_ordered": {
    "description": "Get an ordered tuple of tuples of all available scale names to intervals.",
    "signature": "get_all_scales_ordered() -> tuple :",
    "cpp_signature": "boost::python::tuple get_all_scales_ordered()",
    "returns": {
      "current_type": "tuple",
      "needs": [
        "type"
      ]
    }
  },
  "Live.TakeLane.TakeLane.create_audio_clip": {
    "description": "Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.",
    "signature": "create_audio_clip( (TakeLane)arg1, (object)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TPyHandle<ATakeLane>,TString,double)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "float",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.TakeLane.TakeLane.create_midi_clip": {
    "description": "Creates an empty MIDI clip and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.",
    "signature": "create_midi_clip( (TakeLane)arg1, (float)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_midi_clip(TPyHandle<ATakeLane>,double,double)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "float",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Track.Track.create_audio_clip": {
    "description": "Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.",
    "signature": "create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)",
    "args": {
      "arg2": {
        "current_type": "str",
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "float",
        "needs": [
          "name"
        ]
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
        "needs": [
          "name"
        ]
      },
      "arg3": {
        "current_type": "float",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Track.Track.create_take_lane": {
    "description": "Create a new TakeLane for this track.",
    "signature": "create_take_lane( (Track)arg1) -> LomObject :",
    "cpp_signature": "TWeakPtr<TPyHandleBase> create_take_lane(TTrackPyHandle)",
    "returns": {
      "current_type": "LomObject",
      "needs": [
        "type"
      ]
    }
  },
  "Live.Track.Track.duplicate_clip_slot": {
    "description": "Duplicate a clip and put it into the next free slot and return the index\nof the destination slot. A new scene is created if no free slot is\navailable. If creating the new scene would exceed the limitations,\na runtime error is raised.",
    "signature": "duplicate_clip_slot( (Track)arg1, (int)arg2) -> int :",
    "cpp_signature": "int duplicate_clip_slot(TTrackPyHandle,int)",
    "args": {
      "arg2": {
        "current_type": "int",
        "needs": [
          "name"
        ]
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
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Track.Track.get_data": {
    "description": "Get data for the given key, that was previously stored using set_data.",
    "signature": "get_data( (Track)arg1, (object)key, (object)default_value) -> object :",
    "cpp_signature": "boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object)",
    "args": {
      "default_value": {
        "current_type": "object",
        "needs": [
          "type"
        ]
      }
    },
    "returns": {
      "current_type": "object",
      "needs": [
        "type"
      ]
    }
  },
  "Live.Track.Track.insert_device": {
    "description": "Add a device at a given index in the 'devices' list. At end if -1.",
    "signature": "insert_device( (Track)arg1, (str)DeviceName [, (int)DeviceIndex=-1]) -> LomObject :",
    "cpp_signature": "TWeakPtr<TPyHandleBase> insert_device(TTrackPyHandle,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> [,int=-1])",
    "returns": {
      "current_type": "LomObject",
      "needs": [
        "type"
      ]
    }
  },
  "Live.Track.Track.jump_in_running_session_clip": {
    "description": "Jump forward or backward in the currently running Sessionclip (if any)\nby the specified relative amount in beats. Does nothing if no Session Clip\nis currently running.",
    "signature": "jump_in_running_session_clip( (Track)arg1, (float)arg2) -> None :",
    "cpp_signature": "void jump_in_running_session_clip(TTrackPyHandle,double)",
    "args": {
      "arg2": {
        "current_type": "float",
        "needs": [
          "name"
        ]
      }
    }
  },
  "Live.Track.Track.set_data": {
    "description": "Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.",
    "signature": "set_data( (Track)arg1, (object)key, (object)value) -> None :",
    "cpp_signature": "void set_data(TTrackPyHandle,TString,boost::python::api::object)",
    "args": {
      "value": {
        "current_type": "object",
        "needs": [
          "type"
        ]
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
  "Live.Scene.Scene.set_fire_button_state": {
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
  "Live.MaxDevice.MaxDevice.get_bank_name": {
    "args": {
      "arg2": {
        "call_site_names": [
          "bank_index",
          "mx_index"
        ],
        "_votes": {
          "bank_index": 1,
          "mx_index": 1
        },
        "_total_sites": 4
      }
    }
  },
  "Live.MaxDevice.MaxDevice.get_bank_parameters": {
    "args": {
      "arg2": {
        "call_site_names": [
          "mx_index",
          "bank_index"
        ],
        "_votes": {
          "bank_index": 1,
          "mx_index": 2
        },
        "_total_sites": 5
      }
    }
  },
  "Live.MidiMap.forward_midi_cc": {
    "args": {
      "arg1": {
        "call_site_names": [
          "script_handle",
          "handle"
        ],
        "_votes": {
          "script_handle": 11,
          "handle": 3
        },
        "_total_sites": 14
      },
      "arg2": {
        "call_site_names": [
          "midi_map_handle"
        ],
        "_votes": {
          "midi_map_handle": 14
        },
        "_total_sites": 14
      },
      "arg3": {
        "call_site_names": [
          "channel",
          "chan"
        ],
        "_votes": {
          "chan": 3,
          "channel": 6
        },
        "_total_sites": 14
      },
      "arg4": {
        "call_site_names": [
          "cc",
          "cc_no"
        ],
        "_votes": {
          "cc": 3,
          "cc_no": 3
        },
        "_total_sites": 14
      }
    }
  },
  "Live.MidiMap.forward_midi_note": {
    "args": {
      "arg1": {
        "call_site_names": [
          "handle",
          "script_handle"
        ],
        "_votes": {
          "script_handle": 3,
          "handle": 4
        },
        "_total_sites": 7
      },
      "arg2": {
        "call_site_names": [
          "midi_map_handle"
        ],
        "_votes": {
          "midi_map_handle": 7
        },
        "_total_sites": 7
      },
      "arg3": {
        "call_site_names": [
          "chan"
        ],
        "_votes": {
          "chan": 3
        },
        "_total_sites": 7
      },
      "arg4": {
        "call_site_names": [
          "note"
        ],
        "_votes": {
          "note": 3
        },
        "_total_sites": 7
      }
    }
  },
  "Live.MidiMap.forward_midi_pitchbend": {
    "args": {
      "arg1": {
        "call_site_names": [
          "script_handle"
        ],
        "_votes": {
          "script_handle": 2
        },
        "_total_sites": 2
      },
      "arg2": {
        "call_site_names": [
          "midi_map_handle"
        ],
        "_votes": {
          "midi_map_handle": 2
        },
        "_total_sites": 2
      },
      "arg3": {
        "call_site_names": [
          "channel"
        ],
        "_votes": {
          "channel": 2
        },
        "_total_sites": 2
      }
    }
  },
  "Live.MidiMap.map_midi_note_with_feedback_map": {
    "args": {
      "arg1": {
        "call_site_names": [
          "midi_map_handle"
        ],
        "_votes": {
          "midi_map_handle": 1
        },
        "_total_sites": 1
      },
      "arg2": {
        "call_site_names": [
          "parameter"
        ],
        "_votes": {
          "parameter": 1
        },
        "_total_sites": 1
      },
      "arg3": {
        "call_site_names": [
          "message_channel"
        ],
        "_votes": {
          "message_channel": 1
        },
        "_total_sites": 1
      },
      "arg4": {
        "call_site_names": [
          "message_identifier"
        ],
        "_votes": {
          "message_identifier": 1
        },
        "_total_sites": 1
      },
      "arg5": {
        "call_site_names": [
          "feedback_rule"
        ],
        "_votes": {
          "feedback_rule": 1
        },
        "_total_sites": 1
      }
    }
  },
  "Live.MidiMap.map_midi_pitchbend_with_feedback_map": {
    "args": {
      "arg1": {
        "call_site_names": [
          "midi_map_handle"
        ],
        "_votes": {
          "midi_map_handle": 5
        },
        "_total_sites": 5
      },
      "arg2": {
        "call_site_names": [
          "volume",
          "parameter"
        ],
        "_votes": {
          "parameter": 1,
          "volume": 2
        },
        "_total_sites": 5
      },
      "arg3": {
        "call_site_names": [
          "message_channel"
        ],
        "_votes": {
          "message_channel": 1
        },
        "_total_sites": 5
      },
      "arg4": {
        "call_site_names": [
          "feeback_rule",
          "feedback_rule"
        ],
        "_votes": {
          "feedback_rule": 1,
          "feeback_rule": 4
        },
        "_total_sites": 5
      }
    }
  },
  "Live.MidiMap.send_feedback_for_parameter": {
    "args": {
      "arg1": {
        "call_site_names": [
          "midi_map_handle"
        ],
        "_votes": {
          "midi_map_handle": 8
        },
        "_total_sites": 8
      },
      "arg2": {
        "call_site_names": [
          "parameter",
          "volume"
        ],
        "_votes": {
          "parameter": 2,
          "volume": 2
        },
        "_total_sites": 8
      }
    }
  },
  "Live.RackDevice.RackDevice.copy_pad": {
    "args": {
      "arg2": {
        "call_site_names": [
          "note"
        ],
        "_votes": {
          "note": 2
        },
        "_total_sites": 2
      },
      "arg3": {
        "call_site_names": [
          "note"
        ],
        "_votes": {
          "note": 2
        },
        "_total_sites": 2
      }
    }
  },
  "Live.Song.Song.View.select_device": {
    "args": {
      "arg2": {
        "call_site_names": [
          "device_to_select",
          "device",
          "lom_object"
        ],
        "_votes": {
          "lom_object": 1,
          "device": 2,
          "device_to_select": 3
        },
        "_total_sites": 6
      }
    }
  },
  "Live.Song.Song.create_scene": {
    "args": {
      "arg2": {
        "call_site_names": [
          "scene_count",
          "new_scene_index"
        ],
        "_votes": {
          "new_scene_index": 2,
          "scene_count": 4
        },
        "_total_sites": 8
      }
    }
  },
  "Live.Song.Song.delete_return_track": {
    "args": {
      "arg2": {
        "call_site_names": [
          "track_index"
        ],
        "_votes": {
          "track_index": 1
        },
        "_total_sites": 2
      }
    }
  },
  "Live.Song.Song.delete_scene": {
    "args": {
      "arg2": {
        "call_site_names": [
          "selected_scene_index"
        ],
        "_votes": {
          "selected_scene_index": 1
        },
        "_total_sites": 2
      }
    }
  },
  "Live.Song.Song.delete_track": {
    "args": {
      "arg2": {
        "call_site_names": [
          "track_index"
        ],
        "_votes": {
          "track_index": 1
        },
        "_total_sites": 2
      }
    }
  },
  "Live.Song.Song.duplicate_scene": {
    "args": {
      "arg2": {
        "call_site_names": [
          "index"
        ],
        "_votes": {
          "index": 1
        },
        "_total_sites": 2
      }
    }
  },
  "Live.Song.Song.duplicate_track": {
    "args": {
      "arg2": {
        "call_site_names": [
          "track_index"
        ],
        "_votes": {
          "track_index": 2
        },
        "_total_sites": 3
      }
    }
  },
  "Live.Song.Song.get_current_smpte_song_time": {
    "args": {
      "arg2": {
        "call_site_names": [
          "smpte_25"
        ],
        "_votes": {
          "smpte_25": 1
        },
        "_total_sites": 3
      }
    }
  },
  "Live.Song.Song.jump_by": {
    "args": {
      "arg2": {
        "call_site_names": [
          "beats"
        ],
        "_votes": {
          "beats": 2
        },
        "_total_sites": 10
      }
    }
  },
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
          "target_index": 2,
          "index": 3,
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
  "Live.Track.Track.insert_device": {
    "unresolved_return_type": "LomObject"
  },
  "Live.Licensing.PythonLicensingBridge.get_startup_dialog": {
    "unresolved_arg_types": {
      "authorize_callable": "object",
      "authorize_later_callable": "object"
    }
  },
  "Live.Licensing.PythonLicensingBridge.process_license_response": {
    "unresolved_arg_types": {
      "license_response_lines": "list"
    }
  },
  "Live.Licensing.PythonLicensingBridge.set_network_timer": {
    "unresolved_arg_types": {
      "callback": "object"
    }
  },
  "Live.Licensing.get_unlock_dir": {
    "unresolved_return_type": "tuple"
  },
  "Live.Listener.ListenerHandle.name": {
    "usage_snippets": [
      "display[index % NUM_DISPLAY_SEGMENTS] = item.item.name if item else \"\"",
      "fullname = self.helper.device_name(device) + \".\" + parameter.name",
      "if device.name in FIVETOSIX_DICT:",
      "if i.name == name:",
      "name=(\"{}_With_Shift\".format(button.name)))",
      "return FIVETOSIX_DICT[device.name]",
      "return device.name",
      "self.log(\"device %s, index %s, parameter %s\" % (self.device, idx, parameter.name))",
      "self.logfmt(\"parameter %s %s to %s (quant %s)\", parameter, parameter.name, ccs[encoder], parameter.is_quantized)",
      "self.parent.show_message(str(self.device.name + \" Bank: \" + bank_name))"
    ],
    "unresolved_property_type": true
  },
  "Live.Listener.ListenerVector": {
    "needs_element_repr": true
  },
  "Live.MaxDevice.MaxDevice.get_bank_parameters": {
    "usage_snippets": [
      "indices = self.device.get_bank_parameters(mx_index)",
      "main_bank = device.get_bank_parameters(MX_MAIN_BANK_INDEX)",
      "parameter_indices = device.get_bank_parameters(-1)",
      "parameter_indices = device.get_bank_parameters(bank_index)"
    ],
    "unresolved_return_type": "list"
  },
  "Live.MaxDevice.MaxDevice.get_value_item_icons": {
    "usage_snippets": [
      "custom_images = device.get_value_item_icons(getattr(self._adaptee, \"original_parameter\", self._adaptee))"
    ],
    "unresolved_return_type": "list"
  },
  "Live.MidiMap.CCFeedbackRule.cc_value_map": {
    "usage_snippets": [
      "feeback_rule.cc_value_map = tuple([self._ChannelStrip__v_pot_display_mode * 16 + x for x in range(1, range_end)])",
      "feedback_rule.cc_value_map = (0, )",
      "feedback_rule.cc_value_map = feedback_map",
      "feedback_rule.cc_value_map = tuple()",
      "feedback_rule.cc_value_map = tuple([int(1.5 + float(index) / 127.0 * 10.0) for index in range(128)])",
      "feedback_rule.cc_value_map = tuple([int(1.5 + old_div(float(index), 127.0) * 10.0) for index in range(128)])"
    ],
    "needs_element_repr": true
  },
  "Live.MidiMap.NoteFeedbackRule.vel_map": {
    "usage_snippets": [
      "feedback_rule.vel_map = (0, )",
      "feedback_rule.vel_map = feedback_map"
    ],
    "needs_element_repr": true
  },
  "Live.MidiMap.PitchBendFeedbackRule.value_pair_map": {
    "usage_snippets": [
      "feeback_rule.value_pair_map = tuple()",
      "feedback_rule.value_pair_map = feedback_map"
    ],
    "needs_element_repr": true
  },
  "Live.RackDevice.RackDevice.View.selected_chain": {
    "usage_snippets": [
      "chain = drum_rack_for_pad(drum_pad).view.selected_chain",
      "chain = rack.view.selected_chain",
      "if left_device.can_have_chains and left_device.view.is_showing_chain_devices and left_device.view.selected_chain:",
      "if right_device.can_have_chains and right_device.view.is_showing_chain_devices and right_device.view.selected_chain:",
      "lom_object.canonical_parent.view.selected_chain = lom_object",
      "return self._rack.view.selected_chain",
      "selected_chain = self._view.selected_chain",
      "self._rack.view.selected_chain = chain",
      "self._view.selected_chain = unwrapped_track",
      "unwrapped_track.canonical_parent.view.selected_chain = unwrapped_track"
    ],
    "unresolved_property_type": true
  },
  "Live.Song.Song.View.selected_chain": {
    "usage_snippets": [
      "chain = drum_rack_for_pad(drum_pad).view.selected_chain",
      "chain = rack.view.selected_chain",
      "if left_device.can_have_chains and left_device.view.is_showing_chain_devices and left_device.view.selected_chain:",
      "if right_device.can_have_chains and right_device.view.is_showing_chain_devices and right_device.view.selected_chain:",
      "lom_object.canonical_parent.view.selected_chain = lom_object",
      "return self._rack.view.selected_chain",
      "selected_chain = self._view.selected_chain",
      "self._rack.view.selected_chain = chain",
      "self._view.selected_chain = unwrapped_track",
      "unwrapped_track.canonical_parent.view.selected_chain = unwrapped_track"
    ],
    "unresolved_property_type": true
  },
  "Live.RackDevice.RackDevice.insert_chain": {
    "unresolved_return_type": "LomObject"
  },
  "Live.Sample.Sample.slices": {
    "usage_snippets": [
      "def slices(self):",
      "if slice_index + 1 < len(positions.slices):",
      "is_active=(lambda: sample_available() and len(self._live_object.sample.slices) > 1))",
      "next_pos = max(positions.slices[slice_index + 1].time, positions.selected_slice.time + min_visible_length)",
      "return self._simpler.sample.slices",
      "selected_slice_index = self._simpler.sample.slices.index(self._simpler.view.selected_slice)",
      "self.slices = [SlicePoint(s, self._convert_sample_time(s)) for s in self._simpler.sample.slices]",
      "slice_times = self._adaptee.sample.slices",
      "slices = list(sample.slices) + [sample.end_marker]",
      "slices = self._live_object.sample.slices"
    ],
    "needs_element_repr": true
  },
  "Live.Scene.Scene.color_index": {
    "usage_snippets": [
      "button.color_index = COLOR_CHOOSER_LAYOUT[row][column]",
      "color_index = button.color_index",
      "if button.color_index is None:",
      "if obj.color_index is not None:",
      "return IndexedColor.from_live_index(chain.color_index, DISPLAY_BUTTON_SHADE_LEVEL)",
      "return LIVE_COLOR_INDEX_TO_RGB.get(obj.color_index, 0)",
      "return translate_color_index(slot_or_clip.color_index)",
      "self._render_color_palette(translate_color_index(obj.color_index))",
      "self.object.color_index = inverse_translate_color_index(button.color_index)",
      "self.source_color_index = color_source.color_index if (color_source and color_source.color_index is not None) else UNCOLORED_INDEX"
    ],
    "unresolved_property_type": true
  },
  "Live.Song.Song.View.detail_clip": {
    "usage_snippets": [
      "clip = self.song.view.detail_clip",
      "clip = self.song.view.detail_clip if self.is_enabled() else None",
      "clip = view.detail_clip",
      "if liveobj_changed(song.view.detail_clip, clip_slot.clip):",
      "self.selected_clip = self.parent.song().view.detail_clip",
      "self.set_detail_clip(self.song.view.detail_clip)",
      "song.view.detail_clip = clip_slot.clip",
      "song.view.detail_clip = selected_slot.clip",
      "song_view.detail_clip = track.duplicate_clip_to_arrangement(clip, clip.end_time)",
      "view.detail_clip = view.highlighted_clip_slot.clip"
    ],
    "unresolved_property_type": true
  },
  "Live.Song.Song.appointed_device": {
    "usage_snippets": [
      "if not self._EffectController__parent.song().appointed_device == self._EffectController__assigned_device:",
      "if not self._Encoders__parent.song().appointed_device == self._Encoders__selected_device:",
      "if not self.parent.song().appointed_device == self.device:",
      "if self._appointed_device != self._song.appointed_device:",
      "self._EffectController__change_assigned_device(self._EffectController__parent.song().appointed_device)",
      "self._song.appointed_device = device",
      "self._update_appointed_device(self._song.appointed_device)",
      "self.device = self.parent.song().appointed_device",
      "self.song.appointed_device = appointed_device",
      "song.appointed_device = appointed_device"
    ],
    "unresolved_property_type": true
  },
  "Live.Song.Song.create_audio_track": {
    "usage_snippets": [
      "song.create_audio_track()"
    ],
    "unresolved_arg_types": {
      "index": "object"
    }
  },
  "Live.Song.Song.create_midi_track": {
    "usage_snippets": [
      "song.create_midi_track()"
    ],
    "unresolved_arg_types": {
      "index": "object"
    }
  },
  "Live.Song.Song.find_device_position": {
    "unresolved_arg_types": {
      "target": "LomObject"
    }
  },
  "Live.Song.Song.get_data": {
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
  "Live.Song.Song.move_device": {
    "usage_snippets": [
      "if not self.move_device.is_enabled():",
      "return self.move_device.is_enabled()",
      "self.move_device = MoveDeviceComponent(parent=self, is_enabled=False)",
      "self.move_device = None",
      "self.move_device.set_device(device)",
      "self.move_device.set_enabled(True)",
      "self.song.move_device(self._device, chain, len(chain.devices) if move_to_end else 0)",
      "self.song.move_device(self._device, parent, device_index + 2)",
      "self.song.move_device(self._device, parent, device_index - 1)",
      "self.song.move_device(self._device, parent, rack_index + 1 if move_behind else rack_index)"
    ],
    "unresolved_arg_types": {
      "target": "LomObject"
    }
  },
  "Live.Song.Song.set_data": {
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
  },
  "Live.Song.get_all_scales_ordered": {
    "usage_snippets": [
      "SCALES = tuple([Scale(name=(x[0]), notes=(x[1])) for x in Live.Song.get_all_scales_ordered()])"
    ],
    "unresolved_return_type": "tuple"
  },
  "Live.Track.Track.create_take_lane": {
    "unresolved_return_type": "LomObject"
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

###### name symbol observe

This is the string shown in the title bar of the device.

###### is_using_compare_preset_b bool observe

1 if the device has compare preset B loaded. 0 otherwise.   
(Only relevant if *can_compare_ab*, otherwise errors.)   
  
*Available since Live 12.3.*

##### Functions

### looperdevice.md

#### LooperDevice

This class represents an instance of a Looper device in Live.   
An LooperDevice has all the properties, functions and children of a Device. Listed below are members unique to LooperDevice.

##### Properties

###### export_to_clip_slot

Parameter: `clip_slot` [ClipSlot]   
The target clip slot.   
  
Given a valid LOM ID of an empty clip slot on a non-frozen audio track, will export Looper's content to a clip in that slot. This is similar to using the Drag Me! control on the Looper device, and the same restrictions apply: the audio engine must be turned on, the Looper must actually hold audio content, the content must have a fixed length (i.e. Looper must not be recording), etc.

### maxdevice.md

#### MaxDevice

This class represents a Max for Live device in Live.   
  
A MaxDevice is a type of Device, meaning that it has all the children, properties and functions that a Device has. Listed below are the members unique to MaxDevice.

##### Properties

###### get_bank_name

Parameters: `bank_index` [int]   
Returns: [list of symbols] The name of the parameter bank specified by bank_index.

###### get_bank_parameters

Parameters: `bank_index` [int]   
Returns: [list of ints] The indices of the parameters contained in the bank specified by bank_index. Empty slots are marked as -1. Bank index -1 refers to the "Best of" bank.

### rackdevice.md

#### RackDevice

This class represents a Live Rack Device.   
A RackDevice is a type of Device, meaning that it has all the children, properties and functions that a Device has. Listed below are members unique to RackDevice.

##### Children

###### copy_pad

Parameters:   
`source_index` [int]   
`destination_index` [int]   
Copies all content of a Drum Rack pad from a source pad to a destination pad. The source_index and destination_index refer to pad indices inside a Drum Rack.

###### insert_chain

Parameters: `index` [int] (optional)   
  
Attempts to insert a new chain at the given index, or at the end of the chain list if no index is provided. Throws an error if insertion is not possible.   
Side note: A chain inserted into a Drum Rack will have an initial MIDI In Note setting of "All Notes" (see `DrumChain.in_note`). You likely want the chain to be triggered when a specific pad is played; the way to achieve this is to set the `in_note` to the note value that corresponds to the pad.   
  
*Available since Live 12.3.*

### rackdevice_view.md

#### RackDevice.View

Represents the view aspects of a Rack Device.   
A RackDevice.View is a type of Device.View, meaning that it has all the properties that a Device.View has. Listed below are the members unique to RackDevice.View.

##### Children

###### selected_chain [Chain](/apiref/lom/chain/ "Chain") observe

Currently selected chain.

##### Properties

### sample.md

#### Sample

This class represents a sample file loaded into Simpler.

##### Canonical Path

```
live_set tracks N devices N sample
```

##### Properties

###### slices list of int read-onlyobserve

The positions of all playable slices in the sample, in sample frames. Divide these values by the `sample_rate` to get the slice times in seconds.   
  
*Available since Live 11.0.*

### scene.md

#### Scene

This class represents a series of clip slots in Live's Session View matrix.

##### Canonical Path

```
live_set scenes N
```

##### Children

###### color_index long observe

The color index of the scene.

###### name symbol observe

The name of the scene.

###### set_fire_button_state

Parameter: `state` [bool]   
If the state is set to 1, Live simulates pressing of scene button until the state is set to 0 or until the scene is stopped otherwise.

### song.md

#### Song

This class represents a Live Set. The current Live Set is reachable by the root path `live_set`.

##### Canonical Path

```
live_set
```

##### Children

###### appointed_device [Device](/apiref/lom/device/ "Device") read-onlyobserve

The appointed device is the one used by a control surface unless the control surface itself chooses which device to use. It is marked by a blue hand.

###### name symbol read-only

The name of the current Live Set. If the Live Set hasn't been saved, the name is empty.

###### create_audio_track

Parameter: `index`  
Index determines where the track is added, it is only valid between 0 and len(song.tracks). Using an index of -1 will add the new track at the end of the list.

###### create_midi_track

Parameter: `index`  
Index determines where the track is added, it is only valid between 0 and len(song.tracks). Using an index of -1 will add the new track at the end of the list.

###### create_scene

Parameter: `index`  
Returns: The new scene   
Index determines where the scene is added. It is only valid between 0 and len(song.scenes). Using an index of -1 will add the new scene at the end of the list.

###### delete_scene

Parameter: `index`  
Delete the scene at the given index.

###### delete_track

Parameter: `index`  
Delete the track at the given index.

###### delete_return_track

Parameter: `index`  
Delete the return track at the given index.

###### duplicate_scene

Parameter: `index`  
Index determines which scene to duplicate.

###### duplicate_track

Parameter: `index`  
Index determines which track to duplicate.

###### find_device_position

Parameter:   
`device` [live object]   
`target` [live object]   
`target position` [int]   
Returns:   
[int] The position in the target's chain where the device can be inserted that is the closest possible to the target position.

###### get_current_smpte_song_time

Parameter: `format`  
`format` [int] is the time code type to be returned   
0 = the frame position shows the milliseconds   
1 = Smpte24   
2 = Smpte25   
3 = Smpte30   
4 = Smpte30Drop   
5 = Smpte29   
Returns: *hours:min:sec*

[symbol]   
The current Arrangement playback position.

###### jump_by

Parameter: `beats`  
`beats` [float] is the amount to jump relatively to the current position

###### move_device

Parameter:   
`device` [live object]   
`target` [live object]   
`target position` [int]   
Returns: [int] The position in the target's chain where the device was inserted.   
Move the device to the specified position in the target chain. If the device cannot be moved to the specified position, the nearest possible position is chosen.

###### scrub_by

Parameter: `beats`  
`beats` [float] the amount to scrub relative to the current Arrangement playback position   
Same as `jump_by`, at the moment.

### song_view.md

#### Song.View

This class represents the view aspects of a Live document: the Session and Arrangement Views.

##### Canonical Path

```
live_set view
```

##### Children

###### detail_clip [Clip](/apiref/lom/clip/ "Clip") observe

The clip currently displayed in the Live application's Detail View.

###### selected_chain [Chain](/apiref/lom/chain/ "Chain") observe

The highlighted chain, or "id 0"

###### selected_parameter [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-onlyobserve

The selected parameter, or "id 0"

###### select_device

Parameter: `id NN`  
Selects the given device object in its track.   
You may obtain the id using a [live.path](/reference/live.path "live.path") or by using `get devices` on a track, for example.   
The track containing the device will not be shown automatically, and the device gets the appointed device (blue hand) only if its track is selected.

### takelane.md

#### TakeLane

This class represents a take lane in Live. Tracks in Live can have take lanes in Arrangement View, which are used for comping. If take lanes exist for a track, they can be shown by right-clicking on a track and choosing Show Take Lanes.

##### Canonical Path

```
live_set tracks N take_lanes M
```

##### Children

###### name symbol observe

The name as shown in the take lane header.

##### Functions

###### create_audio_clip

Parameters:   
`file_path` [symbol]   
`start_time` [float]   
Given a valid audio file in a supported format, passing its absolute path (on Mac, starting with `/Volumes/(drive name)/`) creates an audio clip referencing the file in the arrangement view at the specified `start_time` in beats.  
  
Prints an error if the track is not an audio track, if the track is frozen or if the track is being recorded into. `start_time` must be within the range `[0., 1576800]`.

###### create_midi_clip

Parameters:   
`start_time` [float]   
`length` [float]   
Creates an empty MIDI clip with the specified `length` in beats and inserts it into the arrangement at the specified `start_time` in beats.  
  
Prints an error if the track is not a MIDI track, if the track is frozen or when the track is currently being recorded into. `start_time` must be within the range `[0., 1576800]`.

### track.md

#### Track

This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.   
  
Not all properties are supported by all types of tracks. The properties are marked accordingly.

##### Canonical Path

```
live_set tracks N
```

##### Children

###### color_index long observe

The color index of the track.

###### name symbol observe

As shown in track header.

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

###### create_take_lane

Creates a take lane for this track.

###### duplicate_clip_slot

Parameter: `index`  
  
Works like 'Duplicate' in a clip's context menu.

###### insert_device

Parameters: `device_name` [symbol] `target_index` [int] (optional)   
  
Attempts to insert the device specified by `device_name` at the given index in the track's device chain. If no index is provided, attempts to insert the device at the end of the chain. Throws an error if insertion is not possible.   
`device_name` is the name as it appears in the UI of Live.   
Not all indices are valid. As can be expected, indices outside of the range defined by the current length of the device chain are invalid, but there are other limitations: for example, a MIDI effect can't be inserted after an instrument. The rule of thumb is that if an index would be invalid when inserting using the mouse, it's invalid here.   
  
At the moment, only native Live devices can be inserted. Max for Live devices and plug-in are not supported.   
  
*Available since Live 12.3.*

###### jump_in_running_session_clip

Parameter: `beats`  
  
`beats` [float] is the amount to jump relatively to the current clip position.   
Modify playback position in running Session clip, if any.
