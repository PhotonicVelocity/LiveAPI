# Browser (Module)

## Browser (Class)

> `Live.Browser.Browser`

This class represents the live browser data base.

**Live Object:** `yes`

**Access via:**

- `Application.browser`

### Properties

| Property           | Type                           | Settable | Listenable | Description                                                                |
| ------------------ | ------------------------------ | -------- | ---------- | -------------------------------------------------------------------------- |
| `audio_effects`    | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Audio Effects content.       |
| `clips`            | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Clips content.               |
| `colors`           | `tuple[BrowserItem, Ellipsis]` | `no`     | `no`       | Returns a list of browser items containing the configured colors.          |
| `current_project`  | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Current Project content.     |
| `drums`            | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Drums content.               |
| `filter_type`      | `int`                          | `yes`    | `yes`      | Bang triggered when the hotswap target has changed.                        |
| `hotswap_target`   | `None`                         | `yes`    | `yes`      | Bang triggered when the hotswap target has changed.                        |
| `instruments`      | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Instruments content.         |
| `legacy_libraries` | `tuple[BrowserItem, Ellipsis]` | `no`     | `no`       | Returns a list of browser items containing the installed legacy libraries. |
| `max_for_live`     | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Max For Live content.        |
| `midi_effects`     | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Midi Effects content.        |
| `packs`            | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Packs content.               |
| `plugins`          | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Plugins content.             |
| `samples`          | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Samples content.             |
| `sounds`           | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the Sounds content.              |
| `user_folders`     | `tuple[BrowserItem, Ellipsis]` | `no`     | `no`       | Returns a list of browser items containing all the user folders.           |
| `user_library`     | `BrowserItem`                  | `no`     | `no`       | Returns a browser item with access to all the User Library content.        |

#### `audio_effects`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Audio Effects content.

#### `clips`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Clips content.

#### `colors`

- **Type:** `tuple[BrowserItem, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Returns a list of browser items containing the configured colors.

#### `current_project`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Current Project content.

#### `drums`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Drums content.

#### `filter_type`

- **Type:** `int`
- **Settable:** `yes`
- **Listenable:** `yes`

Bang triggered when the hotswap target has changed.

#### `hotswap_target`

- **Type:** `None`
- **Settable:** `yes`
- **Listenable:** `yes`

Bang triggered when the hotswap target has changed.

#### `instruments`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Instruments content.

#### `legacy_libraries`

- **Type:** `tuple[BrowserItem, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Returns a list of browser items containing the installed legacy libraries. The list is always empty as legacy library handling has been removed.

#### `max_for_live`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Max For Live content.

#### `midi_effects`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Midi Effects content.

#### `packs`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Packs content.

#### `plugins`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Plugins content.

#### `samples`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Samples content.

#### `sounds`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Sounds content.

#### `user_folders`

- **Type:** `tuple[BrowserItem, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Returns a list of browser items containing all the user folders.

#### `user_library`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the User Library content.

### Methods

| Method                                          | Returns    | Description                                                                      |
| ----------------------------------------------- | ---------- | -------------------------------------------------------------------------------- |
| `load_item(item: BrowserItem)`                  | `None`     | Loads the provided browser item.                                                 |
| `preview_item(item: BrowserItem)`               | `None`     | Previews the provided browser item.                                              |
| `relation_to_hotswap_target(item: BrowserItem)` | `Relation` | Returns the relation between the given browser item and the current hotswap t... |
| `stop_preview()`                                | `None`     | Stop the current preview.                                                        |

#### `load_item(item: BrowserItem)`

- **Returns:** `None`
- **Args:**
  - `item: BrowserItem`

Loads the provided browser item.

#### `preview_item(item: BrowserItem)`

- **Returns:** `None`
- **Args:**
  - `item: BrowserItem`

Previews the provided browser item.

#### `relation_to_hotswap_target(item: BrowserItem)`

- **Returns:** `Relation`
- **Args:**
  - `item: BrowserItem`

Returns the relation between the given browser item and the current hotswap target

#### `stop_preview()`

- **Returns:** `None`

Stop the current preview.

## Enums

### `FilterType`

| Value | Name                   |
| ----- | ---------------------- |
| `0`   | `hotswap_off`          |
| `1`   | `disabled`             |
| `1`   | `instrument_hotswap`   |
| `2`   | `audio_effect_hotswap` |
| `3`   | `midi_effect_hotswap`  |
| `4`   | `drum_pad_hotswap`     |
| `5`   | `midi_track_devices`   |
| `6`   | `samples`              |
| `7`   | `count`                |

### `Relation`

| Value | Name         |
| ----- | ------------ |
| `0`   | `ancestor`   |
| `1`   | `equal`      |
| `2`   | `descendant` |
| `3`   | `none`       |

## Types

### BrowserItem

> `Live.Browser.BrowserItem`

This class represents an item of the browser hierarchy.

#### Properties

| Property        | Type                           | Settable | Listenable | Description                                                      |
| --------------- | ------------------------------ | -------- | ---------- | ---------------------------------------------------------------- |
| `children`      | `tuple[BrowserItem, Ellipsis]` | `no`     | `no`       | Const access to the descendants of this browser item.            |
| `is_device`     | `bool`                         | `no`     | `no`       | Indicates if the browser item represents a device.               |
| `is_folder`     | `bool`                         | `no`     | `no`       | Indicates if the browser item represents folder.                 |
| `is_loadable`   | `bool`                         | `no`     | `no`       | True if item can be loaded via the Browser's 'load_item' method. |
| `is_selected`   | `bool`                         | `no`     | `no`       | True if the item is ancestor of or the actual selection.         |
| `iter_children` | `BrowserItemIterator`          | `no`     | `no`       | Const iterable access to the descendants of this browser item.   |
| `name`          | `str`                          | `no`     | `no`       | Const access to the canonical display name of this browser item. |
| `source`        | `str`                          | `no`     | `no`       | Specifies where does item come from -- i.e.                      |
| `uri`           | `str`                          | `no`     | `no`       | The uri describes a unique identifier for a browser item.        |

##### `children`

- **Type:** `tuple[BrowserItem, Ellipsis]`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the descendants of this browser item.

##### `is_device`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Indicates if the browser item represents a device.

##### `is_folder`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Indicates if the browser item represents folder.

##### `is_loadable`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

True if item can be loaded via the Browser's 'load_item' method.

##### `is_selected`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

True if the item is ancestor of or the actual selection.

##### `iter_children`

- **Type:** `BrowserItemIterator`
- **Settable:** `no`
- **Listenable:** `no`

Const iterable access to the descendants of this browser item.

##### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the canonical display name of this browser item.

##### `source`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Specifies where does item come from -- i.e. Live pack, user library...

##### `uri`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

The uri describes a unique identifier for a browser item.

### BrowserItemIterator

> `Live.Browser.BrowserItemIterator`

This class iterates over children of another BrowserItem.

### BrowserItemVector

> `Live.Browser.BrowserItemVector`

A container for returning browser items from Live.

#### Methods

| Method                        | Returns | Description |
| ----------------------------- | ------- | ----------- |
| `append(value: BrowserItem)`  | `None`  |             |
| `extend(values: BrowserItem)` | `None`  |             |

##### `append(value: BrowserItem)`

- **Returns:** `None`
- **Args:**
  - `value: BrowserItem`

##### `extend(values: BrowserItem)`

- **Returns:** `None`
- **Args:**
  - `values: BrowserItem`
