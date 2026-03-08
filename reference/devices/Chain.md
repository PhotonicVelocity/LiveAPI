# Chain

> `Live.Chain.Chain`

This class represents a group device chain in Live. Chains exist inside rack devices
(Instrument Rack, Audio Effect Rack, MIDI Effect Rack, Drum Rack). Each chain contains its
own device list and mixer (volume, pan, sends). Chains can be nested -- a rack device inside
a chain can itself contain chains.

??? note "Raw probe notes (temporary)"
    - **Color snaps to palette** -- setting `color=0xABCDEF` reads back as `0xB9C1E3` (idx 37);
      setting `color=0xFF0000` (pure red) reads back as `0xFF3636` (idx 14). Same behavior as
      Track and Scene.
    - **Empty name reverts to default** -- setting `name=''` or `name='  '` (spaces) reads back
      as `'Chain'`. Empty/whitespace names are silently rejected and the name reverts to the
      default chain name.
    - **Solo does NOT update `muted_via_solo` synchronously** -- with 2 chains, soloing chain A
      leaves `B.muted_via_solo=False`. Even with both chains soloed, `muted_via_solo` stays
      `False`. This property may only update during audio engine processing or require a poll/
      dispatch cycle. Treat it as unreliable for immediate readback after setting `solo`.
    - **Audio effect chain I/O** -- `has_audio_input=True`, `has_audio_output=True`,
      `has_midi_input=False`, `has_midi_output=False` for chains in an Audio Effect Rack.
    - **`is_auto_colored`** -- new chains default to `True` with `color_index=0`.

### Open Questions

- ~~Does `insert_device()` work with third-party plug-in names, or only native Live devices?~~
  **Answered (2026-02-26):** Native only. Plug-in names like `"Raum"` return `Device Raum not found.`
  Internal `class_name` (e.g. `"Eq8"`) also fails -- must use exact `class_display_name` (`"EQ Eight"`).
  Case-sensitive (`"eq eight"` fails).
- What happens when calling `delete_device()` on the last device in a chain -- is an empty
  chain allowed, or does the rack collapse it?
- Does `duplicate_device()` appear in the Max docs under a different path? It's in the stub
  but not documented in the Max for Live chain reference.
- Does `muted_via_solo` require audio engine activity or a poll cycle to reflect the current
  state? Immediate readback after setting `solo` returns stale values.

### Children

| Child          | Returns            | Shape    | Listenable | Summary                                          |
| -------------- | ------------------ | -------- | ---------- | ------------------------------------------------ |
| `devices`      | `Sequence[Device]` | `list`   | `yes`      | Devices in this chain's device list.             |
| `mixer_device` | `ChainMixerDevice` | `single` | `no`       | Mixer parameters: volume, pan, sends, activator. |

#### `devices`

- **Type:** `Sequence[Device]`
- **Listenable:** `yes`
- **Since:** `<11`

The ordered list of devices in this chain. The listener fires when devices are added,
removed, or reordered. Use `insert_device()`, `delete_device()`, and `duplicate_device()`
to modify the list.

#### `mixer_device`

- **Type:** `ChainMixerDevice`
- **Listenable:** `no`
- **Since:** `<11`

The chain's mixer device, which exposes mixer parameters as `DeviceParameter` objects.
Contains `volume`, `panning`, `sends` (list), and `chain_activator`. Note: `volume`,
`panning`, and `sends` are only available in Audio Effect Racks and Instrument Racks.
`sends` is available for Drum Rack chains. `chain_activator` is always available.

### Properties

