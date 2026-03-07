# TuningSystem

This class represents a tuning system in Live.

## Canonical Path

```
live_set tuning_system
```

## Properties

### name symbol observe

The name of the currently active tuning system.

### pseudo_octave_in_cents float read-only

The pseudo octave in cents of the currently active tuning system.

### lowest_note dictionary observe

The note index within the pseudo octave and octave of the lowest note.

### highest_note dictionary observe

The note index within the pseudo octave and octave of the highest note.

### reference_pitch dictionary observe

The reference pitch of the current tuning system.

### note_tunings dictionary observe

The relative note tunings of the Tuning System in cents. Provided as a single-element dictionary holding an array.
