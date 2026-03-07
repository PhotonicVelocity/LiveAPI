# Groove

This class represents a groove in Live.   
  
*Available since Live 11.0.*  
All grooves are stored in Live's groove pool.

## Canonical Paths

```
live_set groove_pool grooves N
```

```
live_set tracks N clip_slots M clip groove
```

## Children

### base int

Get/set the groove's base grid (index based setter).   
0 = 1/4   
1 = 1/8   
2 = 1/8T   
3 = 1/16   
4 = 1/16T   
5 = 1/32

### name symbol observe

Get/set/observe the name of the groove.

### quantization_amount float observe

Get/set/observe the groove's quantization amount.

### random_amount float observe

Get/set/observe the groove's random amount.

### timing_amount float observe

Get/set/observe the groove's timing amount.

### velocity_amount float observe

Get/set/observe the groove's velocity amount.
