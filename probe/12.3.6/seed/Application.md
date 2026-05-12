---
module: Application
---

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
signature: 'get_bugfix_version( (Application)arg1) -> int :'
cpp_signature: int get_bugfix_version(TPyHandle<ASongApp>)
returns:
  type: int
raw_doc: Returns an integer representing the bugfix version of Live.
```

##### get_build_id

```yaml
kind: method
signature: 'get_build_id( (Application)arg1) -> str :'
cpp_signature: TString get_build_id(TPyHandle<ASongApp>)
returns:
  type: str
raw_doc: Returns a string identifying the build.
```

##### get_document

```yaml
kind: method
signature: 'get_document( (Application)arg1) -> Song :'
cpp_signature: TWeakPtr<TPyHandle<ASong>> get_document(TPyHandle<ASongApp>)
returns:
  type: Live.Song.Song
raw_doc: Returns the current Live Set.
```

##### get_major_version

```yaml
kind: method
signature: 'get_major_version( (Application)arg1) -> int :'
cpp_signature: int get_major_version(TPyHandle<ASongApp>)
returns:
  type: int
raw_doc: Returns an integer representing the major version of Live.
```

##### get_minor_version

```yaml
kind: method
signature: 'get_minor_version( (Application)arg1) -> int :'
cpp_signature: int get_minor_version(TPyHandle<ASongApp>)
returns:
  type: int
raw_doc: Returns an integer representing the minor version of Live.
```

##### get_variant

```yaml
kind: method
signature: 'get_variant( (Application)arg1) -> str :'
cpp_signature: TString get_variant(TPyHandle<ASongApp>)
returns:
  type: str
raw_doc: Returns one of the strings in Live.Application.Variants.
```

##### get_version_string

```yaml
kind: method
signature: 'get_version_string( (Application)arg1) -> str :'
cpp_signature: TString get_version_string(TPyHandle<ASongApp>)
returns:
  type: str
raw_doc: Returns the full version string of Live.
```

##### has_option

```yaml
kind: method
signature: 'has_option( (Application)arg1, (object)arg2) -> bool :'
cpp_signature: bool has_option(TPyHandle<ASongApp>,TString)
args:
- name: arg2
  type: str
returns:
  type: bool
raw_doc: Returns True if the given entry exists in Options.txt, False otherwise.
```

##### press_current_dialog_button

```yaml
kind: method
signature: 'press_current_dialog_button( (Application)arg1, (int)arg2) -> None :'
cpp_signature: void press_current_dialog_button(TPyHandle<ASongApp>,int)
args:
- name: arg2
  type: int
returns:
  type: None
raw_doc: Press a button, by index, on the current message box.
```

##### show_message

```yaml
kind: method
signature: 'show_message( (Application)arg1, (Text)text [, (int)buttons=Application.MessageButtons.OK_BUTTON [, (bool)enable_markup=False
  [, (bool)show_success_icon=False]]]) -> int :'
cpp_signature: int show_message(TPyHandle<ASongApp>,TText [,int=Application.MessageButtons.OK_BUTTON [,bool=False [,bool=False]]])
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
  default: 'False'
- name: show_success_icon
  type: bool
  optional: true
  default: 'False'
returns:
  type: int
raw_doc: Shows a message box, returning the position of the pressed button.
```

##### show_on_the_fly_message

```yaml
kind: method
signature: 'show_on_the_fly_message( (Application)arg1, (str)message [, (int)buttons=Application.MessageButtons.OK_BUTTON
  [, (bool)enable_markup=False [, (bool)show_success_icon=False [, (int)push_dialog_type=Application.PushDialogType.MESSAGE_BOX]]]])
  -> int :'
cpp_signature: int show_on_the_fly_message(TPyHandle<ASongApp>,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>
  [,int=Application.MessageButtons.OK_BUTTON [,bool=False [,bool=False [,int=Application.PushDialogType.MESSAGE_BOX]]]])
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
  default: 'False'
- name: show_success_icon
  type: bool
  optional: true
  default: 'False'
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

