---
module: Licensing
---

Internal licensing and authorization plumbing used by Live's startup and
trial flows. The `PythonLicensingBridge` class drives session and product
identification, and `ProgressDialog` provides the modal UI shown during
authorization activity.

## Classes

### ProgressDialog

```yaml
kind: class
path: Live.Licensing.ProgressDialog
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: A modal dialog showing a message and a progress animation.
```

#### Methods

##### end_modal_loop

```yaml
kind: method
signature: 'end_modal_loop( (ProgressDialog)arg1) -> None :'
cpp_signature: void end_modal_loop(AProgressDialog {lvalue})
returns:
  type: None
```

##### run_in_modal_loop

```yaml
kind: method
signature: 'run_in_modal_loop( (ProgressDialog)arg1) -> None :'
cpp_signature: void run_in_modal_loop(AProgressDialog {lvalue})
returns:
  type: None
```

##### set_status_message

```yaml
kind: method
signature: 'set_status_message( (object)arg1, (str)msg) -> None :'
cpp_signature: void set_status_message(TWeakPtr<AProgressDialog>,std::__1::basic_string<char, std::__1::char_traits<char>,
  std::__1::allocator<char>>)
args:
- name: msg
  type: str
returns:
  type: None
```

### PythonLicensingBridge

```yaml
kind: class
path: Live.Licensing.PythonLicensingBridge
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Interface to the internal licensing services.
```

#### Properties

##### base_product_id

```yaml
kind: property
type: str
settable: false
raw_doc: Returns Live's current base product ID.
refinement:
  type:
    probed: null
    confidence: high
    sources:
    - '[docstring] "Returns Live''s current base product ID" — product IDs are string identifiers.'
```

##### in_sassafras_mode

```yaml
kind: property
type: bool
settable: false
refinement:
  type:
    probed: null
    confidence: low
    sources:
    - '[probe] property name pattern "in X mode" suggests boolean. No raw_doc, no usage snippets, no M4L doc — pure naming
      inference. Watch for drift if a probe ever reaches this property.'
```

##### license_must_match_variant

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns a bool indicating if we require the license information returned by the server to match the variant of Live.
refinement:
  type:
    probed: null
    confidence: high
    sources:
    - '[docstring] "Returns a bool indicating if we require..." — explicitly typed bool.'
```

##### random_number_for_trial_authorization

```yaml
kind: property
type: int
settable: false
raw_doc: Returns the integer to send along with the Trial authorization request. This same integer will be checked for in
  `process_trial_response` (and then changed).
refinement:
  type:
    probed: null
    confidence: high
    sources:
    - '[docstring] "Returns the integer to send along with the Trial authorization request".'
```

##### set_has_unsaved_changes

```yaml
kind: property
type: bool
settable: false
raw_doc: Returns true if the set has unsaved changes.
refinement:
  type:
    probed: null
    confidence: high
    sources:
    - '[docstring] "Returns true if the set has unsaved changes" — explicitly bool.'
```

#### Methods

##### authorize_with_sassafras

```yaml
kind: method
signature: 'authorize_with_sassafras( (PythonLicensingBridge)arg1) -> None :'
cpp_signature: void authorize_with_sassafras(APythonLicensingBridge {lvalue})
returns:
  type: None
```

##### create_new_live_set

```yaml
kind: method
signature: 'create_new_live_set( (PythonLicensingBridge)arg1) -> None :'
cpp_signature: void create_new_live_set(APythonLicensingBridge {lvalue})
returns:
  type: None
raw_doc: Creates a new live set and discards unsaved changes.
```

##### deauthenticate_user

```yaml
kind: method
signature: 'deauthenticate_user( (PythonLicensingBridge)arg1) -> None :'
cpp_signature: void deauthenticate_user(APythonLicensingBridge {lvalue})
returns:
  type: None
raw_doc: Deletes the current session ID.
```

##### get_progress_dialog

```yaml
kind: method
signature: 'get_progress_dialog( (PythonLicensingBridge)arg1) -> ProgressDialog :'
cpp_signature: TWeakPtr<AProgressDialog> get_progress_dialog(APythonLicensingBridge {lvalue})
returns:
  type: Live.Licensing.ProgressDialog
raw_doc: Retrieves an instance of ProgressDialog.
```

##### get_session_id

```yaml
kind: method
signature: 'get_session_id( (PythonLicensingBridge)arg1) -> str :'
cpp_signature: std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> get_session_id(APythonLicensingBridge
  {lvalue})
returns:
  type: str
raw_doc: Retrieve stored session ID.
```

##### get_startup_dialog

```yaml
kind: method
signature: 'get_startup_dialog( (PythonLicensingBridge)arg1, (object)authorize_callable, (object)authorize_later_callable)
  -> StartupDialog :'