| Property           | Type   | Settable | Listenable | Summary                                                       |
| ------------------ | ------ | -------- | ---------- | ------------------------------------------------------------- |
| `color`            | `int`  | `int`    | `yes`      | Chain color as packed RGB `0x00rrggbb`.                       |
| `color_index`      | `int`  | `int`    | `yes`      | Chain color palette index.                                    |
| `has_audio_input`  | `bool` | no       | `no`       | `True` for all audio chains.                                  |
| `has_audio_output` | `bool` | no       | `no`       | `True` for audio chains and MIDI chains with an instrument.   |
| `has_midi_input`   | `bool` | no       | `no`       | `True` for all MIDI chains.                                   |
| `has_midi_output`  | `bool` | no       | `no`       | `True` for MIDI chains with no instrument.                    |
| `is_auto_colored`  | `bool` | `bool`   | `yes`      | When `True`, chain inherits the containing track/chain color. |
| `mute`             | `bool` | `bool`   | `yes`      | `True` = muted (chain activator off).                         |
| `muted_via_solo`   | `bool` | no       | `yes`      | `True` if muted because another chain in the rack is soloed.  |
| `name`             | `str`  | `str`    | `yes`      | Chain name as shown in the chain header.                      |
| `solo`             | `bool` | `bool`   | `yes`      | `True` = soloed. Does not auto-unsolo other chains.           |

#### `color`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Packed RGB color value in the form `0x00rrggbb` (i.e. `(2^16 * red) + (2^8 * green) + blue`,
where each component is 0-255). When setting, Live snaps to the nearest color in the palette.
Must set `is_auto_colored=False` first for the color to take effect.

- **Quirks:** Setting `color=0xABCDEF` reads back as `0xB9C1E3` (idx 37) due to palette snapping.

#### `color_index`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** `yes`
- **Since:** `<11`

Palette-based color index for the chain. The stub says "Access the color index of the
Chain." Prefer setting `color_index` over `color` when working with the Live palette.

#### `has_audio_input`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this chain can receive an audio signal. This is `True` for all audio chains
(chains inside Audio Effect Racks and Instrument Racks on audio tracks).

#### `has_audio_output`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this chain outputs an audio signal. This is `True` for all audio chains, and also
for MIDI chains that contain an instrument (since the instrument converts MIDI to audio).

#### `has_midi_input`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this chain can receive MIDI events. This is `True` for all MIDI chains (chains
inside MIDI Effect Racks, Instrument Racks on MIDI tracks, and Drum Racks).

#### `has_midi_output`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this chain outputs MIDI events. This is `True` for MIDI chains that do not contain
an instrument (the MIDI passes through unprocessed). `False` for MIDI chains with an
instrument, since the instrument consumes the MIDI and outputs audio.

#### `is_auto_colored`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

When `True`, the chain automatically inherits the color of its containing track or parent
chain. New chains default to `is_auto_colored=True`. Setting to `False` allows the chain to
have an independent color via `color` or `color_index`. Must be set to `False` before
setting `color` for the color change to take effect.

#### `mute`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The mute state of the chain. `True` means the chain activator is off and the chain does not
process audio/MIDI. Equivalent to clicking the chain's activator button in the rack UI.

#### `muted_via_solo`

- **Type:** `bool`
- **Listenable:** `yes`
- **Since:** `<11`

`True` when this chain is muted because another chain in the same rack is soloed. This is
read-only -- to affect this state, toggle `solo` on the other chain(s). Note: this property
does not update immediately after setting `solo` on a sibling chain. It may require audio
engine processing or a listener callback to reflect the current state. Do not rely on
immediate readback after modifying `solo`.

- **Quirks:** Does not update synchronously after setting `solo` on a sibling chain.

#### `name`

- **Type:** `str` (get) · `str` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The display name of the chain as shown in the chain header within the rack. Read/write.
Setting to an empty string `''` or whitespace `'  '` silently reverts to the default name
(e.g. `'Chain'`). The listener fires when the name changes.

- **Quirks:** Empty/whitespace names silently revert to the default name `'Chain'`.

#### `solo`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The solo state of the chain. Setting `solo=True` does **not** automatically unsolo other
chains in the same rack. For exclusive solo behavior, you must manually set `solo=False` on
the other chains. Note: `muted_via_solo` on sibling chains may not update synchronously --
see the `muted_via_solo` entry for details.

### Methods

