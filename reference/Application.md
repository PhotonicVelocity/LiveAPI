# Application

## Application

This class represents the Live application itself. It is the top-level entry point for the
Live Object Model, reachable via the root path `live_app`. The Application object provides
access to version information, CPU usage metrics, dialog management, the current Live Set
(via `get_document()`), the browser, control surfaces, and the application view. It also
exposes several module-level static functions (e.g., `get_application()`) and nested enum
classes (`MessageButtons`, `PushDialogType`, `UnavailableFeature`, `Variants`).

### Sources

- **Primary:** `Live/classes/Application.py` (stub dump)
- **Secondary:** `MaxForLive/application.md`, `MaxForLive/application_view.md`
- **Probes:** None

### Probe Notes

None yet.

### Open Questions

- What are the actual enum values inside `MessageButtons`? The stub defines `OK_BUTTON` as
  the default but does not enumerate the full set (e.g., OK/Cancel, Yes/No).
- What are the actual enum values inside `PushDialogType`? The stub only references
  `MESSAGE_BOX` as a default.
- What are the string values inside `Variants`? The stub says "holds strings representing
  what type of Live is running" but does not list them (e.g., "Live", "Intro", "Lite",
  "Suite", "Beta"?).
- What are the values inside `UnavailableFeature`? No members are listed in the stub.
- The stub exposes `number_of_push_apps_running` — is this useful outside of Ableton's
  internal Push support code?
- `show_message()` and `show_on_the_fly_message()` are in the stub but not in the Max docs.
  Are they accessible from Max for Live, or only from control surface scripts?
- `has_option()` checks for entries in `Options.txt` — what options are valid, and is this
  accessible from Max for Live?
- The module-level statics (`combine_apcs`, `encrypt_challenge`, `encrypt_challenge2`,
  `get_random_int`) appear to be internal utilities. Are any of them useful for M4L?
- `get_build_id()` and `get_variant()` are in the stub but not the Max docs — are they
  accessible from Max for Live?
- `control_surfaces` returns a list that may contain `None` entries for inactive slots.
  The Max docs say `id 0` is returned instead. Which is accurate for the Python API?

### Children

| Child              | Returns                          | Shape    | Access | Listenable | Available Since | Summary                                   |
| ------------------ | -------------------------------- | -------- | ------ | ---------- | --------------- | ----------------------------------------- |
| `browser`          | `Browser`                        | `single` | `get`  | `no`       | `<11`           | Interface to Live's browser.              |
| `control_surfaces` | `Sequence[ControlSurfaceProxy?]` | `list`   | `get`  | `yes`      | `<11`           | Control surfaces selected in Preferences. |
| `view`             | `Application.View`               | `single` | `get`  | `no`       | `<11`           | View aspects of the application.          |

#### `browser`

- **Returns:** `Browser`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns an interface to Live's content browser. The `Browser` class itself is documented
separately. This child is present in the stub but not mentioned in the Max for Live
Application docs.

#### `control_surfaces`

