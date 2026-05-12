---
module: Application
---

Represents the running Live application — the entry point to the LOM, returned by the module-level `get_application()`
function. The `Application` class exposes Live's version, the browser, the control-surface registry, and the
`Application.View` for navigating Live's windows and panels.

## Classes

### Application

```yaml
kind: class
path: Live.Application.Application
ancestors:
  - Live.LomObject.LomObject
  - Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents the Live application.
```

#### Properties

##### average_process_usage

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Reports Live's average CPU load.
```

##### browser

```yaml
kind: property
type: Live.Browser.Browser
settable: false
raw_doc: Returns an interface to the browser.
```

##### canonical_parent

```yaml
kind: property
type: None
settable: false
raw_doc: Returns the canonical parent of the application.
refinement:
  probed: None
  confidence: high
  sources:
    - "[probe] Application is the LOM root. It has no parent — the probe's None observation reflects the structural
      shape, not an instance-specific nullability. Every other class's `canonical_parent` probes as a concrete parent
      type; only this and `Song.canonical_parent` probe as None."
```

##### control_surfaces

```yaml
kind: property
type: Live.Base.Vector[object]
settable: false
listenable: true
raw_doc: |-
  Const access to a list of the control surfaces selected in preferences, in the same order.
  The list contains None if no control surface is active at that index.
```

##### current_dialog_button_count

```yaml
kind: property
type: int
settable: false
raw_doc: Number of buttons on the current dialog.
```

##### current_dialog_message

```yaml
kind: property
type: str
settable: false
raw_doc: Text of the last dialog that appeared; Empty if all dialogs just disappeared.
```

##### number_of_push_apps_running

```yaml
kind: property
type: int
settable: false
raw_doc: Returns the number of connected Push apps.
```

##### open_dialog_count

```yaml
kind: property
type: int
settable: false
listenable: true
raw_doc: The number of open dialogs in Live. 0 if not dialog is open.
```

##### peak_process_usage

```yaml
kind: property
type: float
settable: false
listenable: true
raw_doc: Reports Live's peak CPU load.
```

##### unavailable_features

```yaml
kind: property
type: Live.Application.UnavailableFeatureVector
settable: false
listenable: true
raw_doc: List of features that are unavailable due to limitations of the current Live edition.
element_type_override:
  value: Live.Application.UnavailableFeature
  confidence: high
  sources:
    - "[probe] property's probed_type is UnavailableFeatureVector; element type is the UnavailableFeature enum."
    - "[corpus] checks of the form `Live.Application.UnavailableFeature.X not in
      Live.Application.get_application().unavailable_features`."
```

##### view

```yaml
kind: property
type: Live.Application.Application.View
settable: false
raw_doc: Returns the applications view component.
```

#### Methods

##### get_bugfix_version

```yaml
kind: method
signature: "get_bugfix_version( (Application)arg1) -> int :"
cpp_signature: int get_bugfix_version(TPyHandle<ASongApp>)
returns:
  type: int
raw_doc: Returns an integer representing the bugfix version of Live.
```

##### get_build_id

```yaml
kind: method
signature: "get_build_id( (Application)arg1) -> str :"
cpp_signature: TString get_build_id(TPyHandle<ASongApp>)
returns:
  type: str
raw_doc: Returns a string identifying the build.
```

##### get_document

```yaml
kind: method
signature: "get_document( (Application)arg1) -> Song :"
cpp_signature: TWeakPtr<TPyHandle<ASong>> get_document(TPyHandle<ASongApp>)
returns:
  type: Live.Song.Song
raw_doc: Returns the current Live Set.
```

##### get_major_version

```yaml
kind: method
signature: "get_major_version( (Application)arg1) -> int :"
cpp_signature: int get_major_version(TPyHandle<ASongApp>)
returns:
  type: int
raw_doc: Returns an integer representing the major version of Live.
```

##### get_minor_version

```yaml
kind: method
signature: "get_minor_version( (Application)arg1) -> int :"
cpp_signature: int get_minor_version(TPyHandle<ASongApp>)
returns:
  type: int
raw_doc: Returns an integer representing the minor version of Live.
```

##### get_variant

```yaml
kind: method
signature: "get_variant( (Application)arg1) -> str :"
cpp_signature: TString get_variant(TPyHandle<ASongApp>)
returns:
  type: str
raw_doc: Returns one of the strings in Live.Application.Variants.
```

