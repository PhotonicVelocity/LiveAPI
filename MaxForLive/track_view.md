# Track.View

Representing the view aspects of a track.

## Canonical Path

```
live_set tracks N view
```

## Children

### selected_device [Device](/apiref/lom/device/ "Device") read-onlyobserve

The selected device or the first selected device (in case of multi/group selection).

## Properties

### device_insert_mode int observe

Determines where a device will be inserted when loaded from the browser. 0 = add device at the end, 1 = add device to the left of the selected device, 2 = add device to the right of the selected device.

### is_collapsed bool observe

In Arrangement View: 1 = track collapsed, 0 = track opened.

## Functions

### select_instrument

Returns: bool 0 = there are no devices to select   
Selects track's instrument or first device, makes it visible and focuses on it.
