## Unresolved Items

```json
[
  {
    "path": "Live.Track.DeviceContainer._live_ptr",
    "kind": "property_type",
    "current_type": null
  },
  {
    "path": "Live.Track.RoutingChannelVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "RoutingChannel",
    "signature": "append( (RoutingChannelVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<NRoutingApi::TRoutingChannel, std::__1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Track.RoutingChannelVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "RoutingChannel",
    "signature": "extend( (RoutingChannelVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<NRoutingApi::TRoutingChannel, std::__1::allocator<NRoutingApi::TRoutingChannel>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Track.RoutingTypeVector.append",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "RoutingType",
    "signature": "append( (RoutingTypeVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void append(std::__1::vector<NRoutingApi::TRoutingType, std::__1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Track.RoutingTypeVector.extend",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "RoutingType",
    "signature": "extend( (RoutingTypeVector)arg1, (object)arg2) -> None :",
    "cpp_signature": "void extend(std::__1::vector<NRoutingApi::TRoutingType, std::__1::allocator<NRoutingApi::TRoutingType>> {lvalue},boost::python::api::object)"
  },
  {
    "path": "Live.Track.Track.create_audio_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "str",
    "description": "Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.",
    "signature": "create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)"
  },
  {
    "path": "Live.Track.Track.create_audio_clip",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "float",
    "description": "Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.",
    "signature": "create_audio_clip( (Track)arg1, (object)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_audio_clip(TTrackPyHandle,TString,double)"
  },
  {
    "path": "Live.Track.Track.create_midi_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Creates an empty MIDI clip and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.",
    "signature": "create_midi_clip( (Track)arg1, (float)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_midi_clip(TTrackPyHandle,double,double)"
  },
  {
    "path": "Live.Track.Track.create_midi_clip",
    "kind": "arg_name",
    "arg_name": "arg3",
    "current_type": "float",
    "description": "Creates an empty MIDI clip and inserts it into the arrangement at the specified time.\nThrows an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.",
    "signature": "create_midi_clip( (Track)arg1, (float)arg2, (float)arg3) -> Clip :",
    "cpp_signature": "TWeakPtr<TPyHandle<AClip>> create_midi_clip(TTrackPyHandle,double,double)"
  },
  {
    "path": "Live.Track.Track.delete_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "Clip",
    "description": "Delete the given clip. Raises a runtime error when the clip belongs to another track.",
    "signature": "delete_clip( (Track)arg1, (Clip)arg2) -> None :",
    "cpp_signature": "void delete_clip(TTrackPyHandle,TPyHandle<AClip>)"
  },
  {
    "path": "Live.Track.Track.delete_device",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Delete a device identified by the index in the 'devices' list.",
    "signature": "delete_device( (Track)arg1, (int)arg2) -> None :",
    "cpp_signature": "void delete_device(TTrackPyHandle,int)"
  },
  {
    "path": "Live.Track.Track.duplicate_clip_slot",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Duplicate a clip and put it into the next free slot and return the index\nof the destination slot. A new scene is created if no free slot is\navailable. If creating the new scene would exceed the limitations,\na runtime error is raised.",
    "signature": "duplicate_clip_slot( (Track)arg1, (int)arg2) -> int :",
    "cpp_signature": "int duplicate_clip_slot(TTrackPyHandle,int)"
  },
  {
    "path": "Live.Track.Track.duplicate_device",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "int",
    "description": "Duplicate a device at a given index in the 'devices' list.",
    "signature": "duplicate_device( (Track)arg1, (int)arg2) -> None :",
    "cpp_signature": "void duplicate_device(TTrackPyHandle,int)"
  },
  {
    "path": "Live.Track.Track.get_data",
    "kind": "arg_type",
    "arg_name": "default_value",
    "current_type": "object",
    "description": "Get data for the given key, that was previously stored using set_data.",
    "signature": "get_data( (Track)arg1, (object)key, (object)default_value) -> object :",
    "cpp_signature": "boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object)"
  },
  {
    "path": "Live.Track.Track.get_data",
    "kind": "return_type",
    "current_type": "object",
    "description": "Get data for the given key, that was previously stored using set_data.",
    "signature": "get_data( (Track)arg1, (object)key, (object)default_value) -> object :",
    "cpp_signature": "boost::python::api::object get_data(TTrackPyHandle,TString,boost::python::api::object)"
  },
  {
    "path": "Live.Track.Track.jump_in_running_session_clip",
    "kind": "arg_name",
    "arg_name": "arg2",
    "current_type": "float",
    "description": "Jump forward or backward in the currently running Sessionclip (if any)\nby the specified relative amount in beats. Does nothing if no Session Clip\nis currently running.",
    "signature": "jump_in_running_session_clip( (Track)arg1, (float)arg2) -> None :",
    "cpp_signature": "void jump_in_running_session_clip(TTrackPyHandle,double)"
  },
  {
    "path": "Live.Track.Track.set_data",
    "kind": "arg_type",
    "arg_name": "value",
    "current_type": "object",
    "description": "Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.",
    "signature": "set_data( (Track)arg1, (object)key, (object)value) -> None :",
    "cpp_signature": "void set_data(TTrackPyHandle,TString,boost::python::api::object)"
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


### track.md

# Track

This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.   
  
Not all properties are supported by all types of tracks. The properties are marked accordingly.

## Canonical Path

```
live_set tracks N
```

## Children

### take_lanes list of [TakeLane](/apiref/lom/takelane/ "TakeLane") read-onlyobserve

The list of this track's take lanes

### clip_slots list of [ClipSlot](/apiref/lom/clipslot/ "ClipSlot") read-onlyobserve

### arrangement_clips list of [Clip](/apiref/lom/clip/ "Clip") read-onlyobserve

The list of this track's Arrangement View clip IDs   
  
*Available since Live 11.0.*

### devices list of [Device](/apiref/lom/device/ "Device") read-onlyobserve

Includes mixer device.

### group_track [Track](/apiref/lom/track/ "Track") read-only

The Group Track, if the Track is grouped. If it is not, *id 0* is returned.

### mixer_device [MixerDevice](/apiref/lom/mixerdevice/ "MixerDevice") read-only

### view [Track.View](/apiref/lom/track_view/ "Track.View") read-only

## Properties

### arm bool observe

1 = track is armed for recording. [not in return/master tracks]

### available_input_routing_channels dictionary read-onlyobserve

The list of available source channels for the track's input routing. It's represented as a *dictionary* with the following key:  
`available_input_routing_channels` [list]   
The list contains *dictionaries* as described in *input_routing_channel*.   
Only available on MIDI and audio tracks.

### available_input_routing_types dictionary read-onlyobserve

The list of available source types for the track's input routing. It's represented as a *dictionary* with the following key:  
`available_input_routing_types` [list]   
The list contains *dictionaries* as described in *input_routing_type*.   
Only available on MIDI and audio tracks.

### available_output_routing_channels dictionary read-onlyobserve

The list of available target channels for the track's output routing. It's represented as a *dictionary* with the following key:  
`available_output_routing_channels` [list]   
The list contains *dictionaries* as described in *output_routing_channel*.   
Not available on the master track.

### available_output_routing_types dictionary read-onlyobserve

The list of available target types for the track's output routing. It's represented as a *dictionary* with the following key:  
`available_output_routing_types` [list]   
The list contains *dictionaries* as described in *output_routing_type*.   
Not available on the master track.

### back_to_arranger bool observe

Get/set/observe the current state of the Single Track Back to Arrangement button (1 = highlighted). This button is used to indicate that the current state of the playback differs from what is stored in the Arrangement.   
  
Setting this property to 0 will make Live go back to playing the track's arrangement content. For group tracks, this means that all of the tracks that belong to the group and any subgroups will go back to playing the arrangement.

### can_be_armed bool read-only

0 for return and master tracks.

### can_be_frozen bool read-only

1 = the track can be frozen, 0 = otherwise.

### can_show_chains bool read-only

1 = the track contains an Instrument Rack device that can show chains in Session View.

### color int observe

The RGB value of the track's color in the form `0x00rrggbb` or (2^16 * red) + (2^8) * green + blue, where red, green and blue are values from 0 (dark) to 255 (light).   
  
When setting the RGB value, the nearest color from the track color chooser is taken.

### color_index long observe

The color index of the track.

### fired_slot_index int read-onlyobserve

Reflects the blinking clip slot.   
-1 = no slot fired, -2 = Clip Stop Button fired   
First clip slot has index 0.   
[not in return/master tracks]

### fold_state int

0 = tracks within the Group Track are visible, 1 = Group Track is folded and the tracks within the Group Track are hidden   
[only available if `is_foldable` = 1]

### has_audio_input bool read-only

1 for audio tracks.

### has_audio_output bool read-only

1 for audio tracks and MIDI tracks with instruments.

### has_midi_input bool read-only

1 for MIDI tracks.

### has_midi_output bool read-only

1 for MIDI tracks with no instruments and no audio effects.

### implicit_arm bool observe

A second arm state, only used by Push so far.

### input_meter_left float read-onlyobserve

Smoothed momentary peak value of left channel input meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live. Please take into account that the left/right audio meters put a significant load onto the GUI part of Live.

### input_meter_level float read-onlyobserve

Hold peak value of input meters of audio and MIDI tracks, 0.0 ... 1.0. For audio tracks it is the maximum of the left and right channels. The hold time is 1 second.

### input_meter_right float read-onlyobserve

Smoothed momentary peak value of right channel input meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live.

### input_routing_channel dictionary observe

The currently selected source channel for the track's input routing. It's represented as a *dictionary* with the following keys:  
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_input_routing_channels*.   
Only available on MIDI and audio tracks.

### input_routing_type dictionary observe

The currently selected source type for the track's input routing. It's represented as a *dictionary* with the following keys:  
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_input_routing_types*.   
Only available on MIDI and audio tracks.

### is_foldable bool read-only

1 = track can be (un)folded to hide or reveal the contained tracks. This is currently the case for Group Tracks. Instrument and Drum Racks return 0 although they can be opened/closed. This will be fixed in a later release.

### is_frozen bool read-onlyobserve

1 = the track is currently frozen.

### is_grouped bool read-only

1 = the track is contained within a Group Track.

### is_part_of_selection bool read-only

### is_showing_chains bool observe

Get or set whether a track with an Instrument Rack device is currently showing its chains in Session View.

### is_visible bool read-only

0 = track is hidden in a folded Group Track.

### mute bool observe

[not in master track]

### muted_via_solo bool read-onlyobserve

1 = the track or chain is muted due to Solo being active on at least one other track.

### name symbol observe

As shown in track header.

### output_meter_left float read-onlyobserve

Smoothed momentary peak value of left channel output meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live. Please take into account that the left/right audio meters add a significant load to Live GUI resource usage.

### output_meter_level float read-onlyobserve

Hold peak value of output meters of audio and MIDI tracks, 0.0 to 1.0. For audio tracks, it is the maximum of the left and right channels. The hold time is 1 second.

### output_meter_right float read-onlyobserve

Smoothed momentary peak value of right channel output meter, 0.0 to 1.0. For tracks with audio output only. This value corresponds to the meters shown in Live.

### performance_impact float read-onlyobserve

Reports the performance impact of this track.

### output_routing_channel dictionary observe

The currently selected target channel for the track's output routing. It's represented as a *dictionary* with the following keys:  
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_output_routing_channels*.   
Not available on the master track.

### output_routing_type dictionary observe

The currently selected target type for the track's output routing. It's represented as a *dictionary* with the following keys:  
`display_name` [symbol]   
`identifier` [symbol]   
Can be set to all values found in the track's *available_output_routing_types*.   
Not available on the master track.

### playing_slot_index int read-onlyobserve

First slot has index 0, -2 = Clip Stop slot fired in Session View, -1 = Arrangement recording with no Session clip playing. [not in return/master tracks]

### solo bool observe

Remark: when setting this property, the exclusive Solo logic is bypassed, so you have to unsolo the other tracks yourself. [not in master track]

## Functions

### create_audio_clip

Parameters:   
`file_path` [symbol]   
`position` [float]   
Given an absolute path to a valid audio file in a supported format, creates an audio clip that references the file at the specified position in the arrangement view. Prints an error if the track is not an audio track, if the track is frozen, or if the track is being recorded into. The position must be within the range [0., 1576800].   
  
See the `ClipSlot.create_audio_clip` function if you need to create audio clips in session view instead.

### create_midi_clip

Parameters:   
`start_time` [float]   
`length` [float]   
Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.   
  
See the `ClipSlot.create_clip` function if you need to create audio clips in session view instead.

### create_take_lane

Creates a take lane for this track.

### delete_clip

Parameter: `clip`  
Delete the given clip.

### delete_device

Parameter: `index`  
Delete the device at the given index.

### duplicate_clip_slot

Parameter: `index`  
  
Works like 'Duplicate' in a clip's context menu.

### duplicate_clip_to_arrangement

Parameters: ``` clip``destination_time ``` [float]   
  
Duplicate the given clip to the Arrangement, placing it at the given *destination_time* in beats.

### insert_device

Parameters: `device_name` [symbol] `target_index` [int] (optional)   
  
Attempts to insert the device specified by `device_name` at the given index in the track's device chain. If no index is provided, attempts to insert the device at the end of the chain. Throws an error if insertion is not possible.   
`device_name` is the name as it appears in the UI of Live.   
Not all indices are valid. As can be expected, indices outside of the range defined by the current length of the device chain are invalid, but there are other limitations: for example, a MIDI effect can't be inserted after an instrument. The rule of thumb is that if an index would be invalid when inserting using the mouse, it's invalid here.   
  
At the moment, only native Live devices can be inserted. Max for Live devices and plug-in are not supported.   
  
*Available since Live 12.3.*

### jump_in_running_session_clip

Parameter: `beats`  
  
`beats` [float] is the amount to jump relatively to the current clip position.   
Modify playback position in running Session clip, if any.

### stop_all_clips

Stops all playing and fired clips in this track.


### track_view.md

# Track.View

Representing the view aspects of a track.

## Canonical Path

```
live_set tracks N view
```

## Children

### selected_device [Device](/apiref/lom/device/ "Device") read-onlyobserve

The selected device or the first selected device (in case of multi/group selection).

## Properties

### device_insert_mode int observe

Determines where a device will be inserted when loaded from the browser. 0 = add device at the end, 1 = add device to the left of the selected device, 2 = add device to the right of the selected device.

### is_collapsed bool observe

In Arrangement View: 1 = track collapsed, 0 = track opened.

## Functions

### select_instrument

Returns: bool 0 = there are no devices to select   
Selects track's instrument or first device, makes it visible and focuses on it.


## Reference Documentation

These are curated API reference docs with probed function signatures, parameter names, and types. When these docs show explicit parameter names in function signatures (e.g. `load_item(item)`, `insert_step(start, length, value)`), use those names directly.

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


### reference/tracks/Track.md

# Track

> `Live.Track.Track`

This class represents a track in Live. It can either be an audio track, a MIDI track, a return track or the master
track. The master track and at least one Audio or MIDI track will be always present. Return tracks are optional.
Not all properties are supported by all types of tracks. The properties are marked accordingly.

??? note "Raw probe notes (temporary)"

    - Current probe set included `midi`, `audio`, `group`, `return`, and `master` tracks (grouped-track layout).
    - Dictionary routing members (`input_routing_type/channel`, `output_routing_type/channel`, and `available_*`) were
      readable and settable on all probed track kinds.
    - On several non-master tracks, `available_output_routing_channels` had only one option, so alternate channel
      selection was not always possible.
    - In current probes, setting track color by known palette values round-trips as expected.
    - In current probes, setting `color` to `None` raised an `InternalError` (C++ type mismatch: expected `int`).
    - In current probes, setting `color_index` to `None` returned OK but had no effect — value read back unchanged.
      Tracks always have a color in the Live UI (no "no color" option), so `None` is not a meaningful value and is
      silently discarded.
    - In current probes, `fired_slot_index` and `playing_slot_index` sentinel behavior matched documented values
      (`-2`, `-1`).
    - In current probes, `current_monitoring_state` accepted values `0`, `1`, `2`; setting `>=3` returned
      `Invalid monitoring state!`.
    - In current probes on a MIDI track, immediate read-after-set matched for `name`, `mute`, `solo`, `color_index`,
      `current_monitoring_state`, and `arm`.
    - Legacy string routing members (`current_*`, `*_routings`, `*_sub_routings`) remain in Live API for compatibility,
      but dictionary routing members are the modern replacement:
        - `current_input_routing` -> `input_routing_type`
        - `current_input_sub_routing` -> `input_routing_channel`
        - `input_routings` -> `available_input_routing_types`
        - `input_sub_routings` -> `available_input_routing_channels`
        - `current_output_routing` -> `output_routing_type`
        - `current_output_sub_routing` -> `output_routing_channel`
        - `output_routings` -> `available_output_routing_types`
        - `output_sub_routings` -> `available_output_routing_channels`

### Open Questions

- Semantic naming for `Track.monitoring_states` values (`0/1/2`) is still unconfirmed from raw docs.
- Full validity/error constraints for routing setters by track type.
- Per-member async visibility behavior for mutable track properties beyond the currently probed subset (which updates
  are immediate vs scheduler-delayed).

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `take_lanes` | `Sequence[TakeLane]` | `list` | `yes` | The list of this track's take lanes. |
| `clip_slots` | `Sequence[ClipSlot]` | `list` | `yes` | The list of clip slots for this track. Empty for main and return tracks. |
| `arrangement_clips` | `Sequence[Clip]` | `list` | `yes` | The list of this track's Arrangement View clips. |
| `devices` | `Sequence[Device]` | `list` | `yes` | Includes mixer device. |
| `group_track` | `Track` | `single` | `no` | The Group Track, if the Track is grouped. |
| `mixer_device` | `MixerDevice` | `single` | `no` | The track's mixer device (Volume, Pan, Sends, Crossfade). |
| `view` | `Track.View` | `single` | `no` | View aspects of the track. |

#### `take_lanes`

- **Returns:** `Sequence[TakeLane]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `12.2`