- **Returns:** `Sequence[ControlSurfaceProxy?]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
A read-only list of the control surfaces currently selected in Live's Preferences, in
the same order as the Preferences dialog. Each entry is a `ControlSurfaceProxy` object or
`None` if no control surface is active at that slot. The Max docs note that `id 0` is
returned for inactive slots. The listener fires when the set of active control surfaces
changes. `ControlSurfaceProxy` provides methods for interacting with control surfaces from
Max for Live (grabbing/releasing controls, sending/receiving MIDI and values).

#### `view`

- **Returns:** `Application.View`
- **Shape:** `single`
- **Access:** `get`
- **Listenable:** `no`
- **Applicable to:** `all`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The view component of the application, providing access to visibility state and focus
management for Live's main view panels (Session, Arranger, Browser, Detail, etc.).

### Properties

| Property                      | Get Returns                | Set Accepts | Listenable | Available Since | Summary                                                    |
| ----------------------------- | -------------------------- | ----------- | ---------- | --------------- | ---------------------------------------------------------- |
| `average_process_usage`       | `float`                    | —           | `yes`      | `11.1`          | Live's average CPU load.                                   |
| `canonical_parent`            | `object`                   | —           | `no`       | `<11`           | The canonical parent of the application.                   |
| `current_dialog_button_count` | `int`                      | —           | `no`       | `<11`           | Number of buttons on the current dialog.                   |
| `current_dialog_message`      | `str`                      | —           | `no`       | `<11`           | Text of the last dialog shown; empty if no dialog is open. |
| `number_of_push_apps_running` | `int`                      | —           | `no`       | `11.3`          | Number of connected Push apps.                             |
| `open_dialog_count`           | `int`                      | —           | `yes`      | `<11`           | Number of currently open dialogs.                          |
| `peak_process_usage`          | `float`                    | —           | `yes`      | `11.1`          | Live's peak CPU load.                                      |
| `unavailable_features`        | `UnavailableFeatureVector` | —           | `yes`      | `<11`           | Features unavailable in the current Live edition.          |

#### `average_process_usage`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.1`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Reports Live's average CPU load. The Max docs note that Live's CPU meter shows audio
processing load specifically, not the application's overall CPU usage. The listener fires
whenever the reported average changes.

#### `canonical_parent`

- **Get Returns:** `object`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns the canonical parent of the Application object. Since Application is the root of
the object hierarchy, this likely returns `None` or a module-level wrapper.

#### `current_dialog_button_count`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The number of buttons in the currently displayed message box. Useful in conjunction with
`press_current_dialog_button()` to programmatically dismiss or respond to dialogs.

#### `current_dialog_message`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The text content of the last dialog that appeared. Returns an empty string if no dialogs
are currently shown (i.e., all dialogs have been dismissed).

#### `number_of_push_apps_running`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `11.3`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns the number of Push hardware controllers currently connected and running their
companion apps. Likely only relevant for Ableton's internal Push support code.

#### `open_dialog_count`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
The number of currently open dialog boxes in Live. Returns `0` if no dialog is open. The
listener fires when a dialog opens or closes, making it useful for detecting when dialogs
appear and need programmatic handling via `press_current_dialog_button()`.

#### `peak_process_usage`

- **Get Returns:** `float`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `11.1`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Reports Live's peak CPU load. As with `average_process_usage`, the Max docs note that
Live's CPU meter shows audio processing load, not overall CPU usage. The listener fires
whenever the reported peak changes.

#### `unavailable_features`

- **Get Returns:** `UnavailableFeatureVector`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
A list of features that are unavailable due to limitations of the current Live edition
(e.g., features missing in Live Intro or Lite compared to Suite). Returns an
`UnavailableFeatureVector` containing `UnavailableFeature` enum values. The listener fires
when the set of unavailable features changes.

### Methods

| Signature                                                          | Returns | Available Since | Summary                                                        |
| ------------------------------------------------------------------ | ------- | --------------- | -------------------------------------------------------------- |
| `get_bugfix_version()`                                             | `int`   | `<11`           | Bugfix version number (e.g., 5 in 12.3.5).                     |
| `get_build_id()`                                                   | `str`   | `12.0`          | Build identifier string.                                       |
| `get_document()`                                                   | `Song`  | `<11`           | Returns the current Live Set.                                  |
| `get_major_version()`                                              | `int`   | `<11`           | Major version number (e.g., 12 in 12.3.5).                     |
| `get_minor_version()`                                              | `int`   | `<11`           | Minor version number (e.g., 3 in 12.3.5).                      |
| `get_variant()`                                                    | `str`   | `12.0`          | Live edition variant string (one of `Variants`).               |
| `get_version_string()`                                             | `str`   | `11.2`          | Full version string (e.g., `"12.3.5"`).                        |
| `has_option(option_name)`                                          | `bool`  | `<11`           | Whether an entry exists in `Options.txt`.                      |
| `press_current_dialog_button(index)`                               | `None`  | `<11`           | Press a button by index on the current dialog.                 |
| `show_message(text, buttons?, enable_markup?, show_success_icon?)` | `int`   | `12.0`          | Show a message box and return the pressed button index.        |
| `show_on_the_fly_message(message, buttons?, enable_markup?, ...)`  | `int`   | `12.0`          | Show a message box with a raw string instead of a Text object. |

