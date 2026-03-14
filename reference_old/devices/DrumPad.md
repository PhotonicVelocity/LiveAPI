# DrumPad

> `Live.DrumPad.DrumPad`

This class represents a single pad in a Drum Rack device. Each drum pad is mapped to a
specific MIDI note and can contain its own chain of devices. Drum pads live inside a
Drum Rack device and are accessed via the `drum_pads` property on `RackDevice`.

??? note "Raw probe notes (temporary)"
    Probed against Live 12.3.5 via `probe_rack_macros2.py`.

    - **Type name:** Bridge returns `"DrumPad"`.
    - **Count:** 128 drum pads total, 16 visible at a time (`visible_drum_pads`).
    - **note:** Range 0-127 (standard MIDI). Pad [0] = note 0 (`C-2`), pad [127] = note 127
      (`G8`).
    - **name (empty pad):** Returns the musical note name of the pad (e.g. `"C-2"`, `"C#-2"`,
      `"D-2"`). Derived from contained chains -- when no chains are present, it shows the note name.
    - **mute/solo defaults:** Both `False` on a fresh Drum Rack.
    - **chains (empty pad):** 0 chains for unloaded pads.

### Children

| Child    | Returns           | Shape  | Listenable | Summary                                |
| -------- | ----------------- | ------ | ---------- | -------------------------------------- |
| `chains` | `Sequence[Chain]` | `list` | `yes`      | The chains contained in this drum pad. |

#### `chains`

- **Type:** `Sequence[Chain]`
- **Listenable:** `yes`
- **Since:** `<11`

The list of chains inside this drum pad. A pad can contain zero or more chains, each with
its own device list. The listener fires when chains are added or removed. Use
`delete_all_chains()` to remove all chains from the pad, which is equivalent to deleting the
pad's contents in the Live UI.

### Properties

| Property | Type   | Settable | Listenable | Summary                                                     |
| -------- | ------ | -------- | ---------- | ----------------------------------------------------------- |
| `mute`   | `bool` | yes      | `yes`      | `True` = pad is muted.                                      |
| `name`   | `str`  | no       | `yes`      | Display name of the pad, derived from its contained chains. |
| `note`   | `int`  | no       | `no`       | The MIDI note number this pad is mapped to.                 |
| `solo`   | `bool` | yes      | `yes`      | `True` = pad is soloed.                                     |

#### `mute`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The mute state of the drum pad. When `True`, the pad is muted and does not produce sound.
Equivalent to toggling the pad's mute button in the Drum Rack UI. Defaults to `False`.

#### `name`

- **Type:** `str`
- **Listenable:** `yes`
- **Since:** `<11`

The display name of the drum pad. This is read-only and is derived from the chains contained
in the pad. The listener fires when the name changes, which can happen when chains are added,
removed, or renamed within the pad. Empty pads show musical note names (e.g. `"C-2"`, `"C#-2"`,
`"D-2"`).

#### `note`

- **Type:** `int`
- **Listenable:** `no`
- **Since:** `<11`

The MIDI note number that this drum pad is mapped to. Each pad in a Drum Rack corresponds to
a specific MIDI note. Range 0-127. Pad [0] = note 0 (`C-2`), pad [127] = note 127 (`G8`).

#### `solo`

- **Type:** `bool` (get) · `bool` (set)
- **Listenable:** `yes`
- **Since:** `<11`

The solo state of the drum pad. When `True`, the pad is soloed. Setting `solo=True` does
**not** automatically unsolo other pads in the same Drum Rack. For exclusive solo behavior,
you must manually set `solo=False` on the other pads. Defaults to `False`.

### Methods

| Method                | Returns | Summary                               |
| --------------------- | ------- | ------------------------------------- |
| `delete_all_chains()` | `None`  | Remove all chains from this drum pad. |

#### `delete_all_chains()`

- **Returns:** `None`
- **Since:** `<11`

Deletes all chains contained in this drum pad. This is equivalent to deleting a drum rack
pad's contents in the Live UI. After calling this method, the `chains` list will be empty
and the `chains` listener will fire.

### Open Questions

- Can `mute` and `solo` be set on a pad that has no chains? Or does the pad need at least
  one chain for mute/solo to have any effect?
- Does `delete_all_chains` fire both the `chains` listener and the `name` listener?
