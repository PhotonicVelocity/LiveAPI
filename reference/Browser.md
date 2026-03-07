# Browser

## Browser

This class represents Live's content browser database. It provides access to the
hierarchical tree of browser items -- sounds, instruments, effects, plug-ins, samples,
clips, packs, and user content. Items are exposed as `BrowserItem` trees that can be
traversed and ultimately loaded into the Live Set. The Browser also supports hotswap
mode, item preview, and filtering.

Access the singleton via `Live.Application.get_application().browser` (from MIDI Remote
Scripts) or through the `live_app` path (from Max for Live / Control Surface scripts).

### Sources

- **Primary:** `Live/classes/Browser.py` (stub dump)
- **Secondary:** None (no MaxForLive browser docs found)
- **Probes:** `probe_browser10_limits.py`, `probe_browser11_pagination.py`, `probe_browser12_roots.py`,
  `probe_browser13_actions.py`, `probe_browser18_colors_relation.py`, `probe_browser19_colors_detail.py`

### Probe Notes

- **No `_live_ptr`:** BrowserItems are C++ Boost.Python objects but have no `_live_ptr` attribute. They cannot be
  tracked as handles in the Live object model. The bridge addresses them by content-root name + index path instead.
- **All 12 content roots work:** `sounds`, `drums`, `instruments`, `audio_effects`, `midi_effects`, `max_for_live`,
  `plugins`, `clips`, `samples`, `packs`, `current_project`, `user_library` all return valid BrowserItem trees with
  traversable children. Deep traversal tested to depth 3+.
- **C++ segfault threshold:** Accessing too many BrowserItem properties in a single main-thread call causes a C++
  segfault that bypasses Python exception handling. The threshold is approximately 60–65 items × 7 properties
  (~420–455 total property accesses). Reading `name` alone works for 300+ items. The bridge paginates at 50 items
  per page to stay safely below this limit.
- **`load_item()` works without hotswap:** Loading an instrument (e.g., Drift) onto the selected track works without
  entering hotswap mode. The item loads directly.
- **`preview_item()` / `stop_preview()` work:** Preview tested with a sample (`80s Beat 90 bpm.wav`).
  `stop_preview()` is safe to call even when nothing is playing.
- **`children` is iterable:** `BrowserItemVector` returned by `children` supports Python iteration via `enumerate()`
  and indexed access. Items are ephemeral C++ views — intermediate references must be kept alive to prevent dangling
  pointer crashes.

### Open Questions

- What are the named members of the `Relation` enum? Value `3` observed for all items when no hotswap is active
  (likely "unrelated"). Other values require manual hotswap activation in the Live UI, which is difficult to automate.

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

Browser does not have children in the traditional parent-child object model sense.
Instead, it exposes **content-root properties** that return `BrowserItem` trees (see
Properties below) and list-valued properties that return `BrowserItemVector` containers.

### Properties

| Property           | Get Returns          | Set Accepts | Listenable | Available Since | Summary                                                        |
| ------------------ | -------------------- | ----------- | ---------- | --------------- | -------------------------------------------------------------- |
| `audio_effects`    | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Audio Effects content.                       |
| `clips`            | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Clips content.                               |
| `colors`           | `list`               | —           | `no`       | `<11`           | List of browser items for configured colors.                   |
| `current_project`  | `BrowserItem`        | —           | `no`       | `<11`           | Root item for Current Project content.                         |
| `drums`            | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Drums content.                               |
| `filter_type`      | `int` (FilterType)   | `int`       | `yes`      | `<11`           | Current browser filter type (-1 to 7).                         |
| `hotswap_target`   | `BrowserItem`/`None` | —           | `yes`      | `<11`           | The current hotswap target (None when inactive).               |
| `instruments`      | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Instruments content.                         |
| `legacy_libraries` | `list`               | —           | `no`       | `<11`           | List of installed legacy library items (always empty in 12.x). |
| `max_for_live`     | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Max for Live content.                        |
| `midi_effects`     | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all MIDI Effects content.                        |
| `packs`            | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Packs content.                               |
| `plugins`          | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Plug-ins content.                            |
| `samples`          | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Samples content.                             |
| `sounds`           | `BrowserItem`        | —           | `no`       | `<11`           | Root item for all Sounds content.                              |
| `user_folders`     | `list`               | —           | `no`       | `<11`           | List of browser items for all user-configured folders.         |
| `user_library`     | `BrowserItem`        | —           | `no`       | `<11`           | Root item for User Library content.                            |