The list of this track's take lanes.

#### `clip_slots`

- **Returns:** `Sequence[ClipSlot]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

The list of clip slots for this track. The list will be empty for the main and return tracks.

#### `arrangement_clips`

- **Returns:** `Sequence[Clip]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `11.0`

The list of this track's Arrangement View clips. The list is empty for the main track, send/return tracks, and
group tracks.

#### `devices`

- **Returns:** `Sequence[Device]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

Includes mixer device.

#### `group_track`

- **Returns:** `Track`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

The Group Track, if the Track is grouped. If it is not, `id 0` is returned.

#### `mixer_device`

- **Returns:** `MixerDevice`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

The special Device that every Track has: contains the Volume, Pan, Send amounts, and Crossfade assignment
parameters.

#### `view`

- **Returns:** `Track.View`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

Representing the view aspects of a Track.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `arm` | `bool` | `yes` | `yes` | `True` if track is armed for recording. |
| `available_input_routing_channels` | `dictionary` | `no` | `yes` | Available source channels for input routing. |
| `available_input_routing_types` | `dictionary` | `no` | `yes` | Available source types for input routing. |
| `available_output_routing_channels` | `dictionary` | `no` | `yes` | Available target channels for output routing. |
| `available_output_routing_types` | `dictionary` | `no` | `yes` | Available target types for output routing. |
| `back_to_arranger` | `bool` | `yes` | `yes` | State of the Single Track Back to Arrangement button. |
| `can_be_armed` | `bool` | `no` | `no` | `False` for return and master tracks. |
| `can_be_frozen` | `bool` | `no` | `no` | `True` if the track can be frozen. |
| `can_show_chains` | `bool` | `no` | `no` | `True` if an Instrument Rack can show chains in Session View. |
| `canonical_parent` | `LomObject` | `no` | `no` | The canonical parent of the track. |
| `color` | `int` | `yes` | `yes` | Track color as packed RGB `0x00rrggbb`. |
| `color_index` | `int` | `yes` | `yes` | Track color palette index. |
| `current_input_routing` | `str` | `yes` | `yes` | Legacy input routing name. Prefer `input_routing_type`. |
| `current_input_sub_routing` | `str` | `yes` | `yes` | Legacy input sub-routing name. Prefer `input_routing_channel`. |
| `current_monitoring_state` | `int` | `yes` | `yes` | Monitoring state: `0`, `1`, or `2`. |
| `current_output_routing` | `str` | `yes` | `yes` | Legacy output routing name. Prefer `output_routing_type`. |
| `current_output_sub_routing` | `str` | `yes` | `yes` | Legacy output sub-routing name. Prefer `output_routing_channel`. |
| `fired_slot_index` | `int` | `no` | `yes` | Index of the blinking clip slot. |
| `fold_state` | `int` | `yes` | `no` | `0` = unfolded (children visible), `1` = folded. Group tracks only. |
| `has_audio_input` | `bool` | `no` | `no` | `True` for audio tracks. |
| `has_audio_output` | `bool` | `no` | `no` | `True` for audio tracks and MIDI tracks with instruments. |
| `has_midi_input` | `bool` | `no` | `no` | `True` for MIDI tracks. |
| `has_midi_output` | `bool` | `no` | `no` | `True` for MIDI tracks with no instruments and no audio effects. |
| `implicit_arm` | `bool` | `yes` | `yes` | A second arm state, only used by Push so far. |
| `input_meter_left` | `float` | `no` | `yes` | Smoothed left channel input meter, 0.0 to 1.0. Audio input tracks only. |
| `input_meter_level` | `float` | `no` | `yes` | Hold peak of input meter, 0.0 to 1.0. |
| `input_meter_right` | `float` | `no` | `yes` | Smoothed right channel input meter, 0.0 to 1.0. Audio input tracks only. |
| `input_routing_channel` | `dictionary` | `yes` | `yes` | Currently selected input routing source channel. |
| `input_routing_type` | `dictionary` | `yes` | `yes` | Currently selected input routing source type. |
| `input_routings` | `list[str]` | `yes` | `yes` | Legacy input routing list. Prefer `available_input_routing_types`. |
| `input_sub_routings` | `list[str]` | `yes` | `yes` | Legacy input sub-routing list. Prefer `available_input_routing_channels`. |
| `is_foldable` | `bool` | `no` | `no` | `True` if the track can be folded (Group Tracks). |
| `is_frozen` | `bool` | `no` | `yes` | `True` if the track is currently frozen. |
| `is_grouped` | `bool` | `no` | `no` | `True` if the track is inside a Group Track. |
| `is_part_of_selection` | `bool` | `no` | `no` | Unknown. |
| `is_showing_chains` | `bool` | `yes` | `yes` | Whether an Instrument Rack's chains are showing in Session View. |
| `is_visible` | `bool` | `no` | `no` | `False` if hidden in a folded Group Track. |
| `mute` | `bool` | `yes` | `yes` | Track mute state. Not available on master track. |
| `muted_via_solo` | `bool` | `no` | `yes` | `True` if muted because another track is soloed. |
| `name` | `str` | `yes` | `yes` | Track name as shown in the track header. |
| `output_meter_left` | `float` | `no` | `yes` | Smoothed left channel output meter, 0.0 to 1.0. |
| `output_meter_level` | `float` | `no` | `yes` | Hold peak of output meter, 0.0 to 1.0. |
| `output_meter_right` | `float` | `no` | `yes` | Smoothed right channel output meter, 0.0 to 1.0. |
| `output_routing_channel` | `dictionary` | `yes` | `yes` | Currently selected output routing target channel. |
| `output_routing_type` | `dictionary` | `yes` | `yes` | Currently selected output routing target type. |
| `output_routings` | `list[str]` | `yes` | `yes` | Legacy output routing list. Prefer `available_output_routing_types`. |
| `output_sub_routings` | `list[str]` | `yes` | `yes` | Legacy output sub-routing list. Prefer `available_output_routing_channels`. |
| `performance_impact` | `float` | `no` | `yes` | Performance impact of this track. |
| `playing_slot_index` | `int` | `no` | `yes` | Index of the currently playing clip slot. |
| `solo` | `bool` | `yes` | `yes` | Track solo state. Bypasses exclusive solo logic on set. |

#### `arm`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the track is armed for recording. Not available on return/master tracks.

#### `available_input_routing_channels`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available source channels for the track's input routing, as a dictionary containing a list of
dictionaries (same structure as `input_routing_channel`). Documented as MIDI/audio-only.

- **Quirks:** Current probes (Live 12.3.5) also returned this member on group, return, and master tracks.

#### `available_input_routing_types`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available source types for the track's input routing, as a dictionary containing a list of dictionaries
(same structure as `input_routing_type`). Documented as MIDI/audio-only.

- **Quirks:** Current probes (Live 12.3.5) also returned this member on group, return, and master tracks.

#### `available_output_routing_channels`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available target channels for the track's output routing, as a dictionary containing a list of
dictionaries (same structure as `output_routing_channel`). Documented as unavailable on master track.

- **Quirks:** Current probes (Live 12.3.5) returned this member on the master track as well. On several non-master
  tracks, only one output channel option was available.

#### `available_output_routing_types`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available target types for the track's output routing, as a dictionary containing a list of dictionaries
(same structure as `output_routing_type`). Documented as unavailable on master track.

- **Quirks:** Current probes (Live 12.3.5) returned this member on the master track as well.

#### `back_to_arranger`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `12.0`

Get/set the current state of the Single Track Back to Arrangement button (`1` = highlighted). Setting to `0` makes
Live go back to playing the track's arrangement content. For group tracks, this means all tracks within the group
and any subgroups will go back to playing the arrangement.

#### `can_be_armed`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`False` for return and master tracks.

#### `can_be_frozen`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the track can be frozen.

#### `can_show_chains`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the track contains an Instrument Rack device that can show chains in Session View.

#### `canonical_parent`

- **Type:** `LomObject`
- **Listenable:** `no`
- **Since:** `<11`

The canonical parent of the track.

#### `color`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The RGB value of the track's color in the form `0x00rrggbb`. When setting, Live snaps to the nearest color from
the track color chooser.

- **Quirks:** Setting to `None` raises an `InternalError` (C++ type mismatch: expected `int`).

#### `color_index`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Track color palette index. Tracks always have a color in the Live UI — there is no "no color" option.

- **Quirks:** Setting to `None` is accepted without error but silently discarded; the value remains unchanged.

#### `current_input_routing`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the name of the current active input routing. The new routing must be one of the available ones. Legacy
compatibility property. Prefer `input_routing_type`.

#### `current_input_sub_routing`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the current active input sub routing. Legacy compatibility property. Prefer `input_routing_channel`.

#### `current_monitoring_state`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The track's current monitoring state. Values `0`, `1`, and `2` are accepted.

- **Quirks:** Setting values `>=3` returns `Invalid monitoring state!`. Semantic labels for `0`/`1`/`2` are
  unconfirmed in raw docs.

#### `current_output_routing`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the current active output routing. Legacy compatibility property. Prefer `output_routing_type`.

#### `current_output_sub_routing`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Get/set the current active output sub routing. Legacy compatibility property. Prefer `output_routing_channel`.

#### `fired_slot_index`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Reflects the blinking clip slot. `-1` = no slot fired, `-2` = Clip Stop Button fired. First clip slot has index
`0`. Not available on return/master tracks.

#### `fold_state`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

`0` = tracks within the Group Track are visible, `1` = Group Track is folded and the tracks within are hidden.
Only available if `is_foldable` is `True`.

#### `has_audio_input`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for audio tracks.

#### `has_audio_output`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for audio tracks and MIDI tracks with instruments.

#### `has_midi_input`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for MIDI tracks.

#### `has_midi_output`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` for MIDI tracks with no instruments and no audio effects.

