---
module: Listener
_note: |-
  Module-level prose (subscription model, lifetime, threading, listener-only
  triplets) and the "Listeners" page title now live in
  `stubs/12.3.6/foundation/listeners.md`. That foundation page pulls this
  module's structural content (`ListenerHandle` + `ListenerVector`) in via
  its `include_module: Listener` frontmatter directive.
---

## Classes

### ListenerHandle

```yaml
kind: class
path: Live.Listener.ListenerHandle
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents a Python listener when connected to a Live property.
```

#### Properties

##### listener_func

```yaml
kind: property
type: Callable
settable: false
raw_doc: Returns the original function
refinement:
  type:
    probed: null
    confidence: high
    sources:
    - '[docstring] "Returns the original function" — functions are Callable.'
```

##### listener_self

```yaml
kind: property
type: Any
settable: false
raw_doc: Returns the weak reference to original self, if it was a bound method
refinement:
  type:
    probed: null
    confidence: medium
    sources:
    - '[docstring] "weak reference to original self, if it was a bound method" — can be any object instance (or None for non-bound
      functions). `Any` is appropriately broad but could be `Any | None` if probed.'
```

##### name

```yaml
kind: property
type: str
settable: false
raw_doc: Prints the name of the property that this listener is connected to
refinement:
  type:
    probed: null
    confidence: medium
    sources:
    - '[docstring] "Prints the name of the property that this listener is connected to" — boost.python doc-style "Prints"
      implies a printable string return on a property access (returns the property name as a string). ListenerHandle is internal-only
      (zero corpus references); raw_doc is the strongest evidence available.'
```

#### Methods

##### disconnect

```yaml
kind: method
signature: 'disconnect( (ListenerHandle)arg1) -> None :'
cpp_signature: void disconnect(LPythonRemote {lvalue})
returns:
  type: None
raw_doc: Disconnects the listener from its property
```

### ListenerVector

```yaml
kind: class
path: Live.Listener.ListenerVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: Live.Listener.ListenerHandle
raw_doc: A read only container for accessing a list of listeners.
refinement:
  element_type:
    confidence: high
    sources:
    - '[docstring] "container for accessing a list of listeners" — contains ListenerHandle instances.'
```