##### `__init__`

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
iterable: true
container: true
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
settable: false
```

##### pad_layout

```yaml
kind: property
settable: false
listenable: true
raw_doc: The layout of pads on Push.
```

##### type_name

```yaml
kind: property
settable: false
```

##### control_values_arrived

```yaml
kind: property
listenable: true
```

##### midi_received

```yaml
kind: property
listenable: true
```

#### Methods

##### enable_receive_midi

```yaml
kind: method
signature: 'enable_receive_midi( (ControlSurfaceProxy)arg1, (bool)arg2) -> None :'
cpp_signature: void enable_receive_midi(APythonControlSurfaceProxy {lvalue},bool)
args:
- name: arg2
  type: bool
returns:
  type: None
```

##### fetch_received_midi_messages

```yaml
kind: method
signature: 'fetch_received_midi_messages( (ControlSurfaceProxy)arg1) -> tuple :'
cpp_signature: boost::python::tuple fetch_received_midi_messages(APythonControlSurfaceProxy {lvalue})
returns:
  type: tuple
```

##### fetch_received_values

```yaml
kind: method
signature: 'fetch_received_values( (ControlSurfaceProxy)arg1) -> tuple :'
cpp_signature: boost::python::tuple fetch_received_values(APythonControlSurfaceProxy {lvalue})
returns:
  type: tuple
```

##### grab_control

```yaml
kind: method
signature: 'grab_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :'
cpp_signature: void grab_control(APythonControlSurfaceProxy {lvalue},int)
args:
- name: arg2
  type: int
returns:
  type: None
```

##### release_control

```yaml
kind: method
signature: 'release_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :'
cpp_signature: void release_control(APythonControlSurfaceProxy {lvalue},int)
args:
- name: arg2
  type: int
returns:
  type: None
```

##### send_midi

```yaml
kind: method
signature: 'send_midi( (ControlSurfaceProxy)arg1, (tuple)arg2) -> None :'
cpp_signature: void send_midi(APythonControlSurfaceProxy {lvalue},boost::python::tuple)
args:
- name: arg2
  type: tuple
returns:
  type: None
```

##### send_value

```yaml
kind: method
signature: 'send_value( (ControlSurfaceProxy)arg1, (tuple)arg2) -> None :'
cpp_signature: void send_value(APythonControlSurfaceProxy {lvalue},boost::python::tuple)
args:
- name: arg2
  type: tuple
returns:
  type: None
```

##### subscribe_to_control

```yaml
kind: method
signature: 'subscribe_to_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :'
cpp_signature: void subscribe_to_control(APythonControlSurfaceProxy {lvalue},int)
args:
- name: arg2
  type: int
returns:
  type: None
```

##### unsubscribe_from_control

```yaml
kind: method
signature: 'unsubscribe_from_control( (ControlSurfaceProxy)arg1, (int)arg2) -> None :'
cpp_signature: void unsubscribe_from_control(APythonControlSurfaceProxy {lvalue},int)
args:
- name: arg2
  type: int
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
iterable: true
container: true
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

#### Methods

##### add_is_view_visible_listener

```yaml
kind: method
signature: 'add_is_view_visible_listener( (View)arg1, (object)arg2, (object)arg3) -> None :'
cpp_signature: void add_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
args:
- name: arg2
  type: str
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
signature: 'available_main_views( (View)arg1) -> StringVector :'
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
signature: 'focus_view( (View)arg1, (object)arg2) -> None :'
cpp_signature: void focus_view(TPyViewData<ASongApp>,TString)
args:
- name: arg2
  type: str
returns:
  type: None
raw_doc: Show and focus one through the identifier string specified view.
```

##### hide_view

```yaml
kind: method
signature: 'hide_view( (View)arg1, (object)arg2) -> None :'
cpp_signature: void hide_view(TPyViewData<ASongApp>,TString)
args:
- name: arg2
  type: str
returns:
  type: None
raw_doc: Hide one through the identifier string specified view.
```

##### is_view_visible

