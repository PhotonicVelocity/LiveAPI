# Live Object Model Reference

Comprehensive reference for the Ableton Live Object Model (LOM) — the object hierarchy exposed by Live's
Python runtime to Control Surface scripts, Max for Live devices, and external clients.

## About

Ableton does not publicly document the Live Python API. This reference is auto-generated from
API stubs produced by running introspection inside Live.

## How to Read

Each page documents one LOM class with:

- **Summary tables** — quick overview of all properties and methods
- **Detail sections** — per-member descriptions with type info
- **Enums** — value tables for enum types defined in each namespace

Use the sidebar navigation to browse by LOM hierarchy, or search for a specific class or member.

## Core

| Class                         | Namespace          |
| ----------------------------- | ------------------ |
| [Application](Application.md) | `Live.Application` |
| [Song](Song.md)               | `Live.Song`        |
| [Scene](Scene.md)             | `Live.Scene`       |

## Tracks

| Class                                | Namespace          |
| ------------------------------------ | ------------------ |
| [Track](tracks/Track.md)             | `Live.Track`       |
| [Clip](tracks/Clip.md)               | `Live.Clip`        |
| [ClipSlot](tracks/ClipSlot.md)       | `Live.ClipSlot`    |
| [Envelope](tracks/Envelope.md)       | `Live.Envelope`    |
| [MixerDevice](tracks/MixerDevice.md) | `Live.MixerDevice` |
| [TakeLane](tracks/TakeLane.md)       | `Live.TakeLane`    |

## Devices

| Class                                           | Namespace               |
| ----------------------------------------------- | ----------------------- |
| [Device](devices/Device.md)                     | `Live.Device`           |
| [DeviceParameter](devices/DeviceParameter.md)   | `Live.DeviceParameter`  |
| [Chain](devices/Chain.md)                       | `Live.Chain`            |
| [ChainMixerDevice](devices/ChainMixerDevice.md) | `Live.ChainMixerDevice` |
| [DrumChain](devices/DrumChain.md)               | `Live.DrumChain`        |
| [DrumPad](devices/DrumPad.md)                   | `Live.DrumPad`          |
| [RackDevice](devices/RackDevice.md)             | `Live.RackDevice`       |

## Device Subclasses

| Class                                                         | Namespace                      |
| ------------------------------------------------------------- | ------------------------------ |
| [CcControlDevice](devices/CcControlDevice.md)                 | `Live.CcControlDevice`         |
| [CompressorDevice](devices/CompressorDevice.md)               | `Live.CompressorDevice`        |
| [DeviceIO](devices/DeviceIO.md)                               | `Live.DeviceIO`                |
| [DriftDevice](devices/DriftDevice.md)                         | `Live.DriftDevice`             |
| [DrumCellDevice](devices/DrumCellDevice.md)                   | `Live.DrumCellDevice`          |
| [Eq8Device](devices/Eq8Device.md)                             | `Live.Eq8Device`               |
| [HybridReverbDevice](devices/HybridReverbDevice.md)           | `Live.HybridReverbDevice`      |
| [LooperDevice](devices/LooperDevice.md)                       | `Live.LooperDevice`            |
| [MaxDevice](devices/MaxDevice.md)                             | `Live.MaxDevice`               |
| [MeldDevice](devices/MeldDevice.md)                           | `Live.MeldDevice`              |
| [PluginDevice](devices/PluginDevice.md)                       | `Live.PluginDevice`            |
| [RoarDevice](devices/RoarDevice.md)                           | `Live.RoarDevice`              |
| [Sample](devices/Sample.md)                                   | `Live.Sample`                  |
| [ShifterDevice](devices/ShifterDevice.md)                     | `Live.ShifterDevice`           |
| [SimplerDevice](devices/SimplerDevice.md)                     | `Live.SimplerDevice`           |
| [SpectralResonatorDevice](devices/SpectralResonatorDevice.md) | `Live.SpectralResonatorDevice` |
| [WavetableDevice](devices/WavetableDevice.md)                 | `Live.WavetableDevice`         |

## Other

| Class                                 | Namespace           |
| ------------------------------------- | ------------------- |
| [Browser](Browser.md)                 | `Live.Browser`      |
| [Base](other/Base.md)                 | `Live.Base`         |
| [Conversions](other/Conversions.md)   | `Live.Conversions`  |
| [Groove](other/Groove.md)             | `Live.Groove`       |
| [GroovePool](other/GroovePool.md)     | `Live.GroovePool`   |
| [Licensing](other/Licensing.md)       | `Live.Licensing`    |
| [Listener](other/Listener.md)         | `Live.Listener`     |
| [LomObject](other/LomObject.md)       | `Live.LomObject`    |
| [MidiMap](other/MidiMap.md)           | `Live.MidiMap`      |
| [TuningSystem](other/TuningSystem.md) | `Live.TuningSystem` |