##### get_version_string

```yaml
kind: method
signature: "get_version_string( (Application)arg1) -> str :"
cpp_signature: TString get_version_string(TPyHandle<ASongApp>)
returns:
  type: str
raw_doc: Returns the full version string of Live.
```

##### has_option

```yaml
kind: method
signature: "has_option( (Application)arg1, (object)arg2) -> bool :"
cpp_signature: bool has_option(TPyHandle<ASongApp>,TString)
args:
  - name: option_name
    type: str
    refinement:
      name:
        probed: arg2
        sources:
          - '[docstring] "given entry exists in Options.txt" — the entry is an option name.'
returns:
  type: bool
raw_doc: Returns True if the given entry exists in Options.txt, False otherwise.
```

##### press_current_dialog_button

```yaml
kind: method
signature: "press_current_dialog_button( (Application)arg1, (int)arg2) -> None :"
cpp_signature: void press_current_dialog_button(TPyHandle<ASongApp>,int)
args:
  - name: index
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - "[M4L] external/max-for-live-docs/9.0/application.md names the parameter `index`."
returns:
  type: None
raw_doc: Press a button, by index, on the current message box.
```

##### show_message

```yaml
kind: method
signature:
  "show_message( (Application)arg1, (Text)text [, (int)buttons=Application.MessageButtons.OK_BUTTON [,
  (bool)enable_markup=False [, (bool)show_success_icon=False]]]) -> int :"
cpp_signature:
  int show_message(TPyHandle<ASongApp>,TText [,int=Application.MessageButtons.OK_BUTTON [,bool=False [,bool=False]]])
args:
  - name: text
    type: Live.Base.Text
  - name: buttons
    type: Live.Application.MessageButtons | int
    optional: true
    default: Application.MessageButtons.OK_BUTTON
  - name: enable_markup
    type: bool
    optional: true
    default: "False"
  - name: show_success_icon
    type: bool
    optional: true
    default: "False"
returns:
  type: int
raw_doc: Shows a message box, returning the position of the pressed button.
```

##### show_on_the_fly_message

```yaml
kind: method
signature:
  "show_on_the_fly_message( (Application)arg1, (str)message [, (int)buttons=Application.MessageButtons.OK_BUTTON [,
  (bool)enable_markup=False [, (bool)show_success_icon=False [,
  (int)push_dialog_type=Application.PushDialogType.MESSAGE_BOX]]]]) -> int :"
cpp_signature:
  int show_on_the_fly_message(TPyHandle<ASongApp>,std::__1::basic_string<char, std::__1::char_traits<char>,
  std::__1::allocator<char>> [,int=Application.MessageButtons.OK_BUTTON [,bool=False [,bool=False
  [,int=Application.PushDialogType.MESSAGE_BOX]]]])
args:
  - name: message
    type: str
  - name: buttons
    type: Live.Application.MessageButtons | int
    optional: true
    default: Application.MessageButtons.OK_BUTTON
  - name: enable_markup
    type: bool
    optional: true
    default: "False"
  - name: show_success_icon
    type: bool
    optional: true
    default: "False"
  - name: push_dialog_type
    type: Live.Application.PushDialogType | int
    optional: true
    default: Application.PushDialogType.MESSAGE_BOX
returns:
  type: int
raw_doc: Same as show_message, but for when there is no predefined Text object.
```

### ControlDescription

```yaml
kind: class
path: Live.Application.ControlDescription
ancestors:
  - Boost.Python.instance
init_doc: |-
  __init__( (object)arg1) -> None :

      C++ signature :
          void __init__(_object*)
constructable: true
raw_doc: Describes a control present in a control surface proxy
```

#### Properties

##### id

```yaml
kind: property
type: int
settable: false
```

##### name

```yaml
kind: property
type: str
settable: false
```

#### Methods

##### **init**

```yaml
kind: method
returns:
  type: None
```

### ControlDescriptionVector

```yaml
kind: class
path: Live.Application.ControlDescriptionVector
ancestors:
  - Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: A container for returning control descriptions.
```

### ControlSurfaceProxy

```yaml
kind: class
path: Live.Application.ControlSurfaceProxy
ancestors:
  - Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Represents a control surface running in a different process. For use by M4L
```

#### Properties

##### control_descriptions

