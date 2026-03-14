# Browser

> `Live.Browser.Browser`

This class represents Live's content browser database. It provides access to the hierarchical tree of browser
items -- sounds, instruments, effects, plug-ins, samples, clips, packs, and user content. Items are exposed as
`BrowserItem` trees that can be traversed and ultimately loaded into the Live Set. The Browser also supports
hotswap mode, item preview, and filtering.

Access the singleton via `Live.Application.get_application().browser` (from MIDI Remote Scripts) or through the
`live_app` path (from Max for Live / Control Surface scripts).

??? note "Raw probe notes (temporary)"

    - **No `_live_ptr`:** BrowserItems are C++ Boost.Python objects but have no `_live_ptr` attribute. They cannot
      be tracked as handles in the Live object model. The bridge addresses them by content-root name + index path
      instead.
    - **All 12 content roots work:** `sounds`, `drums`, `instruments`, `audio_effects`, `midi_effects`,
      `max_for_live`, `plugins`, `clips`, `samples`, `packs`, `current_project`, `user_library` all return valid
      BrowserItem trees with traversable children. Deep traversal tested to depth 3+.
    - **C++ segfault threshold:** Accessing too many BrowserItem properties in a single main-thread call causes a
      C++ segfault that bypasses Python exception handling. The threshold is approximately 60–65 items x 7
      properties (~420–455 total property accesses). Reading `name` alone works for 300+ items. The bridge
      paginates at 50 items per page to stay safely below this limit.
    - **`load_item()` works without hotswap:** Loading an instrument (e.g., Drift) onto the selected track works
      without entering hotswap mode. The item loads directly.
    - **`preview_item()` / `stop_preview()` work:** Preview tested with a sample (`80s Beat 90 bpm.wav`).
      `stop_preview()` is safe to call even when nothing is playing.
    - **`children` is iterable:** `BrowserItemVector` returned by `children` supports Python iteration via
      `enumerate()` and indexed access. Items are ephemeral C++ views — intermediate references must be kept alive
      to prevent dangling pointer crashes.

### Open Questions

- What are the named members of the `Relation` enum? Value `3` observed for all items when no hotswap is active
  (likely "unrelated"). Other values require manual hotswap activation in the Live UI, which is difficult to
  automate.

### Content Roots vs UI Sidebar

The API exposes 12 single-item content roots and 3 list-valued roots (see Properties below). These do not cover
every entry in Live's browser sidebar. As of Live 12.3.5, the following UI sidebar entries have **no corresponding
API property**:

- **Library:** All, Modulators, Grooves, Tunings, Templates
- **Places:** Splice, Cloud, Push

"All" is likely a UI-only aggregate view. The others may be newer Live 12 additions or third-party integrations
that Ableton has not exposed in the Python API. The set of available roots is determined by the `Browser` class
stub and could change in future Live versions.