#### `get_bugfix_version()`

- **Returns:** `int`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns the bugfix (patch) version number of the running Live instance. For example,
returns `5` for Live 12.3.5. The Max docs illustrate this as "the 2 in Live 9.1.2."

#### `get_build_id()`

- **Returns:** `str`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `12.0`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns a string identifying the specific build of Live. Useful for debugging or
identifying exact build versions beyond the public version number.

#### `get_document()`

- **Returns:** `Song`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns the current Live Set as a `Song` object. This is the primary way to navigate from
the application level down into the document (tracks, scenes, clips, etc.).

#### `get_major_version()`

- **Returns:** `int`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns the major version number of the running Live instance. For example, returns `12`
for Live 12.3.5. The Max docs illustrate this as "the 9 in Live 9.1.2."

#### `get_minor_version()`

- **Returns:** `int`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns the minor version number of the running Live instance. For example, returns `3`
for Live 12.3.5. The Max docs illustrate this as "the 1 in Live 9.1.2."

#### `get_variant()`

- **Returns:** `str`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `12.0`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns a string from the `Application.Variants` enum identifying which edition of Live is
running (e.g., "Live", "Suite", "Intro", "Lite" — exact values unknown, needs probing).

#### `get_version_string()`

- **Returns:** `str`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `11.2`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns the full version string of the running Live instance (e.g., `"12.3.5"`).

#### `has_option(option_name)`

- **Returns:** `bool`
- **Args:**
  - `option_name: str` — the option key to look up
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns `True` if the given entry exists in Live's `Options.txt` file, `False` otherwise.
`Options.txt` is a text file in Live's Preferences folder that holds undocumented feature
flags and configuration overrides.

#### `press_current_dialog_button(index)`

- **Returns:** `None`
- **Args:**
  - `index: int` — zero-based index of the button to press
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** Dismisses the current dialog by pressing the specified button.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Programmatically presses a button on the currently displayed message box. The button is
identified by its zero-based index. Use `current_dialog_button_count` to determine how many
buttons are available, and `open_dialog_count` or its listener to detect when a dialog
appears.

#### `show_message(text, buttons?, enable_markup?, show_success_icon?)`

- **Returns:** `int` — the index of the pressed button
- **Args:**
  - `text: Text` — a predefined text object to display
  - `buttons: int` (optional, default `MessageButtons.OK_BUTTON`) — which buttons to show
  - `enable_markup: bool` (optional, default `False`) — whether to enable markup rendering
  - `show_success_icon: bool` (optional, default `False`) — whether to show a success icon
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** Displays a modal message box in Live.
- **Async visibility:** `Unknown`
- **Available Since:** `12.0`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Shows a message box with the given predefined `Text` object and returns the index of the
button pressed by the user. The `buttons` parameter accepts a `MessageButtons` enum value
to control which buttons are displayed (e.g., OK only, OK/Cancel). Not documented in the
Max for Live docs — may only be available from control surface scripts.

#### `show_on_the_fly_message(message, buttons?, enable_markup?, show_success_icon?, push_dialog_type?)`

- **Returns:** `int` — the index of the pressed button
- **Args:**
  - `message: str` — the message string to display
  - `buttons: int` (optional, default `MessageButtons.OK_BUTTON`) — which buttons to show
  - `enable_markup: bool` (optional, default `False`) — whether to enable markup rendering
  - `show_success_icon: bool` (optional, default `False`) — whether to show a success icon
  - `push_dialog_type: int` (optional, default `PushDialogType.MESSAGE_BOX`) — dialog type
    for Push display
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** Displays a modal message box in Live.
- **Async visibility:** `Unknown`
- **Available Since:** `12.0`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Same as `show_message()`, but accepts a raw string instead of a predefined `Text` object.
This allows displaying arbitrary text at runtime. The additional `push_dialog_type`
parameter controls how the dialog is presented on Push hardware. Not documented in the
Max for Live docs — may only be available from control surface scripts.