#### `audio_effects`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Audio Effects content. Traverse its `children` to browse
available audio effect devices, categories, and presets.

**Probe Results:** Returns a valid BrowserItem. Children are a mix of folders and loadable devices.

#### `clips`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Clips content. Provides access to clip files that can be
loaded into clip slots.

**Probe Results:** Returns a valid BrowserItem with loadable clip children.

#### `colors`

- **Get Returns:** `BrowserItemVector` (of `BrowserItem`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
A `BrowserItemVector` representing the **Collections** sidebar in Live's browser. Each entry is a color-tag category
(Favorites, Orange, Yellow, Green, Blue, Purple, Gray) that acts as a virtual folder — its `children` are the browser
items the user has tagged with that color via right-click. The return type is `BrowserItemVector` (not Python `list`),
same as `BrowserItem.children`.

**Probe Results:** Returns a `BrowserItemVector` of color-tag entries. Only colors that have at least one tagged item
appear in the list (unassigned colors are omitted). Each entry has a URI like `color:colors=N` where N is the color
index (1=Favorites, 2=Orange, 3=Yellow, 4=Green, 5=Blue, 6=Purple, 7=Gray; 0=Clear All Colors in the UI menu).
Traversing into a color entry (via `browser_children` with `path=[color_index]`) returns the tagged items, each with
URI `color:colors=N#FileId_XXXXX`. Tagged items are `is_loadable=True` and can appear under multiple colors. Cannot
be accessed via the handle system's `get` command (fails with `"Unsupported return type: BrowserItem"`). Accessible
via the `browser_children` bridge command with `root="colors"`.

**Limitations:** The API is read-only for Collections. There is no method to assign or remove color tags on browser
items, and no method to rename color categories (e.g., "Favorites"). Both operations are UI-only.

#### `current_project`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for the current Live project's content. Mirrors the "Current Project"
node in Live's browser sidebar, giving access to samples and other files saved within
the project folder.

**Probe Results:** Returns a valid BrowserItem. Contents depend on the open project.

#### `drums`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Drums content. Provides access to drum kits, drum hits, and
drum rack presets.

**Probe Results:** Returns a valid BrowserItem. Children are folder categories.

#### `filter_type`

- **Get Returns:** `int` (FilterType enum)
- **Set Accepts:** `int` (-1 through 7)
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
The current browser filter type. Controls which content categories are visible in the browser. The stub docstring is
a copy-paste error. The property is both readable and writable (despite the stub suggesting get-only).

**Note:** This is **not** the same as the hierarchical tag-based filters shown in the browser UI (Type, Character,
Genres, etc.). Those are per-item metadata filters that are not exposed in the API. `filter_type` is a coarse
content-root-level filter most useful on heterogeneous roots like `packs`, `user_library`, `current_project`, and
`user_folders`, where items of different types (instruments, effects, samples) are mixed together. When browsing a
type-specific root like `instruments` or `audio_effects`, the filter is redundant.

**Probe Results:** Returns an `int`. Default value is `-1`. Valid range is -1 through 7; values >= 8 or <= -2 raise
`"Invalid filter type"`. The filter affects which content roots return children:

| Value | Behavior            | Visible roots                                                                           |
| ----- | ------------------- | --------------------------------------------------------------------------------------- |
| -1    | No filter (default) | All                                                                                     |
| 0     | No filter           | All (same as -1)                                                                        |
| 1     | Instruments         | sounds, drums, instruments, samples                                                     |
| 2     | Audio Effects       | audio_effects, plugins                                                                  |
| 3     | MIDI Effects        | midi_effects                                                                            |
| 4     | Sounds              | sounds, instruments, samples (drums reduced)                                            |
| 5     | All except clips    | sounds, drums, instruments, audio_effects, midi_effects, max_for_live, plugins, samples |
| 6     | Samples             | samples (drums minimal)                                                                 |
| 7     | All                 | All (same as -1/0)                                                                      |

#### `hotswap_target`

- **Get Returns:** `Device` or `None` (see correction below)
- **Set Accepts:** `Device` handle or `None`
- **Listenable:** `yes`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed 12.3.5`

**Description:**
The current hotswap target. When the user enters hotswap mode in Live (the circular-arrow
button on a device or sample slot), this property points to the target being swapped.
The listener fires when the hotswap target changes.

**Probe Results:** Returns `None` when no hotswap is active (the common case). ~~The C++ signature for
`relation_to_hotswap_target` takes `NPythonBrowser::TPythonBrowserItem`, which originally suggested
`hotswap_target` returns a BrowserItem.~~ **Correction (probed 12.3.5, MS33):** During active hotswap,
`hotswap_target` returns the **Device** object being swapped, not a BrowserItem. Serializes normally via
the handle system — returned `{'oid': 'o_9', 'type': 'CompressorDevice'}` when hotswapping a Compressor.
The stub's `BrowserItem` return type annotation appears to be incorrect.

**Settable (probed 12.3.5, MS33):** Setting `hotswap_target` to a Device handle **activates hotswap mode
directly** — `browse_mode` becomes `True` without needing `select_device()` + `toggle_browse()`. Setting to
`None` **deactivates hotswap** — `browse_mode` returns to `False`. Setting to `None` when already inactive
is a safe no-op. Setting to a different Device while hotswap is already active **redirects** the hotswap
target seamlessly (stays in hotswap mode, target changes). This provides a simpler API than the
`select_device` + `toggle_browse` dance:

```
set(browser, "hotswap_target", device_handle)  # activate
browser_load(root, path)                       # swap preset
set(browser, "hotswap_target", None)           # deactivate
```

**Independence from selected/appointed device (probed 12.3.5, MS33):** `hotswap_target`, the selected device
(white outline in UI), and `appointed_device` (blue hand) are three independent states:

- Setting `hotswap_target` does **not** change `appointed_device` or the selected device.
- Calling `select_device()` (with or without appointment) while hotswap is active does **not** change
  `hotswap_target`.
- `toggle_browse()` copies the currently **selected** device (not `appointed_device`) into `hotswap_target`
  at activation time; after that they diverge independently.

This means `set(hotswap_target, device)` can target any device without disturbing the user's selection.

#### `instruments`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Instruments content. Traverse its `children` to browse
instrument devices, categories, and presets.

**Probe Results:** Returns a valid BrowserItem. Top-level children are individual instruments (Analog, Collision,
Drift, Electric, etc.) with `is_device=True`. Each instrument's children are presets with `is_loadable=True`.
Deep traversal to depth 2+ confirmed.

#### `legacy_libraries`

- **Get Returns:** `list` (empty)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
A list of browser items for installed legacy libraries. The stub explicitly notes that
this list is always empty because legacy library handling has been removed from Live.

**Probe Results:** Confirmed always returns `[]` (empty list) in Live 12.3.5.

#### `max_for_live`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Max for Live content. Provides access to Max for Live devices,
including audio effects, instruments, and MIDI effects built with Max.

**Probe Results:** Returns a valid BrowserItem with folder children.

#### `midi_effects`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all MIDI Effects content. Traverse its `children` to browse
available MIDI effect devices, categories, and presets.

**Probe Results:** Returns a valid BrowserItem. Children are MIDI effect devices and folders.

#### `packs`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Packs content. Provides access to installed Ableton packs
and their contents.

**Probe Results:** Returns a valid BrowserItem. Children are individual packs (all folders).

#### `plugins`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Plug-ins content. Provides access to third-party VST and AU
plug-ins installed on the system.

**Probe Results:** Returns a valid BrowserItem. Children are three top-level format folders:

- **Tree structure** — format-first: `AUv2/`, `VST/`, `VST3/`. AUv2 and VST3 have manufacturer subfolders
  (depth 3: format → manufacturer → plugin). VST2 is flat (depth 2) with manufacturer prefixed in the name
  (e.g. `"Voxengo SPAN"`).
- **API vs UI mismatch** — the API tree is format-first, but the Live browser UI shows manufacturer-first with
  duplicate entries per format. The UI flattens across formats; the API does not.
- **Leaf item metadata** — all loadable plugin items share: `is_device=False` (unlike native devices which have
  `is_device=True`), `is_loadable=True`, `is_folder=False`, `source=''` (native devices have `'Built-in'`).
- **URI format** — `query:Plugins#<format>:<manufacturer>:<name>` (e.g.
  `query:Plugins#VST3:Native Instruments:Raum`). VST2 uses `query:Plugins#VST:Local:<name>`.
