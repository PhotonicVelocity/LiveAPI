---
module: Listener
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
settable: false
raw_doc: Returns the original function
```

##### listener_self

```yaml
kind: property
settable: false
raw_doc: Returns the weak reference to original self, if it was a bound method
```

##### name

```yaml
kind: property
settable: false
raw_doc: Prints the name of the property that this listener is connected to
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
raw_doc: A read only container for accessing a list of listeners.
```