---

## Application.View

Represents the view aspects of the Live application, providing control over which panels
are visible and focused (Session, Arranger, Browser, Detail, etc.). Reachable via
`live_app view`.

### Properties

| Property                | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                          |
| ----------------------- | ----------- | ----------- | ---------- | --------------- | ---------------------------------------------------------------- |
| `browse_mode`           | `bool`      | —           | `yes`      | `<11`           | Whether Hot-Swap mode is active for any target.                  |
| `canonical_parent`      | `object`    | —           | `no`       | `<11`           | The canonical parent of the application view.                    |
| `focused_document_view` | `str`       | —           | `yes`      | `<11`           | Name of the focused document view (`"Session"` or `"Arranger"`). |

#### `browse_mode`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
`True` if Hot-Swap mode is active for any target (i.e., the user or a script has engaged
browser hot-swap to replace a device, sample, or preset). The listener fires when Hot-Swap
mode is toggled on or off.

**Probe Results:** Returns `False` when no hotswap is active (the common default state). Becomes `True`
after `toggle_browse()` activates hotswap on the appointed device, or after setting `Browser.hotswap_target`
to a Device handle. Stays `True` after `load_item()` swaps a preset in-place — must deactivate via
`toggle_browse()` or by setting `Browser.hotswap_target = None`. Probed programmatically (12.3.5, MS33).

#### `canonical_parent`

- **Get Returns:** `object`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Returns the canonical parent of the application view, which is the `Application` object.

#### `focused_document_view`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns the name of the document view shown in the currently focused window — either
`"Session"` or `"Arranger"`. The listener fires when the user switches between Session
and Arrangement view in the focused window.

### Methods

| Signature                                             | Returns        | Available Since | Summary                                       |
| ----------------------------------------------------- | -------------- | --------------- | --------------------------------------------- |
| `available_main_views()`                              | `StringVector` | `<11`           | List of valid view identifier strings.        |
| `focus_view(view_name)`                               | `None`         | `<11`           | Show and focus the named view.                |
| `hide_view(view_name)`                                | `None`         | `<11`           | Hide the named view.                          |
| `is_view_visible(identifier, main_window_only?)`      | `bool`         | `<11`           | Whether the named view is currently visible.  |
| `scroll_view(direction, view_name, modifier_pressed)` | `None`         | `<11`           | Scroll the named view in the given direction. |
| `show_view(view_name)`                                | `None`         | `<11`           | Show the named view.                          |
| `toggle_browse()`                                     | `None`         | `<11`           | Toggle Hot-Swap mode for the selected device. |
| `zoom_view(direction, view_name, modifier_pressed)`   | `None`         | `<11`           | Zoom the named view in the given direction.   |

#### `available_main_views()`

- **Returns:** `StringVector`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns a constant list of view name strings that can be used as arguments to the other
view methods (`show_view`, `hide_view`, `focus_view`, `is_view_visible`, `scroll_view`,
`zoom_view`). The Max docs list these as:
`Browser`, `Arranger`, `Session`, `Detail`, `Detail/Clip`, `Detail/DeviceChain`.

#### `focus_view(view_name)`

- **Returns:** `None`
- **Args:**
  - `view_name: str` — one of the identifiers from `available_main_views()`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** Shows and focuses the named view panel.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Shows the named view and gives it keyboard focus. The Max docs note that you can pass an
empty string `" "` to refer to whichever of the Arrangement or Session View is currently
visible in the main window.

#### `hide_view(view_name)`

- **Returns:** `None`
- **Args:**
  - `view_name: str` — one of the identifiers from `available_main_views()`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** Hides the named view panel.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Hides the named view. Passing an empty string `" "` refers to whichever of the Arrangement
