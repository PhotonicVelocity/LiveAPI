# Base (Module)

## FloatVector (Class)

> `Live.Base.FloatVector`

A simple container for returning floats from Live.

### Methods

| Method                                         | Returns |
| ---------------------------------------------- | ------- |
| [`append(value: float)`](#appendvalue-float)   | `None`  |
| [`extend(values: float)`](#extendvalues-float) | `None`  |

#### `append(value: float)`

- **Returns:** `None`
- **Args:**
  - `value: float`

#### `extend(values: float)`

- **Returns:** `None`
- **Args:**
  - `values: float`

## IntU64Vector (Class)

> `Live.Base.IntU64Vector`

A simple container for returning unsigned long integers from Live.

### Methods

| Method                                     | Returns |
| ------------------------------------------ | ------- |
| [`append(value: int)`](#appendvalue-int)   | `None`  |
| [`extend(values: int)`](#extendvalues-int) | `None`  |

#### `append(value: int)`

- **Returns:** `None`
- **Args:**
  - `value: int`

#### `extend(values: int)`

- **Returns:** `None`
- **Args:**
  - `values: int`

## IntVector (Class)

> `Live.Base.IntVector`

A simple container for returning integers from Live.

### Methods

| Method                                     | Returns |
| ------------------------------------------ | ------- |
| [`append(value: int)`](#appendvalue-int)   | `None`  |
| [`extend(values: int)`](#extendvalues-int) | `None`  |

#### `append(value: int)`

- **Returns:** `None`
- **Args:**
  - `value: int`

#### `extend(values: int)`

- **Returns:** `None`
- **Args:**
  - `values: int`

## LimitationError (Class)

> `Live.Base.LimitationError`

## ObjectVector (Class)

> `Live.Base.ObjectVector`

A simple read only container for returning python objects.

### Methods

| Method                                     | Returns |
| ------------------------------------------ | ------- |
| [`append(value: Any)`](#appendvalue-any)   | `None`  |
| [`extend(values: Any)`](#extendvalues-any) | `None`  |

#### `append(value: Any)`

- **Returns:** `None`
- **Args:**
  - `value: Any`

#### `extend(values: Any)`

- **Returns:** `None`
- **Args:**
  - `values: Any`

## StringVector (Class)

> `Live.Base.StringVector`

A simple container for returning strings from Live.

### Methods

| Method                                     | Returns |
| ------------------------------------------ | ------- |
| [`append(value: str)`](#appendvalue-str)   | `None`  |
| [`extend(values: str)`](#extendvalues-str) | `None`  |

#### `append(value: str)`

- **Returns:** `None`
- **Args:**
  - `value: str`

#### `extend(values: str)`

- **Returns:** `None`
- **Args:**
  - `values: str`

## Text (Class)

> `Live.Base.Text`

A translatable, immutable string.

### Properties

| Property        | Type  | Supports |
| --------------- | ----- | -------- |
| [`text`](#text) | `str` | `get`    |

#### `text`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

## Timer (Class)

> `Live.Base.Timer`

A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback every interval. Errors in the callback will stop the timer.

**Constructor:** `Timer(callback: object, interval: int, repeat: bool = False, start: bool = False)`

### Properties

| Property              | Type   | Supports |
| --------------------- | ------ | -------- |
| [`running`](#running) | `bool` | `get`    |

#### `running`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

### Methods

| Method                  | Returns |
| ----------------------- | ------- |
| [`restart()`](#restart) | `None`  |
| [`start()`](#start)     | `None`  |
| [`stop()`](#stop)       | `None`  |

#### `restart()`

- **Returns:** `None`

#### `start()`

- **Returns:** `None`

#### `stop()`

- **Returns:** `None`

## Vector (Class)

> `Live.Base.Vector`

A simple read only container for returning objects from Live.

### Methods

| Method                                                 | Returns |
| ------------------------------------------------------ | ------- |
| [`append(value: LomObject)`](#appendvalue-lomobject)   | `None`  |
| [`extend(values: LomObject)`](#extendvalues-lomobject) | `None`  |

#### `append(value: LomObject)`

- **Returns:** `None`
- **Args:**
  - `value: LomObject`

#### `extend(values: LomObject)`

- **Returns:** `None`
- **Args:**
  - `values: LomObject`

## Module Functions

| Function                                                                                                                                                            | Returns |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| [`get_text(classname: str, textname: str)`](#get_textclassname-str-textname-str)                                                                                    | `Text`  |
| [`log(string: str)`](#logstring-str)                                                                                                                                | `None`  |
| [`subst_args(text: Text, arg1: str = , arg2: str = , arg3: str = , arg4: str = , arg5: str = )`](#subst_argstext-text-arg1-str-arg2-str-arg3-str-arg4-str-arg5-str) | `str`   |

### `get_text(classname: str, textname: str)`

- **Returns:** `Text`
- **Args:**
  - `classname: str`
  - `textname: str`

Retrieves the (translated) Text identified by `classname` and `textname`.

### `log(string: str)`

- **Returns:** `None`
- **Args:**
  - `string: str`

### `subst_args(text: Text, arg1: str = , arg2: str = , arg3: str = , arg4: str = , arg5: str = )`

- **Returns:** `str`
- **Args:**
  - `text: Text`
  - `arg1: str = `
  - `arg2: str = `
  - `arg3: str = `
  - `arg4: str = `
  - `arg5: str = `