- **Cross-root isolation** — plugins do **not** appear under `instruments` or `audio_effects`. The `plugins` root
  is completely separate from other content roots.
- **User-saved presets** appear as children of the plugin item: `.aupreset` (AU, `source='User Library'`),
  `.vstpreset` (VST3, `source='User Library'`). Preset children are `is_loadable=True, is_device=False,
is_folder=False`. Presets are **format-bound** — `.aupreset` only under the AUv2 entry, `.vstpreset` only under
  the VST3 entry. Not interchangeable across formats.
- **Loading** — `browser_load` works for all plugin formats. VST2/VST3 produce `class_name='PluginDevice'`;
  AU produces `class_name='AuPluginDevice'`. See PluginDevice.md for details.

#### `samples`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Samples content. Provides access to audio sample files
available in the browser.

**Probe Results:** Returns a valid BrowserItem. One of the largest collections — 3,535 top-level children in the
test environment. All children are loadable (non-folder) sample files.

#### `sounds`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for all Sounds content. Sounds are instrument presets organized by
musical category (Bass, Keys, Lead, Pad, etc.).

**Probe Results:** Returns a valid BrowserItem with ~16 top-level category folders. The Bass category has 304 children
(all loadable presets). Deep traversal to depth 3 confirmed (sounds > Bass > first child).