```yaml
kind: property
type: Live.Application.ControlDescriptionVector
settable: false
refinement:
  confidence: high
  sources:
    - "[probe] couldn't reach this class — ControlSurfaceProxy is M4L-only."
    - "[corpus] _MxDCore/ControlSurfaceWrapper.py:238 iterates `c.name for c in self._proxy.control_descriptions` —
      confirms it's a container of ControlDescription objects (each with a `.name` property)."
    - "[schema] ControlDescriptionVector exists in the parsed tree with element_repr fixed below to ControlDescription."
```

##### pad_layout

```yaml
kind: property
type: str
settable: false
listenable: true
raw_doc: The layout of pads on Push.
refinement:
  confidence: high
  sources:
    - "[M4L] external/max-for-live-docs/9.0/controlsurface.md:18: `pad_layout symbol read-only observe` — `symbol` is
      M4L parlance for a string (string-valued layout names like 'session', 'note.drums.64_pads')."
    - '[docstring] "The layout of pads on Push."'
```

##### type_name

```yaml
kind: property
type: str
settable: false
refinement:
  confidence: medium
  sources:
    - "[corpus] no raw_doc, no M4L doc entry; binding access at _MxDCore/ControlSurfaceWrapper.py:234 returns
      `self._proxy.type_name` from a wrapper property and uses the value in tuple/string contexts. `str` is the
      strongest reading — promote via probe."
```

##### control_values_arrived

```yaml
kind: property
listenable: true
```

Fires when control values arrive from the connected hardware after a `subscribe_to_control` registration. Notification
only — read the values via `fetch_received_values` after the callback.

##### midi_received

```yaml
kind: property
listenable: true
```

Fires when MIDI input arrives at the control surface proxy after `enable_receive_midi(True)`. Notification only — read
the messages via `fetch_received_midi_messages`.

#### Methods

##### enable_receive_midi

```yaml
kind: method
signature: "enable_receive_midi( (ControlSurfaceProxy)arg1, (bool)arg2) -> None :"
cpp_signature: void enable_receive_midi(APythonControlSurfaceProxy {lvalue},bool)
args:
  - name: enabled
    type: bool
    refinement:
      name:
        probed: arg2
        sources:
          - "[docstring] method name is `enable_receive_midi` — boolean parameter controls whether MIDI receive is
            enabled."
returns:
  type: None
```

##### fetch_received_midi_messages

```yaml
kind: method
signature: "fetch_received_midi_messages( (ControlSurfaceProxy)arg1) -> tuple :"
cpp_signature: boost::python::tuple fetch_received_midi_messages(APythonControlSurfaceProxy {lvalue})
returns:
  type: tuple[tuple[int, ...], ...]
  refinement:
    probed: tuple
    confidence: medium
    sources:
      - "[docstring] `-> tuple` confirms the outer return is a tuple."
      - "[corpus] _MxDCore/ControlSurfaceWrapper.py:251 iterates `for message in
        self._proxy.fetch_received_midi_messages():` and passes each message to `handle_message(message)`. The corpus
        doesn't unpack the inner tuple, so the inner shape `tuple[int, ...]` is inferred from MIDI semantics (MIDI
        messages are tuples of status + data bytes, all ints)."
```

##### fetch_received_values

```yaml
kind: method
signature: "fetch_received_values( (ControlSurfaceProxy)arg1) -> tuple :"
cpp_signature: boost::python::tuple fetch_received_values(APythonControlSurfaceProxy {lvalue})
returns:
  type: tuple[tuple[int, Any], ...]
  refinement:
    probed: tuple
    confidence: high
    sources:
      - "[docstring] `-> tuple` confirms the outer return is a tuple."
      - "[corpus] _MxDCore/ControlSurfaceWrapper.py:244 explicitly unpacks the inner 2-tuple: `for control_id, value in
        self._proxy.fetch_received_values():`. The first element is then used as a dict key
        (`self._control_proxies_by_id[control_id]`) confirming int; the second element is passed to
        `receive_value(value)` — value type depends on control, so Any."
```

##### grab_control

```yaml
kind: method
signature: "grab_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :"
cpp_signature: void grab_control(APythonControlSurfaceProxy {lvalue},int)
args:
  - name: control_id
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - "[sister method] same shape as `release_control`."
          - "[M4L] external/max-for-live-docs/9.0/controlsurface.md names it `control`, but the binding takes the int ID
            — renamed to `control_id` here for clarity over doc-conformance."
          - "[corpus] _MxDCore/ControlSurfaceWrapper.py:262 (`self._proxy.grab_control(control.id)`)."
returns:
  type: None
```

