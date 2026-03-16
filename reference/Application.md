# Application (Module)

## Application (Class)

> `Live.Application.Application`

This class represents the Live application.

**Access via:**

- `Application.get_application`

### Properties

| Property                                                      | Type                       | Supports       |
| ------------------------------------------------------------- | -------------------------- | -------------- |
| [`average_process_usage`](#average_process_usage)             | `float`                    | `get`/`listen` |
| [`browser`](#browser)                                         | `Browser`                  | `get`          |
| [`canonical_parent`](#canonical_parent)                       | `None`                     | `get`          |
| [`control_surfaces`](#control_surfaces)                       | `Vector[object]`           | `get`/`listen` |
| [`current_dialog_button_count`](#current_dialog_button_count) | `int`                      | `get`          |
| [`current_dialog_message`](#current_dialog_message)           | `str`                      | `get`          |
| [`number_of_push_apps_running`](#number_of_push_apps_running) | `int`                      | `get`          |
| [`open_dialog_count`](#open_dialog_count)                     | `int`                      | `get`/`listen` |
| [`peak_process_usage`](#peak_process_usage)                   | `float`                    | `get`/`listen` |
| [`unavailable_features`](#unavailable_features)               | `UnavailableFeatureVector` | `get`/`listen` |
| [`view`](#view)                                               | `View`                     | `get`          |

#### `average_process_usage`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Reports Live's average CPU load.

#### `browser`

- **Type:** `Browser`
- **Settable:** `no`
- **Listenable:** `no`

Returns an interface to the browser.

#### `canonical_parent`

- **Type:** `None`
- **Settable:** `no`
- **Listenable:** `no`

Returns the canonical parent of the application.

#### `control_surfaces`

- **Type:** `Vector[object]`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to a list of the control surfaces selected in preferences, in the same order. The list contains None if no control surface is active at that index.

#### `current_dialog_button_count`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Number of buttons on the current dialog.

#### `current_dialog_message`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Text of the last dialog that appeared; Empty if all dialogs just disappeared.

#### `number_of_push_apps_running`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Returns the number of connected Push apps.

#### `open_dialog_count`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

The number of open dialogs in Live. 0 if not dialog is open.

#### `peak_process_usage`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `yes`

Reports Live's peak CPU load.

#### `unavailable_features`

- **Type:** `UnavailableFeatureVector`
- **Settable:** `no`
- **Listenable:** `yes`

List of features that are unavailable due to limitations of the current Live edition.

#### `view`

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Returns the applications view component.

### Methods

| Method                                                                                                                                                                                      | Returns |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| [`get_bugfix_version()`](#get_bugfix_version)                                                                                                                                               | `int`   |
| [`get_build_id()`](#get_build_id)                                                                                                                                                           | `str`   |
| [`get_document()`](#get_document)                                                                                                                                                           | `Song`  |
| [`get_major_version()`](#get_major_version)                                                                                                                                                 | `int`   |
| [`get_minor_version()`](#get_minor_version)                                                                                                                                                 | `int`   |
| [`get_variant()`](#get_variant)                                                                                                                                                             | `str`   |
| [`get_version_string()`](#get_version_string)                                                                                                                                               | `str`   |
| [`has_option()`](#has_optionoption-str)                                                                                                                                                     | `bool`  |
| [`press_current_dialog_button()`](#press_current_dialog_buttonindex-int)                                                                                                                    | `None`  |
| [`show_message()`](#show_messagetext-text-buttons-messagebuttons-int-0-enable_markup-bool-false-show_success_icon-bool-false)                                                               | `int`   |
| [`show_on_the_fly_message()`](#show_on_the_fly_messagemessage-str-buttons-messagebuttons-int-0-enable_markup-bool-false-show_success_icon-bool-false-push_dialog_type-pushdialogtype-int-0) | `int`   |

#### `get_bugfix_version()`

- **Returns:** `int`

Returns an integer representing the bugfix version of Live.

#### `get_build_id()`

- **Returns:** `str`

Returns a string identifying the build.

#### `get_document()`

- **Returns:** `Song`

Returns the current Live Set.

#### `get_major_version()`

- **Returns:** `int`

Returns an integer representing the major version of Live.

#### `get_minor_version()`

- **Returns:** `int`

Returns an integer representing the minor version of Live.

#### `get_variant()`

- **Returns:** `str`

Returns one of the strings in Live.Application.Variants.

#### `get_version_string()`

- **Returns:** `str`

Returns the full version string of Live.

#### `has_option(option: str)`

- **Returns:** `bool`
- **Args:**
  - `option: str`

Returns True if the given entry exists in Options.txt, False otherwise.

#### `press_current_dialog_button(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Press a button, by index, on the current message box.

#### `show_message(text: Text, buttons: MessageButtons | int = 0, enable_markup: bool = False, show_success_icon: bool = False)`

- **Returns:** `int`
- **Args:**
  - `text: Text`
  - `buttons: MessageButtons | int = 0`
  - `enable_markup: bool = False`
  - `show_success_icon: bool = False`

Shows a message box, returning the position of the pressed button.

#### `show_on_the_fly_message(message: str, buttons: MessageButtons | int = 0, enable_markup: bool = False, show_success_icon: bool = False, push_dialog_type: PushDialogType | int = 0)`

- **Returns:** `int`
- **Args:**
  - `message: str`
  - `buttons: MessageButtons | int = 0`
  - `enable_markup: bool = False`
  - `show_success_icon: bool = False`
  - `push_dialog_type: PushDialogType | int = 0`

Same as show_message, but for when there is no predefined Text object.

## Application.View (Subclass)

> `Live.Application.Application.View`

This class represents the view aspects of the Live application.

**Live Object:** `yes`

### Properties

| Property                                          | Type          | Supports       |
| ------------------------------------------------- | ------------- | -------------- |
| [`browse_mode`](#browse_mode)                     | `bool`        | `get`/`listen` |
| [`canonical_parent`](#canonical_parent)           | `Application` | `get`          |
| [`focused_document_view`](#focused_document_view) | `str`         | `get`/`listen` |

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

| Method                                                                           | Returns        |
| -------------------------------------------------------------------------------- | -------------- |
| [`available_main_views()`](#available_main_views)                                | `StringVector` |
| [`focus_view()`](#focus_viewarg2-str)                                            | `None`         |
| [`hide_view()`](#hide_viewview_name-str)                                         | `None`         |
| [`is_view_visible()`](#is_view_visibleidentifier-str-main_window_only-bool-true) | `bool`         |
| [`scroll_view()`](#scroll_viewdirection-int-view_name-str-modifier_pressed-bool) | `None`         |
| [`show_view()`](#show_viewarg2-str)                                              | `None`         |
| [`toggle_browse()`](#toggle_browse)                                              | `None`         |
| [`zoom_view()`](#zoom_viewdirection-int-view_name-str-modifier_pressed-bool)     | `None`         |

#### `available_main_views()`

- **Returns:** `StringVector`

Return a list of strings with the available subcomponent views, which is to be specified, when using the rest of this classes functions. A 'subcomponent view' is a main view component of a document view, like the Session view, the Arranger or Detailview and so on...

#### `focus_view(arg2: str)`

- **Returns:** `None`
- **Args:**
  - `arg2: str`

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

#### `show_view(arg2: str)`

- **Returns:** `None`
- **Args:**
  - `arg2: str`

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

## Enums

### NavDirection

> `Live.Application.Application.View.NavDirection`

| Value | Name    |
| ----- | ------- |
| `0`   | `up`    |
| `1`   | `down`  |
| `2`   | `left`  |
| `3`   | `right` |

### MessageButtons

> `Live.Application.MessageButtons`

Specifies the characteristics of the message box, e.g. which buttons to show.

| Value | Name                    |
| ----- | ----------------------- |
| `0`   | `OK_BUTTON`             |
| `1`   | `OK_NEW_SET_BUTTON`     |
| `2`   | `OK_RETRY_BUTTON`       |
| `3`   | `SAVE_DONT_SAVE_BUTTON` |
| `4`   | `OK_ACCOUNT_BUTTON`     |
| `5`   | `OK_PURCHASE_BUTTON`    |

### PushDialogType

> `Live.Application.PushDialogType`

Specifies the dialog type for Push.

| Value | Name                                 |
| ----- | ------------------------------------ |
| `0`   | `MESSAGE_BOX`                        |
| `5`   | `OUT_OF_UNLOCKS_DIALOG`              |
| `7`   | `RENT_TO_OWN_LICENSE_EXPIRED_DIALOG` |

### UnavailableFeature

> `Live.Application.UnavailableFeature`

| Value | Name                                     |
| ----- | ---------------------------------------- |
| `0`   | `note_velocity_ranges_and_probabilities` |

### Variants

> `Live.Application.Variants`

Holds strings representing what type of Live is running.

| Value      | Name       |
| ---------- | ---------- |
| `Beta`     | `BETA`     |
| `Intro`    | `INTRO`    |
| `Lite`     | `LITE`     |
| `Standard` | `STANDARD` |
| `Suite`    | `SUITE`    |
| `Trial`    | `TRIAL`    |

## ControlDescription (Type)

> `Live.Application.ControlDescription`

Describes a control present in a control surface proxy

**Constructor:** `ControlDescription()`

### Properties

| Property        | Type  | Supports |
| --------------- | ----- | -------- |
| [`id`](#id)     | `int` | `get`    |
| [`name`](#name) | `str` | `get`    |

#### `id`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

#### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

## ControlDescriptionVector (Type)

> `Live.Application.ControlDescriptionVector`

A container for returning control descriptions.

### Methods

| Method                                         | Returns |
| ---------------------------------------------- | ------- |
| [`append()`](#appendvalue-controldescription)  | `None`  |
| [`extend()`](#extendvalues-controldescription) | `None`  |

#### `append(value: ControlDescription)`

- **Returns:** `None`
- **Args:**
  - `value: ControlDescription`

#### `extend(values: ControlDescription)`

- **Returns:** `None`
- **Args:**
  - `values: ControlDescription`

## ControlSurfaceProxy (Type)

> `Live.Application.ControlSurfaceProxy`

Represents a control surface running in a different process. For use by M4L

### Properties

| Property                                        | Type                       | Supports       |
| ----------------------------------------------- | -------------------------- | -------------- |
| [`control_descriptions`](#control_descriptions) | `ControlDescriptionVector` | `get`          |
| [`pad_layout`](#pad_layout)                     | `str`                      | `get`/`listen` |
| [`type_name`](#type_name)                       | `str`                      | `get`          |

#### `control_descriptions`

- **Type:** `ControlDescriptionVector`
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

| Method                                                               | Returns                                 |
| -------------------------------------------------------------------- | --------------------------------------- |
| [`enable_receive_midi()`](#enable_receive_midienabled-bool)          | `None`                                  |
| [`fetch_received_midi_messages()`](#fetch_received_midi_messages)    | `tuple[tuple[int, Ellipsis], Ellipsis]` |
| [`fetch_received_values()`](#fetch_received_values)                  | `tuple[tuple[int, Any], Ellipsis]`      |
| [`grab_control()`](#grab_controlcontrol-int)                         | `None`                                  |
| [`release_control()`](#release_controlarg2-int)                      | `None`                                  |
| [`send_midi()`](#send_midiarg2-tuple)                                | `None`                                  |
| [`send_value()`](#send_valuearg2-tuple)                              | `None`                                  |
| [`subscribe_to_control()`](#subscribe_to_controlcontrol-int)         | `None`                                  |
| [`unsubscribe_from_control()`](#unsubscribe_from_controlcontrol-int) | `None`                                  |

#### `enable_receive_midi(enabled: bool)`

- **Returns:** `None`
- **Args:**
  - `enabled: bool`

#### `fetch_received_midi_messages()`

- **Returns:** `tuple[tuple[int, Ellipsis], Ellipsis]`

#### `fetch_received_values()`

- **Returns:** `tuple[tuple[int, Any], Ellipsis]`

#### `grab_control(control: int)`

- **Returns:** `None`
- **Args:**
  - `control: int`

#### `release_control(arg2: int)`

- **Returns:** `None`
- **Args:**
  - `arg2: int`

#### `send_midi(arg2: tuple)`

- **Returns:** `None`
- **Args:**
  - `arg2: tuple`

#### `send_value(arg2: tuple)`

- **Returns:** `None`
- **Args:**
  - `arg2: tuple`

#### `subscribe_to_control(control: int)`

- **Returns:** `None`
- **Args:**
  - `control: int`

#### `unsubscribe_from_control(control: int)`

- **Returns:** `None`
- **Args:**
  - `control: int`

## UnavailableFeatureVector (Type)

> `Live.Application.UnavailableFeatureVector`

A container for returning unavailable features.

### Methods

| Method                                         | Returns |
| ---------------------------------------------- | ------- |
| [`append()`](#appendvalue-unavailablefeature)  | `None`  |
| [`extend()`](#extendvalues-unavailablefeature) | `None`  |

#### `append(value: UnavailableFeature)`

- **Returns:** `None`
- **Args:**
  - `value: UnavailableFeature`

#### `extend(values: UnavailableFeature)`

- **Returns:** `None`
- **Args:**
  - `values: UnavailableFeature`

## Module Functions

| Function                                                                           | Returns                |
| ---------------------------------------------------------------------------------- | ---------------------- |
| [`combine_apcs()`](#combine_apcs)                                                  | `bool`                 |
| [`encrypt_challenge()`](#encrypt_challengedongle1-int-dongle2-int-key_index-int-0) | `tuple[int, Ellipsis]` |
| [`encrypt_challenge2()`](#encrypt_challenge2challenge-int)                         | `int`                  |
| [`get_application()`](#get_application)                                            | `Application`          |
| [`get_random_int()`](#get_random_intmin_value-int-max_value-int)                   | `int`                  |

### `combine_apcs()`

- **Returns:** `bool`

Returns true if multiple APCs should be combined.

### `encrypt_challenge(dongle1: int, dongle2: int, key_index: int = 0)`

- **Returns:** `tuple[int, Ellipsis]`
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
