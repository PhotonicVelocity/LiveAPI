# RackDevice (Module)

## RackDevice (Class)

> `Live.RackDevice.RackDevice`

This class represents a Rack device.

**Live Object:** `yes`

### Properties

| Property                    | Type                               | Supports             |
| --------------------------- | ---------------------------------- | -------------------- |
| `can_compare_ab`            | `bool`                             | `get`                |
| `can_have_chains`           | `bool`                             | `get`                |
| `can_have_drum_pads`        | `bool`                             | `get`                |
| `can_show_chains`           | `bool`                             | `get`                |
| `canonical_parent`          | `Track`                            | `get`                |
| `chain_selector`            | `DeviceParameter`                  | `get`                |
| `chains`                    | `tuple`                            | `get`/`listen`       |
| `class_display_name`        | `str`                              | `get`                |
| `class_name`                | `str`                              | `get`                |
| `drum_pads`                 | `tuple`                            | `get`/`listen`       |
| `has_drum_pads`             | `bool`                             | `get`/`listen`       |
| `has_macro_mappings`        | `bool`                             | `get`/`listen`       |
| `is_active`                 | `bool`                             | `get`                |
| `is_showing_chains`         | `bool`                             | `get`/`set`/`listen` |
| `is_using_compare_preset_b` | `bool`                             | `get`/`set`          |
| `latency_in_ms`             | `float`                            | `get`                |
| `latency_in_samples`        | `int`                              | `get`                |
| `macros_mapped`             | `tuple`                            | `get`/`listen`       |
| `name`                      | `str`                              | `get`/`set`          |
| `parameters`                | `tuple[DeviceParameter, Ellipsis]` | `get`                |
| `return_chains`             | `tuple`                            | `get`/`listen`       |
| `selected_variation_index`  | `int`                              | `get`/`set`          |
| `type`                      | `DeviceType`                       | `get`                |
| `variation_count`           | `int`                              | `get`/`listen`       |
| `view`                      | `View`                             | `get`                |
| `visible_drum_pads`         | `tuple`                            | `get`/`listen`       |
| `visible_macro_count`       | `int`                              | `get`/`listen`       |

#### `can_compare_ab`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the Device has the capability to AB compare.

#### `can_have_chains`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the device is a rack.

#### `can_have_drum_pads`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Returns true if the device is a drum rack.

#### `can_show_chains`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Rack contains a rack instrument device that is capable of showing its chains in session view.

#### `canonical_parent`

- **Type:** `Track`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the Device.

#### `chain_selector`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the chain selector parameter.

#### `chains`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to the list of chains in this device. Throws an exception if can_have_chains is false.

#### `class_display_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to the name of the device's class name as displayed in Live's browser and device chain

#### `class_name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to the name of the device's class.

#### `drum_pads`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to the list of drum pads in this device. Throws an exception if can_have_drum_pads is false.

#### `has_drum_pads`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if the device is a drum rack which has drum pads. Throws an exception if can_have_drum_pads is false.

#### `has_macro_mappings`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Returns true if any of the rack's macros are mapped to a parameter.

#### `is_active`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.

#### `is_showing_chains`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Returns True, if it is showing chains.

#### `is_using_compare_preset_b`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.

#### `latency_in_ms`

- **Type:** `float`
- **Settable:** `no`
- **Listenable:** `no`

Returns the latency of the device in ms.

#### `latency_in_samples`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `no`

Returns the latency of the device in samples.

#### `macros_mapped`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

A list of booleans, one for each macro parameter, which is True iffthat macro is mapped to something

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Return access to the name of the device.

#### `parameters`

- **Type:** `tuple[DeviceParameter, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the list of available automatable parameters for this device.

#### `return_chains`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to the list of return chains in this device. Throws an exception if can_have_chains is false.

#### `selected_variation_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

Access to the index of the currently selected macro variation.Throws an exception if the index is out of range.

#### `type`

- **Type:** `DeviceType`
- **Settable:** `no`
- **Listenable:** `no`

Return the type of the device.

#### `variation_count`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the number of macro variations currently stored.

#### `view`

- **Type:** `View`
- **Settable:** `no`
- **Listenable:** `no`

Representing the view aspects of a device.

#### `visible_drum_pads`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to the list of visible drum pads in this device. Throws an exception if can_have_drum_pads is false.

#### `visible_macro_count`

