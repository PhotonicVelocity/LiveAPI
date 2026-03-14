# FloatVector

> `Live.Base.FloatVector`

A simple container for returning floats from Live.

## Methods

| Method                  | Returns | Description |
| ----------------------- | ------- | ----------- |
| `append(value: float)`  | `None`  |             |
| `extend(values: float)` | `None`  |             |

### `append(value: float)`

- **Returns:** `None`
- **Args:**
  - `value: float`

### `extend(values: float)`

- **Returns:** `None`
- **Args:**
  - `values: float`

# IntU64Vector

> `Live.Base.IntU64Vector`

A simple container for returning unsigned long integers from Live.

## Methods

| Method                | Returns | Description |
| --------------------- | ------- | ----------- |
| `append(value: int)`  | `None`  |             |
| `extend(values: int)` | `None`  |             |

### `append(value: int)`

- **Returns:** `None`
- **Args:**
  - `value: int`

### `extend(values: int)`

- **Returns:** `None`
- **Args:**
  - `values: int`

# IntVector

> `Live.Base.IntVector`

A simple container for returning integers from Live.

## Methods

| Method                | Returns | Description |
| --------------------- | ------- | ----------- |
| `append(value: int)`  | `None`  |             |
| `extend(values: int)` | `None`  |             |

### `append(value: int)`

- **Returns:** `None`
- **Args:**
  - `value: int`

### `extend(values: int)`

- **Returns:** `None`
- **Args:**
  - `values: int`

# LimitationError

> `Live.Base.LimitationError`

# ObjectVector

> `Live.Base.ObjectVector`

A simple read only container for returning python objects.

## Methods

| Method                | Returns | Description |
| --------------------- | ------- | ----------- |
| `append(value: Any)`  | `None`  |             |
| `extend(values: Any)` | `None`  |             |

### `append(value: Any)`

- **Returns:** `None`
- **Args:**
  - `value: Any`

### `extend(values: Any)`

- **Returns:** `None`
- **Args:**
  - `values: Any`

# StringVector

> `Live.Base.StringVector`

A simple container for returning strings from Live.

## Methods

| Method                | Returns | Description |
| --------------------- | ------- | ----------- |
| `append(value: str)`  | `None`  |             |
| `extend(values: str)` | `None`  |             |

### `append(value: str)`

- **Returns:** `None`
- **Args:**
  - `value: str`

### `extend(values: str)`

- **Returns:** `None`
- **Args:**
  - `values: str`

# Text

> `Live.Base.Text`

A translatable, immutable string.

## Properties

| Property | Type  | Settable | Listenable | Description |
| -------- | ----- | -------- | ---------- | ----------- |
| `text`   | `str` | `no`     | `no`       |             |

### `text`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

# Timer

> `Live.Base.Timer`

A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback every interval. Errors in the callback will stop the timer.

**Constructor:** `Timer(callback: object, interval: int, repeat: bool = False, start: bool = False)`

## Properties

| Property  | Type   | Settable | Listenable | Description |
| --------- | ------ | -------- | ---------- | ----------- |
| `running` | `bool` | `no`     | `no`       |             |

### `running`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

## Methods

| Method      | Returns | Description |
| ----------- | ------- | ----------- |
| `restart()` | `None`  |             |
| `start()`   | `None`  |             |
| `stop()`    | `None`  |             |

### `restart()`

- **Returns:** `None`

### `start()`

- **Returns:** `None`

### `stop()`

- **Returns:** `None`

# Vector

> `Live.Base.Vector`

A simple read only container for returning objects from Live.

## Methods

| Method                      | Returns | Description |
| --------------------------- | ------- | ----------- |
| `append(value: LomObject)`  | `None`  |             |
| `extend(values: LomObject)` | `None`  |             |

### `append(value: LomObject)`

- **Returns:** `None`
- **Args:**
  - `value: LomObject`

### `extend(values: LomObject)`

- **Returns:** `None`
- **Args:**
  - `values: LomObject`

## Module Functions

| Function                                                                                       | Returns | Description                                                               |
| ---------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------- |
| `get_text(classname: str, textname: str)`                                                      | `Text`  | Retrieves the (translated) Text identified by `classname` and `textname`. |
| `log(string: str)`                                                                             | `None`  |                                                                           |
| `subst_args(text: Text, arg1: str = , arg2: str = , arg3: str = , arg4: str = , arg5: str = )` | `str`   |                                                                           |

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
