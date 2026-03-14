# Application

> `Live.Application.Application`

This class represents the Live application itself. It is the top-level entry point for the Live Object Model,
reachable via the root path `live_app`. The Application object provides access to version information, CPU usage
metrics, dialog management, the current Live Set (via `get_document()`), the browser, control surfaces, and the
application view. It also exposes several module-level static functions (e.g., `get_application()`) and nested
enum classes (`MessageButtons`, `PushDialogType`, `UnavailableFeature`, `Variants`).

### Open Questions

- What are the actual enum values inside `MessageButtons`? The stub defines `OK_BUTTON` as the default but does
  not enumerate the full set (e.g., OK/Cancel, Yes/No).
- What are the actual enum values inside `PushDialogType`? The stub only references `MESSAGE_BOX` as a default.
- What are the string values inside `Variants`? The stub says "holds strings representing what type of Live is
  running" but does not list them (e.g., "Live", "Intro", "Lite", "Suite", "Beta"?).
- What are the values inside `UnavailableFeature`? No members are listed in the stub.
- The stub exposes `number_of_push_apps_running` — is this useful outside of Ableton's internal Push support code?
- `show_message()` and `show_on_the_fly_message()` are in the stub but not in the Max docs. Are they accessible
  from Max for Live, or only from control surface scripts?
- `has_option()` checks for entries in `Options.txt` — what options are valid, and is this accessible from Max
  for Live?
- The module-level statics (`combine_apcs`, `encrypt_challenge`, `encrypt_challenge2`, `get_random_int`) appear
  to be internal utilities. Are any of them useful for M4L?
- `get_build_id()` and `get_variant()` are in the stub but not the Max docs — are they accessible from Max for
  Live?
- `control_surfaces` returns a list that may contain `None` entries for inactive slots. The Max docs say `id 0`
  is returned instead. Which is accurate for the Python API?

### Children

| Child | Returns | Shape | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `browser` | `Browser` | `single` | `no` | Interface to Live's browser. |
| `control_surfaces` | `Sequence[ControlSurfaceProxy?]` | `list` | `yes` | Control surfaces selected in Preferences. |
| `view` | `Application.View` | `single` | `no` | View aspects of the application. |

#### `browser`

- **Returns:** `Browser`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

Returns an interface to Live's content browser. The `Browser` class itself is documented separately. This child
is present in the stub but not mentioned in the Max for Live Application docs.

#### `control_surfaces`

- **Returns:** `Sequence[ControlSurfaceProxy?]`
- **Shape:** `list`
- **Listenable:** `yes`
- **Since:** `<11`

A read-only list of the control surfaces currently selected in Live's Preferences, in the same order as the
Preferences dialog. Each entry is a `ControlSurfaceProxy` object or `None` if no control surface is active at
that slot. The listener fires when the set of active control surfaces changes.

#### `view`

- **Returns:** `Application.View`
- **Shape:** `single`
- **Listenable:** `no`
- **Since:** `<11`

The view component of the application, providing access to visibility state and focus management for Live's main
view panels (Session, Arranger, Browser, Detail, etc.).

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `average_process_usage` | `float` | `no` | `yes` | Live's average CPU load. |
| `canonical_parent` | `object` | `no` | `no` | The canonical parent of the application. |
| `current_dialog_button_count` | `int` | `no` | `no` | Number of buttons on the current dialog. |
| `current_dialog_message` | `str` | `no` | `no` | Text of the last dialog shown; empty if no dialog is open. |
| `number_of_push_apps_running` | `int` | `no` | `no` | Number of connected Push apps. |
| `open_dialog_count` | `int` | `no` | `yes` | Number of currently open dialogs. |
| `peak_process_usage` | `float` | `no` | `yes` | Live's peak CPU load. |
| `unavailable_features` | `UnavailableFeatureVector` | `no` | `yes` | Features unavailable in the current Live edition. |

#### `average_process_usage`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.1`

Reports Live's average CPU load. The Max docs note that Live's CPU meter shows audio processing load specifically,
not the application's overall CPU usage. The listener fires whenever the reported average changes.

