# Stub Audit Fixes

## 1. Parameterize bare `tuple` properties in stub generator

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
