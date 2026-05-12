---
module: Base
---

The LOM's foundational layer. The `Vector` family — the generic base plus
its concrete subclasses — is what every collection-valued LOM property
returns; `Text` carries Live's translatable strings, and `Timer` schedules
callbacks.

## Classes

### FloatVector

```yaml
kind: class
path: Live.Base.FloatVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: float
raw_doc: A simple container for returning floats from Live.
refinement:
  element_type:
    confidence: high
    sources:
    - '[docstring] "A simple container for returning floats from Live".'
```

### IntU64Vector

```yaml
kind: class
path: Live.Base.IntU64Vector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: int
raw_doc: A simple container for returning unsigned long integers from Live.
refinement:
  element_type:
    confidence: high
    sources:
    - '[docstring] "container for returning unsigned long integers".'
```

### IntVector

```yaml
kind: class
path: Live.Base.IntVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: int
raw_doc: A simple container for returning integers from Live.
```

### LimitationError

```yaml
kind: class
path: Live.Base.LimitationError
ancestors:
- Exception
constructable: false
```

### ObjectVector

```yaml
kind: class
path: Live.Base.ObjectVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: object
raw_doc: A simple read only container for returning python objects.
```

### StringVector

```yaml
kind: class
path: Live.Base.StringVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: str
raw_doc: A simple container for returning strings from Live.
```

### Text

```yaml
kind: class
path: Live.Base.Text
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: A translatable, immutable string.
```

#### Properties

##### text

```yaml
kind: property
type: str
settable: false
refinement:
  type:
    probed: null
    confidence: high
    sources:
    - '[corpus] assigns/reads as string: pushbase/message_box_component.py:159 `self._message_box.text = message`; Push2/model/repr.py:726
      reads.'
    - '[M4L] docs confirm string content.'
```

### Timer

```yaml
kind: class
path: Live.Base.Timer
ancestors:
- Boost.Python.instance
init_doc: |-
  __init__( (object)arg1, (object)callback, (int)interval [, (bool)repeat=False [, (bool)start=False]]) -> None :

      C++ signature :
          void __init__(_object*,boost::python::api::object,int [,bool=False [,bool=False]])
constructable: true
raw_doc: A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback
  every interval. Errors in the callback will stop the timer.
```

#### Properties

##### running

```yaml
kind: property
type: bool
settable: false
```

#### Methods

##### `__init__`

```yaml
kind: method
args:
- name: callback
  type: object
- name: interval
  type: int
- name: repeat
  type: bool
  optional: true
  default: 'False'
- name: start
  type: bool
  optional: true
  default: 'False'
returns:
  type: None
```

##### restart

```yaml
kind: method
signature: 'restart( (Timer)arg1) -> None :'
cpp_signature: void restart(PythonTimer {lvalue})
returns:
  type: None
```

##### start

```yaml
kind: method
signature: 'start( (Timer)arg1) -> None :'
cpp_signature: void start(PythonTimer {lvalue})
returns:
  type: None
```

##### stop

```yaml
kind: method
signature: 'stop( (Timer)arg1) -> None :'
cpp_signature: void stop(PythonTimer {lvalue})
returns:
  type: None
```

### Vector

```yaml
kind: class
path: Live.Base.Vector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
parametric: true
raw_doc: A simple read only container for returning objects from Live.
```

Parametric base class — Live registers a single `Live.Base.Vector`
on the Boost.Python side and reuses it for every LOM list-valued
property whose elements are LomObjects. `Vector[Track]`,
`Vector[Clip]`, `Vector[Scene]`, `Vector[Device]`, ... all return
the **same** Python class; the element type varies per call site.

LomObject elements get the parametric form. Non-LomObject element
types get their own concrete container class (`IntVector`,
`StringVector`, `RoutingChannelVector`, `MidiNoteVector`,
`WarpMarkerVector`, ...), each declared on the module that owns
the element type and registered separately on the Boost.Python
side. One observed exception:
`Device.ATimeableValueVector` holds `DeviceParameter` (a
LomObject) but is its own concrete class — Live's naming suggests
"automatable value" is the relevant identity, not just "container
of parameters."

Behavior is identical across both patterns: iterable, indexable.
The structural distinction matters only for `isinstance` checks
and type annotations. The concrete `XVector` classes do **not**
derive from `Vector` — both `Live.Base.Vector` and every
`XVector` have the same single direct base,
`Boost.Python.instance`; they're siblings in the runtime class
hierarchy, not a parent / child chain.
`isinstance(routing_channels, Live.Base.Vector)` is structurally
False.

**Bound mutators.** Every container class binds `append` and
`extend` methods at the runtime level — Boost.Python wraps the
underlying C++ `std::vector<T>` operations. Live's own
docstring on `Vector` describes the class as "read only,"
however, and the LOM provides dedicated state-change methods
(`Track.create_audio_clip`, `Song.delete_track`, ...) for
modifying tracked collections. Whether calling `append` /
`extend` directly on a LOM-returned vector produces consistent
state (listener fires, UI updates, persistence) is **unverified**.

## Functions

### get_text

```yaml
kind: function
signature: 'get_text( (str)classname, (str)textname) -> Text :'
cpp_signature: TText const* get_text(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>,std::__1::basic_string<char,
  std::__1::char_traits<char>, std::__1::allocator<char>>)
args:
- name: classname
  type: str
- name: textname
  type: str
returns:
  type: Live.Base.Text
raw_doc: Retrieves the (translated) Text identified by `classname` and `textname`.
```

### log

```yaml
kind: function
signature: 'log( (str)arg1) -> None :'
cpp_signature: void log(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>)
args:
- name: string
  type: str
  refinement:
    name:
      probed: arg1
      sources:
      - '[corpus] callsite, 3/3 defs name `string`: corpus def external/corpus/LV2_LX2_LC2_LD2/FaderfoxComponent.py:24 (+2
        more).'
returns:
  type: None
```

### subst_args

```yaml
kind: function
signature: 'subst_args( (Text)text [, (str)arg1='''' [, (str)arg2='''' [, (str)arg3='''' [, (str)arg4='''' [, (str)arg5='''']]]]])
  -> str :'
cpp_signature: std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>> subst_args(TText [,std::__1::basic_string<char,
  std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>=''
  [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char,
  std::__1::char_traits<char>, std::__1::allocator<char>>='' [,std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char>>='']]]]])
args:
- name: text
  type: Live.Base.Text
- name: arg1
  type: str
  optional: true
  default: ''''''
- name: arg2
  type: str
  optional: true
  default: ''''''
- name: arg3
  type: str
  optional: true
  default: ''''''
- name: arg4
  type: str
  optional: true
  default: ''''''
- name: arg5
  type: str
  optional: true
  default: ''''''
returns:
  type: str
```
