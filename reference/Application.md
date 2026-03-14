# Application

> `Live.Application.Application`

This class represents the Live application.

## View

> `Live.Application.Application.View`

This class represents the view aspects of the Live application.

### Properties

| Property                | Type          | Settable | Listenable | Description                                                                      |
| ----------------------- | ------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `browse_mode`           | `bool`        | `no`     | `yes`      | Return true if HotSwap mode is active for any target.                            |
| `canonical_parent`      | `Application` | `no`     | `no`       | Get the canonical parent of the application view.                                |
| `focused_document_view` | `str`         | `no`     | `yes`      | Return the name of the document view ('Session' or 'Arranger') shown in the c... |

#### `browse_mode`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Return true if HotSwap mode is active for any target.

#### `canonical_parent`

- **Type:** `Application`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the application view.

#### `focused_document_view`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `yes`

Return the name of the document view ('Session' or 'Arranger') shown in the currently selected window.

### Methods

| Method                                                                | Returns        | Description                                                                      |
| --------------------------------------------------------------------- | -------------- | -------------------------------------------------------------------------------- |
| `available_main_views()`                                              | `StringVector` | Return a list of strings with the available subcomponent views, which is to b... |
| `focus_view(view: str)`                                               | `None`         | Show and focus one through the identifier string specified view.                 |
| `hide_view(view_name: str)`                                           | `None`         | Hide one through the identifier string specified view.                           |
| `is_view_visible(identifier: str, main_window_only: bool = True)`     | `bool`         | Return true if the through the identifier string specified view is currently ... |
| `scroll_view(direction: int, view_name: str, modifier_pressed: bool)` | `None`         | Scroll through the identifier string specified view into the given direction,... |
| `show_view(view: str)`                                                | `None`         | Show one through the identifier string specified view.                           |
| `toggle_browse()`                                                     | `None`         | Reveals the device chain, the browser and starts hot swap for the selected de... |
| `zoom_view(direction: int, view_name: str, modifier_pressed: bool)`   | `None`         | Zoom through the identifier string specified view into the given direction, i... |

#### `available_main_views()`

- **Returns:** `StringVector`

Return a list of strings with the available subcomponent views, which is to be specified, when using the rest of this classes functions. A 'subcomponent view' is a main view component of a document view, like the Session view, the Arranger or Detailview and so on...

#### `focus_view(view: str)`

- **Returns:** `None`
- **Args:**
  - `view: str`

Show and focus one through the identifier string specified view.

#### `hide_view(view_name: str)`

- **Returns:** `None`
- **Args:**
  - `view_name: str`

Hide one through the identifier string specified view.

#### `is_view_visible(identifier: str, main_window_only: bool = True)`

- **Returns:** `bool`
- **Args:**
  - `identifier: str`
  - `main_window_only: bool = True`

Return true if the through the identifier string specified view is currently visible. If main_window_only is set to False, this will also check in second window. Notifications from the second window are not yet supported.

#### `scroll_view(direction: int, view_name: str, modifier_pressed: bool)`

- **Returns:** `None`
- **Args:**
  - `direction: int`
  - `view_name: str`
  - `modifier_pressed: bool`

Scroll through the identifier string specified view into the given direction, if possible. Will silently return if the specified view can not perform the requested action.

#### `show_view(view: str)`

- **Returns:** `None`
- **Args:**
  - `view: str`

Show one through the identifier string specified view. Will throw a runtime error if this is called in Live's initialization scope.

#### `toggle_browse()`

- **Returns:** `None`

Reveals the device chain, the browser and starts hot swap for the selected device. Calling this function again stops hot swap.

#### `zoom_view(direction: int, view_name: str, modifier_pressed: bool)`

- **Returns:** `None`
- **Args:**
  - `direction: int`
  - `view_name: str`
  - `modifier_pressed: bool`

Zoom through the identifier string specified view into the given direction, if possible. Will silently return if the specified view can not perform the requested action.

### Enums

#### `NavDirection`

| Value | Name    |
| ----- | ------- |
| `0`   | `up`    |
| `1`   | `down`  |
| `2`   | `left`  |
| `3`   | `right` |

## Properties