cpp_signature: TWeakPtr<AStartupDialog> get_startup_dialog(APythonLicensingBridge {lvalue},boost::python::api::object,boost::python::api::object)
args:
- name: authorize_callable
  type: Callable
  refinement:
    type:
      probed: object
      confidence: high
      sources:
      - '[docstring] "callables connected to its buttons" — both args are callback functions.'
- name: authorize_later_callable
  type: Callable
  refinement:
    type:
      probed: object
      confidence: high
      sources:
      - '[docstring] "callables connected to its buttons" — both args are callback functions.'
returns:
  type: Live.Licensing.StartupDialog
raw_doc: Retrieves an instance of the startup dialog with the passed callables connected to its buttons.
```

##### get_trial_time_left

```yaml
kind: method
signature: 'get_trial_time_left( (PythonLicensingBridge)arg1) -> str :'
cpp_signature: TString get_trial_time_left(APythonLicensingBridge {lvalue})
returns:
  type: str
raw_doc: Returns remaining time on a trial as a formatted string.
```

##### invoke_pack_installation_callback

```yaml
kind: method
signature: 'invoke_pack_installation_callback( (PythonLicensingBridge)arg1) -> None :'
cpp_signature: void invoke_pack_installation_callback(APythonLicensingBridge {lvalue})
returns:
  type: None
raw_doc: Call package installation callback.
```

##### load_and_convert_legacy_unlock_cfg

```yaml
kind: method
signature: 'load_and_convert_legacy_unlock_cfg( (PythonLicensingBridge)arg1) -> dict :'
cpp_signature: boost::python::dict load_and_convert_legacy_unlock_cfg(APythonLicensingBridge {lvalue})
returns:
  type: dict[str, Any]
  refinement:
    type:
      probed: dict
      confidence: high
      sources:
      - '[docstring] "Loads the Unlock.cfg file and returns either an empty dict or one that can be converted to an UnlockData
        object."'
      - '[C++ signature] explicitly returns `boost::python::dict`.'
      - '[probe] the dict''s keys/values aren''t enumerated in the docs (varies with the legacy cfg format), so `dict[str,
        Any]` is the honest parameterization.'
raw_doc: Loads the Unlock.cfg file and returns either an empty dict or one that can be converted to an UnlockData object.
```

##### process_license_response

```yaml
kind: method
signature: 'process_license_response( (PythonLicensingBridge)arg1, (list)license_response_lines) -> UnlockStatus :'
cpp_signature: TUnlockStatus process_license_response(APythonLicensingBridge {lvalue},boost::python::list)
args:
- name: license_response_lines
  type: list[str]
  refinement:
    type:
      probed: list
      confidence: high
      sources:
      - '[docstring] "list of strings, each representing a server response".'
returns:
  type: Live.Licensing.UnlockStatus
raw_doc: Processes a list of strings, each representing a server response to a product authorization.
```

##### process_trial_response

```yaml
kind: method
signature: 'process_trial_response( (PythonLicensingBridge)arg1, (str)trial_response_line) -> bool :'
cpp_signature: bool process_trial_response(APythonLicensingBridge {lvalue},std::__1::basic_string<char, std::__1::char_traits<char>,
  std::__1::allocator<char>>)
args:
- name: trial_response_line
  type: str
returns:
  type: bool
raw_doc: Process the server's response to a Trial authorization.
```

##### request_exit

```yaml
kind: method
signature: 'request_exit( (PythonLicensingBridge)arg1 [, (int)exit_code=0]) -> None :'
cpp_signature: void request_exit(APythonLicensingBridge {lvalue} [,int=0])
args:
- name: exit_code
  type: int
  optional: true
  default: '0'
returns:
  type: None
```

##### save_current_set

```yaml
kind: method
signature: 'save_current_set( (PythonLicensingBridge)arg1) -> None :'
cpp_signature: void save_current_set(APythonLicensingBridge {lvalue})
returns:
  type: None
raw_doc: Saves the current Live session.
```

##### set_network_timer

```yaml
kind: method
signature: 'set_network_timer( (PythonLicensingBridge)arg1, (object)callback, (int)interval_in_ms) -> None :'
cpp_signature: void set_network_timer(APythonLicensingBridge {lvalue},boost::python::api::object,int)
args:
- name: callback
  type: Callable | None
  refinement:
    type:
      probed: object
      confidence: high
      sources:
      - '[docstring] "Pass None as callback to stop the timer".'
- name: interval_in_ms
  type: int
returns:
  type: None
raw_doc: Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer. If any callback
  invocation raises an exception, the timer is stopped.
```

##### store_session_id