Additionally, the UI has a rich **tag-based filtering system** that is not exposed in the API. When a content root
is selected, the UI shows filterable tags organized by category (e.g., Type, Character, Genres, instrument/drum
sub-categories). Items also have visible tags at the bottom of the browser (e.g., "Tags: Pad" or "Tags: Analog,
Bongo, Electronic, One Shot"). The API's `filter_type` property is a coarse root-level filter (-1 to 7) that
controls which content roots are visible — it does not interact with the per-item tag system. There is no `tags`
property on `BrowserItem`.

### Children

Browser does not have children in the traditional parent-child object model sense. Instead, it exposes
**content-root properties** that return `BrowserItem` trees (see Properties below) and list-valued properties
that return `BrowserItemVector` containers.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `audio_effects` | `BrowserItem` | `no` | `no` | Root item for all Audio Effects content. |
| `clips` | `BrowserItem` | `no` | `no` | Root item for all Clips content. |
| `colors` | `list` | `no` | `no` | List of browser items for configured colors. |
| `current_project` | `BrowserItem` | `no` | `no` | Root item for Current Project content. |
| `drums` | `BrowserItem` | `no` | `no` | Root item for all Drums content. |
| `filter_type` | `int (FilterType)` | `yes` | `yes` | Current browser filter type (-1 to 7). |
| `hotswap_target` | `BrowserItem/None` | `yes` | `yes` | The current hotswap target (None when inactive). |
| `instruments` | `BrowserItem` | `no` | `no` | Root item for all Instruments content. |
| `legacy_libraries` | `list` | `no` | `no` | List of installed legacy library items (always empty in 12.x). |
| `max_for_live` | `BrowserItem` | `no` | `no` | Root item for all Max for Live content. |
| `midi_effects` | `BrowserItem` | `no` | `no` | Root item for all MIDI Effects content. |
| `packs` | `BrowserItem` | `no` | `no` | Root item for all Packs content. |
| `plugins` | `BrowserItem` | `no` | `no` | Root item for all Plug-ins content. |
| `samples` | `BrowserItem` | `no` | `no` | Root item for all Samples content. |
| `sounds` | `BrowserItem` | `no` | `no` | Root item for all Sounds content. |
| `user_folders` | `list` | `no` | `no` | List of browser items for all user-configured folders. |
| `user_library` | `BrowserItem` | `no` | `no` | Root item for User Library content. |

#### `audio_effects`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Audio Effects content. Traverse its `children` to browse available audio effect
devices, categories, and presets.

#### `clips`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Clips content. Provides access to clip files that can be loaded into clip slots.

#### `colors`

- **Type:** `BrowserItemVector` (of `BrowserItem`)
- **Listenable:** `no`
- **Since:** `<11`

A `BrowserItemVector` representing the **Collections** sidebar in Live's browser. Each entry is a color-tag
category (Favorites, Orange, Yellow, Green, Blue, Purple, Gray) that acts as a virtual folder — its `children`
are the browser items the user has tagged with that color via right-click.

- **Limitations:** The API is read-only for Collections. There is no method to assign or remove color tags on
  browser items, and no method to rename color categories.

#### `current_project`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for the current Live project's content. Mirrors the "Current Project" node in Live's browser
sidebar, giving access to samples and other files saved within the project folder.

#### `drums`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Drums content. Provides access to drum kits, drum hits, and drum rack presets.

#### `filter_type`

- **Type:** `int` (FilterType enum)
- **Listenable:** `yes`
- **Since:** `<11`

The current browser filter type. Controls which content categories are visible in the browser. Both readable and
writable. Default value is `-1`. Valid range is -1 through 7; values >= 8 or <= -2 raise `"Invalid filter type"`.

**Note:** This is **not** the same as the hierarchical tag-based filters shown in the browser UI (Type, Character,
Genres, etc.). Those are per-item metadata filters that are not exposed in the API. `filter_type` is a coarse
content-root-level filter most useful on heterogeneous roots like `packs`, `user_library`, `current_project`, and
`user_folders`.

| Value | Behavior | Visible roots |
| --- | --- | --- |
| -1 | No filter (default) | All |
| 0 | No filter | All (same as -1) |
| 1 | Instruments | sounds, drums, instruments, samples |
| 2 | Audio Effects | audio_effects, plugins |
| 3 | MIDI Effects | midi_effects |
| 4 | Sounds | sounds, instruments, samples (drums reduced) |
| 5 | All except clips | sounds, drums, instruments, audio_effects, midi_effects, max_for_live, plugins, samples |
| 6 | Samples | samples (drums minimal) |
| 7 | All | All (same as -1/0) |

#### `hotswap_target`

- **Type:** `Device` or `None`
- **Listenable:** `yes`
- **Since:** `<11`

The current hotswap target. When the user enters hotswap mode in Live (the circular-arrow button on a device or
sample slot), this property points to the target being swapped. Returns `None` when no hotswap is active.

During active hotswap, `hotswap_target` returns the **Device** object being swapped, not a BrowserItem. The
stub's `BrowserItem` return type annotation appears to be incorrect.

**Settable:** Setting `hotswap_target` to a Device handle activates hotswap mode directly — `browse_mode` becomes
`True` without needing `select_device()` + `toggle_browse()`. Setting to `None` deactivates hotswap. Setting to a
different Device while hotswap is already active redirects the hotswap target seamlessly.

```
set(browser, "hotswap_target", device_handle)  # activate
browser_load(root, path)                       # swap preset
set(browser, "hotswap_target", None)           # deactivate
```

- **Quirks:** `hotswap_target`, the selected device (white outline in UI), and `appointed_device` (blue hand) are
  three independent states. Setting `hotswap_target` does not change `appointed_device` or the selected device.

#### `instruments`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Instruments content. Traverse its `children` to browse instrument devices, categories,
and presets.

#### `legacy_libraries`

- **Type:** `list` (empty)
- **Listenable:** `no`
- **Since:** `<11`

A list of browser items for installed legacy libraries. Always empty because legacy library handling has been
removed from Live.

#### `max_for_live`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Max for Live content. Provides access to Max for Live devices, including audio effects,
instruments, and MIDI effects built with Max.

#### `midi_effects`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all MIDI Effects content. Traverse its `children` to browse available MIDI effect devices,
categories, and presets.

#### `packs`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Packs content. Provides access to installed Ableton packs and their contents.

#### `plugins`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Plug-ins content. Provides access to third-party VST and AU plug-ins installed on
the system.

- **Quirks:** The API tree is format-first (`AUv2/`, `VST/`, `VST3/`), but the Live browser UI shows
  manufacturer-first with duplicate entries per format. Plugins do not appear under `instruments` or
  `audio_effects` — the `plugins` root is completely separate.

#### `samples`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Samples content. Provides access to audio sample files available in the browser.

#### `sounds`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for all Sounds content. Sounds are instrument presets organized by musical category (Bass,
Keys, Lead, Pad, etc.).