#### `implicit_arm`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

A second arm state, only used by Push so far.

#### `input_meter_left`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Smoothed momentary peak value of left channel input meter, 0.0 to 1.0. For tracks with audio input only.

#### `input_meter_level`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Hold peak value of input meters of audio and MIDI tracks, 0.0 to 1.0. For audio tracks it is the maximum of the
left and right channels. The hold time is 1 second.

#### `input_meter_right`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Smoothed momentary peak value of right channel input meter, 0.0 to 1.0. For tracks with audio input only.

#### `input_routing_channel`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected source channel for the track's input routing. A dictionary with `display_name` and
`identifier` keys. Can be set to any value from `available_input_routing_channels`. Documented as MIDI/audio-only.

- **Quirks:** Current probes (Live 12.3.5) also returned this member on group, return, and master tracks. Set/get
  round-trip succeeded across all probed track kinds.

#### `input_routing_type`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected source type for the track's input routing. A dictionary with `display_name` and `identifier`
keys. Can be set to any value from `available_input_routing_types`. Documented as MIDI/audio-only.

- **Quirks:** Current probes (Live 12.3.5) also returned this member on group, return, and master tracks. Set/get
  round-trip succeeded across all probed track kinds.

#### `input_routings`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available input routings. Legacy compatibility property. Prefer `available_input_routing_types`.