##### release_control

```yaml
kind: method
signature: "release_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :"
cpp_signature: void release_control(APythonControlSurfaceProxy {lvalue},int)
args:
  - name: control_id
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - "[C++ signature] binding takes the control's int ID."
          - "[M4L] external/max-for-live-docs/9.0/controlsurface.md names the parameter `control` (the M4L abstraction
            passes a control object), but Live's binding is one layer below — it takes the int. Renamed to `control_id`
            for clarity over doc-conformance."
          - "[corpus] _MxDCore/ControlSurfaceWrapper.py:266 confirms: `self._proxy.release_control(control.id)` — passes
            `.id`, an int."
returns:
  type: None
```

##### send_midi

```yaml
kind: method
signature: "send_midi( (ControlSurfaceProxy)arg1, (tuple)arg2) -> None :"
cpp_signature: void send_midi(APythonControlSurfaceProxy {lvalue},boost::python::tuple)
args:
  - name: midi_event_bytes
    type: tuple[int, ...]
    refinement:
      name:
        probed: arg2
        sources:
          - "[corpus] 10/20 callsite defs use `midi_event_bytes` across Python wrapper classes (FaderfoxComponent.py:41,
            FaderfoxScript.py:110, Axiom_49_61_Classic/Axiom.py:69, etc.)."
      type:
        probed: tuple
        confidence: high
        sources:
          - "[C++ signature] `void send_midi(APythonControlSurfaceProxy {lvalue}, boost::python::tuple)` — the binding
            takes an untyped tuple at the C++ level."
          - "[schema] narrowed to `tuple[int, ...]` per function semantics — MIDI bytes are 0–255 ints by definition."
          - "[corpus] binding calls pass int tuples: FaderfoxScript.py:111
            (`self.c_instance.send_midi(midi_event_bytes)`), Axiom_49_61_Classic/Axiom.py:70
            (`self._Axiom__c_instance.send_midi(midi_event_bytes)`); wrapper composers also produce int tuples
            (LV2_LX2_LC2_LD2/LV2TransportController.py:69-71 `(NOTEON_STATUS + channel, note, 127)`,
            LV2_LX2_LC2_LD2/FaderfoxMixerController.py:142 `(175, 16, 16)`)."
returns:
  type: None
```

##### send_value

```yaml
kind: method
signature: "send_value( (ControlSurfaceProxy)arg1, (tuple)arg2) -> None :"
cpp_signature: void send_value(APythonControlSurfaceProxy {lvalue},boost::python::tuple)
args:
  - name: value
    type: tuple[Any, ...]
    refinement:
      name:
        probed: arg2
        sources:
          - "[corpus] 16/19 callsite defs use `value` across Python wrapper classes
            (_Framework/InputControlElement.py:324, ableton/v2/control_surface/elements/button.py:102, etc.)."
      type:
        probed: tuple
        confidence: high
        sources:
          - "[C++ signature] `void send_value(APythonControlSurfaceProxy {lvalue}, boost::python::tuple)` — the binding
            strictly accepts a tuple."
          - "[schema] `tuple[Any, ...]` matches the untyped Boost.Python tuple — the binding itself doesn't constrain
            element type at the C++ level."
          - "[corpus] calls like `interface.send_value(0)` or `button.send_value(value)` don't contradict this — those
            go to Python wrappers (SysexElement.send_value at sysex_element.py:25, InputControlElement.send_value at
            InputControlElement.py:324) which compose a tuple internally before the binding call. Zero direct
            `Live.Application.ControlSurfaceProxy.send_value` callsites exist in the corpus."
returns:
  type: None
```

##### subscribe_to_control

```yaml
kind: method
signature: "subscribe_to_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :"
cpp_signature: void subscribe_to_control(APythonControlSurfaceProxy {lvalue},int)
args:
  - name: control_id
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - "[sister method] same shape as `grab_control` / `release_control`."
          - "[C++ signature] `void subscribe_to_control(..., int)` — int control ID."
          - "[corpus] _MxDCore/ControlSurfaceWrapper.py:201 (`self._proxy.subscribe_to_control(self._id)` — passes int)."
returns:
  type: None
```

