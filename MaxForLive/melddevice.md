# MeldDevice

This class represents an instance of a Meld device in Live.   
A MeldDevice has all the properties, functions and children of a Device.

## Properties

### selected_engine int observe

Meld's oscillator engine selector. The modes are encoded as follows:   
0 = Engine A   
1 = Engine B

### unison_voices int observe

Selects the Unison voice count. The modes are encoded as follows:   
  
0 = off   
1 = two   
2 = three   
3 = four

### mono_poly int observe

Selects the polyphony mode. The modes are encoded as follows:   
  
0 = mono   
1 = poly

### poly_voices int observe

Selects the polyphony voice count. The modes are encoded as follows:   
  
0 = two   
1 = three   
2 = four   
3 = five   
4 = six   
5 = eight   
6 = twelve