#### `user_folders`

- **Get Returns:** `list` (of `BrowserItem`)
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
A list of browser items representing all user-configured folders. These correspond to
the folders the user has added via Live's browser "Add Folder" feature.

**Probe Results:** Returns `[]` in the test environment (no user folders configured). Would return BrowserItems for
each user-added folder if configured.

#### `user_library`

- **Get Returns:** `BrowserItem`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Root browser item for User Library content. The User Library is the default location
where user presets, samples, and other personal content are stored.

**Probe Results:** Returns a valid BrowserItem. Contents depend on the user's library.

### Methods

| Signature                          | Returns    | Available Since | Summary                                                     |
| ---------------------------------- | ---------- | --------------- | ----------------------------------------------------------- |
| `load_item(item)`                  | `None`     | `<11`           | Load a browser item into the Live Set.                      |
| `preview_item(item)`               | `None`     | `<11`           | Preview (audition) a browser item.                          |
| `relation_to_hotswap_target(item)` | `Relation` | `<11`           | Return the relation between an item and the hotswap target. |
| `stop_preview()`                   | `None`     | `<11`           | Stop the currently playing preview.                         |

#### `load_item(item)`

- **Returns:** `None`
- **Args:**
  - `item: BrowserItem`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `Unknown`
- **Side Effects:** Loads the given browser item into the Live Set.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Loads the provided browser item into the Live Set. The item must be loadable
(`is_loadable=True`).

**Probe Results:** Does **not** require an active hotswap target. Loading an instrument (e.g., Drift via
`instruments[2]`) places it on the currently selected track. Tested successfully via bridge `browser_load` command.

**Targeting behavior (probed 12.3.5):** Always loads onto the currently selected track's top-level device chain.
Cannot target into rack chains — selecting a rack device, focusing a chain, or selecting a device inside a chain
via `View.select_device()` does not change where the device lands. Respects programmatically-set
`Song.View.selected_track`. Does not change `selected_track` as a side effect.

**Preset loading (probed 12.3.5):** Works for device presets nested in the browser tree (e.g.,
`instruments → Drift → Bass → 808 Drifter.adg`). Category folders have `is_loadable=False`; leaf preset files
(`.adg`, `.adv`) have `is_loadable=True`.

**Workaround for chain targeting:** Load onto track via `load_item`, then use `Song.move_device()` to relocate
the device into a chain. Works at any nesting depth.

