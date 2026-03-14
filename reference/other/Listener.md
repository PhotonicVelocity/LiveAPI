# Listener (Module)

## ListenerHandle (Class)

> `Live.Listener.ListenerHandle`

This class represents a Python listener when connected to a Live property.

### Properties

| Property                          | Type       | Supports |
| --------------------------------- | ---------- | -------- |
| [`listener_func`](#listener_func) | `Callable` | `get`    |
| [`listener_self`](#listener_self) | `Any`      | `get`    |
| [`name`](#name)                   | `str`      | `get`    |

#### `listener_func`

- **Type:** `Callable`
- **Settable:** `no`
- **Listenable:** `no`

Returns the original function

#### `listener_self`

- **Type:** `Any`
- **Settable:** `no`
- **Listenable:** `no`

Returns the weak reference to original self, if it was a bound method

#### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Prints the name of the property that this listener is connected to

### Methods

| Method                        | Returns |
| ----------------------------- | ------- |
| [`disconnect()`](#disconnect) | `None`  |

#### `disconnect()`

- **Returns:** `None`

Disconnects the listener from its property

## ListenerVector (Class)

> `Live.Listener.ListenerVector`

A read only container for accessing a list of listeners.

### Methods

| Method                                                           | Returns |
| ---------------------------------------------------------------- | ------- |
| [`append(value: ListenerHandle)`](#appendvalue-listenerhandle)   | `None`  |
| [`extend(values: ListenerHandle)`](#extendvalues-listenerhandle) | `None`  |

#### `append(value: ListenerHandle)`

- **Returns:** `None`
- **Args:**
  - `value: ListenerHandle`

#### `extend(values: ListenerHandle)`

- **Returns:** `None`
- **Args:**
  - `values: ListenerHandle`
