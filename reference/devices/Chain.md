# Chain (Module)

## Chain (Class)

> `Live.Chain.Chain`

This class represents a group device chain in Live.

**Live Object:** `yes`

**Access via:**

- `RackDevice.insert_chain()`

### Properties

| Property                                | Type                | Supports             |
| --------------------------------------- | ------------------- | -------------------- |
| [`canonical_parent`](#canonical_parent) | `RackDevice`        | `get`                |
| [`color`](#color)                       | `int`               | `get`/`set`/`listen` |
| [`color_index`](#color_index)           | `int`               | `get`/`set`/`listen` |
| [`devices`](#devices)                   | `Vector[LomObject]` | `get`/`listen`       |
| [`has_audio_input`](#has_audio_input)   | `bool`              | `get`                |
| [`has_audio_output`](#has_audio_output) | `bool`              | `get`                |
| [`has_midi_input`](#has_midi_input)     | `bool`              | `get`                |
| [`has_midi_output`](#has_midi_output)   | `bool`              | `get`                |
| [`is_auto_colored`](#is_auto_colored)   | `bool`              | `get`/`set`/`listen` |
| [`mixer_device`](#mixer_device)         | `ChainMixerDevice`  | `get`                |
| [`mute`](#mute)                         | `bool`              | `get`/`set`/`listen` |
| [`muted_via_solo`](#muted_via_solo)     | `bool`              | `get`/`listen`       |
| [`name`](#name)                         | `str`               | `get`/`set`/`listen` |
| [`solo`](#solo)                         | `bool`              | `get`/`set`/`listen` |

#### `canonical_parent`

- **Type:** `RackDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the chain.

#### `color`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access the color index of the Chain.

#### `color_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access the color index of the Chain.

#### `devices`

- **Type:** `Vector[LomObject]`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to all available Devices that are present in the chains

#### `has_audio_input`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Chain can be feed with an Audio signal. This is true for all Audio Chains.

#### `has_audio_output`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Chain sends out an Audio signal. This is true for all Audio Chains, and MIDI chains with an Instrument.

#### `has_midi_input`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Chain can be feed with an Audio signal. This is true for all MIDI Chains.

#### `has_midi_output`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Chain sends out MIDI events. This is true for all MIDI Chains with no Instruments.

#### `is_auto_colored`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/set access to the auto color flag of the Chain. If True, the Chain will always have the same color as the containing Track or Chain.

#### `mixer_device`

- **Type:** `ChainMixerDevice`
- **Settable:** `no`
- **Listenable:** `no`

Return access to the mixer device that holds the chain's mixer parameters: the Volume, Pan, and Sendamounts.

#### `mute`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Mute/unmute the chain.

#### `muted_via_solo`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `yes`

Return const access to whether this chain is muted due to some other chain being soloed.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `yes`

Read/write access to the name of the Chain, as visible in the track header.

#### `solo`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `yes`

Get/Set the solo status of the chain. Note that this will not disable the solo state of any other Chain in the same rack. If you want exclusive solo, you have to disable the solo state of the other Chains manually.

### Methods

| Method                                                                 | Returns  |
| ---------------------------------------------------------------------- | -------- |
| [`delete_device()`](#delete_devicedevice-int)                          | `None`   |
| [`duplicate_device()`](#duplicate_deviceindex-int)                     | `None`   |
| [`insert_device()`](#insert_devicedevice_name-str-device_index-int--1) | `Device` |

#### `delete_device(device: int)`

- **Returns:** `None`
- **Args:**
  - `device: int`

Remove a device identified by its index from the chain. Throws runtime error if bad index.

#### `duplicate_device(index: int)`

- **Returns:** `None`
- **Args:**
  - `index: int`

Duplicate the device at the given index in the chain.

#### `insert_device(device_name: str, device_index: int = -1)`

- **Returns:** `Device`
- **Args:**
  - `device_name: str`
  - `device_index: int = -1`

Add a device at a given index in the chain. At end if -1.
