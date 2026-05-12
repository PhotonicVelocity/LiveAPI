---
title: Remote scripts
slug: remote-scripts
sidebar_badge: core
_note: |
  Foundation page describing the runtime model that wraps every
  interaction with the LOM — not a class reference. Hoisted above
  the alphabetical Modules group in the sidebar (see
  `web/astro.config.mjs`).
---

A Remote Script is a Python module Live loads at startup to drive
external integrations — MIDI controllers, custom control surfaces,
network bridges. The script runs inside Live's bundled CPython
(3.11) and has direct in-process access to the Live Object Model.

Live ships a small helper framework (`_Framework`) used by every
Ableton-shipped surface, but a Remote Script doesn't have to use
it. Minimum viable script: any Python package whose `__init__.py`
exposes a `create_instance(c_instance)` factory.

```python
# Remote Scripts/MyScript/__init__.py
from .my_script import MyScript

def create_instance(c_instance):
    return MyScript(c_instance)
```

```python
# Remote Scripts/MyScript/my_script.py
class MyScript:
    def __init__(self, c_instance):
        self._c_instance = c_instance
        c_instance.show_message("MyScript loaded")

    def disconnect(self):
        pass
```

## Loading

Live scans `<User Library>/Remote Scripts/<ScriptFolder>/` once at
launch — script discovery runs only at startup. Adding or renaming
a script package requires a Live restart.

Activate via **Preferences → Link, Tempo & MIDI → Control Surface**
dropdown. Folder name is the script name shown in the dropdown.

Hot-swap during a running session: flip the dropdown to **None**,
then back. Live calls `disconnect()` on the old instance and
`create_instance()` fresh on the package — re-imports module-level
code, picks up edits.

Optional second top-level export: `get_capabilities()`. Returns a
dict declaring USB vendor/product IDs and default port settings.
Lets Live auto-detect the controller on hot-plug and pre-fill port
suggestions in the preferences UI. Used by most Ableton-shipped
scripts; not required for software-only scripts.

```python
def get_capabilities():
    return {
        CONTROLLER_ID_KEY: controller_id(
            vendor_id=0x09E8, product_ids=[0x0031],
            model_name="My Controller"),
        PORTS_KEY: [...],
    }
```

## The `c_instance` handle

Live passes one argument to `create_instance`: an opaque handle
representing the script's side of the bridge. The script keeps it
for the session and uses it to talk back to Live:

| Call | Effect |
|------|--------|
| `c_instance.song()` | Root `Song` object — entry point into the LOM. |
| `c_instance.show_message(text)` | Flash text in Live's status bar. |
| `c_instance.log_message(text)` | Append to `Log.txt`. |
| `c_instance.send_midi(bytes)` | Send a MIDI message back to the controller's output port. |
| `c_instance.request_rebuild_midi_map()` | Ask Live to call `build_midi_map()` again. |
| `c_instance.set_pad_translation(table)` | Pad-translation mapping (drum-pad surfaces). |
| `c_instance.set_feedback_velocity(value)` | Velocity used for LED feedback on velocity-sensitive pads. |
| `c_instance.toggle_lock()` | Toggle the script's device-lock state. |
| `c_instance.update_locks()` | Refresh device-lock state. |
| `c_instance.handle` | Opaque handle used by the MIDI map machinery. |

More callbacks exist on the handle (`playhead`, `preferences`,
`set_session_highlight`, ...) — survey a shipped script's
`c_instance.*` references for the full surface relevant to the
controller class being implemented.

Equivalent root access without `c_instance`: importing `Live`
directly works inside Remote Scripts (Live's bundled Python has
the binding pre-imported). `Live.Application.get_application()`
returns the application; `.get_document()` returns the same
`Song` as `c_instance.song()`.

## Lifecycle methods

Live calls these on the script instance at the relevant moments.
None are mandatory — a script that doesn't implement a method
gets the default no-op behavior.

| Method | When |
|--------|------|
| `__init__(c_instance)` | Once, at script load (via `create_instance`). |
| `disconnect()` | Live tearing down the script — app closing, dropdown switched, reload. Last chance to release listeners and close sockets / files. |
| `connect_script_instances(scripts)` | After all enabled scripts have loaded. Lets co-loaded scripts find each other (e.g. Mackie main + extender). |
| `update_display()` | Periodic tick — see below. |
| `receive_midi(bytes)` | Inbound MIDI from the assigned input port. |
| `receive_midi_chunk(chunk)` | Modern alternative — Live can deliver multi-message bursts in one call. |
| `build_midi_map(handle)` | Live asks the script to populate its mapping table — usually after `request_rebuild_midi_map()` or a port change. |
| `port_settings_changed()` | Live's MIDI port preferences changed. |
| `refresh_state()` | Force a full state push (LEDs, displays). |
| `is_extension()` | Return `True` if the script is a secondary surface paired with a main one. |
| `can_lock_to_devices()` / `lock_to_device(device)` / `unlock_from_device(device)` | Device-lock support. |
| `suggest_input_port()` / `suggest_output_port()` / `suggest_map_mode()` / `suggest_needs_takeover()` | Hints surfaced in Live's preferences UI. |
| `supports_pad_translation()` | Whether the script accepts pad-translation tables. |

