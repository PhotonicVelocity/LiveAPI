# RackDevice.View

Represents the view aspects of a Rack Device.   
A RackDevice.View is a type of Device.View, meaning that it has all the properties that a Device.View has. Listed below are the members unique to RackDevice.View.

## Children

### selected_drum_pad [DrumPad](/apiref/lom/drumpad/ "DrumPad") observe

Currently selected Drum Rack pad.   
Only available for Drum Racks.

### selected_chain [Chain](/apiref/lom/chain/ "Chain") observe

Currently selected chain.

## Properties

### drum_pads_scroll_position int observe

Lowest row of pads visible, range: 0 - 28.   
Only available for Drum Racks.

### is_showing_chain_devices bool observe

1 = the devices in the currently selected chain are visible.