**Hotswap interaction (probed 12.3.5, MS33):** When `browse_mode` is `True` (hotswap active), `load_item()`
behavior changes: instead of appending a new device to the selected track, it **swaps the preset in-place**
on the hotswap target device. Same-device presets keep the OID (parameters change); cross-device presets
within the same browser root replace the device entirely (new OID, count unchanged). Cross-root loading fails
(`Browser child index out of range`) because the browser filters items by the hotswap target's category.

#### `preview_item(item)`

- **Returns:** `None`
- **Args:**
  - `item: BrowserItem`
- **Raises/Errors:** `Unknown`
- **Undo-tracked:** `N/A` (preview is non-destructive)
- **Side Effects:** Begins audio preview of the given browser item.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Previews (auditions) the provided browser item. This plays a preview of the item
through Live's preview/cue output. Call `stop_preview()` to stop playback.

**Probe Results:** Tested with a sample (`samples[0]` = `80s Beat 90 bpm.wav`). Audio preview plays through
Live's cue output. Tested via bridge `browser_preview` command.

#### `relation_to_hotswap_target(item)`

- **Returns:** `Relation` (int)
- **Args:**
  - `item: BrowserItem`
- **Raises/Errors:** Path errors for cross-root items during hotswap (browser filters by category)
- **Undo-tracked:** `N/A` (read-only query)
- **Side Effects:** None.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed 12.3.5`

**Description:**
Returns the relationship between the given browser item and the current hotswap target.
The return value is a `Relation` enum (int). See `Relation` section below for known values.
Useful for determining whether a browser item is relevant to the current hotswap context.

**Probe Results:** The C++ signature is
`relation_to_hotswap_target(TPyHandle<ABrowserDelegate>, NPythonBrowser::TPythonBrowserItem)`. Cannot be called via
the handle system (BrowserItems have no `_live_ptr`). Accessible via the `browser_relation` bridge command.

**Values observed during active hotswap on a Compressor (probed 12.3.5, MS33):**

| Item queried             | Relation | Meaning                           |
| ------------------------ | -------- | --------------------------------- |
| Compressor device item   | `1`      | Same device as hotswap target     |
| Compressor preset [0]    | `2`      | Preset of the hotswap target      |
| Compressor preset [1]    | `2`      | Preset of the hotswap target      |
| EQ Eight device item     | `3`      | Unrelated (different device)      |
| EQ Eight category folder | `3`      | Unrelated                         |
| Any item (no hotswap)    | `3`      | Unrelated (default when inactive) |
| Cross-root items (Drift) | ERROR    | Browser filters by category       |
| Root-level paths (`[]`)  | ERROR    | Requires non-empty path           |

#### `stop_preview()`

- **Returns:** `None`
- **Args:** None
- **Raises/Errors:** None observed
- **Undo-tracked:** `N/A`
- **Side Effects:** Stops any currently playing browser preview.
- **Async visibility:** `Unknown`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Stops the currently playing preview that was started by `preview_item()`.

**Probe Results:** Safe to call even when nothing is being previewed (no error raised). Successfully stops a playing
preview. Tested via bridge `browser_stop_preview` command.

---

## BrowserItem

Represents a single item in the browser hierarchy. Browser items form a tree: each item
has a `name`, optional `children`, and metadata flags indicating whether it is a folder,
a device, or a loadable file. Browser items are returned by the Browser's content-root
properties (`sounds`, `instruments`, etc.) and can be traversed recursively via
`children`.

### Content Type Discrimination

Content roots like `drums` contain a heterogeneous mix of content types: samples (`.wav`, `.aif`), device group
presets (`.adg`), device presets (`.adv`), clips (`.alc`), and actual devices (e.g., Drum Rack, Drum Sampler).
The only type discrimination available is through the boolean flags:

- `is_device=True` — the item is a device (Drift, Drum Rack, etc.)
- `is_folder=True` — the item is a category folder
- `is_loadable=True` — the item can be loaded via `load_item()`

Samples, presets, clips, and rack presets are all `is_device=False, is_loadable=True`. There is no `type`,
`file_type`, or `extension` property. The only way to distinguish between them is by parsing the file extension
from `name` (e.g., `"Acid Bass.adv"`, `"Bell Chop.wav"`, `"Blue Thunder Kit.adg"`).

### Cross-Root Indexing

Content roots are virtual indexed views, not filesystem mirrors. The same item can appear in multiple roots — for
example, Drum Rack appears under both `drums` and `instruments`. Each root is a different view into Live's content
database.

Importantly, the **tree structure differs between roots** for the same device. In `instruments`, devices like
Drum Rack expand to show preset children (`.adg` files). In `drums`, the same device appears as a flat sibling
alongside all the presets — it has no children. This means `is_device=True` does not guarantee the item has
children, and a device's tree structure depends entirely on which root it was accessed through.

### Sources

- **Primary:** `Live/classes/Browser.py` (stub dump)
- **Probes:** `probe_browser10_limits.py`, `probe_browser11_pagination.py`, `probe_browser12_roots.py`,
  `probe_browser20_remaining.py`

### Probe Notes

- **No `_live_ptr`:** BrowserItems are C++ Boost.Python objects but do not have a `_live_ptr` attribute. They cannot
  be tracked as OID handles. The bridge uses content-root name + index path to address them instead.
- **All 7 properties confirmed:** `name` (str), `uri` (str), `source` (str), `is_folder` (bool), `is_device` (bool),
  `is_loadable` (bool), `is_selected` (bool) all return the expected types. Confirmed across all 12 content roots.
- **URI format:** Hierarchical identifier, e.g. `query:Sounds#Bass:FileId_15087`,
  `query:Instruments#Instrument%20Rack`. Not a filesystem path — it's Live's internal index key.
