---
module: Groove
---

Represents a single groove template stored in the Live Set's groove pool.
The `Groove` class exposes the groove's name and shaping parameters, which
any clip can adopt to bend its timing, velocity, and timing-random feel.

## Classes

### Groove

```yaml
kind: class
path: Live.Groove.Groove
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a groove in Live.
```

#### Properties

##### base

```yaml
kind: property
type: Live.Groove.Base
settable: true
raw_doc: Get/set the groove's base grid.
```

##### canonical_parent

```yaml
kind: property
type: Live.GroovePool.GroovePool
settable: false
raw_doc: Get the canonical parent of the groove.
```

##### name

```yaml
kind: property
type: str
settable: true
listenable: true
raw_doc: Read/write/listen access to the groove's name
```

##### quantization_amount

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Read/write/listen access to the groove's quantization amount.
```

##### random_amount

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Read/write/listen access to the groove's random amount.
```

##### timing_amount

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Read/write/listen access to the groove's timing amount.
```

##### velocity_amount

```yaml
kind: property
type: float
settable: true
listenable: true
raw_doc: Read/write/listen access to the groove's velocity amount.
```

## Enums

### Base

```yaml
kind: enum
members:
  gb_four: 0
  gb_eight: 1
  gb_eight_triplet: 2
  gb_sixteen: 3
  gb_sixteen_triplet: 4
  gb_thirtytwo: 5
  count: 6
```
