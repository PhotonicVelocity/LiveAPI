# Stub Audit Fixes

## 1. Parameterize bare `tuple` properties in stub generator

Properties like `macros_mapped`, `cc_value_map`, `vel_map`, `value_pair_map`, `slices` return bare `tuple`
instead of `tuple[bool, ...]` etc. The `element_repr` is already on these property nodes — the generator
just needs to use it.

In `generate_stubs.py`, near the Vector parameterization block (~line 391), add a similar check for
`probed_type == "tuple"` properties with `element_repr`. Resolve the element repr to a type name and
emit `tuple[T, ...]`.

## 2. Add `LomObject` as unresolved return type for LLM resolution

Functions like `create_take_lane()`, `insert_device()`, `insert_chain()` return `LomObject` where a more
specific type is known.

In `extract_unresolved.py` `_check_function`, add `"LomObject"` to the set of unresolved return/arg types
(currently only `"object"` and `"tuple"`). The existing LLM flow will then resolve them.

Affected functions:
- `Track.create_take_lane() -> LomObject` (should be `TakeLane`)
- `Track.insert_device() -> LomObject` (should be `Device`)
- `Chain.insert_device() -> LomObject` (should be `Device`)
- `RackDevice.insert_chain() -> LomObject` (should be `Chain`)
- `Conversions.move_devices_on_track_to_new_drum_rack_pad() -> LomObject`

## 3. Convert PascalCase parameter names to snake_case in parse

Parameters like `CaptureMode`, `DeviceName`, `DeviceIndex`, `Quantized`, `ShouldConsumeEvent`, `Index`
come from C++ signature parsing and were never lowercased.

In `parse_apicapture_results.py`, during signature parsing, detect PascalCase arg names and convert to
snake_case. E.g. `CaptureMode` → `capture_mode`, `DeviceName` → `device_name`.

Note: `CaptureMode: CaptureMode` even shadows its type name.

Affected params (from audit):
- Song: CaptureMode, Destination, Index (x2), Quantized
- Track: DeviceName, DeviceIndex, Quantized
- Chain: DeviceName, DeviceIndex
- RackDevice: Index
- MidiMap: ShouldConsumeEvent (x2)

## 4. Fix FilterType.disabled enum value to -1

In `Browser/__init__.pyi`, `FilterType.disabled = 1` and `instrument_hotswap = 1` share the same value.
The raw capture data should have `disabled = -1`. Fix wherever the enum values are parsed/stored.

Check `LiveTree.raw.json` or `LiveTree.parsed.json` for the `Browser.FilterType` enum and verify the
raw value. Fix at the source (likely in the raw capture or parse step).

## 5. Wrap Vector `extend` arg type in `Iterable[...]`

Concrete vector classes (e.g., `MidiNoteVector`, `ClipDataVector`) have `extend` methods whose arg is typed
as the bare element type (`T`) instead of `Iterable[T]`. For example, `MidiNoteVector.extend` currently
accepts `MidiNoteSpecification` but should accept `Iterable[MidiNoteSpecification]`.

Needs investigation to determine where the fix belongs — could be in stub generation (`generate_stubs.py`),
in the resolved tree (`apply_refinements.py`), or in the LLM resolution output. The generic `Base.Vector`
class has the same issue (resolved as `Any` instead of `Iterable[Any]`).
