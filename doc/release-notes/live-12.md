# Ableton Live 12 Release Notes

## 12.3.6 (March 3, 2026)

### New Features and Improvements

- Added Control Surface support for the Novation Launch Control 3.

### Bugfixes

- Fixed a bug in the Launch Control XL 3 Control Surface that could cause the Track button LEDs to show incorrect states while Shift was held after return tracks were added or removed.
- Fixed an issue that occurred when macro mapping Simpler's legacy filter type, where it was not possible to set the filter type to Notch.

## 12.3.5 (January 26, 2026)

### New Features and Improvements

**Bounce to Audio**

- When using the Bounce to New Track command, bounced tracks now display a unique track number instead of the source track’s number. When first bounced, new tracks will use one number higher than the source track, so if track 3 is bounced, the new track becomes track 4.

**Browser**

- When starting a new search with the Ctrl F (Win) / Cmd F (Mac) shortcut, any previous search terms and active filters in the All label are now cleared.

**Interface**

- Updated software text in various areas of Live.
- Updated various software text translations in German, Spanish, French, Italian, Japanese, and Simplified Chinese.

**Live Bugfixes**

- Bouncing a Group Track no longer produces a silent bounce file when a track outside the group is soloed. This behavior is now consistent with bouncing individual tracks.
- Fixed an issue where bouncing a nested Group Track caused the main Group Track’s effects to be applied to the bounced audio twice.

**Setup**

- Files that are older than one week in the Crash folder of Live’s preferences are now automatically deleted when Live is launched.

### Bugfixes

**Live Bugfixes**

- Fixed an issue where it was possible to extend the right edge of a bounced audio clip past the original source clip length.
- Fixed an issue where MIDI signals routed to a plug-in via the External Instrument device were ignored when exporting the track containing the plug-in using the Selected Tracks Only option.
- Fixed a bug in the APC64 Control Surface that could result in an error being written to Live's Log.txt file when using a touch strip to adjust a disabled parameter.
- Accessibility: Fixed an issue that occurred when navigating Max for Live devices with the keyboard while wrapped navigation was turned off.
- Fixed an issue where the DS HH instrument could miss notes.
- Fixed an issue where samples could not be dropped from the Session or Arrangement View onto plug-in windows as expected.
- Fixed an issue where adding a device with a focused control to a multiselection caused the multiselection to be lost. Adding devices to a multiselection now works as expected. As a result of this change, selecting a device’s title bar now clears the focus of any controls within the device.
- Fixed a crash that could occur on Windows when closing Live from the taskbar after confirming whether to save a modified Live Set.
- Fixed a crash that could occur when loading a Soundtoys plug-in and then performing an undo step to remove the plug-in.
- The buttons in the Help View header now use a square shape.
- Fixed an issue where using the Bounce Track In Place command on a track containing only a very short clip created an additional undo step.
- Live no longer crashes when selecting and deleting multiple tracks when one of the tracks has a remote~ mapped to a track parameter.
- Fixed an issue where soloing would not work as expected in some scenarios involving an instrument modulated by a Max for Live device.
- Fixed a crash that occurred in Session View when dragging a clip selection containing a clip that was being recorded.
- Fixed a crash that occurred when starting Live with the screen zoomed in using the macOS Zoom accessibility feature.

**Max for Live**