| Property                      | Type                                  | Settable | Listenable | Description                                                                      |
| ----------------------------- | ------------------------------------- | -------- | ---------- | -------------------------------------------------------------------------------- |
| `average_process_usage`       | `float`                               | `no`     | `yes`      | Reports Live's average CPU load.                                                 |
| `browser`                     | `Browser`                             | `no`     | `no`       | Returns an interface to the browser.                                             |
| `canonical_parent`            | `None`                                | `no`     | `no`       | Returns the canonical parent of the application.                                 |
| `control_surfaces`            | `tuple[object, Ellipsis]`             | `no`     | `yes`      | Const access to a list of the control surfaces selected in preferences, in th... |
| `current_dialog_button_count` | `int`                                 | `no`     | `no`       | Number of buttons on the current dialog.                                         |
| `current_dialog_message`      | `str`                                 | `no`     | `no`       | Text of the last dialog that appeared; Empty if all dialogs just disappeared.    |
| `number_of_push_apps_running` | `int`                                 | `no`     | `no`       | Returns the number of connected Push apps.                                       |
| `open_dialog_count`           | `int`                                 | `no`     | `yes`      | The number of open dialogs in Live.                                              |
| `peak_process_usage`          | `float`                               | `no`     | `yes`      | Reports Live's peak CPU load.                                                    |
| `unavailable_features`        | `tuple[UnavailableFeature, Ellipsis]` | `no`     | `yes`      | List of features that are unavailable due to limitations of the current Live ... |
| `view`                        | `View`                                | `no`     | `no`       | Returns the applications view component.                                         |

### `average_process_usage`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Reports Live's average CPU load.

### `browser`

- **Type:** `Browser`
- **Settable:** `no`
- **Listenable:** `no`

Returns an interface to the browser.

### `canonical_parent`

- **Type:** `None`
- **Settable:** `no`
- **Listenable:** `no`

Returns the canonical parent of the application.

### `control_surfaces`