#### `canonical_parent`

- **Type:** `object`
- **Listenable:** `no`
- **Since:** `<11`

Returns the canonical parent of the Application object. Since Application is the root of the object hierarchy,
this likely returns `None` or a module-level wrapper.

#### `current_dialog_button_count`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

The number of buttons in the currently displayed message box. Useful in conjunction with
`press_current_dialog_button()` to programmatically dismiss or respond to dialogs.

#### `current_dialog_message`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

The text content of the last dialog that appeared. Returns an empty string if no dialogs are currently shown.

#### `number_of_push_apps_running`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `11.3`

Returns the number of Push hardware controllers currently connected and running their companion apps. Likely only
relevant for Ableton's internal Push support code.

#### `open_dialog_count`

- **Type:** `int`
- **Listenable:** `yes`
- **Since:** `<11`

The number of currently open dialog boxes in Live. Returns `0` if no dialog is open. The listener fires when a
dialog opens or closes, making it useful for detecting when dialogs appear and need programmatic handling via
`press_current_dialog_button()`.

#### `peak_process_usage`

- **Type:** `float`
- **Listenable:** `yes`
- **Since:** `11.1`

Reports Live's peak CPU load. As with `average_process_usage`, the Max docs note that Live's CPU meter shows
audio processing load, not overall CPU usage.

#### `unavailable_features`

- **Type:** `UnavailableFeatureVector`
- **Listenable:** `yes`
- **Since:** `<11`

A list of features that are unavailable due to limitations of the current Live edition (e.g., features missing
in Live Intro or Lite compared to Suite). The listener fires when the set of unavailable features changes.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `get_bugfix_version()` | `int` | Bugfix version number (e.g., 5 in 12.3.5). |
| `get_build_id()` | `str` | Build identifier string. |
| `get_document()` | `Song` | Returns the current Live Set. |
| `get_major_version()` | `int` | Major version number (e.g., 12 in 12.3.5). |
| `get_minor_version()` | `int` | Minor version number (e.g., 3 in 12.3.5). |
| `get_variant()` | `str` | Live edition variant string (one of `Variants`). |
| `get_version_string()` | `str` | Full version string (e.g., `"12.3.5"`). |
| `has_option(option_name)` | `bool` | Whether an entry exists in `Options.txt`. |
| `press_current_dialog_button(index)` | `None` | Press a button by index on the current dialog. |
| `show_message(text, buttons?, enable_markup?, show_success_icon?)` | `int` | Show a message box and return the pressed button index. |
| `show_on_the_fly_message(message, buttons?, enable_markup?, ...)` | `int` | Show a message box with a raw string instead of a Text object. |

#### `get_bugfix_version()`

- **Returns:** `int`
- **Args:** None
- **Since:** `<11`

Returns the bugfix (patch) version number of the running Live instance. For example, returns `5` for Live 12.3.5.

#### `get_build_id()`

- **Returns:** `str`
- **Args:** None
- **Since:** `12.0`

Returns a string identifying the specific build of Live. Useful for debugging or identifying exact build versions
beyond the public version number.

#### `get_document()`

- **Returns:** `Song`
- **Args:** None
- **Since:** `<11`

Returns the current Live Set as a `Song` object. This is the primary way to navigate from the application level
down into the document (tracks, scenes, clips, etc.).

#### `get_major_version()`

- **Returns:** `int`
- **Args:** None
- **Since:** `<11`

Returns the major version number of the running Live instance. For example, returns `12` for Live 12.3.5.

#### `get_minor_version()`

- **Returns:** `int`
- **Args:** None
- **Since:** `<11`

Returns the minor version number of the running Live instance. For example, returns `3` for Live 12.3.5.

#### `get_variant()`

- **Returns:** `str`
- **Args:** None
- **Since:** `12.0`

Returns a string from the `Application.Variants` enum identifying which edition of Live is running (e.g., "Live",
"Suite", "Intro", "Lite" — exact values unknown, needs probing).

