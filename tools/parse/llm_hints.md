# Manual Hints for LLM Resolution

These are facts about the Live API that cannot be inferred from the type skeleton, decompiled code,
or MaxForLive docs. Use them to guide your resolutions.

## Domain facts

- Song and Application are root objects that have no parent. Their `canonical_parent` is always None.
- Browser.hotswap_target points to the Device that will be hotswapped.
- The bools in midi map pitchbending methods indicate whether takeover is needed to prevent value jumps.
- The generics `Base.Vector` and `Base.ObjectVector` are used for `LomObject` collections and python `object` 
  collections respectively.
- MIDI data values (CC, note, pitchbend) are always `int`. Tuples of MIDI values are `tuple[int, ...]`.

## Naming guidance

- methods that create audio clips should use `file_path` for the audio file argument, not `path` or `file`.
- argument pairs that define a time range should be named `start_time` and `end_time`.
  A single argument that places something at a point in time should be named `position`.
- argument names should hint at the type where possible: 
  - `device_parameter` over `parameter` - the type is `DeviceParameter`, not just any parameter
  - `option_name` over `option` - the argument is a string name
- Callback and listener parameters should use bare `Callable`, not `Callable[[], None]` or other 
  parameterized forms. Only add `| None` when the description explicitly says None is accepted 
  (e.g. "pass None to stop").

## Pinned types

Use these exact types. Do not vary them.

- `ControlSurfaceProxy.send_value` arg2 type → `tuple[int, ...]` (MIDI values are always ints)
- `Licensing.PythonLicensingBridge.get_startup_dialog` authorize_callable → `Callable`
- `Licensing.PythonLicensingBridge.get_startup_dialog` authorize_later_callable → `Callable`
- `Licensing.PythonLicensingBridge.set_network_timer` callback → `Callable | None` (docs say "pass None to stop")
- `Listener.ListenerHandle.listener_func` probed_type → `Callable`