- **Type:** `tuple[object, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of the control surfaces selected in preferences, in the same order. The list contains None if no control surface is active at that index.

### `current_dialog_button_count`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Number of buttons on the current dialog.

### `current_dialog_message`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Text of the last dialog that appeared; Empty if all dialogs just disappeared.

### `number_of_push_apps_running`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Returns the number of connected Push apps.

### `open_dialog_count`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

The number of open dialogs in Live. 0 if not dialog is open.

### `peak_process_usage`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Reports Live's peak CPU load.

### `unavailable_features`

- **Type:** `tuple[UnavailableFeature, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `yes`

List of features that are unavailable due to limitations of the current Live edition.

### `view`

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Returns the applications view component.

## Methods

| Method                                                         | Returns                                                                                                 | Description                                                             |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| `get_bugfix_version()`                                         | `int`                                                                                                   | Returns an integer representing the bugfix version of Live.             |
| `get_build_id()`                                               | `str`                                                                                                   | Returns a string identifying the build.                                 |
| `get_document()`                                               | `Song`                                                                                                  | Returns the current Live Set.                                           |
| `get_major_version()`                                          | `int`                                                                                                   | Returns an integer representing the major version of Live.              |
| `get_minor_version()`                                          | `int`                                                                                                   | Returns an integer representing the minor version of Live.              |
| `get_variant()`                                                | `str`                                                                                                   | Returns one of the strings in Live.Application.Variants.                |
| `get_version_string()`                                         | `str`                                                                                                   | Returns the full version string of Live.                                |
| `has_option(section_name: str)`                                | `bool`                                                                                                  | Returns True if the given entry exists in Options.txt, False otherwise. |
| `press_current_dialog_button(index: int)`                      | `None`                                                                                                  | Press a button, by index, on the current message box.                   |
| `show_message(text: Text, buttons: MessageButtons              | int = 0, enable_markup: bool = False, show_success_icon: bool = False)`                                 | `int`                                                                   | Shows a message box, returning the position of the pressed button. |
| `show_on_the_fly_message(message: str, buttons: MessageButtons | int = 0, enable_markup: bool = False, show_success_icon: bool = False, push_dialog_type: PushDialogType | int = 0)`                                                               | `int`                                                              | Same as show_message, but for when there is no predefined Text object. |

### `get_bugfix_version()`

- **Returns:** `int`

Returns an integer representing the bugfix version of Live.

### `get_build_id()`

- **Returns:** `str`

Returns a string identifying the build.

### `get_document()`

- **Returns:** `Song`

Returns the current Live Set.

### `get_major_version()`

- **Returns:** `int`

Returns an integer representing the major version of Live.

### `get_minor_version()`

- **Returns:** `int`

Returns an integer representing the minor version of Live.

### `get_variant()`

- **Returns:** `str`

Returns one of the strings in Live.Application.Variants.

### `get_version_string()`

- **Returns:** `str`

Returns the full version string of Live.

### `has_option(section_name: str)`

- **Returns:** `bool`
- **Args:**
  - `section_name: str`

Returns True if the given entry exists in Options.txt, False otherwise.

### `press_current_dialog_button(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Press a button, by index, on the current message box.

### `show_message(text: Text, buttons: MessageButtons | int = 0, enable_markup: bool = False, show_success_icon: bool = False)`

- **Returns:** `int`
- **Args:**
  - `text: Text`
  - `buttons: MessageButtons | int = 0`
  - `enable_markup: bool = False`
  - `show_success_icon: bool = False`

Shows a message box, returning the position of the pressed button.

### `show_on_the_fly_message(message: str, buttons: MessageButtons | int = 0, enable_markup: bool = False, show_success_icon: bool = False, push_dialog_type: PushDialogType | int = 0)`

- **Returns:** `int`
- **Args:**
  - `message: str`
  - `buttons: MessageButtons | int = 0`
  - `enable_markup: bool = False`
  - `show_success_icon: bool = False`
  - `push_dialog_type: PushDialogType | int = 0`

Same as show_message, but for when there is no predefined Text object.

## Enums

### `MessageButtons`

Specifies the characteristics of the message box, e.g. which buttons to show.

| Value | Name                    |
| ----- | ----------------------- |
| `0`   | `OK_BUTTON`             |
| `1`   | `OK_NEW_SET_BUTTON`     |
| `2`   | `OK_RETRY_BUTTON`       |
| `3`   | `SAVE_DONT_SAVE_BUTTON` |
| `4`   | `OK_ACCOUNT_BUTTON`     |
| `5`   | `OK_PURCHASE_BUTTON`    |

### `PushDialogType`

Specifies the dialog type for Push.

| Value | Name                                 |
| ----- | ------------------------------------ |
| `0`   | `MESSAGE_BOX`                        |
| `5`   | `OUT_OF_UNLOCKS_DIALOG`              |
| `7`   | `RENT_TO_OWN_LICENSE_EXPIRED_DIALOG` |

### `UnavailableFeature`

| Value | Name                                     |
| ----- | ---------------------------------------- |
| `0`   | `note_velocity_ranges_and_probabilities` |

### `Variants`

Holds strings representing what type of Live is running.

| Value      | Name       |
| ---------- | ---------- |
| `Beta`     | `BETA`     |
| `Intro`    | `INTRO`    |
| `Lite`     | `LITE`     |
| `Standard` | `STANDARD` |
| `Suite`    | `SUITE`    |
| `Trial`    | `TRIAL`    |

## ControlDescription

> `Live.Application.ControlDescription`

Describes a control present in a control surface proxy

**Constructor:** `ControlDescription()`

### Properties

| Property | Type  | Settable | Listenable | Description |
| -------- | ----- | -------- | ---------- | ----------- |
| `id`     | `int` | `no`     | `no`       |             |
| `name`   | `str` | `no`     | `no`       |             |

#### `id`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

#### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

## ControlDescriptionVector

> `Live.Application.ControlDescriptionVector`

A container for returning control descriptions.

### Methods

| Method                               | Returns | Description |
| ------------------------------------ | ------- | ----------- |
| `append(value: ControlDescription)`  | `None`  |             |
| `extend(values: ControlDescription)` | `None`  |             |

#### `append(value: ControlDescription)`

- **Returns:** `None`
- **Args:**
  - `value: ControlDescription`

#### `extend(values: ControlDescription)`

- **Returns:** `None`
- **Args:**
  - `values: ControlDescription`

## ControlSurfaceProxy

> `Live.Application.ControlSurfaceProxy`

Represents a control surface running in a different process. For use by M4L

### Properties

| Property               | Type                                  | Settable | Listenable | Description                 |
| ---------------------- | ------------------------------------- | -------- | ---------- | --------------------------- |
| `control_descriptions` | `tuple[ControlDescription, Ellipsis]` | `no`     | `no`       |                             |
| `pad_layout`           | `str`                                 | `no`     | `yes`      | The layout of pads on Push. |
| `type_name`            | `str`                                 | `no`     | `no`       |                             |

#### `control_descriptions`

- **Type:** `tuple[ControlDescription, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

#### `pad_layout`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `yes`

The layout of pads on Push.

#### `type_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

### Methods

| Method                                   | Returns | Description |
| ---------------------------------------- | ------- | ----------- |
| `enable_receive_midi(enabled: bool)`     | `None`  |             |
| `fetch_received_midi_messages()`         | `tuple` |             |
| `fetch_received_values()`                | `tuple` |             |
| `grab_control(control: int)`             | `None`  |             |
| `release_control(control: int)`          | `None`  |             |
| `send_midi(midi_event_bytes: tuple)`     | `None`  |             |
| `send_value(value: tuple)`               | `None`  |             |
| `subscribe_to_control(control: int)`     | `None`  |             |
| `unsubscribe_from_control(control: int)` | `None`  |             |

#### `enable_receive_midi(enabled: bool)`

- **Returns:** `None`
- **Args:**
  - `enabled: bool`

#### `fetch_received_midi_messages()`

- **Returns:** `tuple`

#### `fetch_received_values()`

- **Returns:** `tuple`

#### `grab_control(control: int)`

- **Returns:** `None`
- **Args:**
  - `control: int`

#### `release_control(control: int)`

- **Returns:** `None`
- **Args:**
  - `control: int`

#### `send_midi(midi_event_bytes: tuple)`

- **Returns:** `None`
- **Args:**
  - `midi_event_bytes: tuple`

#### `send_value(value: tuple)`

- **Returns:** `None`
- **Args:**
  - `value: tuple`

#### `subscribe_to_control(control: int)`

- **Returns:** `None`
- **Args:**
  - `control: int`

#### `unsubscribe_from_control(control: int)`

- **Returns:** `None`
- **Args:**
  - `control: int`

## UnavailableFeatureVector

> `Live.Application.UnavailableFeatureVector`

A container for returning unavailable features.

### Methods

| Method                               | Returns | Description |
| ------------------------------------ | ------- | ----------- |
| `append(value: UnavailableFeature)`  | `None`  |             |
| `extend(values: UnavailableFeature)` | `None`  |             |

#### `append(value: UnavailableFeature)`

- **Returns:** `None`
- **Args:**
  - `value: UnavailableFeature`

#### `extend(values: UnavailableFeature)`

- **Returns:** `None`
- **Args:**
  - `values: UnavailableFeature`

## Module Functions

| Function                                                            | Returns       | Description                                                 |
| ------------------------------------------------------------------- | ------------- | ----------------------------------------------------------- |
| `combine_apcs()`                                                    | `bool`        | Returns true if multiple APCs should be combined.           |
| `encrypt_challenge(dongle1: int, dongle2: int, key_index: int = 0)` | `tuple`       | Returns an encrypted challenge based on the TEA algortithm. |
| `encrypt_challenge2(challenge: int)`                                | `int`         | Returns the UMAC hash for the given challenge.              |
| `get_application()`                                                 | `Application` | Returns the application instance.                           |
| `get_random_int(min_value: int, max_value: int)`                    | `int`         | Returns a random integer from the given range.              |

### `combine_apcs()`

- **Returns:** `bool`

Returns true if multiple APCs should be combined.

### `encrypt_challenge(dongle1: int, dongle2: int, key_index: int = 0)`

- **Returns:** `tuple`
- **Args:**
  - `dongle1: int`
  - `dongle2: int`
  - `key_index: int = 0`

Returns an encrypted challenge based on the TEA algortithm

### `encrypt_challenge2(challenge: int)`

- **Returns:** `int`
- **Args:**
  - `challenge: int`

Returns the UMAC hash for the given challenge.

### `get_application()`

- **Returns:** `Application`

Returns the application instance.

### `get_random_int(min_value: int, max_value: int)`

- **Returns:** `int`
- **Args:**
  - `min_value: int`
  - `max_value: int`

Returns a random integer from the given range.
