# DrumPad

## DrumPad

This class represents a single pad in a Drum Rack device. Each drum pad is mapped to a
specific MIDI note and can contain its own chain of devices. Drum pads live inside a
Drum Rack device and are accessed via the `drum_pads` property on `RackDevice`.

### Sources

- **Primary:** `Live/classes/DrumPad.py` (stub dump)
- **Secondary:** `MaxForLive/drumpad.md`
- **Probes:** `probe_rack_macros.py`, `probe_rack_macros2.py`

### Probe Notes

Probed against Live 12.3.5 via `probe_rack_macros2.py`.

- **Type name:** Bridge returns `"DrumPad"`.
- **Count:** 128 drum pads total, 16 visible at a time (`visible_drum_pads`).
- **note:** Range 0–127 (standard MIDI). Pad [0] = note 0 (`C-2`), pad [127] = note 127 (`G8`).
- **name (empty pad):** Returns the musical note name of the pad (e.g. `"C-2"`, `"C♯-2"`, `"D-2"`).
  Derived from contained chains — when no chains are present, it shows the note name.
- **mute/solo defaults:** Both `False` on a fresh Drum Rack.
- **chains (empty pad):** 0 chains for unloaded pads.

### Open Questions

- Can `mute` and `solo` be set on a pad that has no chains? Or does the pad need at least
  one chain for mute/solo to have any effect?
- ~~Does `solo` behave like an exclusive solo, or can multiple pads be soloed simultaneously?~~
  **Confirmed: non-exclusive** (Max docs + same pattern as Chain).
- ~~What is the range of valid `note` values?~~ **Answered: 0–127 (standard MIDI).**
- ~~Does `name` reflect a user-assigned name, or is it always derived from the contained
  chains?~~ **Answered: always derived. Empty pads show musical note names (e.g. `"C-2"`).**
- Does `delete_all_chains` fire both the `chains` listener and the `name` listener?

### Children

| Child    | Returns           | Shape  | Access | Listenable | Available Since | Summary                                |
| -------- | ----------------- | ------ | ------ | ---------- | --------------- | -------------------------------------- |
| `chains` | `Sequence[Chain]` | `list` | `get`  | `yes`      | `<11`           | The chains contained in this drum pad. |

#### `chains`

- **Returns:** `Sequence[Chain]`
- **Shape:** `list`
- **Access:** `get`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The list of chains inside this drum pad. A pad can contain zero or more chains, each with
its own device list. The listener fires when chains are added or removed. Use
`delete_all_chains()` to remove all chains from the pad, which is equivalent to deleting the
pad's contents in the Live UI. Probed: empty pads return 0 chains.

### Properties

| Property | Get Returns | Set Accepts | Listenable | Available Since | Summary                                                     |
| -------- | ----------- | ----------- | ---------- | --------------- | ----------------------------------------------------------- |
| `mute`   | `bool`      | `bool`      | `yes`      | `<11`           | `True` = pad is muted.                                      |
| `name`   | `str`       | —           | `yes`      | `<11`           | Display name of the pad, derived from its contained chains. |
| `note`   | `int`       | —           | `no`       | `<11`           | The MIDI note number this pad is mapped to.                 |
| `solo`   | `bool`      | `bool`      | `yes`      | `<11`           | `True` = pad is soloed.                                     |

#### `mute`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The mute state of the drum pad. When `True`, the pad is muted and does not produce sound.
Equivalent to toggling the pad's mute button in the Drum Rack UI. Probed: defaults to
`False` on a fresh Drum Rack. Readable on empty pads (no chains).

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The display name of the drum pad. This is read-only and is derived from the chains contained
in the pad. The listener fires when the name changes, which can happen when chains are added,
removed, or renamed within the pad. Probed: empty pads show musical note names (e.g. `"C-2"`,
`"C♯-2"`, `"D-2"`).

#### `note`

- **Get Returns:** `int`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The MIDI note number that this drum pad is mapped to. Each pad in a Drum Rack corresponds to
a specific MIDI note. This value is read-only and does not have a listener. Probed: range
0–127. Pad [0] = note 0 (`C-2`), pad [127] = note 127 (`G8`).

#### `solo`

- **Get Returns:** `bool`
- **Set Accepts:** `bool`
  - **Undo-tracked:** `Unknown`
  - **Async visibility:** `Unknown`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `probed 12.3.5`

**Description:**
The solo state of the drum pad. When `True`, the pad is soloed. Setting `solo=True` does
**not** automatically unsolo other pads in the same Drum Rack. For exclusive solo behavior,
you must manually set `solo=False` on the other pads. Probed: defaults to `False`.
Readable on empty pads (no chains).

### Methods

| Signature             | Returns | Available Since | Summary                               |
| --------------------- | ------- | --------------- | ------------------------------------- |
| `delete_all_chains()` | `None`  | `<11`           | Remove all chains from this drum pad. |

#### `delete_all_chains()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Removes all chains from the pad, clearing its contents.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub | max`
- **Probe Status:** `unprobed` (not probed — need pad with content to test)

**Description:**
Deletes all chains contained in this drum pad. This is equivalent to deleting a drum rack
pad's contents in the Live UI. After calling this method, the `chains` list will be empty
and the `chains` listener will fire.
