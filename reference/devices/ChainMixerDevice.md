---
toc_depth: 2
---

# ChainMixerDevice (Module)

## ChainMixerDevice (Class)

> `Live.ChainMixerDevice.ChainMixerDevice`

This class represents a Chain's Mixer Device in Live, which gives you access to the Volume, Panning, and Send properties of a Chain.

**Live Object:** `yes`

**Access via:**

- `Chain.mixer_device`
- `DrumChain.mixer_device`

### Properties

| Property                                | Type              | Supports       |
| --------------------------------------- | ----------------- | -------------- |
| [`canonical_parent`](#canonical_parent) | `Chain`           | `get`          |
| [`chain_activator`](#chain_activator)   | `DeviceParameter` | `get`          |
| [`panning`](#panning)                   | `DeviceParameter` | `get`          |
| [`sends`](#sends)                       | `tuple`           | `get`/`listen` |
| [`volume`](#volume)                     | `DeviceParameter` | `get`          |

#### `canonical_parent`

- **Type:** `Chain`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the mixer device.

#### `chain_activator`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Chain's Activator Device Parameter.

#### `panning`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Chain's Panning Device Parameter.

#### `sends`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the Chain's list of Send Amount Device Parameters.

#### `volume`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Chain's Volume Device Parameter.