or Session View is visible in the main window.

#### `is_view_visible(identifier, main_window_only?)`

- **Returns:** `bool`
- **Args:**
  - `identifier: str` — the view name to check
  - `main_window_only: bool` (optional, default `True`) — if `False`, also checks the
    second window
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A`
- **Side Effects:** None
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Returns `True` if the named view is currently visible. By default, only checks the main
window. If `main_window_only` is set to `False`, the second window is also checked. The
stub notes that notifications from the second window are not yet supported. This property
also supports a listener via `add_is_view_visible_listener(view_name, callback)` — note
the listener takes the view name as a first argument, making it a parameterized listener.

#### `scroll_view(direction, view_name, modifier_pressed)`

- **Returns:** `None`
- **Args:**
  - `direction: int` — `0`=up, `1`=down, `2`=left, `3`=right
  - `view_name: str` — one of the identifiers from `available_main_views()`
  - `modifier_pressed: bool` — modifies behavior in certain views
- **Raises/Errors:** Silently returns if the view cannot perform the action.
- **Undo-tracked:** `N/A`
- **Side Effects:** Scrolls the specified view.
- **Async visibility:** Immediate
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Scrolls the named view in the given direction. Not all views support scrolling in all directions. An empty string
`" "` refers to the currently visible Arrangement or Session View.

**Probe results (12.3.5, MS34):**

| View               | Direction  | `modifier=False`                                              | `modifier=True`                                                  |
| ------------------ | ---------- | ------------------------------------------------------------- | ---------------------------------------------------------------- |
| Arranger           | left       | Deselects region, moves insert cursor from start of selection | Shrinks selected region, left end fixed (shift+left equivalent)  |
| Arranger           | right      | Deselects region, moves insert cursor from start of selection | Expands selected region, left end fixed (shift+right equivalent) |
| Arranger           | up         | Moves selected region up by one track height (up arrow)       | No difference                                                    |
| Arranger           | down       | Moves selected region down by one track height (down arrow)   | No difference                                                    |
| Session            | left/right | Track selection moves in direction                            | No difference                                                    |
| Session            | up/down    | Scene selection moves in direction                            | No difference                                                    |
| Detail/DeviceChain | left/right | Device selection moves in direction                           | No difference                                                    |
| Detail/DeviceChain | up/down    | No effect                                                     | No effect                                                        |
| Browser            | up/down    | Browser selection moves in direction                          | No difference                                                    |
| Browser            | left       | Browser selection moves to library panel                      | No difference                                                    |
| Browser            | right      | Browser selection moves to root folder, then expands groups   | No difference                                                    |

**Probe conclusions:**

- `modifier_pressed` only affects **Arranger** scroll. All other views ignore it.
- Arranger left/right: modifier changes from "move cursor" to "resize selection region" (shift+arrow equivalent).
  Up/down are unaffected by modifier.
- Session scroll moves track/scene selection (equivalent to arrow keys).
- Detail/DeviceChain only responds to left/right (moves device selection). When selection reaches the end, a blue
  insert-position indicator appears after the last device (relates to `track.devices.insert_mode`).
- Browser scroll works all 4 directions. Left/right navigate between library panel and content tree.
- Detail/Clip scroll has no effect in any direction.

#### `show_view(view_name)`

- **Returns:** `None`
- **Args:**
  - `view_name: str` — one of the identifiers from `available_main_views()`
- **Raises/Errors:** Raises a runtime error if called during Live's initialization scope.
- **Undo-tracked:** `N/A`
- **Side Effects:** Shows the named view panel.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed`

**Description:**
Shows the named view. The stub warns that calling this during Live's initialization phase
will throw a runtime error — use it only after initialization is complete.

#### `toggle_browse()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** None observed
- **Undo-tracked:** `N/A`
- **Side Effects:** Opens/closes Hot-Swap mode for the selected device.
- **Async visibility:** Immediate
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Reveals the device chain and the browser, and activates Hot-Swap mode for the currently
selected device. Calling this again deactivates Hot-Swap mode. Equivalent to clicking the
Hot-Swap button on a device.