```yaml
kind: method
signature: 'is_view_visible( (View)arg1, (object)identifier [, (bool)main_window_only=True]) -> bool :'
cpp_signature: bool is_view_visible(TPyViewData<ASongApp>,TString [,bool=True])
args:
- name: identifier
  type: str
- name: main_window_only
  type: bool
  optional: true
  default: 'True'
returns:
  type: bool
raw_doc: |-
  Return true if the through the identifier string specified view is currently
  visible. If main_window_only is set to False, this will also check in second
  window. Notifications from the second window are not yet supported.
```

##### is_view_visible_has_listener

```yaml
kind: method
signature: 'is_view_visible_has_listener( (View)arg1, (object)arg2, (object)arg3) -> bool :'
cpp_signature: bool is_view_visible_has_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
args:
- name: arg2
  type: str
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
signature: 'remove_is_view_visible_listener( (View)arg1, (object)arg2, (object)arg3) -> None :'
cpp_signature: void remove_is_view_visible_listener(TPyViewData<ASongApp>,TString,boost::python::api::object)
args:
- name: arg2
  type: str
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
signature: 'scroll_view( (View)arg1, (int)arg2, (object)arg3, (bool)arg4) -> None :'
cpp_signature: void scroll_view(TPyViewData<ASongApp>,int,TString,bool)
args:
- name: arg2
  type: int
- name: arg3
  type: str
- name: arg4
  type: bool
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
signature: 'show_view( (View)arg1, (object)arg2) -> None :'
cpp_signature: void show_view(TPyViewData<ASongApp>,TString)
args:
- name: arg2
  type: str
returns:
  type: None
raw_doc: |-
  Show one through the identifier string specified view. Will throw a
  runtime error if this is called in Live's initialization scope.
```

##### toggle_browse

```yaml
kind: method
signature: 'toggle_browse( (View)arg1) -> None :'
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
signature: 'zoom_view( (View)arg1, (int)arg2, (object)arg3, (bool)arg4) -> None :'
cpp_signature: void zoom_view(TPyViewData<ASongApp>,int,TString,bool)
args:
- name: arg2
  type: int
- name: arg3
  type: str
- name: arg4
  type: bool
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
signature: 'combine_apcs() -> bool :'
cpp_signature: bool combine_apcs()
returns:
  type: bool
raw_doc: Returns true if multiple APCs should be combined.
```

### encrypt_challenge

```yaml
kind: function
signature: 'encrypt_challenge( (int)dongle1, (int)dongle2 [, (int)key_index=0]) -> tuple :'
cpp_signature: boost::python::tuple encrypt_challenge(int,int [,int=0])
args:
- name: dongle1
  type: int
- name: dongle2
  type: int
- name: key_index
  type: int
  optional: true
  default: '0'
returns:
  type: tuple
raw_doc: Returns an encrypted challenge based on the TEA algortithm
```

### encrypt_challenge2

```yaml
kind: function
signature: 'encrypt_challenge2( (int)arg1) -> int :'
cpp_signature: int encrypt_challenge2(int)
args:
- name: arg1
  type: int
returns:
  type: int
raw_doc: Returns the UMAC hash for the given challenge.
```

### get_application

```yaml
kind: function
signature: 'get_application() -> Application :'
cpp_signature: TWeakPtr<TPyHandle<ASongApp>> get_application()
returns:
  type: Live.Application.Application
raw_doc: Returns the application instance.
```

### get_random_int

```yaml
kind: function
signature: 'get_random_int( (int)arg1, (int)arg2) -> int :'
cpp_signature: int get_random_int(int,int)
args:
- name: arg1
  type: int
- name: arg2
  type: int
returns:
  type: int
raw_doc: Returns a random integer from the given range.
```

## Constants

### BETA

```yaml
kind: constant
parent: Variants
type: str
value: Beta
```

### INTRO

```yaml
kind: constant
parent: Variants
type: str
value: Intro
```

### LITE

```yaml
kind: constant
parent: Variants
type: str
value: Lite
```

### STANDARD

```yaml
kind: constant
parent: Variants
type: str
value: Standard
```

### SUITE

```yaml
kind: constant
parent: Variants
type: str
value: Suite
```

### TRIAL

```yaml
kind: constant
parent: Variants
type: str
value: Trial
```
