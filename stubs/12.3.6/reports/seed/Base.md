---
module: Base
---

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
raw_doc: A simple container for returning floats from Live.
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
raw_doc: A simple container for returning unsigned long integers from Live.
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
settable: false
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
- name: arg1
  type: str
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
