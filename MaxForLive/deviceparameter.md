# DeviceParameter

This class represents an (automatable) parameter within a MIDI or audio device. To modify a device parameter, set its `value` property or send its object ID to [live.remote~](/reference/live.remote~ "live.remote~").

## Canonical Path

```
live_set tracks N devices M parameters L
```

## Properties

### automation_state int read-onlyobserve

Get the automation state of the parameter.   
0 = no automation.   
1 = automation active.   
2 = automation overridden.

### default_value float read-only

Get the default value for this parameter.   
Only available for parameters that aren't quantized (see *is_quantized*).

### is_enabled bool read-only

1 = the parameter value can be modified directly by the user, by sending `set` to a [live.object](/reference/live.object "live.object"), by automation or by an assigned MIDI message or keystroke.   
Parameters can be disabled because they are macro-controlled, or they are controlled by a live-remote~ object, or because Live thinks that they should not be moved.

### is_quantized bool read-only

1 for booleans and enums   
0 for int/float parameters   
Although parameters like MidiPitch.Pitch appear quantized to the user, they actually have an is_quantized value of 0.

### max float read-only

Largest allowed value.

### min float read-only

Lowest allowed value.

### name symbol read-only

The short parameter name as shown in the (closed) automation chooser.

### original_name symbol read-only

The name of a Macro parameter before its assignment.

### state int read-onlyobserve

The active state of the parameter.   
0 = the parameter is active and can be changed.   
1 = the parameter can be changed but isn't active, so changes won't have an audible effect.   
2 = the parameter cannot be changed.

### value float observe

The internal value between min and max. Use display_value for the value as visible in the GUI.

### display_value float observe

The value as visible in the GUI.

### value_items StringVector read-only

Get a list of the possible values for this parameter.   
Only available for parameters that are quantized (see *is_quantized*).

## Functions

### re_enable_automation

Re-enable automation for this parameter.

### str_for_value

Parameter: `value` [float] Returns: [symbol] String representation of the specified value.

### __str__

Returns: [symbol] String representation of the current parameter value.