#### `user_folders`

- **Type:** `list` (of `BrowserItem`)
- **Listenable:** `no`
- **Since:** `<11`

A list of browser items representing all user-configured folders. These correspond to the folders the user has
added via Live's browser "Add Folder" feature.

#### `user_library`

- **Type:** `BrowserItem`
- **Listenable:** `no`
- **Since:** `<11`

Root browser item for User Library content. The User Library is the default location where user presets, samples,
and other personal content are stored.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `load_item(item)` | `None` | Load a browser item into the Live Set. |
| `preview_item(item)` | `None` | Preview (audition) a browser item. |
| `relation_to_hotswap_target(item)` | `Relation` | Return the relation between an item and the hotswap target. |
| `stop_preview()` | `None` | Stop the currently playing preview. |

#### `load_item(item)`

- **Returns:** `None`
- **Args:**
  - `item: BrowserItem`
- **Since:** `<11`

Loads the provided browser item into the Live Set. The item must be loadable (`is_loadable=True`). Does not
require an active hotswap target — loading an instrument places it on the currently selected track.

- **Quirks:** Always loads onto the currently selected track's top-level device chain. Cannot target into rack
  chains. Use `Song.move_device()` to relocate after loading.
- **Limitations:** When `browse_mode` is `True` (hotswap active), `load_item()` swaps the preset in-place on
  the hotswap target device instead of appending a new device. Cross-root loading fails during hotswap.

#### `preview_item(item)`

- **Returns:** `None`
- **Args:**
  - `item: BrowserItem`
- **Since:** `<11`

Previews (auditions) the provided browser item. This plays a preview of the item through Live's preview/cue
output. Call `stop_preview()` to stop playback.

#### `relation_to_hotswap_target(item)`

- **Returns:** `Relation` (int)
- **Args:**
  - `item: BrowserItem`
- **Since:** `<11`

Returns the relationship between the given browser item and the current hotswap target. The return value is a
`Relation` enum (int). Useful for determining whether a browser item is relevant to the current hotswap context.

| Item queried | Relation | Meaning |
| --- | --- | --- |
| Same device as hotswap target | `1` | Same device |
| Preset of the hotswap target | `2` | Preset of target |
| Different device / no hotswap | `3` | Unrelated |

