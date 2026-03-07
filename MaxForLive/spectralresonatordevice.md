# SpectralResonatorDevice

This class represents an instance of a Spectral Resonator device in Live.   
An SpectralResonatorDevice has all the properties, functions and children of a Device. Listed below are members unique to SpectralResonatorDevice.

## Properties

### frequency_dial_mode int observe

Get, set and observe the Freq control's mode.  
0 = Hertz, 1 = MIDI note values.

### midi_gate int observe

Get, set and observe the MIDI gate switch's state.  
0 = Off, 1 = On.

### mod_mode int observe

Get, set and observe the Modulation Mode.  
0 = None, 1 = Chorus, 2 = Wander, 3 = Granular.

### mono_poly int observe

Get, set and observe the Mono/Poly switch's state.  
0 = Mono, 1 = Poly.

### pitch_mode int observe

Get, set and observe the Pitch Mode.  
0 = Internal, 1 = MIDI.

### pitch_bend_range int observe

Get, set and observe the Pitch Bend Range.\

### polyphony int observe

Get, set and observe the Polyphony.  
0 = 2, 1 = 4, 2 = 8, 3 = 16 voices.