#### `get_version_string()`

- **Returns:** `str`
- **Args:** None
- **Since:** `11.2`

Returns the full version string of the running Live instance (e.g., `"12.3.5"`).

#### `has_option(option_name)`

- **Returns:** `bool`
- **Args:**
  - `option_name: str` — the option key to look up
- **Since:** `<11`

Returns `True` if the given entry exists in Live's `Options.txt` file, `False` otherwise. `Options.txt` is a
text file in Live's Preferences folder that holds undocumented feature flags and configuration overrides.

#### `press_current_dialog_button(index)`

- **Returns:** `None`
- **Args:**
  - `index: int` — zero-based index of the button to press
- **Since:** `<11`

Programmatically presses a button on the currently displayed message box. Use `current_dialog_button_count` to
determine how many buttons are available, and `open_dialog_count` or its listener to detect when a dialog appears.

#### `show_message(text, buttons?, enable_markup?, show_success_icon?)`

- **Returns:** `int` — the index of the pressed button
- **Args:**
  - `text: Text` — a predefined text object to display
  - `buttons: int` (optional, default `MessageButtons.OK_BUTTON`) — which buttons to show
  - `enable_markup: bool` (optional, default `False`) — whether to enable markup rendering
  - `show_success_icon: bool` (optional, default `False`) — whether to show a success icon
- **Since:** `12.0`

Shows a message box with the given predefined `Text` object and returns the index of the button pressed by the
user. Not documented in the Max for Live docs — may only be available from control surface scripts.

#### `show_on_the_fly_message(message, buttons?, enable_markup?, show_success_icon?, push_dialog_type?)`

- **Returns:** `int` — the index of the pressed button
- **Args:**
  - `message: str` — the message string to display
  - `buttons: int` (optional, default `MessageButtons.OK_BUTTON`) — which buttons to show
  - `enable_markup: bool` (optional, default `False`) — whether to enable markup rendering
  - `show_success_icon: bool` (optional, default `False`) — whether to show a success icon
  - `push_dialog_type: int` (optional, default `PushDialogType.MESSAGE_BOX`) — dialog type for Push display
- **Since:** `12.0`

Same as `show_message()`, but accepts a raw string instead of a predefined `Text` object. This allows displaying
arbitrary text at runtime. Not documented in the Max for Live docs — may only be available from control surface
scripts.

---

## Application.View

> `Live.Application.Application.View`

Represents the view aspects of the Live application, providing control over which panels are visible and focused
(Session, Arranger, Browser, Detail, etc.). Reachable via `live_app view`.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `browse_mode` | `bool` | `no` | `yes` | Whether Hot-Swap mode is active for any target. |
| `canonical_parent` | `object` | `no` | `no` | The canonical parent of the application view. |
| `focused_document_view` | `str` | `no` | `yes` | Name of the focused document view (`"Session"` or `"Arranger"`). |

#### `browse_mode`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` if Hot-Swap mode is active for any target (i.e., the user or a script has engaged browser hot-swap to
replace a device, sample, or preset). The listener fires when Hot-Swap mode is toggled on or off.

#### `canonical_parent`

- **Type:** `object`
- **Listenable:** `no`
- **Since:** `<11`

Returns the canonical parent of the application view, which is the `Application` object.

#### `focused_document_view`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

Returns the name of the document view shown in the currently focused window — either `"Session"` or `"Arranger"`.
The listener fires when the user switches between Session and Arrangement view.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `available_main_views()` | `StringVector` | List of valid view identifier strings. |
| `focus_view(view_name)` | `None` | Show and focus the named view. |
| `hide_view(view_name)` | `None` | Hide the named view. |
| `is_view_visible(identifier, main_window_only?)` | `bool` | Whether the named view is currently visible. |
| `scroll_view(direction, view_name, modifier_pressed)` | `None` | Scroll the named view in the given direction. |
| `show_view(view_name)` | `None` | Show the named view. |
| `toggle_browse()` | `None` | Toggle Hot-Swap mode for the selected device. |
| `zoom_view(direction, view_name, modifier_pressed)` | `None` | Zoom the named view in the given direction. |