#### `input_sub_routings`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of available input sub routings. Legacy compatibility property. Prefer `available_input_routing_channels`.

#### `is_foldable`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the track can be (un)folded to hide or reveal the contained tracks. This is currently the case for Group
Tracks. Instrument and Drum Racks return `False` although they can be opened/closed.

#### `is_frozen`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the track is currently frozen.

#### `is_grouped`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if the track is contained within a Group Track.

#### `is_part_of_selection`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

Unknown.

#### `is_showing_chains`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Get or set whether a track with an Instrument Rack device is currently showing its chains in Session View.

#### `is_visible`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`False` if the track is hidden in a folded Group Track.

#### `mute`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Track mute state. Not available on master track.

#### `muted_via_solo`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if the track or chain is muted due to Solo being active on at least one other track.

#### `name`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

As shown in track header.

#### `output_meter_left`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Smoothed momentary peak value of left channel output meter, 0.0 to 1.0. For tracks with audio output only. Note
that the left/right audio meters add a significant load to Live GUI resource usage.

#### `output_meter_level`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Hold peak value of output meters of audio and MIDI tracks, 0.0 to 1.0. For audio tracks, it is the maximum of the
left and right channels. The hold time is 1 second.

#### `output_meter_right`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `<11`

Smoothed momentary peak value of right channel output meter, 0.0 to 1.0. For tracks with audio output only.

