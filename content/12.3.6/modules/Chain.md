---
module: Chain
---

Represents a single device chain inside an Instrument, Drum, Audio Effect, or MIDI Effect Rack. The `Chain` class hosts
the chain's nested devices, per-chain `ChainMixerDevice`, and key/velocity/chain-selector zones.

## Classes

### Chain

```yaml
kind: class
path: Live.Chain.Chain
ancestors:
  - Live.Track.DeviceContainer
  - Live.LomObject.LomObject
  - Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a group device chain in Live.
behavior:
  - id: lifetime-c-owned
    assertion:
      Chain lifetime is owned by the parent rack — `Chain` instances are invalidated when the parent rack is deleted,
      replaced, or restructured. Holding a Chain reference across such operations raises on next access.
    confidence: high
    sources:
      - "[inference] LOM-wide invariant: every non-root LomObject's lifetime is bound to its parent's identity."
quirks:
  - id: phantom-via-devices
    assertion: A chain's `mixer_device` isn't reachable via `chain.devices` even though it's structurally a device.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.RackDevice.RackDevice
settable: false
raw_doc: Get the canonical parent of the chain.
```

##### color

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access the color index of the Chain.
```

##### color_index

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Access the color index of the Chain.
```

##### devices

```yaml
kind: property
type: Live.Base.Vector[Live.Device.Device]
settable: false
listenable: true
raw_doc: Return const access to all available Devices that are present in the chains
refinement:
  type:
    probed: Live.Base.Vector[Live.LomObject.LomObject]
    confidence: high
    sources:
      - "[C++ signature] binding declares the element type as `LomObject` — wider than what the container actually
        holds."
      - "[sister method] `Track.devices` is declared `Vector[Device]`."
      - '[docstring] "all available Devices" — matches the narrower runtime type.'
      - "[corpus] treats `track.devices` and `chain.devices` interchangeably as Device sequences:
        Launchpad_Pro/DrumGroupFinderComponent.py:65,74 filters `track_or_chain.devices` on `d.type ==
        DeviceType.instrument` (Device.type is a DeviceType enum; only Devices carry it);
        Push2/device_navigation.py:134,269,511 indexes `chain.devices[i]` as Device; pushbase/browser_modes.py:84-92
        indexes `chain.devices` as Device."
behavior:
  - id: excludes-mixer
    assertion:
      The vector excludes the chain's `mixer_device` — that lives on a separate property and isn't traversed by
      iteration here.
    confidence: high
    verified_against: 12.3.6
    sources:
      - "[probe] iterating `chain.devices` on a populated rack never yields `mixer_device`; the mixer is only reachable
        via `chain.mixer_device`."
      - "[corpus] every corpus access pairs `chain.devices` with a separate `chain.mixer_device` access when the mixer
        is needed (Push2/device_navigation.py, pushbase/browser_modes.py)."
quirks:
  - id: chain-order
    assertion:
      Order in the vector matches the audible signal chain — left-to-right in Live's Rack UI, top-to-bottom in the LOM.
```

Devices contained in the chain, in chain-order. The vector excludes the chain's `mixer_device`[^excludes-mixer] — that
lives on a separate property and is reached through its own accessor. Iteration is read-only^[Use `delete_device`,
`duplicate_device`, `insert_device` to mutate; in-place writes via `chain.devices[i] = ...` raise.] and the order
matches the audible signal chain — left-to-right in Live's Rack UI corresponds to top-to-bottom in the LOM, with audio
flowing from index 0 toward the end of the vector.

For most navigation purposes you treat this collection as if it returned plain `Device` values, even though the C++
binding's declared element type is the broader `LomObject` — that's why the type carries a refinement footnote
explaining the narrowing. Reflecting back into the LOM via `chain.devices[i].canonical_parent` returns the chain itself,
which is useful when walking the tree without keeping a separate parent reference.

##### has_audio_input

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Chain can be feed with an Audio signal. This is
  true for all Audio Chains.
