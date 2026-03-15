---
toc_depth: 2
---

# Licensing (Module)

## ProgressDialog (Class)

> `Live.Licensing.ProgressDialog`

A modal dialog showing a message and a progress animation.

### Methods

| Method                                               | Returns |
| ---------------------------------------------------- | ------- |
| [`end_modal_loop()`](#end_modal_loop)                | `None`  |
| [`run_in_modal_loop()`](#run_in_modal_loop)          | `None`  |
| [`set_status_message()`](#set_status_messagemsg-str) | `None`  |

#### `end_modal_loop()`

- **Returns:** `None`

#### `run_in_modal_loop()`

- **Returns:** `None`

#### `set_status_message(msg: str)`

- **Returns:** `None`
- **Args:**
  - `msg: str`

## PythonLicensingBridge (Class)

> `Live.Licensing.PythonLicensingBridge`

Interface to the internal licensing services.

### Properties

| Property                                                                          | Type   | Supports |
| --------------------------------------------------------------------------------- | ------ | -------- |
| [`base_product_id`](#base_product_id)                                             | `int`  | `get`    |
| [`in_sassafras_mode`](#in_sassafras_mode)                                         | `bool` | `get`    |
| [`license_must_match_variant`](#license_must_match_variant)                       | `bool` | `get`    |
| [`random_number_for_trial_authorization`](#random_number_for_trial_authorization) | `int`  | `get`    |
| [`set_has_unsaved_changes`](#set_has_unsaved_changes)                             | `bool` | `get`    |

#### `base_product_id`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Returns Live's current base product ID.

#### `in_sassafras_mode`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

#### `license_must_match_variant`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns a bool indicating if we require the license information returned by the server to match the variant of Live.

#### `random_number_for_trial_authorization`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Returns the integer to send along with the Trial authorization request. This same integer will be checked for in `process_trial_response` (and then changed).

#### `set_has_unsaved_changes`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the set has unsaved changes.

### Methods

| Method                                                                                                     | Returns          |
| ---------------------------------------------------------------------------------------------------------- | ---------------- |
| [`authorize_with_sassafras()`](#authorize_with_sassafras)                                                  | `None`           |
| [`create_new_live_set()`](#create_new_live_set)                                                            | `None`           |
| [`deauthenticate_user()`](#deauthenticate_user)                                                            | `None`           |
| [`get_progress_dialog()`](#get_progress_dialog)                                                            | `ProgressDialog` |
| [`get_session_id()`](#get_session_id)                                                                      | `str`            |
| [`get_startup_dialog()`](#get_startup_dialogauthorize_callable-callable-authorize_later_callable-callable) | `StartupDialog`  |
| [`get_trial_time_left()`](#get_trial_time_left)                                                            | `str`            |
| [`invoke_pack_installation_callback()`](#invoke_pack_installation_callback)                                | `None`           |
| [`load_and_convert_legacy_unlock_cfg()`](#load_and_convert_legacy_unlock_cfg)                              | `dict`           |
| [`process_license_response()`](#process_license_responselicense_response_lines-list)                       | `UnlockStatus`   |
| [`process_trial_response()`](#process_trial_responsetrial_response_line-str)                               | `bool`           |
| [`request_exit()`](#request_exitexit_code-int-0)                                                           | `None`           |
| [`save_current_set()`](#save_current_set)                                                                  | `None`           |
| [`set_network_timer()`](#set_network_timercallback-callable-interval_in_ms-int)                            | `None`           |
| [`store_session_id()`](#store_session_idsession_id-str)                                                    | `None`           |

#### `authorize_with_sassafras()`

- **Returns:** `None`

#### `create_new_live_set()`

- **Returns:** `None`

Creates a new live set and discards unsaved changes.

#### `deauthenticate_user()`

- **Returns:** `None`

Deletes the current session ID.

#### `get_progress_dialog()`

- **Returns:** `ProgressDialog`

Retrieves an instance of ProgressDialog.

#### `get_session_id()`

- **Returns:** `str`

Retrieve stored session ID.

#### `get_startup_dialog(authorize_callable: Callable, authorize_later_callable: Callable)`

- **Returns:** `StartupDialog`
- **Args:**
  - `authorize_callable: Callable`
  - `authorize_later_callable: Callable`

Retrieves an instance of the startup dialog with the passed callables connected to its buttons.

#### `get_trial_time_left()`

- **Returns:** `str`

Returns remaining time on a trial as a formatted string.

#### `invoke_pack_installation_callback()`

- **Returns:** `None`

Call package installation callback.

#### `load_and_convert_legacy_unlock_cfg()`

- **Returns:** `dict`

Loads the Unlock.cfg file and returns either an empty dict or one that can be converted to an UnlockData object.

#### `process_license_response(license_response_lines: list)`

- **Returns:** `UnlockStatus`
- **Args:**
  - `license_response_lines: list`

Processes a list of strings, each representing a server response to a product authorization.

#### `process_trial_response(trial_response_line: str)`

- **Returns:** `bool`
- **Args:**
  - `trial_response_line: str`

Process the server's response to a Trial authorization.

#### `request_exit(exit_code: int = 0)`

- **Returns:** `None`
- **Args:**
  - `exit_code: int = 0`

#### `save_current_set()`

- **Returns:** `None`

Saves the current Live session.

#### `set_network_timer(callback: Callable, interval_in_ms: int)`

- **Returns:** `None`
- **Args:**
  - `callback: Callable`
  - `interval_in_ms: int`

Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer. If any callback invocation raises an exception, the timer is stopped.

#### `store_session_id(session_id: str)`

- **Returns:** `None`
- **Args:**
  - `session_id: str`

Securely stores the user's session ID (aka cookie, aka credentials).

## StartupDialog (Class)

> `Live.Licensing.StartupDialog`

Serves as an entry point for the user to authorize Live on first launch.

### Methods

| Method                                                                                                | Returns |
| ----------------------------------------------------------------------------------------------------- | ------- |
| [`end_modal_loop()`](#end_modal_loop)                                                                 | `None`  |
| [`run_in_modal_loop()`](#run_in_modal_loopshow_only_offline_auth_instructions-bool)                   | `None`  |
| [`set_notification_message()`](#set_notification_messagenotification_text-str-show_progress_bar-bool) | `None`  |

#### `end_modal_loop()`

- **Returns:** `None`

#### `run_in_modal_loop(show_only_offline_auth_instructions: bool)`

- **Returns:** `None`
- **Args:**
  - `show_only_offline_auth_instructions: bool`

#### `set_notification_message(notification_text: str, show_progress_bar: bool)`

- **Returns:** `None`
- **Args:**
  - `notification_text: str`
  - `show_progress_bar: bool`

## UnlockStatus (Class)

> `Live.Licensing.UnlockStatus`

Returns relevant information after unlock

**Constructor:** `UnlockStatus()`

### Properties

| Property                                                  | Type   | Supports |
| --------------------------------------------------------- | ------ | -------- |
| [`authorization_deactivated`](#authorization_deactivated) | `bool` | `get`    |
| [`authorization_expired`](#authorization_expired)         | `bool` | `get`    |
| [`has_max_unlock_products`](#has_max_unlock_products)     | `bool` | `get`    |
| [`temp_demo_mode`](#temp_demo_mode)                       | `bool` | `get`    |
| [`time_limited`](#time_limited)                           | `bool` | `get`    |
| [`unlock_error`](#unlock_error)                           | `bool` | `get`    |
| [`unlocked`](#unlocked)                                   | `bool` | `get`    |

#### `authorization_deactivated`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

#### `authorization_expired`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

#### `has_max_unlock_products`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

#### `temp_demo_mode`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

#### `time_limited`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

#### `unlock_error`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

#### `unlocked`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

## Enums

### TrialContext

> `Live.Licensing.TrialContext`

| Value | Name           |
| ----- | -------------- |
| `0`   | `SAVE`         |
| `2`   | `FORCE_UPDATE` |
| `3`   | `STARTUP`      |

## Module Functions

| Function                                                                                    | Returns |
| ------------------------------------------------------------------------------------------- | ------- |
| [`authorization_clock_days_ahead()`](#authorization_clock_days_ahead)                       | `int`   |
| [`get_authorization_page_url()`](#get_authorization_page_urlreauthorize-bool-is_trial-bool) | `str`   |
| [`get_purchase_live_url()`](#get_purchase_live_url)                                         | `str`   |
| [`get_services_url()`](#get_services_url)                                                   | `str`   |
| [`get_unlock_dir()`](#get_unlock_dir)                                                       | `tuple` |
| [`launch_web_browser()`](#launch_web_browserurl-str)                                        | `None`  |

### `authorization_clock_days_ahead()`

- **Returns:** `int`

Advances the current date by the number of days specified by \_AuthClockDaysAhead

### `get_authorization_page_url(reauthorize: bool, is_trial: bool)`

- **Returns:** `str`
- **Args:**
  - `reauthorize: bool`
  - `is_trial: bool`

Retrieves the appopriate URL on ableton.com where the unser can initiate the authorization.

### `get_purchase_live_url()`

- **Returns:** `str`

Returns the environment-aware purchase URL for purchasing Live licenses

### `get_services_url()`

- **Returns:** `str`

Returns the URL against which service calls (e.g. for authorization) can be performed.

### `get_unlock_dir()`

- **Returns:** `tuple`

Returns a tuple containing the unlock file directory and a flag indicating if the unlock file is in the system domain.

### `launch_web_browser(url: str)`

- **Returns:** `None`
- **Args:**
  - `url: str`

Opens a web browser at the specified URL on the user's computer.
