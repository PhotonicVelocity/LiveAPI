# ChainMixerDevice

> `Live.ChainMixerDevice.ChainMixerDevice`

This class represents a Chain's Mixer Device in Live, which gives you access to the Volume, Panning, and Send properties of a Chain.

**Live Object:** `yes`

## Properties

| Property           | Type              | Settable | Listenable | Description                                                        |
| ------------------ | ----------------- | -------- | ---------- | ------------------------------------------------------------------ |
| `canonical_parent` | `Chain`           | `no`     | `no`       | Get the canonical parent of the mixer device.                      |
| `chain_activator`  | `DeviceParameter` | `no`     | `no`       | Const access to the Chain's Activator Device Parameter.            |
| `panning`          | `DeviceParameter` | `no`     | `no`       | Const access to the Chain's Panning Device Parameter.              |
| `sends`            | `tuple`           | `no`     | `yes`      | Const access to the Chain's list of Send Amount Device Parameters. |
| `volume`           | `DeviceParameter` | `no`     | `no`       | Const access to the Chain's Volume Device Parameter.               |

### `canonical_parent`

- **Type:** `Chain`
- **Settable:** `no`
- **Listenable:** `no`

Get the canonical parent of the mixer device.

### `chain_activator`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Chain's Activator Device Parameter.

### `panning`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Chain's Panning Device Parameter.

### `sends`

- **Type:** `tuple`
- **Settable:** `no`
- **Listenable:** `yes`

Const access to the Chain's list of Send Amount Device Parameters.

### `volume`

- **Type:** `DeviceParameter`
- **Settable:** `no`
- **Listenable:** `no`

Const access to the Chain's Volume Device Parameter.