##### unsubscribe_from_control

```yaml
kind: method
signature: "unsubscribe_from_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :"
cpp_signature: void unsubscribe_from_control(APythonControlSurfaceProxy {lvalue},int)
args:
  - name: control_id
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - "[sister method] same shape as `subscribe_to_control`."
          - "[C++ signature] `void unsubscribe_from_control(..., int)` — int control ID."
          - "[corpus] _MxDCore/ControlSurfaceWrapper.py:209 (`self._proxy.unsubscribe_from_control(self._id)` — passes
            int)."
returns:
  type: None
```

### UnavailableFeatureVector

```yaml
kind: class
path: Live.Application.UnavailableFeatureVector
ancestors:
  - Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: A container for returning unavailable features.
```

### Variants

```yaml
kind: class
path: Live.Application.Variants
ancestors:
  - Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Holds strings representing what type of Live is running.
```

### View

```yaml
kind: class
path: Live.Application.Application.View
parent: Application
ancestors:
  - Live.LomObject.LomObject
  - Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents the view aspects of the Live application.
```

#### Properties

##### browse_mode

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: Return true if HotSwap mode is active for any target.
```

##### canonical_parent

```yaml
kind: property
type: Live.Application.Application
settable: false
raw_doc: Get the canonical parent of the application view.
```

##### focused_document_view

```yaml
kind: property
type: str
settable: false
listenable: true
raw_doc: |-
  Return the name of the document view ('Session' or 'Arranger')
  shown in the currently selected window.
```

##### view_focus_changed

```yaml
kind: property
listenable: true
```

Fires when the focused view changes (Session/Arrangement switch, popup open/close, primary/secondary window focus
shifts). Programmatic triggers include `focus_view`, `show_view`, `hide_view`, and `toggle_browse`; user interaction
with Live's UI also fires it.

#### Methods

##### add_is_view_visible_listener

```yaml
kind: method
signature: "add_is_view_visible_listener( (View)arg1, (object)arg2, (object)arg3) -> None :"
cpp_signature: void add_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
args:
  - name: view_name
    type: str
    refinement:
      name:
        probed: arg2
        sources:
          - "[C++ signature] TString parameter for view identifier."
  - name: callback
    type: Callable[[], None]
returns:
  type: None
raw_doc: |-
  Add a listener function or method, which will be called as soon as the
  property "is_view_visible" has changed.
```

##### available_main_views

```yaml
kind: method
signature: "available_main_views( (View)arg1) -> StringVector :"
cpp_signature: std::__1::vector<TString, std::__1::allocator<TString>> available_main_views(TPyViewData<ASongApp>)
returns:
  type: Live.Base.StringVector
raw_doc: |-
  Return a list of strings with the available subcomponent views, which
  is to be specified, when using the rest of this classes functions.
  A 'subcomponent view' is a main view component of a document view, like
  the Session view, the Arranger or Detailview and so on...
```

##### focus_view

```yaml
kind: method
signature: "focus_view( (View)arg1, (object)arg2) -> None :"
cpp_signature: void focus_view(TPyViewData<ASongApp>,TString)
args:
  - name: view
    type: str
    refinement:
      name:
        probed: arg2
        sources:
          - "[corpus] 2/2 callsite defs use `view` (
            external/corpus/ableton/v2/control_surface/components/view_control.py:168 and one more)."
returns:
  type: None
raw_doc: Show and focus one through the identifier string specified view.
```

##### hide_view

```yaml
kind: method
signature: "hide_view( (View)arg1, (object)arg2) -> None :"
cpp_signature: void hide_view(TPyViewData<ASongApp>,TString)
args:
  - name: view_name
    type: str
    refinement:
      name:
        probed: arg2
        sources:
          - "[M4L] external/max-for-live-docs/9.0/application_view.md names the parameter `view_name`."
returns:
  type: None
raw_doc: Hide one through the identifier string specified view.
```

##### is_view_visible

```yaml
kind: method
signature: "is_view_visible( (View)arg1, (object)identifier [, (bool)main_window_only=True]) -> bool :"
cpp_signature: bool is_view_visible(TPyViewData<ASongApp>,TString [,bool=True])
args:
  - name: view_name
    type: str
  - name: main_window_only
    type: bool
    optional: true
    default: "True"
returns:
  type: bool
