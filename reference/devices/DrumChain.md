# DrumChain

> `Live.DrumChain.DrumChain`

This class represents a drum group device chain in Live.

## Properties

| Property           | Type               | Settable | Listenable | Description                                                                      |
| ------------------ | ------------------ | -------- | ---------- | -------------------------------------------------------------------------------- |
| `canonical_parent` | `RackDevice`       | `no`     | `no`       | Get the canonical parent of the chain.                                           |
| `choke_group`      | `int`              | `yes`    | `yes`      | Access to the chain's choke group setting.                                       |
| `color`            | `int`              | `yes`    | `no`       | Access the color index of the Chain.                                             |
| `color_index`      | `int`              | `yes`    | `no`       | Access the color index of the Chain.                                             |
| `devices`          | `tuple`            | `no`     | `no`       | Return const access to all available Devices that are present in the chains.     |
| `has_audio_input`  | `bool`             | `no`     | `no`       | return True, if this Chain can be feed with an Audio signal.                     |
| `has_audio_output` | `bool`             | `no`     | `no`       | return True, if this Chain sends out an Audio signal.                            |
| `has_midi_input`   | `bool`             | `no`     | `no`       | return True, if this Chain can be feed with an Audio signal.                     |
| `has_midi_output`  | `bool`             | `no`     | `no`       | return True, if this Chain sends out MIDI events.                                |
| `in_note`          | `int`              | `yes`    | `yes`      | Access to the incoming MIDI note that will trigger this chain.                   |
| `is_auto_colored`  | `bool`             | `yes`    | `no`       | Get/set access to the auto color flag of the Chain.                              |
| `mixer_device`     | `ChainMixerDevice` | `no`     | `no`       | Return access to the mixer device that holds the chain's mixer parameters: th... |
| `mute`             | `bool`             | `yes`    | `no`       | Mute/unmute the chain.                                                           |
| `muted_via_solo`   | `bool`             | `no`     | `no`       | Return const access to whether this chain is muted due to some other chain be... |
| `name`             | `str`              | `yes`    | `no`       | Read/write access to the name of the Chain, as visible in the track header.      |
| `out_note`         | `int`              | `yes`    | `yes`      | Access to the MIDI note sent to the devices in the chain.                        |
| `solo`             | `bool`             | `yes`    | `no`       | Get/Set the solo status of the chain.                                            |

### `canonical_parent`

- **Type:** `RackDevice`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the chain.

### `choke_group`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the chain's choke group setting.

### `color`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

Access the color index of the Chain.

### `color_index`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `no`

Access the color index of the Chain.

### `devices`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to all available Devices that are present in the chains

### `has_audio_input`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Chain can be feed with an Audio signal. This is true for all Audio Chains.

### `has_audio_output`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Chain sends out an Audio signal. This is true for all Audio Chains, and MIDI chains with an Instrument.

### `has_midi_input`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Chain can be feed with an Audio signal. This is true for all MIDI Chains.

### `has_midi_output`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

return True, if this Chain sends out MIDI events. This is true for all MIDI Chains with no Instruments.

### `in_note`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the incoming MIDI note that will trigger this chain.

### `is_auto_colored`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/set access to the auto color flag of the Chain. If True, the Chain will always have the same color as the containing Track or Chain.

### `mixer_device`

- **Type:** `ChainMixerDevice`
- **Settable:** `no`
- **Listenable:** `no`

Return access to the mixer device that holds the chain's mixer parameters: the Volume, Pan, and Sendamounts.

### `mute`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Mute/unmute the chain.

### `muted_via_solo`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Return const access to whether this chain is muted due to some other chain being soloed.

### `name`

- **Type:** `str`
- **Settable:** `yes`
- **Listenable:** `no`

Read/write access to the name of the Chain, as visible in the track header.

### `out_note`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Access to the MIDI note sent to the devices in the chain.

### `solo`

- **Type:** `bool`
- **Settable:** `yes`
- **Listenable:** `no`

Get/Set the solo status of the chain. Note that this will not disable the solo state of any other Chain in the same rack. If you want exclusive solo, you have to disable the solo state of the other Chains manually.