#### `output_routing_channel`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected target channel for the track's output routing. A dictionary with `display_name` and
`identifier` keys. Can be set to any value from `available_output_routing_channels`. Documented as unavailable on
master track.

- **Quirks:** Current probes (Live 12.3.5) returned this member on the master track as well. On several non-master
  tracks, only one output channel option was available.

#### `output_routing_type`

- **Type:** `dictionary`
- **Listenable:** `yes`
- **Since:** `<11`

The currently selected target type for the track's output routing. A dictionary with `display_name` and
`identifier` keys. Can be set to any value from `available_output_routing_types`. Documented as unavailable on
master track.

- **Quirks:** Current probes (Live 12.3.5) returned this member on the master track as well.

#### `output_routings`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of all available output routings. Legacy compatibility property. Prefer `available_output_routing_types`.

#### `output_sub_routings`

- **Type:** `list[str]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of all available output sub routings. Legacy compatibility property. Prefer
`available_output_routing_channels`.

#### `performance_impact`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.1`

Reports the performance impact of this track.

#### `playing_slot_index`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

First slot has index `0`. `-2` = Clip Stop slot fired in Session View, `-1` = Arrangement recording with no
Session clip playing. Not available on return/master tracks.

#### `solo`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

Track solo state. Not available on master track.