- **Source values observed:** `"Factory Packs/Core Library"` for built-in content, pack names for pack content.
- **Ephemeral C++ views:** BrowserItems are views into Live's C++ index. Intermediate references (parent vectors and
  items) must be kept alive during traversal to prevent dangling pointer crashes.
- **Segfault on bulk access:** Accessing all 7 properties on more than ~60–65 items in a single main-thread call
  causes a C++ segfault. Reading `name` alone works for 300+ items. The crash is in the Boost.Python layer and
  bypasses Python exception handling.

### Properties

| Property        | Get Returns           | Set Accepts | Listenable | Available Since | Summary                                                    |
| --------------- | --------------------- | ----------- | ---------- | --------------- | ---------------------------------------------------------- |
| `children`      | `BrowserItemVector`   | —           | `no`       | `<11`           | The child items of this browser item.                      |
| `is_device`     | `bool`                | —           | `no`       | `<11`           | Whether this item represents a device.                     |
| `is_folder`     | `bool`                | —           | `no`       | `<11`           | Whether this item represents a folder.                     |
| `is_loadable`   | `bool`                | —           | `no`       | `<11`           | Whether this item can be loaded via `Browser.load_item()`. |
| `is_selected`   | `bool`                | —           | `no`       | `<11`           | Whether this item is the selection or an ancestor of it.   |
| `iter_children` | `BrowserItemIterator` | —           | `no`       | `<11`           | An iterator over the child items.                          |
| `name`          | `str`                 | —           | `no`       | `<11`           | The display name of this browser item.                     |
| `source`        | `str`                 | —           | `no`       | `<11`           | Where the item comes from (e.g., pack, user library).      |
| `uri`           | `str`                 | —           | `no`       | `<11`           | A unique identifier URI for this browser item.             |

#### `children`

- **Get Returns:** `BrowserItemVector`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Read-only access to the child items of this browser item. Returns a `BrowserItemVector`
(a list-like container of `BrowserItem` objects). For leaf items (loadable files), this
will be empty. For folders and categories, this contains the nested items.

**Probe Results:** Supports Python iteration via `enumerate()`. Tested with collections up to 3,535 items (samples
root). The vector reference must be kept alive while accessing its items — if the vector is garbage collected,
subsequent item property accesses may segfault.

#### `is_device`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
`True` if this browser item represents a device (instrument, audio effect, MIDI effect,
or plug-in). `False` for folders, samples, clips, and other non-device items.

**Probe Results:** Confirmed `True` for instrument entries (e.g., Analog, Drift) and `False` for folder categories
and sample files.

