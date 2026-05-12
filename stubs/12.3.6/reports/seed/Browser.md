---
module: Browser
---

## Classes

### Browser

```yaml
kind: class
path: Live.Browser.Browser
ancestors:
- Live.LomObject.LomObject
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents the live browser data base.
```

#### Properties

##### audio_effects

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Audio Effects content.
```

##### clips

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Clips content.
```

##### colors

```yaml
kind: property
type: Live.Browser.BrowserItemVector
settable: false
raw_doc: Returns a list of browser items containing the configured colors.
```

##### current_project

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Current Project content.
```

##### drums

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Drums content.
```

##### filter_type

```yaml
kind: property
type: int
settable: true
listenable: true
raw_doc: Bang triggered when the hotswap target has changed.
```

##### hotswap_target

```yaml
kind: property
type: None
settable: true
listenable: true
raw_doc: Bang triggered when the hotswap target has changed.
```

##### instruments

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Instruments content.
```

##### legacy_libraries

```yaml
kind: property
type: Live.Browser.BrowserItemVector
settable: false
raw_doc: Returns a list of browser items containing the installed legacy libraries. The list is always empty as legacy library
  handling has been removed.
```

##### max_for_live

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Max For Live content.
```

##### midi_effects

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Midi Effects content.
```

##### packs

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Packs content.
```

##### plugins

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Plugins content.
```

##### samples

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Samples content.
```

##### sounds

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the Sounds content.
```

##### user_folders

```yaml
kind: property
type: Live.Browser.BrowserItemVector
settable: false
raw_doc: Returns a list of browser items containing all the user folders.
```

##### user_library

```yaml
kind: property
type: Live.Browser.BrowserItem
settable: false
raw_doc: Returns a browser item with access to all the User Library content.
```

##### full_refresh

```yaml
kind: property
listenable: true
```

#### Methods

##### load_item

```yaml
kind: method
signature: 'load_item( (Browser)arg1, (BrowserItem)arg2) -> None :'
cpp_signature: void load_item(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
args:
- name: arg2
  type: Live.Browser.BrowserItem
returns:
  type: None
raw_doc: Loads the provided browser item.
```

##### preview_item

```yaml
kind: method
signature: 'preview_item( (Browser)arg1, (BrowserItem)arg2) -> None :'
cpp_signature: void preview_item(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
args:
- name: arg2
  type: Live.Browser.BrowserItem
returns:
  type: None
raw_doc: Previews the provided browser item.
```

##### relation_to_hotswap_target

```yaml
kind: method
signature: 'relation_to_hotswap_target( (Browser)arg1, (BrowserItem)arg2) -> Relation :'
cpp_signature: ableton::live_library::Relation relation_to_hotswap_target(TPyHandle<ABrowserDelegate>,NPythonBrowser::TPythonBrowserItem)
args:
- name: arg2
  type: Live.Browser.BrowserItem
returns:
  type: Live.Browser.Relation
raw_doc: Returns the relation between the given browser item and the current hotswap target
```

##### stop_preview

```yaml
kind: method
signature: 'stop_preview( (Browser)arg1) -> None :'
cpp_signature: void stop_preview(TPyHandle<ABrowserDelegate>)
returns:
  type: None
raw_doc: Stop the current preview.
```

### BrowserItem

```yaml
kind: class
path: Live.Browser.BrowserItem
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
raw_doc: This class represents an item of the browser hierarchy.
```

#### Properties

##### children

```yaml
kind: property
type: Live.Browser.BrowserItemVector
settable: false
raw_doc: Const access to the descendants of this browser item.
```

##### is_device

```yaml
kind: property
type: bool
settable: false
raw_doc: Indicates if the browser item represents a device.
```

##### is_folder

```yaml
kind: property
type: bool
settable: false
raw_doc: Indicates if the browser item represents folder.
```

##### is_loadable

```yaml
kind: property
type: bool
settable: false
raw_doc: True if item can be loaded via the Browser's 'load_item' method.
```

##### is_selected

```yaml
kind: property
type: bool
settable: false
raw_doc: True if the item is ancestor of or the actual selection.
```

##### iter_children

```yaml
kind: property
type: Live.Browser.BrowserItemIterator
settable: false
raw_doc: Const iterable access to the descendants of this browser item.
```

##### name

```yaml
kind: property
type: str
settable: false
raw_doc: Const access to the canonical display name of this browser item.
```

##### source

```yaml
kind: property
type: str
settable: false
raw_doc: Specifies where does item come from -- i.e. Live pack, user library...
```

##### uri

```yaml
kind: property
type: str
settable: false
raw_doc: The uri describes a unique identifier for a browser item.
```

### BrowserItemIterator

```yaml
kind: class
path: Live.Browser.BrowserItemIterator
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
raw_doc: This class iterates over children of another BrowserItem.
```

### BrowserItemVector

```yaml
kind: class
path: Live.Browser.BrowserItemVector
ancestors:
- Boost.Python.instance
init_doc: |-
  Raises an exception
  This class cannot be instantiated from Python
constructable: false
iterable: true
container: true
element_type: Live.Browser.BrowserItem
raw_doc: A container for returning browser items from Live.
```

## Enums

### FilterType

```yaml
kind: enum
members:
  disabled: -1
  hotswap_off: 0
  instrument_hotswap: 1
  audio_effect_hotswap: 2
  midi_effect_hotswap: 3
  drum_pad_hotswap: 4
  midi_track_devices: 5
  samples: 6
  count: 7
```

### Relation

```yaml
kind: enum
members:
  ancestor: 0
  equal: 1
  descendant: 2
  none: 3
```