- **Quirks:** When setting this property, the exclusive Solo logic is bypassed — you have to unsolo the other tracks
  yourself.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `create_audio_clip(file_path: str, position: float)` | `Clip` | Create an arrangement audio clip from a file. |
| `create_midi_clip(start_time: float, length: float)` | `Clip` | Create an empty arrangement MIDI clip. |
| `create_take_lane()` | `LomObject` | Create a take lane for this track. |
| `delete_clip(clip: Clip)` | `None` | Delete the given clip. |
| `delete_device(index: int)` | `None` | Delete the device at the given index. |
| `duplicate_clip_slot(index: int)` | `int` | Duplicate a clip slot (like context menu Duplicate). |
| `duplicate_clip_to_arrangement(clip: Clip, destination_time: float)` | `Clip` | Duplicate a clip to the Arrangement at the given time. |
| `duplicate_device(index: int)` | `None` | Duplicate a device at the given index. |
| `get_data(key: object, default_value: object)` | `object` | Get persistent data for the given key. |
| `insert_device(device_name: str, device_index: int)` | `LomObject` | Insert a native device at the given index. |
| `jump_in_running_session_clip(beats: float)` | `None` | Relative jump in the running session clip. |
| `set_data(key: object, value: object)` | `None` | Store persistent data for the given key. |
| `stop_all_clips(quantized: bool)` | `None` | Stop all playing and fired clips in this track. |