## The tick

`update_display()` fires periodically on Live's main thread — the
same thread that calls `receive_midi()` and `build_midi_map()`.
Effective cadence is **~100 ms**: Ableton's `_Framework` advances
its task scheduler by `TIMER_DELAY = 0.1` seconds on every
`update_display`, and shipped scripts that schedule with
`schedule_message(N, callback)` treat one tick as 100 ms. Live
itself doesn't expose the cadence as a configurable; assume 100 ms
and design accordingly.

This is the only periodic callback Live provides; scripts can't
register their own timers.

Schedule one-shot future work via `c_instance.schedule_message(
delay_in_ticks, callback)` (or `self.schedule_message` when
inheriting from `_Framework.ControlSurface`).

Pattern for "do work continuously without blocking": chunk it,
run a slice per tick, re-schedule self.

```python
def _tick(self):
    self._do_one_unit_of_work()
    self.schedule_message(1, self._tick)
```

## Threading

**All Live API access is main-thread only.** Reading a property,
calling a method, registering a listener, firing a clip — every
LOM operation must be invoked from inside one of the lifecycle
callbacks above (or from a `schedule_message` callback, which
runs in the same context). Touching the LOM from a worker thread
is undefined behavior — typical outcomes are silent state
corruption, immediate crash, or sporadic crashes that are hard
to reproduce.

**No asyncio.** Live's bundled Python doesn't run an event loop
for Remote Scripts; `async def` coroutines aren't awaited.
Cooperative multitasking happens through the tick.

**Main thread is also Live's UI thread.** A callback that doesn't
return promptly stalls the UI: clip launches feel laggy, the GUI
freezes. A callback that hangs forever hangs the entire app —
the user has to force-quit Live, losing unsaved work.

**The audio engine runs on a separate real-time thread.** A slow
or hung Remote Script doesn't interrupt audio playback, MIDI
clock, or already-running clips — the song keeps going while the
GUI is frozen. Practical consequence: a script can't cause audio
dropouts by being slow on the main thread, but it absolutely can
destroy the user's ability to interact with their running set.

## What not to do in a callback

Anything that holds the main thread for tens of milliseconds is
felt as UI lag. Anything that holds it indefinitely freezes Live.

Avoid in any lifecycle / tick / listener callback:

- Blocking I/O — `socket.recv()` without `setblocking(False)`,
  synchronous HTTP, large file reads
- `time.sleep()` of any duration
- Tight loops over large LOM collections without yielding
- Spawning threads that touch the LOM (touching from a worker
  thread is UB regardless of duration)

Acceptable: bounded non-blocking I/O (drain a non-blocking
socket for a few ms then yield), small file reads at startup,
spawning threads that do their own pure-Python work and post
results back via a queue the main thread polls in `_tick`.

## Logging

Two channels:

```python
c_instance.log_message("...")    # appends to Log.txt
c_instance.show_message("...")   # flashes Live's status bar
```

`Log.txt` location: `<User Library>/Preferences/Log.txt` on
macOS, the equivalent on Windows. Tail this during development.
Uncaught Python exceptions print full tracebacks here.

Python's stdlib `logging` module also lands in `Log.txt` —
works as expected; no special configuration needed.

## Reload during development

Live only re-scans the Remote Scripts directory at startup, so
iterating on a script normally means restarting Live every
edit. Two ways around it:

1. **Dropdown bounce.** Flip Control Surface to None, then back.
   Live calls `disconnect()`, then `create_instance()` fresh —
   picks up edits to anything `__init__.py` imports.

2. **In-process `importlib.reload()`.** Wire any controllable
   trigger the script can detect — a specific MIDI message, a
   file-watch hit, an external signal — to reload chosen
   submodules. Module-level state in the reloaded submodules
   resets; the script-class instance itself survives, so
   anything stored on `self` persists across the reload. The
   script package's `__init__.py` cannot reload itself
   in-process — only the submodules it imports.

Pre-existing wired-up callbacks (Live listeners, scheduled
messages) survive a `disconnect()` only if your `disconnect()`
releases them — leak audits are a development-time
responsibility.
