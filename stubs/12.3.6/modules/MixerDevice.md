---
module: MixerDevice
---

Represents the per-track mixer in Live. The `MixerDevice` class exposes
volume, panning, sends, cue volume, crossfader assignment, and track
activator as `DeviceParameter` objects ready for automation or remote
control.

## Classes

### MixerDevice

```yaml
kind: class
path: Live.MixerDevice.MixerDevice
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: |-
  This class represents a Mixer Device in Live, which gives you
  access to the Volume and Panning properties of a Track.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Track.Track
settable: false
raw_doc: Get the canonical parent of the mixer device.
```

##### crossfade_assign

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: 'Player- and ReturnTracks only: Access to the Track''s Crossfade Assign State.'
```

##### crossfader

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: 'MainTrack only: Const access to the Crossfader.'
```

##### cue_volume

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: 'MainTrack only: Const access to the Cue Volume Parameter.'
```

##### left_split_stereo

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Track's Left Split Stereo Panning Device Parameter.
```

##### panning

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Tracks Panning Device Parameter.
```

##### panning_mode

```yaml
kind: property
type: Live.MixerDevice.MixerDevice.panning_modes | int
settable: true
listenable: true
raw_doc: Access to the Track's Panning Mode.
refinement:
  type:
    probed: int
    confidence: high
    sources:
    - '[schema] applied per the enum-arg convention (see schema header).'
    - '[sister method] `panning_modes` enum lives nested inside `MixerDevice` (members `stereo: 0`, `stereo_split: 1`); the
      property name `panning_mode` is the direct snake-case of the enum.'
```

##### right_split_stereo

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Track's Right Split Stereo Panning Device Parameter.
```

##### sends

```yaml
kind: property
type: Live.Base.Vector[Live.DeviceParameter.DeviceParameter]
settable: false
listenable: true
raw_doc: Const access to the Tracks list of Send Amount Device Parameters.
```

##### song_tempo

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: 'MainTrack only: Const access to the Song''s Tempo.'
```

##### track_activator

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Tracks Activator Device Parameter.
```

##### volume

```yaml
kind: property
type: Live.DeviceParameter.DeviceParameter
settable: false
raw_doc: Const access to the Tracks Volume Device Parameter.
```

## Enums

### crossfade_assignments

```yaml
kind: enum
parent: MixerDevice
members:
  A: 0
  NONE: 1
  B: 2
```

### panning_modes

```yaml
kind: enum
parent: MixerDevice
members:
  stereo: 0
  stereo_split: 1
```
