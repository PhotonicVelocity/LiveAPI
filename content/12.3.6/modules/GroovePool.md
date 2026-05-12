---
module: GroovePool
---

Represents the Live Set's groove pool — the collection of `Groove` templates
available to clips. The `GroovePool` class lists the loaded grooves and
supports adding, removing, and committing changes back to the pool.

## Classes

### GroovePool

```yaml
kind: class
path: Live.GroovePool.GroovePool
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents the groove pool in Live.
```

#### Properties

##### canonical_parent

```yaml
kind: property
type: Live.Song.Song
settable: false
raw_doc: Get the canonical parent of the groove pool.
```

##### grooves

```yaml
kind: property
type: Live.Base.Vector[Live.Groove.Groove]
settable: false
listenable: true
raw_doc: Access to the list of grooves
```