```yaml
kind: method
signature: 'store_session_id( (PythonLicensingBridge)arg1, (str)session_id) -> None :'
cpp_signature: void store_session_id(APythonLicensingBridge {lvalue},std::__1::basic_string<char, std::__1::char_traits<char>,
  std::__1::allocator<char>>)
args:
- name: session_id
  type: str
returns:
  type: None
raw_doc: Securely stores the user's session ID (aka cookie, aka credentials).
```

### StartupDialog

```yaml
kind: class
path: Live.Licensing.StartupDialog
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: Serves as an entry point for the user to authorize Live on first launch.
```

#### Methods

##### end_modal_loop

```yaml
kind: method
signature: 'end_modal_loop( (StartupDialog)arg1) -> None :'
cpp_signature: void end_modal_loop(AStartupDialog {lvalue})
returns:
  type: None
```

##### run_in_modal_loop

```yaml
kind: method
signature: 'run_in_modal_loop( (StartupDialog)arg1, (bool)show_only_offline_auth_instructions) -> None :'
cpp_signature: void run_in_modal_loop(AStartupDialog {lvalue},bool)
args:
- name: show_only_offline_auth_instructions
  type: bool
returns:
  type: None
```

##### set_notification_message

```yaml
kind: method
signature: 'set_notification_message( (StartupDialog)arg1, (object)notification_text, (bool)show_progress_bar) -> None :'
cpp_signature: void set_notification_message(AStartupDialog {lvalue},TString,bool)
args:
- name: notification_text
  type: str
- name: show_progress_bar
  type: bool
returns:
  type: None
```

### UnlockStatus

```yaml
kind: class
path: Live.Licensing.UnlockStatus
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1) -> None :

      C++ signature :
          void __init__(_object*)
constructable: true
raw_doc: Returns relevant information after unlock
```

#### Properties

##### authorization_deactivated

```yaml
kind: property
type: bool
settable: false
```

##### authorization_expired

```yaml
kind: property
type: bool
settable: false
```

##### has_max_unlock_products

```yaml
kind: property
type: bool
settable: false
```

##### temp_demo_mode

```yaml
kind: property
type: bool
settable: false
```

##### time_limited

```yaml
kind: property
type: bool
settable: false
```

##### unlock_error

```yaml
kind: property
type: bool
settable: false
```

##### unlocked

```yaml
kind: property
type: bool
settable: false
```

#### Methods

##### `__init__`

```yaml
kind: method
returns:
  type: None
```

## Enums

### TrialContext

```yaml
kind: enum
members:
  SAVE: 0
  FORCE_UPDATE: 2
  STARTUP: 3
```

## Functions

### authorization_clock_days_ahead

```yaml
kind: function
signature: 'authorization_clock_days_ahead() -> int :'
cpp_signature: int authorization_clock_days_ahead()
returns:
  type: int
raw_doc: Advances the current date by the number of days specified by _AuthClockDaysAhead
```

### get_authorization_page_url

```yaml
kind: function
signature: 'get_authorization_page_url( (bool)reauthorize, (bool)is_trial) -> str :'
cpp_signature: TString get_authorization_page_url(bool,bool)
args:
- name: reauthorize
  type: bool
- name: is_trial
  type: bool
returns:
  type: str
raw_doc: Retrieves the appopriate URL on ableton.com where the unser can initiate the authorization.
```

### get_purchase_live_url

```yaml
kind: function
signature: 'get_purchase_live_url() -> str :'
cpp_signature: std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> get_purchase_live_url()
returns:
  type: str
raw_doc: Returns the environment-aware purchase URL for purchasing Live licenses
```

### get_services_url

```yaml
kind: function
signature: 'get_services_url() -> str :'
cpp_signature: std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> get_services_url()
returns:
  type: str
raw_doc: Returns the URL against which service calls (e.g. for authorization) can be performed.
```

### get_unlock_dir

```yaml
kind: function
signature: 'get_unlock_dir() -> tuple :'
cpp_signature: boost::python::tuple get_unlock_dir()
returns:
  type: tuple[str, bool]
  refinement:
    type:
      probed: tuple[object, ...]
      confidence: high
      sources:
      - '[docstring] "Returns a tuple containing the unlock file directory and a flag" — directory is str, flag is bool.'
      - '[probe] probe stamps `tuple` with element_reprs `[str, bool]`; this refinement narrows to the fixed-position tuple
        shape.'
raw_doc: Returns a tuple containing the unlock file directory and a flag indicating if the unlock file is in the system domain.
```

### launch_web_browser

```yaml
kind: function
signature: 'launch_web_browser( (str)url) -> None :'
cpp_signature: void launch_web_browser(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
args:
- name: url
  type: str
returns:
  type: None
raw_doc: Opens a web browser at the specified URL on the user's computer.
```