#### `is_folder`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
`True` if this browser item represents a folder or category node in the hierarchy.
Folders have `children` that can be traversed further.

**Probe Results:** Confirmed `True` for category nodes (e.g., "Bass" under sounds) and `False` for leaf items.
Note: `is_folder` and `is_device` are not mutually exclusive — instrument root entries have
`is_folder=False, is_device=True` even though they may contain preset children.

#### `is_loadable`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
`True` if this item can be loaded into the Live Set via `Browser.load_item()`. Folders
and category nodes are typically not loadable; devices, presets, samples, and clips are.

**Probe Results:** Confirmed `True` for devices and presets, `False` for folder categories. Instruments root-level
entries (e.g., Drift) are `is_loadable=True` and can be loaded directly.

#### `is_selected`

- **Get Returns:** `bool`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
`True` if this item is the currently selected item in the browser, or if it is an
ancestor of the currently selected item. Useful for highlighting the active path in a
browser tree traversal.

**Probe Results:** Confirmed returns `bool`. Observed as `False` for most items during programmatic traversal.

#### `iter_children`

- **Get Returns:** `BrowserItemIterator`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
An iterable accessor over the child items of this browser item. Returns a `BrowserItemIterator`
rather than a `BrowserItemVector`. Supports standard Python `for` loop iteration.

**Probe Results:** Works. Returns the same items in the same order as `children`. The bridge uses `children` with
`enumerate()` for indexed access; `iter_children` could be used when only sequential iteration is needed.

#### `name`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
The canonical display name of this browser item as shown in Live's browser (e.g.,
`"Operator"`, `"Bass"`, `"Drums"`, `"My Preset.adv"`).

**Probe Results:** Confirmed returns `str`. The cheapest property to access — reading `name` alone works for 300+
items in a single call without triggering the C++ segfault threshold.

#### `source`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Indicates where this browser item originates from — for example, a Live Pack, the user
library, or the core library.

**Probe Results:** Observed values include `"Factory Packs/Core Library"` for built-in content. Pack-sourced content
shows the pack name. Empty string observed for some items.

#### `uri`

- **Get Returns:** `str`
- **Set Accepts:** —
- **Listenable:** `no`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
A unique identifier URI for this browser item. Can be used to uniquely reference a
specific item in the browser hierarchy across sessions.

**Probe Results:** Format is a hierarchical Live-internal identifier, e.g. `query:Sounds#Bass:FileId_15087`,
`query:Instruments#Instrument%20Rack`. Not a filesystem path. Uses URL-encoding for spaces. The scheme is
`query:` for content-root items and `color:` for color-tag items (e.g., `color:colors=1`).

---

## BrowserItemIterator

An iterator for traversing the children of a `BrowserItem`. Returned by
`BrowserItem.iter_children`. Follows Python's iterator protocol.

### Sources

- **Primary:** `Live/classes/Browser.py` (stub dump)
- **Probes:** None

### Probe Notes

None yet.

**Description:**
This class iterates over the children of a `BrowserItem`. The stub provides no methods
or properties beyond the constructor -- it likely implements the standard Python iterator
protocol (`__iter__` / `__next__`).

---

## BrowserItemVector

A read-only, list-like container returned by Live when providing collections of `BrowserItem`
objects. Returned by `BrowserItem.children` and by list-valued Browser properties
(`colors`, `legacy_libraries`, `user_folders`).

### Sources

- **Primary:** `Live/classes/Browser.py` (stub dump)
- **Probes:** `probe_browser10_limits.py`, `probe_browser11_pagination.py`, `probe_browser12_roots.py`,
  `probe_browser20_remaining.py`

### Probe Notes

- **Supports Python iteration:** `enumerate()` and `for` loops work. Indexed access via iteration confirmed (no
  direct `[]` indexing tested — the bridge uses sequential `enumerate()` to find target indices).
- **Reference lifetime matters:** The vector object must be kept alive while accessing its items. If the vector is
  garbage collected while items are still being accessed, subsequent property reads on those items may segfault.
  The bridge holds vector references in a `parent_refs` list during traversal.
- **Large collections observed:** `samples` root has 3,535 direct children. `sounds > Bass` has 304 children.
  Pagination is required for safe access when reading multiple properties per item.

