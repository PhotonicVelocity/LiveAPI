# Stub Audit Fixes

## ~~1. Parameterize bare `tuple` properties in stub generator~~

Properties like `macros_mapped`, `cc_value_map`, `vel_map`, `value_pair_map`, `slices` return bare `tuple`
instead of `tuple[bool, ...]` etc. The `element_repr` is already on these property nodes — the generator
just needs to use it.

In `generate_stubs.py`, near the Vector parameterization block (~line 391), add a similar check for
`probed_type == "tuple"` properties with `element_repr`. Resolve the element repr to a type name and
emit `tuple[T, ...]`.

## ~~2. Add `LomObject` as unresolved return type for LLM resolution~~ ✓

Done — added `"LomObject"` to unresolved types in `extract_unresolved.py`. Resolved via LLM pipeline.

## ~~3. Convert PascalCase parameter names to snake_case in parse~~ ✓

Done — added `_pascal_to_snake()` in `parse_apicapture_results.py` `_resolve_arg()`. All PascalCase params
(`CaptureMode`, `DeviceName`, `DeviceIndex`, `Quantized`, `ShouldConsumeEvent`, `ShouldAppointDevice`,
`Index`, `Destination`) now convert to snake_case during parsing.

## ~~4. Fix FilterType.disabled enum value to -1~~ ✓

Done — `_ENUM_VALUE_RE` in `parse_apicapture_results.py` used `\d+` which dropped the negative sign.
Changed to `-?\d+` so negative enum values are captured correctly.

## ~~5. Wrap Vector `extend` arg type in `Iterable[...]`~~ ✓

Done — handled in `parse_apicapture_results.py` during signature resolution and property merge.

## ~~6. Add missing `Iterable` import to stub generator~~ ✓

`Iterable` is used in `extend()` signatures across 9 `__init__.pyi` files and several `Clip.pyi` methods,
but never imported. This is a hard type-checker error.

Fix in `generate_stubs.py` — add `Iterable` to the typing imports in the header templates (both `_HEADER`
and `_VECTOR_HEADER`), or conditionally when `Iterable` appears in any annotation.

## ~~7. Resolve `Vector[LomObject]` to concrete element types~~ ✓

7 properties are typed `Vector[LomObject]` where specific types are known:

- `Chain.devices` → `Vector[Device]` (docstring: "all available Devices")
- `RackDevice.chains` → `Vector[Chain]`
- `RackDevice.return_chains` → `Vector[Chain]`
- `DrumPad.chains` → `Vector[Chain]` or `Vector[DrumChain]`
- `ChainMixerDevice.sends` → `Vector[DeviceParameter]`
- `MaxDevice.midi_inputs` → `Vector[DeviceIO]`
- `MaxDevice.midi_outputs` → `Vector[DeviceIO]`

Root cause: the probe saw `LomObject` as the element type because the generic `Base.Vector` holds
heterogeneous objects. The `element_repr` on the property needs to be more specific — likely needs
LLM resolution or probe improvements to capture the concrete element type.

## ~~8. Fix `-> None` on nullable properties (should be `T | None`)~~ ✓

~15 properties return `None` instead of `T | None`. These are nullable references where the probe
happened to see `None` at capture time. Examples:

- `Song.appointed_device` → `Device | None`
- `Clip.groove` → `Groove | None`
- `Browser.hotswap_target` → `BrowserItem | None`
- `Song.View.detail_clip` → `Clip | None`
- `Song.View.selected_chain` → `Chain | None`
- `Song.View.selected_parameter` → `DeviceParameter | None`
- `Scene.color_index` → `int | None`
- `RackDevice.View.selected_chain` → `Chain | None`

Root cause: `PropertyProbe` records whatever type it sees at probe time. If the property was `None`
during probing, `probed_type` is `NoneType`. Fix likely belongs in the probe (re-probe on non-None
instances) or as a post-processing step that recognizes nullable patterns.

## ~~9. Parameterize bare `list` returns~~ ✓

Done — added `"list"` to unresolved types in `extract_unresolved.py`. LLM resolved function args/returns.
Generator now parameterizes `list` properties using `element_repr` (same pattern as tuple).

## ~~10. Classes are missing inheritance in stubs~~ ✓

Done — added `_ancestor_base()` in `generate_stubs.py` that reads the `ancestors` list from the tree.
Uses the first ancestor (direct parent), skipping `Boost.Python.instance`. Qualifies with module name
when the parent class name matches the current class (e.g. `Device.View` not self-referential `View`).

## ~~11. Enums and type nodes missing inheritance in stubs~~ ✓

Done — added `bases` capture for enums in `CaptureModule.py` (same pattern as regular classes).
Updated `resolve_inheritance` in `parse_apicapture_results.py` to process `enum` and `type` nodes
(not just `class`). Updated `_ancestor_base()` in `generate_stubs.py` to map `Boost.Python.enum` → `int`.
Removed hardcoded `Exception` from `_render_type_node` — now uses ancestor data.
Result: enums render as `class FilterType(int):`, `LimitationError` renders as `class LimitationError(Exception):`.

## 12. `BrowserItemIterator` gets inheritance from `Vector[BrowserItem]`