- **Type:** `int`
- **Settable:** `no`
- **Listenable:** `yes`

Access to the number of macros that are currently visible.

### Methods

| Method                                                | Returns     | Description                                                                      |
| ----------------------------------------------------- | ----------- | -------------------------------------------------------------------------------- |
| `add_macro()`                                         | `None`      | Increases the number of visible macro controls in the rack.                      |
| `copy_pad(source_index: int, destination_index: int)` | `None`      | Copies all contents of a drum pad from a source pad into a destination pad.      |
| `delete_selected_variation()`                         | `None`      | Deletes the currently selected macro variation.Does nothing if there is no se... |
| `insert_chain(Index: int = -1)`                       | `LomObject` | Inserts a new chain, either at the specified index or, if not index was speci... |
| `randomize_macros()`                                  | `None`      | Randomizes the values for all macro controls not excluded from randomization.    |
| `recall_last_used_variation()`                        | `None`      | Recalls the macro variation that was recalled most recently.Does nothing if n... |
| `recall_selected_variation()`                         | `None`      | Recalls the currently selected macro variation.Does nothing if there are no v... |
| `remove_macro()`                                      | `None`      | Decreases the number of visible macro controls in the rack.                      |
| `store_variation()`                                   | `None`      | Stores a new variation of the values of all currently mapped macros.             |

#### `add_macro()`

- **Returns:** `None`

Increases the number of visible macro controls in the rack. Throws an exception if the maximum number of macro controls is reached.

#### `copy_pad(source_index: int, destination_index: int)`

- **Returns:** `None`
- **Args:**
  - `source_index: int`
  - `destination_index: int`

Copies all contents of a drum pad from a source pad into a destination pad. copy_pad(source_index, destination_index) where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack. Throws an exception when the source pad is empty, or when the source or destination indices are not between 0 - 127.

#### `delete_selected_variation()`

- **Returns:** `None`

Deletes the currently selected macro variation.Does nothing if there is no selected variation.

#### `insert_chain(Index: int = -1)`

- **Returns:** `LomObject`
- **Args:**
  - `Index: int = -1`

Inserts a new chain, either at the specified index or, if not index was specified, at the end of the chain sequence.

#### `randomize_macros()`

- **Returns:** `None`

Randomizes the values for all macro controls not excluded from randomization.

#### `recall_last_used_variation()`

- **Returns:** `None`

Recalls the macro variation that was recalled most recently.Does nothing if no variation has been recalled yet.

#### `recall_selected_variation()`

- **Returns:** `None`

Recalls the currently selected macro variation.Does nothing if there are no variations.

#### `remove_macro()`

- **Returns:** `None`

Decreases the number of visible macro controls in the rack. Throws an exception if the minimum number of macro controls is reached.

#### `store_variation()`

- **Returns:** `None`

Stores a new variation of the values of all currently mapped macros

## RackDevice.View (Subclass)

> `Live.RackDevice.RackDevice.View`

Representing the view aspects of a rack device.

**Live Object:** `yes`

### Properties

| Property                    | Type         | Supports             |
| --------------------------- | ------------ | -------------------- |
| `canonical_parent`          | `RackDevice` | `get`                |
| `drum_pads_scroll_position` | `int`        | `get`/`set`/`listen` |
| `is_collapsed`              | `bool`       | `get`/`set`          |
| `is_showing_chain_devices`  | `bool`       | `get`/`set`/`listen` |
| `selected_chain`            | `None`       | `get`/`set`/`listen` |
| `selected_drum_pad`         | `DrumPad`    | `get`/`set`/`listen` |

#### `canonical_parent`

- **Type:** `RackDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the View.

#### `drum_pads_scroll_position`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the index of the lowest visible row of pads. Throws an exception if can_have_drum_pads is false.

#### `is_collapsed`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/Set/Listen if the device is shown collapsed in the device chain.

#### `is_showing_chain_devices`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Return whether the devices in the currently selected chain are visible. Throws an exception if can_have_chains is false.

#### `selected_chain`

- **Type:** `None`
- **Settable:** `yes`
- **Listenable:** `yes`

Return access to the currently selected chain.

#### `selected_drum_pad`

- **Type:** `DrumPad`
- **Settable:** `yes`
- **Listenable:** `yes`

Return access to the currently selected drum pad. Throws an exception if can_have_drum_pads is false.