### Methods

| Signature       | Returns | Available Since | Summary                                |
| --------------- | ------- | --------------- | -------------------------------------- |
| `append(item)`  | `None`  | `N/A`           | Append a browser item to the vector.   |
| `extend(items)` | `None`  | `N/A`           | Extend the vector with multiple items. |

#### `append(item)`

- **Returns:** `None`
- **Args:**
  - `item: object`
- **Raises/Errors:** `"Cannot modify read only container."`
- **Undo-tracked:** `N/A`
- **Side Effects:** None — raises immediately.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Present in the stub but non-functional. Raises `"Cannot modify read only container."` when called.
`BrowserItemVector` containers returned by Live are read-only.

#### `extend(items)`

- **Returns:** `None`
- **Args:**
  - `items: object`
- **Raises/Errors:** `"Cannot modify read only container."`
- **Undo-tracked:** `N/A`
- **Side Effects:** None — raises immediately.
- **Async visibility:** `N/A`
- **Available Since:** `<11`
- **Sources:** `stub`, `probe`
- **Probe Status:** `probed`

**Description:**
Present in the stub but non-functional. Raises `"Cannot modify read only container."` when called.
`BrowserItemVector` containers returned by Live are read-only.

---

## FilterType

An integer enum representing the browser filter type. Used by `Browser.filter_type`.

### Sources

- **Primary:** `Live/classes/Browser.py` (stub dump)
- **Probes:** `probe_browser15_enums.py`, `probe_browser17_filter_matrix.py`

### Probe Notes

- **Valid range:** -1 through 7. Values >= 8 or <= -2 raise `"Invalid filter type"`.
- **Named members unknown:** The stub provides no named values, and the C++ enum names are not exposed to Python.
  The values below are inferred from their effect on content root visibility.

### Members (inferred from behavior)

| Value | Inferred Name     | Effect                                                                                   |
| ----- | ----------------- | ---------------------------------------------------------------------------------------- |
| -1    | Disabled / None   | No filter applied (default)                                                              |
| 0     | All               | Same as -1                                                                               |
| 1     | Instruments       | Shows sounds, drums, instruments, samples; hides audio/midi effects, m4l, plugins, clips |
| 2     | Audio Effects     | Shows audio_effects, plugins; hides everything else                                      |
| 3     | MIDI Effects      | Shows midi_effects only                                                                  |
| 4     | Sounds            | Shows sounds, instruments, samples; drums reduced to 1                                   |
| 5     | Devices + Samples | Shows everything except clips                                                            |
| 6     | Samples           | Shows samples; drums reduced to 1                                                        |
| 7     | All               | Same as -1/0                                                                             |

---

## Relation

An integer enum representing the relationship between a `BrowserItem` and the current
hotswap target. Returned by `Browser.relation_to_hotswap_target()`.

### Sources

- **Primary:** `Live/classes/Browser.py` (stub dump)
- **Probes:** `probe_browser15_enums.py`, `probe_browser18_colors_relation.py`

### Known Values (probed 12.3.5, MS33)

| Value | Name (inferred)  | Observed when                                            |
| ----- | ---------------- | -------------------------------------------------------- |
| `1`   | Same device      | Querying the same device type as the hotswap target      |
| `2`   | Preset of target | Querying a preset that belongs to the hotswap target     |
| `3`   | Unrelated        | All items when no hotswap active; different device types |

Value `0` was not observed. There may be a value for "ancestor" or "descendant" in the category tree,
but only same-root items can be queried during hotswap (cross-root items cause path errors due to browser
filtering).

### Probe Notes

- **Accessible via bridge:** The `browser_relation` bridge command resolves `root` + `path` to a BrowserItem and calls
  `relation_to_hotswap_target()`. Cannot be called via the handle system because BrowserItems have no `_live_ptr`.
- **Cross-root errors:** During active hotswap, querying items from a different browser root (e.g., instruments
  while hotswapping an audio effect) fails with `NotFound: Browser child index out of range` because the
  browser filters items by the hotswap target's category.

### Open Questions

- What is value `0`? Possibly "equal" (exact same BrowserItem as the target)?
- The stub shows only a `from_bytes` method — the actual enum member names are unknown.
