# Browser (Module)

## Browser (Class)

> `Live.Browser.Browser`

This class represents the live browser data base.

**Live Object:** `yes`

**Access via:**

- `Application.browser`

### Properties

| Property                                | Type                | Supports             |
| --------------------------------------- | ------------------- | -------------------- |
| [`audio_effects`](#audio_effects)       | `BrowserItem`       | `get`                |
| [`clips`](#clips)                       | `BrowserItem`       | `get`                |
| [`colors`](#colors)                     | `BrowserItemVector` | `get`                |
| [`current_project`](#current_project)   | `BrowserItem`       | `get`                |
| [`drums`](#drums)                       | `BrowserItem`       | `get`                |
| [`filter_type`](#filter_type)           | `int`               | `get`/`set`/`listen` |
| [`hotswap_target`](#hotswap_target)     | `Device \| None`    | `get`/`set`/`listen` |
| [`instruments`](#instruments)           | `BrowserItem`       | `get`                |
| [`legacy_libraries`](#legacy_libraries) | `BrowserItemVector` | `get`                |
| [`max_for_live`](#max_for_live)         | `BrowserItem`       | `get`                |
| [`midi_effects`](#midi_effects)         | `BrowserItem`       | `get`                |
| [`packs`](#packs)                       | `BrowserItem`       | `get`                |
| [`plugins`](#plugins)                   | `BrowserItem`       | `get`                |
| [`samples`](#samples)                   | `BrowserItem`       | `get`                |
| [`sounds`](#sounds)                     | `BrowserItem`       | `get`                |
| [`user_folders`](#user_folders)         | `BrowserItemVector` | `get`                |
| [`user_library`](#user_library)         | `BrowserItem`       | `get`                |

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

- **Type:** `BrowserItemVector`
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

- **Type:** `Device | None`
- **Settable:** `yes`
- **Listenable:** `yes`

Bang triggered when the hotswap target has changed.

#### `instruments`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the Instruments content.

#### `legacy_libraries`

- **Type:** `BrowserItemVector`
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

- **Type:** `BrowserItemVector`
- **Settable:** `no`
- **Listenable:** `no`

Returns a list of browser items containing all the user folders.

#### `user_library`

- **Type:** `BrowserItem`
- **Settable:** `no`
- **Listenable:** `no`

Returns a browser item with access to all the User Library content.

### Methods

| Method                                                                        | Returns    |
| ----------------------------------------------------------------------------- | ---------- |
| [`load_item()`](#load_itemitem-browseritem)                                   | `None`     |
| [`preview_item()`](#preview_itemitem-browseritem)                             | `None`     |
| [`relation_to_hotswap_target()`](#relation_to_hotswap_targetitem-browseritem) | `Relation` |
| [`stop_preview()`](#stop_preview)                                             | `None`     |

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

### FilterType

> `Live.Browser.FilterType`

| Value | Name                   |
| ----- | ---------------------- |
| ``    | `disabled`             |
| `0`   | `hotswap_off`          |
| `1`   | `instrument_hotswap`   |
| `2`   | `audio_effect_hotswap` |
| `3`   | `midi_effect_hotswap`  |
| `4`   | `drum_pad_hotswap`     |
| `5`   | `midi_track_devices`   |
| `6`   | `samples`              |
| `7`   | `count`                |

### Relation

> `Live.Browser.Relation`

| Value | Name         |
| ----- | ------------ |
| `0`   | `ancestor`   |
| `1`   | `equal`      |
| `2`   | `descendant` |
| `3`   | `none`       |

## BrowserItem (Type)

> `Live.Browser.BrowserItem`

This class represents an item of the browser hierarchy.

### Properties

| Property                          | Type                  | Supports |
| --------------------------------- | --------------------- | -------- |
| [`children`](#children)           | `BrowserItemVector`   | `get`    |
| [`is_device`](#is_device)         | `bool`                | `get`    |
| [`is_folder`](#is_folder)         | `bool`                | `get`    |
| [`is_loadable`](#is_loadable)     | `bool`                | `get`    |
| [`is_selected`](#is_selected)     | `bool`                | `get`    |
| [`iter_children`](#iter_children) | `BrowserItemIterator` | `get`    |
| [`name`](#name)                   | `str`                 | `get`    |
| [`source`](#source)               | `str`                 | `get`    |
| [`uri`](#uri)                     | `str`                 | `get`    |

#### `children`

- **Type:** `BrowserItemVector`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the descendants of this browser item.

#### `is_device`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Indicates if the browser item represents a device.

#### `is_folder`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

Indicates if the browser item represents folder.

#### `is_loadable`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

True if item can be loaded via the Browser's 'load_item' method.

#### `is_selected`

- **Type:** `bool`
- **Settable:** `no`
- **Listenable:** `no`

True if the item is ancestor of or the actual selection.

#### `iter_children`

- **Type:** `BrowserItemIterator`
- **Settable:** `no`
- **Listenable:** `no`

Const iterable access to the descendants of this browser item.

#### `name`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the canonical display name of this browser item.

#### `source`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

Specifies where does item come from -- i.e. Live pack, user library...

#### `uri`

- **Type:** `str`
- **Settable:** `no`
- **Listenable:** `no`

The uri describes a unique identifier for a browser item.

## BrowserItemIterator (Type)

> `Live.Browser.BrowserItemIterator`

This class iterates over children of another BrowserItem.

## BrowserItemVector (Type)

> `Live.Browser.BrowserItemVector`

A container for returning browser items from Live.

### Methods

| Method                                          | Returns |
| ----------------------------------------------- | ------- |
| [`append()`](#appendvalue-browseritem)          | `None`  |
| [`extend()`](#extendvalues-iterablebrowseritem) | `None`  |

#### `append(value: BrowserItem)`

- **Returns:** `None`
- **Args:**
  - `value: BrowserItem`

#### `extend(values: Iterable[BrowserItem])`

- **Returns:** `None`
- **Args:**
  - `values: Iterable[BrowserItem]`
