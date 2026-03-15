---
toc_depth: 2
---

# DrumChain (Module)

## DrumChain (Class)

> `Live.DrumChain.DrumChain`

This class represents a drum group device chain in Live.

**Live Object:** `yes`

### Properties

| Property                                | Type               | Supports             |
| --------------------------------------- | ------------------ | -------------------- |
| [`canonical_parent`](#canonical_parent) | `RackDevice`       | `get`                |
| [`choke_group`](#choke_group)           | `int`              | `get`/`set`/`listen` |
| [`color`](#color)                       | `int`              | `get`/`set`          |
| [`color_index`](#color_index)           | `int`              | `get`/`set`          |
| [`devices`](#devices)                   | `tuple`            | `get`                |
| [`has_audio_input`](#has_audio_input)   | `bool`             | `get`                |
| [`has_audio_output`](#has_audio_output) | `bool`             | `get`                |
| [`has_midi_input`](#has_midi_input)     | `bool`             | `get`                |
| [`has_midi_output`](#has_midi_output)   | `bool`             | `get`                |
| [`in_note`](#in_note)                   | `int`              | `get`/`set`/`listen` |
| [`is_auto_colored`](#is_auto_colored)   | `bool`             | `get`/`set`          |
| [`mixer_device`](#mixer_device)         | `ChainMixerDevice` | `get`                |
| [`mute`](#mute)                         | `bool`             | `get`/`set`          |
| [`muted_via_solo`](#muted_via_solo)     | `bool`             | `get`                |
| [`name`](#name)                         | `str`              | `get`/`set`          |
| [`out_note`](#out_note)                 | `int`              | `get`/`set`/`listen` |
| [`solo`](#solo)                         | `bool`             | `get`/`set`          |

#### `canonical_parent`

- **Type:** `RackDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the chain.

#### `choke_group`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the chain's choke group setting.

#### `color`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

Access the color index of the Chain.

#### `color_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

Access the color index of the Chain.

#### `devices`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `no`

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

#### `in_note`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the incoming MIDI note that will trigger this chain.

#### `is_auto_colored`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/set access to the auto color flag of the Chain. If True, the Chain will always have the same color as the containing Track or Chain.

#### `mixer_device`

- **Type:** `ChainMixerDevice`
- **Settable:** `no`
- **Listenable:** `no`

Return access to the mixer device that holds the chain's mixer parameters: the Volume, Pan, and Sendamounts.

#### `mute`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Mute/unmute the chain.

#### `muted_via_solo`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to whether this chain is muted due to some other chain being soloed.

#### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Read/write access to the name of the Chain, as visible in the track header.

#### `out_note`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the MIDI note sent to the devices in the chain.

#### `solo`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/Set the solo status of the chain. Note that this will not disable the solo state of any other Chain in the same rack. If you want exclusive solo, you have to disable the solo state of the other Chains manually.