#### `create_audio_clip(file_path: str, position: float)`

- **Returns:** `Clip`
- **Args:**
  - `file_path: str` -- absolute path to a valid audio file
  - `position: float` -- arrangement position in beats (range `[0, 1576800]`)
- **Since:** `11.3`

Creates an audio clip referencing the file at the specified position in the arrangement view. Errors if the track is
not audio, is frozen, or is being recorded into. See `ClipSlot.create_audio_clip` for session view clips.

#### `create_midi_clip(start_time: float, length: float)`

- **Returns:** `Clip`
- **Args:**
  - `start_time: float` -- arrangement position in beats (range `[0, 1576800]`)
  - `length: float` -- clip length in beats
- **Since:** `12.1`

Creates an empty MIDI clip in the arrangement at the specified time. Errors on non-MIDI tracks, frozen tracks, or
tracks being recorded into. See `ClipSlot.create_clip` for session view clips.

#### `create_take_lane()`

- **Returns:** `LomObject`
- **Args:** None
- **Since:** `12.2`

Creates a take lane for this track.

#### `delete_clip(clip: Clip)`

- **Returns:** `None`
- **Args:**
  - `clip: Clip` -- the clip to delete
- **Since:** `<11`

Delete the given clip.

#### `delete_device(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- device index to delete
- **Since:** `<11`

Delete the device at the given index.

#### `duplicate_clip_slot(index: int)`

- **Returns:** `int`
- **Args:**
  - `index: int` -- clip slot index to duplicate
- **Since:** `<11`

Works like 'Duplicate' in a clip's context menu.

#### `duplicate_clip_to_arrangement(clip: Clip, destination_time: float)`

- **Returns:** `Clip`
- **Args:**
  - `clip: Clip` -- the clip to duplicate
  - `destination_time: float` -- arrangement position in beats
- **Since:** `<11`

Duplicate the given clip to the Arrangement, placing it at the given destination time in beats.

#### `duplicate_device(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int` -- device index to duplicate
- **Since:** `12.3`

Duplicate a device at the given index in the device chain.

#### `get_data(key: object, default_value: object)`

- **Returns:** `object`
- **Args:**
  - `key: object` -- the key to look up
  - `default_value: object` -- returned if the key was never set
- **Since:** `<11`

Get data for the given key, that was previously stored using `set_data`. Data is persistent across save/load.

- **Quirks:** After `set_data(key, None)`, `get_data(key, default)` returns `None` rather than the provided
  default.

#### `insert_device(device_name: str, device_index: int)`

- **Returns:** `LomObject`
- **Args:**
  - `device_name: str` -- exact `class_display_name` (e.g. `"EQ Eight"`, not `"Eq8"`); case-sensitive
  - `device_index: int` -- position in the device chain (optional; defaults to end)