**Probe Results (12.3.5, MS33):** Works programmatically — no manual UI interaction required. Full flow:
`Song.View.select_device(device)` → `toggle_browse()` → `browse_mode` becomes `True`. During active hotswap,
`Browser.load_item()` swaps presets in-place on the target device (same OID, parameters change) instead of
appending a new device. Hotswap stays active after `load_item()` — must call `toggle_browse()` again to exit.
Cross-device swap within the same browser root (e.g., Compressor → EQ Eight) also works: replaces the device
entirely (new OID, device count unchanged). Cross-root swap (e.g., audio effect → instrument) fails because
the browser filters items by the hotswap target's category.

**Selected vs appointed (probed 12.3.5, MS33):** `toggle_browse()` targets the **selected** device (white
outline), not the **appointed** device (blue hand). When `select_device(dev, ShouldAppointDevice=False)` is
used, the selected and appointed devices can differ — `toggle_browse()` follows the selection. Once hotswap
is active, changing the selection does not redirect `hotswap_target`.

**Note:** Setting `Browser.hotswap_target` directly is a simpler alternative to `select_device()` +
`toggle_browse()`. See `Browser.hotswap_target` docs for details.

#### `zoom_view(direction, view_name, modifier_pressed)`

- **Returns:** `None`
- **Args:**
  - `direction: int` — `0`=up, `1`=down, `2`=left, `3`=right
  - `view_name: str` — one of the identifiers from `available_main_views()`
  - `modifier_pressed: bool` — modifies behavior in certain views
- **Raises/Errors:** Silently returns if the view cannot perform the action.
- **Undo-tracked:** `N/A`
- **Side Effects:** Zooms the specified view.
- **Async visibility:** Immediate
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
Zooms the named view in the given direction. An empty string `" "` refers to the currently visible Arrangement or
Session View.

**Probe results (12.3.5, MS34):**

| View     | Direction  | `modifier=False`              | `modifier=True`           |
| -------- | ---------- | ----------------------------- | ------------------------- |
| Arranger | left       | Zooms timeline out            | No difference             |
| Arranger | right      | Zooms timeline in             | No difference             |
| Arranger | up         | Shrinks selected track height | Shrinks all track heights |
| Arranger | down       | Expands selected track height | Expands all track heights |
| Session  | left/right | Track selection moves         | No difference             |
| Session  | up/down    | Scene selection moves         | No difference             |

**Probe conclusions:**

- Only the **Arranger** actually zooms. Session zoom is identical to Session scroll (both just move selection).
- `modifier_pressed` only affects Arranger up/down zoom: without modifier, changes the selected track's height;
  with modifier, changes all track heights simultaneously. Left/right (timeline zoom) are unaffected by modifier.
- The prior Max docs description was inaccurate — modifier does **not** affect left/right zoom, only up/down.
- Views not listed (Browser, Detail/DeviceChain, Detail/Clip) have no zoom behavior at all.

### Listeners

| Listener                | Sources | Summary                                                                  |
| ----------------------- | ------- | ------------------------------------------------------------------------ | -------------------------------------------------------------- |
| `browse_mode`           | `stub   | max`                                                                     | Fires when Hot-Swap mode is toggled.                           |
| `focused_document_view` | `stub   | max`                                                                     | Fires when the focused view switches between Session/Arranger. |
| `is_view_visible`       | `stub`  | Parameterized listener; fires when a specific view's visibility changes. |
| `view_focus_changed`    | `stub`  | Fires when the focused view component changes.                           |

#### `view_focus_changed`

- **Listenable:** `yes`
- **Sources:** `stub`
- **Probe Status:** `unprobed`

**Description:**
Fires when the focused view component within the application changes. This is a standalone
listener (not tied to a readable property) — there is no corresponding `view_focus_changed`
property, only `add_view_focus_changed_listener` / `remove_view_focus_changed_listener`.