```

##### has_audio_output

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Chain sends out an Audio signal. This is
  true for all Audio Chains, and MIDI chains with an Instrument.
```

##### has_midi_input

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Chain can be feed with an Audio signal. This is
  true for all MIDI Chains.
```

##### has_midi_output

```yaml
kind: property
type: bool
settable: false
raw_doc: |-
  return True, if this Chain sends out MIDI events. This is
  true for all MIDI Chains with no Instruments.
```

##### is_auto_colored

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/set access to the auto color flag of the Chain.
  If True, the Chain will always have the same color as the containing
  Track or Chain.
```

##### mixer_device

```yaml
kind: property
type: Live.ChainMixerDevice.ChainMixerDevice
settable: false
raw_doc: |-
  Return access to the mixer device that holds the chain's mixer parameters:
  the Volume, Pan, and Sendamounts.
```

##### mute

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: Mute/unmute the chain.
```

##### muted_via_solo

```yaml
kind: property
type: bool
settable: false
listenable: true
raw_doc: |-
  Return const access to whether this chain is muted due to some other chain
  being soloed.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Read/write access to the name of the Chain, as visible in the track header.
```

##### solo

```yaml
kind: property
type: bool
settable: true
listenable: true
raw_doc: |-
  Get/Set the solo status of the chain. Note that this will not disable the
  solo state of any other Chain in the same rack. If you want exclusive solo,
  you have to disable the solo state of the other Chains manually.
```

#### Methods

##### delete_device

```yaml
kind: method
signature: "delete_device( (Chain)arg1, (int)arg2) -> None :"
cpp_signature: void delete_device(TChainPyHandle,int)
args:
  - name: index
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - "[C++ signature] `void delete_device(TChainPyHandle, int)` — int."
          - '[docstring] "Remove a device identified by its index from the chain".'
          - "[M4L] chain.md: `Parameter: index [int]`."
          - "[corpus] the previous `device` rename was wrong: its lone def-vote came from Push2/device_navigation.py:151
            `def delete_device(device)`, a module-level helper that takes a Device object as a convenience and converts
            to an int index before calling the binding (`device_parent.delete_device(device_index)` at line 154)."
returns:
  type: None
raw_doc: Remove a device identified by its index from the chain. Throws runtime error if bad index.
```

##### duplicate_device

```yaml
kind: method
signature: "duplicate_device( (Chain)arg1, (int)arg2) -> None :"
cpp_signature: void duplicate_device(TChainPyHandle,int)
args:
  - name: index
    type: int
    refinement:
      name:
        probed: arg2
        sources:
          - '[docstring] "Duplicate the device at the given index in the chain".'
returns:
  type: None
raw_doc: Duplicate the device at the given index in the chain.
```

##### insert_device

```yaml
kind: method
signature: "insert_device( (Chain)arg1, (str)DeviceName [, (int)DeviceIndex=-1]) -> LomObject :"
cpp_signature:
  TWeakPtr<TPyHandleBase> insert_device(TChainPyHandle,std::__1::basic_string<char, std::__1::char_traits<char>,
  std::__1::allocator<char>> [,int=-1])
args:
  - name: device_name
    type: str
  - name: device_index
    type: int
    optional: true
    default: "-1"
returns:
  type: Live.Device.Device
  refinement:
    type:
      probed: Live.LomObject.LomObject
      confidence: high
      sources:
        - "[C++ signature] returns `TWeakPtr<TPyHandleBase>` (the generic LomObject handle) — no specific type enforced."
        - "[probe] `chain.devices` element_reprs are `<class 'Device.Device'>` (plus the `WavetableDevice` subclass) —
          the runtime returns properly-typed Device instances when iterated, so `insert_device` returning `Device`
          matches the observed instance type."
        - '[docstring] + [M4L] confirm semantics ("Add a device at a given index").'
raw_doc: Add a device at a given index in the chain. At end if -1.
```
