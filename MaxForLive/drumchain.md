# DrumChain

This class represents a Drum Rack device chain in Live.   
  
A DrumChain is a type of Chain, meaning that it has all the children, properties and functions that a Chain has. Listed below are the members unique to DrumChain.

## Properties

### in_note int observe

Get/set the MIDI note that will trigger this chain. The value -1 corresponds to the "All Notes" setting in the UI.   
  
*Available since Live 12.3*

### out_note int observe

Get/set the MIDI note sent to the devices in the chain.

### choke_group int observe

Get/set the chain's choke group.
