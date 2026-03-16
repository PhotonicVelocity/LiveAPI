# Base (Module)

## FloatVector (Class)

> `Live.Base.FloatVector`

A simple container for returning floats from Live.

### Methods

| Method                            | Returns |
| --------------------------------- | ------- |
| [`append()`](#appendvalue-float)  | `None`  |
| [`extend()`](#extendvalues-float) | `None`  |

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

| Method                          | Returns |
| ------------------------------- | ------- |
| [`append()`](#appendvalue-int)  | `None`  |
| [`extend()`](#extendvalues-int) | `None`  |

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

| Method                          | Returns |
| ------------------------------- | ------- |
| [`append()`](#appendvalue-int)  | `None`  |
| [`extend()`](#extendvalues-int) | `None`  |

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

| Method                                  | Returns |
| --------------------------------------- | ------- |
| [`append()`](#appendvalue-any)          | `None`  |
| [`extend()`](#extendvalues-iterableany) | `None`  |

#### `append(value: Any)`

- **Returns:** `None`
- **Args:**
  - `value: Any`

#### `extend(values: Iterable[Any])`

- **Returns:** `None`
- **Args:**
  - `values: Iterable[Any]`

## StringVector (Class)

> `Live.Base.StringVector`

A simple container for returning strings from Live.

### Methods

| Method                          | Returns |
| ------------------------------- | ------- |
| [`append()`](#appendvalue-str)  | `None`  |
| [`extend()`](#extendvalues-str) | `None`  |

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

| Method                                         | Returns          |
| ---------------------------------------------- | ---------------- |
| [`__iter__()`](#__iter__)                      | `Iterator[T]`    |
| [`__getitem__()`](#__getitem__index-int)       | `T`              |
| [`__getitem__()`](#__getitem__index-slice)     | `Vector[T]`      |
| [`__getitem__()`](#__getitem__index-int-slice) | `T \| Vector[T]` |
| [`__len__()`](#__len__)                        | `int`            |
| [`__contains__()`](#__contains__value-object)  | `bool`           |
| [`__bool__()`](#__bool__)                      | `bool`           |
| [`append()`](#appendvalue-any)                 | `None`           |
| [`extend()`](#extendvalues-iterableany)        | `None`           |

#### `__iter__()`

- **Returns:** `Iterator[T]`

#### `__getitem__(index: int)`

- **Returns:** `T`
- **Args:**
  - `index: int`

#### `__getitem__(index: slice)`

- **Returns:** `Vector[T]`
- **Args:**
  - `index: slice`

#### `__getitem__(index: int | slice)`

- **Returns:** `T | Vector[T]`
- **Args:**
  - `index: int | slice`

#### `__len__()`

- **Returns:** `int`

#### `__contains__(value: object)`

- **Returns:** `bool`
- **Args:**
  - `value: object`

#### `__bool__()`

- **Returns:** `bool`

#### `append(value: Any)`

- **Returns:** `None`
- **Args:**
  - `value: Any`

#### `extend(values: Iterable[Any])`

- **Returns:** `None`
- **Args:**
  - `values: Iterable[Any]`

## Module Functions

| Function                                                                            | Returns |
| ----------------------------------------------------------------------------------- | ------- |
| [`get_text()`](#get_textclassname-str-textname-str)                                 | `Text`  |
| [`log()`](#logarg1-str)                                                             | `None`  |
| [`subst_args()`](#subst_argstext-text-arg1-str-arg2-str-arg3-str-arg4-str-arg5-str) | `str`   |

### `get_text(classname: str, textname: str)`

- **Returns:** `Text`
- **Args:**
  - `classname: str`
  - `textname: str`

Retrieves the (translated) Text identified by `classname` and `textname`.

### `log(arg1: str)`

- **Returns:** `None`
- **Args:**
  - `arg1: str`

### `subst_args(text: Text, arg1: str = , arg2: str = , arg3: str = , arg4: str = , arg5: str = )`

- **Returns:** `str`
- **Args:**
  - `text: Text`
  - `arg1: str = `
  - `arg2: str = `
  - `arg3: str = `
  - `arg4: str = `
  - `arg5: str = `
