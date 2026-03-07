# Application.View

This class represents the aspects of the Live application related to viewing the application.

## Canonical Path

```
live_app view
```

## Properties

### browse_mode bool read-onlyobserve

1 = Hot-Swap Mode is active for any target.

### focused_document_view unicode read-onlyobserve

The name of the currently visible view in the focused Live window ('Session' or 'Arranger').

## Functions

### available_main_views

Returns: `view names` [list of symbols].   
This is a constant list of view names to be used as an argument when calling other functions: `Browser Arranger Session Detail Detail/Clip Detail/DeviceChain`.

### focus_view

Parameter: `view_name`  
Shows named view and focuses on it. You can also pass an empty view_name “ ", which refers to the Arrangement or Session View (whichever is visible in the main window).

### hide_view

Parameter: `view_name`  
Hides the named view. You can also pass an empty view_name “ ", which refers to the Arrangement or Session View (whichever is visible in the main window).

### is_view_visible

Parameter: `view_name`  
Returns: [bool] Whether the specified view is currently visible.

### scroll_view

Parameters: `direction view_name modifier_pressed`  
`direction` [int] is 0 = up, 1 = down, 2 = left, 3 = right   
`modifier_pressed` [bool] If view_name is "Arranger" and modifier_pressed is 1 and direction is left or right, then the size of the selected time region is modified, otherwise the position of the playback cursor is moved.   
Not all views are scrollable, and not in all directions. Currently, only the `Arranger`, `Browser`, `Session`, and `Detail/DeviceChain` views can be scrolled.   
You can also pass an empty view_name `" "`, which refers to the Arrangement or Session View (whichever view is visible).

### show_view

Parameter: `view_name`

### toggle_browse

Displays the device chain and the browser and activates Hot-Swap Mode for the selected device. Calling this function again deactivates Hot-Swap Mode.

### zoom_view

Parameter: `direction view_name modifier_pressed`  
`direction` [int] - 0 = up, 1 = down, 2 = left, 3 = right   
`modifier_pressed` [bool] If `view_name` is 'Arrangement', `modifier_pressed` is 1, and `direction` is left or right, then the size of the selected time region is modified, otherwise the position of the playback cursor is moved. If `view_name` is Arrangement and `modifier_pressed` is 1 and `direction` is up or down, then only the height of the highlighted track is changed, otherwise the height of all tracks is changed.   
Only the Arrangement and Session Views can be zoomed. For Session View, the behaviour of zoom_view is identical to scroll_view. You can also pass an empty view_name “ ", which refers to the Arrangement or Session View (whichever is visible in the main window).