- **Raises:** `ValidationError: Device {name} not found.` if the name doesn't match any native device.
- **Since:** `12.3`

Inserts a native Live device at the given index. Only native devices are supported — third-party plug-ins (VST/AU)
and Max for Live devices are not (the empty M4L container shell can be inserted as it is native). Not all indices
are valid; structural constraints apply (e.g., a MIDI effect cannot be inserted after an instrument).

#### `jump_in_running_session_clip(beats: float)`

- **Returns:** `None`
- **Args:**
  - `beats: float` -- amount to jump relative to the current clip position
- **Since:** `<11`

Modify playback position in the running Session clip on this track, if any.

#### `set_data(key: object, value: object)`

- **Returns:** `None`
- **Args:**
  - `key: object` -- the key to store under
  - `value: object` -- the value to store
- **Since:** `<11`

Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.

#### `stop_all_clips(quantized: bool)`

- **Returns:** `None`
- **Args:**
  - `quantized: bool` -- `False` stops immediately, `True` (default) respects launch quantization
- **Since:** `<11`

Stops all playing and fired clips in this track.

---

## Track.View

> `Live.Track.Track.View`

Representing the view aspects of a track.

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `selected_device` | `Device` | `single` | `yes` | The selected device (or first in a multi-selection). |

#### `selected_device`

- **Returns:** `Device`
- **Shape:** `single`
- **Listenable:** `yes`
- **Since:** `<11`

The selected device or the first selected device (in case of multi/group selection).

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `canonical_parent` | `Track` | `no` | `no` | The canonical parent of the track view. |
| `device_insert_mode` | `int` | `yes` | `yes` | Where a device is inserted when loaded from the browser. |
| `is_collapsed` | `bool` | `yes` | `yes` | In Arrangement View: `True` = track collapsed. |

#### `canonical_parent`

- **Type:** `Track`
- **Listenable:** `no`
- **Since:** `<11`

The canonical parent of the track view.

#### `device_insert_mode`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

Determines where a device will be inserted when loaded from the browser. `0` = add at end, `1` = left of selected
device, `2` = right of selected device.

#### `is_collapsed`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

In Arrangement View: `True` = track collapsed, `False` = track opened.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `select_instrument()` | `bool` | Select the track's instrument or first device. |

#### `select_instrument()`

- **Returns:** `bool` -- `False` if there are no devices to select
- **Args:** None
- **Since:** `<11`

Selects the track's instrument or first device, makes it visible and focuses on it.

---

## Track.DeviceContainer

> `Live.Track.Track.DeviceContainer`

Common super class of Track and Chain. No user-facing properties or methods beyond the internal `_live_ptr`.

---

## Track.DeviceInsertMode

> `Live.Track.Track.DeviceInsertMode`

Enumeration used by `Track.View.device_insert_mode`. Values: `0` = add at end, `1` = insert left of selected
device, `2` = insert right of selected device.

---

## Track.RoutingChannel

> `Live.Track.Track.RoutingChannel`

Represents a routing channel with `display_name` and `layout` properties.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `display_name` | `str` | `no` | `no` | Display name of the routing channel. |
| `layout` | `Track.RoutingChannelLayout` | `no` | `no` | The channel layout (e.g., mono or stereo). |

#### `display_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Display name of the routing channel.

#### `layout`

- **Type:** `Track.RoutingChannelLayout`
- **Listenable:** `no`
- **Since:** `<11`

The routing channel's layout, e.g., mono or stereo.

---

## Track.RoutingChannelLayout

> `Live.Track.Track.RoutingChannelLayout`

Enumeration for routing channel layout (e.g., mono/stereo).

---

## Track.RoutingChannelVector

> `Live.Track.Track.RoutingChannelVector`

A container for returning routing channels from Live. Supports `append()` and `extend()`.

---

## Track.RoutingType

> `Live.Track.Track.RoutingType`

Represents a routing type with `attached_object`, `category`, and `display_name` properties.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `attached_object` | `LomObject` | `no` | `no` | Live object associated with the routing type. |
| `category` | `Track.RoutingTypeCategory` | `no` | `no` | Category of the routing type. |
| `display_name` | `str` | `no` | `no` | Display name of the routing type. |

#### `attached_object`

- **Type:** `LomObject`
- **Listenable:** `no`
- **Since:** `<11`

Live object associated with the routing type.

#### `category`

- **Type:** `Track.RoutingTypeCategory`
- **Listenable:** `no`
- **Since:** `<11`

Category of the routing type.

#### `display_name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Display name of the routing type.

---

## Track.RoutingTypeCategory

> `Live.Track.Track.RoutingTypeCategory`

Enumeration for routing type categories.

---

## Track.RoutingTypeVector

> `Live.Track.Track.RoutingTypeVector`

A container for returning routing types from Live. Supports `append()` and `extend()`.

---

## Track.monitoring_states

> `Live.Track.Track.monitoring_states`

Enumeration used by `Track.current_monitoring_state`. Values `0`, `1`, `2` are accepted; `>=3` returns
`Invalid monitoring state!`. Semantic labels for the three states are unconfirmed in raw docs.