#### `available_main_views()`

- **Returns:** `StringVector`
- **Args:** None
- **Since:** `<11`

Returns a constant list of view name strings that can be used as arguments to the other view methods
(`show_view`, `hide_view`, `focus_view`, `is_view_visible`, `scroll_view`, `zoom_view`). The Max docs list these
as: `Browser`, `Arranger`, `Session`, `Detail`, `Detail/Clip`, `Detail/DeviceChain`.

#### `focus_view(view_name)`

- **Returns:** `None`
- **Args:**
  - `view_name: str` — one of the identifiers from `available_main_views()`
- **Since:** `<11`

Shows the named view and gives it keyboard focus. You can pass an empty string `" "` to refer to whichever of
the Arrangement or Session View is currently visible in the main window.

#### `hide_view(view_name)`

- **Returns:** `None`
- **Args:**
  - `view_name: str` — one of the identifiers from `available_main_views()`
- **Since:** `<11`

Hides the named view. Passing an empty string `" "` refers to whichever of the Arrangement or Session View is
visible in the main window.

#### `is_view_visible(identifier, main_window_only?)`

- **Returns:** `bool`
- **Args:**
  - `identifier: str` — the view name to check
  - `main_window_only: bool` (optional, default `True`) — if `False`, also checks the second window
- **Since:** `<11`

Returns `True` if the named view is currently visible. By default, only checks the main window. This property
also supports a listener via `add_is_view_visible_listener(view_name, callback)` — note the listener takes the
view name as a first argument, making it a parameterized listener.

#### `scroll_view(direction, view_name, modifier_pressed)`

- **Returns:** `None`
- **Args:**
  - `direction: int` — `0`=up, `1`=down, `2`=left, `3`=right
  - `view_name: str` — one of the identifiers from `available_main_views()`
  - `modifier_pressed: bool` — modifies behavior in certain views
- **Since:** `<11`

Scrolls the named view in the given direction. Not all views support scrolling in all directions. An empty string
`" "` refers to the currently visible Arrangement or Session View.

- **Quirks:** `modifier_pressed` only affects **Arranger** scroll. Arranger left/right: modifier changes from
  "move cursor" to "resize selection region" (shift+arrow equivalent). Session scroll moves track/scene selection.
  Detail/DeviceChain only responds to left/right (device selection). Browser works all 4 directions.

#### `show_view(view_name)`

- **Returns:** `None`
- **Args:**
  - `view_name: str` — one of the identifiers from `available_main_views()`
- **Raises:** Raises a runtime error if called during Live's initialization scope.
- **Since:** `<11`

Shows the named view. Calling this during Live's initialization phase will throw a runtime error — use it only
after initialization is complete.

#### `toggle_browse()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Reveals the device chain and the browser, and activates Hot-Swap mode for the currently selected device. Calling
this again deactivates Hot-Swap mode. Equivalent to clicking the Hot-Swap button on a device.

- **Quirks:** Targets the **selected** device (white outline), not the **appointed** device (blue hand). Once
  hotswap is active, changing the selection does not redirect `hotswap_target`. Setting `Browser.hotswap_target`
  directly is a simpler alternative to `select_device()` + `toggle_browse()`.

#### `zoom_view(direction, view_name, modifier_pressed)`

- **Returns:** `None`
- **Args:**
  - `direction: int` — `0`=up, `1`=down, `2`=left, `3`=right
  - `view_name: str` — one of the identifiers from `available_main_views()`
  - `modifier_pressed: bool` — modifies behavior in certain views
- **Since:** `<11`

Zooms the named view in the given direction. An empty string `" "` refers to the currently visible Arrangement
or Session View.

- **Quirks:** Only the Arranger actually zooms. Session zoom is identical to Session scroll. `modifier_pressed`
  only affects Arranger up/down zoom: without modifier, changes the selected track's height; with modifier,
  changes all track heights simultaneously. Left/right (timeline zoom) are unaffected by modifier.
