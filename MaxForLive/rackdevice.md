# RackDevice

This class represents a Live Rack Device.   
A RackDevice is a type of Device, meaning that it has all the children, properties and functions that a Device has. Listed below are members unique to RackDevice.

## Children

### chain_selector [DeviceParameter](/apiref/lom/deviceparameter/ "DeviceParameter") read-only

Convenience accessor for the Rack's chain selector.

### chains list of [Chain](/apiref/lom/chain/ "Chain") read-onlyobserve

The Rack's chains.

### drum_pads list of [DrumPad](/apiref/lom/drumpad/ "DrumPad") read-onlyobserve

All 128 Drum Pads for the topmost Drum Rack. Inner Drum Racks return a list of 0 entries.

### return_chains list of [Chain](/apiref/lom/chain/ "Chain") read-onlyobserve

The Rack's return chains.

### visible_drum_pads list of [DrumPad](/apiref/lom/drumpad/ "DrumPad") read-onlyobserve

All 16 visible DrumPads for the topmost Drum Rack. Inner Drum Racks return a list of 0 entries.

## Properties

### can_show_chains bool read-only

1 = The Rack contains an instrument device that is capable of showing its chains in Session View.

### has_drum_pads bool read-onlyobserve

1 = the device is a Drum Rack with pads. A nested Drum Rack is a Drum Rack without pads.   
Only available for Drum Racks.

### has_macro_mappings bool read-onlyobserve

1 = any of a Rack's Macros are mapped to a parameter.

### is_showing_chains bool observe

1 = The Rack contains an instrument device that is showing its chains in Session View.

### variation_count int read-onlyobserve

The number of currently stored macro variations.   
  
*Available since Live 11.0.*

### selected_variation_index int

Get/set the currently selected variation.   
  
*Available since Live 11.0.*

### visible_macro_count int read-onlyobserve

The number of currently visible macros.

## Functions

### copy_pad

Parameters:   
`source_index` [int]   
`destination_index` [int]   
Copies all content of a Drum Rack pad from a source pad to a destination pad. The source_index and destination_index refer to pad indices inside a Drum Rack.

### add_macro

Increases the number of visible macro controls.   
  
*Available since Live 11.0.*

### insert_chain

Parameters: `index` [int] (optional)   
  
Attempts to insert a new chain at the given index, or at the end of the chain list if no index is provided. Throws an error if insertion is not possible.   
Side note: A chain inserted into a Drum Rack will have an initial MIDI In Note setting of "All Notes" (see `DrumChain.in_note`). You likely want the chain to be triggered when a specific pad is played; the way to achieve this is to set the `in_note` to the note value that corresponds to the pad.   
  
*Available since Live 12.3.*

### remove_macro

Decreases the number of visible macro controls.   
  
*Available since Live 11.0.*

### randomize_macros

Randomizes the values of eligible macro controls.   
  
*Available since Live 11.0.*

### store_variation

Stores a new variation of the values of all currently mapped macros.   
  
*Available since Live 11.0.*

### recall_selected_variation

Recalls the currently selected macro variation.   
  
*Available since Live 11.0.*

### recall_last_used_variation

Recalls the macro variation that was recalled most recently.   
  
*Available since Live 11.0.*

### delete_selected_variation

Deletes the currently selected macro variation. Does nothing if there is no selected variation.   
  
*Available since Live 11.0.*