#### `stop_preview()`

- **Returns:** `None`
- **Args:** None
- **Since:** `<11`

Stops the currently playing preview that was started by `preview_item()`. Safe to call even when nothing is
being previewed.

---

## BrowserItem

> `Live.Browser.BrowserItem`

Represents a single item in the browser hierarchy. Browser items form a tree: each item has a `name`, optional
`children`, and metadata flags indicating whether it is a folder, a device, or a loadable file. Browser items
are returned by the Browser's content-root properties (`sounds`, `instruments`, etc.) and can be traversed
recursively via `children`.

### Content Type Discrimination

Content roots like `drums` contain a heterogeneous mix of content types: samples (`.wav`, `.aif`), device group
presets (`.adg`), device presets (`.adv`), clips (`.alc`), and actual devices (e.g., Drum Rack, Drum Sampler).
The only type discrimination available is through the boolean flags:

- `is_device=True` — the item is a device (Drift, Drum Rack, etc.)
- `is_folder=True` — the item is a category folder
- `is_loadable=True` — the item can be loaded via `load_item()`

Samples, presets, clips, and rack presets are all `is_device=False, is_loadable=True`. There is no `type`,
`file_type`, or `extension` property. The only way to distinguish between them is by parsing the file extension
from `name`.

### Cross-Root Indexing

Content roots are virtual indexed views, not filesystem mirrors. The same item can appear in multiple roots — for
example, Drum Rack appears under both `drums` and `instruments`. Each root is a different view into Live's content
database.

Importantly, the **tree structure differs between roots** for the same device. In `instruments`, devices like Drum
Rack expand to show preset children (`.adg` files). In `drums`, the same device appears as a flat sibling
alongside all the presets — it has no children. This means `is_device=True` does not guarantee the item has
children, and a device's tree structure depends entirely on which root it was accessed through.

### Properties

| Property | Type | Settable | Listenable | Summary |
| --- | --- | --- | --- | --- |
| `children` | `BrowserItemVector` | `no` | `no` | The child items of this browser item. |
| `is_device` | `bool` | `no` | `no` | Whether this item represents a device. |
| `is_folder` | `bool` | `no` | `no` | Whether this item represents a folder. |
| `is_loadable` | `bool` | `no` | `no` | Whether this item can be loaded via `Browser.load_item()`. |
| `is_selected` | `bool` | `no` | `no` | Whether this item is the selection or an ancestor of it. |
| `iter_children` | `BrowserItemIterator` | `no` | `no` | An iterator over the child items. |
| `name` | `str` | `no` | `no` | The display name of this browser item. |
| `source` | `str` | `no` | `no` | Where the item comes from (e.g., pack, user library). |
| `uri` | `str` | `no` | `no` | A unique identifier URI for this browser item. |

#### `children`

- **Type:** `BrowserItemVector`
- **Listenable:** `no`
- **Since:** `<11`

Read-only access to the child items of this browser item. Returns a `BrowserItemVector` (a list-like container
of `BrowserItem` objects). For leaf items (loadable files), this will be empty.

- **Quirks:** The vector reference must be kept alive while accessing its items — if the vector is garbage
  collected, subsequent item property accesses may segfault.

#### `is_device`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this browser item represents a device (instrument, audio effect, MIDI effect, or plug-in). `False` for
folders, samples, clips, and other non-device items.

#### `is_folder`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this browser item represents a folder or category node in the hierarchy. Folders have `children` that
can be traversed further.

- **Quirks:** `is_folder` and `is_device` are not mutually exclusive — instrument root entries have
  `is_folder=False, is_device=True` even though they may contain preset children.

#### `is_loadable`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this item can be loaded into the Live Set via `Browser.load_item()`. Folders and category nodes are
typically not loadable; devices, presets, samples, and clips are.

#### `is_selected`

- **Type:** `bool`
- **Listenable:** `no`
- **Since:** `<11`

