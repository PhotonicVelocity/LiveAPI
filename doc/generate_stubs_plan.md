# Stub Generator from LiveTree.parsed.json

## Context

The current stub generator (`tools/other/StubGenerator.py`) reads the old flat `Live.json` + `probe_results.json`
format. The new v2 parse pipeline produces `LiveTree.parsed.json` — a hierarchical tree where type resolution,
signature parsing, and probe merging are already done. We need a new generator that walks the tree and emits `.pyi`
stubs, letting the tree structure drive the output layout naturally.

## New File

**`tools/parse/generate_stubs.py`** — single file.

```bash
python tools/parse/generate_stubs.py 12.3.6
python tools/parse/generate_stubs.py 12.3.6 --input path/to/parsed.json --output path/to/Live
```

Reads `build/{version}/LiveTree.parsed.json`, writes to `build/{version}/Live/`.

## Output File Layout

The tree is: `Live` (root module) → 43 namespace modules → classes/enums/functions.

Each namespace module becomes a package directory. The `repr` field on each class/enum node encodes its canonical path
(e.g. `<class 'Song.Song'>` means `Live.Song.Song`), so the file layout mirrors this directly:

```
Live/
├── __init__.py              # from . import Application, Base, ... (all 43 modules)
├── py.typed                 # PEP 561 marker
├── Application/
│   ├── __init__.py          # module-level funcs, helper classes/enums, re-export main class
│   └── Application.pyi      # main class (same name as module)
├── Song/
│   ├── __init__.py          # CaptureMode, Quantization, etc., re-export Song
│   └── Song.pyi             # Song class with nested View
├── Base/
│   └── __init__.py          # all classes (no Base.Base exists, so no split)
├── Conversions/
│   └── __init__.py          # enums + module-level functions only (no classes named Conversions)
...
```

**Split rule** (derived from tree): A module gets a separate `.pyi` file when it has a direct child class node whose
`name` matches the module name (i.e., `repr` is `<class '{Module}.{Module}'>`). That class and its entire subtree go
into `{Module}.pyi`. Everything else stays in `__init__.py`.

## Rendering by Node Type

The tree has 7 node types. Each renders differently:

### `module` (44 nodes)

Not rendered directly — module nodes become directories. Their children are iterated.

### `class` (103 nodes)

```python
class Song:
    """This class represents a Live set."""

    class View:
        """View aspects of a Live set."""
        ...
```

- Ancestors available but NOT emitted in the class signature (no usable base in stubs, and `LomObject` /
  `Boost.Python.instance` are internal). Exception: `type` nodes (see below).
- Docstring from `raw_doc` if present.
- Children rendered recursively at indent+1.
- Empty body (only ref children or no children) gets `...`.

#### Constructable classes

14 classes have `"constructable": true` and an `init_doc` field containing a Boost.Python `__init__` signature string.
These classes can be instantiated by user code — the stubs must expose an `__init__` method so type checkers accept
constructor calls.

The `init_doc` is a raw Boost.Python docstring (same format as function `raw_doc`). The generator parses it with a
lightweight regex to extract `(type)name` argument pairs and optional `= default` values, then emits:

```python
class MidiNoteSpecification:
    """An object specifying the data for creating a MIDI note."""

    def __init__(
        self,
        pitch: int,
        start_time: float,
        duration: float,
        velocity: float = 100.0,
        mute: bool = False,
        probability: float = 1.0,
        velocity_deviation: float = 0.0,
        release_velocity: float = 64.0,
    ) -> None: ...
```

Rules:

- Skip the first `(object)arg1` parameter (it's the implicit `self`).
- Map Boost types to Python types using `_TYPE_MAP` (same as property types).
- Preserve defaults as literals.
- If `init_doc` has only `(object)arg1` (no real parameters), emit `def __init__(self) -> None: ...`.
- If `init_doc` is missing or unparseable, skip `__init__` (class won't appear constructable in stubs).

### `enum` (43 nodes)

```python
class GridQuantization:
    g_thirtysecond: int = 0
    g_sixteenth: int = 1
```

Members from `node["members"]`, sorted by value. Each: `{name}: int = {value}`.
Note: some enums are nested inside classes (e.g. `MixerDevice.crossfade_assignments`, `Application.View.NavDirection`).

### `function` (1747 nodes)

**As a method (parent is a class):**

```python
def capture_and_insert_scene(self, CaptureMode: CaptureMode | int = 0) -> None:
    """Capture currently playing clips."""
    ...
```

**As a module-level function (parent is a module):**

```python
def get_application() -> Application:
    """Returns the application instance."""
    ...
```

Key details:

- `self` arg (already identified by parser, `name == "self"`) emitted bare with no type annotation.
- Other args: `{name}: {type}` from `arg["type"]`, with `= {default}` when present.
- Enum defaults resolved to int via lookup table built during indexing.
- When default references an enum, widen type: `{EnumClass} | int`.
- Return type from `node["returns"]["type"]`.
- Docstring from `description` (clean) or `raw_doc` (fallback).

### `property` (890 nodes)

```python
@property
def tempo(self) -> float:
    """The tempo of the song."""
    ...

@tempo.setter
def tempo(self, value: float) -> None: ...
```

Type from `probed_type`, mapped through `_TYPE_MAP` (see below). Setter when `settable` is true.
If `probed_type` is missing/null, omit return annotation.

### `str` (6 nodes — in Application.Variants)

```python
BETA: str = "Beta"
```

Value from `node["value"]` (comes as `"'Beta'"` — strip outer quotes, re-emit).

### `type` (1 node — Base.LimitationError)

```python
class LimitationError(Exception): ...
```

Rendered as an exception class. The `names`/`values` fields are `"None"` strings and ignored.

### Ref nodes (`"ref": true`, 384 nodes)

**Skipped entirely.** Inherited members — the canonical definition lives on the declaring class.

## Type Resolution

### Property types via \_TYPE_MAP

```python
_TYPE_MAP = {
    "bool": "bool", "int": "int", "float": "float", "str": "str", "NoneType": "None",
    "Vector": "tuple",
    "StringVector": "tuple[str, ...]", "IntVector": "tuple[int, ...]",
    "IntU64Vector": "tuple[int, ...]", "FloatVector": "tuple[float, ...]",
    "BrowserItemVector": "tuple[BrowserItem, ...]",
    "RoutingChannelVector": "tuple[RoutingChannel, ...]",
    "RoutingTypeVector": "tuple[RoutingType, ...]",
    "ObjectVector": "tuple[object, ...]",
    "UnavailableFeatureVector": "tuple[UnavailableFeature, ...]",
    "ATimeableValueVector": "tuple[DeviceParameter, ...]",
    "WarpMarkerVector": "tuple[WarpMarker, ...]",
    "MidiNoteVector": "tuple[MidiNote, ...]",
    "EnvelopeEventVector": "tuple[EnvelopeEvent, ...]",
    "ControlDescriptionVector": "tuple[ControlDescription, ...]",
    "BrowserItemIterator": "BrowserItemIterator",
    "RoutingChannelLayout": "RoutingChannelLayout",
    "list": "list", "tuple": "tuple", "object": "object", "dict": "dict",
}
```

Any `probed_type` not in this map is a class name — passes through as-is (e.g., `"Browser"`, `"Song"`).

### Function arg/return types

Already resolved by the parse pipeline. The `type` field on args and `returns.type` contain Python type names
directly. The generator just passes them through.

### Cross-module TYPE_CHECKING imports

After rendering a file body into a buffer:

1. Regex-scan for capitalized identifiers (`[A-Z][A-Za-z0-9]+`).
2. Filter to names present in `_class_to_module` (built during indexing from every class/enum node's `name` and
   the module it lives in).
3. Remove names defined locally in this file.
4. Remove stdlib names: `None`, `Callable`, `TYPE_CHECKING`.
5. Group by source module:
   - **Same module, from class file:** `from . import {Name}` (sibling defined in `__init__.py`)
   - **Same module, from init file:** skip (locally defined)
   - **Cross-module:** `from Live.{Module} import {Name}`

The `_class_to_module` index is built by walking the tree once before generation. For each non-ref class/enum/type
node, map `node["name"] → module_name`. The `repr` field confirms the mapping (e.g.,
`<class 'Browser.BrowserItem'>` → module `Browser`, name `BrowserItem`).

**View ambiguity:** `View` appears in 8 modules as a nested class. Since it's always nested, any `View` type reference
in a file refers to the local `View` (sibling within the same class file or defined locally). The regex scanner may
pick it up, but it will be in `defined_names` and filtered out.

## Generator Structure

```python
class StubGenerator:
    def __init__(self, tree: dict, output_dir: str)

    # --- Phase 1: Index the tree ---
    _build_indexes()
    _index_node(node, module_name, parent_class)
    # Builds:
    #   _class_to_module: dict[str, str]       name → module
    #   _module_classes: dict[str, set[str]]    module → {names}
    #   _enum_lookup: dict[str, int]            "Song.CaptureMode.all" → 0

    # --- Phase 2: Generate ---
    generate()
    _write_module(module_node)
    _write_class_file(module_name, main_class_node)
    _write_init_file(module_name, nodes, import_main)
    _write_top_init(module_names)

    # --- Renderers (write to StringIO) ---
    _render_class(node, buf, indent)
    _render_init(node, buf, indent)          # parse init_doc for constructable classes
    _render_enum(node, buf, indent)
    _render_function(node, buf, indent, is_method)
    _render_property(node, buf, indent)
    _render_str_const(node, buf, indent)
    _render_type_node(node, buf, indent)
    _render_children(children, buf, indent, is_class_body)

    # --- Type helpers ---
    _resolve_probed_type(probed_type)
    _format_arg(arg)
    _resolve_default(default)
    _build_type_checking_block(body, module_name, defined_names)
```

## Concrete Output Examples

### Song/**init**.py

```python
from __future__ import annotations
from typing import TYPE_CHECKING, Callable
from .Song import Song


class CaptureDestination:
    auto: int = 0
    session: int = 1
    arrangement: int = 2


class CaptureMode:
    all: int = 0
    ...


class Quantization:
    q_no_q: int = 0
    ...


class RecordingQuantization:
    rec_q_no_q: int = 0
    ...


class SessionRecordStatus:
    off: int = 0
    ...


__all__ = ["Song", "CaptureDestination", "CaptureMode", "Quantization", "RecordingQuantization", "SessionRecordStatus"]
```

### Song/Song.pyi

```python
from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from . import CaptureMode, Quantization, RecordingQuantization
    from Live.Clip import Clip
    from Live.Scene import Scene
    from Live.Track import Track


class Song:
    """This class represents a Live set."""

    class View:
        """This class represents the view aspects of a Live set."""

        @property
        def detail_clip(self) -> Clip: ...

        @property
        def selected_track(self) -> Track: ...

        def select_device(self, arg2: Device) -> None:
            """Select the given device."""
            ...

    @property
    def tempo(self) -> float:
        """Get/set the song's overall tempo."""
        ...

    @tempo.setter
    def tempo(self, value: float) -> None: ...

    def capture_and_insert_scene(self, CaptureMode: CaptureMode | int = 0) -> None:
        """Capture currently playing clips and insert them as a new scene."""
        ...


__all__ = ["Song"]
```

### Base/**init**.py (no split — no Base.Base class)

```python
from __future__ import annotations
from typing import TYPE_CHECKING, Callable


class LimitationError(Exception): ...


class FloatVector:
    def append(self, arg2: float) -> None: ...
    def extend(self, arg2: float) -> None: ...


class IntVector:
    def append(self, arg2: int) -> None: ...
    def extend(self, arg2: int) -> None: ...


...


def log(arg1: str) -> None: ...


__all__ = ["LimitationError", "FloatVector", "IntVector", ..., "log"]
```

## Key Files

- **Create:** `tools/parse/generate_stubs.py`
- **Reference:** `tools/other/StubGenerator.py` (v1 generator — TYPE_MAP values, import block pattern)
- **Input:** `build/12.3.6/LiveTree.parsed.json`
- **Reference:** `tools/parse/Notes.md` (manual type refinements — future follow-up, not for this PR)

## Verification

1. `python tools/parse/generate_stubs.py 12.3.6`
2. `find build/12.3.6/Live -type f | sort` — confirm 43 module dirs, correct file split
3. Spot-check syntax: `python -m py_compile build/12.3.6/Live/Song/Song.pyi` (and a few others)
4. Check Song/Song.pyi has: nested View class, proper TYPE_CHECKING imports, enum default resolution
5. Check Base/**init**.py has: LimitationError(Exception), vector classes, module-level functions
6. Check Application/Application.pyi has: nested View with nested NavDirection enum
7. Check Clip/MidiNoteSpecification or Clip/**init**.py has: `__init__` with parsed args for MidiNoteSpecification
8. Check Base/**init**.py has: `Timer.__init__` with callback, interval, repeat, start args
