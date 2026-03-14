# DrumChain

> `Live.DrumChain.DrumChain`

This class represents a Drum Rack device chain in Live. DrumChain extends [Chain](Chain.md), inheriting all
of Chain's children, properties, and methods. The members documented below are the additions unique to
DrumChain.

Each pad in a Drum Rack corresponds to one DrumChain. The chain is triggered by an incoming MIDI note
(`in_note`) and can remap that note before sending it to its internal devices (`out_note`). Chains can be
assigned to a choke group so that triggering one pad silences others in the same group.

??? note "Raw probe notes (temporary)"
    Probed with Live 12.3.5. A fresh Drum Rack has no chains; `insert_chain(0)` creates a
    `DrumChain` (type name confirmed: `"DrumChain"`). Default values on a newly inserted
    chain: `choke_group=0`, `in_note=36`, `out_note=60`.

    - **`choke_group`** — range is **0–16**. `0` means no choke group. Values 17+ and
      negative values raise `"Invalid choke group"`.
    - **`in_note`** — range is **0–127**. `-1` raises `"Invalid note number"` — the "All
      Notes" setting from the Max docs is **not settable** via the Python API.
    - **`out_note`** — range is **0–127**. Values outside this range raise `"Invalid note"`.
      Default is `60` (C3), independent of `in_note` (which defaults to `36`/C1).
    - **Duplicate `in_note`** — multiple chains can share the same `in_note` without error.
      No auto-reassignment or validation against existing chains.
    - **`insert_chain` defaults** — every newly inserted chain gets `in_note=36`, `out_note=60`
      regardless of how many chains already exist (no auto-assignment to unique notes).
    - **Undo tracking** — inconclusive. Calling `song.undo()` after setting `choke_group`
      invalidated the chain handle (likely undid the `insert_chain` operation, destroying the
      object). A more targeted test with a pre-existing chain is needed.

### Open Questions

- Undo tracking for all three properties (see probe notes).

### Properties

| Property      | Type  | Settable | Listenable | Summary                                            |
| ------------- | ----- | -------- | ---------- | -------------------------------------------------- |
| `choke_group` | `int` | yes      | yes        | Choke group (0–16). `0` = no choke group.          |
| `in_note`     | `int` | yes      | yes        | Incoming MIDI note (0–127). `-1` is NOT supported. |
| `out_note`    | `int` | yes      | yes        | Output MIDI note (0–127).                          |

#### `choke_group`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `<11`

The choke group assignment for this drum chain. When multiple chains share the same choke group, triggering
one chain silences the others in that group — useful for open/closed hi-hat behavior. `0` means no choke
group. Valid range is 0–16 (16 choke groups plus "none"). Values outside this range raise
`"Invalid choke group"`.

#### `in_note`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `12.3`

The incoming MIDI note number that triggers this drum chain. Each pad in a Drum Rack maps to a specific MIDI
note (0–127). The listener fires when the trigger note assignment changes.

**Limitations:**

- The Max docs describe `-1` as "All Notes", but setting `-1` via the Python API raises
  `"Invalid note number"` — the "All Notes" mode appears to be UI-only.

#### `out_note`

- **Type:** `int` (get) · `int` (set)
- **Listenable:** yes
- **Since:** `<11`

The MIDI note sent to the devices inside this chain. By default `60` (C3) on a newly inserted chain,
independent of `in_note` (`36`/C1). Can be set independently to remap the note before it reaches the chain's
devices. Values outside 0–127 raise `"Invalid note"`. The listener fires when the output note changes.