`True` if this item is the currently selected item in the browser, or if it is an ancestor of the currently
selected item.

#### `iter_children`

- **Type:** `BrowserItemIterator`
- **Listenable:** `no`
- **Since:** `<11`

An iterable accessor over the child items of this browser item. Returns a `BrowserItemIterator` rather than a
`BrowserItemVector`. Supports standard Python `for` loop iteration.

#### `name`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

The canonical display name of this browser item as shown in Live's browser (e.g., `"Operator"`, `"Bass"`,
`"Drums"`, `"My Preset.adv"`).

#### `source`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

Indicates where this browser item originates from — for example, a Live Pack, the user library, or the core
library. Observed values include `"Factory Packs/Core Library"` for built-in content.

#### `uri`

- **Type:** `str`
- **Listenable:** `no`
- **Since:** `<11`

A unique identifier URI for this browser item. Format is a hierarchical Live-internal identifier, e.g.
`query:Sounds#Bass:FileId_15087`, `query:Instruments#Instrument%20Rack`. Not a filesystem path.

---

## BrowserItemIterator

> `Live.Browser.BrowserItemIterator`

An iterator for traversing the children of a `BrowserItem`. Returned by `BrowserItem.iter_children`. Follows
Python's iterator protocol (`__iter__` / `__next__`).

---

## BrowserItemVector

> `Live.Browser.BrowserItemVector`

A read-only, list-like container returned by Live when providing collections of `BrowserItem` objects. Returned
by `BrowserItem.children` and by list-valued Browser properties (`colors`, `legacy_libraries`, `user_folders`).

- **Quirks:** Supports Python iteration via `enumerate()` and `for` loops. The vector object must be kept alive
  while accessing its items — if garbage collected, subsequent property reads on items may segfault.

### Methods

| Method | Returns | Summary |
| --- | --- | --- |
| `append(item)` | `None` | Append a browser item to the vector. |
| `extend(items)` | `None` | Extend the vector with multiple items. |

#### `append(item)`

- **Returns:** `None`
- **Args:**
  - `item: object`
- **Raises:** `"Cannot modify read only container."`
- **Since:** `<11`

Present in the stub but non-functional. Raises `"Cannot modify read only container."` when called.

#### `extend(items)`

- **Returns:** `None`
- **Args:**
  - `items: object`
- **Raises:** `"Cannot modify read only container."`
- **Since:** `<11`

Present in the stub but non-functional. Raises `"Cannot modify read only container."` when called.

---

## FilterType

> `Live.Browser.FilterType`

An integer enum representing the browser filter type. Used by `Browser.filter_type`.

### Members (inferred from behavior)

| Value | Inferred Name | Effect |
| --- | --- | --- |
| -1 | Disabled / None | No filter applied (default) |
| 0 | All | Same as -1 |
| 1 | Instruments | Shows sounds, drums, instruments, samples; hides audio/midi effects, m4l, plugins, clips |
| 2 | Audio Effects | Shows audio_effects, plugins; hides everything else |
| 3 | MIDI Effects | Shows midi_effects only |
| 4 | Sounds | Shows sounds, instruments, samples; drums reduced to 1 |
| 5 | Devices + Samples | Shows everything except clips |
| 6 | Samples | Shows samples; drums reduced to 1 |
| 7 | All | Same as -1/0 |

---

## Relation

> `Live.Browser.Relation`

An integer enum representing the relationship between a `BrowserItem` and the current hotswap target. Returned
by `Browser.relation_to_hotswap_target()`.

### Known Values (probed 12.3.5)

| Value | Name (inferred) | Observed when |
| --- | --- | --- |
| `1` | Same device | Querying the same device type as the hotswap target |
| `2` | Preset of target | Querying a preset that belongs to the hotswap target |
| `3` | Unrelated | All items when no hotswap active; different device types |

### Open Questions

- What is value `0`? Possibly "equal" (exact same BrowserItem as the target)?
- The stub shows only a `from_bytes` method — the actual enum member names are unknown.