- Updated the bundled Max version to build 9.0.10. This includes a fix for an issue on Push 3 that occurred when disabling OpenGL in the context of Max for Live. Please see the [Max 9.0.10 Release Notes](https://cycling74.com/releases/max/9.0.10) for all updates.

## 12.3.2 (December 17, 2025)

### Bugfixes

- Fixed an issue with the Max for Live API that caused Live to lag or freeze.

## 12.3.1 (December 9, 2025)

### Bugfixes

- Fixed a crash that could occur when loading a Soundtoys plug-in and then performing an undo step to remove the plug-in.
- Updated software text in various areas of Live.

## 12.3 (November 25, 2025)

### Stem Separation

Live Suite now features built-in stem separation that runs locally. Any recorded audio material — such as a song, loop, or sample — can be separated into four stems: Vocals, Drums, Bass, and Others. The Others stem includes all parts of the audio that are not recognized as vocals, drums, or bass.

You can separate audio files from the browser or separate clips from the Session or Arrangement View. To do so, right-click a sample in the browser or a clip in Session or Arrangement View and select Separate Stems to New Audio Tracks. Each stem is rendered onto its own track in a new Group Track. Any audio effects from the source track are also added to the Group Track. The clip used for separation is muted to avoid doubled output.

You can choose between two quality modes for the separation: High Speed and High Quality. The mode determines whether the separation process prioritizes quickness or accuracy. In High Speed mode, all stems are separated in a single pass, so the process will be faster, though it may still take several minutes on older system configurations. In High Quality mode, the separation accuracy is improved (as measured by a higher Signal-to-Distortion Ratio, i.e., SDR score), at the cost of slower processing. The Vocals, Drums, and Bass parts are processed through their own dedicated separation passes. The Others stem is then created from the remaining audio after the three passes.

Generally speaking, the overall amount of time required for the separation process highly depends on your system configuration. Stem separation may take a while on older Windows computers, Intel Macs, and Mac computers running macOS 11 Big Sur. Due to an incompatibility issue, stem separation will also run slowly on Apple Silicon computers with macOS 26.1 Tahoe. See this article for more information on macOS compatibility with Live.

### Splice Integration

Splice - the industry’s leading sample library - is now integrated into Live’s browser. Anyone with a free or paid Splice account can access their library, browse, preview, and download samples directly within Live.

You can browse and save samples to your Splice library, as well as preview Splice samples in sync with Live's transport. When you find a sample you like, you can drag it from the Splice label into the Session or Arrangement View. Alternatively, you can double-click the sample name or press the Enter key to load the sample into a Set.

Imported samples are saved to the User Library → Samples → Splice folder by default. You can update this location to the Current Project folder or a custom folder using the Download Folder for Splice Samples option in Live’s Library Settings.

In addition to searching for samples, you can have Splice find samples that would fit with existing material in your Set. To do so, make a clip or time selection within Session or Arrangement View, then click the Search with Sound widget in the Home tab of the Splice label. Splice will then find and display complementary samples based on the style and rhythm of the selection.

The Key filter in the sample categories within Splice includes an “Apply Key from DAW” option, which automatically detects the scale root and name set in Live’s transport bar when Scale Mode is active. You can use this option to constrain search results to the detected key and scale. Note that only major and minor scales are supported with this option. You can also use the Transpose option in the Splice Preview settings to set different transpositions for sample playback within the Splice label or sync the Splice Preview to the Set’s key.

By default, the Splice label is visible within the browser, but you can hide it via the “Hide from Sidebar” command in its context menu. The corresponding option in Live's Library Settings will also be updated accordingly.

Note that a Splice account is required to use this feature, including non-subscription accounts (which offer around 2,500 free samples). You can follow the instructions in the Splice label to create a new account as needed.

### Auto Pan-Tremolo Updates

Auto Pan now features an updated interface, including dedicated modes for panning and tremolo effects. To reflect its expanded functionality, the device has been renamed Auto Pan-Tremolo.

- Two modes are now available: Panning and Tremolo. Panning modulates the placement of the source sound in the stereo panorama, while Tremolo modulates the signal level.
- A real-time visualization displays either the current panning position in Panning mode or the current tremolo level in Tremolo mode.
- New LFO Time modes include 16th, Triplet, Dotted, and Time. In Time mode, you can set the period of the LFO in seconds, which is useful for creating very long modulation cycles.
- The Modulation Attack parameter ramps the LFO modulation when an onset occurs in the input signal. This causes the modulation to increase gradually so that it mainly affects the sustained portion of the signal. In Tremolo mode, this helps preserve transients, while in Panning mode, this keeps them in the center of the stereo field.
- The Frequency Modulation parameter dynamically scales the LFO frequency based on the input signal’s level over time. Positive values speed up the modulation, while negative values slow it down.
Tremolo mode offers several distinctive traits:

- A single LFO waveform is available, which can be morphed using the Shape parameter and inverted using the Invert toggle. Exponential and linear ramp shapes are useful for gating and ducking effects.
- Harmonic mode modulates the signal level across fixed frequency bands in an alternating pattern, creating a dense, lush tremolo effect.
- Vintage mode introduces additional warmth and grit alongside the tremolo effect by modulating the intensity of a non-linear curve instead of the signal level.
Note that the original Auto Pan device remains available in the browser and has been renamed Auto Pan Legacy. When opening existing Sets that contain Auto Pan presets, the legacy device will be automatically loaded.

### Bounce Group Tracks

It is now possible to bounce Group Tracks via two new commands: Bounce Group to New Track and Bounce Group in Place.

The Bounce Group to New Track command is available in the context menu for individual group slots or selections of group slots in Session View, and within the main lane of a Group Track in Arrangement View. The Group Track is bounced with all its processing, including any return tracks used via sends from the Group Track or any of its included tracks. For that reason, bouncing is performed from the Main track, pre-FX. The bounced audio is added as a clip to a new track.

The Bounce Group in Place command is available in a track title bar’s context menu, as well as the context menu for group slots in Session View and for the insert marker within the main lane of a Group Track in Arrangement View. This command bounces the Group Track along with all of its processing, including return tracks, as previously described for Bounce Group to New Track. The bounced audio replaces the Group Track with a single audio track.

Note that bouncing Group Tracks works similarly to rendering Group Tracks with the Include Return and Main Effects option. The key difference is that rendering is performed post-mixer on the Main track, while bouncing is performed pre-mixer on the Main track. This means that some routing configurations may produce silence or a partial signal when bouncing Group Tracks. For example, any tracks routed outside the Group Track are not included in the bounce. Additionally, return tracks that are part of the Group Track’s signal path are only included in the bounce if their final output reaches the Main track.

### Paste Bounced Audio

It is now possible to paste bounced audio from copied material as an alternative to using the Bounce to New Track or Bounce Group to New Track command.

To do this, first copy one or more clips in Session View, or a time selection in the Arrangement, from a single MIDI, audio, or Group Track using the regular Copy command. Then, right-click in an audio track, an empty MIDI track, or a take lane, and select the Paste Bounced Audio command from the context menu or the Edit menu. The copied material will then be bounced and pasted onto the track or lane.

Note that the source material is bounced in its current state when Paste Bounced Audio is used. This means you can modify the material and use the command again to create variations. Additionally, if the material is deleted, the Paste Bounced Audio command will no longer be available.

### Device A/B Comparison

Two new entries have been added to the device title bar’s Options menu: Compare: Switch to A/B and Compare: Copy A/B to B/A.

You can use Compare: Switch to A/B to toggle between two different device states: A and B. Each state can have its own unique set of parameter values. You can, for example, use state A for tweaking values while leaving state B at the device’s default settings, and then switch between the two to assess the differences. The corresponding shortcut for comparing device states is P .

To copy the current parameter settings from one device state to another, use Compare: Copy A/B to B/A. This is useful for preserving specific parameter changes that you want to keep while freeing up the other state for more experimentation.

Note that this feature is also accessible via the Max for Live API.

### New Features and Improvements

**Arrangement View**

- In Arrangement clips, MIDI notes where the note start is not part of the Arrangement will not be drawn, since they should not be played.
- In the Arrangement View, the Insert Empty MIDI Clip command can now be used without time selection and will insert a clip at the insert marker. The clip length will be one bar or the currently selected grid size, whichever is longer.
- Double-clicking to create an empty MIDI clip in the Arrangement View will now work when the grid cell is not completely empty. The clip created as a result will fill the available space in the grid cell.
- It is now possible to create Arrangement MIDI clips in a definable time range by holding Shift while double-clicking.

**Browser**

- The browser now features new default sidebar icons for Drums, Instruments, Audio Effects, and Packs.
- Updated the icons for devices and presets to improve discoverability and to better distinguish between type (audio, MIDI, instruments) and architecture (built-in devices, Max for Live).
- When filtering for Content|Set, the results no longer show backup Sets. A new Content|Backup Set filter can be used to filter by backup Sets instead.
- When the browser is in focus, it is now possible to show and hide the Filter View and Tag Editor with the following shortcuts: Filter View: Ctrl Alt G (Win) / Cmd Option G (Mac) Tag Editor: Ctrl Shift E (Win) / Cmd Shift E (Mac)
- Double-clicking a tag in the Quick Tags panel now adds that tag to the search field and triggers a tag search.
- There is a new context menu entry "Show tag X in Tag Editor" available when right-clicking a tag button in the Quick Tags panel. Selecting this entry opens the Tag Editor and moves focus to the tag.
- It is now possible to hide the Splice, Cloud, and Push labels by right-clicking on them in the browser sidebar and selecting the "Hide from Sidebar" command. The corresponding options in Live's Settings will be updated accordingly.

**Clip View**

- It is now possible to use the "Set 1.1.1 Here" context menu command for multiple audio clips as long as all clips are of the same length and have the same warp marker positions.

**Control Surfaces**

- Newer control surfaces can now access an additional parameter bank in the CC Control device.
- The Move Control Surface now offers a wider array of LED brightness options when using recent firmware.
- When using the Move Control Surface, it is now possible to navigate between device parameter banks by pressing Shift and turning the wheel.

**Core Library**

- Added new Drum Racks and samples by Tamuz.
- Added two new templates for recording vocals and guitar.
- Added new presets for Auto Pan-Tremolo (the previous presets are now stored in the Auto Pan Legacy folder).
- Added Push XY mappings to Rack presets.
- Added small refinements to the Vocal Recording Template and Drum Rack presets.
- Fixed the Lydian Scale preset.

**Interface**

- Reduced the minimum mixer height, which makes it possible to substantially decrease the size of the mixer when editing clips or Arrangement content. As a result of this change: The mixer pan controls will be hidden as the mixer's size is reduced. The track activator buttons will become compressed as the mixer gets smaller.
- When using time-limited licenses (such as rent-to-own), Live now periodically displays a progress dialog during runtime while attempting to re-authorize the license. If the license has expired, a prompt to save the Set appears before saving and exporting are disabled. If no internet connection is available during the re-authorization, a prompt to retry is displayed; otherwise, saving and exporting will be disabled.
- Added purchasing options to several areas within the trial version of Live.
- Updated the What's New in Live lesson to include features from Live 12.3.
- Updated software text in various areas of Live.
- Updated various software text translations in German, Spanish, French, Italian, Japanese, and Chinese.

**Max for Live**

- Updated the bundled Max version to build 9.0.9: Max for Live Improvements JS Live API: fixed crash when path to jsliveapi_setpathfromid is invalid live.banks: support button assignments for parameter banks live.grid: direction arrows redraw after click Read the complete release notes from Cycling '74: Max 9.0.9 Release Notes | Cycling '74
- The following attributes are now available via the Max for Live API: Track.insert_device and Chain.insert_device: Inserts the specified device at the optionally provided index in the track or chain. If no index is provided, the device will be inserted at the end of the chain. The device name is the name as it appears in the browser. Only native Live devices can be inserted; Max for Live devices and plug-ins are not supported. RackDevice.insert_chain: Inserts a new chain at the given index, or at the end of the chain list if no index is provided. DrumChain.in_note: Get/set/observe access to the MIDI note that will trigger the chain. This is useful in conjunction with insert_chain used on RackDevices that are Drum Racks, since by default they will be created with the In Note set to "All Notes,” encoded by -1.

**Performance**

- Improved the speed of adding a new track to a Set in cases where a default audio or MIDI track is configured.
- On certain Windows laptops running under power-savings modes, the CPU meter's behavior will now be less erratic and dropouts less likely. However, it is recommended to run Live with the best performance power plans and with no CPU frequency scaling.

**Setup**

- A different installer technology is now used on Windows, which makes the installation and uninstallation of Live significantly faster. The installer’s interface looks slightly different, but its functionality remains the same as before. Additional improvements include: The new installer can now replace any existing Live installation going back to Live 10. When selecting an installation folder that already contains Live, the installer will offer to uninstall the existing version and replace it with the new one. Previously, this was only possible if the existing version was the same edition and version as the new one. It is now possible to install Live into a folder that already contains files. In this case, the installer displays a warning and asks for confirmation. Previously, installation into a non-empty folder was not possible. Note that installing into a non-empty folder may overwrite existing files. When uninstalling Live, all files in the installation folder are removed, including those that were present before the installation.
- The Ableton USB Windows Audio Driver for Push and Move has been updated to version 5.72.0.
- The Visual C++ distributable has been updated in order for Live’s auto-update functionality to work properly. Follow the prompt in Live’s Status Bar to update it.

### Bugfixes

**Live Bugfixes**

- Fixed an issue where a MIDI track's soloed state would not be preserved when bouncing the track in place.
- The UI of VST3 plug-ins will now animate more smoothly when changing plug-in parameters.
- Reduced Live's CPU load when nudging clips within a Set with many (i.e., several hundred) locators.
- Preset changes for some plug-ins with a large number of parameters will now occur noticeably faster on some platforms.
- Fixed an issue where Live would hang when recording a large number of automation events.
- Fixed a crash in Live that occurred when instantiating some plug-ins, including SoundBetter’s Halo Effect, if Push 2 was connected.
- Fixed an issue that occurred in plug-in sliders, where it was impossible to set a slider to the minimum or maximum value in some circumstances.
- Fixed a bug that caused Live to hang when recording dense MIDI CC.
- Fixed an issue that caused visual glitches to appear when changing VST3 parameters from the plug-in’s UI.
- Fixed MIDI program change for some VST3 plug-ins, including Korg M1, Sylenth1, and Viper.
- Fixed an issue with incorrect labels in Analog's Glide Time mode.
- Fixed an issue where the Quick Tags view would sometimes obscure items in the content pane.
- Fixed a bug where Expression Control's curve controls would not work until switching from the Velocity tab to a different tab.
- Adjusted the way Live plays back tempo automation ramps and curves to be more mathematically accurate. Previously, ramps with increasing tempo were played slightly too slow and ramps with decreasing tempo were played slightly too fast.
- Clicking on the clip title bar in the Clip View now fully scrolls Arrangement clips into view as expected, zooming out if necessary. When multiple clips are selected, all clips are scrolled into view. Previously, only the time selection start was scrolled into view.
- Fixed an issue where the volume for Group Tracks would not appear after clicking the Optimize Arrangement Height toggle. Folded Group Tracks in the Arrangement View are now taller so that the volume controls are visible again.
- Fixed an issue that occurred when using the Bounce to New Track command on a part of a clip from a frozen Group Track, where the entire bounced clip was muted instead of only the time range that was bounced, while at the same time the UI indicated that only the bounced region was muted.
- Fixed an issue where the mixer or device parameters would sometimes briefly show a wrong value when adding or bouncing a track, or loading a Set.
- Fixed a crash that occurred when discarding unsaved changes in the File Manager.
- Live will no longer crash when using the ASIO driver for audio interfaces with an odd number of output audio channels, e.g., 3 or 9 channels.
- On Windows, added support for odd-numbered input and output channels. Previously, opening a device that used an odd-numbered channel would fail.
- Fixed a crash that occurred when viewing the browser history after restoring a Set with exactly two undo steps.
- Fixed a bug in the Komplete Kontrol S Mk3 Control Surface that could cause delays when renaming tracks and devices.
- The Komplete Kontrol S Mk3 Control Surface no longer shows device-related information in Live's Status Bar.
- Fixed a crash that could occur when calling duplicate_clip_to_arrangement on a track in the Max for Live API.
- On Windows, Live no longer hangs while working with certain videos.
- When in automation mode, take lanes can now be inserted and made visible from the tracks header context menu. When these entries are selected, the automation mode is closed in order to show the take lanes.
- Fixed an issue where crossfades would be reset after dragging and dropping a clip.
- When soloing a track, track activators for Group Tracks are now grayed out like other track activators, as expected.
- Fixed an issue where the "Reset Fades" command was disabled for clips with no fades.
- Reduced the spacing between the track index number and track name in default track names.
- The GPU renderer on Windows will now perform much better with curves such as MPE curves in the MIDI Note Editor, allocating a lot less memory. The changes should also reduce the likelihood of audio glitches that could occur because of the GPU renderer.
- Accessibility fixes: Live no longer crashes when navigating the transport bar using VoiceOver. Cleaned up the contents of the Control Bar for screen reader users. Improved the way Live's sample rate indicator reports itself to screen readers.
- On Windows, Live will no longer crash with NVDA or Narrator screen readers when the browser or File Manager is shown or has its elements expanded.
- Fixed an issue where Live would hang when bouncing a track that contained samples with high sample rates.
- Fixed a crash that could occur during multi-clip editing when right-clicking a note in a background clip if there were no notes of the same pitch in the foreground clip.
- Fixed a crash that could occur when capturing MIDI into the Arrangement if existing clips were overwritten during the process.
- Fixed a bug where automatically generated files might not have adhered to the file path length limitation on Windows.
- Fixed a bug in Hybrid Reverb where the previous reverb tail was still audible after the device was turned off and then back on.
- Fixed an issue where focus was lost after closing certain views, such as the Undo History or File Manager in the Help View. Now, when one of these views is closed, focus returns to the visible main view (Arrangement or Session) as expected.
- The context menu options "Set 1.1.1 Here" and "Warp from Here" are no longer shown for the rightmost edge of a clip.
- Fixed minor timing issues that could occur when recording or bouncing clips with tempo automation.
- Fixed a crash that occurred when duplicating scenes by holding Alt (Win) / Option (Mac) and dragging them above other scenes.
- Fixed a bug on macOS that could cause Live to hang indefinitely in certain scenarios.
- Fixed a bug where duplicating multiple scenes with linked scene follow actions resulted in some of the follow actions to not be triggered as expected.
- Fixed a bug in the Komplete Kontrol S Mk3 Control Surface script that caused some pitch-related parameters to be too sensitive.
- Fixed a bug in the APC64 Control Surface script that could result in a crash when hot-swapping devices via Push.
- Fixed a bug in the Move Control Surface script that incorrectly allowed the loop menu to be accessed for audio tracks.
- Fixed a bug in the Move Control Surface script that caused step durations to be displayed incorrectly when a triplet step grid was used.
- Fixed a crash that occurred when dragging Group Tracks from the browser into a Set.
- Fixed a crash that occurred when pressing Enter with two or more selected scenes.
- Fixed a crash that could occur when clicking on specific sample references in the File Manager.
- Fixed an issue where latency would not be correctly compensated in bounced audio when using plug-ins that have a dedicated latency for offline processing.
- Fixed a bug that caused sidechaining to fail when exporting audio if the sidechain source was a Group Track and the “Include Master and Return Effects” option was enabled.
- Fixed a crash that occurred when dragging files into the Arrangement.

**Max for Live Bugfixes**

- Clip IDs accessed by Max patches will now remain stable when clips are moved in the Arrangement View.
- Fixed the following issues in Max for Live: Sending getid to a live.remote~ or live.modulate~ now returns 0 if the last mapping failed. Fixed errors that occurred when undoing or redoing operations such as duplication of a Max device with a remote~ or modulate~ that has been mapped to a parameter.
- Fixed an issue where bouncing a track involving Max for Live Modulators would not work correctly if the Modulator was mapped to a device in the bounced track but was located on a different track.
Note: When saving a Set in Live 12.3 that was created in an earlier version, you will be prompted to save it under a new name.

## 12.2.7 (November 12, 2025)

### New Features and Improvements

- On Windows, Live will no longer crash with NVDA or Narrator screen readers when the browser or File Manager is shown or has its elements expanded.
- Fixed an issue where macOS machines would not connect to Push 2 or 3 in some cases.
- Updated Max 9.0.8 to build 82d284e: amxd~: unnecessary directories are not created on export array.change / dict comparison objects: unordered mode matching non-matching atom arrays array.fill: fix hang when incoming array is empty Audio Driver: fixed audio prefs for Thread Priority and Latency (Windows) Audio Drivers: Fix potential crash on launch due to ad_mme bug (Windows) chooser: fixed crash when cmd-dragging curve~ / line~: fixed issues when used in pfft~ Define: improved functionality with v8 / arguments jit.gl.texture: fixed shared context errors jweb: appropriately intercepts keys when it has focus live.banks: notify when parameter mappings change MIDI: improved behavior of port filtering / disambiguation midiin: unsupported MIDI RT messages are output numbox: fixed parameter usage Patching: fixed potential crash with deletion of outlets Projects: fixed issues with resolving file paths with localized files textedit: fixed crash with single quote character Timing: fixed ITM parsing not to be fooled by symbols containing the letter 'n' UI Objects Value Popup: fixed potential crashes v8: fixed crash with max.frontpatcher when Max is in the background v8: load/free performance optimizations v8: notifyclients() notifies on the object (not the box)

## 12.2.6 (October 14, 2025)

### New Features and Improvements

- Added Control Surface support for Akai MPK mini IV.

## 12.2.5 (August 27, 2025)

### New Features and Improvements

**Control Surfaces**

- Added control surface support for the Novation Launch Control XL 3.
- Improved device navigation in newer control surfaces (such as APC64 and Move) in order to better account for device selections made in Live.
- Updated the Komplete Kontrol S MK3 Control Surface: Track meters are displayed using the track's color. Encoders can fine-tune parameter values while Shift is held. The tempo can be controlled in Tempo mode (accessed via Shift + Metro). Devices can be selected, controlled, and viewed in Plugin mode.

**Interface**

- Updated various software text translations in French, German, Italian, Japanese, Spanish, and Simplified Chinese.
- Updated software text in various areas of Live.
- The following Kilohearts plug-ins are now shown as MPE-compatible: Phase Plant, Mulitpass, and Snap Heap.
- On Windows, the GPU renderer now displays icons more quickly, improving the responsiveness in the browser, mixer, and Session views when expanded to a large size.

**Move Control Surface**

- When using Move in Control Live Mode, the parameter mappings of Auto Filter are now consistent with Standalone Mode.

### Bugfixes

**Live Bugfixes**

- Fixed an issue where the content of the Clip View's editor would disappear when zooming in a non-playing clip with the + or - keys while Follow mode was active.
- Fixed a cut-off label that appeared in the Record, Warp & Launch Settings when using Live in French.
- Fixed a bug that caused an offset at the start of the recording when resampling audio.
- Fixed a crash that occurred when moving the insert marker with arrow keys while dragging a breakpoint with the mouse at the same time.
- Fixed an issue where the color entries were missing from the Arrangement clip context menu after renaming a clip.
- Sample rate, bit depth, and channel count are now displayed in the Clip View when multiple audio clips are selected, as expected.
- Fixed an issue where Collision's noise generator would randomly skip MIDI notes during playback when switching between Noise and Mallet.
- Fixed a bug where Analog would sometimes skip first note with the buffer size set to 32 samples.
- Live now correctly updates the color of the waveform in the Clip View when muting and unmuting an audio clip.
- Fixed a bug where Arrangement clips starting at 1.1.1 would sometimes fail to send a program change when starting playback immediately after loading a Set.
- Fixed MIDI program change for some VST3 plug-ins, including Korg M1, Sylenth1, and Viper.
- Fixed a crash that occurred while playing back audio clips.
- Fixed a bug where bouncing to a new track was not disabled when the Arrangement time selection contained only take lane clips.
- Tracks with a selection only containing take lane clips or muted Arrangement clips are now ignored when bouncing to a new track. Before this fix, this would have created empty tracks without any clips.
- Fixed a crash that occurred when zooming the Arrangement View via the Python API while renaming a locator.
- When Live is synced to a MIDI clock leader, the latency between the leader and Live is reduced and no longer changes with the tempo. While the fix results in a more stable latency, it may change timing in old Sets where Live was synced to an external MIDI clock source, so the -UseLegacyExtMidiClockIncrement option can be added to the Options.txt file to revert to the original behavior.
- Fixed an issue that occurred when bouncing a track with a delay or reverb effect, where the resulting effect tail clip of a clip that was followed by a muted clip before the bounce would have an incorrect length and and an incorrect name.
- Fixed an issue that occurred if an effect tails clip was overlapping a muted clip, where the tail clip would be split at the border of the muted clip. Fixed a bug where, in muted clips, a bounced clip and effect tail clip would be created if the track had a generator-like effect such as Vinyl Distortion.
- Fixed a crash that occurred when opening .ablbundle files when no User Library was configured.
- Fixed an issue in Drift where enabling the Mono and Oscillator Retrigger modes in Drift then playing a note and holding it while pressing another note would not change the pitch of the oscillators.
- Fixed a bug in Auto Filter where a new value for the SC Gain parameter value was not correctly saved when saving the changes as a new default preset.
- The LFO step quantizer in Auto Filter will now correctly take into account the LFO Phase and LFO Phase Offset parameter values when the values are changed during playback.
- Fixed a crash on macOS that occurred when attempting to open a Set with a removed alias file.
- Fixed a bug where the first file would be overwritten when exporting two tracks with the same name but different capitalization when using the Selected Tracks Only export option.
- Fixed an issue that caused graphical artifacts with automation curves that used a large number of breakpoints.
- Plug-in scanning and browser indexing is now faster on Windows.
- Fixed a crash that occurred when dragging corrupt MIDI files into Live.
- Fixed a crash that occurred when loading a Set containing MP3 files if the set cache folder was missing.
- When loading a Move or Note Set in Live, the Melodic Sampler instrument is converted to Simpler with the expected number of voices.
- Capture will no longer clear its buffer when notes are played over a playing clip and the transport is stopped. Previously, the buffer could be unintentionally cleared in some cases.
- Fixed a bug where changes to playing session clips were not reflected if the take lane audition switch was enabled for that track.
- On Windows, the GPU renderer no longer causes unexpected pauses longer than 100ms in certain scenarios, such as when displaying all automation envelopes in the Arrangement view.

**Push Bugfixes**

- Added a speculative fix for an issue that prevented Push 2 from starting after updating to Live 12.2 on Windows.

## 12.2.2 (August 13, 2025)

### New Features and Improvements

- Updated the Komplete Kontrol S MK3 Control Surface: Track meters are displayed using the track's color. Encoders can fine-tune parameter values while Shift is held. The tempo can be controlled in Tempo mode (accessed via Shift + Metro). Devices can be selected, controlled, and viewed in Plugin mode.
- Improved device navigation in newer control surfaces (such as APC64 and Move) in order to better account for device selections made in Live.

## 12.2.1 (June 19, 2025)

### New Features and Improvements

- Added Control Surface support for Novation Launch Control XL 3.
- When using Move in Control Live Mode, the parameter mappings of Auto Filter are now consistent with Standalone Mode.

## 12.2 (June 11, 2025)

### New Features and Improvements

### Auto Filter Updates

Auto Filter has been redesigned, both in terms of the UI and sound.

The new device layout emphasizes key parameters and features improved visualizations. Filter frequency modulation is now displayed separately for the left and right channels. Additionally, a real-time signal spectrum for the output has been added to visualize how the parameters affect the output.

**New Filter Types**

Several new creative filter types have been added:

- The DJ filter controls both a low-pass and a high-pass filter with a single parameter, similar to certain DJ mixers. Values above zero filter out low frequencies and emphasize high frequencies, while values below zero filter out high frequencies and emphasize low frequencies.
- The Comb filter produces flanging effects, especially when modulated.
- The Vowel filter shapes the sound to resemble the human voice by emphasizing formants.
- The Morph filter now features four different slopes. Furthermore, it is now possible to morph between low-pass and high-pass filtering, with band-pass in between.
- A Resampling filter and a Notch + LP filter complete the new additions.

**Updated Filter Circuits**

The available filter circuits have changed:

- SVF functions as a linear/clean filter, but can also introduce distortion if Drive is set above zero.
- DFM is a new filter circuit that internally feeds back more of its distortion, resulting in a broad range of tones from subtle filter sweeps to warm drive.
- MS2 uses a Sallen-Key design and soft clipping to limit resonance. It is modeled on the filters used in a famous semi-modular Japanese monosynth.
- PRD uses a ladder design and has no explicit resonance limiting. It is modeled on the filters used in a legacy dual-oscillator monosynth from the United States.

**Modulation Improvements**

- The list of available LFO shapes has been extended to include: Wander, Ramp Up, and Ramp Down.
- LFO Morph transforms and tilts the LFO shape in various ways.
- The S&H shape now has a dedicated smoothing parameter.
- LFO quantization can be applied in one of two modes: In Steps mode, the LFO modulation only updates at specific intervals, which are defined by the current LFO speed divided by the selected number of steps. In S&H mode, the LFO only updates based on the selected S&H beat time.
- In the Envelope Follower, the Envelope Attack Hold parameter ensures the envelope completes its full attack phase, even if the input signal consists only of short transients.
- The sidechain signal can be summed to mono via the Mono Sidechain option in the device title bar’s context menu.
- An EQ has been added to the sidechain section.

**Improved Signal Flow**

- A dedicated Output control allows you to compensate for increases in loudness, which is useful when using high Drive values.
- Enabling the Clip toggle applies soft clipping to ensure the output signal does not exceed 0 dB, which is especially useful when using high resonance and Drive values.
- The Dry/Wet control lets you balance the dry and processed signals.

### Automation and Modulation Keyboard Workflow

You can now add, edit, and delete automation breakpoints using a new keyboard workflow. Breakpoints can be selected one at a time, making it possible to move between them and make edits using the keyboard or mouse. Screen reader announcements provide feedback for each action.

**Navigation**

- Select the current breakpoint: Enter on a breakpoint
- Create and select a new breakpoint: Enter without selecting a breakpoint
- Move the insert marker along the grid: left and right arrow keys
- Jump to the previous/next breakpoint: Alt (Win) / Option (Mac) + left and right arrow keys
- Select an existing breakpoint at the insert marker: Enter
- Restore highlight of the previously moved breakpoint: Undo

**Editing Selected Breakpoints**

- Move the breakpoint in time/value: arrow keys
- Delete the breakpoint: Delete
- Edit the value: start typing
- Commit the change and deselect: Enter
- Cancel the change and deselect: Escape
- Select the next/previous breakpoint: Tab and Shift Tab

**Mouse Selection**

- Select a breakpoint and move the insert marker: Alt (Win) / Option (Mac) + click

**Changing Envelopes in Arrangement View**

- Cycle through automated parameters of all devices on a track: Alt (Win) / Option (Mac) + up and down arrow keys
- Cycle through all parameters of all devices on a track: Shift Alt (Win) / Shift Option (Mac) + up and down arrow keys

### Bounce Tracks to Audio

Two new commands for bouncing tracks have been added: Bounce Track in Place and Bounce to New Track. You can use Bounce Track in Place to render entire tracks as new audio tracks, and Bounce to New Track to render the time selection of a track into a new audio clip on a separate track. Bouncing is performed pre-mixer and post-FX. This means the source track’s effects processing is included in the rendered audio.

- The Bounce Track in Place command is available in the track title bar and clip context menus. The Bounce to New Track command is available in the clip context menu, as well as via the shortcut Ctrl B (Win) / Cmd B (Mac).
- When bouncing to a new track, the rendered audio clips are added to a separate track beneath the source track. After bouncing, the source clips are muted so that there is no doubled output.
- The Freeze and Flatten Track command and the Flatten command for frozen tracks have been renamed to Bounce Track in Place.
- Bounced files are stored in a new Samples/Processed/Bounce folder within the Project folder.

### Browser Improvements

**Filter View Redesign**

The browser's Filter View has been redesigned to better accommodate the recently added filtering and tagging features:

- The Filters title bar has been removed and replaced by a new toggle to the right of the search bar, which can be used to show or hide the Filter View.
- Added a Filter View Menu drop-down next to the Show/Hide Filter View toggle. This menu includes options to show or hide filter groups and the Tag Editor, enable auto tags, and open or close the new Quick Tags panel.
- The Browse Back and Browse Forward icons have been slightly updated.

**Browser Content Columns**

The Content Options menu in the content pane adds some new display options:

- You can customize which content columns are displayed, as well as reorder them in the content pane by dragging.
- The content list can be sorted by clicking on the column header.
- The new Show File Extensions option lets you show or hide all file extensions.

**Quick Tags**

The new Quick Tags panel, located above the Preview tab, lets you view assigned tags, as well as add or remove tags for selected browser items.

- User-created tags and auto tags include an X icon, which you can click to remove the tag from the selected item. Note that factory tags cannot be removed or edited.
- When multiple items are selected, any tags which are not assigned to all of the selected items are displayed with an asterisk.
- Double-clicking a tag in the Quick Tags panel opens the corresponding tag in the Tag Editor.
- Use the shortcut Ctrl E (Win) / Cmd E (Mac) when the browser is in focus to go directly to the Add… field of the Quick Tags panel.
- The Quick Tags panel is displayed by default but can be hidden via the Show Quick Tags option in the Filter View Menu.

**Custom Icons**

It is now possible to assign custom icons to any label in Library, as well as any user folder in Places:

- Right-click on a label to choose a new icon from the predefined list of custom icons.
- Reset to the default icon by choosing “Default Icon.”
Note that it is not possible to update the icons for the Packs, Cloud, Push, User Library, and Current Project labels.

**Search Bar Improvements**

- The design of the tag suggestion popover that appears when searching for tags has been refined.

**Results Bar Improvements**

- The Results bar now displays the number of selected filters.
- The Clear Filters and Add Label icons have been updated.

**New Filters**

- The Content filter group now has a new MIDI Tool filter.
- Added a new filter group called MIDI Tools that contains Generator, Transformation, and Stacks filters.
- When filtering in the All label, presets are now grouped into their device folders.

### Device Improvements

**Meld**

Added a new Chord oscillator type, which is comprised of four sawtooth oscillators that play a variety of chords. When the Use Current Scale toggle is enabled in the device title bar, generated chords use the notes of the set scale. If no scale is set, a major scale is used with the incoming MIDI note as the root.

Added a new Scrambler LFO 1 FX, which permutes four different amplitude ranges of the input modulator.

**Roar**

- Added a new Delay routing mode. In this mode, the second stage processes the delayed signal from Stage 1. Unlike the Feedback routing mode, the delayed signal is sent to the second stage without being scaled by the feedback gain. This creates single (distorted) repetitions or slapbacks. The output of Stage 2 is fed back into itself and scaled with the feedback gain, enabling multiple repetitions and long signal tails. The Blend control can be used to mix between the output of Stage 1 and Stage 2.
- Added a new Dispersion filter type. This filter distorts the signal's phase in a frequency-dependent manner. This can lead to interesting metallic, spring-like artifacts, especially when modulated.
- Added an external sidechain that can be used to feed the envelope follower modulation source with signals from other chains or tracks.
- Added a MIDI sidechain that can be used to control the pitch of the feedback in Note mode.
- An Envelope Hold toggle is now available in the Envelope section. It ensures that the envelope completes its entire attack phase before entering the release phase.
- Modulation signals are now visualized using LEDs in the Modulation column. This helps identify how modulation sources are set up and whether they are active in any modulation routing—without needing to dive into the Modulation Matrix.
- Enabling the MIDI > FB Note toggle now leads to MIDI input changing the pitch of the device's feedback irrespective of the Feedback Time Mode setting, making it easier to use Roar's MIDI sidechain feature.

**Resonators**

- The Resonators device now supports scale awareness, which you can enable via the Use Current Scale toggle in the device title bar. When enabled, the Note and Pitch controls can be transposed in scale degrees.
- The Resonators device also now supports tuning systems. When a tuning system is loaded, the resonators' pitches can be adjusted based on the tuning's set of pitches, and the Note and Pitch controls use integers rather than note names or semitones.

**Spectral Resonator**

- The Spectral Resonator device now supports scale awareness, which you can enable via the Use Current Scale toggle in the device title bar. When enabled, the Frequency control can be adjusted in scale degrees when using MIDI note values. When using MIDI Mode, the Transpose control can be set in scale degrees. You can also quantize the resonator's harmonics to the scale by enabling the Quantize option above the Spectrogram.
- The Spectral Resonator device also now supports tuning systems. When a tuning system is loaded, the Frequency control is set to the tuning's root note when using MIDI note values. Additionally, the control uses integers and not note names or scale degrees. As with scale awareness, you can enable the Quantize option to quantize the resonator's harmonics to the tuning's pitches.

**Operator**

- Operator now supports a maximum voice count of 32 voices.

**Device Header Improvements**

- The triangle toggle used for expanding a device’s sidechain settings or breakout view is now only used for sidechain settings. A new arrow toggle is used for devices with a breakout view.
- The sidechain toggle has been moved to the left side of the device and now includes its own header for increased visibility. This change affects the Auto Filter, Compressor, Corpus, Gate, Glue Compressor, Multiband Dynamics, and Shifter devices. Additionally, the Sidechain Filter in Compressor is now accessible in its own panel.
- The context menu options for all devices are now accessible via a dedicated button in the device title bar; previously, these options were only available through right-clicking.

**Additional Device Improvements**

- The Sample Start and End markers are now preserved when converting Simpler to Drum Sampler.
- In Drum Sampler, added the Envelope Follows Pitch option to the device title bar context menu. This option is enabled by default and ensures that the timing of the envelope follows the re-pitching of the sample so that the same portion of the sample is always played regardless of transposition changes.
- In Drum Sampler, the Hold parameter in Trigger mode now uses Inf as the maximum value, which plays the sample for its complete length.
- You can now enable Hi-Quality mode for Drift by selecting the option from the context menu in the device title bar.
- Updated the Core Library: A new default preset is now used for Auto Filter. Added a new selection of Auto Filter presets. Auto Filter Legacy presets are now saved in: Core Library/Devices/Audio Effects/Legacy/Auto Filter Legacy A new default preset is now used for Roar that has Envelope Hold enabled. Corrected the tuning for the Upright Bass.adv preset. Fixed the tuning for the Fretless Bass.adv preset. Fixed some small typos in Audio Effect Racks presets. Added new Meld presets that feature the Chord oscillator. The Drum Sampler default preset and Drum Rack presets that use Drum Sampler now have Envelope Follows Pitch on by default.

### Max for Live Improvements

- Max for Live devices now feature an Edit in Max option in the device title bar context menu. This option replaces the functionality of the Edit button, which has been removed and replaced with an icon that signifies the device is a Max for Live device. You can restore the Edit button functionality by adding the -MaxForLiveDeveloperMode option to the Options.txt file.
- Updated the bundled Max version to the 9.0.7 official release build. Please see the Max 9.0.7 Release Notes for more details. The following Max for Live changes from Max 9.0.6 are also now available: jspainter: live.button/menu/tab/toggle mapping overlay works live.menu: popup menu icon drawing improvements live.push: attributes work properly if no push is connected live.text: button roundness matches Live appearance Max Console: fixed potential crash in the context of Max for Live Max for Live Parameter context menu: scales with Live UI scaling Max for Live: fixed MIDI keyboard handling when device has focus Max for Live: fixed potential crash when Max application is shut down Max for Live: fixed potential crash with undo/redo stack when deleting device Max for Live: Max's global zoom preference is not used inside Live phasor~ in Max for Live: improved transport sync v8: improved fix for LiveAPI observer callback issues The Clip.start_time property is now observable in the Max for Live API. Max for Live can now access a device parameter's display_value through the LOM. Other than the existing value property, the display_value refers to the parameter's value as visible in the user interface.
- It is now possible to access a take lane's name through Max for Live.
- Take lanes can now be created through Max for Live.
- Clips in Take Lanes can now be accessed via the Max for Live API. Additionally, the create_audio_clip and create_midi_clip functions have been added to the API, making it possible to add clips to Take Lanes.

### Arrangement View Improvements

- Track headers now display a Show/Hide Take Lanes button when more than one take has been recorded on a given track or after choosing Insert Take Lane from a track’s context menu. Note that in order to access the Show/Hide Take Lanes button, Automation Mode needs to be disabled and tracks need to be unfolded.
- Right-clicking on a track or take lane header now displays context menu options to: Delete All Take Lanes Delete Unused Take Lanes (i.e., take lanes containing clips that are not audible on the track’s main lane)
- Adjusting the size of the browser or the application window now zooms the contents of the Arrangement View instead of pushing it outside of the visible area.
- Group Tracks with many nested tracks now take up less space in Arrangement View. The overview shown for Group Tracks is no longer fixed in size, but now zooms depending on the Group Track’s size. Also, clips from tracks in nested sub-groups are no longer shown as individual lanes on the parent group, but are aggregated into a single lane per sub-group.
- The Add Automation Lane button is now hidden when a parameter already has an existing automation lane. This means the automation for a given parameter is no longer shown more than once in the Arrangement View. Selecting Show Automation or Show Automation in New Lane from the context menu of a device parameter now focuses the corresponding automation lane.

### Session View Improvements

- Scene Follow Actions can now be toggled between Unlinked and Longest. When set to Longest, the Follow Action is triggered at the end of the longest clip in the scene or after that clip has played the number of loops defined by the Follow Action Multiplier. When set to Unlinked, the Follow Action is triggered after the scene has played for the duration specified by the Follow Action Time.
- A linked scene follow action now displays the longest clip's loop length next to the multiplier. In case the longest clip is unlooped, "Clip End" is displayed to indicate that the action will be triggered once that clip reaches its end.

### Move Control Surface Updates

- In Note Mode, the playback position of the longest playing full-bar clip is now displayed when the transport is running and an empty clip is selected.
- A notification is now shown when steps are transposed.
- The LED feedback in loop mode is now consistent with Move standalone.
- The parameter mappings for Drift, Simpler, and Drum Sampler are now consistent with Move standalone.
- The auto-arming behavior is now more consistent with Push.
- Detail View is now always shown when steps are held down. Additionally, Detail View is always shown when navigating devices.
- When switching to the Note Mode, the selected track will now be auto-armed and, where applicable, other tracks will be disarmed.
- Mute-related LEDs now indicate when tracks and drum pads have been muted via solo.
- Shift + Mute can now be used for soloing tracks and drum pads.
- Shift + Step 16 can now be used for quantizing drum pad notes.
- Steps can now be nudged finely while Shift is held.
- It is now possible to select a 4ths or Octaves layout for scales.
- When using Note Repeat, there should no longer be a dip in velocity shortly after a note is pressed.
- Modifier screens are now more responsive.
- Fixed a bug that caused momentary track muting to not complete correctly after releasing Mute.
- Fixed an issue where using modifiers (such as Mute) quickly could result in undesired actions being triggered.
- Fixed a bug where the scale and root note menus would not be initialized correctly when loading a set.
- Fixed a bug where some scales would not use all of the pad columns.

### Third-Party Control Surface Improvements

- Added control surface support for the Akai MPK Mini Plus.
- The arming behavior in newer control surfaces (such as the ones for the APC64 and Move) is now more consistent with the behavior in the Push control surface.
- When using the Launchkey MK3 and MK4 control surfaces, it is now possible to navigate between groups of eight tracks using the Track Left and Right buttons while Shift is held down. The first track in the group will also be selected.
- In newer control surfaces (such as the ones for the APC64 and Move), mute-related LEDs now indicate when tracks and drum pads have been muted via solo.
- In the Komplete Kontrol S Mk3 Control Surface, the play button now toggles playback.
- The play button of the Launchkey_MK3 and Launchkey_Mini_MK3 Control Surfaces no longer resets song time.
- In newer Control Surfaces (such as APC64), mute-related LEDs will now indicate when tracks and drum pads have been muted via solo. Additionally, the auto-arming behavior of newer Control Surfaces is now more consistent with Push.
- Detail View is now always shown when steps are held down via the Launchkey MK4, and Launchkey Mini MK4 Control Surfaces.
- The arm icon in the display of the KeyLab_mk3 Control Surface now uses different shades to better distinguish a track’s arm state.
- With the Launchkey_MK3 and Launchkey_MK4 Control Surfaces, it is now possible to navigate between groups of eight tracks with the Track Left and Right buttons while Shift is held down. The first track in the group will also be selected.
- Fixed a crash that could occur when triggering "Slice to Drum Rack" while using the APC64 Control Surface.
- Fixed a crash that could occur when triggering "Slice to Drum Rack" while using the Launchkey MK4 Control Surface.
- Fixed a bug in the KeyLab Essential mk3 Control Surface where only one bank of parameters would be available for plug-ins regardless of how many parameters were configured.

### Additional Improvements

- On Windows, you can now enable a hardware-accelerated GPU renderer to significantly improve Live’s UI performance. This option is disabled by default but can be enabled in the Display & Input section of Live's Settings.
- Live will now use less memory when loading large Sets.
- Selecting a tag from the auto-completion suggestions now works also when selecting the tag with the arrow keys.
- In the Transformation/Generator Selector, added an indicator that shows which of the MIDI Tools have been applied.
- It is now possible to specify the min and max values for enum parameters when they are remote controlled via macro or MIDI-mapping.
- It is now possible to select multiple notes in the MIDI Note Editor by holding Shift, pressing and holding the mouse button over a selected note, and then dragging the mouse over any other notes you want to select.
- Improved performance when opening .ablbundle files (from Move or Note) in Live, or when expanding them in Live's browser. In addition, if an .ablbundle contains audio files that have already been downloaded for Sets stored in Ableton Cloud, those files will be reused.
- The range of the Brightness parameter in the Themes and Colors Settings has been increased for all colors that make up a theme's background, whereas most chromatic colors (clip/track colors, button states, etc.) are now prevented from being affected.
- Live now supports setting MIDI program change events in VST3 plug-ins.
- A message is now displayed in Settings if the GPU cannot be toggled on or off, for example because the graphics card is not supported graphics card or the GPU renderer is forced on or off with an entry in the Options.txt file.
- Updated the What's New in Live lesson to include features from Live 12.2.
- Updated software text in various areas of Live.
- Updated various software text translations in French, German, Italian, Japanese, Simplified Chinese, and Spanish.

### Bugfixes

- When editing Stacks' parameters and chord patterns when the MIDI Tool is inactive (e.g. when the MIDI Note Editor is in the Envelopes view mode), the chord pattern diagram is now updated as expected.
- Fixed the following bugs in Arpeggiator: Fixed an issue where a groove was not applied when Gate was set to values above 75% and below 100%. Fixed a bug where the pattern would skip or repeat notes when the Arrangement timeline was looped.
- Accessibility: Restored the ability to extend selection to notes of the same pitch using the Ctrl (Win) / Option (Mac) + left or right arrow keys with a note selection in the MIDI Note Editor.
- Sets that contain unknown scale names now load as expected. Unknown scales are reset to a default major scale in the process.
- Fixed an issue that caused note dropouts if only one note was present in a clip when using the DS Clap instrument.
- Fixed an issue that caused occasional note dropouts when using the DS HH instrument.
- Copying a folder in the browser by dragging and dropping it while holding Alt (Win) / Option (Mac) now works as expected.
- The IR envelope in Hybrid Reverb now decays as expected.
- Fixed an issue where the name of a tuning system would get cut off when saved if it included a dash followed by a number in the middle of the name, e.g., Tuning-3System.
- Phaser-Flanger and Redux will now use less CPU when silent.
- A newly loaded Wavetable device with Retrigger set to off will now have LFOs synced to the transport.
- With Retrigger set to off, Wavetable's free LFOs will sound the same when restarting the transport at any point in the Set.
- Fixed a crash that occurred when navigating the Tags Editor with the arrow keys.
- The New Folder option is no longer shown in the context menu when the browser is showing a flat search result list.
- On Windows, improved the speed of plug-in scanning and the browser indexer.
- Fixed a bug in Auto Shift where MIDI modulation was active even when the MIDI input was disabled.
- Removed non-functional options in the Push and Cloud labels' context menus.
- Removed the Browser File Preview option from the Push label.
- When pressing Ctrl F (Win) / Cmd F (Mac) and then Esc , the focus will now move back to the content pane as expected.
- Fixed an issue that occurred when hot-swapping on loaded presets, where the browser would always jump to the top of the list.
- MPE Control no longer stops outputting MIDI when continuously automating the curve min/max settings.
- Fixed an issue where the browser's search bar would show "Start typing for tags" or a list of autocompletion suggestions even after the search bar was cleared.
- Roar's LFOs now progress continuously in Free rate mode when the device is reactivated, as expected.
- Accessibility: In Auto Shift, the keyboard navigation and screen reader are now always synchronized to ensure there are no accidental changes of the state of one element while another element is focused.
- The Stretch playback effect in Drum Sampler now sounds consistent across various sample rates.
- The play button behavior for the Launchkey MK3 and Launchkey Mini MK3 control surfaces no longer resets the song time.
- The arm icon in the display of the KeyLab MK3 control surface now uses different shades to better distinguish track arm states.
- Fixed a bug where the first file would be overwritten when exporting two tracks with the same name but different capitalization when using the Selected Tracks Only export option.
- Fixed a crash that could occur when triggering Slice to Drum Rack while using the APC64 control surface.
- Fixed an issue that caused graphical artifacts with automation curves that used a large number of breakpoints.
- Plug-in scanning and browser indexing is now faster on Windows.
- The following Kilohearts plug-ins are now shown as MPE-compatible: Phase Plant, Mulitpass, and Snap Heap.
- Fixed a crash that occurred when dragging corrupt MIDI files into Live.
- Fixed a crash that occurred when loading a Set containing MP3 files if the set cache folder was missing.
- Capture will no longer clear its buffer when notes are played over a playing clip and the transport is stopped. Previously, the buffer could be unintentionally cleared in some cases.
- Fixed a bug where changes to playing session clips were not reflected if the take lane audition switch was enabled for that track.
- Latency compensation now works more reliably when Push is in Control mode.
- Clicking on Find and Select toggles (such as the pitch toggles in the Pitch filter) no longer removes focus from the MIDI Note Editor.
- Fixed a bug where notes that were selected with the Pitch filter in Find and Select Notes were not retained when switching to another filter.
- In Drift, the waveform display now reacts to parameter changes as expected even when the device is inactive.
- Fixed a bug that caused ramps in MIDI CC automation to generate sequences of redundant messages (e.g., 0, 0, 0, 0, 0, 1, 1, 1, 1). Now each CC value will only output once unless multiple messages are manually added. As a result, it is now possible to draw more MIDI CC automation envelopes before reaching an external MIDI device’s maximum data rate.
- The width of the Main track in the default Live Set has been expanded so that the dB scale is shown on the mixer.
- Live now sets the allowed note range according to the maximum set by the NOTE_RANGE_BY_FREQUENCY directive in tuning systems (.ascl) files, so that the tuning system stops at the last note below or equal to the maximum frequency. Previously, it could stop one note too late.
- Fixed a regression that prevented certain non-monotonic tuning systems from using their full range.
- Accessibility: Fixed a bug where screen readers wouldn't properly report accidentals for the Transpose control in the Pitch and Time Utilities panel.
- Fixed a bug in Max for Live where sending getpath to a live.object that referenced a Push 2 or 3 control would result in an error.
- In Live Lite, it is now possible to access the Release Velocity lane in the MIDI Note Editor. Additionally, the menu shown for swapping lanes now only contains the relevant entries.
- Fixed a bug where launching or clicking the currently highlighted scene would stop showing the selected clip in Clip View and instead show a “No clip selected” message.
- Fixed a bug that caused Live to crash when clicking on Wavetable's waveform display if VoiceOver was enabled.
- Dragging tracks from the browser into a Set no longer causes the tracks’ send levels and automation to be reset. When copying and pasting or duplicating tracks, the send levels from the original tracks are also retained.
- Fixed a crash that occurred when pressing Enter on automation/modulation in Clip View after the action of moving a breakpoint with the keyboard was undone.
- When loading Sets created in Live 10 or earlier, MIDI clips no longer show Scale Mode as enabled in Clip View.
- Fixed an issue that caused duplicate note IDs to corrupt Live Sets.
- Fixed a crash that occurred when selecting No Color from a scene’s context menu in certain conditions. Additionally, the color menu would not be displayed as expected.
- Fixed an issue where Live would report that another instance of the software was running, and therefore a Live Set could not be recovered after a crash, even if only one instance of Live was running at the time.
- Fixed an issue where an incorrect track would become selected when clicking on an Arrangement clip while the Device View contained a device that had an expanded breakout view if the selected clip was not on a track that also contained a device with an expanded view.
- When an envelope is focused in Clip View’s Envelope Editor, using Ctrl (Win) or Option (Mac) with the up and down arrow keys cycles through all automated parameters. Adding Shift cycles through all parameters.
- Duplicating a large number of scenes is now faster.
- Fixed an issue where some items were hidden in the browser when hot-swapping.
- In Spectral Resonator, Granular mode now produces grains as soon as it is active, and grains will not always produce four sinusoids. This should make the sound more consistent across different modulation modes and between separate instances.
- Fixed a bug where the playhead visualization became stuck when using the Sub Osc playback effect type in Drum Sampler.
- When the song start time is set to the Arrangement loop start or a locator, the corresponding marker now appears in green.
- Fixed an issue that occurred when exporting audio for multiple tracks (including return and Main track effects), where the progress display text would start at "0 %" and go to "100 %" for every track that was rendered instead of showing the progress of the entire process.
- Expression Control now switches tabs immediately after the mouse is clicked.
- Fixed a bug in Compressor where the effect of the sidechain filter was not audible when the Sidechain Listen toggle was on.
- Using the Collect All and Save option will no longer copy already collected samples into a project again.
- Updated tags for some third-party Packs.
- Fixed a bug where, when overdubbing arrangement automation using the mouse, the second mouse click would start playing back the original automation instead of staying at the last recorded value.
- Fixed a bug that occurred in Find and Select Notes when filtering by Time, where it was impossible to reset the first parameter of the Repeat interval to the default value.
- Right-clicking on the device title bar will no longer select other devices in the chain.
- Similarity Swapping buttons are now disabled in Simpler and Drum Sampler while in Hot-Swap Mode.
- Addressed the following issues in the real-time rendering dialog: Fixed an issue where the dialog would be displayed when rendering audio for individual tracks of a Live Set that contains external effects or instruments, even though no tracks with external devices contributed to the exported tracks. Fixed a bug where the Restart button would disappear from the dialog when exporting more than two tracks with external devices and the option to include returns and Main effects was switched on in the dialogue.
- Fixed a crash that occurred when using the Quick Tags editor on Windows.
- Old Sets that include Saturator can now be loaded again without the "Document is corrupt" warning being displayed.
- Fixed an issue where Live could not read AIFF files larger than 2GB, although it could write such files.
- On Windows, fixed a crash that occurred on startup when trying to show an error message.
- Fixed an issue where a sample waveform would be generated slower than expected.
- When scrolling in the Arrangement View, it is now possible again to press Ctrl (Win) / Cmd (Mac) to switch to zooming without having to stop scrolling first.
- It is now possible again to copy and paste a full tag path and then press Enter to search by that tag.
- Fixed an issue with inconsistent fades when the Arrangement loop would coincide with a playing Session clip loop.
- Fixed a crash that occurred when trying to load a sample from the browser.
- Fixed a bug where Auto Shift produced sound that was louder than expected when the MIDI input was turned off while notes were still playing.
- The CPU meter now spikes less when nudging clips in Sets that contain many locators (e.g., several hundred).
- Fixed an issue that caused the source track to remain frozen when restarting the Bounce to New Track process for a track that included real-time devices.
- Fixed an issue where Live could hang during export when the Create Analysis File option was enabled in certain scenarios.
- Fixed a crash that occurred when moving tracks in the Arrangement View.
- The phase of partials in the Spectral Resonator device are now randomly distributed as expected, resulting in a more even sound when using unison and modulation.
- Fixed a bug in the Resonators device where using extreme pitch values in scale-aware mode could cause glitches or crashes.
- Fixed a crash that occurred when selecting Fixed Grid from the Options menu when an unwarped audio clip was selected in Arrangement View. Now, the Fixed Grid option is no longer available for unwarped clips.
Note that when saving a Set in Live 12.2, any Set created in an older version of Live must be saved with a new name.

## 12.1.11 (April 14, 2025)

### Bugfixes

- Fixed an issue that caused duplicate note IDs to corrupt Live Sets.
- Sets created in older Live versions (e.g., Live 6) that include Saturator can now be loaded without triggering a "Document is corrupt" warning.
- When using Note Repeat with Move in Control Live mode, there should no longer be a dip in velocity shortly after a note is pressed.

## 12.1.10 (February 25, 2025)

### New Features and Improvements

- Native devices, including built-in Max for Live devices, are now sorted before plugins in search results.
- Max for Live parameter objects with their @active attribute set to 0 are now greyed out on Push, much like parameters in native devices.
- Fixed the following issues in the browser: Fixed a bug where the auto-completion suggestion would not be updated as more characters were typed in. Fixed a bug that prevented tags containing a space from being auto-completed.
- When filtering, the number of selected filters will now be displayed above the content pane.
- Live will now start up slightly faster.
- The "Clear" button visible above the content pane when searching or filtering in the browser has been replaced with an "X" button.
- The "+" button used for saving a custom label has been replaced with a bookmark button.
- A new Track.create_midi_clip function is exposed in the Max for Live API allowing the user to create empty clips in the Arrangement View. The function accepts two arguments, both floats, which indicate the start time and length of the empty clip.
- Update Core Library for 12.1 to r60939: Updated tuning files. New presets added from Note and Move Core Libraries. Improved tags for Core Library content.

### Bugfixes

- Accessibility: Improved screen reader support and keyboard control in Auto Shift.
- Replaced the -inf value that represents negative infinity with the -∞ symbol.
- Fixed an issue where Live would temporarily freeze when entering the Hot-Swap mode in certain conditions.
- When playing high pitches, there is now less aliasing in Wavetable set to Hi-Quality mode.
- When editing parameters and chords in the Stacks MIDI Tool while it is inactive (e.g., when using the Envelopes editor mode), the chord pictogram now updates as expected.
- Fixed a performance regression that occurred when zooming into the Arrangement in a Set that contained many clips.
- Fixed a crash that occurred when browsing Max for Live devices on Push 1 or Push 2 while using the -Push2UseLegacyScript debug option.
- Accessibility: Fixed a crash that occurred when deleting a MIDI clip while a screen reader was in use and focused on the MIDI Note Editor.
- Fixed an issue where devices with automated parameter would sometimes produce silence on the output.
- Live now shows an error when attempting to load an empty tuning system file (.scl or .ascl) without pitches.
- Smoothing now works as expected for long times in Roar's LFO and Noise.
- Live no longer crashes when exporting the full duration of a video. If there is a failure while reading a video during export, Live will display a notification stating there was a problem with the export and the exported file may not work.
- Fixed a bug in Meld, where scale degree transpose parameters instead of the semitone transpose parameters were displayed on Push while a tuning system was loaded.
- In USB MIDI setups where there are multiple units of the same type of device there should now be no problems when routing to those devices, and MIDI routings should be correctly restored when unplugging and replugging the devices.
- Fixed an Indexer crash which occurred when analyzing certain corrupted or unsupported audio files.
- In Auto Shift, fixed a bug where MIDI modulation was active even when the MIDI input was disabled.
- Fixed an issue that made it impossible to dismiss dialog windows displayed by plugins while they were being loaded.
- Restored the Ctrl (Win) / Cmd (Mac) + up or down arrow keyboard shortcut, used for moving selected scenes.
- Fixed an issue where Velocity and Chance filter results in the MIDI Note Editor were incorrect when fine tuning the parameters.
- Live no longer crashes when loading a sample from the browser while the currently selected device chain includes a MIDI Effect Rack nested in an Instrument Rack.
- Fixed a crash that occurred when chopping notes with the Ctrl E (Win) / Cmd E (Mac) keyboard shortcut while editing multiple clips and clicking on a note in a background clip.
- Capture will no longer clear its buffer when notes are played over a playing clip and the transport is stopped. Previously, the buffer could be unintentionally cleared in some cases.
- Fixed an issue with the Pitch, Random, and Arpeggiator devices where per-note pitch bend messages were processed incorrectly when scale awareness was enabled and the incoming note was out of scale.

## 12.1.5 (December 12, 2024)

### New Features and Improvements

- Updated the design of the Hot-Swap Sample and Swap to Previous/Next Similar Sample buttons in Simpler and Drum Sampler.
- Drum Rack presets will no longer be excluded from the Sounds label. Additionally, Drum Rack and Drum Sampler presets tagged with "Sounds|..." will no longer be shown in the Drums label.
- Selecting a large number of track headers or tracks in the Session or Arrangement View is now faster.
- The Scale filter in Find and Select Notes is now available even if Scale Mode is turned off.
- Accessibility: Changed the Info View header for Help View's home button from "Lessons Start Page" to "View All Lessons" for an improved screen reader announcement.
- In Auto Shift, MPE pitch bend now uses a 48 semitones range.
- Items tagged with "Devices|Drums" will now be included in the Drums label as well.
- When browsing the All label, presets will once again be grouped into their respective devices. However, the grouping will be discarded when applying any filter, in favor of showing a flat list. The grouping will also be omitted when saving a custom view based on the All label.
- Improved filtering of devices and presets.
- A small arrow is now displayed next to a tag's name to indicate that the tag includes subtags. When clicking on a tag with subtags, the nested tags will be grouped along a yellow line.
- It is now possible to use the # symbol to search for all filters, including Content, Function, Format, and Creator.
- Significantly improved the frame rate when scrolling or zooming in the Arrangement when there are many clips and tracks.
- VST2 and VST3 plug-ins now use different icons in the browser.
- The different view modes in the Clip View's Clip Content Editor now use individual Info View descriptions.
- The context dictionary outlet of the live.miditool.in Max object now includes a "seed" value which should be used to seed random number generators that are used to determine a MIDI Tool's output.
- Updated the bundled Max build to 8.6.5. Max for Live improvements: live.miditool.in: displays correct annotation for 3rd outlet live.scope~: fixed memory corruption issues when resized live.text: text / texton accepts multiple words without quoting live.thisdevice: undo no longer triggers output M4L.chooser.js: fixed chain_selector parameter case Max for Live Colors: added 'scale_awareness' Max for Live Device: ensure that searchpaths are marked valid when unfreezing Max for Live Device: fixed crash with loadbang Max for Live Documentation: M4L-specific patcher attributes are documented Max for Live Parameters: improvements to Stored Only parameters and undo/redo Max for Live Parameters: only changed parameters get added to undo mc.plugin~: fixed spurious output from second channel

### Bugfixes

- Deleting a Max for Live device now releases any control surface controls the device has previously grabbed.
- Fixed a crash that could occur when instantiating certain plug-ins.
- A newly created Arrangement locator will now be focused after it is created.
- Fixed a bug where all the changes made to Warp Markers with the keyboard would be undone at once, regardless of which markers were selected.
- Fixed a rare crash that occurred when a count-in was started.
- The distance dial for Arpeggiator is now bipolar.
- The mapping controls in Modulator devices now look correct when disabled.
- When Oscillator Retrigger is on, Drift no longer clicks at note start.
- Recently searched tags are now prioritized higher in tag suggestions once again.
- Drum Sampler now fades out the end of samples in order to avoid clicks.
- Live no longer tries to import unsupported file formats to clips and tracks in the Arrangement View.
- Automation value display is now hidden when zooming or scrolling in the Arrangement.
- Fixed a crash that could occur under certain circumstances when setting the looping and warping API properties from the same event.
- Removed the option to make the Chop and Split commands a part of a MIDI Tools chain.
- Addressed the following issues in Max for Live: Fixed an issue where undo or redo would trigger output from automatable parameters. Fixed an issue where undo or redo would trigger output from live.thisdevice.
- Fixed a crash that occurred in different circumstances, for example when navigating the browser.
- Fixed a bug which caused the background scanning Indexer to crash when analyzing certain audio files with untypical bit depths.
- When repeatedly triggering different clips manually, using follow actions or scenes, Play One note groups are now correctly re-evaluated and the same notes no longer play all the time.
- Fixed an issue where Live would hang on startup.
- Switching between templates on the Launch Control XL no longer breaks the Pickup and Value Scaling takeover modes.
- The sound is no longer sustained indefinitely when the Envelope 1 Release control in Drift is set to a value above 55 seconds.
- Accessibility: When resizing clips with the keyboard, pressing the Esc key now reliably cancels the action. Additionally, screen readers will announce "Cancel adjusting clip edge.." to confirm the action has been cancelled.
- Accessibility: Restored the ability to extend a note selection to include notes of the same pitch using Ctrl (Win) / Option (Mac) + the left and right arrow keys in the MIDI Note Editor.
- Fixed a crash that occurred when enabling warping in Simpler after the device was converted from Drum Sampler. Additionally, fixed a crash that occurred when ungrouping a Rack that contained Drum Sampler using the shortcut Ctrl Shift G (Win) / Cmd Shift G (Mac).
- Fixed a bug that caused phasing artifacts in Auto Shift when MIDI Input was turned off while notes were still playing.
- Mapping the Scale and Root parameters to a Rack’s Macro Controls now works as expected in the Scale, Arpeggiator, and Auto Shift devices.
- Fixed an issue where it was not possible to load a Live Set that contained unknown scale names.

## 12.1.1 (October 30, 2024)

### Bugfixes

- Fixed an issue where Live would hang on startup.

## 12.1 (October 8, 2024)

**To see the updates Live 12.1 brings to Push, head to our Push release notes page.**

### New Features

**Auto Shift**

Auto Shift is a new realtime monophonic pitch tracking and correction device with formant shifting, available in all Live editions. Its design makes it especially suitable for working with vocals but it can be used with any other monophonic signals. It is also possible to play and harmonize the incoming signal polyphonically via the MIDI sidechain.

Auto Shift includes two modulation sources: a dedicated vibrato LFO and a multi-purpose LFO that allow you to modulate all important features of the device. When in MIDI mode, the device is capable of MPE modulation as well.

The device also comes with Live Mode that you can enable to reduce latency. This can be particularly useful for live performances.

Auto Shift supports both built-in scales and user-defined scales.

**Drum Sampler**

Drum Sampler is a new instrument tailored to playing back one-shot samples in Drum Racks. It includes essential sample playing features such as sample start and length controls, an AHD amplitude envelope, Transpose and Detune controls, a filter section, and a number of playback effects which allow to time stretch and loop samples, apply frequency and ring modulation, layer a sub-oscillator or noise, add punch or degrade the sound.

Drum Sampler's compact filter section allows you to select one of four filters optimized for playing back drum hits: 12 or 24 dB low-pass filter, 12 dB high-pass, or a simple single-band half-parametric EQ to emphasize or notch out a portion of the spectrum.

Velocity or Slide in Drum Sampler can be used to modulate volume as well as an additional parameter that you can select, such as one of the envelope controls, filter or a playback effect.

Drum Sampler can also be used as the new default for Drum Racks: to do so, simply right-click on a Drum Rack pad containing Drum Sampler and select "Save as Default Pad" from the context menu. Note that when a Drum Pad is selected, you can now simply double click a sample in the browser to load it inside the current pad: if the pad is empty, the default for Drum Racks will be used - otherwise the currently selected device (if different from the default) will be used instead.

Drum Sampler is available in all Live editions. Note that with the introduction of Drum Sampler, the DS Sampler device has been deprecated. DS Sampler will still be available when loading older Sets that include the device.

**Updated Limiter**

The Limiter effect has been completely overhauled both in sound and appearance. An improved envelope makes Limiter's release smoother, which is especially noticeable when longer release times are used. A completely new UI provides better level and gain reduction metering and a more pleasant look.

A Mid/Side routing mode was added, which can be used to limit the monophonic and the stereo portion of the signal independently. For both Mid/Side mode as well as the Left/Right routing, Gain Reduction Link now works as a continuous parameter, so that users can blend the effect of gain reduction across the two channels with more freedom.

Besides the Standard mode of operation, Limiter now includes Soft Clip and True Peak modes. Soft Clip introduces gentle clipping to signals approaching the ceiling level, whereas True Peak prevents peaks between samples. The new Maximize toggle allows you to control the dynamic range and loudness with a single control, Threshold.

**Updated Saturator**

Saturator has been fundamentally redesigned, so that the main view is focused around the most important parameters. A real time visualization displays the signal level over the curve.

A new Bass Enhancer shaper curve was added, perfect for processing low-end signals such as 808 kick drums and synth basslines. The curve comes with a dedicated Threshold parameter, which makes it possible to seamlessly morph between soft and hard clipping. Only signals above the set threshold will be saturated.

An additional clipping mode for the second stage was added: alongside Soft, you can now opt for a Hard Clipping stage.

In the expanded view, the pre-shaper EQ curve is displayed alongside input and output spectra, for superior control over the Color parameters.

**Filter and Select MIDI Notes**

The new Find and Select Notes feature introduces additional workflow for selecting notes in the MIDI Note Editor, including searching for specific notes using different filters.

Find and Select Notes can be activated by clicking on the magnifying glass button located in the Clip Content Editor Settings. When Find and Select Notes is active, you can use the following filters to look for and select notes:

- Pitch — find and select notes of the specified pitches. This applies to pitches in any octave.
- Time — find and select notes within the specified time range. The range can be repeated.
- Velocity — find and select notes of the specified velocity or within a specified velocity range.
- Chance — find and select notes of the specified probability or within a specified probability range.
- Duration — find and select notes of the specified length or within a specified duration range.
- Count — find and select every nth note or chord.
- Condition — find and select notes that fulfill the specified conditions, such as notes that are active/inactive, or other states.
- Scale — find and select notes that belong to the specified scale.
You can combine the available filters to make more precise note selections.

When Find and Select Notes is on, the new repeated time selection feature can be used to make evenly spaced selections. To create repeated time selections, first make a selection that will be used as the basis for the size of the repeated selections, then press Shift and click and drag in the MIDI Note Editor.

Find and Select Notes also makes it possible to select notes of multiple pitches, by holding Shift and clicking on different keys in the piano ruler.

**Chopping MIDI Notes**

Chopping MIDI notes is now easier and more powerful thanks to a new dedicated MIDI Transformation. It is also still possible to chop notes through the Chop note operation in the MIDI Note Editor, which now features improved workflow.

_Chop MIDI Tool_

A new Chop MIDI Tool is available in the Transform tab/panel. The tool allows chopping selected notes into up to 64 parts, selecting or designing patterns for note chunks and gaps, extending selected chunks relatively to others, and adding random variations.

_Chop Note Operation_

Mouse workflow was improved for the Chop note operation, making the mouse and keyboard interactions more similar.

When chopping notes into more or fewer parts with the mouse, changing the number of parts into which notes are chopped is now achieved with the following workflow:

- Press Ctrl + E (Windows) / Cmd + E (Mac) (this chops notes on the grid).
- Keep holding Ctrl (Windows) / Cmd (Mac).
- Click and drag up or down, or use the arrow up or down key to increase or decrease the number of parts.
It is still possible to add the Shift modifier key to increase/decrease the number of parts by a power of two.

**MPE MIDI Tools**

New MPE MIDI Tools can be used to create curves for MPE parameters of selected notes, with changes visible in the Clip Content Editor's MPE View Mode. Two MPE MIDI Transformation Tools are now available: Glissando and LFO.

_Glissando_

The Glissando MIDI Tool ties successive notes or groups of simultaneous notes, making the pitch bend envelope of each note connect to the pitch of the successive one. Controls in the Transformation allow to adjust the shape and starting point of the envelope. At least two notes must be selected in order to use Glissando.

_LFO_

The LFO MIDI Tool sets an oscillating envelope for one of the MPE parameters of selected notes: Pitch Bend, Pressure or Slide. It is possible to select a shape, rate and set a global amplitude envelope for the oscillator.

**Max for Live: Export Looper's Content to a Clip**

The LooperDevice LOM class now offers a new export_to_clip_slot function. Calling the function with a valid LOM ID of an empty clip slot as an argument on a non-frozen audio track will export Looper's content to a clip in that slot.

**Scale Awareness for Audio Clips**

It is now possible to associate a scale with an audio clip using dedicated controls in Clip View's Main Clip Properties tab/panel. Setting a scale in an audio clip doesn’t affect the audio playback itself (similar to how the clip time signature setting doesn’t affect playback) but it is forwarded to scale aware devices on the device chain.

As a result of this change, Auto Pitch becomes the first scale aware audio effect.

**Apply Grooves Instantly**

A groove is now loaded with the default Live Set and automatically applied to any new MIDI clip. By default, the Global Groove Amount is set to 0%, so all you need to do to apply the groove is adjust this value. The Global Groove Amount is visible in the Groove Pool and, once a MIDI clip is added to the Set, also in the transport bar.

In the Groove Pool, there is a new Auto Load Groove toggle, on by default, that controls whether a groove is auto-loaded on new MIDI clips. You can switch the toggle off and no grooves will be auto-loaded. A dedicated Hot-Swap button allows you to select which groove you would like to be auto-loaded.

**Undo History**

It is now possible to use the new Undo History feature in order to display a list of the available undo and redo steps, with the possibility to undo and redo multiple steps at once by clicking on an entry in the list, or by selecting an entry with the arrow keys and pressing Enter .

The "Undo History" option is available in the View menu and can also be opened with the shortcut Ctrl + Alt + Z (Win) / Cmd + Option + Z (Mac).

**Full-Height Browser**

It is now possible to switch from the standard-height browser to a full-height view of the browser, stretching all the way down to the Status Bar.

The "Full-Height Browser" option is available in the drop-down menu next to the Show/Hide Browser toggle, as well as in the View menu.

**Auto Tagging User Content**

Any samples under 60 seconds are now analyzed and automatically assigned a tag which best matches their sound.

Auto tags can be shown and hidden in the browser using a new Include Auto Tags toggle, and can be removed or changed to user tags in the Tags Editor. Files which have been auto-tagged use blue checkmarks in the Tag Editor, while user tags use yellow checkmarks.

**Auto Tagging Plug-ins**

VST3 plug-ins will now be assigned a tag based on VST3 meta data if the plug-in uses a VST Sub Category that maps to one of Live's categories.

Note: All plug-ins will be rescanned when upgrading to Live 12.1 for the first time. This eliminates potential issues with Live hanging or crashing after the install, and allows for the plug-ins to be tagged automatically.

### Feature Improvements

**Accessibility Improvements**

- Accessibility: Filters and Tags Editor now work meaningfully with screen readers and can be navigated and selected using the keyboard.
- Accessibility: Users can now navigate through Live UI Objects in Max for Live devices by pressing the Tab key. Live UI Objects also offer basic screen reader support.
- Accessibility: Pressing Ctrl (Windows) / Cmd (Mac) together with plus or minus keys now zooms the UI.

**Browser Updates**

**Filters and Tags Editor Improvements**

- Reordering tags and tag groups: It is now possible to reorder tag groups and tags in the Tags Editor, creating a custom order. You can restore the default order by right-clicking on a tag group in the Tags Editor and selecting the "Reset Tag Order" option. Filter groups in the Filters view will follow the custom order set in the Tags editor. Note that only the groups available in the Tags Editor can be reordered.
- Tagging user folders: It is now possible to tag folders in the Library and Places. When a folder is tagged, all the content contained within it is also tagged.
- Creating subtags: You can now create subtags (up to one nesting level). Right-click on a tag and select the "Add Tag in..." option to easily create a subtag within another tag.
- Folding subtags: Tags containing subtags can now be folded in the Tags Editor to save space. When tagged content is selected in the browser, and its tag groups as well as parent tags (in the case of subtags) are folded, the fold/unfold arrow for tags and tag groups assigned to the content are now indicated by a more prominent, white-on-black arrow in the Tags Editor.

**Sidebar Improvements**

- You can now restore Library labels order to default by right-clicking on the Library section's header and selecting the "Reset order to default" option.

**Core Library Updates**

- Added new artist Drum Racks and samples by DECAP, L.Dre, and Taka Perry.
- Slice to New MIDI Track: Optimized the selection of Slicing Presets in the dropdown menu.
- Added new MPE Drum Racks that utilize Drum Sampler's Slide feature.
- Added new tuning systems.
- Added new presets for Meld, Chord, Saturator, and Limiter.

**Devices Updates**

_CC Control_

The CC Control effect now offers a convenient MIDI CC learn mode. When the Learn toggle is on, the device can receive CC data via regular track or device input. The user can then select one of the customizable controls to learn the specific CC data being sent.

_Echo_

The Echo effect now allows to freely adjust smoothing time for the Repitch parameter. This allows to adjust how slow or fast a new delay time is applied.

_Meld_

New Phase Reset and Phase Spread parameters are available in Meld's Settings tab. They allow to restart the oscillator phases with a MIDI note and to spread the start position of the oscillator phases, respectively.

_Sidechain in Envelope Follower_

The Envelope Follower modulator device now includes a sidechain routing, which allows to route another signal source from other tracks and mix it with the source of the track the device is added to. This feature can be useful in achieving a ducking effect.

_Tuner_

The Tuner device now supports tuning systems.

**MIDI Editing Improvements**

- Release Velocity now has a dedicated lane below the MIDI Note Editor.
- When editing multiple clips, the foreground clip is now indicated with an LED which uses the clip color.

**MIDI Tools Improvements**

_Stacks MIDI Tool_

- Custom Chords: It is now possible to load user-defined chord banks or "chord rules" in the Stacks generator. Chord banks are text files in the JSON format. To load a Stacks chord bank, double-click a chord bank JSON file located in the browser. You can find out how to create custom chord banks in our Knowledge Base .
- Extended Support: Stacks is now better at handling less common use cases such as Drum Rack tracks or non-12TET tuning systems.
- The inversion parameter can now be set to negative values.

_Recombine MIDI Tool_

- The tool has been redesigned and now affects only one note parameter at a time.
- In addition to the previous parameters (pitch, velocity, and duration) it is now also possible to use Recombine on note positions, which can be rotated on other existing note positions or according to the current grid settings.
- It is possible to rotate notes by single steps using the dedicated Rotate Step Down/Up buttons.
General MIDI Tools Improvements

- Key/MIDI Mapping: The parameters in MIDI Tools are now Key/MIDI mappable. Note that this does not apply to Max for Live MIDI Tools.
- Updated "Apply" buttons: The design of the Auto Apply toggle in MIDI Tools has been changed to display "Auto" instead of the former "Transform" or "Generate" (used in Transformations and Generators respectively). The design of the Apply toggle has been changed from the former circular arrow button to a rounded button that displays the word "Transform" or "Generate" (depending on the type of the MIDI Tool used)
- Apply MIDI Tools in a chain: You can now chain MIDI Tools together so that you can keep editing their parameters and see the changes reflected throughout the entire chain. The chain is created when a Generator or Transformation is applied to the clip content, and other Transformations are added afterwards. It is possible to return to any MIDI Tool in the chain and adjust its parameters, affecting the rest of the chain. The chain listing all of the active MIDI Tools is displayed in the Status Bar.
- Apply Transformations to duplicated content: When you apply a MIDI Transformation Tool and then duplicate the transformed notes, it is now possible to tweak the parameters of the MIDI Tool and the changes are immediately applied to the duplicated content.
- Remember MIDI Tool on a track: Tracks now retain information about the last-selected Transformation and Generator.
- Set Pitch for Generators: It is now possible to set a pitch or pitch range for MIDI Generative Tools by clicking on a key or clicking and dragging over the keys of the piano ruler. It is also possible to select the pitch or pitch range directly in the MIDI Note Editor by holding Alt (Windows) / Option (Mac) while clicking or clicking and dragging inside the Editor.
- Select notes to apply: When no notes are selected, Transformations will no longer be started automatically when their parameters are tweaked.
Tuning Systems Improvements

- Tuning systems with 12 notes per octave will now work with Live's collection of built-in scales. Note that this feature is not currently supported in scale-aware MIDI Tools and other pitch editing utilities, such as Fit To Scale.
- Tuning System properties are now accessible to and adjustable using the Max for Live API. A loaded tuning system is accessible at the LOM path live_set tuning_system . The Global.TuningSystem Max for Live snippet in the Max editor can help with converting tuning system data to mtof messages.
Additional Live Improvements

- It is now possible to split Arrangement clips (both audio and MIDI) from the Clip View, using the dedicated Split Clip command in the Sample Editor or MIDI Note Editor or the following keyboard shortcut: Ctrl + Shift + E (Windows) / Cmd + Shift + E (Mac).
- Improved Crop commands in the Arrangement View so that clips are cropped according to the actual time selection made in the Arrangement.
- The Mixer in Arrangement can now be focused separately from the Arrangement View and has its own dedicated focus frame.
- The Overview is now included in the focus frame when the Session or Arrangement is focused.
- Time selection, split and crop clip operations are now available in unwarped audio clips.
- It is now possible to edit pitch bend in tracks containing Drum Racks using a dedicated lane in the MPE Editor.
- Roar's Mid High Crossover color was changed to match the color used in the third stage.
- When closing a Live Set that contains many Arrangement clips, the Set is now closed more quickly.
- Simpler and Drum Racks now feature a new entry in their context menus. The entry makes it possible to replace Simpler with Drum Sampler, Drum Sampler with Simpler, or all instances of one of the sampling Devices with the corresponding counterpart in a Drum Rack.
- It is now possible to associate a scale with tracks containing Drum Racks. The scale is used in the devices which have the Use Current Scale toggle switched on.
- Max for Live Improvements: Live Object Model: updated documentation Max for Live Parameters: annotations are shown when setting focus Max for Live: improved screen reader support Max for Live: new Tuning System abstractions / clipping / helper udpreceive: fixed issues with freeing object on Push 3 Max for Live Device: saving after freeze via window close button works as expected
- Browser Improvements: Made small improvements to the Devices tags group and added new tags to accommodate VST3 auto-tagging. Drum Racks using tags from the "Sounds" tag group now show up in the Sounds label. Added the following improvements to filtering in the browser: In the All label, presets are now displayed as a flat list instead of being grouped under their respective devices. When filtering for "Content|Preset" in any label, presets are now displayed as a flat list instead of being grouped under their respective devices. Clips tagged with the "Clips|Drum Clip" tag will now be shown in the Drums label. In the "Content" filter group, users will now see separate Audio Clip and MIDI Clip buttons, rather than just the Clip button. Adjusted the size of the tag auto-completion pop-up in the search field to accommodate the longest Ableton factory tags. The browser now displays the number of selected items next to the Preview button, if previewing files is not active, either because the Preview button is toggled off or because the selected item does not support previewing. Made the following changes to the browser's context menus: Some context menu entries were reordered. The "Locate Patch File" entry was changed to "Show Max Device." The "Show Old Versions" entry was changed to "Show Backups."
- Sound Similarity Searching Improvements: Live now supports Sound Similarity Searching for 32-bit integer WAV files. When started from within an existing search, a new search will no longer switch the browser to the All label. When starting a search, any active filters and the text search input field will now be cleared.
- Core Library Improvements: A selection of existing Drum Racks was updated to use the new Drum Sampler device. Modulator presets now use Mod instead of Remote. Various sound and naming refinements.
- The embedded Python interpreter has been updated to version 3.11.6. Because of this, remote scripts that use compiled byte code (.pyc) need to be recompiled using this Python version to work properly with Live 12.1.
- Added support for the Move control surface.
- Updated software text in various areas of Live.
- Updated some software text translations in French, German, Italian, and Spanish.

### Bugfixes

- On macOS, fixed a bug where exporting video when there was no video clip at the start of the exported time range caused the exported video to be zoomed in a lot, showing only a small portion of the original video.
- Accessibility: Fixed that relationships between items in the browser were not spoken properly by screen readers on Windows.
- Fixed an issue that caused an error message to appear in the Status Bar when duplicating a mapped modulator.
- Scroll bars visible when entering long custom text using the Edit Info Text option now use Live 12 UI styling.
- Accessibility: The accessible names of send sliders in the Arrangement mixer now correctly include the name of the corresponding return track.
- The Triplets control in the Quantize Audio/MIDI Tool now correctly updates depending on the chosen Quantize Grid option.
- The Stacks MIDI Tool no longer displays a preview of the selected chord when the Generator is disabled (e.g. in the Envelopes Editor View Mode).
- Fixed an issue which prevented toggles in Live's UI to automatically open their corresponding views when dragging and hovering content over the toggles. This bug affected the Show/Hide Browser, Mixer View, Clip View and Device View toggles.
- Fixed an issue where focus was placed in an incorrect part of the UI when opening the Clip View's Grid Settings menu.
- Fixed a bug in the Envelopes Editor View Mode where resizing an automation envelope time selection while zoomed in would resize the selected part of the envelope to fill the entire view rather than only the small distance dragged.
- Fixed a bug that would cause a Max for Live MIDI Tool saved to a location unknown to the browser to become deselected as soon as the Transformation/Generator Selector drop-down menu was opened.
- MPE Control now properly restores the Pitch Range parameter after reloading a Set.
- Fixed the following issues: A strip representing scene color no longer appears under the scroll bar in Session View. Navigating to scene tempo and time signature with arrow keys is now possible regardless of whether the scene is visible or not. The Scene Tempo And Time Signature entry in the scene context menu and View menu will now show the correct state, even if the first scene is scrolled out of view.
- Fixed a bug that would sometimes prevent the Transformation/Generator Selector from updating correctly when a new Max for Live MIDI Tool was saved.
- Fixed a crash that could potentially occur when closing a Live Set with a Max for Live device observing the mute property on a chain mixer.
- Fixed a crash that occurred when transferring certain types of files (e.g. presets) to Push in Standalone Mode.
- Fixed a crash that occurred when dragging and dropping samples into a Drum Rack.
- Fixed an issue where notes and their velocity values would disappear in MIDI clips longer than 10000 beats.
- Accessibility: Fixed a bug that caused the accessible representation of scenes to be inconsistent when the "View>Scene Tempo and Time Signature" option was active.
- Fixed the following issues with crash recovery: Crash recovery is now enabled for multiple instances of Live when those instances use different versions of Live. A message will now be displayed when crash recovery is disabled in cases where another instance of Live using the same version is running.
- DS Snare no longer occasionally mutes notes early.
- Horizontal sliders now support fine control using the Shift key.
- Horizontal slider sensitivity now works as expected in the chain selector.
- Improved the appearance of Shaper's and Shaper MIDI's waveforms at zoom levels other than 100%.
- Fixed a bug where the Connect button was not visible for Pushes available for pairing.
- When MPE data is edited while notes are transformed by any of the MIDI tools or Pitch and Time utilities, edits now won't be lost when continuing or updating the transformation.
- Fixed a crash that occurred after clicking on inactive MIDI Dump buttons in the Link, Tempo & MIDI Settings.
- Fixed an issue where note probability, velocity deviation and per-note events were not copied to the extracted clip when using the Extract Chain command.
- Freezing tracks that contain clips without names will no longer result in creating clips with a name that starts with a space character.
- The "Save Default Clip" button in an audio clip's title bar is now reachable through keyboard navigation.
- Accessibility: Fixed a bug that caused keyboard focus to get stuck in the Arrangement timeline.
- Fixed a bug that caused the Session View layout to be broken when making return tracks visible.
- Fixed an issue where the track and scene highlight could not be moved with the arrow keys on an hidden return track in the Session View.
- Fixed an issue where Packs folders in the Packs label in the browser would not show assigned colors after switching labels.
- Accessibility: Fixed a bug that could cause the MIDI Note Editor to have an incorrect accessible name.
- Fixed a crash that occurred when dragging the last label in the Library section of the browser onto itself.
- On Windows, the right Alt key now functions the same as the left Alt key for all keyboard layouts that do not implement the AltGr mechanism, such as US English.
- On macOS, fixed a regression in the display of the outer frame of drop-down menus.
- When opening a Live 11 Set which had the tempo and/or time signature fields visible, and any of the values of those fields were changed, the visibility of those fields will now be preserved if the Set is open in Live 12.
- Accessibility: Fixed a bug in screen reader navigation between the scene control, tempo field, and time signature field in scenes.
- Fixed a bug where devices would not be initialized with a correct scale when no clip was playing on a track.
- Fixed a crash that occurred when loading an old Live Set containing VST2.
- On macOS, fixed an issue where the striped clip panel header of multiple-clip selection was rendered incorrectly.
- Fixed a crash that could potentially occur when closing Live.
- Search terms will now be cleared after entering the Hot-Swap mode. It is possible to restore the search after exiting Hot-Swap, then going back in the browser's history.
- Fixed a bug where a recording in progress could be unexpectedly stopped (and the track disarmed) when selecting a different track in Live with Push connected.
- Sets with routings to external MIDI devices will retain those routings as expected when they are saved in Live on a computer and opened on Push 3 in Standalone Mode, or vice versa. Note that Sets saved after the introduction of this fix will lose their routings when loaded in an older version of Live.
- Selecting time with the mouse in the MIDI Editor Stretch Area now behaves consistently with making time selections in the MIDI Note Editor.
- Fixed an issue where expanding one device would incorrectly close expanded views in other devices.
- Accessibility: The "Save Default Clip" button in the audio clip title bar is now reachable with keyboard navigation.
- Fixed an issue where automation breakpoints located within or outside the clip and intersecting with the insert marker would not be deleted after pressing the Delete key.
- For multiple deleted breakpoints, the Undo text in the Edit menu was updated from "Delete Envelope" to a more accurate "Delete Breakpoints".
- Fixed a bug that prevented the Ctrl + Enter (Windows) / Cmd + Enter (Mac) shortcut in a MIDI Tool panel from applying the Transformation/Generation if a Max for Live MIDI Tool was selected.
- Resolving paths to the following elements via live.path will no longer result in an error: GroovePool.grooves MaxDevice.audio_outputs MaxDevice.audio_inputs MaxDevice.midi_outputs MaxDevice.midi_inputs Track.arrangement_clips
- It is now possible again to repeatedly trigger Undo step by pressing and holding Ctrl + Enter (Windows) / Cmd + Enter (Mac).
- Updated the Core Library: EQ Eight default preset: no Adaptive Q for shelf filters. Fixed the timing of Swing 8ths/16ths/32nds groove presets. Fixed Turkish Makam and Sundanese Gamelan tunings.
- Fixed an issue where pads would not turn green and the MIDI Track Out indicator would not flash in MIDI control surfaces such as Push 1 (or Push 2 with the legacy script option) when notes were played back in Live on the control surface's selected track.
- Fixed a bug where the "Clear Envelope" option would be erroneously displayed in the context menu of Clip View's buttons in some circumstances.
- The notification shown on Push 2 when moving scenes now correctly mentions encoders instead of the jog wheel.
- Fixed a bug where EQ Eight would turn silent when moved across tracks.
- In Analog, Meld and AutoPan, fixed some minor issues that occurred in the devices' displays when a value was changed via Undo.
- Fixed an issue where the modulation matrix cell in Wavetable and Meld became disabled when a target was mapped to a macro.
- In Meld, fixed an incorrect Push mapping on the Matrix bank to the Engine B Pressure modulation amount page when Engine A was selected.
- The Time Warp MIDI Tool now takes into account MPE events as expected.
- Fixed an issue where Live would freeze when loading or showing the Info View description of a tuning system with a descending pseudo-octave. An error will now be shown in this situation instead.
- It is now possible to apply tuning to MPE-capable plug-ins and Max for Live devices via a context menu in the plug-in/device header.
- When a tuning is loaded, MPE pitch bend is now tuned so that one step is one tuned step rather than one 12TET step.
- Fixed a bug that prevented some control surfaces from being automatically configured in Live’s Settings.
- When recording a new Session clip and selecting a different clip while recording, Live would stop updating the visible time range in the clip. This had the effect that when stopping the recording and then displaying the clip again, Live would show the time range that was visible when showing the clip for the last time. This behavior is now fixed and Live shows the entire clip.
- Phase cancellation no longer depends on the song start time when two tracks are set up to be canceled via the Utility device's phase inversion buttons.
- Pressing the arrow down key in the search field now moves keyboard focus directly to the search results.
- Fixed a crash that would occur when moving the Session slot highlight from an audio or MIDI track to the main track or vice versa, without any return tracks present.
- Fixed an issue which could cause Live to freeze when encountering certain corrupted WAV files.
- Improved performance in the Plug-ins label when using the Group by Creator option.
- On macOS, fixed an issue where custom key mappings using the Option modifier would not work.
- Fixed an issue that occurred when using a custom tag in a Drum Rack, where unexpected devices would be displayed under the tag.
- In the Arpeggiate MIDI Tool, when generated notes would go over the note range, the resulting note is now folded down an octave also when scale is off, and works correctly with tuning systems as well.
- The Channel Configuration windows in the Audio Settings now follow the same zoom level as the rest of the UI.
- Fixed a bug where the Similar Files button remained visible after file analysis failed.
- The UI is no longer interrupted when the preference "Auto-Warp Long Samples" is set to On and a Live Set containing samples for which there is no .asd file is opened. This means that importing clips from an existing Set will no longer cause an interruption to the UI.
- Fixed an issue where the browser would shortly flicker, and then become empty, displaying the message "No Content" or "No Results".
- Creator tags for plug-ins used in group presets are not shown in the Filters view anymore.
- Fixed an issue where, when filtering for "Content|Preset" in a label grouping presets by device and then saving the results as a custom label, the resulting custom label showed no content.
- Fixed a bug where the browser would not open the expected "Content|Device" filter view when hot-swapping a device that was instantiated using the "Content|Device" filter.
- Fixed issues with Help View formatting in Japanese and Simplified Chinese.
- In Drift, the UI of the LFO and Mod section is now consistent with the UI in other Live devices.
- Fixed a crash that could occur when warping long samples.
- Fixed an issue where "Delete" commands were erroneously displayed in the context menus of clip loop and other beat time editors.
- The "Clear" button in the browser is now wider to better accommodate text in languages other than English.
- Live's user interface is now more responsive when changing tempo automation in Sets with a very large number of clips.
- In the MIDI Note Editor, fixed a bug where some menu commands were not available after switching clips using the loop bar and then selecting a note in the Editor.
- Fixed an issue that occurred when navigating the timeline in the MIDI Note Editor with the keyboard, where clicking on the MIDI Note Editor Preview button would move keyboard focus from the timeline to the button.
- When exporting a video on Windows, the exported video frame rate will now match the frame rate chosen in the video export dialog as expected.
- Fixed an issue where, when hot-swapping a device, the browser would automatically scroll to the to the top of the content pane instead of moving to the device itself.
- Users can now search for multiple auto-completed tags in a row without needing to add a space between the tags.
- In Live's browser, switching between labels will no longer restore the previous position in the list if the search text has changed since last using the label. This includes similarity searches, as well as tag searches triggered from the search field.
- Collections are now visible and accessible from the Instruments, Audio Effects, and MIDI Effects labels again, as expected.
- Configuring sliders for plug-ins should now work as expected.
- Fixed a bug where switching to a Drum Rack clip and back to a non-Drum Rack clip would disable the Fold to Scale option.
- Fixed an issue that could potentially result in MIDI Tools corrupting note data.
- Fixed a bug where, for some actions performed via mapped keys, Undo would not revert individual value changes and as a consequence no individual entries would show up in the Undo History, since no individual Undo steps were created.
- When repeatedly triggering the same clip manually, e.g. by using Follow Actions or starting the clip's scene, Play One note groups are now correctly reevaluated and the same note no longer plays all the time.
- Fixed a crash that would occur when loading the "Faded Keys" Drift preset.
- Fixed the following issues with multi-clip editing: Fixed a bug where extending note length with the keyboard would not update the time selection. Fixed an issue where, when multiple notes were selected in the MIDI Note Editor the time selection would change to include only the recently clicked note.
- Fixed a bug where resizing track headers in the Session View in Sets that contained many scenes would cause Live to hang.
- The state of the Chain Auto Select setting is now stored in the Audio Effect Rack, Instrument Rack, and MIDI Effect Rack presets.
- Fixed an issue that could cause Live to hang when exporting audio for certain Sets.
- Fixed an issue where warp markers would not be displayed after undoing a delete action on a clip.
- Fixed an issue where audio clips in the Beats Warp Mode with the Transients Granular Resolution would not play back if there was a very small transient distance.
- Fixed a bug where MPE data was not sent correctly if the Arpeggiator or Note Length device was placed inside or after a MIDI Effects Rack device.
- Fixed a bug where instruments or plug-ins that apply MPE data relatively to the value at the start of a note would not receive per-note expression correctly for notes output from the Chord device if its Strum control was set to non-zero values.
- Fixed a bug where the Note Length and Arpeggiator devices would send superfluous MPE events.
- Selecting another element in Live's UI now deselects an automation breakpoint previously selected for keyboard editing with the Alt (Win) / Option (Mac) + mouse click combination as expected.
- Fixed a crash that occurred on shutdown in some cases.
- Fixed an issue where the automation value was displayed after undoing the action of moving a time selection in the Automation Mode while the "Move Selected Arrangement Clips with Arrow Keys" option is enabled. The value will now be displayed only for an empty time selection (i.e. insert marker), as expected.
- When dragging a clip to the browser and dropping it onto a folded item before it unfolds, the drop position outline now disappears immediately after completing the drag and drop action, as expected.
- Fixed a crash that occurred when switching audio devices under certain circumstances.
- Fixed an issue where scanning plug-ins at startup could cause Live to hang or freeze.
- Fixed an issue where unwarped cross-clips that were cross-fading in would not play back or render at the correct time if the cross-fading happened during song tempo automation.
- Fixed an issue where the Session mixer was not visible when switching to the Session View for the first time after loading a Set that was saved in Arrangement.
- Fixed two crashes: Live will no longer crash when making a multi-clip selection which is a mix of frozen and unfrozen MIDI clips. Live will no longer crash in some cases when changing the foreground clip while multi-clip editing.
- Fixed a bug where a deactivated Chord device would alter per-note pitch bend messages when following a scale.
- Fixed a crash that occurred in some cases when undoing a change while viewing a MIDI clip in the Clip View.
- Fixed an issue where the send values of audio, MIDI and group tracks imported from the browser would be reset to -∞dB.

## 12.0.25 (August 29, 2024)

### New Features and Improvements

- Added Control Surface support for Arturia KeyLab mk3, Novation Launchkey mk4 and Novation Launchkey Mini mk4.

## 12.0.20 (Aug 6, 2024)

No Live specific release notes, please refer to the release notes of Push 3 (Push 2.0.20 with Live 12.0.20).

## 12.0.15 (July 23, 2024)

No Live specific release notes, please refer to the release notes of Push 3 (Push 2.0.15 with Live 12.0.15).

## 12.0.10 (June 28, 2024)

### New Features and Improvements

- ​​​ Live's authorization code has been reviewed and simplified (without functionality change) and now uses a JSON format for the unlock file.

## 12.0.5 (June 5, 2024)

### New Features and Improvements

**Accessibility**

- Accessibility: Mixed state of a control is now exposed to screen readers as "Mixed Value". For example, in a multiple clip selection, where loop is on in some clips and off in others, the state of the Loop switch in the Clip View will be announced as "Mixed Value".
- Accessibility: Screen reader announcements in the MIDI Note Editor now use a description of the time selection which is made specifically for screen readers, instead of using the generic description from the Status Bar. Additionally, times can be announced in seconds by enabling the “Speak Time in Seconds” option in the Accessibility menu, otherwise they will be announced in bars.
- Accessibility: The Step Input Mode of the MIDI Note Editor now includes announcements for screen readers.
- Accessibility: When the new option “Speak Time in Seconds” in the Accessibility submenu of the Options menu is enabled, time announcements in the Arrangement View timeline will be announced in milliseconds formatted as: hh:mm:ss:ms.
- Accessibility: When arming tracks is disabled, the reason why will now be announced by screen readers. When any other menu command is disabled, screen readers will announce the command and “command not enabled”.
- Accessibility: Added a new “Speak Extended MIDI Note Description” command to the Accessibility submenu within the Options menu. By default the command is enabled, but if deactivated, parameter names (e.g., "Duration", "Velocity", "Probability") are omitted in the screen reader announcements, as well as any probability values that are set to 100%.
- Accessibility: When downloading Packs, the download status is now announced by screen readers.
- Accessibility: Added basic keyboard navigation support and screen reader announcements for tabs in Live devices and Clip View.
- Accessibility: Error messages displayed in the Status Bar are now announced by screen readers.
- Accessibility: In the Stacks MIDI Tool, changes made on selected chord pads are now announced by screen readers.
- Accessibility: The MIDI Note Editor now uses "MIDI Note Editor" as a role description for screen readers and is named based on the current clip and time selection.
- Accessibility: Added some small improvements for keyboard navigation and screen reader announcements for a number of Live devices.
- Accessibility - Added some improvements for MIDI Note selection announcements: When selecting a MIDI Note with the keyboard while a note is already selected, the word “Select” will be omitted from the announcement. When the note selection is expanded using the keyboard to include another note, there will be a unique “Add Note” announcement describing only the additional note. Collapsing the note selection using the [Esc] or [Enter] key is announced as “All notes deselected”.
- Accessibility: The Chord Selector Pads in the Stacks MIDI Tool now have unique labels for screen reader announcements.
- Accessibility: Status indicators in the Modes and Monitoring control groupings are now accessible to keyboard and screen reader users. Activating them with the Enter key or pressing them via screen reader will cause Live to announce the time in seconds since the last message which caused the LED to flash.

**Arrangement View**

- In the Arrangement View, when the mixer is not focused, the [CTRL][ALT][I] (Win) / [CMD][ALT][I] (Mac) keyboard shortcut will toggle the visibility of the In/Out section, while the [CTRL][ALT][R] (Win) / [CMD][ALT][R] (Mac) keyboard shortcut will toggle the visibility of the return tracks.
- The volume section of the mixer in the Arrangement View can now be resized by dragging its top border, like in the Session View.
- Scrollable automation lanes in the Arrangement View will now only respond to mousewheel if their lane is highlighted.

**Browser**

- In the Plug-Ins label of the browser, VST2 plug-ins are no longer displayed with an expandable folder icon.
- In the browser, Creator tags for VST2 plug-ins are now automatically assigned.
- It is now possible to group plug-ins into a folder based on the Creator tag in the Plug-Ins label of the browser. To do so, right-click on a plug-in and select “Group by Vendor.” If a plug-in does not have an assigned Creator tag, it will be displayed in a flat list below any grouped plug-ins.
- The browser’s Plug-Ins label will now by default show plug-ins grouped by their Creator.
- When deleting a tag, the confirmation dialog will now include a note informing the user that the tag is used in one or more custom labels.
- In the browser, the context menu option "Show in Places" is now accessible when filtering or using Similarity Search inside Places and the Packs label.
- Users can now reorder labels in the browser’s Library section, except for the All label, which is fixed.
- Added additional tags to content in various legacy Packs.
- Updated the Core Library: Added Demo Set presets by Chuck Sutton. Added new and refined Meld presets (Note Pitch Bend and Mod Wheel mappings). Added tags for Devices and FX Racks like "Mixing & Mastering", "Vintage Emulation", "Live Control", "Performance & DJ" Refined the Demo Set.

**Clip View**

- When the Clip View is focused, the [ALT][+/-] keyboard shortcut can now be used to zoom in and out of the MIDI Note Editor.
- Accessibility: Added screen reader support for audio clip markers in the Sample Editor, including warp markers, start and end markers, and loop start and end markers. Markers can be navigated with the [Tab] key and moved in time with left and right arrow keys.
- Previously, undoing changes in MIDI Tools via the Undo command could be slow if the tool’s parameters had been significantly changed. Now, the undo action happens instantaneously.
- It is now possible to drag up and down in the Strum Transformation’s display to adjust the value of the Tension parameter.
- In the MIDI Note Editor, when key tracks are folded, any tracks that are left empty after applying Fit to Scale will now be automatically hidden.
- In the Arpeggiate, Connect and Ornament MIDI Tools, the velocity and chance deviation values from the original notes are now applied to any new notes that are added from the note transformation.
- The Arpeggiate, Ornament, Connect and Shape MIDI Tools now only generate notes in active key tracks when using Drum Racks.
- When applying changes in the MIDI Note Editor with Arpeggiate, Connect, Stacks, or Ornament’s Grace Notes option with the key tracks in a folded state, the folded and unfolded key tracks will be updated dynamically in response to the changes in the MIDI Note Editor.
- Holding [Shift] while pressing the Page Up or Page Down key will scroll the MIDI Note Editor vertically by one key track up or down.
- In the Time Warp MIDI Tool, it is now possible to type values into the Breakpoint Time and Breakpoint Speed parameter fields using the keyboard.
- The [CTRL][ALT][L] (Win) / [CMD][ALT][L] (Mac) keyboard shortcut can now be used to show and hide the Clip View and Device View.
- The Add Interval Pitch Tool now works with key tracks when using Drum Racks.
- When using the ×2 or /2 buttons or the Stretch dial in Clip View, the time selection (if any) will now be updated to stay in sync with the changes to note lengths.
- It is now possible to type in values (for pitches you can type a note number, e.g., 60 instead of the note name e.g., C3, and using spaces for text input is also supported, e.g., "Hi Hat") using the keyboard for the following MIDI Tool parameters when they are focused: Seed - Min/Max Pitch or Key Track, Min/Max Duration Shape - Min/Max Pitch Rhythm - Pitch, Duration Arpeggiate - Rate Connect - Rate Shape - Rate Stacks - Root, Inversions
- In the Velocity lane, the Ramp Start Value control is now editable when a single note is selected in the MIDI Note Editor. When multiple notes are selected that start at the same time, only the Ramp End Value control is deactivated.

**Devices**

- The Velocity MIDI effect is now easier to navigate using the computer keyboard. When using the [Tab] key to move focus through the controls, tabbing will go through each parameter in a column from top to bottom, and when the end of a column is reached, tabbing will move between columns from left to right.
- The Pitch control in the Pitch device is now less sensitive when adjusting it with the mouse.
- The Shepard’s Pi oscillator type in Meld has been optimized to use fewer CPU resources.
- It is now possible to access device header tabs when navigating with the computer keyboard.
- In Meld, added an Info View description for modulation sources, which appears when the user is hovering over the column headers in the Modulation Matrix.
- The parameter dials in the CC Control device no longer respond sluggishly to mouse movements.
- Some improvements for the Meld device: The scaling of the global volume control has been improved. The mixer meters now show the summed volume of the engine. Aliasing artifacts in Meld’s Noisy Shapes oscillator are now reduced. In Meld, the default envelope attack time value is now 1.00 ms. Additional software text descriptions have been added for Meld’s oscillator macro controls, filters, and filter type parameters.
- In Drum Racks, it is now possible to spell note names as MIDI numbers in the MIDI Note Editor. These numbers are also indicated in the Status Bar’s description of the drum pads.
- After dropping something onto a Drum Rack pad, that pad will become selected.

**Interface**

- Added some improvements to context menu entries in the Live UI: The text of the entries is used more consistently in the different places where they appear, respecting the singular/plural forms whenever possible. The "Crop" command is now available in the loop brace's context menu.
- The "Crop" command can now be invoked in the Arrangement or Clip View with the [CTRL][Shift][J] (Win) / [CMD][Shift][J] (Mac) screenshot.
- The Info View description is now shown for more context menu items.
- When using any of the keyboard shortcuts for Similar Sample Swapping, the corresponding Swap to Next/Previous Sample buttons will flash to indicate the swap is being performed.
- Made some improvements to Live’s UI: The width of the Main track in the Session View can now be increased to allow for longer scene names. The text editor for cue points is now wider by default, to allow for longer cue names.
- The mixer peak hold time was reduced from 10 seconds to 2 seconds.
- Highlighting and selecting tracks when using Solo and Track Activator buttons now work in a consistent way: A track is highlighted when it is soloed in the Session or Arrangement.This behavior can be stopped by using the debug option NoHighlightOnSolo. In Drum Racks, the chain is now selected when its pad is soloed. This behavior can be stopped by using the debug option NoHighlightOnSolo. In Drum, Instrument, and MIDI Effect Racks, a chain is only selected if the chain's Solo or Track Activator buttons are turned on.
- Live’s Preferences menu has been renamed to “Settings”.
- If the Show Scroll Bars option in the Display & Input Settings is set to "When Scrolling", the scrollbars are now also displayed after hovering over the scrollbar area for a fraction of a second.
- The “Show Scroll Bars” option in the Display & Input Settings now includes a “Follow System” entry. When selected, the display behavior of scrollbars in Live will match whatever is specified in the OS system preferences.
- When using the up and down arrow keys to adjust volume or level parameters in dB, values now change consistently in increments of 1 dB (or 0.1 dB when fine-tuning with the [Shift] modifier).
- Updated software text in various areas of Live.
- Updated the What’s New in Live Help View lesson.

**Max for Live**

- Updated the bundled Max to version 8.6.2: Max 8.6.1 Max for Live Improvements amxd~: fixes issues related to setting a parameter with another parameter live.* UI objects: improved unfocus behavior live.remote~: normalization fallback for Live 11 and earlier Max for Live: device window always opens on a display Max for Live: modulator mappings are saved/restored Parameter: clip modulation mode attribute defaults to 'Additive' selector~/gate~/etc: fixed issues when audio is off in the Max for Live editor Windows multitouch: fixed touch / drag in Max for Live devices Max 8.6.2 Max for Live Improvements Dynamic Colors: loadtime performance improvements jit.gl.text: fixed crash when freeing (fixes VectorMap crash) Live.routing: sends if the port has no DeviceIO objects Max for Live Device: dependency files are extracted to the correct location Max for Live Device: fixed issues with file reorganization Max for Live: Updated LOM documentation to the state of Live 12.0.x. SVG: loadtime improvements
- Users will now be able to see a live.line object in the Max for Live MIDI Tool templates, which indicates the lower visual boundary of a Max for Live Generator or Transformation.
- Users who create their own Max for Live Note Transformations or Generators can now access the scale name when working with MIDI Tools, using the scale_name key. When there is no active scale, the value of the scale_name key will default to "Chromatic".
- In the Max for Live API, added a new get/set/observe Song.scale_mode property that gives access to the Scale Mode toggle in Live.
- The Max for Live window can now be opened from the View menu, even when there are no Max for Live devices in the Live Set. The associated keyboard shortcut is [CTRL][Shift][Alt][M] (Win) / [CMD][Shift][Alt][M] (Mac).
- In Max for Live API, the Track class now has a gso property called back_to_arranger, which works similarly to Song.back_to_arranger but provides access to the Single Track Back To Arrangement feature.
- Max for Live modulator devices now use less CPU power.
- The following Looper properties are now available in the Max for Live API: record overdub play stop clear undo half_speed/double_speed half_length/double_length record_length_index/record_length_list overdub_after_record loop_length tempo

**Session View**

- In an unfolded Session View Instrument Rack chain, dragging and dropping a device into the empty area below clip slots, will now only replace or insert the device in the chain where the new device is being dropped onto, rather than the parent chain.
- Updated the behavior of the Scene Tempo and Scene Time Signature fields in the Main track: Scene Tempo and Scene Time Signature fields in the main track are now visible by default. The View menu Scene Tempo and Time Signature entry is now the main control for toggling visibility of the Scene Tempo and Scene Time Signature fields, with the state dictating whether extending the main track will re-display the fields. The Scene Tempo and Time Signature command is now also available via the main track’s context menu.

**Setup**

- Removed the restriction of eight hours of maximum recordable sample length. Live should now be able to record audio continuously for approximately 17 hours.
- The audio test tone will now automatically stop when the Settings window is closed.
- Made the following changes to the Windows installer for Live: The installer now supports HiDPI. Two nested installers are no longer shown and all user interaction is done in one installer interface. The Start menu entry is now installed per machine, i.e., for all user profiles. Previously, the entry would only appear in the Start menu of the installing user’s profile, even though Live was installed for all users. Added a Launch button on the success page of the installer, which allows to directly launch the installed version of Live. Fixed an issue where the icon of the Start menu shortcut was a placeholder until rebooting. Fixed a bug where when replacing an existing installation, the entry listing the previous installation would remain in Windows's "Add/Remove Programs".

**Tuning Systems**

- The tuning system name displayed in the Tuning section of the browser and the Info View header no longer shows the “.ascl” or “.scl” extension. Note that Live Sets created in 12.0 that have a tuning system loaded will still display the tuning system name with the corresponding file extension until the tuning file is reloaded.
- When a tuning system is loaded and the Bypass Tuning toggle is enabled on a MIDI track, the Track Tuning MIDI Controller Layout and Configuration options are now greyed out.
- It is now possible to adjust the lowest and highest notes in a tuning system, allowing for a range of fewer than 128 notes. When setting the lowest note, the total number of notes is maintained, and the highest note is shifted to keep the range intact. Setting the highest note lets you decrease the range to less than 128 notes. If you attempt to increase the highest note beyond the current 128-note range, the lowest note will automatically adjust to maintain the maximum range of 128 notes.
- If a custom controller layout becomes invalid due to switching to a tuning system with incompatible values, the invalid values will now be grayed out in the layout customization dialog.

### Bugfixes

**Live Bugfixes**

- The Scale Mode toggle in the Control Bar now has an outlined focus frame when it is focused using keyboard navigation.
- Fixed an issue that could cause Meld’s limiter to distort.
- The Filter On/Off toggle in the Corpus effect no longer displays incorrect text.
- Made the following minor adjustments to Roar’s UI: Correct background colors are now used for the breakout view meters. The filter types labels now use all capital letters.
- In Session View, when hovering above the chain volume sliders in an expanded chain mixer, the cursor is changed to a double-arrow to indicate that the volume section can be resized by dragging up or down.
- Accessibility: Improved screen reader announcements for note velocity.
- The UI panel in the Tuning section now uses the correct color.
- If the Show Scroll Bars preference is set to When Scrolling, scrollbars will now be shown when scrolling occurs while dragging and dropping content.
- Accessibility: Fixed a bug where changing the label section in the browser using object navigation from a screen reader wouldn’t update the content list.
- Fixed an issue in Roar where animated UI widgets such as the shaper curve or filter curve would flicker at large buffer sizes.
- It is no longer possible to tag factory Packs via the Tags Editor.
- Fixed an issue where, depending on the total number of samples, performing with Round Robin in the Other mode would seemingly skip a sample.
- Fixed a bug where the expanded view was missing a focus outline even when it was the active view.
- Fixed a couple of small issues in Meld: The Engine A/B Volume parameter can now be mapped to macros as normal. The Oscillator Type list now wraps around when using the Previous and Next buttons.
- When entering the name of a non-existent tag while searching for tags with the # symbol, a warning message is now displayed informing the user that a tag of that name does not exist. If the user presses Return at this point the search input will not be saved as a tag but remain in the search field as a plain text.
- When applying a note transformation via a MIDI Tool that produces no visible change (such as quantizing a note that is already on the grid), a step is now generated in the undo history.
- When running a similarity search from within an existing search, the browser will now scroll back to the top of the list of results instead of remaining at the position of the previous search.
- Fixed a bug that prevented audio tracks over 2 GB from being frozen or consolidated.
- Accessibility: Fixed an incorrect accessible name on the audio editor timeline in Clip View. Also cleaned up excess speech when navigating the audio editor.
- Fixed an issue where adding a tagged item to the User Library or Collections would not display the associated tag in those locations until Live was restarted.
- Fixed a bug in the Arrangement View mixer where double-clicking on a device in the browser to load it onto a selected Rack chain would insert the device after the Rack itself instead of the selected chain.
- Fixed some UI layout issues in Live’s Settings that caused some translated text to be cut off.
- Fixed a bug in Plug-Ins Settings that caused Live to scan for plug-ins even after canceling the folder chooser that opens after enabling the “Use VST2 Plug-In Custom Folder" or "Use VST3 Plug-In Custom Folder" option.
- Fixed a bug where built-in devices that were saved to the Collections label in Live 11 would be shown as unloadable folders when displayed in Live 12.
- Fixed a crash that occurred after dropping a sample onto a selected Drum Rack Pad that already contained an instrument.
- Fixed two small bugs in the Roar device: Values for the Blend parameter can now be set and adjusted using arrow keys. The Noise modulator no longer resets to 0 when the device is reactivated.
- Fixed a crash that occurred when simultaneously selecting time or tracks in the Arrangement View while moving through tracks in the Arrangement mixer.
- Fixed a bug where the oscillator transpose parameters on Push didn't have an effect when Meld was following the clip scale.
- Fixed an issue that prevented cropped or reversed samples from being swapped out when using the Swap to Next/Previous Similar Sample buttons in Simpler.
- Accessibility: The status of playing clips in Session View (e.g., playing, triggered, stopped) is now available via screen reader announcements.
- When using a second window, the Clip View’s height will no longer reset after selecting an empty clip.
- Accessibility: Screen reader announcements for track names now include their status, e.g., armed, soloed or frozen.
- Roar now uses the correct UI colors when it is a part of an inactive group.
- The browser now displays the message “No results” or “No content” more reliably.
- Reduced the gap between Preference Page Chooser rows.
- The CC Control MIDI effect is now available in all Live editions.
- Accessibility: Added the following fixes: Fixed a bug that caused some sliders to be inaccessible. Fixed an issue that caused some sliders to be excluded from the "Speak Min and Max Values for Sliders" accessibility option. Fixed a bug which caused some hidden controls to take screen reader focus.
- Missing separator lines in the Audio and Link, Tempo & MIDI Settings pages have been re-added.
- In the Connect MIDI Tool, the correct Info View description is now shown for the Spread control when hovering over the space surrounding the control.
- In the MIDI Note Editor, the time selection is now updated when inverting the note selection.
- Accessibility: Fixed the following issues: The controls in a device’s expanded view are now wrapped in a group. Fixed a bug which caused some buttons to not have a name.
- Fixed a bug where resizing the Arrangement mixer in a second window while the Clip and Device Views were expanded caused the second window to briefly and erratically change in height.
- When quantizing note ends, if the nearest quantization point is over or before the note start, the note will now be quantized to the next quantization point. This prevents invalid note lengths.
- Removed an internal-use parameter mistakenly displayed in envelope choosers for Analog, Electric, Collision, and Tension.
- The Similar Sample Swap controls are now hidden in nested Drum Racks (i.e., a Drum Rack within a drum pad).
- Fixed an issue where a multiple clip selection would start in a different clip slot than expected.
- Fixed an issue that caused name fields in the CC Control device parameters, Rack macros, and Drum pads to be displayed slightly off-center.
- When clicking on a slot or scene in the Session View while the mixer in the Arrangement View was visible in another window, Live would scroll the Session View erratically and potentially start to drag content, leading to things like unwanted reordering of scenes or moving of clips. This behavior is now fixed.
- The rows in the MIDI Input section of the Link, Tempo & MIDI Settings are now aligned correctly.
- Corrected the height of the bottom margin of a second window.
- Fixed an issue that cause saved User Labels to display no results if the custom tag that was used to generate the contents within the label was renamed.
- Fixed an issue on Windows that could cause Live to sporadically crash when exporting video.
- Fixed a bug where the mixer volume section would disappear and it would be impossible to resize the mixer when the Live window was made smaller.
- Fixed a bug that prevented the [E] key actions (e.g., note splitting) from working in the MIDI Note Editor when in Live’s second window.
- The device insert marker in Rack devices now uses the background color of the divider line between devices.
- Fixed a bug where using Undo on moving warp markers would undo the movement in very small increments, requiring a lot of undo steps to get back to the previous state.
- Fixed a crash that occurred due to invalid note lengths in the Arpeggiate MIDI Tool.
- CC 119 is now part of the list of available CC Messages in CC Control.
- In the Phaser-Flanger device, the color of the separator lines between different UI elements is now more visible in dark themes.
- Fixed an issue that occurred when using the Stacks MIDI Tool with a Drum Rack, where the Chord Root parameter would correctly refer to drum pads on the first chord's root pitch parameter, but would use note names instead after adding a new chord.
- Fixed an issue with multi-clip editing where selected notes in non-focused clips would remain selected when interacting with the Velocity or Chance editors, even though those editors don’t show notes in non-focused clips.
- Fixed a bug that prevented users from deleting automation breakpoints using the Delete command in the context menu.
- Fixed a bug where extending the note selection with the shortcut [OPT][Shift] + down arrow key would not work correctly when two notes with the same pitch were selected.
- Fixed an issue where the device expanded view would reopen after dragging it closed.
- Accessibility: When using the Stacks MIDI Tool, the C# note on the Root Pitch dial is now announced as “C sharp” (previously the “sharp” was omitted).
- Fixed an issue with spacing below the transport bar becoming too large when resizing the Clip View or device expanded view all the way to the top.
- Accessibility: In MIDI Tools, the key names in pitch controls are now announced using the note name along with their corresponding spelling preferences (i.e., sharp, flat) and tuning options.
- Fixed a UI issue that occurred when duplicating a device with an expanded breakout view.
- Fixed a bug that could cause the Indexer to freeze while analyzing certain MP3 files on Windows.
- Folder names containing the | character can once again be used in the browser.
- On Windows, fixed an issue where the Status Bar would get cut off when the Live window was made smaller.
- Fixed a few issues in the Recombine MIDI Tool: The Rotate display doesn’t silently catch focus anymore, the focus goes to the Rotation Steps parameter. If the number of rotate steps exceeds the maximum available, the selected bar is centered and is not displayed wider than usual. After making a time selection, the bars in the Rotate display update correctly. Fixed the software text for the Shuffle parameter.
- Fixed a bug in the Arpeggiate MIDI Tool where generated notes would sometimes start at the edge of the input time range, causing generated notes to fall outside of the range.
- When selecting a new lane to add from the lane selector in the MIDI Note Editor, the newly selected lane becomes the active lane and the controls at the bottom of the Editor are updated accordingly.
- Updated the UI color of the Seed, Time Warp and Recombine MIDI Tools when the panels are deactivated.
- Fixed an issue where Live could be installed on Windows computers that did not meet in the minimum system requirements, but would not start when the program was launched. Now, it is no longer possible to install the program at all if the system requirements are not met.
- A grid settings chooser is no longer displayed in the header in unwarped audio clips.
- Fixed some small issues when using the Add Interval option with Drum Racks or sampled instruments: When not all key tracks are in use, Add Interval no longer generates notes on unused/invisible tracks. The Interval parameter no longer shows a unit, e.g., “st” or “sd.”
- Fixed an issue where the text in Live’s Settings would be cut off in some languages.
- Fixed an issue that caused vertical scrolling to move too fast when adjusting values in the MIDI Note Editor’s MPE and Envelopes view modes.
- When using the Fold mode in the MIDI Note Editor, the Seed, Shape and Rhythm MIDI Tools will no longer automatically shrink key tracks by hiding unused tracks.
- Fixed a performance regression that occurred when resizing tracks in the Session View with Sets containing hundreds of scenes.
- Accessibility: Fixed a bug where toggling a checkable menu entry would incorrectly announce the new checked or unchecked state of the menu entry.
- Fixed an issue on Windows where the title bar of Live’s window would be cut off when launching the program with a window size larger than the available screen size (for example, if the display scale setting was changed on Windows).
- Fixed an issue where the Info View descriptions for parameters in the Euclidean and Velocity Shaper Generators were duplicated or missing in some cases.
- Fixed an issue where the “Follow System" option for the "Show Scroll Bars" preference in Display & Input Settings was ignored when starting Live for the first time.
- Fixed a crash that occurred when redoing the action of moving a group track that contains an Instrument Rack device.
- The Randomize Velocity option now works as expected again.
- Fixed the following keyboard input issues: Typing a space as the first character no longer enters edit mode on enumeration value sliders and doesn't block the global play/stop command. Typing a value that is outside of the available choices now correctly has no effect. Previously, the invalid value would be stuck in the edit field.
- Fixed a crash that would sometimes occur when moving tracks with the keyboard using the [CTRL] (Win) / [CMD] (Mac) key with arrow keys.
- Accessibility: Fixed a bug that caused Live to lose focus in the Settings dialog.
- The Pitch effect will now always appear the same width regardless of whether it is locked to a control surface (i.e., regardless of whether the hand icon is showing in the title bar).
- Fixed a bug where a Similarity Search could not be triggered using the View menu or the context menu in the browser when the file has not been analyzed in the background.
- Fixed a bug that caused slowed installation times when replacing an existing installation on Windows.
- Fixed a visual issue where text would be cut off when renaming Arrangement locators.
- In the Max for Live API, the performance when calling API functions with large dictionaries as inputs (e.g. apply_note_modifications) has been greatly improved.
- Fixed a crash that occurred when moving a group track and then undoing that action in certain scenarios.
- Fixed a crash that occurred when dropping a file into the File Manager when replacing missing files in a Set.
- Accessibility: Fixed an issue that prevented the Live 12 Trial from being authorized when using certain screen readers on Windows.
- Fixed a crash that occurred when replacing a missing sample in Simpler via the File Manager.
- Fixed a visual issue that caused the initial layout of the Main track to be misaligned when the “Show Scroll Bars” option was set to “When Scrolling”.
- Fixed a crash that could occur when quitting Live.
- Updated the bundled Max version to 8.6.2 hot fix release 3191a3e. This fixes the following issue: Live no longer requires admin credentials when launched from a secondary user account.
- Fixed an alignment issue in Live’s Audio Settings when the warning dialog about configuring inputs/outputs was shown.
- Fixed a bug in the Stacks MIDI Tool that caused the Root parameter to behave erratically when using Drum Racks. Now the parameter stops at the last pad in the Rack as expected.
- Fixed a crash that occurred when resizing multiple clips on different tracks, undoing the action, and then resizing again.
- Fixed a crash that could occur when resizing the video window on Windows.
- Fixed a bug where chain lists in Racks would become slightly misaligned when switching the Show Scroll Bars option between When Scrolling and Always.
- Fixed a crash that would occur in rare cases when audio with infinite volume was routed into Live.
- Fixed the behavior of commands when the content menu is opened via the computer keyboard in audio and MIDI clips so that auto-warp commands, such as Set 1.1.1 Here or Warp From Here, now use the current position of the insert marker.
- Fixed a bug where some Live Clips based on locked Racks, such as Grain Slap 136 bpm.alc, would fail to open in certain Live editions.
- Fixed a bug that prevented options in the context menu of audio and MIDI clips from working as expected when the menu was opened using the computer keyboard and a clip start marker or the loop brace was selected.
- Fixed a bug where navigation with the arrow keys from a scene to the clip slots was not possible if return tracks were folded. Now the selection is moved to the last track before any hidden return tracks.
- Fixed a bug that caused the Crossfader horizontal slider to be misaligned if the Main track was wider than the default size. Fixed a bug where a configured plug-in parameter value would become locked when clicking in the middle of the parameter’s horizontal slider.

**Max for Live Device Bugfixes**

- Max for Live patches located in nested subfolders in the User Library will now correctly be listed in the Max for Live label as well.
- Unmapping a Max modulation source from a Max for Live parameter now clears the modulation value.
- Fixed a bug where the GUI of a Max MIDI Tool would remain accessible and editable even when the selected track was frozen.
- Fixed visual glitches that occurred after clicking away from a Max for Live device or MIDI Tool, such as unnecessary triggering of note selection or drag behaviors in the MIDI Note Editor.
- Fixed a bug that affected the load time of Live Sets containing certain Max for Live devices.
- Fixed an issue where renaming a Max for Live file in the User Library made it impossible to load the same file from the Max for Live label.
- Fixed the following issue with Max for Live devices: Modulators can now only have one Map button active across all devices. In DS devices voices are now never muted before the end of envelopes. In Note Echo, fixed a bug where C-2 would not be echoed.
- Fixed a bug that caused the Save As dialog to be shown every time a user-created Max for Live MIDI Tool was saved using the regular “Save” command due to the default Max MIDI Transformation.amxd and Max MIDI Generator.amxd presets being marked as read-only.
- Fixed a bug in DS Clap where the first note played after adding the device would have an unexpected sound.
- Improved performance of Sets containing Max for Live instruments and audio effects.
- In MPE Control and Expression Control, fixed an issue where two-breakpoint curves with the second breakpoint at the maximum values (127 127) would be slightly off.
- Fixed a crash that occurred when loading certain Max for Live devices with MIDI routings.
- Fixed a bug that would display the class name of a Max for Live MIDI Tool in the Status Bar instead of the Tool's actual name.
- The default save locations for Max for Live MIDI Tools are now set to User Library/MIDI Tools/Transformations and User Library/MIDI Tools/Generators.

## 12.0.2 (April 18, 2024)

### Bugfixes

- Accessibility: Fixed an issue that prevented the Live 12 Trial from being authorized when using certain screen readers on Windows.

## 12.0.1 (March 14, 2024)

### New Features and Improvements

- When accessing the Live Manual through the Help menu, users will now be redirected to the version of the manual corresponding to the version of Live they are using.

### Bugfixes

- Content from the Orchestral Strings, Session Drums Club and Session Drums Studio Packs is now correctly authorized in Live Standard.
- Fixed broken links in the German language version of the "What's New in Live" lesson.

## 12.0

### New Features

Please note that for Mac installations Live 12 is only supported on macOS Big Sur or higher.

Accessibility Browser Filtering and Tags CC Control Keyboard Navigation Keyboard Workflow Meld MIDI Note Editing Operations MIDI Note Probability Groups MIDI Tools Max for Live MIDI Tools Mixer in Arrangement Pitch and Time Utilities Roar Scale Awareness Screen Reader Support Similarity Search Similar Sample Swapping Toggle Clip View Alongside Device View Tuning Systems UI View Styling

**Accessibility**

Improved accessibility support on macOS and Windows; this includes many updates such as new themes with high-contrast variants, improved organization of Live's Preferences menu, as well as support for screen reader software and other assistive devices. While any screen reader software should work, we recommend VoiceOver (Mac) and NVDA (Win) for the best experience.

In Live’s Options menu, there is a new Accessibility entry which contains commands corresponding to different accessibility preferences, such as "Speak Menu Commands" and "Speak Minimum and Maximum Slider Values".

As part of the accessibility implementation, many improvements for keyboard navigation and keyboard workflows have also been added. You can find out more about these updates in the related subsections of the release notes.

**Browser Filtering and Tags**

The browser now includes a set of filters which can be used to search and find specific content using descriptive tags.

Relevant filters are displayed based on which category of the browser is selected. To search with all available filters, use the All label in the browser’s Library. Filter Groups can be hidden/shown by right-clicking the Filters header in the browser, or by right-clicking on individual Filter Group names.

You can search for content and tags in the following ways:

- Select filters and tags in a browser category. Use [CTRL] (Win) / [CMD] (Mac) to multiselect tags within the same Tag Group.
- Use the browser's search bar (corresponding filter results will also be displayed).
- Search for specific tags in the search bar using the format: #[tag]. For example, if you are looking for samples tagged as "punchy", type "#punchy." Autocomplete suggestions for tags will be shown as you type.
When viewing populated filter results, you can save the current search using the Add Label button to the right of the Results header in the browser content pane. Once saved, a custom label is created in the browser's sidebar that contains the filter results. As new items are tagged, the content will also be updated in any relevant saved custom labels.

You can use the toggle to the right of the filters to show/hide the Tags Editor. A collection of default tags is included for all of Live’s built-in content.

The Tags Editor lists all tags in each filter and you can create new user tags for any filter by clicking Add Tag... at the bottom of the Tags Editor.

New Tag Groups can be created by clicking Add Group... in the Tags Editor. User created tags or tag groups can be deleted or renamed via their [right-click](Win) / [CTRL-click](Mac) context menus.

Tags can be assigned to/removed from the selected item in the browser content pane by clicking the checkboxes next to the tag names in the Tags Editor.

Note that tags have replaced folder groups within the browser’s category labels.

**CC Control**

CC Control is a new utility device that can be used to send MIDI CC messages to hardware devices, or used in automation lanes on MIDI clips to send out MIDI CC data during a performance.

There are default controls for mod wheel, pitch bend, and pressure data, as well as several additional custom controls that can be configured for individual MIDI messages. The custom controls also appear on Push for easy navigation.

The Custom A button control can be used to send Sustain messages by default, or if set to another CC message, can toggle between sending minimum/maximum values to a MIDI device.

If CC automation already exists for the same CC message chosen in the device, the data will be merged.

**Keyboard Navigation**

Most of Live’s menus, views and controls can now be navigated using the computer keyboard.

A new Navigate menu has been added to Live's menu bar which contains commands for moving keyboard focus to different areas of the UI, as well as the option to toggle the Use Tab to Move Focus functionality on or off.

When on, the Tab key can be used to switch between different controls in a selected view. The following shortcuts related to this behavior are:

- [Tab] moves to the next control.
- [Shift][Tab] moves to the previous control.
- [CTRL][Tab] (Windows) / [ALT][Tab] (Mac) moves to the next control in the same row.
- [CTRL][Shift][Tab] (Windows) / [ALT][Shift][Tab] (Mac) moves to the previous control in the same row.
When Use Tab to Move Focus is off, pressing the [Tab] key will switch between the Session and Arrangement View, as in previous Live versions.

The Use Tab to Move Focus option can also be enabled in Live's Display & Input Preferences, which also include the additional Navigation and Keyboard options:

- Wrap Tab Navigation - When this option is enabled, navigating with Tab will not stop at the last control in a focused view, but will navigate back to the first control. If the first control is selected, using [Shift][Tab] will navigate to the last control.
- Move Clips with Arrow Keys - This option is enabled by default, and lets you use the left and right arrow keys to move the time selection in the Arrangement View.
Navigation between the previous and next controls of an area, such as a single track in the Session View, can be done using the following shortcuts:

- [ALT] + up arrow key moves to the previous control.
- [ALT] + down arrow key moves to the next control.
To navigate between rows of controls, such as from one track volume slider to another in the Session View, use the following shortcuts:

- [ALT] + left arrow key moves to the previous control in the same row.
- [ALT] + right arrow key moves to the next control in the same row.
You can navigate to different areas of Live’s interface using the following shortcuts:

- [ALT][0] - focus the Control Bar
- [ALT][1] - focus Session View
- [ALT][2] - focus Arrangement View
- [ALT][3] - focus Clip View
- [ALT][4] - focus Device View
- [ALT][5] - focus the browser
- [ALT][6] - focus Groove Pool
- [ALT][7] - focus Help View
Improved keyboard navigation in Live’s Preferences:

- [Tab] and [Shift][Tab] keys can be used to navigate between options inside the Preferences tabs. These shortcuts work regardless of whether the Use Tab to Move Focus option is active or not.
- When focusing on the options inside Preferences tabs, up and down arrow keys can be used to change the state of a toggle, make adjustments, or cycle through the available options for a given preference.
- For options that utilize toggle buttons, it is possible to toggle between states or trigger an action by using the [Enter] key.
- It is possible to navigate the Preference Page Chooser using [ALT][Tab] and [Shift][ALT][Tab] or the up and down arrow keys when the chooser is focused. If the keyboard focus is inside any given Preferences tab, use the [Shift][Tab] shortcut once or more to return the focus to the Preference Page Chooser.
Additional keyboard navigation improvements:

- It is now possible to use keyboard shortcuts to navigate to identical controls across tracks in the Arrangement View. Enabling the Navigate menu's Use Tab Key to Move Focus command and using the shortcuts [ALT][Tab] and [Shift][ALT][Tab] will jump from the currently selected control to the same control in the next or previous track.
- In Session View, the [PgUp] and [PgDwn] keys now move up or down by eight scenes at a time, instead of jumping to the first or last scenes.
- When focused on a track's Session slot, Arrangement lane, or mixer controls, pressing [Esc] will jump to that track's header.
- On Windows, the [ALT] key now behaves as it does in other applications. Pressing [ALT] without a corresponding shortcut key will focus the Global menu, which can then be navigated using the arrow keys or alphanumeric keys as expected.
- The behavior of radio button keyboard navigation is now consistent with other applications on macOS and Windows: When navigating to a radio button group using [Tab] or [Shift][Tab], the selected radio button will be focused, instead of the first or last one in the group. When using Previous/Next Neighbor navigation with [CTRL][Tab] or [CTRL][Shift][Tab] to focus a radio button, the selected radio button will be focused, instead of the first or last one in the group.
- Added a Mixer entry to the Navigate menu, which brings focus to the mixer in the Arrangement View. The corresponding keyboard shortcut is [Shift][ALT][M].
- It is now possible to tab to some links in Live’s UI. Note that currently, focused links do not appear focused.

**Keyboard Workflow**

Various keyboard shortcuts have been added and updated to make it easier to work and navigate in Live directly from a computer keyboard.

Shortcuts that contain a single letter key, such as [S] to solo a track, can now be used even when the Computer MIDI Keyboard is enabled by adding [Shift], e.g., [Shift][S].

The [Delete] key can be used to return radio buttons (for example, track volume buttons) to their default state.

Tracks can be frozen using the new shortcut [CTRL][ALT][Shift][F] (Win) / [CMD][ALT][Shift][F] (Mac).

A new submenu called Clip Markers has been added to the Edit menu, which allows you to set clip start, end, and loop markers to MIDI clips when in Clip View. The corresponding shortcuts are also available in the [right-click](Win) / [CTRL-click](Mac) context menu in the MIDI Note Editor:

- [CTRL][F9] (Win) / [CMD][F9] (Mac) - sets the clip start marker to the selected time area of the MIDI Note Editor.
- [CTRL][F10] (Win) / [CMD][F10] (Mac) - sets the clip loop start marker to the selected time area of the MIDI Note Editor.
- [CTRL][F11] (Win) / [CMD][F11] (Mac) - sets the clip loop end marker to the selected time area of the MIDI Note Editor.
- [CTRL][F12] (Win) / [CMD][F12] (Mac) - sets the clip end marker to the selected time area of the MIDI Note Editor.
The new command Move Insert Marker To Playhead in the Playback menu, also accessible via the shortcut [CTRL][Shift][Space] (Win) / [CMD][Shift][Space] (Mac), will move the Arrangement insert marker to the location of the playhead.

Some shortcuts can now be momentarily latched. This means you can hold down the shortcut key and briefly toggle the shortcut action. After releasing the key, Live’s UI will return to its previous state. Momentary latching becomes available after holding down a shortcut key for about 500 ms. The following shortcut keys can be momentarily latched:

- [A] - toggles Arrangement automation mode
- [B] - toggles Draw Mode
- [S] - toggles soloing or un-soloing the selected track
- [Z] - toggles zooming into the Arrangement selection
- [F1] through [F8] - toggles the Track Activator switch on and off for the first eight tracks
- [Tab] - toggles between Arrangement and Session View
If needed, momentary latching can be turned off using the Options.txt entry: -DisableHotKeyLatching

In the MIDI Note Editor, if the insert marker is selected, you can use [ALT] + the up and down arrow keys to select the next and previous notes.

In the MIDI Note Editor, it is possible to adjust note velocity and chance with the following keyboard shortcuts:

- Adjust note velocity: [ALT] up and down arrow keys (Win) / [CMD] up and down arrow keys (Mac)
- Adjust note velocity deviation: [ALT][Shift] up and down arrow keys (Win) / [CMD][Shift] up and down arrow keys (Mac)
- Adjust note chance: [CTRL][ALT] up and down arrow keys (Win) / [CMD][ALT][Shift] up and down arrow keys (Mac)
It is now possible to resize an Arrangement clip with the keyboard by putting the insert marker at either edge of the clip, pressing [Enter] and then using the left or right arrow key to resize. Pressing [Enter] again will apply the resize action. Pressing [ESC] will cancel the resize action.

The commands Fold/Unfold Selected Tracks [U] and Collapse/Unfold All Tracks [Shift][U] have been added to the View menu.

The keyboard shortcut for the Control Bar's Follow switch was changed to [ALT][Shift][F].

Updated keyboard shortcuts for the View menu's Browser and Groove Pool entries, and introduced a new keyboard shortcut for the View menu's Help View entry:

- Show/Hide Browser: [CTRL][ALT][5] (Win) / [CMD][ALT][5] (Mac)
- Show/Hide Groove Pool: [CTRL][ALT][6] (Win) / [CMD][ALT][6] (Mac)
- Show/Hide Help View: [CTRL][ALT][7] (Win) / [CMD][ALT][7] (Mac)
When the Computer MIDI Keyboard is enabled, all hotkeys on the first and home rows are disabled to prevent causing unexpected changes to a Set when hitting a wrong key.

Added a shortcut for toggling Record in the Session View: [CTRL][Shift][F9] (Win) / [CMD][Shift][F9] (Mac).

The keyboard shortcut for the metronome was changed to [O].

**Meld**

Meld is a powerful and versatile bi-timbral macro oscillator synthesizer that comes with Live 12 Suite. Meld’s deep sound-shaping capabilities can be used to create evolving textural sounds, rhythmic drones, harmonic effects, atonal sounds and more.

Meld features two macro oscillator engines (A and B) which can be layered to create a wide variety of sounds. Each engine is a full synth on its own, and offers unique shaping and tonal variations depending on the chosen oscillator type.

Two envelopes are available for Amp and Modulation per engine, which both offer various looping modes. The Link toggles can be used to apply the same envelope or filter settings to the A and B engines.

A diverse set of modulation routings are accessible in a fully mappable and expandable matrix. Meld also contains two LFOs for each engine: the first is an LFO waveform that is fed into an LFO FX section that contains two possible effects which can be used to finely tune the resulting modulation, and the second is a simple LFO that can be used for standard LFO modulation.

Several filter options are available for each oscillator engine, as well as two scale aware resonator choices in the Filters section. Individual panning, tone, and volume controls can be used to further refine each engine’s sound independently. The Tone control is a combined low/high-pass filter that can be used to round out the signal before it reaches the device’s final output.

The Settings tab contains Glissando, Portamento, and Glide Time options for each engine, as well as Osc Key Tracking toggles. When Osc Key tracking is off, the oscillator will play at a constant pitch of C3 for all MIDI notes or, if using a scale, at the root note of the scale in the C3 octave. It is also possible to enable scale awareness for the oscillators or filters.

In Meld’s Global section, you can choose between Poly or Mono voice mode, set the Stacked Voices amount (similar to unison voices), add a bit of saturation with the Drive control, and adjust the global volume.

Meld’s deep modulation and routing capabilities allow for playful and expressive performances with Push 3 and other MPE controllers, but Meld also provides expressive playfulness with non-MPE devices.

**MIDI Note Editing Operations**

New commands for editing MIDI notes have been added, making it quick and convenient to adjust notes directly in the MIDI Note Editor.

Split divides a note into two or more parts by using either the mouse or computer keyboard. Note that in order to use this functionality with the mouse, Draw Mode must be switched off.

Split with mouse – Hold [E] and click inside a note at the desired location or drag vertically across it to split it. You can split multiple notes simultaneously in the same way: make a note selection, then click at the desired location in any of the selected notes to split them or drag vertically across the selection to split the notes.

Split with keyboard – If no note is selected, press [CTRL][E] (Win) / [CMD][E] (Mac) to split the note at the insert marker location or at the boundaries of the time selection.

Chop divides selected notes into multiple parts based on the current grid settings or in equal parts, either by using the mouse or computer keyboard.

Chop with mouse – Hold [E][CTRL] (Win) / [E][ALT] (Mac) and hover the cursor over a note, so that the cursor changes to an arrow and dashed line symbol. Click on a note and drag up to divide the note into equal parts, increasing by one as you drag up. You can hold the [Shift] key together with the shortcut and the number of equal parts will increase by a factor of two as you drag up (note that [Shift] will have no effect if the Computer MIDI Keyboard is switched on). The same operations can be applied to multiple notes simultaneously.

Chop with keyboard  – Use the shortcut [CTRL][E] (Win) / [CMD][E] (Mac) to chop notes into parts based on the current grid settings. While still holding the shortcut keys, you can use the up and down arrow keys to divide notes into equal parts instead of grid steps. The up arrow key adds more divisions, while the down arrow key uses fewer divisions. If you add the [Shift] key, the up and down arrow keys will divide notes by a power of two (note that [Shift] will have no effect if the Computer MIDI Keyboard is switched on).

It is possible to split and chop notes in Notes and Expression view modes.

Join creates a single note from all selected notes that have the same pitch. Any MPE envelope data will be preserved when notes are joined. Use the Join Notes Edit menu command, the context menu option in the MIDI Note Editor, or the shortcut [CTRL][J] (Win) / [CMD][J] (Mac) to join selected notes.

Span (Fit to Time Range) extends selected notes so that their start and end times match the current time selection. For example, if you select multiple notes that have varying end times within a time selection of the first two bars of a four bar clip, using Span will adjust the notes so that they start at 1.1.1 and end at 3.1.1. Use the Fit to Time Range context menu option or the shortcut [CTRL][ALT][J] (Win) / [CMD][ALT][J] (Mac) to span notes.

When using letter-based shortcuts, such as [E] to Split, make sure that the Computer MIDI Keyboard option is switched off so that the keyboard triggers the shortcut and not a MIDI note. Alternatively, you can add the [Shift] key to the shortcut in order to be able to use it while the Computer MIDI Keyboard is on (note that operations that use shortcuts which include the [Shift] key will have no effect in that case).

**MIDI Note Probability Groups**

A single Chance value can now be assigned to a group of notes so that either all notes play according to the set probability, or only one note out of the group plays at a time.

There are a few different ways to group note probabilities together:

- Use the Edit menu command Group Notes (Play All).
- Use the shortcut [CTRL][G] (Win) / [CMD][G] (Mac).
- Use the [right-click](Win) / [CTRL-click](Mac) context menu option Group Notes (Play All) or Group Notes (Play One) in the MIDI Note Editor.
Once grouped, a single marker will be available for the set of grouped notes in the Chance editor. The marker will have a diamond handle (Play All) or triangle handle (Play One) rather than a circle handle, to visually signal that it affects grouped notes, not a single note.

Right-clicking on a grouped note marker lets you pick from two options:

- Play All – All notes will be played (or not) depending on the Chance amount.
- Play One – Only one note in the group will be played at a time based on the Chance amount.
Grouped notes can be ungrouped using the Edit command Ungroup Notes, shortcut [CTRL][Shift][G] (Win) / [CMD][Shift][G] (Mac), or by right-clicking on a grouped note marker and selecting Ungroup Notes. Once ungrouped, individual markers will be available for each note in the Chance editor.

Hovering over a note that belongs to a group now highlights all the notes within the group.

The Status Bar now indicates the Probability Group Type when selecting multiple notes. When all the notes belong to the same group the type is listed explicitly, otherwise it is marked with an asterisk.

The Probability Group Type selected when grouping notes or changing the group’s type will now be used as the default type for the next note group created through the Edit menu or using the [CTRL][G] (Win) / [CMD][G] (Mac) keyboard shortcut.

A small triangle displayed on MIDI notes that have a probability value of <1.0 is now also displayed when a note belongs to a probability group (even if the probability of this group is 1).

**MIDI Tools**

Introduced MIDI Tools, a set of MIDI Transformations and Generators which can be used to automatically shape and create MIDI notes in creative and surprising ways.

In Clip View, two new Tools tabs have been added, one containing transformations and the other generators.

MIDI Transformations:

- Arpeggiate splits up chords into smaller arpeggiated notes based on the chosen pattern settings.
- Connect fills empty gaps between successive notes or chords by adding connecting notes with specified density, length, rate, and pitch settings.
- Ornament adds short strokes (flam) or grace notes at the beginning of existing notes.
- Quantize applies quantization based on the chosen grid options.
- Recombine rearranges the properties of a series of notes so that the pitch, length, or velocity settings of one note in the series are applied to a different note.
- Span adjusts the length of note end times using legato, tenuto, or staccato timing.
- Strum applies an offset to note start times for all successive notes in a chord, starting at either the highest or lowest note.
- Time Warp stretches or compresses notes based on the speed curve as determined by two adjustable breakpoints.
MIDI Generators:

- Rhythm generates a rhythmic pattern of notes and velocity accents.
- Seed randomly generates notes using adjustable pitch, duration, and velocity ranges.
- Shape generates a sequence of notes with varying pitches based on drawn shapes or selected shape presets.
- Stacks generates between one and four chords based on various chord rules that can be further tweaked and inverted.
Each MIDI Tool has an Auto Apply toggle, labeled as Transform or Generate depending on the type of the tool. When toggled on, any changes that are made to the tool’s parameters are applied to notes in real-time. When toggled off, parameters can be adjusted freely, and the changes will only be applied after pressing the Apply button. The Reset button can be used to restore the tool's parameters to the default values.

Changes made to MIDI Tool parameters are saved with Live Sets.

**Max for Live MIDI Tools**

In addition to the built-in MIDI Tools, new Max for Live objects can be used to create custom MIDI Transformations and Generators.

By default, two Max for Live MIDI Tools are included in the Clip View’s Transformation Tools and Generative Tools tabs/panels:

- Velocity Shaper allows transforming note velocities using an envelope.
- Rhythm Euclidean generates a rhythmic pattern of notes.
These tools utilize the new Array and String objects that were recently added to Max 8.6.0.

The Transformation/Generator Selector menu also contains two template devices that can be used as a basis for creating custom Max for Live MIDI Tools. To create a custom MIDI Tool, click on the Edit button when a Max for Live MIDI Tool is selected to open its corresponding Max patcher. You can change the existing parameters and then save the updated patcher as a new .amxd file.

For custom MIDI Tools to show in Clip View, they must be saved to a folder in Live's Places.

In the browser, Max for Live MIDI Tools can be found in the All and Max for Live labels. Max for Live MIDI Tools can also be found using the new filters MIDI Transformation and MIDI Generator within the Device Function filter group.

**Mixer in Arrangement**

The Session View mixer is now accessible in the Arrangement View.

You can click the Mixer View toggle at the bottom right corner of Live's window to expand or collapse the mixer in either the Session or Arrangement View. Using the drop-down menu next to the toggle, you can select which areas of the mixer are displayed, e.g., I/O, Sends, Track Volume, etc.

The mixer can also be opened from the View menu using the Mixer entry or the shortcut [CTRL][ALT][M] (Win) / [CMD][ALT][M] (Mac).

The term "mixer" now refers to the entire subview that contains In/Out, Sends, Returns, Volume, Track Delay, Crossfader, and Performance Impact controls.

You can configure individual mixer sections and Return Tracks using the Mixer Controls entry in the View menu.

The section that contains meters is now called Volume and it currently doesn’t have an assigned shortcut.

The sections to the right of Track Headers in the Arrangement View are now called Arrangement Track Controls. You can configure their visibility as well as the visibility of the Return Tracks in the View menu under the Arrangement Track Controls entry. Arrangement Track Controls no longer have shortcuts assigned to them since these are now used for the mixer sections.

**Pitch and Time Utilities**

In Clip View, the Notes tab/panel has been renamed to Pitch and Time Utilities and has been divided into two sections: Pitch and Time, which contain controls for adjusting note pitch and timing, respectively.

Pitch Tools:

- Fit to Scale moves notes to fit within the current clip scale.
- Invert flips the notes "upside-down" so that the highest note is swapped with the lowest note.
- Transpose adjusts the pitch transposition for notes in either semitones or scale degrees, if the clip has an active scale.
- Add Interval creates new notes at the given number of semitones or scale degrees as specified in the Interval Size parameter.
Time Tools:

- Double stretches notes, the time region, or loop by a factor of 2.
- Halve compresses notes, the time region, or loop by a factor of 2.
- Stretch Factor compresses or stretches notes by a factor that can be set in the range from ÷10 to x10.
- Set Length determines the note length of notes, including fitting note lengths to grid or selected time range.
- Humanize adds an amount of slight random variation to note start times specified in the Humanize Amount slider, ranging from 0% to 100%.
- Reverse reverses notes horizontally around the center of the time selection. If no time is selected, all notes in the clip will be reversed.
- Legato lengthens or shortens each note so that it is just long enough to reach the beginning of the next note.

**Roar**

Roar is a dynamic saturation audio effect that comes with Live 12 Suite. Roar can comfortably move from subtle and precise mastering-grade warmth to wild and unpredictable sound mangling.

Input signals can be routed into one of five different routing modes: Single, Serial, Parallel, Multi Band, Mid Side, and Feedback. In Multi Band mode, Low/High crossover frequencies are available. In Feedback mode, you can blend between the direct and the feedback signal. Drive and Tone controls can be used to adjust the incoming signal before it is sent to the Gain Stage section.

Depending on which routing mode is selected, you can apply a shaper curve to the signal in one or more gain stages. Roar offers a selection of wide saturation shaper curves, varying from subtle to distorted, that can be adjusted further using Amount and Bias controls. Several filter options are available and can be applied before or after the shaper.

There are two LFOs, an Envelope Follower, and a Noise generator for complex modulation possibilities, as well as an expansive Modulation Matrix for easy mappings for most of the device’s parameters. You can use the toggle in the device title bar to access the matrix in an expanded view.

Feedback can be added to define the amount of signal that gets fed back into the device’s input using various time modes. The feedback signal can also be inverted and adjusted with a band-pass filter.

The Compress control lets you determine the amount of masterbus compression, while the global Output control sets the overall processed signal in dB.

**Scale Awareness**

Live 12 offers a new way of choosing and viewing scales, as well as the option of applying scales across MIDI effects and devices.

You can now select or change a scale for clips using the Scale Mode controls in Live's Control Bar.

The Scale Mode controls will also reflect any changes when clips with different scales are played, making it easy to see at a glance which scales are in use in a Set.

When multiple clips are selected with different scale values, these differences are indicated with asterisks in the Current Scale Name and Current Scale Root Note drop-down menus.

When multiple clips are selected with different scale awareness states (e.g., if a scale is active or not), this difference is indicated by partially color-filling the Scale Mode toggle.

When multiple clips are selected, changes to scale settings made in the Control Bar will apply to all selected clips.

In Clip View, when a scale is active, new Highlight Scale and Fold to Scale options appear in the MIDI Note Editor. When Highlight Scale is enabled, the key tracks that belong to notes of the scale will be highlighted in a unique purple color that is used to signify scale awareness throughout Live. When Fold to Scale is on, only the key tracks that belong to notes of the scale will be displayed in the MIDI Note Editor.

When a scale is active, the pitch-related parameters in MIDI Tools and Pitch and Time Utilities will also use the selected scale.

The built-in MIDI effects Arpeggiator, Chord, Pitch, Random, and Scale have new Use Current Scale toggles in their device title bars. When switched on, the clip's current scale will be applied and pitch-based device parameters can be adjusted in scale degrees opposed to semitones.

In the Meld device, it is also possible to enable scale awareness for the oscillators or filters.

**Screen Reader Support**

With the introduction of screen reader support, most of Live's core workflows are now accessible to screen reader users. The following Live features can be used with screen readers:

- Transport controls
- Browser search
- Arrangement View
- Session View
- Clip and Scene properties
- MIDI clip editing
- Native effects and instruments
- MIDI and Key mapping
- Working with grooves
- Tuning systems
The following features are not supported for screen readers in Live 12:

- Browser filtering and tagging
- Audio warping
- Automation, modulation, and MPE editing
- Max for Live devices
- MIDI and audio metering
Third-party devices are supported for screen reader use, but only to a certain extent.

**Similarity Search**

Similarity Search can be used to find sounds similar to a reference file and works with audio samples, instrument presets, and drum presets. Please note that Similarity Search does not support samples longer than 60 seconds.

In the browser, compatible files will include a Similarity Search icon, clicking on which will return a list of sounds similar to the given file. You can also right-click on an item and select Show Similar Files or use the [CTRL][Shift][F] (Win) / [CMD][Shift][F] (Mac) shortcut to view this list. The reference file will be shown in the search field and all relevant similar sounding items will be listed below in the order from most to least similar. The results will be populated in the All label in the browser. To the right of each result is a visual representation of how similar an item is compared to the reference sound.

Custom-saved browser categories will remember and reestablish the sound file on which the Similarity Search was based when the category was saved. Note that in such a custom-saved category, the reference file will not be displayed in the search field when opening the category.

Core Library content is pre-analyzed for sound similarity features. Please note that it might take a while for Live to analyze larger libraries and for the feature to be usable for all files.

A similarity sound analysis section is displayed in the Status Bar when background scanning and analysis are in progress to provide information on the current status. The Pause button next to the analysis state can be used to stop the analysis for sound similarity. While it is a paused, the Resume button can be used to start the analysis again. There are a few different states that are shown:

- Analysis: Scanning - This is shown when new unanalyzed files are detected.
- Analysis: Pending - This displays the number of queued tasks.
- Analysis: Processing - This shows the number of tasks left.
- Analysis: Paused - This is shown when the process has been paused.
- Analysis: Done - This is shown when the analysis has finished.

**Similar Sample Swapping**

In addition to searching for similar sounds, it is also possible to swap samples based on their similarity in the Simpler and Drum Rack devices using Similar Sample Swapping.

In Simpler, you can click the Swap to Previous Similar Sample or Swap to Next Similar Sample buttons at the bottom right corner of the Sample Display next to the Hot-Swap button to load and cycle through similar sounds. Alternatively, you can cycle through samples using the [CTRL] (Win) / [CMD] (Mac) + left and right arrows shortcut.

You can use the Return to Reference context menu option or the [CTRL] (Win) / [CMD] (Mac) + down arrow key shortcut to go back to the original sample that was used as the basis for establishing sound similarity, while the Save as Similarity Reference option or the [CTRL] (Win) / [CMD] (Mac) + up arrow key shortcut can be used to set the currently loaded sample as the new reference sound.

In Drum Racks, the Show/Hide Sample Swap Buttons toggle at the right of the device's title bar can be switched on to display similarity swapping options for both the entire Rack and individual pads:

- Swap All Pads to Previous Similar Sample - swaps all pads in the Rack to the previous similar sample.
- Swap All Pads to Next Similar Sample - swaps all pads in the Rack to the next similar sample.
- Swap to Previous Similar Sample - swaps an individual pad to the previous similar sample.
- Swap to Next Similar Sample - swaps an individual pad the next similar sample.
- Lock Pad for Similar Sample Swapping - locks an individual pad so that the sample is not updated when swapping out samples in the entire Rack.
You can also hold the [ALT] key to temporarily display the similarity swapping options, as well as use the [CTRL] (Win) / [CMD] (Mac) + left and right arrows shortcut to swap previous and next similar samples respectively.

As in Simpler, you can go back to the original sample using the Return to Reference context menu option or keyboard shortcut, or set the currently loaded sample as the new reference sound using the Save as Similarity Reference option or shortcut.

When using Hot-Swap mode with Simpler, Drum Rack, or an individual Drum Rack pad, clicking the Show Similar Files button next to the selected sample in the browser will display similar-sounding samples which can then be loaded into the device as needed.

Note that Similar Sample Swapping does not support samples longer than 60 seconds.

**Toggle Clip View Alongside Device View**

It is now possible to access Clip View and Device View at the same time.

To open both views simultaneously, use the triangle buttons next to the Clip View and Device View Selectors located to the left of the Mixer View toggle in the bottom-right corner of the Live window, or use the keyboard shortcuts [CTRL][ALT][3] (Win) / [CMD][ALT][3] (Mac) for showing Clip View and [CTRL][ALT][4] (Win) / [CMD][ALT][4] (Mac) for showing Device View.

When only one of the views is displayed, you can still switch between them using the [Shift][Tab] keyboard shortcut or by clicking on the respective view selector tab. When both are shown, [Shift][Tab] will move the focus between the two views. (Note that in order for the shortcut to work, the Use Tab Key to Navigate option in Live's Display & Input Preferences must be switched off.)

Holding [ALT] and clicking on either the Clip View or Device View toggle will open both views at the same time.

Note that the width of the Device View when the view is expanded is no longer constrained by the browser, it stretches across the entire application window.

**Tuning Systems**

Live now supports Scala files, which can be used in Sets to access new tuning options apart from Live’s default 12TET tuning. The Live 12 Core Library also includes a set of various tuning systems, which you can find in the new Tunings label in the browser.

You can select the Tuning entry in Live’s View menu or double-click an .ascl file in the browser to open the Tuning panel. When browsing tuning systems in the Tunings label of the browser, a description containing number of notes per octave, short description and defined source for the .ascl file is shown in the Info View.

When a tuning system is loaded, the corresponding pitches will be played when using any of Live's built-in instruments, as well as any MPE-enabled plug-ins and external instruments, provided that the pitch bend range is set to 48 semitones. Note that non-MPE-enabled instruments or instruments with different pitch bend ranges will play out of tune.

Plug-ins and Max for Live MIDI effects will also be adjusted to follow a loaded tuning system. Note that Drum Racks will automatically bypass a loaded tuning system when added to MIDI tracks.

When a tuning system is loaded into a Set, the scale controls and features in MIDI clips and in the Control Bar will be hidden.

In the Tuning panel of the browser, additional options are available for adjusting the reference pitch of a loaded tuning system. The default octave for tuning system reference pitch is set to 3.

The toggle to the left of a tuning system's name can be used to access the details of the tuning system in an expanded view. The following details are taken from the description included in the Scala file and  displayed in Live: Source, Link, and Number of notes per octave.

The details of a tuning system file are displayed in the Info View when hovering over a loaded tuning system's name

A loaded tuning system can be saved as an .ascl file by clicking the floppy disk icon in the Tuning section of the browser.

The Bypass Tuning toggle in the I/O section of the mixer can be used to bypass a loaded tuning system for an individual MIDI track.

It is also possible to configure a track tuning layout for external MIDI controllers using the Track Tuning MIDI Mapper chooser in the I/O section. When using tuning systems with different MIDI controller layouts, it is possible to see the corresponding input key for different notes in the Status Bar when hovering over notes in the piano roll.

You can select a loaded tuning system and press the [Delete] key to return to Live's default of 12-tone equal temperament.

**UI View Styling**

Live’s UI has been modernized and streamlined, making it easier to view at a glance.

The overall appearance of Live's various views (such as the Arrangement View, Clip View, Session View, and Live's browser and Preferences) has been updated as follows:

- New view controls for the browser, the Session/Arrangement View, the mixer, and Info View have been added to the outer corners of Live's window and can be toggled to show/hide the corresponding views.
- New Live Themes have been added with specific options for warm/cool tones and high contrast. Live can also be set to follow your operating system's Light or Dark theme.
- When using a second window, the zoom level of Live’s first and second windows can be adjusted independently in the Display & Input Preferences.
- The Groove Pool selector has been removed for now. The Groove Pool can now be shown/hidden via the new drop-down menu next to the Show/Hide Browser and Groove Pool toggle, and it can still be shown/hidden via the View menu's Groove Pool option.
- The Show/Hide controls for all Session/Arrangement View mixer sections (i.e., In/Out, Sends, Returns, Mixer, Track Delays, Crossfader, and Performance Impact) have been removed. The various mixer sections can still be shown/hidden via the View menu's respective options or using the drop-down menu to the right of the Mixer View toggle.
- The Arrangement View's Clip Overview area, Beat-Time Ruler, and Time Ruler have been visually integrated into the Arrangement View.
- Scrollbars have been redesigned and will now appear as an element inside the scrolled area. A Show Scroll Bars option has been added to the Display & Input Preferences, which can be set to "Always" or "When Scrolling". When selecting the latter, scrollbars will only appear in the UI while scrolling or if the current scroll position changes through another action, such as changing the size of Live’s window.
- Live’s Preferences now use a new tab styling.
- The borders around all of Live's views have been removed.
- All main views now have a slight rounding at their edges.
- The Control Bar now adapts to the application’s window width so that all controls fit within 1280px width screen resolution.

### Feature Improvements

Arrangement View Browser Clip View Devices Device View Interface Max for Live Mixer Improvements Push Improvements Session View Setup Tempo Follower

**Arrangement View**

- MIDI clips can now be reversed in the Arrangement View by pressing the [R] key.
- The full clip content is now displayed for deactivated clips in the Arrangement View.
- A new toggle to the right of the Time Ruler can be used to switch on vertical waveform zooming for all audio clip waveforms. There is also a slider to set the zoom factor, which can be applied in x (multiplied by) or dB (which can be selected using the right-click context menu). The waveforms in the Arrangement View will be displayed using the set zoom level. If there is a positive zoom level set it will also be applied to audio clip waveforms as they are recorded.
- A new Move Clips with Arrow Keys option has been added to the Display & Input Preferences. When enabled, it is possible to move selected clips using the left and right arrow keys in the Arrangement View. When switched off, the left arrow key will collapse the time selection to the start point, and the right arrow key will collapse the time selection to the end point.
- Moving the Insert Marker to the edges of clips with [CTRL] (Win) / [ALT] (Mac) and the left/right arrow keys now works in Automation Mode.
- When selecting a track, take lane or automation lane header in the Arrangement View while the Clip/Device View is open, that lane's content is now also selected.
- The Optimize Arrangement Height/Width toggles in the Arrangement View are now situated underneath the Main track, next to the time ruler and the new waveform vertical zoom controls.
- Comping is now available in all Live editions, including Live Lite. Previously, take lanes were not available in Lite.

**Browser**

- The new All category replaces the “All results” category that previously appeared when entering a term in the search field. When using search, the results displayed in the All category are any items from the entire library (Packs, Plug-ins, Max for Live, User Library and folders) that match the search query, displayed as a flat list.
- Almost all items within the browser’s categories can now be multi-selected.
- When unfolding a Live Set in the browser, the expanded list of tracks now includes the Set’s return tracks and Main track. You can unfold the tracks in the Set to reveal a Devices icon representing their device chains. You can then move these chains into the currently open Set using drag and drop or by double-clicking on the chain. The Device settings from the original Set are retained, but any previously recorded automation is not.
- Sorting plug-ins by Rank in the header of Live’s browser now sorts content by the frequency of use, as expected.
- Users can now view Live’s browser history. The Browse Forward and Browse Back buttons next to the search bar can be used to take a step forward or back in the browser’s history.
- The browser can be opened and closed by dragging away from and towards the window margin, respectively.
- Parts of the browser will now run asynchronously, and therefore won’t block the UI anymore when using large libraries. If needed, asynchronous mode can be switched off using the Options.txt entry: _Feature.Browser.AsyncLoading=off.
- Added a "Browser File Preview" entry to the Options menu. When enabled, this option will automatically play the selected browser item.
- The Sounds category now shows all built-in presets and user presets.
- Core Library updates: New and refined presets for Meld, Roar and Drift. New Instrument Racks: Meld Racks and 808 Selector Rack. New Drum Racks: MPE Meld Kit, Sound Oracle Kits including MIDI Clips. Refined Templates including a new Quick Start Beat Template. Refined Tunings and Browser Tags. Most of the samples and Racks released with Note are now also available in the Live Core library. Operator presets now have Note Pitch Bend enabled. Added the Live 12 Demo Set featuring a song called "Patience" by Chuck Sutton to all Live editions.

**Clip View**

_Editor View Modes_

- The MIDI and audio editing parameters in Live 11’s Tool tabs have been moved to the top of the MIDI Note Editor/Sample Editor and are now stored in different tabs referred to as Editor View Modes. You can cycle to the next or previous view mode using the keyboard shortcuts [ALT][Tab] and [ALT][Shift][Tab].
- In audio clips, the following Editor view modes are available: Sample - displays the audio file and sample editing options. Envelopes - displays the Envelope Editor. This mode replaced the Envelopes tab/panel; the respective controls are now displayed at the bottom of the Envelopes Editor.
- In MIDI clips, the available Editor view modes are: Notes - displays the MIDI Note Editor and Velocity/Chance Editors (except in Live editions where Chance is not supported). The Randomize, Randomize Range, and Velocity Range (renamed to Velocity Deviation) controls previously located in the Notes tab/panel are now displayed at the bottom of the Notes Editor. A drop-down menu can be used to show/hide the Velocity and Chance lanes. A lane header's context menu allows to swap the currently visible lane with a hidden lane, making it possible to quickly change which lane is visible. Envelopes - displays the Envelopes Editor. This mode replaced the Envelopes tab/panel; the respective controls are now displayed at the bottom of the Envelopes Editor. Note that when the Envelopes Editor is open, the Pitch and Time Utilities, MIDI Transformative and Generative Tools tabs/panels are disabled. MPE - displays the MPE Editor. This mode replaced the Note Expression tab/panel. The expression lane names were removed from the lane headers, and they are now displayed when hovering over the lanes. A drop-down menu can be used to show/hide the Slide, Pressure, Velocity, and Release Velocity (previously named "R.Velocity") expression lanes. A lane header's context menu allows to swap the currently visible lanes with hidden lanes, making it possible to quickly change which lanes are visible.

_MIDI Note Editor/Sample Editor Updates_

- The Quantize Settings dialog was replaced by a Quantize tab/panel in audio clips and the Quantize MIDI Tool in MIDI clips. The Edit menu's Quantize command and the [CTRL][Shift][U] (Win) / [CMD][Shift][U] (Mac) keyboard shortcut now open the Quantize Settings controls in their new locations.
- Multiple audio clips can now be quantized at the same time. If the Current Grid option is selected, the Triplets option will now be grayed out.
- Grid Options are now accessible from the Sample/MIDI Note Editor title bar.
- The shortcuts Narrow Grid [CTRL][1] (Win) / [CMD][1] (Mac) and Widen Grid [CTRL][2] (Win) / [CMD][2] (Mac) have been added to the context menus in the MIDI Note Editor and Sample Editor, as well as in the Grid chooser within both Editors.
- Added a Step Input Mode entry to the Options menu, enabled when a single MIDI clip is selected. When activated, Step Input Mode will arm the track containing the clip, focus the Clip View and toggle the Computer MIDI Keyboard, to allow for faster step recording using either the Computer MIDI Keyboard or an external MIDI device. Note that the Step Input Mode menu entry is not a toggle.
- Added clip modulation and MIDI mapping support for the following warp modes: Beats - Transient Envelope Tones - Grain Size Texture - Grain Size, Flux Complex Pro - Formants, Envelope
- Added the Normalize Clip Sample command to the Sample Editor’s context menu.
- The MIDI Step Input buttons are now located next to the Grid Options in the MIDI Note Editor’s title bar when in Key or MIDI mapping mode.
- The Fold to Notes (previously Fold) and Fold to Scale commands were added to the View menu.
- When a scale is enabled in Clip View or in the Control Bar, the Fold to Scale option becomes available in the MIDI Note Editor. A Highlight Scale checkbox also becomes available and allows to switch scale highlighting on and off.
- The Fold to Notes and Fold to Scale modes can be toggled by pressing [F] and [G] keys respectively. Note that if the Computer MIDI Keyboard is on, you need to also add the [Shift] key for the shortcuts to work.
- A "MIDI Editor Note Preview" command has been added to the Options menu.
- The MIDI Editor Preview button is now located above the piano roll.
- When the MIDI Editor Preview switch is enabled, selecting one or more notes using the computer keyboard navigation controls [CTRL] + left/right or up/down arrow keys (Win) / [ALT] + left/right or up/down arrow keys (Mac) will play the notes. When using multi-clip editing, keyboard selection will also work if Focus mode is enabled.
- Added the Crop Clip to Time Selection command to the time selection context menu in the Sample Editor and MIDI Note Editor.
- When cropping MIDI clips, notes that extend beyond the selected cropping range are trimmed to fit within the new clip boundaries.
- The sample information of an audio clip (i.e., the file name, sample rate, bit depth, and channel count) is now displayed in the Sample Editor’s title bar instead of the clip's title bar.
- Loop controls will now be hidden when the Linked switch is toggled in Clip View’s Envelopes panel.
- The duration of note preview when holding down the mouse on the note or the piano roll was increased.
- The Clip Gain slider design has been updated to show a scale representing the highest and lowest possible gain amounts, as well as a colored bar that appears when making adjustments above or below 0 dB. This design now matches the updated meters in the mixer.
- The velocity ramp controls now display the velocity of the first and last note in the selection. They become inactive if the selection has fewer than two notes.
- The Randomize button and Randomize Range slider were moved to the MIDI Note Editor footer in both the Velocity and Chance lanes. Randomize now uses a specific starting point to generate random values every time the button is pressed, making results more predictable as you adjust the amount of randomization.
- The Velocity Range slider was renamed to Velocity Deviation and moved to the MIDI Note Editor footer.

_Additional Clip View Improvements_

- Clip View and Device View can now be toggled open by clicking on the entire length and width of the Clip and Device View Selectors. Previously, the clickable area was smaller.
- Clip View and Device View toggles will now be displayed in yellow whenever the views associated with them are selected.
- The Quantize command [CTRL][U] (Win) / [CMD][U] (Mac) has been improved to apply within a time selection when relevant.
- Added an Invert Selection command to the Edit menu, which inverts the selection of notes in the MIDI Note Editor. Invert Selection is also accessible via the MIDI Note Editor's context menu or the [CTRL][Shift][A] (Win) / [CMD][Shift][A] (Mac) keyboard shortcut.
- It is now possible to label a clip’s notes with their MIDI note numbers instead of accidentals, by using the new MIDI Note Number command in the piano roll’s context menu. Also, the Accidentals/MIDI Note Number setting most recently applied to a clip will now be used for the next created clip.

**Devices**

_Arpeggiator_

- Added a toggle to the device's title bar that collapses/expands the device view.
- Added a Use Current Scale toggle to the device's title bar. When enabled, and if a clip has an active scale, Arpeggiator follows the scale selected in the Current Scale Root Note and Current Scale Name choosers, which is indicated by purple dots on the Root Note and Scale choosers in the device. If a scale is not active, the device follows the scale selected in its own Root Note and Scale choosers.
- Updated the UI of the device to feature a display which includes Style, Hold, Offset, and Groove controls, as well as a visualization of the selected Arpeggiator pattern.
- Added Previous/Next Style Pattern arrow buttons respectively to the left and right side of the Style Pattern visualization, below the Style chooser. The buttons allow cycling through and choosing the rhythmical pattern used by Arpeggiator.
- Adjusted some spacing and rearranged some controls.
- The Distance control is grayed out when Steps is set to 0.
- When Arpeggiator uses a scale (either the current clip scale or an internal scale selected from Arpeggiator’s own transpose mode chooser), the Distance parameter will display scale degrees instead of semitones.
- The Arpeggiator device now transforms per-note pitch bend messages in scale when the Use Current Scale option is enabled.

_Chord_

- Added a Use Current Scale toggle to the device's title bar. When enabled, and if a clip has an active scale, Pitch follows the scale selected in the Current Scale Root Note and Current Scale Name choosers.
- Added a Strum control that can be used to insert a delay between the notes in the chord. The Strum Tension control can be used to accelerate or decelerate the strumming. Note that Strum Tension is only enabled if Strum is activated.
- Added a Strum Crescendo parameter that applies an additional multiplier to the velocities of notes in a chord, in addition to the already existing Velocity parameters. Positive values produce velocities with an upwards ramp, whereas negative values produce velocities with a downwards ramp. The velocity ramp is applied to outgoing notes in the order in which they're played. Note that Strum Crescendo is only enabled if Strum is activated.
- Added a Velocity/Chance toggle that allows adjusting velocity/probability values for each note.
- Added a Learn feature that saves chord parameter settings from its MIDI input. When the Learn button is activated, the Shift and Velocity parameter settings will be overwritten by the next played chord.
- Added LEDs next to each shift dial, to indicate when the corresponding note is played.
- Chord can now send MPE data to notes by enabling the Send Per Note Events to Generated Notes context menu option. When scale awareness is enabled, Chord will transform pitch bend messages so that bent chords stay within the scale.

_Envelope MIDI_

- The ADSR envelope display was updated to allow changing slopes directly in the envelope UI as well as with the Attack, Decay and Release Slopes sliders.
- Envelope MIDI features a new implementation of Sync mode. Note that this may result in a slight sound difference compared to previous device builds.

_Expression Control_

- The UI of Expression Control has been completely overhauled. It is now possible to edit modulation sources in separate tabs, each of which includes its own curve display. As in the other updated modulator devices, the Modulate toggle can be used to apply modulation to a target without taking over the value completely. This new version of Expression Control replaces the older one, which has been renamed to Expression Control Legacy; when opening Live Sets created with Live 11 that contain Expression Control, the legacy version of the device will be loaded.

_LFO_

- A new Steps parameter can be used to adjust up to 24 steps in the selected waveform.
- A new Shape parameter allows to bend or skew the selected waveform.
- Added Stray, a new LFO waveform type.
- Added Glider, a new LFO waveform type.
- A dynamic offset line has been added.
- A 10x toggle for audio rate modulation has been added.

_Max for Live Devices Improvements_

- The LFO, Shaper, Expression Control, Envelope Follower, Envelope MIDI, and Shaper MIDI devices now support modulation; this means that a parameter's relative value can be modulated without taking the value over completely. The behavior can be controlled via the Mod toggle. There are also Modulation Polarity switches which can be used to flip the polarity of the modulation. If the Mod toggle is switched off, any mapped modulation behaves exactly as it did prior to this change, i.e., the parameter value is taken over and cannot be adjusted independently.
- Clip Modulation is now enabled on all built-in Max for Live device parameters.
- The devices now feature faster load times and optimized performance.
- In modulator devices: Non-LCD numboxes now use slider controls. The visual mapping state is canceled after trying to map to a parameter that was already mapped.
- Patch code is formatted and commented consistently, using all latest Max features, for users who open up the devices (note that this does not apply to DS devices).

_Multiband Dynamics_

- The Multiband Dynamics device’s interface has been updated. The Time (Attack and Release) parameters, Above Threshold and Ratio parameters, and Below Threshold and Ratio parameters are now displayed in individual sections.

_Note Length_

- Added a Latch mode, which you can turn on using the new Latch button beneath the Trigger Source switch. Latch mode operates differently based on whether the Trigger Source switch is set to Note On or Note Off. If Note On is selected, latched notes will end when all keys and a sustain pedal (if connected) are released and a new Note On message is received. If Note Off is selected, latched notes will start playing when all keys and a sustain pedal (if connected) are released and a new Note Off message is received.
- Swapped the positions of the Gate and Length knobs.
- Split the Time mode toggle into two separate buttons, now positioned below the Length knob.
- Renamed the "Release Vel.2" control to "Rel Vel".
- Renamed the "Decay Time" control to "Decay".

_Operator_

- Added per-note pitch-bend support to the Operator device, which can be enabled via the Enable Note Pitch Bend context menu entry in the device's title bar. Note: Switching this option off can help preserve a stable pitch when using an MPE controller as input.

_Pitch_

- Added a Use Current Scale toggle to the device's title bar. When enabled, and if a clip has an active scale, Pitch follows the scale selected in the Current Scale Root Note and Current Scale Name choosers.
- Added Step Down/Up (-/+) buttons and a dedicated Step Width slider underneath the Pitch control. The Step Down/Up buttons decrease/increase the Pitch parameter by the distance set in the Step Width slider. All of these controls can be assigned Key and/or MIDI mappings.
- Repositioned the Lowest and Range sliders.
- Added a Mode drop-down menu containing three different modes to choose from: Block, Fold, and Limit. The selected mode determines what happens to notes outside of the range defined by the Lowest and Range parameters.
- The Pitch device now transforms per-note pitch bend messages in scale when the Use Current Scale option is enabled.

_Random_

- Added a Use Current Scale toggle to the device's title bar. When enabled, and if a clip has an active scale, Random follows the scale selected in the Current Scale Root Note and Current Scale Name choosers.
- The Scale parameter has been renamed to Interval to avoid confusion with Live’s new scale features.
- The Mode switch has been split into two separate toggles: Random and Alt.
- Random now transforms per-note pitch bend messages in scale when the Use Current Scale option is enabled.

_Sampler_

- A new Round Robin feature has been added to the Sampler device’s Zone Editor. This feature lets you cycle through samples in four different ways: Forward, Backward, Other, and Random. The Zone Editor also has a Round Robin Reset Interval selector, which resets the counter at a chosen time interval (¼ Bar, ½ Bar, 1 Bar, 2 Bars, or 4 Bars).

_Shaper_

- The Shaper device now offers different play modes: Loop, One-shot and Manual. In the Manual mode, the adjusted shape can be scrolled through back and forth with a dial, while the One-shot mode offers a mappable button to trigger the Shape once.

_Scale_

- If there is an active clip in the track containing the device, Scale's parameters now follow the clip’s Root Note and Scale Name settings.
- When following the song or clip scale, the effective scale and root note are indicated in the Base and Scale name choosers.
- Added info text for the Scale Name chooser and Transpose knob.

_Other Device Improvements_

- Drum Rack return chains can now be reordered.
- When selecting two or more chains within a Drum, Instrument, Audio Effect, or MIDI Effect Rack, the parameters of the selected chains can be altered at the same time.
- Improved delay time calculations in the Echo device, which ensures more consistent and reliable sound effects.
- Removed the MPE label from the title bars of the following devices: Electric, Simpler, Sampler, Wavetable as all Live instruments now support MPE.

**Device View**

- Audio and MIDI signal meters in the Device View are now taller, making them significantly easier to read.
- Added a background and rounded corners to device drop areas.
- When adding an audio effect to a device chain in which there are no instruments present, there is now an additional audio meter visible on the right side of the instrument drop area.
- Device chain input meters are now displayed on the separator between the Info View and Device View if the Info View is open. If the Info View is closed, the meters are displayed on the leftmost edge of the Device View.

**Interface**

- Added a Resync External Hardware option for sending resync messages to clock-synced hardware. When Sync is enabled for a device, you can set the resync behavior using the drop-down menu in the MIDI port’s output via the Link, Tempo & MIDI Preferences. In the same Preferences page, you can also enable the Show Resync Button option, and a Resync External Hardware indicator will be displayed in Live’s Control Bar.
- Added a Playback menu, which contains commands related to playback and recording.
- The Master Track was renamed to "Main Track", and the Master routing target was renamed to "Main".
- The View menu now has a Scene Tempo and Time Signature entry, which shows or hides scene tempo and time signature values in the Main Track.
- Live's demo Set can now be loaded using the new Load Demo Set entry in the Help menu.
- Using the "Insert Empty MIDI Clips" command in the Create menu or in the context menu for multiple selected empty clip slots (Session View) or multiple selected empty MIDI track lanes (Arrangement View) now creates multiple empty MIDI clips.
- You can now freeze and flatten tracks in a single step using the new "Freeze and Flatten Track" command. This command can be found in the Edit menu, or the right-click context menu of a Track Title Bar.
- The "Track Delay" option in the View menu was renamed to "Track Options". When opened, Track Options still features the Track Delay control, as well as a new Keep Latency button. When Keep Latency is on with monitoring active, the recording reflects the monitoring latency. When Keep Latency is off, Live no longer uses the monitoring latency in the recording. When monitoring is off, the Keep Latency control is disabled. If recording two tracks with monitoring enabled at the same time, one with Keep Latency on, and one with Keep Latency off, the former will show the recorded audio later on the timeline.
- Return tracks can now be copied, pasted, duplicated, and reordered.
- Switching between the Session View and Arrangement View when dragging a clip to the respective view selector button now happens immediately in the second window.
- When selecting a clip or time selection in the Session or Arrangement View, the content in the track will remain selected when switching between the Session and Arrangement. This means that the track highlighting will stay with the expected track when moving between views.
- Holding down the mouse-wheel now pans views in Live, such as the Arrangement View, Session View, or any scrollable area.
- Resetting a value to its default by either double-clicking on a slider or pressing the Delete key is now possible in more places in Live.
- If an audio device selected in the Preferences doesn't open correctly, the audio device chooser will now preserve the selection instead of reverting to the last used device.
- Live’s Splash, About and Welcome screens now feature a new look.
- The list of tabs in Live's Preferences is now named the Preference Page Chooser.
- The Look/Feel Preferences have been split into two new tabs: Display & Input and Theme & Colors. The Theme & Colors Preferences contain a new section called Theme, which can be used to set Live’s theme, as well as adjust the theme’s color tone and contrast. There is also an option to “Follow System” which will set Live’s theme based on the system’s currently selected light/dark mode preference.
- Live's title bar now uses the Colors system setting for light/dark mode on Windows 10 and 11.
- Inactive controls in Live’s Control Bar now use the same foreground color.
- On macOS, when viewing an existing Live Set, the main window now shows an icon that represents the document. You can right-click on the icon to reveal the directory path for the Live Set.
- The project name has been removed from the title bar.
- Live's default Set now has the Cue Out volume set to -6 dB.
- Replaced the link in the Help menu that points to Ableton's homepage with one that points to Ableton's Help page.
- Added a link to ableton.com to the Help View’s front page.
- Help View's Table of Contents has been updated for Live 12.
- Updated the What’s New lesson to include new Live 12 features.
- Updated software texts in various areas of Live in English and the following localized languages: French, German, Italian, Japanese, Simplified Chinese, and Spanish.

**Max for Live**

- Updated the bundled Max build to version 8.6.0.
- Max is now started during the splash screen loading process when opening Live.
- Introduced live.modulate~ object, which allows users to modulate Live parameters from within Max for Live.
- Introduced live.map object, designed to make it simpler to retrieve the name, Live API ID and Live Object Modal path of parameters. The object is intended to simplify patches that obtain information about parameters through clicking interactions.
- Using Live to open the Max editor no longer opens the in-app Max Tour.
- Max no longer checks for updates when using Live to open the Max editor.
- Introduced support for the @normalized attribute in live.remote~ object.
- The Live Object Model paths of the following items can now be obtained via their context menus: clip slots Session clips Arrangement clips tracks scenes devices device parameters Rack chains Drum Rack pads
- The Live Object Model paths of the following items can now be copied via their context menus: track scene session clip slot session clip arrangement clip device device parameter device rack chain/drum chain drumpad mixer device/volume mixer device/panning mixer device/left split stereo mixer device/right split stereo mixer device/track activator mixer device/sends chain mixer device/chain_activator chain mixer device/panning

**Mixer Improvements**

- The overall design of the mixer has been updated to improve visibility: Mixer faders now have larger handles, which have also been moved to the left of the meters. The dB values remain on the right of the meters. The meters now provide better contrast and have rounded corners. The maximum possible height for the mixer panel has been increased.
- The meter gradient was overhauled and now shows a gradient starting at -16 dB towards 0 dB to have better visual guidance in this critical area of mixing.
- The meter ballistics for peak and RMS metering have been improved.
- Mouse handling has been improved in order to avoid sudden volume jumps.
- A Mixer View toggle that opens/closes the mixer in the Session or Arrangement View has been added to the bottom right corner of Live's window. Next to the toggle, there is a drop-down menu that can be used to select which areas of the mixer to display, e.g., In/Out, Sends, and so on. The enabled areas are stored with the individual view, rather than being linked across the Session and Arrangement.
- Added a 6-pixel-high stripe that mirrors the track color to the bottom of the mixing area in order to help with navigation and track identification.

**Push Improvements**

_Push 1, 2 and 3_

- Push 1, 2 and 3 now support the newly introduced tuning systems. When a tuning system is loaded in Live, Push’s pads and interface will update to reflect the change: When using no tuning system or a tuning system with twelve notes with identical intervals between adjacent notes (equal temperament), the full Scales menu is available. When using a tuning system with twelve notes with differing intervals between adjacent notes (non-equal temperament), the root note selector is not available in the Scales menu. When using a tuning system that is not built with twelve notes, the Scales menu is displayed in the same way as before for all tuning systems: with one list for configuring the interval between rows in semitones. The Layout control has more options to help suit the different needs of different systems. Adjust this control to change the number of semitones each row is offset from the one below it. For example, if Layout is set to 5st the first pad will be pitch 1, then the pad above it will be pitch 6, and the pad above that will be pitch 11, and so on. In Melodic mode, Push's pads will display the root note of the system in the track color, and all other notes of the system in white. The sequencers update to indicate the correct pitches in the normal levels of white. Note names in Push’s Clip View will be updated to reflect whatever notes are used in a loaded tuning system. When Push 3 is set to MPE Expression Mode and Note Pitch Bend is set to Automatic, pitch bend will be disabled if a tuning system is enabled in Live.
- New parameter banks for the Live 12 devices Meld, Roar, and CC Control have been added.
- The Scale, Chord, Random and Arpeggiator device parameter banks have been updated.
- The Scale parameter in the Random device has been renamed to Interval to match the updated device UI.
- Changing probability values of grouped notes from Push will affect all notes in that group and the grouped value in Live.

_Push 2 and 3_

- Push 2 will now use the same technology as Push 3, instead of using a remote script. This introduces some UI changes to Push 2: Press Clip to cycle between Clip mode and the new Session Mode The visualizations for Tuner and External Instrument devices have been added. The browsing experience has been updated to the same simplified browsing experience as Push 3.
- It is possible to force the use of the remote script by adding the option -Push2UseLegacyScript to Live's Options.txt file.
- The Load Previous and Load Next actions are now assigned to the lower display buttons instead of the upper display buttons.
- The Preview button and text now change color depending on whether Preview is active or not.

**Session View**

- Changed the behavior of moving clips from the Session View to the Arrangement View: Looped clips taken from the same scene will be extended so that they span the same duration as the longest clip in the selection. Clips taken from different scenes are ordered sequentially and clips taken from the same scene are aligned vertically so that they also play in the same order in the Arrangement as in the Session.
- When selecting a track header in the Session View, the slot selection is no longer collapsed when the track has a selected slot. This keeps the highlighted track and the device chain in sync with the current clip shown in the Clip View.
- Added a [CTRL][Enter] (Win) / [CMD][Enter] (Mac) keyboard shortcut for triggering the Clip Stop button for all tracks with selected slots. The button will be highlighted when the shortcut is used.

**Setup**

- A Keep Monitoring Latency in Recorded Audio option has been added to the [right-click](Win) / [CTRL-click](Mac) context menu of the Monitor radio buttons for each track. This option is enabled by default, but when unchecked, recordings will have the same latency as if recorded with monitoring set to Off, regardless of which monitoring mode is selected.
- Live can now import and export audio files greater than 4 GB (such as .bwf and .rf64 files) by using the ITU Broadcast Wave file format. Please note, however, that Live does not support Sony Digital Pictures Wave64 files, which have the extension .w64.
- When clicking a link to ableton.com from Live, the website now loads in the language set in Live’s Preferences. Previously, the website’s language was based on the web browser’s settings.
- On Windows, video playback no longer requires third-party decoders for common video codecs. Live now supports the same video files as Windows Media Player.

**Tempo Follower**

- When deleting a track containing a clip whose tempo is being followed, the tempo automation is also deleted.

### Bugfixes

**Live Bugfixes**

- Fixed a bug which caused clips to incorrectly be copied rather than moved when dragging multiple clips.
- Fixed a bug that occurred when drag-copying notes while editing multiple clips at the same time, which could result in corrupt documents showing "Note IDs are not unique" error message.
- Fixed an issue where renaming files in the Clips, Samples, or Grooves categories would cause Live’s browser to open the User Library.
- Fixed a bug that caused mapped keys to be incorrectly triggered when used in key combinations, for example with the [ALT] key.
- On macOS, fixed a bug that caused video export to fail if the time range selected for export contained no video. Now, the export succeeds and produces an all-black video.
- Double-clicking the piano roll while the MIDI Note Editor is in Fold mode and there are more active key tracks than can fit in the view, will now zoom the Editor to fit the key tracks that contain notes rather than all of the active key tracks.
- Modulated sliders (e.g. mixer sliders) now use the modulation color for the dot indicator.
- The volume LEDs for meters in MIDI tracks are now correctly bottom aligned, eliminating potential issues with partially displayed LEDs.
- Fixed an issue where selecting a track containing a Drum Rack would cause the Session View to scroll to the last selected chain.
- Fixed an issue where the Arpeggiator device didn't use the full range of the Steps parameter when the pattern is set to Random.
- Fixed a crash that could occur when entering Macro Map Mode under certain circumstances.
- When running a new version of Live for the first time, Live would sometimes copy preferences and retrieve information from a user-made copy of an old preferences directory. This could lead to symptoms such as settings being lost or Live needing to be reauthorized depending on the contents of the user-made copy. This behavior is now fixed.
- In the Clip View, fixed an issue where vertical text in a collapsed clip title bar would sometimes be displayed with a colored frame that could render the text barely legible.
- When zooming into a frozen audio clip, the indicators showing which elements are frozen now move as expected.
- Fixed a bug which prevented Live from being closed when the Preferences folder was missing.
- On macOS, context and drop-down menus will no longer lag on certain devices using the Apple M2 chip.
- Horizontal sliders (e.g., Follow Action Chance or sliders in the Seed generator) now work in pen tablet mode. The value range is now preserved when dragging with a mouse.
- Fixed a bug that prevented notes from being freely resized when the grid was off.
- The “Auto-Scale Plugin Window” context menu item is now available in the Plug-ins label again.
- It is now possible to collapse a device's expanded view by double-clicking on the gap between the device's expanded view and the view above it.
- In Drum Rack’s I/O section, the columns header in the MIDI In Note chooser now uses the expected color.
- The Chain Selector modulation envelope for Racks no longer shows modulation units in “st”.

**Max for Live Device Bugfixes**

- Fixed a crash that could occur when changing the type of an automated Max for Live parameter belonging to a device on the Main track.
- Fixed an issue where the UI was laggy while scrolling in the Session View when using many presets that included MPE Control.
- Max for Live devices now correctly release focus when navigating away from them using a mouse.
- Parameters in Max for Live devices now initialize properly even when Live's audio engine is turned off.
