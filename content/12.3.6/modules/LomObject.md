---
module: LomObject
_note: |-
  Module-level prose (intro, lifetime/identity model, collections) and
  the "Live Object Model" page title now live in
  `content/12.3.6/live-object-model.md`. That foundation page pulls
  this module's structural content (`Live.LomObject.LomObject` class +
  `_live_ptr` / `canonical_parent` properties) in via its
  `include_module: LomObject` frontmatter directive.
---

## Classes

### LomObject

```yaml
kind: class
path: Live.LomObject.LomObject
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: this is the base class for an object that is accessible via the LOM
```

#### Properties

##### `_live_ptr`

```yaml
kind: property
type: int
settable: false
```

##### canonical_parent

```yaml
kind: property
type: Live.LomObject.LomObject | None
settable: false
raw_doc: Get the canonical parent — the structural owner one step up the LOM tree.
_synthesized: true
_synthesis_note: |-
  Conceptually universal across LOM-tree nodes but not declared
  on `LomObject` itself in Live's runtime. Application and Song
  probe as the only LOM nodes whose `canonical_parent` returns
  None (they sit at the root). All other concrete LOM classes
  return a concrete parent type.
```