| Method                                             | Returns  | Summary                                         |
| -------------------------------------------------- | -------- | ----------------------------------------------- |
| `delete_device(index: int)`                        | `None`   | Remove a device by index from this chain.       |
| `duplicate_device(index: int)`                     | `None`   | Duplicate the device at the given index.        |
| `insert_device(device_name: str, index: int = -1)` | `Device` | Insert a native Live device at the given index. |

#### `delete_device(index: int)`

- **Returns:** `None`
- **Args:**
    - `index: int` -- the index of the device to remove in the `devices` list
- **Raises:** Runtime error if `index` is out of range.
- **Since:** `<11`

Removes the device at the given index from this chain's device list. Throws a runtime error
if the index is invalid. The `devices` listener fires after the device is removed.

#### `duplicate_device(index: int)`

- **Returns:** `None`
- **Args:**
    - `index: int` -- the index of the device to duplicate in the `devices` list
- **Since:** `12.3`

Duplicates the device at the given index in this chain's device list. The copy is inserted
after the original. This method appears only in the stub -- not documented in the Max for
Live reference.

#### `insert_device(device_name: str, index: int = -1)`

- **Returns:** `Device` (the newly inserted device)
- **Args:**
    - `device_name: str` -- name of the device as it appears in the Live browser UI
    - `index: int = -1` -- position to insert at; `-1` means end of the chain
- **Raises:** `ValidationError: Device {name} not found.` if the name doesn't match any native device.
- **Since:** `12.3`

Inserts a native Live device at the specified position in this chain's device list.
**`device_name` must be the exact `class_display_name`** -- the name shown in the Live browser
(e.g. `"Compressor"`, `"EQ Eight"`, `"Operator"`). Matching is case-sensitive. The internal
`class_name` (e.g. `"Eq8"`, `"Compressor2"`) is not accepted.

Not all indices are valid. Indices outside the current device count are invalid, and
structural constraints apply -- for example, a MIDI effect cannot be inserted after an
instrument. The rule is: if the position would be invalid when dragging with the mouse,
it's invalid here.

- **Limitations:** Only native Live devices can be inserted. Max for Live devices and third-party
  plug-ins (VST/AU) are not supported.

---

## ChainMixerDevice

> `Live.Chain.ChainMixerDevice`

This class represents a chain's mixer device, which holds the mixer parameters for a chain
inside a rack device: volume, panning, send amounts, and the chain activator.

### Open Questions

- What does `sends` contain for chains in MIDI Effect Racks? Likely empty.
- Is `chain_activator` always index 0 in the mixer's parameter list?

### Children

| Child             | Returns                     | Shape    | Listenable | Summary                                                     |
| ----------------- | --------------------------- | -------- | ---------- | ----------------------------------------------------------- |
| `chain_activator` | `DeviceParameter`           | `single` | `no`       | The on/off toggle parameter for the chain.                  |
| `panning`         | `DeviceParameter`           | `single` | `no`       | Pan parameter. Audio/Instrument Racks only.                 |
| `sends`           | `Sequence[DeviceParameter]` | `list`   | `yes`      | Send amount parameters. Audio/Instrument Racks, Drum Racks. |
| `volume`          | `DeviceParameter`           | `single` | `no`       | Volume parameter. Audio/Instrument Racks only.              |

#### `chain_activator`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The chain activator parameter -- controls whether the chain is on or off. This is the same
toggle controlled by the `mute` property on the `Chain` object, exposed here as a
`DeviceParameter` for automation and mapping purposes.

#### `panning`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The pan parameter for the chain. Only available in Audio Effect Racks and Instrument Racks.

#### `sends`

- **Type:** `Sequence[DeviceParameter]`
- **Listenable:** `yes`
- **Since:** `<11`

The send amount parameters for the chain. Available in Audio Effect Racks, Instrument Racks,
and Drum Racks. The list fires a listener when send configuration changes.

#### `volume`

- **Type:** `DeviceParameter`
- **Listenable:** `no`
- **Since:** `<11`

The volume parameter for the chain. Only available in Audio Effect Racks and Instrument Racks.