raw_doc: |-
  Return true if the through the identifier string specified view is currently
  visible. If main_window_only is set to False, this will also check in second
  window. Notifications from the second window are not yet supported.
```

Returns whether the view named by `view_name` is currently visible. With `main_window_only=False`, also checks the
second window — note that notifications from the second window are not yet supported.

Parameterized observable — the LOM's only one (as of 12.3.6). Read by calling `is_view_visible(view_name)`. Subscribe
via the matching listener triplet, which takes view_name as its first parameter:

```
add_is_view_visible_listener(view_name, callback)
remove_is_view_visible_listener(view_name, callback)
is_view_visible_has_listener(view_name, callback)
```

##### is_view_visible_has_listener

```yaml
kind: method
signature: "is_view_visible_has_listener( (View)arg1, (object)arg2, (object)arg3) -> bool :"
cpp_signature: bool is_view_visible_has_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
args:
  - name: view_name
    type: str
    refinement:
      name:
        probed: arg2
        sources:
          - "[C++ signature] TString parameter for view identifier."
  - name: callback
    type: Callable[[], None]
returns:
  type: bool
raw_doc: |-
  Returns true, if the given listener function or method is connected
  to the property "is_view_visible".
```

##### remove_is_view_visible_listener

```yaml
kind: method
signature: "remove_is_view_visible_listener( (View)arg1, (object)arg2, (object)arg3) -> None :"
cpp_signature: void remove_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
args:
  - name: view_name
    type: str
    refinement:
      name:
        probed: arg2
        sources:
          - "[C++ signature] TString parameter for view identifier."
  - name: callback
    type: Callable[[], None]
returns:
  type: None
raw_doc: |-
  Remove a previously set listener function or method from
  property "is_view_visible".
```

##### scroll_view

```yaml
kind: method
signature: "scroll_view( (View)arg1, (int)arg2, (object)arg3, (bool)arg4) -> None :"
cpp_signature: void scroll_view(TPyViewData<ASongApp>,int,TString,bool)
args:
  - name: direction
    type: Live.Application.Application.View.NavDirection | int
    refinement:
      name:
        probed: arg2
        sources:
          - "[M4L] external/max-for-live-docs/9.0/application_view.md names the parameter `direction`."
      type:
        probed: int
        confidence: high
        sources:
          - '[docstring] "into the given direction".'
          - "[schema] Application.View nests a single enum (`NavDirection`) with members up/down/left/right — direct
            semantic match. Boost.Python emits the enum class as an int subclass, hence `NavDirection | int` (standard
            enum-widening pattern)."
  - name: view_name
    type: str
    refinement:
      name:
        probed: arg3
        sources:
          - "[M4L] external/max-for-live-docs/9.0/application_view.md names the parameter `view_name`."
  - name: modifier_pressed
    type: bool
    refinement:
      name:
        probed: arg4
        sources:
          - "[M4L] external/max-for-live-docs/9.0/application_view.md names the parameter `modifier_pressed`."
returns:
  type: None
raw_doc: |-
  Scroll through the identifier string specified view into the given
  direction, if possible. Will silently return if the specified view
  can not perform the requested action.
```

##### show_view

```yaml
kind: method
signature: "show_view( (View)arg1, (object)arg2) -> None :"
cpp_signature: void show_view(TPyViewData<ASongApp>,TString)
args:
  - name: view
    type: str
    refinement:
      name:
        probed: arg2
        sources:
          - "[corpus] 3/3 callsite defs use `view`
            (external/corpus/ableton/v2/control_surface/components/view_control.py:158 and 2 more)."
returns:
  type: None
raw_doc: |-
  Show one through the identifier string specified view. Will throw a
  runtime error if this is called in Live's initialization scope.
```

##### toggle_browse

```yaml
kind: method
signature: "toggle_browse( (View)arg1) -> None :"
cpp_signature: void toggle_browse(TPyViewData<ASongApp>)
returns:
  type: None
raw_doc: |-
  Reveals the device chain, the browser and starts hot swap for
  the selected device. Calling this function again stops hot swap.
```

##### zoom_view

```yaml
kind: method
signature: "zoom_view( (View)arg1, (int)arg2, (object)arg3, (bool)arg4) -> None :"
cpp_signature: void zoom_view(TPyViewData<ASongApp>,int,TString,bool)
args:
  - name: direction
    type: Live.Application.Application.View.NavDirection | int
    refinement:
      name:
        probed: arg2
        sources:
          - "[M4L] external/max-for-live-docs/9.0/application_view.md names the parameter `direction`."
      type:
        probed: int
        confidence: high
        sources:
          - '[docstring] "into the given direction".'
          - "[schema] Application.View nests a single enum (`NavDirection`) with members up/down/left/right — direct
            semantic match. Boost.Python emits the enum class as an int subclass, hence `NavDirection | int` (standard
            enum-widening pattern)."
  - name: view_name
    type: str
    refinement:
      name:
        probed: arg3
        sources:
          - "[M4L] external/max-for-live-docs/9.0/application_view.md names the parameter `view_name`."
  - name: modifier_pressed
    type: bool
    refinement:
      name:
        probed: arg4
        sources:
          - "[M4L] external/max-for-live-docs/9.0/application_view.md names the parameter `modifier_pressed`."
returns:
  type: None
raw_doc: |-
  Zoom through the identifier string specified view into the given
  direction, if possible. Will silently return if the specified view
  can not perform the requested action.
```

## Enums

### MessageButtons

```yaml
kind: enum
members:
  OK_BUTTON: 0
  OK_NEW_SET_BUTTON: 1
  OK_RETRY_BUTTON: 2
  SAVE_DONT_SAVE_BUTTON: 3
  OK_ACCOUNT_BUTTON: 4
  OK_PURCHASE_BUTTON: 5
raw_doc: Specifies the characteristics of the message box, e.g. which buttons to show.
```

### PushDialogType

```yaml
kind: enum
members:
  MESSAGE_BOX: 0
  OUT_OF_UNLOCKS_DIALOG: 5
  RENT_TO_OWN_LICENSE_EXPIRED_DIALOG: 7
raw_doc: Specifies the dialog type for Push.
```

### UnavailableFeature

```yaml
kind: enum
members:
  note_velocity_ranges_and_probabilities: 0
```

### NavDirection

```yaml
kind: enum
parent: View
members:
  up: 0
  down: 1
  left: 2
  right: 3
```

## Functions

### combine_apcs

```yaml
kind: function
signature: "combine_apcs() -> bool :"
cpp_signature: bool combine_apcs()
returns:
  type: bool
raw_doc: Returns true if multiple APCs should be combined.
```

### encrypt_challenge

```yaml
kind: function
signature: "encrypt_challenge( (int)dongle1, (int)dongle2 [, (int)key_index=0]) -> tuple :"
cpp_signature: boost::python::tuple encrypt_challenge(int,int [,int=0])
args:
  - name: dongle1
    type: int
  - name: dongle2
    type: int
  - name: key_index
    type: int
    optional: true
    default: "0"
returns:
  type: tuple[int, ...]
  refinement:
    probed: tuple
    confidence: high
    sources:
      - "[corpus] Push/handshake_component.py:53 wraps it for encryption; _APC/APC.py:79 compares the return to a dongle
        challenge tuple."
      - "[docstring] baseline Application.md:38 lists it as a module-level static."
raw_doc: Returns an encrypted challenge based on the TEA algortithm
```

### encrypt_challenge2

```yaml
kind: function
signature: "encrypt_challenge2( (int)arg1) -> int :"
cpp_signature: int encrypt_challenge2(int)
args:
  - name: challenge
    type: int
    refinement:
      name:
        probed: arg1
        sources:
          - '[docstring] "UMAC hash for the given challenge" — parameter is the challenge.'
returns:
  type: int
raw_doc: Returns the UMAC hash for the given challenge.
```

### get_application

```yaml
kind: function
signature: "get_application() -> Application :"
cpp_signature: TWeakPtr<TPyHandle<ASongApp>> get_application()
returns:
  type: Live.Application.Application
raw_doc: Returns the application instance.
```

### get_random_int

```yaml
kind: function
signature: "get_random_int( (int)arg1, (int)arg2) -> int :"
cpp_signature: int get_random_int(int,int)
args:
  - name: min_value
    type: int
    refinement:
      name:
        probed: arg1
        sources:
          - '[docstring] "random integer from the given range" — first arg is the minimum.'
  - name: max_value
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - '[docstring] "random integer from the given range" — second arg is the maximum.'
returns:
  type: int
raw_doc: Returns a random integer from the given range.
```
