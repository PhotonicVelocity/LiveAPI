# Ableton Live 11 Release Notes

## 11.3.43 (October 14, 2025)

### New features and improvements

- Added Control Surface support for Akai MPK mini IV.
- The Move Control Surface now offers a wider array of LED brightness options when using recent firmware.
- Improved device navigation in newer control surfaces (such as APC64 and Move) in order to better account for device selections made in Live.

## 11.3.42 (April 14, 2025)

**Move Control Surface Updates**

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

**Third-Party Control Surfaces Updates**

- The play button of the Launchkey_MK3 and Launchkey_Mini_MK3 Control Surfaces no longer resets song time.
- In newer Control Surfaces (such as APC64), mute-related LEDs will now indicate when tracks and drum pads have been muted via solo. Additionally, the auto-arming behavior of newer Control Surfaces is now more consistent with Push.
- Detail View is now always shown when steps are held down via the Launchkey MK4, and Launchkey Mini MK4 Control Surfaces.
- The arm icon in the display of the KeyLab_mk3 Control Surface now uses different shades to better distinguish a track’s arm state.
- With the Launchkey_MK3 and Launchkey_MK4 Control Surfaces, it is now possible to navigate between groups of eight tracks with the Track Left and Right buttons while Shift is held down. The first track in the group will also be selected.
- Fixed a crash that could occur when triggering "Slice to Drum Rack" while using the APC64 Control Surface.
- Fixed a crash that could occur when triggering "Slice to Drum Rack" while using the Launchkey MK4 Control Surface.
- Fixed a bug in the KeyLab Essential mk3 Control Surface where only one bank of parameters would be available for plug-ins regardless of how many parameters were configured.

## 11.3.41 (February 10, 2025)

### Bugfixes

- Fixed a crash that occurred after removing an audio device.

## 11.3.40 (January 24, 2025)

### New features and improvements

- The plug-in Noisy2 from Expressive-E now starts in MPE mode by default.
- Added Control Surface support for Arturia KeyLab MK3, Novation Launchkey MK4, and Launchkey Mini MK4.
- On Windows, Live will show a dialog window if a Move unit is connected and a compatible audio driver is not present.

### Bugfixes

- When connecting/disconnecting MIDI devices or changing MIDI port settings, LEDs and displays related to newer Control Surfaces (such as MiniLab 3 or APC64) will no longer flicker.
- Fixed the following issues with note repeat: Sending polyphonic aftertouch of 0 for a playing note no longer "freezes" the pressure value for that note at 0; raising the pressure again will raise the corresponding velocity of note repeats. The All Notes Off event is no longer ignored for notes with a current polyphonic aftertouch or channel pressure of 0. Notes with a polyphonic aftertouch or channel pressure of 0 will now continue to repeat (with a velocity value of 1) rather than being stuck on.
- Compressors's gain reduction meter now once again shows negative Gain Reduction values as a blue bar in the Expand mode.
- Fixed an issue with flickering windows and menus sometimes observed on Apple Silicon computers when using Live in full screen mode on an external display.
- The state of the Chain Auto Select setting is now stored in the Audio Effect Rack, Instrument Rack, and MIDI Effect Rack presets.
- Fixed an issue where unwarped cross-clips that were cross-fading in would not play back or render at the correct time if the cross-fading happened during song tempo automation.
- Fixed an issue in the APC64 Control Surface where note mode would use an incorrect layout after power-cycling the hardware in certain cases.
- Fixed a bug in several control surfaces (such as Push 1 and ATOMSQ) that prevented multi-selecting devices in some cases.
- Fixed an issue where cross-fades looked broken when resizing fade lengths by dragging fade handles.
- Fixed a bug where the previously assigned MIDI Mapping Mode type was not displayed in the Status Bar after saving and reopening a Set.
- Fixed a bug in the Move control surface that caused the pad LEDs in the Session Overview sub-mode to not work correctly in some cases.
- Fixed a bug in several newer control surfaces (such as APC64 and Move) that could cause the Device View to be displayed incorrectly in certain cases.
- Fixed an issue in the KeyLab Essential mk3 control surface that prevented parameter information pop-ups from being shown when touching the encoders in some cases.
- Fixed a bug in the Move control surface where steps could not be edited unless they were held down for some time.
- The sound is no longer sustained indefinitely when the Envelope 1 Release control in Drift is set above 55 seconds.
- Fixed a crash that could occur when replacing Max for Live devices with different versions of the .amxd that had compatible but not identical parameters.

## 11.3.35 (October 8, 2024)

**New features**

- Added support for the Move control surface.

## 11.3.30 (September 4, 2024)

### New features and improvements

- In the APC64 and ATOMSQ Control Surface scripts, device navigation has been improved so that navigation is only enabled when there are devices available to navigate to. This also allows LEDs related to device navigation to reflect whether navigation is possible.
- Updated the Report a Crash Help View lesson.
- Updated software text in various areas of Live.
- Made the following changes to the Windows installer for Live: The installer now supports HiDPI. Two nested installers are no longer shown and all user interaction is done in one installer interface. The Start menu entry is now installed per machine, i.e., for all user profiles. Previously, the entry would only appear in the Start menu of the installing user’s profile, even though Live was installed for all users. Added a Launch button on the success page of the installer, which allows to directly launch the installed version of Live. Fixed an issue where the icon of the Start menu shortcut was a placeholder until rebooting. Fixed a bug where when replacing an existing installation, the entry listing the previous installation would remain in Windows's "Add/Remove Programs".
- It is now possible to quantize a selected clip from the SL MkIII Control Surface by pressing Shift + Select button 6.
Bugfixes:

- Fixed an issue in the Launch Control and Launch Control XL Control Surface scripts where the track range displayed in the Status Bar was sometimes incorrect.
- Fixed a bug that caused the MIDI CC mappings of a VST3 plug-in to be incorrectly cleared in rare circumstances.
- Fixed an issue where Live would incorrectly warn about low disk space and stop recording when recording to volumes with more than ~250 TiB of free space (or other thresholds depending on recording bit depth, sample rate, and number of simultaneously recorded tracks).
- Fixed the polarity in Drift’s waveform scope so that it is now in phase with device output and icons.
- Fixed an issue where breakpoints that were directly under the insert marker would not be deleted when using the Delete menu command or pressing the Delete key.
- Fixed a crash that occurred when trying to recover a crashed Live Set that contained a Simpler device that had previously moved slices from unanalyzed audio files in Slice Mode.
- Fixed a crash that occurred when resizing the left edge of an unwarped clip in Arrangement while there was also tempo automation on the Master track.
- Fixed a bug that led to an invalid mixed selection of track and Arrangement lane content after a deleted track was restored using the Undo command. Content selection is now restored when undoing or redoing actions for track and lane interactions that are based on content selection.
- Fixed a potential crash that could occur when restoring a deleted track while the Main track header was selected. Content selection is now restored when undoing actions that have to do with swapping content, instead of track selection.
- Fixed restored header selection after undoing or redoing track movement with the keyboard.
- The text in the Audio to MIDI dialog is now easier to read when using dark themes.
- Fixed a bug that could crash Live when closing a Set containing a Max for Live device that was observing the mute property on a chain mixer.
- When controlling Delay from newer Control Surfaces (such as MiniLab 3 or APC64), parameter mappings no longer shift positions when the device's state changes.
- Fixed an issue where per-note expression envelopes were played back incorrectly when started in the middle of an already playing note.
- On macOS, fixed an issue that sometimes occurred when mirroring screens, where Live's UI would hang for a short amount of time on one of the mirrored screens when opening a context menu or drop-down menu.
- Fixed a crash that occurred when calling get_all_notes_extended on an audio clip.
- Fixed a bug where recording a new clip with the Session Record Button via key or MIDI mapping would create an unnecessary Undo step.
- Unified the names of Undo steps for adding or deleting locators, regardless of how the addition or deletion was triggered.
- Fixed an issue where groove was incorrectly applied to per-note events when playing back a MIDI clip that included per-note events.
- Groove is now applied to per-note events when it is added to a MIDI clip.
- Fixed an issue in the SL MkIII Control Surface where track names would not be displayed correctly in some cases.
- Fixed an issue in the SL MkIII Control Surface, where certain clip-related actions (such as clip duplication) could not be undone.
- Fixed an issue that occurred when freezing clips with delay effects, where the effect at the end was not included if there was a period of silence before the effect tail.
- Fixed a broken link in the Report a Crash Help View lesson in English, French, German, Italian, Japanese, Spanish, and Chinese.
- Fixed a crash that occurred when deleting a note shortly after clicking it in the Velocity Editor.
- On macOs, context and dropdown menus will no longer lag on certain devices using the Apple M2 chip.
- The level animation dot on Compressor's transfer curve will now correctly follow RMS input meter values when the device is in RMS mode.

## 11.3.26 (August 29, 2024)

### New features and improvements

- Added Control Surface support for Arturia KeyLab mk3, Novation Launchkey mk4 and Novation Launchkey Mini mk4.

## 11.3.25 (May 8, 2024)

**Live - New features and improvements**

- Reduced the number of audio dropouts when running Live on Windows machines with processors that have performance and efficient cores, e.g., Intel Alder Lake.
- Introduced the option to create new audio clips in a Live Set via the Max for Live API, given a valid audio file path. This was achieved by adding two new endpoints: a Track.create_audio_track function and a ClipSlot.create_audio_track function, which create clips respectively in the Arrangement and Session View.
- The Song object in Max for Live now has a name property and a file_path property. Both properties are get-only.
- When using the APC64 Control Surface, it is now possible to lock device control with the [Shift] + [Device] combination. Additionally, the Quantize button LED now always reflects the record quantization state.
- In the AKAI APC64 Control Surface script, the cursor buttons now navigate the session ring in the Project mode.
- In the Komplete Kontrol S Mk3 Control Surface script, turning the 4D encoder will now scroll the song time when not in the DAW page (e.g., when the MIDI page is selected).
- When connecting several MIDI controllers of the same type, Live will add numbers to the names of their ports so that the ports can be addressed separately.
- The bundled Max version has been updated to 8.5.8.
- The following Drift device properties are now available in the Max for Live API: mod_matrix_target_1_index mod_matrix_target_1_list mod_matrix_target_2_index mod_matrix_target_2_list mod_matrix_target_3_index mod_matrix_target_3_list

**Live - Bugfixes**

- Live now detects 32-bit integer PCM .wav files and displays a warning dialog stating that such files cannot be loaded.
- Live now accepts all MIDI CCs (0-127) sent by VST3 plug-ins.
- Drift's LFO will no longer reset after a period of inactivity when LFO Retrigger is off.
- Fixed a bug that occurred when opening a Set, where in some cases the software text to the right of devices in the Device View would say "Drop an Instrument or Sample Here" instead of "Drop Audio Effects Here", and would only update after adding or removing devices.
- Fixed an issue in the Novation Launchpad and Launchkey MK3 Control Surfaces where pressing the Play button could result in clips being inaudible.
- Fixed a performance issue in macOS ARM-based desktop machines, where increasing the buffer size would lead to degraded performance.
- Fixed a crash that occurred when loading a device Rack preset that included a plugin that either did not exist or was deactivated.
- Fixed an issue where Live would hang when loading a Set containing a large number of video clips on Apple Silicon machines.
- Fixed a crash that sometimes occurred when undoing a track deletion where the track contained a plug-in and automation or modulation envelopes.
- Fixed an issue where the meters would incorrectly show a different CPU load when playing a test tone with the CPU Usage Simulator option in Live’s Audio Preferences set to below 35%.
- When the “Show Downloadable Packs” option is switched off in Live’s Library Preferences, no details about available Packs will be shown in the browser.
- Fixed a bug that caused the currently selected clip slot not to be brought into focus when renaming the clip or clicking the Clip View header in some scenarios.
- Fixed a bug that caused Live to reset its Preferences and other software settings if the program was started during the auto-update process.
- Fixed a performance regression that occurred particularly with smaller buffer sizes.
- Fixed a crash that occurred at startup on Windows 11 for computers with more than 64 CPUs.
- Fixed a bug where starting to edit an automation value and pressing return without typing in a value would create unnecessary breakpoints.
- Fixed a crash that could occur when changing the type of an automated Max for Live parameter for a device loaded onto the Master track.
- Improved some MIDI note selection descriptions in the Status Bar: The velocity range of MIDI notes with negative velocity is now displayed correctly. Time ranges with a granularity lower than 1/16 are indicated with the “+” sign.
- Fixed a bug that caused Simpler to produce no sound after enabling the device’s filter.
- The Chain Selector modulation envelope for Racks no longer shows modulation units in “st”.
- Fixed a bug that caused muted MIDI notes to become unmuted when extracting chains from a Drum Rack into a new MIDI track.
- Text within the Groove Pool is now aligned properly.
- When importing a sample from a Factory Pack which was created prior to 2014, Live will not launch a modal dialog which cannot be cancelled.
- Fixed a bug that could cause erratic behavior in the DS Sampler device.
- Drum Rack chain Preview Buttons in Session View now use the correct color when chains are unfolded for the first time.
- Fixed a bug on macOS Sonoma that caused the tempo to be set to 20 bpm when clicking in the tempo field if Live was in full screen mode.
- The alignment of the MIDI Ports settings in the Link, Tempo & MIDI Preferences has been corrected.
- The display of the tick and label markers in the Arrangement View Time Ruler now depends only on the zoom factor. Previously, the current view size could change the appearance of these markers as well.
- In the MiniLab 3 Control Surface script, a more accurate tempo is now displayed when using the Tap Tempo feature.
- Fixed a bug that would cause live.device to output id 0 instead of the newly created MIDI clip's ID in response to a call to the previously-available ClipSlot.create_clip function.
- Fixed a potential crash that could occur when editing an automation breakpoint value via its context menu.
- On macOS, Live now uses the hardware-accelerated Metal renderer in more situations, leading to improved UI performance with large window sizes on large low-DPI displays.
- On macOS, fixed a crash that occurred when dragging long Arrangement clips while zoomed in a lot and when the Live window was very large.
- Fixed an issue where some newer Control Surfaces (such as the one for APC64) could interfere with Push’s auto-arming behavior.
- Fixed a crash that occurred when attempting to stretch an Arrangement clip by [Shift]-dragging its edge while in automation mode and while the insert marker or a time selection was on an automation lane above the clip.
- After copying later parts of unwarped clips from take lane to main lane, the take lane would not show the copied region highlighted. This behavior is now fixed.
- Fixed an issue where playback of MPE curves would sound audibly different from the original performance when recording those curves.
- Fixed a performance problem with Windows 10 on computers using Intel Alder Lake processors.
- In previously affected Sets, fixed missing automation segments, glitches, hangs and crashes associated with broken automation curve coefficients. The Sets will now work correctly when they are loaded.
- Simpler will no longer load empty audio files that Live created for slot recordings.
- Gain reduction meters no longer flicker when using large buffer sizes.
- Improved performance of Sets containing Max for Live devices.
- On Windows, fixed issues with detection of some VST3 plug-ins, including AURA plug-ins.
- On macOS, fixed a crash that could occur when the Live window was moved between displays.
- Resizing to the left an unwarped Arrangement audio clip with tempo automation will now shift its audio to the right of the previous start position.
- Fixed an issue where Live's zoom level, and additionally the display scale setting on Windows, would affect the speed of moving automation breakpoints and the Knee parameter of Compressor’s transfer curve.
- Fixed an issue that occurred on Windows 11 machines with P-cores and E-cores such as Intel Alder Lake processor, where more worker threads than necessary would get created.
- When setting Live's thread affinity via third party tools or the Windows Task Manager, Live would have tried to override it for audio calculation threads instead of adopting the settings. This behavior is now fixed.
- Fixed an issue that caused vertical scrolling to move too fast when adjusting values in the MIDI Note Editor’s MPE and Envelopes view modes.
- Fixed a bug that caused Live's meters to stay permanently red after a signal of "infinity" level loudness was received in the audio engine.
- Fixed an issue that caused high CPU usage or audio dropouts when the scene tempo was updated very frequently while using Link.
- Fixed a crash that could potentially occur when pressing the arrow up, arrow down, page up or page down keys in the Session View while the main track was highlighted.
- On macOS, fixed a bug which would cause the contents of the Live window to disappear when moving the window from one display to another.

## 11.3.22 (March 11, 2024)

**Push - Bugfixes**

- The following Control Surfaces will now work again when using Push 3 in Standalone Mode: - APC Mini - APC mini MK2 - Launchkey Mini mkIII - Launchpad MK2 - APC40 MK1 - APC40 mk2 - Launchpad Pro MK3 - Push 1

## 11.3.21 (January 25, 2024)

**Live - Bugfixes**

- Fixed an issue where the playback of some Core Library samples would start at the end, which could result in silence or misplaced audio in Sets.

## 11.3.20

Live - New features and improvements

- It is now possible to access and edit Note PB and PB Range values directly in the Simpler device. The Note PB and PB Range controls have also been added to Simpler’s parameter banks on Push 3 and 2.
- The Drift device’s non-automatable parameters are now available as properties in the Max for Live API.
- A progress bar now appears when transferring files from Push 3 to Live.
- Updated the bundled Max build to version 8.5.6. For the changelog, visit: https://cycling74.com/releases/max/8.5.6
- Added Control Surface support for the Native Instruments Komplete Kontrol S Mk3.
- Added Control Surface support for the AKAI APC64.
- When loading a Note Set containing features from a version of Note that Live does not recognize, the names of those features are now included in the warning dialog.
- Updated the Core Library: Fixed SP 1200 16ths Grooves. Changed Hybrid Reverb default routing mode to Parallel. Restored the Hip-Hop Sub Bass preset.
- Added Control Surface support for the KORG Keystage.
- Previously, when loading a Set that included devices unknown to the currently used version of Live, an error message was displayed and the Set would fail to open. Now, the Set is opened without the unknown devices.
Live - Bugfixes

- Using the Dry/Wet controls in the Redux device while in Eco mode now works as expected instead of producing a phased sound.
- Previously, Live might crash when loading a complex Live Set (e.g., a Set containing a large number of Drum Racks.)
- Added the following changes to User Remote Scripts: Clarified information regarding button behavior in the UserConfiguration.txt file. The behavior of SessionRecButton is now consistent with the behavior of MIDI mapping the Session Record button.
- Fixed some rare crashes that might occur under certain circumstances.
- While scrolling is in progress upon using a quick flicking gesture on a touch pad and the view under the mouse changes (e.g., by pressing [Tab] to switch between the Session and Arrangement View), the scroll gesture now stops. Previously, the scrolling behavior would continue in the next view.
- Limited the number of threads created for audio calculation on Windows to the number of threads that can be created with the highest thread priority. This may prevent audio dropouts on computers with many processor cores.
- The text "Connect Push with Live..." in Live's browser now changes color when selecting a dark theme.
- Improved the display of Packs normally available for download when Live cannot connect to the internet or the authorization link to the Ableton server is lost.
- Fixed a crash that could occur when configuring a parameter in an Audio Unit plug-in.
- Fixed an issue in the SL_MkIII Control Surface script where parameter names and values were not correctly displayed in some cases on macOS.
- Fixed a bug that caused CPU spikes when using MPE with Instrument Racks or Drum Racks containing many chains.
- Live no longer crashes when deleting a take lane while scrolling with the mouse wheel.
- Fixed a crash that could potentially occur when running the Convert Melody to New MIDI Track command.
- Fixed an issue where the DS Clang device would get triggered by any note of the same choke group.
- The MPE Control device no longer affects UI responsiveness when scrolling in the Session View.
- Capture MIDI will not cause Live to crash when using MIDI hardware that creates notes of zero duration.
- Previously, re-enabling automation was necessary for many AU plug-ins when reloading a Live Set. This issue is now fixed.
- Fixed an issue where adding or removing return tracks while mixer sends were not visible resulted in the mixer send view being incorrectly sized when made visible again.
- Link is now able to connect to peers it could not connect to before in some cases.
- Fixed the following issues that occurred when launching Live in full screen on macOS: A gray rectangle is no longer shown for a short time at the bottom of the screen. The padding on the top and bottom of the window is now correct.
- Fixed a crash that occurred when editing the numeric value of an automation breakpoint.
- Fixed an issue that caused audio dropouts when dragging a selection of many small clips in Arrangement View.
- Fixed a bug that made notes appear as if they were jumping around when the start marker or loop brace were adjusted by small amounts.
- Fixed an issue in several Control Surface scripts (such as APC mini mk2) where Racks containing macros with duplicate names could not be controlled as expected.
- Fixed a bug where some AU and AUv3 plug-ins show no parameters after a changed configuration was saved as default.
- Fixed a bug where exporting audio containing an external audio effect or instrument would not create a resulting audio file when restarted manually or due to dropouts.
- Fixed a crash that occurred when restarting exporting audio within 100ms after starting Live.
- Live no longer crashes when switching away from track (for example via MIDI mapping that changes tracks) while clicking in the Device tab.
- Live will no longer repeatedly attempt to re-download an invalid Note Set from the Cloud.
- Fixed a crash on Windows that occurred as a result of Direct3D 11 device driver resets and upgrades.
- Fixed a “Serious Program Error" crash that occurred when loading a corrupted Max for Live device.
- On macOS, fixed an issue that caused CPU dropouts when freezing tracks or rendering Sets which contained External Instrument.
- Capture MIDI now correctly compensates for latency across loop jump boundaries.
- Fixed a crash that occurred when opening a new Set or closing Live while certain plug-in UIs were visible.
- Fixed a crash that occurred when pressing the [CTRL][Q] keyboard shortcut to quit Live while a VST plug-in editor window was in focus.
- Fixed an issue where the KeyLab Essential mk3 control surface wouldn't be automatically set up on macOS.
- Live's window size is no longer limited to 4096x4096 pixels on Mac.
Push 3 - New features and improvements

- Push’s pads and some of the buttons can now be used when browsing the Push 3 Tips lesson on the hardware.
- When Note Pitch Bend is set to Automatic in Push’s Expression settings, the glissando type will be pitch bend when using the External Instrument device with the Channel set to MPE.
- Two new buttons, ÷2 and ×2, have been added to Clip View for halving and doubling an audio clip’s tempo.
- External Sync can now be enabled in the MIDI tab of the Setup menu, this makes it possible to set up external MIDI clock sync directly from Push.
- The half-tempo button for audio clips and the Simpler device is now labelled as ÷2.
- A Crop command has been added to Clip View for audio clips.
- The layout for the Resonators device has been improved on Push 2 and 3.
- In the Audio tab of the Setup menu, there are now two entries for Clock Source: Internal and ADAT In. When set to ADAT In, Push will be synced to the external clock, and Live’s audio engine will follow the external clock rate.
- When hot-swapping audio clips, the browser will open to the location of the selected clip. When hot-swapping empty clips, the browser will open to its main list of categories.
- The current firmware version is now displayed in the Software settings even when Push is in Control Mode.
- Updated the design of the Quantize options: The % character next to the Swing Amount and Quantize Amount controls are larger. The Quantize To lists are now arranged vertically.
- The Play button is now deactivated when external sync is enabled.
- In the External Instrument device, meters are now visible for the Channel list of inputs.
- The Status and MIDI tabs in the Setup menu now have indicators which tell the user when MIDI data and MIDI clock data is being sent or received, as well as the tempo that Push is synced to if external sync is in use.
- The selected MIDI port's sync delay is now shown in the Setup menu's MIDI tab where it can be changed with an encoder.
- Push's Play button will now show the state of Live's transport even when it is synced to an external MIDI clock, but pressing the button when it is externally synced will have no effect.
- The turn off dialog will now be displayed after a short power button press.
- The selected MIDI port's sync delay is now shown in the Setup menu's MIDI tab where it can be changed with an encoder.
- Users can now upload usage data from when Push was used in Standalone Mode to Live.
Push 3 - Bugfixes

- When loading a Set with a wavetable selected in the Wavetable device, the device's visualization is now reliably shown after loading; this fixes an issue where Push would show "No Device" under certain circumstances.
- When entering Hot-Swap Mode while the second Macro page of a Rack device is visible, the Rack device can now be hot-swapped.
- Selecting the second Macro page of a Rack device while holding the Delete button will now delete the Rack device.
- Push no longer crashes when selecting the first slice of a manually sliced Simpler device by pressing the pad representing that slice while holding the Select button.
- When switching between two clips in Clip Mode, the clip's name and parameters are now correctly updated and displayed.
- Connecting Push 3 to a computer now works correctly when the currently selected track contains a Wavetable device.
- The timing of MIDI coming out of Push 3 is now more accurate, especially at higher audio buffer sizes.
- When sliding between pads to change pitch on Push 3 with the Repeat button active, the repeated notes now follow the pitch bend and timbre correctly.
- Fixed a typo in the message that appears on Push's display after successfully authorizing Live.
- The Transpose parameter is now correctly available in Sampler's main bank on Push 3.
- The waveform in Push's Clip View for audio clips is now correctly updated when dragging warp markers around or when using the ÷2 or ×2 buttons.
- Max for Live devices that observe the values of controls without getting them will now work with Push 3.
- Push 3 will now retain the last chosen buffer size after being rebooted.
- When nudging a Simpler slice's start position past the end marker of the sample, Push will no longer crash in Standalone Mode.
- After changing the metronome sound setting on Push 3, and then restarting the unit, the sound setting is now preserved.
- Previously, files with names containing percent characters would not show correctly on Push.
- A MIDI track's instrument can now be played when its input routing is set to "FromPush".
- After Push starts up in Standalone Mode, there is now less of a delay before certain features start to work. Also, the first device or Set loaded after starting Push will take longer than before if it uses Max for Live.
- The playhead in Push 3's Clip View of audio clips is now correctly displayed when using the ÷2 or ×2 buttons.
- It is now possible to open the same Set twice in a row via Live's Push browser label.
- An icon now appears to indicate whens a selection cannot be dropped when attempting to drag and drop it on or within the Push label in Live.
- The demo song will now be loaded on startup if the onboarding tutorial wasn't finished during Push's previous run.
- When starting Push 3 in Standalone Mode, the bottom row of buttons are no longer lit.
- It is now possible to use Max for Live patches and presets that utilize Node.js on Push 3 in Standalone Mode.
- Toggle controls are once again shown in a white instead of gray when active.
- The Cue volume can now be reset to its default value by tapping the Volume encoder when holding the Delete button, while the encoder is controlling the Cue volume.
- Samples and .amxd files collected and saved into Projects no longer show up as duplicates in their respective browser categories.
- Previously, when holding a step and a note in the Melodic Sequencer + 32 Notes layout, releasing the note after releasing the step would "deactivate" the step sequencer.
- When saving a Set after renaming it, the Set is correctly saved under the new name.
- Fixed an issue with PMC power button handling to ensure that units in Control Mode can be switched on and off correctly.
- While the scale menu is open after pressing the Scale button, Push no longer shows notifications such as "Play C2 to C4".
- Trying to delete a device parameter's automation no longer results in an error that causes unexpected behavior.
- MIDI and pad feedback will be more reliable on Push in Standalone Mode, especially at lower audio buffer sizes. It is also less likely that the audio will freeze at random times, especially when sending MIDI clock from Push.
- Live no longer crashes when deleting multiple Group Tracks at the same time while Push 3 is connected.
- It is once again possible to enter Note Edit mode using the jog wheel or Edit button, and select notes.
- When connecting Push 3 while in Control Mode to a computer running Live, it will be properly set up and connected to Live - even if Live was previously running seven Control Surfaces.
- Sets with larger numbers of tracks don't lag as much when editing steps in a step sequencer.
- Live no longer crashes when using Push 3 and changing the length of a note via a step sequencer while at the same time modifying that note via one of the encoders (e.g. Nudge).
- Push 3 will no longer crash when going from having an output selected to having no output.
- Push will now be less likely to hang before starting when switching from Standalone Mode to Control Mode.
- Push units without processor should now start more reliably.
- Canceling the shutdown dialog now restores previous views as expected.
- Removed the FromPush and ToPush MIDI ports from the Control Surface configuration. When used, these could lead to some erratic behavior. Any Control Surfaces that the user has configured to use these ports will be disconnected.
- Push should now be more responsive when switching between Control Mode and Standalone Mode.
- Improved Hot-Swap Mode so that the Load Previous and Load Next buttons are now only visible if the previous or next item can be loaded, respectively.
- Pads are now less likely to intermittently stop and start working again when playing on Push.
- Fixed a crash that occurred when pressing the Edit upper display button in Clip View while an empty MIDI clip was selected.
- Push will continue to be automatically armed for recording as expected, even after connecting and then disconnecting a control surface with an auto-arming feature.
- Fixed a crash in Live that occurred when quickly turning the Start and End encoders in Simpler on Push.
- Pink track Arm buttons are now properly disabled in Live after unplugging Push 2 or Push 3 (in Tethered Mode).
- Updated Push’s firmware to version 1.4.0. This addresses the following issues: An issue with audio distortions that occur when booting into higher sample rates. A problem with unexpected high velocity outliers on outer pads. An issue with Y jitter at the lower third of the bottom row of pads.
- Fixed a crash that occurred when shutting down Live while a return or the Master track was selected.
- Fixed a crash in Live that occurred when changing the scale root from Push 2 or 3.

## 11.3.13

### New features and improvements

- Added Control Surface support for the KORG Keystage.

## 11.3.12

### New features and improvements

- Added Control Surface support for the AKAI APC64.

## 11.3.11

### New features and improvements

- Added Control Surface support for the Native Instruments Komplete Kontrol S Mk3.

## 11.3.10

Live - New features and improvements

- Users that have Cloud enabled but are not logged in will be greeted with a new landing view when selecting the Cloud label in the browser.
- Updated the Core Library to make adjustments to Note Pitch Bend settings for some MIDI clip presets.
- Users can now control Drift using Max for Live.
- Added default values to Drift's Stereo and Unison modes.
- Users will now be redirected to the online manual on ableton.com when clicking on links to the manual in Help View lessons.
- Added software texts for Pitch Bend Range and Note PB Range in the MIDI/MPE tab in Collision.
- Added software texts for the Global/MPE radio buttons in Analog.
- Updated various software texts for Drift and the Cloud label.
- Updated some software text translations in French, German, Italian, Japanese, and Spanish.
- Updated the Max for Live Devices Help View lesson.
- Fixed a typo in the A Tour of Live Help View lesson.
- Updated the bundled Max build to version 8.5.5. For the changelog, visit: https://cycling74.com/forums/max-8-5-5-released
Live - Bugfixes

- Auto-Warp fixes: Fixed a bug that caused Live to hang when browsing factory packs and loading multisampled instruments. Improved the loading speed for Sets that contain samples which include .asd files, as well as for Packs that contain sampled instruments. Fixed an issue that caused noise artifacts to be added to audio signals when using the Complex or Complex Pro warp modes on Apple silicon computers. When auto-warping samples that were created at a fixed tempo, Live will now often warp these files using a single warp marker with a constant tempo. Improved the tempo choice of the “Warp From Here (Straight)” context menu option. Recording samples will no longer result in UI lag.
- When the Auto-Warp Long Samples option in Live's Record/Warp/Launch Preferences is switched off, opening existing Live Sets will no longer cause UI freezes due to auto-warp analysis. However, there a few scenarios that could still result in a UI freeze or lag: If the preference “Auto-Warp Long Samples” is switched on in the Record/Warp/Launch Preferences, long samples will be analyzed when they are imported into Live. If “Auto-Warp Long Samples” preference is switched off and a sample is imported or recorded directly in Live, the sample will be analyzed when using the context menu options “Warp From Here” or “Warp From Here Straight." Similarly, if an unwarped sample is warped using a context menu option, it will be analyzed.
- Updated the End User License Agreement in Live’s installer.
- When selecting one or more notes in the MIDI Note Editor and entering a velocity value with the keyboard, the possible velocity range is now limited to 1-127 rather than 0-127.
- Fixed a bug which sometimes caused a MIDI note’s velocity value shown in the MIDI Note Editor to be different from the velocity value shown in the Status Bar.
- The screen no longer flashes pink when starting Live in full screen on macOS ARM-based machines.
- Fixed a bug that prevented Wavetable’s expanded view from filling the entire width of the Live window.
- Fixed a bug that caused grooves to replace existing grooves in the Groove Pool instead of being copied when dragging and dropping grooves from Live’s browser or clips while holding the copy modifier CTRL (Win) / ALT (Mac).
- In Drift, using a Sample & Hold LFO Waveform in combination with the Retrigger option now correctly changes the initial value of the shape with each triggered note.
- Fixed an issue in Drift’s filter that sometimes caused notes to sound as if attack was applied to them.
- When using Drift with a sustain pedal, releasing the pedal no longer stops notes that are still held on a MIDI keyboard or Push.
- Fixed a bug in the Analog device that caused negative values of the Pitch Env Initial parameter to behave as positive values.
- Note-off velocity is now correctly passed through in MPE Control.
- On macOS, Live no longer crashes when the Output Device in Audio Preferences is set to "Use System Device" and the Input Device is set to a device which is incompatible with the Output Device.
- On macOS, Live no longer crashes when disconnecting certain audio interfaces while the Input Config dialog is open.
- Fixed a potential crash that could occur when audio devices or their properties were changed in Live’s Audio Preferences.
- Max for Live devices that have only an external output routing no longer cause unwanted delay compensation.
- Fixed a crash that sometimes occurred when loading the Samplex3 VST3 plug-in. As a result of this fix, the Device View now displays the Show/Hide Plug-In Window wrench icon for VST3 plug-ins.
- Fixed an issue that caused plug-ins with 17 output busses to crash Live in some circumstances.
- Fixed a crash that occurred when changing a parameter or recording automation while adding or editing an automation value.
- On macOS, fixed a crash that sometimes occurred when opening drop-down menus containing very long entries.
- Fixed an issue that caused Live to hang at the end of a Pack installation.
- Fixed an issue on Apple silicon computers that caused CPU overload and dropouts when using multiple Simpler devices on a drum pad within a Drum Rack.
- Fixed a bug that caused Min/Max values for mapped Macro parameters in AUv2 plug-ins to be lost when loading a preset or a Live Set.
Push 3 - New features and improvements

- Updated the Push 3 firmware package to version 1.3.0 (includes XMOS 1.0.71 firmware).
- User Mode is now available when using Push in Control Mode. All of Push's built-in functionality can be deactivated via User Mode. This allows Push to be reprogrammed to control alternate functions in Live or other software. Press the User button to enter User Mode.
- Items in the Projects folder are now arranged according to the selected sorting criteria.
- Made the following changes to Browse Mode: Packs are now shown with the Packs folder. The Favorites button is now no longer shown when navigating away from a folder. Browse Mode can now be closed correctly if the User Mode was toggled when viewing the browser.
- Improved discoverability of available Pushes in Live’s browser.
- Improved the design of various icons in Browse Mode.
- It is now possible to set global launch quantization by holding the Metronome button and turning the fifth encoder from the left.
Push 3 - Bugfixes

- Fixed an issue that prevented the XMOS firmware from being updated correctly for some units.
- Fixed an issue that caused lost or jumping notes when pressing a column of pads with considerable force.
- Fixed a bug that caused ADAT clock synchronization to be intermittently lost when changing sample rates.
- When using Hot-Swap Mode to swap an empty pad after swapping a non-empty pad, the browser will now open the location of the non-empty pad. This behavior matches hot-swapping on Push 2.
- Fixed an issue that caused an error message stating Live had crashed to appear when first turning on a new Push unit. This fix also prevents the same message from appearing when turning on Push in Standalone Mode after shutting it down.
- Fixed a bug that caused Live to hang when attempting to recover the Live Intro demo Set after loading the Set crashed Live.
- Fixed an issue that made it seem as if Push was in recovery mode after a software update. Rebooting after a software update will now correctly trigger shutdown and startup animations.
- Max for Live devices which use grab_midi and receive_midi now work correctly when Push is in Control Mode.
- When changing octaves while a clip is playing in Note Mode, the pad feedback will now be updated immediately.
- The connect screen is now displayed on Push when Live is closed and Push is in Control Mode.
- Improved reliability of pads when using low pressure values.
- Double triggers on certain drum hits are now suppressed.
- Fixed an issue that caused the touch strip to get stuck.
- Fixed a bug that caused some firmware update failures.
- Fixed a bug that caused the velocity curve to jump after connecting Push to Live.
- Fixed an issue that caused double-finger hits of non-drum MPE pads to be lost.
- Fixed an issue where the external ADAT clock source was not working on macOS.
- Fixed a crash that occurred when loading a Set with the Master track selected and then pressing the Master Track button.
- When the amount of Gain on a sample in Simpler is turned down to the minimum, the value will now be correctly displayed as -inf.
- Fixed an issue that prevented users from changing the length of notes in clips when using pads in the step sequencers.
- Fixed a bug that prevented audio clips from being immediately available for conversion after being recorded.
- Fixed a bug that caused display visualizations to overlap when holding a step in a step sequencer for automation recording while the Setup menu was open.
- The input meter will now indicate clipping in cases where too much digital gain is applied.
- A value of -0.0 no longer appears when fine-tuning Wavetable's parameters.
- When attempting to load a Max for Live device that cannot be opened on Push, an error message will now be immediately displayed on the hardware.
- Added icons for Group Tracks and tracks containing Drum Racks or Instrument Racks.
- If a new Set is created as a part of a lesson on Push, the display no longer shows a notification about a new Set.
- Fixed an issue that caused the sensitivity curve to change abruptly when adjusting settings in the Sensitivity tab of the Setup menu.
- Fixed a bug that resulted in parameters representing notes to display an integer value instead of the note name.
- Increased the encoder sensitivity when adjusting the pitch bend range in Drift.
- When playing repeated notes using the Repeat button in the 16-Velocities layout, changing pressure on the pads will no longer change the velocity of the notes.
- Removed the option to choose a different volume option by holding the Select button and tapping the Volume encoder.
- Adjusting pressure applied to the pads when playing repeated notes while using the Poly or Mono Aftertouch Expression Modes will now correctly affect the velocity of the notes.
- Fixed a bug that prevented the Mute button from working when attempting to mute steps in a step sequencer.
- Fixed an issue that could result in the shutdown confirmation message being displayed at the same time as the save confirmation message.
- Improved responsiveness of the touch strip when changing octaves in Note Mode while playing back a Set with a high CPU load.
- Fixed an issue where Packs available for download or update were not visible after using the Hot-Swap Mode.
- Fixed a bug that caused the battery charge level to be displayed as “N/A” after charging to 99%.
- Improved handling of data removal, so that installing and then uninstalling a Pack when using Push in Standalone Mode will now result in the same amount of free disk space as before installation.
- Deleting the last item in a given folder will now result in the browser returning to the parent folder.
- When dragging and dropping a clip onto the Push label in Live’s browser, the cursor now changes to indicate that the action cannot be performed.
- Pressing the Preview upper display button in Push’s browser now affects the state of the Preview switch in Live’s browser and vice versa.
- Fixed a crash that occurred when stopping all playing clips with a return track selected.
- Fixed a bug that sometimes caused the upper display buttons and editing options for MIDI clips to appear in white instead of matching the clip’s color.
- It is now possible to adjust Drift’s Voice Count parameter on Push.
- The available options for the Type B parameter in the EQ Eight device are now represented by icons.

## 11.3.4

**Live - Bugfixes**

- Auto-Warp Improvements: Improved the loading speed for Sets that contain samples which include .asd files, as well as for Packs that contain sampled instruments. Fixed a bug that caused Live to hang when browsing factory packs and loading multisampled instruments.

**Push 3 - Bugfixes**

- Fixed an issue where Packs available for download or update were not visible after using the Hot-Swap Mode.
- Fixed an issue that caused a message that Live crashed to appear when a new Push unit was first turned on or, in some cases, when turning on Push in Standalone Mode after shutting it down.
- Fixed a bug that caused Live to hang when trying to recover an Intro edition demo Set after a crash.
- Push firmware package was updated to version 1.2.0 (including XMOS firmware 1.0.69): The connect screen is now displayed on Push when Live is closed when using Push in Control Mode. Improved reliability of pads when using low pressure. Double triggers on certain drum hits are now suppressed. Fixed an issue that caused the touch strip to get stuck. Fix a bug that caused some firmware update failures. Fixed a bug that caused the velocity curve to jump after connecting Push to Live. Fixed an issue that caused double finger hits of non-drum MPE pads to be lost. Fixed an issue where the external ADAT clock source was not working on macOS.

## 11.3.3

### New features and improvements

- Added Control Surface support for the KeyLab Essential mk3.

## 11.3.2

### New features and improvements

- Auto-Warp Improvements: Live now uses a new Auto-Warp algorithm. Both downbeat and tempo variations are more accurately analyzed, making it possible to work with longer samples and entire songs without the need for manual warping in most cases. To run the new Auto-Warp algorithm on clips within an existing Live Set, use any of the Warp From Here commands (found in the Sample Editor's context menu) from any location in a clip.
- Cloud in Live: Song updates made to a synced Note Set will download more quickly to Live, under certain circumstances. Song updates made to a synced Note Set that is currently open on Windows and has not been saved using the Collect All and Save option will no longer cause a download to fail and retry endlessly. Samples that are no longer used by a Set.abl file will not be displayed under that Set within the browser's Cloud label.
- Control Surfaces: It is now possible to redo actions using the Launchkey MK3 Control Surface script by holding down Shift button and pressing the Undo button.
- Core Library: Added new presets and Racks featuring MPE. Added improved MPE mappings in MPE-enabled instruments. An update to zplane libraries may cause subtle sound changes when using Complex and Complex Pro warp modes in audio clips or the Simpler device.
- Interface Improvements: Accessing Legal Information through the About Live dialog now opens Live’s factory content Legal folder that contains Ableton's End User License Agreement and licensing documents. Updated the End User License Agreement to: include new Ableton products better reflect the Ableton product ecosystem respond to requests for clarification on our policies include other small and compliance-related updates Updated software texts in various areas of Live. Updated various Help View lessons. Updated various Help View lessons and software text translations in German, Spanish, French, Italian, and Japanese languages. The "Read the Live Manual…" option in the Help menu will now direct users to the online version of the manual. Replaced the link in the Help menu that points to Ableton's homepage with one that points to Ableton's Help page. Help menu items that are related to learning Live are now grouped into one section, and "Get Support..." now appears as "Get Support", to indicate that it is not an external link. Renamed the Help menu's "Help View" item to "Built-In Lessons". Renamed the Home button's "Help View" info text in the main Built-In Lessons page to "Lessons Start Page". Added a link to the Help View's table of contents page that points to Ableton's Help page. Removed unnecessary dots from the File menu's "Manage Files..." entry. When Zoom Display is set to 100% on Windows, Live now uses less GPU resources with certain combinations of GPUs and drivers. Removed the option to "Use System Device" for audio input on macOS. If audio output is set to “Use System Device” and the system device changes, Live no longer pauses audio with a "System device changed" dialog on macOS.
- Max for Live Improvements: Updated the bundled Max build to version 8.5.4. For the changelog, visit: https://cycling74.com/releases/max/8.5.4 fixed parsing error with large gen Patchers fixed matrix color input fixed audioschedulertime calculation when device is open in the Editor Live Object Model: updated docs sfplay~: fixed crash with timestretching in efficient mode vst~: improved loading speed for VST shell single plugin vst~: partian-scan results are used in fas-scan mode vst~: unique ID argument is used with plug_{format} messages vst~: VST3 shell plugins cache info about other plugs in the shell metro in Max for Live: outputs bangs consistently when the Arrangement View's loop brace is active RNBO in Max for Live: starts up only after a rnbo~ object is present
- MIDI Clips and Note Editing: In MIDI clips, the setting of the Envelope Editor's MIDI Envelope Auto-Reset context menu entry is always respected, even when the respective track's Monitor switch is set to "In".
- New Devices and Device Improvements: AAS Device Improvements: Added MPE support to the Analog, Collision, Electric, and Tension devices. Updated info texts in the Analog, Collision, Electric, and Tension devices. Added visual improvements to the Collision and Tension devices. Drift : Introduced Drift, a new Instrument available in all editions of Live. Drift is a compact subtractive synthesizer that comes with a wide sonic palette and an approachable interface. Expression Control: Changed the way MIDI and MPE data are parsed for improved reliability. This also delivers a potential performance boost to the device. Expressive Content for Live: Added a number of presets to the AAS devices (i.e., Analog, Collision, Electric, and Tension), and the Drift, Sampler, and Wavetable devices, with an emphasis on expressive playability. The updated MPE Control Device can further adjust their playability and also enhance interaction with non-MPE devices such as Operator (via MPE to MIDI). External Instrument: The External Instrument device is now available in Live Intro. MIDI Monitor: Incoming MPE data can now be viewed in the MIDI Monitor device in the MPE display. Incoming note, velocity, slide, pressure and per-note pitch data are shown in a continuous stream as notes are played. MPE Control: Redesigned the UI to include dedicated tabs for MPE sources. This makes it possible to separately adjust each source’s settings, including configuring a default modulation value which will be used when playing notes that do not contain per-note MIDI data. It also introduces the ability to individually mute MPE sources. Introduced the Swap to Slide option when using the Press MPE source. This is useful for example when controlling an external synth which only supports polyphonic aftertouch, but the user intends to control the modulation via the vertical axis instead. Introduced a Centered option to the Slide MPE Source, so that the center of the vertical axis corresponds to a Slide value of 0, reaching 127 in both directions when moving away from the center. This feature is meant to help users who utilize a pad based MPE controller. Centered transforms Slide data so that hitting the center of the pad generates non modulated sound and the modulation value increases progressively as the finger slides away from the center alongside the vertical axis. Added the Ons option to the Slide MPE source. When activated, Slide values are only updated on Note On, without further changes until a new note plays. Optimized the device for better CPU performance. The default modulation value will always be used when playing a note which does not contain per-note MIDI data, also in cases where min, max and curve values are tweaked. Improved the text layout of live.tab objects. Note Echo: Added MPE support to the Note Echo device. Each MPE dimension has a feedback control, which defines how fast MPE modulation decays over time. MPE can be enabled with a toggle; when this toggle is disabled, the device behaves exactly how it did in 11.2. Minor changes have been made to parameter names in Sampler and Wavetable.
- Push: Added support for the Drift device to Push 2. Improved the UI of the following devices on Push 2: Analog, Collision, Tension, Beat Repeat, Filter Delay, Amp, Vinyl Distortion, Saturator, and Grain Delay. On Push 2, it is now possible to edit MPE parameters in the Analog device, and missing parameters have been added to the device's banks. It is now possible to edit MPE parameters in the Tension device on Push 2. Reduced the knob sensitivity of the Tension device's Octave and Semitone parameters on Push 2.
- Setup: To avoid incompatibilities, you will be asked to save Live Sets created with an older version of Live as a new file in Live 11.3.

**Live Bugfixes**

- Fixed a bug that caused incorrect formatting of some text in the Info View when Live’s language preference was set to German.
- The Sample Editor will now always display the audio clip the user interacted with last, even in cases where multiple audio clips are selected.
- Fixed a bug that resulted in an incorrect latency compensation when using positive track delays on Group Tracks or return tracks.
- Scale Name and Root Note values of clips which are not in key will now be correctly retrieved when re-opening a saved Live Set. Previously, they would reset to default values when the clip was changed to be in key with the Set.
- Fixed a crash that would sometimes occur when pressing [Tab] or [Shift][Tab] after clicking on a Session clip title in the Clip View in a second window.
- When using a second window, Live will no longer switch between Session and Arrangement Views when clicking on a clip title in the Clip View, even when interacting with a clip from the other view.
- Fixed a bug that prevented automation lanes of some AUv2 plug-in devices from showing up when reloading a Live Set.
- Fixed an issue in the APC Key 25 mk2, APC mini mk2, ATOM, and ATOMSQ control surfaces where button LEDs would indicate that upward scrolling was possible under the wrong circumstances.
- Fixed a bug that might cause Live to crash on Windows when quitting the application.
- Fixed a crash that could occur when configuring a plug-in device's parameter while the containing track was unselected.
- Fixed a crash that could occur when pressing the [Tab] key after switching to the Arrangement by hovering over the Arrangement View Selector while dragging a Session clip.
- Previously, dragging a Drum Rack return chain to the Session/Arrangement View drop area would create an uncolored return track.
- Fixed a bug that created an Ableton Folder Info subfolder in the wrong location, or under the wrong circumstances.
- Fixed a bug that caused the Analog device's amplifier envelope to ignore the release phase when its Free Run Mode switch was enabled.
- Previously, when pressing the Cancel button in the "This action will stop audio. Proceed?" dialog that appears during the Collect All and Save process, the current Set would be moved into the respective Backup folder.
- Fixed an issue in the Multiband Dynamics device that would cause its band meters to flicker when used with certain VST plug-ins.
- Fixed a bug that caused Live to switch to “Use System Device: No Device” after disconnecting wired headphones while the “Use System Device” setting was enabled.
- When using an incompatible device with the “Use System Device” setting active, Live no longer stays connected to the device and instead switches audio devices to "No Device" as indicated in the warning dialog.
- Fixed a crash that occurred after canceling a package installation.
- Fixed a regression which prevented the Note Echo device from working correctly with MPE.
- Fixed a crash that occurred when receiving a call while using AirPods as audio output device.
- Fixed a crash that would sometimes occur if loading sample chunks took a long time.
- The MIDI input ports of the APC Key 25 mk2 and APC Mini mk2 controllers are now visible in Live's Link/Tempo/MIDI preferences, which allows these controllers to be used for MIDI mapping.
- Fixed a performance issue in Sets with many particular VST3 plug-ins, that caused the UI to lag or become unresponsive.
- Fixed a typo in the French translation of the Quantize dialog window.
- Fixed a bug that allowed dropping a Rack chain containing only audio effects on an audio track header, which caused Live to crash.
- Per-track performance impact meters now use less graphics-rendering resources.

**Max for Live Bugfixes**

- Fixed a crash that occurred when running the duplicate_clip_slot function on return tracks or the Master track with Max for Live.
- Fixed a crash that occurred when running the duplicate_clip_to_arrangement function on an Arrangement clip using the same start time as the original.
- Fixed a bug which allowed users to run the duplicate_clip_to_arrangement function with negative start time.
- Fixed a bug in the MPE Control device that prevented Sustain Messages from working.
- Fixed a bug in the Expression Control device that prevented Global Aftertouch from working as expected, under certain conditions.
- Fixed a bug in the Shaper MIDI device that caused its envelope to be triggered once a Note Off message was sent.
- Fixed a bug in the Shaper device which caused some UI elements to be inconsistent with Live’s color palette when using Dark Theme.
- Fixed a bug that caused sound to cut off while triggering the DS Cymbal device and adjusting its Decay parameter.

## 11.2.11

### New features and improvements

- Song updates made to a synced Note Set will download more quickly to Live, under certain circumstances.
- Song updates made to a synced Note Set that is currently open on Windows and has not been saved using the Collect All and Save option will no longer cause a download to fail and retry endlessly.

### Bugfixes

- Fixed a bug that created an Ableton Folder Info subfolder in the wrong location, or under the wrong circumstances.

## 11.2.10

New features and improvements

- Capture MIDI A sequence of Capture MIDI attempts will not be biased by the tempo of previous captured clips. More material will be kept by Capture MIDI when the transport is playing. When Live's transport is stopped, Capture MIDI now requires a slightly longer gap to detect new phrases.
- Clip View Opening a Note Set in Live where the Set has the In Key setting switched on will now activate each clip's Scale Mode (except in tracks containing Drum Racks). Scale Mode is toggled with the Scale button in the Clip panel of the Clip View for MIDI clips.
- Cloud in Live In the Cloud tab of Live’s browser, the Date Modified column now appears as Cloud Modified. The Cloud Sign In button has been expanded to fit translated texts. A loading icon is now displayed next to the Cloud label when syncing Sets. After signing out of Cloud in Live, the Manage Cloud tab of the ableton.com User Account no longer shows an active session. When transferring Note Sets to Live, the Sets will now be visible in the Cloud label in Live’s browser. They will appear grayed out until the sync is complete.
- Control Surfaces The Record button on ATOM, ATOM SQ and MiniLab 3 Control Surfaces will now record the view in the second window when it is in focus. Previously, it would always record the view selected in the main Live screen. Improved the parameter mappings for Hybrid Reverb and Phaser-Flanger in the AKAI APC Key 25 mk2, APC Mini mk2 and Arturia MiniLab 3 Control Surfaces. Improved the parameter mappings for Drum Buss, Hybrid Reverb, Phaser-Flanger and Redux on Push and in the AKAI FORCE and Novation SL MkIII Control Surfaces.
- Device Improvements The Pitch MIDI effect UI has been slightly updated. In Audio and MIDI Effect Racks, chains are now automatically named based on whichever devices are added.
- Interface Updated various Help View lessons. Updated various software texts in English and Simplified Chinese. Updated the software texts for the Electric device. Updated the appearance of the "Record/Warp/Launch" tab in Live's Preferences. Added support for MIDI files with the .midi extension. When viewing search results in Live’s browser, plug-ins are now organized as expected when sorting by Type. The Follow button in the Control Bar is no longer hidden when selecting multiple clips in Arrangement View. When switching audio devices with the Use System Device option activated, Live no longer displays a dialog window about system devices if the device change doesn't impact the current device selection.
- Max for Live Updated the bundled Max build to version 8.3.3. For the changelog, visit: https://cycling74.com/forums/max-8-3-3-released A new accessor in the C++, Python, and Max for Live APIs allows users to directly access the chain selector of a RackDevice in Max for Live instead of indexing into a parameter list. Users can now access Live's full version string (instead of only the major, minor, and bugfix version numbers) using the Max for Live API. Two new properties in the Max for Live API allow users to observe the latency of a device in either samples or milliseconds. A new property in the Max for Live API allows users to observe the number of visible Macro Controls for a RackDevice. Improved the sorting of output when getinfo is called on a live.object by making a Rack Chain selector a child property of RackDevice rather than a simple value property. Updated the LOM documentation to correctly reflect the available values when getting a device’s type. LiveAPI: A Compressor's input_routing_channel and input_routing_type are now settable. The properties of the Shifter device are now accessible via Max for Live.
- Push Updated some parameter names for the Reverb device on Push 2.
- Setup The Export Audio/Video dialog is now slightly larger to accommodate translated texts. When exporting multiple tracks, the option to also export video at the same time is now deactivated in the Export Audio/Video dialog. Introduced a Use System Device Option in the audio input/output choosers in Live’s Audio Preferences on macOS. Selecting Use System Device will set the input/output device in Live to match what is set in the macOS Sound System Preferences. If the Use System Device setting is chosen for audio input or output on macOS and the System Audio Device changes, Live’s audio engine will turn off, and a dialog window will appear. The dialog window will prompt you to either accept the changes made by the system or configure Live’s audio settings on your own.
Bugfixes

- Live Bugfixes Fixed two bugs relating to Link: Fixed a bug where Live would sometimes play out of alignment with Link peers when starting playback somewhere after a time signature change. Fixed a bug where Live’s playhead would move around unpredictably when clicking in the Scrub Area to jump playback into a section with a different time signature while Link was enabled. Fixed a bug that disabled file synchronization between Live's browser and secondary drive volumes on macOS. Fixed a bug on macOS that would sometimes prevent Live's UI from updating (and sometimes scaling incorrectly) after connecting or disconnecting an external monitor. Fixed a bug that caused the minimum parameter values of AU plug-in presets to load instead of their assigned values. Fixed a bug that incorrectly cropped a warning text in Live's Audio Preferences when the text becomes too long. Fixed a bug that sometimes caused .als files saved in Collections to disappear from the list when using the “Save Live Set” or “Collect All and Save” commands in the File menu. Fixed a bug where Live would sometimes fail to auto-update when the application was renamed to fit the exact version number (e.g. “Ableton Live 11.2.5 Suite”), and then placed in a folder of the same name. Fixed a bug where the blue modulation dot would not appear next to modulated sliders immediately after adding a modulation envelope for it. Fixed a bug that would occur when dragging device chains that contain external files (e.g., the LFO device) into a folder that is not in the User Library. This previously created an entirely new Project folder, even if the Collect Files on Export setting in the Library Preferences was set to “Ask” or “Never,” and the dialog box that appeared when moving the file was not set to copy it. Fixed a bug where Sets with emojis in their title would stay in the Cloud tab of Live’s browser, even after removing them from Cloud in Note. Fixed a bug that caused Live to remain synced to an external MIDI clock even when the corresponding MIDI port’s Sync input was deactivated. Fixed a crash that occurred when renaming samples in selected Drum Rack pads that were outside of the Rack’s displayed Pad Overview. Fixed a crash on Windows that occurred when using the [right-click] context menu to rename an audio/MIDI clip or locator while it was already being renamed. Now, right-clicking a clip or locator while renaming it no longer opens a context menu. Fixed a crash on macOS that sometimes occurred when selecting an audio output device in Live’s Audio Preferences and disconnecting it shortly thereafter. Fixed a crash that occurred when dragging a Session clip away from its original track, holding it over another track long enough to select it, and proceeding to drop it into Live’s browser. Fixed an issue that caused disk overloads when using MIDI notes with randomized velocities to play Sampler presets in certain Packs (such as Session Drums Club). Fixed an issue in the MackieControl and MackieControl Classic Control Surface scripts where exclusive arming wouldn't work in some cases. Fixed an issue in the MackieControl and MackieControl Classic Control Surface scripts where changing a track's input type could leave Rec/Rdy LEDs in incorrect states. Fixed an issue where under certain circumstances, Draw Mode in the Velocity and Chance Editor lanes did not work correctly when editing multiple clips. Fixed an issue where under certain circumstances, drawing ramps in the Velocity and Chance Editor lanes when editing multiple clips did not correctly highlight affected notes. Fixed an issue that caused a value range to be displayed when using the [ALT][Shift] keys to draw linear ramps in the Velocity and Chance Editor lanes instead of a fixed value. Fixed an issue where drop-down menus in Live’s Preferences would disappear when the initial mouse click was released if the menu was clicked on the leftmost side. Fixed an issue where clicking the empty area beneath scenes in the Master track would not select the Master track. Fixed an issue with Sampler devices in Drum Rack pads that created disk overloads under rare circumstances. Fixed two bugs relating to emojis in Live: Fixed a bug where Set names with emojis would stay in the Cloud tab of Live’s browser, even after removing them from Cloud in Note. Fixed a regression on macOS where folders saved in the Places section of Live’s browser wouldn’t show any contents if a folder name contained certain emojis. Fixed a regression on Windows where keyboard shortcuts with the copy modifier [ALT] would not work after using the [F11] shortcut to enter and exit Full Screen Mode until you pressed another key first. Previously, loading an instance of the Shifter device with the Delay parameter enabled would cause timing and pitch issues during playback. Previously, crashes on macOS caused by a specific VST2 plug-in would open a Help View lesson that displayed the name of the faulty plug-in along with a few common troubleshooting tips. Due to changes in macOS crash reporting, this feature has been removed. Previously, video export failed when a warped video clip contained a Start or End marker before the start or after the end of the video. When dragging or [Shift]-dragging a Warp Marker within a video clip, Live's Video Window now displays the video at the position of the Warp Marker. Double-clicking the right edge of Live’s browser now folds the window as expected. Loading older Live Sets, presets, and samples created on macOS will no longer cause Live or the Indexer to crash on Windows if the content contains a forward slash (e.g. “Clip 1/8.adg”). Opening a pop-up menu with [Enter] then closing it with [ESC] now works as expected. When using Capture MIDI with Reduce Latency When Monitoring enabled, the resulting MIDI clip now has the exact timing as what was played. Certain UI elements of the Spectral Resonator, Spectral Time, and Limiter devices are now consistent with Live’s color palette when using the Dark Theme. The Optimize Arrangement Width command (accessible via the [W] shortcut) now ignores invisible take lanes. Metal rendering is now turned off for macOS 10.13 High Sierra to fix issues that arise when using Full Screen Mode. Metal rendering can be restored using the "-_MacOSForceMetalLayerOnHighSierra" debug option in the Options.txt file. Packs will now be selected in Live’s browser when they are finished installing. Loop start/end markers for audio clips are now properly aligned with the borders of the Push 2 display. Nudging clips on linked tracks now works as expected. Under certain circumstances, launching different Rack Macro Control variations would create ramps in recorded automation envelopes due to missing endpoints. These envelopes now appear as discrete automation line segments. Using [Shift]-click to select clips in Arrangement View now shows the correct selection lengths in Live's Status Bar. When using [Shift]-click to extend the time selection of linked tracks with take lanes, the selection is no longer extended to all lanes. Main menus on Windows can be accessed in Full Screen Mode by using [ALT] + character shortcuts. When using scene Follow Actions to switch between scenes with different tempos, Live now correctly changes tempo with a scene change even when the Arrangement loop is activated. Previously, if the Arrangement loop was on, the tempo would prematurely change when reaching the end of the Arrangement loop brace. Fixed a bug which prevented the Optimize Arrangement Width button from working correctly when loading Note Sets in Live. When loading a corrupt Live Set containing non-unique Pointee IDs, Live now automatically offers to repair the set. Fixed an issue where Live sometimes would not update the UI when switching between viewing note-on and note-off velocities in the MIDI Velocity Editor. Fixed a bug which prevented adaptive grid modes from working correctly. The grid lines now reappear as expected when zooming out after having previously fully zoomed in. Fixed a regression which prevented the Expression Control device from recalling mappings to certain parameters when loading a Live Set or preset. Fixed a bug which caused the Reverb device to stop outputting sound when using long predelay times. Fixed a crash that occurred when connecting to audio system devices when no output device was available. Fixed a regression that prevented the MackieControl and MackieControl_Classic Control Surfaces from working correctly in Live Sets that contained Group Tracks.
- Max for Live Bugfixes LiveAPI: A Compressor's input_routing_type now correctly returns input_routing_type instead of the input_routing_channel.

## 11.2.7

### New features and improvements

- Added Control Surface support for the AKAI APC Key 25 mk2 and APC Mini mk2.

## 11.2.6

### New features and improvements

- Updated various software texts.
- Individual track names are now visible when expanding Note Sets in the Cloud tab of Live’s browser.

### Bugfixes

- Fixed a crash that occurred when enabling warping in Simpler devices in tracks from Sets originally imported from Note.
- Fixed a crash that would sometimes occur when deactivating Ableton Cloud in the middle of Cloud authorization or when downloading a Note Set.
- Fixed an issue where hot-swapping certain devices in Sets imported from Ableton Note wouldn’t produce any results in Live’s browser.
- Fixed a regression that caused certain AU and VST2 plug-ins to load with incorrect parameter values (and sometimes fail to pass audio) when loading a Live Set.

## 11.2.5

### New Features and improvements

- Ableton Cloud Introduced Ableton Cloud, a service that sends Sets from Ableton Note directly to Live’s browser, as well as other instances of Note across various iOS devices. To enable cloud functionality in Live, open Live’s Preferences, go to the Library tab, and switch the Show Cloud option to On. Once enabled, a Cloud label will appear in the Places section of Live’s browser, along with a message prompting you to sign in to ableton.com. Click the Sign In button to open a web browser window, this will lead you through the activation process required to connect the service to your Ableton User Account. After activating Cloud, any Sets that are uploaded to Cloud in Note will appear in Live’s browser in real-time, assuming both devices are connected to a reliable network and logged into the same Ableton User Account. Various Cloud-related software texts have been added in English, French, German, Italian, Japanese, Simplified Chinese, and Spanish. For more information about Cloud and Note, please refer to the following: Note Manual - http://www.ableton.com/en/note/manual Note FAQ - https://help.ableton.com/hc/en-us/articles/6240279343772
- Control Surfaces Added Control Surface support for the Arturia MiniLab 3.

## 11.2

### New features and improvements

- Capture MIDI Capture results are no longer influenced by the song tempo set by the target track's previous Capture attempts. When Live’s transport is running, Capture MIDI will keep longer phrases in captured clips.
- Control Surfaces In the Launchkey MK3 Control Surface script, the Quantise button can now quantize clips in Session or Arrangement View. The Launchkey MK3 Control Surface script now also works with the Launchkey 88. On the PreSonus ATOM SQ, it is now possible to scroll between device parameter banks by holding the bank navigation buttons down. In the ATOM SQ Control Surface script, it is now possible to control the Master Track volume and pan in Song mode when the Master Track is selected. The encoder sensitivity for the ATOM SQ Control Surface script has been refined to better match the parameters they control. Additionally, the encoders can be used to fine tune parameter values when the Shift button is pressed.
- Core Library Added audio and MIDI clips to Session View in Live’s Demo Song. In the DS Drum Rack preset, devices contained in the selected chain are now always shown by default.
- Interface The icons in Live’s Preferences and dialogs have been improved. Updated the appearance of the "Record/Warp/Launch" tab in Live's Preferences. The error dialog window that appears when loading a Live Set with disabled plug-ins now displays the track name before the timestamp. Live now shows different icons for Live Clip (.alc) files that distinguish between Audio and MIDI content in the browser. When renaming tracks, [Tab] will navigate to the next track or chain header, while [Shift][Tab] navigates to the previous track or chain header. Value ranges on vertical rulers in the MIDI Note Editor are now always displayed as two values stacked vertically. Improved drag and drop behavior within list views (such as the Groove Pool and device chains). Instead of always being inserted before the target item, dropped items will now be placed dynamically, depending on which half of the target item the cursor hovers over. In addition, the copy modifier [ALT] now works more consistently. When Num Lock is switched off on Windows, the number pad arrows, PgUp, PgDn, Home, and End keys now function as expected. Disabled devices now display an alert icon above error messages in Device View. When exporting multiple tracks, the option to also export video at the same time is now deactivated in the Export Audio/Video dialog. Updated various software texts. Updated various Help View lessons. Updated various software text and Help View lesson translations in German, Spanish, French, Italian, Japanese, and Simplified Chinese.
- Max for Live Updated the bundled Max build to version 8.3.1. For the changelog, visit: https://cycling74.com/forums/max-8-3-1-released live.banks: added warnings to explain non-reactivity in Max-only Dynamic Colors: changed label of ‘live_control_fg’ to ‘Text /Icon’ jweb / CEF: fixed usage in Max for Live (Windows) live.* ui objects: updated color code live.banks: banks configuration is retained if device is opened and saved in Max live.comment: linecount is preserved live.gain~: @orientation 1 typed-in a box works as expected live.gain~: auto-adapts when transforming to MC version live.observer: fixed value output after opening/closing Max editor crosspatch: works in the context of a Max for Live device hosted in Live Max for Live / Gen: improved fixes for intermittent crashes A new property in the Max for Live API allows users to observe the number of visible Macro Controls for a RackDevice. Audio driver input and output latencies are now taken into account for Max for Live devices that contain audio routings to external targets. If needed, users can revert to the previous behavior by using the -DisableM4LRoutingCompensation debug option in an Options.txt file. The time_signature_numerator, time_signature_denominator, time_signature_enabled and tempo_enabled properties are now available in the Max for Live API. Corrected descriptions for the properties have also been added. Improved and updated the scale_name and scale_intervals descriptions in the Max for Live API.
- New Devices and Device Improvements Reverb: The Reverb device's interface has been updated with a fresh design. The Reverb device's Density and Quality parameters have been renamed to Diffusion and Density. The parameter values for Density (previously Quality) have also been changed from Eco, Mid, and High to Sparse, Low, Mid, and High. Sparse mode allows for lower CPU usage. Added a Smooth dropdown menu to the Reverb device. You can now specify how the Size parameter responds when changed using the Smooth options None, Slow, or Fast. Setting Smooth to None means that some artifacts may occur when changing the Size parameter values. The Slow and Fast options ensure that new delay times are updated over a specific period of time, resulting in a more musical sound. Added a switchable filter type to the High filter in Reverb’s Diffusion Network. You can choose between a one-pole low-pass filter or a low-shelf filter. Optimized for better CPU performance. Tuner: The Tuner device now includes three new options for note spellings. You can access a menu with these options when you right-click anywhere within Tuner's UI: Sharps (C#) Flats (D♭) Sharps and Flats (C#/D♭) It is now possible to zoom out to a full octave in Tuner's Histogram View by clicking the interface and dragging the cursor horizontally. In the Phaser-Flanger device, the Phase parameter of the LFO now has a default value of 180 degrees. The Excitator section of the Tension device is now called “Exciter” in Live and on Push. A context menu option for a Hi-Quality mode has been added to the Delay device. Switching off Hi-Quality uses less CPU resources. The Channel EQ device now uses less CPU resources. Presets containing the Saturator device now run with improved CPU usage. Inactive visualization data will no longer be sent in the Wavetable and Phaser devices, resulting in slightly improved performance. When mapping and unmapping device parameters to Macros, the Map/Unmap labels now appear as expected. A Hi-Quality option has been added to the [right-click](Win) / [CTRL-click](Mac) context menu of the Redux device. Using Redux with Hi-Quality switched off saves some extra CPU.
- Plug-ins Added native support for AUv3 plug-ins on macOS 10.15 or higher. Live's Preferences now include options to enable both AUv2 and AUv3 plug-ins. Plug-in errors are now shown in Live’s Status Bar, along with a linked detailed error report. If the connection to an AUv3 plug-in gets lost, an error message will be displayed. The plug-in will also be disabled, the output muted, and the plug-in window closed.
- Push On Push 2, the parameter names of the AAS devices (Analog, Collision, Tension and Electric) have been improved and aligned with the UI for readability.
- Session View Improvements It is now possible to simultaneously rename multiple Rack chains in Session View. When navigating tracks and device chains using the left arrow key in Session View, navigation will stop at the first track header as expected.
- Setup To avoid incompatibilities, you will be asked to save Live Sets created with an older version of Live as a new file in Live 11.2. Renamed the Customization section of Live's Preferences to Display Customization, which now also includes the Zoom Display setting. Metal rendering is now enabled on macOS by default to improve UI rendering performance. To deactivate this, use the Options.txt entry -DisableGraphicsHardwareAcceleration.

### Bugfixes

- Live Bugfixes Improved Live's performance when selecting or deselecting many clips. On macOS, Live's UI would sometimes show graphical errors after opening Live on a HiDPI monitor, changing the Zoom Display settings to a value other than 100%, and moving the window to a LowDPI monitor. Fixed the appearance of the Phaser-Flanger device's Env Fol parameter when the device is deactivated. Fixed a bug that would stop the manual freeze output when switching the Spectral Time device's Freezer Fade Shape from Crossfade to Envelope mode. Fixed an issue that caused the Corpus device to output silence when using larger buffer sizes on Windows. Added info texts for the Frz > Dly and Dly > Frz toggles in the Spectral Time device. Added a missing info text for the Env Amt parameter in Collision’s Noise Filter section. Fixed some issues with the LFO and MPE Control devices. Previously, Live would crash when routing an Ext. Instrument's MIDI output to an MPE routing target if the track's device chain also contained a plug-in, Max for Live device, or certain built-in audio effects. The dropdown menu for Reverb's Density parameter is now 2px wider to avoid cutting off the word "Sparse.” Fixed an issue that could cause an invalid selection when selecting all chains in a Drum Rack in Session View. On Windows, Live’s UI now refreshes as expected after tapping [ALT] to open the main menu. Any time the Clip Detail view panels are arranged vertically, Live now opens the Envelopes panel and scrolls it into view when creating per-step automation on Push or using the "Show Automation" or "Show Modulation" context menu entries on a parameter. Opening a context menu on Windows with the keyboard shortcut [Shift][F10] no longer changes the time selection in Arrangement View, Session scene selection, or browser selection. On Windows, opening a context menu with the [Shift][F10] keyboard shortcut no longer changes the selected Session track header or Session clip. Fixed an issue that could cause artifacts when using the Complex or Complex Pro warping mode on clips that were only slightly warped. Fixed an issue that caused unnecessary freeze tail clips when freezing and flattening clips with small gaps between them. Fixed a bug that caused MIDI notes and audio waveforms to jiggle slightly when adjusting clip edges in Arrangement View. Selecting a velocity or probability marker and typing in a number sets the value as expected. When Rack Macro Controls and chains are unfolded, the Rand and Map buttons are now properly aligned. When showing or hiding chains in a Rack, the buttons would previously move up and down depending on the view shown. These buttons are now evenly spaced at all times. Fixed an issue that caused Session clips to be added over Arrangement clips when copying a track in Session View and pasting it into Arrangement View. Fixed an issue that caused inconsistent time signatures when launching scenes with specific time signatures in Session View, and then quickly going back to the Arrangement View. This issue could also cause the Re-enable Automation button to become stuck. When a track is frozen, the Velocity Range slider will now freeze as expected in MIDI clips. Fixed an issue that prevented the keyboard shortcut to expand Clip View [CTRL][ALT][E] (Win) / [CMD][OPT][E] (Mac) from working when switching from Session View to Arrangement View (or vice versa) when no clip was selected. Selecting time in the MIDI Velocity Editor now works as expected when multi-clip editing. When a user changes the MIDI Envelope Auto-Reset option in a set, they will be prompted to save the changes when they close the set or quit Live. Fixed an issue that caused Live to hang when zooming out of a clip with a small loop region that was being recorded. Fixed a crash that occurred when loading certain Live Sets containing more than 1,000 tracks. Fixed a crash that occurred when using the header area of a time selection to select time in a MIDI clip when in the Expression tab. Fixed a potential crash when opening old Live Sets that contained devices that have since been removed from Live. AU plug-ins are now informed about silent inputs so that they can release CPU resources and report output silence if possible. This will allow any device in the device chain after the AU plug-in to release CPU resources as well. Fixed an issue that caused note feedback to break when using certain Control Surface script interactions, such as repeatedly switching the note layout on Push while a MIDI clip was playing. Fixed an issue that inadvertently showed blue hand icons and device locking options for particular device control features not available in some Control Surface scripts. Fixed a bug that kept internal buffers of VST3 plug-ins from resetting properly. As a result of this fix, lingering signals (like reverb and delay tails) are now reset before audio export starts. Lingering signals can also be cut off quickly by clicking the Stop button three times. Fixed an issue with certain VST3 plug-ins that created unwanted artifacts in rendered audio. Fixed a crash that occurred when loading a Live Set with plug-in automation on the Master track, or on a Return or Group Track. Live no longer hangs when opening a dropdown menu while Grammarly is running. Fixed a crash that would occur when VST plug-ins requested the dedicated GPU, or when the user changed the macOS Battery "Automatic graphics switching” preference. Fixed a bug that caused silence and/or hanging notes when recording MIDI notes into clips that already contained those same notes. Improved high DPI support for VST3 plug-ins on Windows: Plug-ins that support high DPI and IPlugViewContentScale should be the correct size. Plug-ins that have their own resizing logic should not resize when the user drags the window around. Plug-in windows are instantiated with the correct size in both scaled and non-scaled modes. Plug-ins that support host-initiated resizing are interrogated by calling checkSizeContraint in the correct place. Plug-ins that support host-initiated resizing can be maximized by double-clicking on the title bar. Fixed a potential crash on Windows that occurred when closing Live right before the program tried to install default Packs. Fixed an issue with various Control Surface scripts that caused clip launch button LEDs to be in an incorrect state when changing the input type of a track. When using the ATOM, ATOM SQ, and FANTOM Control Surface scripts, Arm button LEDs now reflect a track’s implicit armed state. Fixed an issue in the SL_MKIII Control Surface script that resulted in incorrect LED button states when exiting Drum Mode. Fixed a crash when loading a corrupt Live Set containing non-unique Pointee IDs. Live now recognizes if the set is corrupt and displays a corresponding error message. Users can reach out to Support to see if their sets can be repaired. Fixed a bug where context menus would close abruptly if Voice Control was enabled on System Settings on macOS. Switching between Session and Arrangement View while a launched clip is playing on Push will now always display the clip as expected. Previously, Live would crash when deleting an instance of Simpler from a Drum Rack pad while the Simpler's Envelopes view was visible on Push. Previously, Live would crash when using the Extract Chains command on a Drum Rack chain that had automation or modulation for the Chain Send Level. Fixed an issue that deselected AU plug-ins after duplicating a selected plug-in. Fixed a crash that sometimes occurred when loading a plug-in that could not instantiate its presets. Fixed an issue that caused Live’s menu bar to become invisible after deleting all video clips if the video window was in Full Screen Mode on macOS. Fixed a crash that occurred when dragging and dropping another Live Set with Group Tracks into Session View as a new scene in certain circumstances.
- Max for Live Bugfixes Fixed a bug where adding Expression Control would create unnecessary undo steps. Fixed an issue that caused Shaper MIDI to produce unnecessary Undo steps. Fixed an issue that resulted in incorrect Undo values when using Align Delay in Distance mode.

## 11.1.6

### New features and improvements

- The Launchkey MK3 Control Surface script now works with the Launchkey 88.

### Bugfixes

- Live no longer hangs when opening a dropdown menu while Grammarly is running.

## 11.1.5

### New Features and Improvements

- When renaming multiple scenes via the context menu, the edit area will appear on the scene that you right-click and the scene selection will be preserved even if a highlighted scene was not selected.
- The Expand Clip Detail View shortcut is only enabled when it makes sense, e.g., when a clip is selected and the Clip View is visible.
- When collapsing the Clip View (for example by using the shortcut [OPT][CMD][L]) while it’s expanded and then re-opening it again, Clip View comes back in its expanded size as expected.
- Clip borders are now drawn in an opaque color to improve visibility.
- In Arrangement View, the right-click context menu grid setting options now appear as expected, even when there are various time signatures in the Arrangement.
- When a new software update is available and your auto-update preferences are set to Ask Me, a link to the latest release notes is included in Live’s Status Bar notification.
- Live will also show a link to the release notes in the Status Bar when downloading a new update, and once the download is complete.
- Updated the software texts for the Collision instrument.
- Updated software texts and Help View lessons in English, French, German, Italian, Japanese, Spanish, and Simplified Chinese.
- Users will see shorter names for certain values (e.g. waveform shapes) in various devices on Push 2.

**Max for Live Updates and Improvements**

- Updated the bundled Max build to version 8.2.2. For the complete changelog visit: https://cycling74.s3.amazonaws.com/support/version_8_2_2.html
- amxd~: eliminated extra border added to device after being dragged into patcher
- amxd~: improved error message object identification
- Dynamic Colors: default Max for Live device patcher background color follows Live's theme
- Dynamic Colors: load time improvements
- jsliveapi: ensure boxpath (fixes M4L.chooser issues)
- live.dial: fixed triangle color
- live.gain~: fixed cursor location on mouse up
- live.step: dynamic colors work as expected
- Max for Live Device Projects: dirty the device when dependencies are added
- Max for Live Patter device: fixed crash on load (Live 11.1.b8)
- Max for Live unique identifier / ---: maintained when loading poly~ patchers
- panel: fixed enabling / disabling window_drag in Max for Live device subpatchers
- It is possible to unset the property when using live.observer by sending a property message without an argument (or property “”) without Max printing a warning to the console.
- Max for Live users now have access to the duplicate_notes_by_id function of the Clip LOM object.
- The view properties of the Wavetable and Compressor devices are now available in the Max for Live API.
- In the Max for Live API, get_notes_extended, get_all_notes_extended, get_selected_notes_extended and get_notes_by_id now optionally take their arguments in the form of a single dict. This dict can have an additional key or filters mapped to a list of note property names. If filters are provided, the returned dictionaries will only contain the specified properties rather than the full note descriptions.
- Setting a property on a live.observer without a valid LOM ID no longer causes a warning to be printed to the Max console.

### Bugfixes

- Improved Live’s performance when resizing clips in Arrangement View.
- Fixed a visual bug that caused small time selections to flicker when zooming out in Arrangement View.
- Fixed a bug on macOS that distorted the appearance of mouse cursors on HiDPI/Retina screens.
- Selecting Jump from the Follow Action drop-down menu now shows the text "Jump" (the full text is slightly cut off). The Follow Action Chance percentages are also now aligned to the right.
- Fixed a bug that caused missing MIDI notes when drawing with the pencil tool in quick or large gestures while multi-clip editing.
- Fixed an issue that caused Live to incorrectly show video clips on the uppermost track (instead of the bottommost track) in Live Sets with multiple overlapping video clips.
- When a warped clip is frozen, the Grain Size parameter of the Tones warp mode is also frozen.
- When renaming multiple clips in Arrangement or Session view via the context menu, the edit area will be shown in the clip that you right-click.
- Fixed an issue that occurred when navigating with the Tab key while renaming multiple clips.
- The clip names of frozen take lane clips now appear as expected in Draw Mode.
- Extending an unwarped clip past the original clip end now functions as expected.
- When Draw Mode is enabled, grid lines will appear as expected in take lane clips.
- The time selection of folded tracks in Automation Mode now appears as expected.
- Using [Tab] and [Shift][Tab] while renaming tracks now allows the user to cycle between the first and last tracks in Arrangement View.
- In multi-clip editing, the Transpose and Velocity range sliders now become activated/deactivated as expected based on note/time selection.
- Fixed an issue that caused extra spacing to appear in track title bars when deleting multiple tracks.
- Fixed an issue that caused duplicate send letters in a return chain when renaming the chain in a Drum Rack.
- Fixed a bug that caused loud audio spikes in Wavetable under rare circumstances.
- Fixed a small bug with multi-clip editing where some notes would not be selected properly in certain scenarios.
- Scrollbars appear as expected when a long list of items is displayed.
- Consolidating audio clips no longer takes additional time when plug-ins are on corresponding return tracks.
- If making a time selection with the mouse in multi-clip editing mode, the time selection will be preserved when clicking and dragging a note from the background clip.
- In multi-clip editing, selecting multiple notes by dragging the mouse right to left and then moving the selected notes now works as expected.
- Navigation behavior between take lanes, clips, scenes, and tracks is now more consistent.
- Fixed an issue that caused time signatures changes in Arrangement View to be removed when freezing a track that also contained Session View clips.
- Fixed an issue that caused tracks that were copied and pasted into an automation lane or take lane in Arrangement View to be added to the last track position.
- Fixed a bug that would cause Live to crash or hang when unplugging the audio output device during export.
- Fixed a bug that caused Live to mistakenly load an outdated DefaultLiveSet.als in newer versions of Live.
- Duplicating time between two time signature change markers no longer adds an unexpected duplicate time signature change marker in the Arrangement.
- Updated values for automated MIDI CCs are now sent when scrubbing in the Arrangement or setting an Arrangement insert marker, even on armed MIDI tracks.
- The Auto option in the piano roll’s Accidentals context menu now always displays the actual spelling used.
- Fixed an issue that caused Host Automation from a plug-in routed to an Ext. Instrument or Ext. Audio Effect device on another track to not play back when the track was frozen.
- Fixed a bug that caused note-off and pitch bend reset messages to be sent to all routed MIDI outputs when the device chain of any track changed.
- MIDI CC automations from the clip will play when the track monitor mode is set to “In”, which is consistent with how other automations are played back.
- On Push 2, the Frequency and Width parameters for the Corpus device are now displayed correctly.
- Fixed a crash that sometimes occurred when selecting tracks that contained missing VST2 plug-ins.
- Fixed a speculative issue with Audio Unit plug-in parameters that have type MIDINoteNumber, have no display names attached to their values, and have a value range that does not begin at zero.
- Fixed a crash that occurred when adding a preset of an unavailable plug-in to the end of a device chain.
- Fixed a crash caused by adding certain plug-ins (such as Omnisphere) to a track and then undoing the action. Live would also sometimes crash when trying to re-open the same Live Set after the initial crash.
- ​​Fixed a bug that caused preset parameters to load incorrectly in VST plug-ins on Apple M1 machines.
- Fixed a crash caused by adding MIDI Effect Racks onto MIDI tracks that were routed to one another but contained no instruments in their device chains.
- Fixed a crash that occurred when opening Flux:: VST2 plug-ins.
- Fixed an issue for VST3 plug-in development that caused projectTimeSamples to sometimes be incorrect.
- Fixed a regression that impaired Live's ability to deliver host information to VST2 plug-ins.
- Fixed an issue that caused scanning VST plug-ins from Live’s Preferences on Apple Silicon computers to take longer than expected.
- Scanning VST2 and VST3 custom folder paths now works as expected.
- Added support for the sharp symbol (♯) to Control Surface scripts that display parameter values as pitch names.
- Fixed the device selection behavior of several Control Surface Scripts (such as APC Mini and Launch Control XL) so that it no longer interferes when selecting chains within an unfolded Drum or Instrument Rack in Session View.
- Fixed an issue that caused adjustments to song time using a Control Surface script encoder or jog wheel to stop working after a play maker had been set in Arrangement View.
- Fixed several issues with the MackieControl and MackieControl_Classic control surface scripts that resulted in button LEDs being left in incorrect states.
- The KeyLab and KeyLab88 control surfaces no longer cause Live to lag when active.
- Fixed an issue in several control surface scripts (such as ATOM SQ and KeyLab_Essential) that created unnecessary undo steps when adjusting parameters.
- Fixed an issue in the SL_MkIII control surface script that caused the knob widgets of the displays to move abruptly.
- Fixed an issue in the SL_MkIII control surface script that created unnecessary undo steps when adjusting volume with the sliders.

## 11.1.1

### New features and improvements

- The FANTOM control surface script will now be automatically configured for FANTOM 06, 07, and 08 users.

## 11.1

Please note there is no automatic software update for 11.1. Check out this article for information on manually updating Live .

### New features and improvements

- Native Apple Silicon Support Live 11.1 adds native support for Apple M1 computers.
- Arrangement View Improvements You can use the left arrow key to navigate from an automation lane or take lane to the main track, this will fold the lanes as well. You can also use the left arrow key to navigate from tracks in a group to the main Group Track. The Arrow Left/Right shortcut has been added to the Arrangement Track Title Bar info text. The shortcut folds/unfolds the track. The Arrow Left/Right shortcut has been added to the Toggle Additional Automation Lanes info text. The shortcut folds/unfolds additional automation lanes.
- Browser A new Devices icon has been added to Live’s Browser: When viewing Sets in the browser, you will see a Devices icon for device chains on a track that contain at least one device. When you expand a Live Set in the browser, either from the Current Project folder, Templates folder, or a folder of Sets you have added in Places, you can unfold the tracks in the Set to reveal their device chains. These chains can then be moved into the current open Set using drag and drop or by double-clicking on the chain. The Device settings from the original Set are retained but any previously recorded automation is not.
- Capture MIDI In the first captured MIDI clip (in an empty set with the transport stopped), if the detected loop is eight bars or less, the first played note is considered the start of the loop. When only one note is played in the first captured MIDI clip (in an empty set with the transport stopped), the loop boundaries are set to the note start and end, and the tempo is accordingly calculated, resulting in a one, two, four, or eight bar loop. This is particularly useful when playing a rhythmical sample with a single MIDI note. In Session View, new captured clips now use the “Adaptive Grid: Narrow” setting instead of “Fixed Grid: 1/16.”
- Clip View Added responsive Clip View options: In Clip View, all clip properties are now displayed in panels/tabs instead of separate panels. Clip View properties can be arranged vertically by moving the mouse cursor to the left from the Clip View panel edge next to the Sample Editor/MIDI Note Editor. Clip View properties can also be arranged automatically, which switches between the horizontal and vertical views depending on the height of the Clip View area. Select “Arrange Clip View Panels Automatically” from the View menu to enable this option. When Clip View panels are arranged vertically, the individual tabs (e.g. Clip, Audio, Envelopes, etc) can be collapsed and expanded using the arrow icon to the right of the tab header. When Clip View panels are arranged vertically, the individual tabs (e.g. Clip, Audio, Envelopes, etc) can be folded/unfolded using the Arrow Left/Right keys. Sample information for audio clips (e.g. sample name, sample rate, etc) is also displayed in the Clip View and appears differently in the vertical/horizontal view modes. Clip View panels can now be accessed using keyboard shortcuts. In MIDI clips, ALT + 1 switches to the Notes panel, ALT + 2 switches to the Envelopes panel, and ALT + 3 switches to the Note Expression panel. In audio clips, ALT + 1 switches to the Audio panel and ALT + 2 switches to the Envelopes panel. Clip View can be toggled to its maximum height using the keyboard shortcut CTRL+ALT+E (Win) / CMD+OPT+E (Mac) or the View menu entry “Expand Clip Detail View.” The chosen Responsive Clip View mode is now saved in Live’s Preferences.cfg file. When multiple audio clips are selected, the sample properties (sample rate, bit depth, and channel count) for all samples will be displayed in the Clip View. If a value is not the same for all samples, the character “*” will be displayed. In Clip View, you will also see the total number of samples selected. The Pitch dial is now smaller and the Gain slider has been enlarged. When switching between panels in Clip View using the keyboard shortcuts ALT + 1/2/3, the panel header that was switched to will be selected. If Clip View is arranged horizontally when Live is first opened and either the Audio or Notes tab is selected, the corresponding panels in both audio and MIDI clips will remain unfolded when switching to Clip View’s vertical arrangement.
- Comping You can now duplicate selected take lanes using the keyboard shortcuts CMD + D (Mac) / CTRL + D (Win), or by right-clicking on the take lane header and selecting “Duplicate.” Changing the color of a clip in a take lane changes the color of the corresponding clip in the track’s main lane and vice versa. Splits are created on the updated clips in certain cases when the relation between other highlights on different clips change. The horizontal lines that separate multiple take lanes match the color of the clips that are in those lanes. When renaming multiple tracks or take lanes using the context menu option, you will see the edit field when you right-click on a track or take lane.
- Control Surfaces When navigating between devices on a selected track with the PreSonus ATOM SQ, you can now scroll between devices by holding the navigation buttons down. If an invalid CC, note, or channel value is used in a UserConfiguration.txt file, the associated User Remote Script can still be loaded.
- Core Library Frequency Shifter presets are still available in Core Library/Devices/Audio Effects/Legacy/Frequency Shifter
- CPU Meter The CPU meter drop-down menu now can be customized to display: both the Average or Current CPU usage levels only the Average level, with the Current level switched off only the Current level, with the Average level switched off Alternatively, the CPU meter can also be switched off entirely. By default, Live will not display the Current level; it must be enabled from the drop-down menu.
- Interface You can use the left and right arrow keys to switch between radio buttons anywhere in Live. If you are switching between radio buttons on a device that is inside of a Rack with the left and right arrow keys, you can get back to moving between devices in the Rack using the left and right arrow keys by hitting the ESC key. In Session and Arrangement View, the Monitor radio buttons now have a default state that can be restored. When the In/Out section is expanded, you can press the Delete key to reset the Monitor radio buttons to the default (“Off” for audio tracks and “Auto” for MIDI tracks). This option is also accessible via the Edit menu option “Return to Default.” The Quantize Settings dialog buttons in the MIDI Note Editor now say “Apply” and “Close” instead of “OK” and “Cancel.” Deactivated device title bars are easily readable in all Live Themes, even if the device is selected. On Mac, the mouse cursor will now display an arrow pointing in a single direction when hovering over split views which can be resized in one direction only. An error message will be displayed in the status bar if an auto-update cannot be downloaded. Added a new "MIDI Envelope Auto-Reset" entry to the Options menu: When enabled, certain MIDI control message types that are not automated for a given clip will automatically reset at the start of a new clip. Note: for users who intentionally work opposite to this behavior, enabling this change will make corresponding Live Sets behave differently. In Live 11.0.5, "MIDI Envelope Auto-Reset" is disabled by default. In Live 11.1, "MIDI Envelope Auto-Reset" is enabled by default for new Sets, and disabled by default in older Sets. Updated various info texts. Updated some Help View lessons. Added support for keyboard shortcuts on French keyboard layouts for macOS versions 10.14 and older. Keyboard shortcuts that have numbers can be accessed without having to press Shift to access the number keys.
- Max for Live Updated the bundled Max build to version 8.2.1. Link functions have been added to the Max for Live API. You can access the IDs of newly created notes using the Python API or the Max for Live API. It is possible to get a dictionary of all the notes in a MIDI clip using the Python API or Max for Live. It is now possible to call select_notes_by_id on a Clip object in Max for Live, passing a list of note IDs. This will select only those notes that have the provided IDs. Users can now get and observe the average_process_usage, peak_process_usage, and a track's performance_impact via Max for Live. When Max fails to load, an error message will be displayed that contains a link to a Knowledge Base article that explains potential causes for the issue and steps to take to resolve it. Error reporting in the Max Window is more consistent. Four new theme colors are available in Max for Live. amxd~: ‘realtime_params’ attr for realtime report of parameter data from outlets Dynamic Colors: ability to use a name which references a dynamic color (follows Live or Max color Themes) live.adsr~ / live.adsrui: new objects
- MPE Added the ability to configure zone settings for MPE output. You can use the settings to: configure the MPE zone and range of note channels used by Live when sending MPE to an external MIDI device or plug-in select the upper or lower zone and number of note channels select multi-channel mode, which sets an arbitrary range of note channels
- The MPE settings dialog can be accessed via the External Instrument device, the context menu that appears when right-clicking an MPE-enabled plug-in, or through the I/O panel of MIDI tracks with no instrument in their device chain.
- The above MPE settings can be used for hardware synths that require a specific MPE configuration, or plug-ins that do not officially support MPE but can be used with MPE controllers due to their multi-timbral support.
- Multi-Clip Editing Time selection interactions, note selection interactions, and new note editing options have been added to multi-clip editing: Time in the MIDI Note Editor can be selected across loop and clip boundaries. Note editing (e.g. copy, cut, paste, delete) can be used when working with note selections across clips and loop boundaries. Notes can be cut or copied from multiple clips and inserted into the same set of clips, as long as the clip selection/foreground clip has not changed, or into a different clip once that new clip has been selected. Selected loop bars can now be duplicated using the context menu or the CMD + D (Mac) / CTRL + D (Win) keyboard shortcuts. In Arrangement View, it is possible to draw notes in background clips without first changing the foreground clip. Notes can also be drawn continually across clip boundaries, except in Focus Mode. When using a pen to draw notes with "Draw Notes with Pitch Lock" enabled, any notes that cross a loop boundary are no longer deleted. When more than 64 clips or eight tracks are selected in Arrangement View, the MIDI Note Editor is no longer available for multi-clip editing to prevent potential performance issues.
- New Devices and Device Improvements Introduced "Shifter", a new audio effect in Live Standard and Suite. Shifter is a multi-purpose audio effect for pitch shifting, frequency shifting, and ring modulation. The pitch or frequency of incoming audio can be tuned using Coarse or Fine parameters and further adjusted with a Tone filter and Window parameter. Shifter also has Delay, LFO, and Envelope Follower sections for additional modulation. The Shifter device can set pitch or frequency using its own parameters or by incoming MIDI notes. Introduced the Align Delay device, which is now included in the set of Max for Live devices that come with a Suite license, or a Standard plus Max for Live license. Align Delay is a Max for Live device that delays incoming signals by samples, milliseconds, or meters/feet. Introduced the Shaper MIDI device, which is now included in the set of Max for Live devices that come with a Suite license, or a Standard plus Max for Live license. Shaper MIDI is a Max for Live MIDI device that uses multi-breakpoint envelopes to generate mappable modulation data. The Cytomic Filters, which are used in the Wavetable, Echo, Simpler, Sampler, Operator, and Auto Filter devices, have been updated and improved in stability, sound and performance. As of 11.1, the Cytomic filters (particularly the MS2 and SMP options) might deviate in sound compared to previous Live versions, especially when driven hard. An update to the Softtube libraries may cause subtle sound changes in the Amp and Cabinet audio effects. In the Sampler, Wavetable, Impulse, Simpler, Channel EQ, Hybrid Reverb, Chorus-Ensemble, Phaser-Flanger, Echo (output knob only), Spectral Resonator (input send only) devices, Gain controls now increment/decrement consistently by 1 dB when pressing the up/down arrow key, or by 0.1 dB when pressing the [Shift] key. Spectral Time: The effect order can now be reversed using two radio buttons “Frz > Dly” or “Dly > Frz” on the right panel of the Spectral Time device above the Dry/Wet knob. A “Zero Dry Signal Latency” option has been added to the context menu in the Spectral Time device. Enabling it reduces the latency of the dry signal to zero instead of syncing it with the output of the effect. This option is useful when playing a live instrument through Spectral Time and monitoring the output. Spectral Resonator: In the Spectral Resonator device, the Shift parameter will now increment/decrement by one semitone when pressing the up or down arrow keys, or by one octave when holding the Shift key. Wavetable: A context menu option for Hi-Quality mode has been added to the Wavetable device. When Hi-Quality is off, Wavetable modulation is calculated every 32 samples. Low-power versions of the Cytomic filters are also used to further reduce CPU. Using Wavetable with Hi-Quality mode off can save up to 25% CPU compared to having it enabled, which is ideal for working with large sets or maintaining low latencies. Please note that as of 11.1, Hi-Quality mode will be off by default when loading a new instance of Wavetable or any of its Core Library presets. However, any user presets or Live Sets created previously will still load Wavetable in Hi-Quality mode to ensure sound consistency with earlier Live versions. Subtle sound differences may occur when Hi-Quality mode is enabled.
- Packs For the latest Live Pack updates and bugfixes, check out the Packs Release Notes .
- Push Device Visualization On Push 2, the Hybrid Reverb parameter banks Algorithm 1 and Algorithm 2 have been renamed to Algorithm Pg 1 and Algorithm Pg 2. Also some parameters for Hybrid Reverb on Push 2 have been rearranged for easier navigation. Updated some parameter names for the Chorus-Ensemble device on Push 2. The Saw Up and Saw Down icons for Sampler’s LFO waveforms on Push 2 now appear as expected.
- Session View Improvements Using the left and right arrow keys to navigate the Session View no longer skips return tracks, if they are visible. Multi-selecting scenes now behaves the same as multi-selecting clip slots. Selecting scenes no longer highlights the Master track, instead the scene itself is highlighted. Navigating from the last clip slot to a scene with the right arrow key will highlight the Master track. You can click on a scene number or the Master track header to access the Master track and Scene View panel.
- Setup To avoid incompatibilities, you will be asked to save Live Sets created with an older version of Live as a new file in Live 11.1. In Live’s Preferences, file paths that are unavailable (e.g. if an external drive is not connected) display a “(not available)” message. Paths that haven’t been set yet display a “(not set)” message.

### Bugfixes

- Live Bugfixes Devices that use beat sync divisions now remain in sync when the device is re-enabled during playback. The Filter LFO dropdown menu in the Tension device now appears as expected. Previously, when merging a device chain containing no instrument with another device chain containing an instrument, the instrument would be deleted from the merged chain. Live no longer moves samples from a temporary project to the final saved project folder. Fixed a bug that created file path issues with the Live Recordings temporary folder if it was also saved and renamed in Places. The undo text for changed clip colors has been corrected in the Edit menu. Previously, if a plugin was grouped into an Instrument or Drum Rack, the MPE settings of the plugin were not retained when the Rack was saved as a preset. Fixed a crash that occurred if non-supported MPE data (e.g. MIDI CCs other than Pitch, Slide, or Pressure) was sent to a Sampler/Simpler device. Fixed a crash that occurred when clicking on a parameter in Live and adjusting the same parameter using an encoder on Push at the same time. Fixed a crash that occurred if all return/delay tracks were deleted and then a track containing a take lane was duplicated and moved. Live would crash if undo was selected twice after duplicating and moving the track. In the Filter/Mod section of the Delay device, a custom icon for the Ping Pong setting is now displayed on Push 2. Fixed a crash that occurred when going to “Save Set as Template” from the File menu, then typing the name of the set, and finally pressing the [Escape] key twice to cancel the process. Fixed a bug that caused peak CPU load to be calculated incorrectly if the buffer size selected in Live’s Preferences wasn’t a multiple of 64 samples. Fixed a crash caused by loading multiple instances of certain VST3 plug-ins when Live’s transport was running. Fixed an issue in Session View that caused notes to sometimes be triggered twice when recording a MIDI clip with both “Record Quantization” and “Chase MIDI Notes” enabled. Fixed an issue caused when using multiple Control Surface scripts that are set to automatically arm MIDI tracks. When highlighting an area of a take lane using Draw Mode, the clip name appears as expected. Plug-ins that cannot be loaded appear with a standard device background that includes a more detailed error message. Loading .alc files from Core Drum Kits into Arrangement View now preserves the Drum Rack chain routings. In Arrangement View, the dialog box that appears when multi-clip editing is no longer available because more than eight tracks are selected appears as expected. When several audio clips with different pitch values are selected, you will see the range of values for each clip highlighted in blue on the Pitch dial in Clip View. Renaming take lanes in linked tracks works as expected. Folded clips with long fades appear as expected. Fixed an issue that caused clip fades to reset when resizing adjacent clips. Fixed a crash caused by some VST3 plug-ins with certain undesignated MIDI CC mapping parameters. The CTRL + 5 fixed/zoom adaptive grid keyboard shortcut works as expected on Windows. Fixed an issue in Session View that caused notes to sometimes be triggered twice when recording a MIDI clip with both “Record Quantization” and “Chase MIDI Notes” enabled. Fixed two bugs that caused the time selection to not be updated as expected when editing several clips compared to editing a single clip. E-Piano Wurli.adg preset: Volume Macro is now excluded from randomization. Womp Bass.adg preset: Typo in original file name is now fixed. If the preset was previously part of Collections it needs to be added again. Fixed a crash caused by copying and pasting a device from the browser into a Drum Rack’s return chain in the Session Mixer under certain conditions. Fixed a crash caused by clicking in a certain area of the Sample Editor when editing unwarped audio clips in Clip View. Fixed a crash that occurred if a user tried to change the scale of a Live Set from Push while having the Focus mode on in multi-clip editing mode without a clip selected. Fixed an issue that caused some Live Sets to become corrupted even though the sets could be opened normally in earlier Live versions. Removing the MIDI mapping of the Pitch control in audio clips using the Delete key works as expected. Fixed a bug that caused the Pitch parameter in audio clips to move too quickly when “Pen Tablet Mode” was enabled in Live’s Preferences. Fixed a crash caused by pressing Tab or Shift-Tab while holding the mouse cursor on a parameter in Clip View. In Draw Mode, when Pitch Lock is off, users will now get consistent results: a line/curve of notes will follow mouse movement without producing gaps or unexpected layers. In Draw Mode, when Pitch Lock is on, users can draw back and forth along a key track without removing any notes that are placed underneath (the same as in Live versions prior to 11.0). When syncing Live to an external MIDI clock, if the MIDI clock signal gets lost, the Ext Sync button will switch off after the dialog in Live appears saying that the signal has been lost. The grid spacing is now displayed in the MIDI editor as expected after warping and unwarping audio clips. Fixed an issue when resizing audio clips in Arrangement View using the mouse and Shift key that caused clips to continually be resized even after letting go of the mouse. Fixed an issue in several Control Surface scripts that resulted in incorrect LED button states when deleting tracks. Fixed an issue on Apple silicon computers where Drum Racks nested inside of an Instrument Rack could produce CPU overload and audio dropouts even when many of the nested chains were silent. Fixed a bug that caused the Freezer section of the Spectral Time device to remain active even if the device itself was deactivated. Fixed an issue that caused auto-updates to fail on certain computers on Windows OS. Fixed an issue that caused MPE pitch bend breakpoints to be removed if a note transformation, such as Quantization, was applied. Fixed a crash caused by certain plug-in parameters if they no longer existed in a newer version of the plug-in. Plug-in parameters that are no longer available will be displayed as deactivated. Fixed a crash caused by pasting a track in Arrangement View immediately after scrolling with a mouse wheel or trackpad. Fixed a crash that occurred when deleting the last scene in Group Tracks under certain circumstances. Fixed a crash that occurred when frequently switching the Max for Live Note Delay device on and off in between note on and off messages. Fixed an issue with the Note Length MIDI effect that caused the incorrect velocity to be generated in release mode if a note was released after recording in a loop. The Launchpad Mini MK3 Control Surface script now works as expected when pressing the Scene Launch Buttons after entering and then exiting Session Overview. Fixed an issue that caused the Scale MIDI Effect to cut off played notes if the scale was set to a single note. AU plug-ins are now informed about silent inputs so that they can release CPU resources and report output silence if possible. This will allow any device in the device chain after the AU plug-in to release CPU resources as well. Fixed a crash on Windows that occurred if a dialog window opened while a context menu was also visible. Fixed an issue that caused Push to get stuck on the logo screen. MIDI notes and waveforms no longer jiggle when dragging a clip back and forth from its left edge. On Windows, closing a VST3 plug-in window no longer minimizes Live. In large sets containing thousands of scenes, Live’s UI no longer lags when changing a parameter value with MIDI CC. Crashes that occurred when dropping a device with no MIDI or audio output onto a device chain are now prevented. Fixed certain crashes that involved VST3 plug-ins or Max for Live devices on Windows. Fixed a crash caused by dragging multiple Drum Rack chains into the panel window of the rack that displays how many chains are selected. Fixed a crash that occurred when freezing or rendering audio in certain scenarios. An error message will now appear saying that the rendering process has been stopped and to contact Support. A custom location for the User Library or Factory Packs will not reset back to default if Live launches and cannot find the custom path (for example, a disconnected external hard drive). Fixed several issues with the MackieControl and MackieControl_Classic control surface scripts that caused incorrect button LED feedback. When using the Mackie Control Surface script, the Mixer button LED will flash on or off depending on whether Follow is on or off in Live.
- Max for Live Bugfixes When the LFO device's modulation waveform exceeds its minimum/maximum, it now draws a horizontal line, as is consistent with the Envelope Follower and Shaper devices. The MPE Control device no longer creates high CPU spikes when receiving MIDI CC 64 (Sustain). Fixed various bugs that affected these bundled Max for Live devices: Envelope MIDI, LFO, Note Echo, and MIDI Monitor. Fixed a bug with the Expression Control device. Fixed a bug that caused the Max for Live device MPE Control to block MIDI Program Change messages. Key events keep working when a selected Max for Live device becomes invisible. Selected parameters of a Max for Live device can still be controlled by key events even if the device is no longer visible. The correct return IDs of newly created notes will be added to new clips when using the Python API or Max for Live API. Mapped waveforms in the LFO device appear as expected. Setting the MPE Control device Pitch Curve to an S Curve shape works as expected. Fixed an issue that could cause CPU spikes when using Channel Aftertouch in the MPE Control device. Control Surfaces are now represented by their LOM ID as expected when retrieving the list of control_surfaces via live_app in Max for Live. The waveform displays in the Max for Live devices Envelope Follower and Shaper now appear as expected. Assigned grooves are no longer lost when using the "duplicate_clip_to_arrangement" Max for Live API function to duplicate a Session clip to Arrangement View. amxd~: notifies parameter hub when device state changes jit.gl.model: fixed file loading when embedded in a Max for Live device jsliveapi: eliminate crash when there's no 'this' for operations jsliveapi: improved handling of large strings live.* UI objects: improve negative value handling with some units live.* ui objects: Outputs the correct value when opened and initialized by pattr live.banks: error reporting refinements live.banks: fixed bank renaming in response to '-' argument live.banks: fixed crash when adding a new bank with index 1 when banks are empty live.banks: fixed crash with certain 'edit' messages live.banks: fixed crashing with bad input live.dial: fixed large mode automation drawing live.drop: ensure value when restoring live.scope~: fixed delayed drawing after deletion Help patchers: fixed crash clicking '?' menu in Live Device project: fixed hang when changing the "development path type" Editor Startup: improved Windows startup times Live Object Model doc: updated with Live 11 additions Parameters: filters hidden parameters before generating automation for Live pcontrol: scheduler works in patches opened via load message Timing: improved locked metro accuracy Max Console in Max for Live: long text wrapped and shows device name Object Browser: Max for Live UI objects shown in correct category Object Palette: icons added for all live.* UI objects Parameters Window / Inspector: auto-quote Info Title / Info Parameters: only dirty if it exists in a Max for Live device Performance: CPU usage improvements after starting Editor jit.gl.lua: fixed outlet functionality (fixes Inspired by Nature Max for Live devices) live.scope~ / live.adsrui: updated icons umenu: improved popup positioning with multiple displays at mixed resolution/zoom Windows: increased main thread stack size to match OSX (8 MB)

## 11.0.12

### New features and improvements

- Fixed an issue on Apple silicon computers where Drum Racks nested inside of an Instrument Rack could produce CPU overload and audio dropouts even when many of the nested chains were silent.

## 11.0.11

### Bugfixes

- Fixed an issue that caused some Live Sets to become corrupted even though the sets could be opened normally in earlier Live versions.

## 11.0.10

### New features and improvements

**Arrangement View**

- It is now possible to solo tracks with the "S" key and arm tracks with the "C" key when take lane headers or automation lane headers are selected. Before, this was only possible when track headers were selected.
- Pressing "Tab"/"Shift"+"Tab" while renaming an Arrangement clip now selects the next/previous clip on the same track or take lane.
- When reaching the end when navigating with the "Tab"/"Shift"+"Tab" or Arrow Up/Down keys while renaming tracks or clips in the Session or Arrangement View, the navigation now cycles to the beginning or end of the tracks or clips, similar to using "Tab"/"Shift"+"Tab" when renaming scenes.
- It is now possible to fold/unfold a track's additional automation lanes with the left/right arrow keys when that track's main automation lane is selected.

**Clip View**

- When transposing an unwarped audio clip: The time ruler below the waveform will change to show the accurate amount of seconds in the waveform. The play position is preserved, causing smooth playback of the waveform and respecting scheduled Follow Actions.

**Comping**

- When choosing a take lane for recording, Live now uses the first take lane that provides enough space. Before, Live used the take lane following the last take lane that did not provide enough space.
- Previously, unnecessary splits might be created on an Arrangement track's main lane, when dragging the split line of adjacent highlights on a take lane. Now the behavior when resizing adjacent take lane highlights is more consistent.
- The vertical size of take lanes on linked tracks is now synced with a take lane that is being resized by dragging. The position of the dragged lane is sustained to keep the visible resized dragged lane visible and avoid jumping.

**Control Surfaces**

- Added the following improvement to the functionality of User Remote Scripts: Device Control: Up to 16 encoders can be used for controlling Device Parameters. The Device Activator button can be controlled. Mixer Control: An unlimited number of Tracks can be controlled. Track Mute, Solo and Selection can be controlled. The Crossfader and Cue/Preview Volume can be controlled. Transport Control: Session Record, Arrangement Overdub, Metronome, Punch-In, Punch-Out, Nudge Down, Nudge Up and Tap Tempo can be controlled.

**Follow Actions**

- When transposing an unwarped audio clip, the position of the Follow Action marker will change to keep in sync with the playhead and the actual beat-time of the Follow Action.

**Interface**

- On Windows, if a UI element has the focus, its context menu can now be opened via the Menu key or "Shift"+"F10".
- On Windows, context menus shown when pressing "Shift"+"F10" more accurately represent what would be shown when right-clicking using the mouse.
- When Sets are saved with the File menu's "Save Live Set as Template..." or "Save Live Set as Default Set..." command, they are automatically self-contained in the same way as Sets that use the File Manager’s "Collect and Save" function.
- The splitter between Live's main window and the Help View can now be grabbed and adjusted at its full height.
- Note names in Drum Rack pads are now displayed until no character fits at all. Standard note names are now displayed without the octave number if the full name does not fit.
- Live now has improved performance in certain scenarios.

**MIDI Editing**

- Added the following changes to how velocity/probability values are displayed: A MIDI note's velocity/probability values are now displayed in the respective Velocity/Chance Editor’s lane header when hovering over its velocity/probability markers. In Draw Mode, a note's velocity/probability values are displayed when hovering over the area in which the drawing action is available for that note. If any notes are selected, only those note's values can be displayed in the ruler, and hovering respects the quantization grid. When drawing a velocity/probability ramp, the value range is displayed in the respective Velocity/Chance Editor’s lane header. If any notes are selected, only those note's values can be displayed in the ruler, however hovering does not respect the quantization grid.
- When adding a new note to a MIDI clip or reactivating a previously deactivated note, if the clip is playing and the playhead is within the new or deactivated note, the note will be played immediately.

**MPE Editing**

- When the Note Expression tab is open, a "Clear All Envelopes" entry in the context menu of the MIDI Note Editor and per-note expression lanes clears all expression envelopes of one or multiple selected notes.
- Stretching a MIDI note using the MIDI stretch markers in the MIDI Editor or the ÷2 and x2 buttons in the Notes tab will now cause any per-note expression belonging to that note to be stretched as well.
- When sending notes to a plug-in device, external device, or Max for Live device that has MPE Mode enabled, reoccurring notes with the same note number will now reuse the same channel. This can result in more consistent behavior of multitimbral instruments.
- MIDI track meters now indicate MPE per-note controller changes. The lowest dot in a meter lights up in a blue color if per-note controller changes pass that meter.

**New Devices and Device Improvements**

- Plug-in devices that have MIDI outs and that have MPE enabled can now output MPE.
- Spectral Time: The Freeze Trigger LED in the Spectral Time device is now visible and flashes when Retrigger mode has Sync enabled.
- Wavetable: When the transport is stopped, any hanging notes in the Wavetable device will now be stopped, as in other Live instruments.

**Session View**

- Making a selection (or multi-selection) using keyboard navigation in the Session View's scene area now works as expected.
- It is now possible to navigate to and rename the next/previous track using the "Tab"/"Shift"+"Tab" keys while renaming multiple selected tracks in the Session View. Previously, this only worked in the Arrangement View.
- When resizing the Session View, the clip slot selection will stay in view as much as possible. When the selection is off-screen, resizing the Session View does not scroll to show it.
- Pressing "Shift"+"Tab" now selects the previous clip while renaming a Session clip.
- When renaming a Session clip, the "Tab"/"Shift"+"Tab" keys now skips empty clips slots.
- When reaching the end when navigating with the "Tab"/"Shift"+"Tab" or Arrow Up/Down keys while renaming tracks or clips in the Session or Arrangement View, the navigation now cycles to the beginning or end of the tracks or clips, similar to using "Tab"/"Shift"+"Tab" when renaming scenes.

### Bugfixes

**Arrangement View**

- Previously, reactivating a take lane selection when Draw Mode was enabled would create a flickering effect.
- Previously, the automation control chooser is empty instead of showing "None" when loading a new Set and "Show Automated Parameters Only" is chosen. Also, clicking on the automation control chooser would not select the main automation lane header when "Show Automated Parameters Only" is chosen. These bugs have been fixed.
- Previously, trying to resize multiple selected tracks via the resize handle of the last automation lane would resize the main automation lane instead.
- Previously, certain elements (such as insert markers, the loop brace and fade handles) were drawn on top of the Single Track Back to Arrangement button.
- Previously, the triangle icon in the Single Track Back to Arrangement button was cropped when the track was almost scrolled almost out of the visible Arrangement View. Now the triangle icon is only shown when it can be fully displayed.
- Recording auto-quantization now applies to take lane clips as well as main lane clips.
- Previously, the Arrangement View would abruptly scroll upwards after renaming a clip in a take lane at the bottom of the view. Instead, the clip's take lane is now scrolled into view. Similarly, the clip's main lane is now scrolled into view when renaming a main lane clip, whereas before, the entire track (including take lanes and automation lanes) was scrolled into view.

**Clip View**

- In the Sample tab, typing arbitrary values into the Pitch control's Transposition/Cents field now works as expected. Dragging the Transposition/Cents slider beyond the minimum/maximum pitch also now works as expected.

**Control Surfaces**

- Mapping the Macro Variations selector to relative MIDI controllers now works as expected. A controller that sends high-resolution pitch bend can now be mapped to the scene selector and the snapshot selector.
- The LEDs surrounding the encoders on the Novation Remote SL MkII once again provide feedback about the value of the controlled parameter.

**Devices**

- Some Racks that only contain licensed Max for Live devices and were previously locked in certain editions of Live (such as the DS Drum Rack in Live Standard) are no longer locked.
- Plug-in window titles now update when changing the name of the containing track. AU plug-in devices are now displayed as disabled if plug-in creation fails.
- In order to prevent an issue with filter cutoff being reset on every note start in the TAL J-8 plug-in, the VST3 version of the plug-in is no longer loaded in MPE Mode by default. The VST2 version of the plug-in will still load in MPE Mode by default.
- Arpeggiator: Fixed a bug that could cause a crash when repeatedly adding and removing notes from a held chord when using the Arpeggiator device with the Hold parameter active.
- Collision: Fixed a regression that resulted in missing parameters in the Collision device.
- Hybrid Reverb: Previously, Live would crash when loading a one-sample length file into the Hybrid Reverb device and adjusting the Size parameter.
- Sampler: Previously, cropping a sample in the Sampler device would chop off the portion of the sample between the Release Loop Start and the Loop Start, if the Release Loop Mode was set to "Loop Back and Forth" and the Release Loop Start was before the Sample Start point.
- Tension: The Filter LFO dropdown menu in the Tension device now appears as expected.

**Interface Improvements**

- Fixed an incorrect error message that appeared when trying to insert a non-audio device into an Audio Effect Rack.
- Corrected the Edit menu entry text for undoing a clip color change.
- Fixed a crash that could occur when undoing in a Set that had previously been restored after another crash.
- Previously, Live's crash recovery would silently fail if the undo history contained an empty band file (e.g. after a power outage).
- Under certain circumstances on macOS, audio/MIDI meters, the global transport time and other parameters would stop updating while editing parts of a Live Set with the mouse or a trackpad.
- Previously, when clicking on a half-hidden track header to select it, Live might sometimes copy or move the track.
- Fixed a crash that occurred when freezing a track in a Live Set that contained an external MIDI instrument that was routing MIDI to a device in the Master track.
- Previously, renaming did not work as expected when selecting a track header or take lane header and unselecting the cursor item using "CMD"+click (Mac) / "CTRL"+click (Win).
- Fixed crashes and error messages pertaining to corrupt documents that occurred when loading some Live Sets.
- Fixed crashes that occurred after deleting a device while a take lane clip has an envelope for that device.
- Fixed a crash that occurred when renaming a take lane inside of a linked track and then pressing Tab.
- Fixed document corruption and subsequent possible crashes or other issues when restoring a Set after a crash under certain circumstances.
- Fixed the alignment of shortcut entries in Live’s context menus on macOS.

**Link**

- Fixed a bug where Live would not accept tempo changes from Link peers in some cases.

**Max for Live**

- Zooming Arrangement tracks via the Max for Live Application.View.zoom_view API function no longer breaks when multiple automation or take lanes are visible.

**MIDI Editing**

- Pitch Bend, Sustain, Expression, Mod Wheel, and other MIDI controllers that one would expect to reset to a default value will now do so at the beginning of clips that do not specify them. (Note: for users who intentionally use the previous behavior, this change will make their Live Sets behave differently. Therefore, the behavior is disabled by default. The behavior can be enabled by checking the "MIDI Envelope Auto-Reset" entry in the Options menu.)
- Improved Live's performance when a very large amount of notes are visible in the Velocity or Chance Editor.
- Previously, when changing note velocities or probabilities with the Arrow Up/Down keys, Live would not show the changed value when the mouse was hovering over the respective editor.
- Previously, the MIDI Editor pitch grid might jump by one pixel when folded on tracks with a Drum Rack while Highlight Scales was disabled.
- Fixed a bug that caused MIDI notes in a selected area to get deleted even if the notes themselves were not selected when pressing Delete.

**MPE Editing**

- Fixed a bug where selecting or deselecting MIDI notes showed unexpected behavior or was not possible when the Note Expression tab was open and the MIDI Note Editor had Fold enabled.
- Fixed a bug where the per-note breakpoint editor would not be focused when clicking on an expression curve in the Pressure or Slide lanes, when the Note Expression tab was visible.
- Fixed a bug that could cause a crash when using MPE data with MIDI Effect Racks.
- When the Note Expression tab is open and no note is selected, double-clicking on the Note Ruler now correctly zooms to all notes including their pitch-bend curves.
- Fixed an issue where a note could have per-note events behind the note end when recording a transposed MIDI clip into the Arrangement.
- In the unlikely event that an extremely high amount of MPE control change messages come in, Live will no longer crash, and all notes will be stopped.
- Previously, when the Note Expression tab was open, moving the mouse from an unselected expression curve to a selected expression curve could cause the highlight to become stuck.
- The Insert Time and Delete Time commands are no longer available when editing per-note expression breakpoints. Fixed a bug that could cause per-note expression to play incorrectly after a note-editing action resulted in an existing note becoming shortened.
- Fixed an issue where undoing a per-note breakpoint editor change while the breakpoint editor was not open would not redraw the expression curves.
- The Duplicate Time command is no longer available when editing per-note expression breakpoints. Fixed a bug where the Duplicate command would truncate the original note when duplicating the selected note while working in the per-note expression breakpoint editor.

**Plug-ins**

- Fixed a crash that occurred when opening a Live Set that contained a plug-in with sidechain automation/modulation that could not be loaded.

**Push**

- On Push 2, the Spectral Resonator device's main bank parameter now correctly switches to Transpose when the sidechain mode is set to MIDI.
- Fixed a crash that occurred when clicking on a parameter in Live and adjusting the same parameter using an encoder on Push at the same time.

**Session View**

- Fixed a bug where mappings in MIDI/Key Map Mode were hidden by the scene number.
- Navigating with the Tab key once again works as expected when renaming scenes.
- Fixed a bug where Follow Actions were not scheduled as expected, under certain circumstances.
- Fixed a crash that occurred when pressing the [Space] or [Tab] key after clicking on Track Status Display in Session View if a clip in Arrangement View was being played.

**Setup**

- Previously, exporting audio might start single-threaded rendering before switching to multi-threaded rendering after a while. This could impact render performance significantly for Live Sets that benefit from multi-threaded rendering.
- Improved shared Library folder setup when installing Live in multi-user environments.
- The Library.cfg file in a shared Preferences folder now gets copied as expected when installing Live in a multi-user environment.
- Fixed a crash that occurred in certain scenarios if two instances of Live were running at the same time.

## 11.0.6

### Bugfixes

- Fixed an issue where the Session frame of the ATOM control surface script was visible even when the hardware was not connected.

## 11.0.5

### New features and improvements

**Arrangement View**

- Using "CMD"-click (Mac) / "CTRL"-click (Win) no longer deselects track headers that contain a hidden lane selection.
- Take lane headers with a standby selection are now shown in the respective standby selection color when more than one track, take lane, and/or automation lane is selected.
- It is now possible to rename multiple selected tracks simultaneously.

**Clip View**

- The Sample tab's Clip Gain control has been changed back to a vertical slider, and it has been repositioned above the Transpose controls.
- The Sample tab's Reverse button now shows an icon instead of text.
- The Sample tab's Reverse and Edit buttons are now positioned next to each other.
- Added a Pitch dial to the Sample tab, which enables shifting an audio clip's pitch in semitones. The Transpose controls now appear as adjacent slider controls, positioned beneath the Pitch control.
- When multiple audio clips with different Clip Gain values are selected, the value range is shown with split triangle handles on the Clip Gain slider.
- Added some visual refinements to the Clip View tabs.
- Improved the names of MIDI controllers that appear in the Control chooser when the Clip View's Envelopes tab is visible and the "MIDI Ctrl" is selected in the Device chooser.

**Follow Actions**

- The Follow Action Chance slider now displays a split triangle instead of just a black bar when it is showing multiple different values.

**Interface**

- Updated various Help View lessons.
- Updated various Help View lesson translations in German, Spanish, French, Italian, Japanese and Chinese languages.
- Updated some Japanese and Chinese info text translations.
- The audio engine can now be turned on or off via a new "Audio Engine On" entry in the Options menu, or using the "CMD"+"ALT"+"Shift"+"E" (Mac) / "CTRL"+"ALT"+"Shift"+"E" (Win) keyboard shortcut.
- The Overload Indicator is disabled by default for new Live 11 installations.
- Live's performance is improved when deselecting many clips at once.

**Max for Live**

- Updated the bundled Max build to version 8.1.11. For the changelog, visit: http://cycling74.s3.amazonaws.com/support/version_8_1_11.html
- The following new properties and functions are available in the Clip API: add_warp_marker move_warp_marker delete_warp_marker sample_rate sample_length
- The Max for Live API now supports large dicts.

**MIDI Editing**

- It is now possible to resize the velocity, probability, and per-note expression lanes in the MIDI Editor using the mousewheel/pinch gesture while holding "ALT".
- The background color of lane headers is now consistent with the Notes tab.
- Clicking on a lane with a standby selection now selects that lane instead of collapsing the time selection.

**MPE Editing**

- The "Pitch Bend Range Settings..." context menu entry now appears when right-clicking in the area where per-note pitch-bend is editable.
- When the Expression tab is open, making a time selection in the Note Editor or the Slide/Pressure expression lane while editing per-note expression now only shows the focused lane with a selection highlight, while all other lanes are shown with a standby selection highlight.
- When the Expression tab is open, using the "Zoom to Clip Selection" command (or "Z" key shortcut) now adjusts the zoom level according to pitch bend values contained in the time selection.
- It is now possible to clear all per-note Pitch, Slide and Pressure expression envelopes of a note at once by using the "Clear All Envelopes" entry in the context menu of the per-note expression breakpoint editor.

**Multi-Clip Editing**

- When clips are selected/unselected in the Session View, the highlighted track and scene now point to the foreground clip, if any exists.
- Changing the foreground clip from the Clip View updates the highlighting of the track (in both the Session View and Arrangement View) and the scene corresponding to the new foreground clip.
- Clicking on a clip's multi-clip loop bar in the Clip View updates the highlighted track, even if this clip is already the foreground clip.

**New Devices and Device Improvements**

- The enabled/disabled state of a plug-in device's MPE Mode is now saved with that device's default configuration.
- Plug-in devices now look similar to built-in Ableton devices when disabled.
- Chorus-Ensemble: The Chorus-Ensemble device now uses less CPU when certain settings are applied.
- Phaser-Flanger: In the Phaser-Flanger device, when the LFO Stereo Mode is set to Spin and the Spin value is changed, a second LFO line is now visible and its frequency changes accordingly.
- Spectral Resonator: The Spectral Resonator device now uses about 15% less CPU. The Spectral Resonator device now uses about 20% less CPU when very few partials are audible. The spectrogram should now display about 30% of its former CPU load. Note: this is only visible in the system's CPU monitor, not in Live's audio processing meter. When low polyphony and unison voices are set, less CPU usage should be shown.
- Spectral Time: The background of the Stereo slider now displays a blue color when its value is above 0%. "Freeze On/Off" is now called "Frozen On/Off" in Automation Mode and on Push. "Delay DryWet" is now called "Delay Mix" in Automation Mode, and "Mix" in the device UI and on Push. In the Spectral Time device, the spectrogram should now display about 30% of its former CPU load. Note: this is only visible in the system's CPU monitor, not in Live's audio processing meter. The Spectral Time device now runs at about 60% of its previous CPU load.
- Wavetable: Added support for Drum Rack choke groups to the Wavetable device.

**Push**

- When editing multiple MIDI clips at once, a connected Push device now follows all highlight changes of tracks/scenes, and the focus on the corresponding track.
- Updated the notification style for scenes, and updated the scene name visualization to include the absolute position, tempo and time signature on Push.
- Adjusting multiple encoders while recording automation now creates less undo steps on Push 1 and 2.

**Session View**

- When a Session track slot is highlighted but not selected, using the Arrow Up/Down keys, Home/End, or PageUp/PageDown keys now moves the highlight to the adjacent track slot in the given direction.
- It is now possible to rename multiple selected scenes simultaneously.
- It is now possible to rename multiple selected tracks simultaneously.
- In the Session View's Track Status display, the remaining play time of an unlooped clip now always displays the seconds with two digits (e.g., "10:07" instead of "10:7").

**Control Surfaces**

- Added control surface support for the Roland Fantom.
- Added control surface support for the M-Audio Hammer 88 Pro, Oxygen Pro Mini and Oxygen MKV Series.
- The functionality of the Oxygen Pro control surface script has been drastically changed. Specifically: The Rewind and Fastforward buttons will now rewind and fastforward the Arrangement position. Turning the Encoder will now scroll the Session frame up and down. Holding the Encoder down and turning it will scroll the selected Scene up and down. The Knobs can now control multiple features (Device parameters, Track Panning, Track Sends and, in the case of the 25 key, Track Volume) that can be selected by holding down Shift and pressing the Pads used for DAW KNOB CONTROL.  Additionally, it is possible to toggle between controlling Send A and Send B by holding down Shift and pressing the SENDS Pad. Live's Takeover feature is now enforced for the Knobs and Faders when switching between DAW and Preset Modes. The Pads now provide LED feedback in respect to Clip/Clip Slot states in Live. The Buttons beneath the Faders can now control multiple features (Track Arming, Track Muting, Track Soloing and Track Selection) that can be toggled between via the Mode button. Fixed an issue where the Session frame was visible even when the hardware was not connected.

### Bugfixes

**Arrangement View**

- Fixed an issue where Live hangs when zooming in Arrangement View in some cases.
- Previously, reordering automation lanes via dragging and dropping or using the "CMD" and Arrow Up/Down (Mac) / "CTRL" and Arrow Up/Down (Win) keys would not mark the document as modified.
- Fixed the width of the divider line between Arrangement lanes and track/lane headers.
- Previously, after selecting content by clicking on the Arrangement loop brace or pressing "CMD"+"A" (Mac) / "CTRL"+"A" (Win), content of tracks nested in a folded Group Track would not be selected when unfolding the containing Group Track.
- Previously, track lanes and headers could not be deselected via "CMD"+click (Mac) / "CTRL"+click (Win) when their tracks contained hidden and selected automation lanes, take lanes, and/or Group Tracks.
- Fixed a crash that could occur when restoring the Arrangement View's zoom state using the "Z" keyboard shortcut after deleting a take lane.
- Fixed a crash that could occur when clicking in a track's main lane after track content had been selected during recording, under certain circumstances.
- Previously, mixer controls in linked tracks would still be linked when selecting a take lane, after multiple track headers had previously been selected.
- Arrangement clip headers no longer have an uneven appearance.
- Previously, an Arrangement clip header would not be displayed as having a standby selection when the focus was moved away.
- Previously, it was not possible to unlink all tracks when some tracks were nested inside a Group Track.
- Fixed a crash that occurred when inserting a take lane.
- Fixed a crash that could occur when trying to move a selected main automation lane by pressing the "CMD" and Arrow Up/Down (Mac) / "CTRL" and Arrow Up/Down (Win) keys.

**Control Surfaces**

- User Remote Scripts work as expected on Windows again.

**Devices**

- The EQ Eight device will now scale the displayed spectrum the same way as the Channel EQ and Hybrid Reverb devices.
- Previously, the Operator device could crash or calculate inaccurate frequencies when its Fixed Mode and Spread parameters were enabled.
- In the Spectral Resonator and Spectral Time devices, the limiter's LED now correctly lights up when the limiter is active.
- Switching between oscillator effects in the Wavetable device now changes labels within each matrix as expected.
- In the Sampler, Simpler, and Wavetable devices, the MPE label text now updates according to the device's selected/deselected state.
- Previously in the Spectral Resonator and Spectral Time devices, gaps would sometimes appear in the Spectrogram at high frequencies.
- A Max for Live device's background color now updates correctly after moving that device between tracks.
- Fixed two bugs in the MPE Control device: The Pressure curve would not follow Live's themes when the device was instantiated while using the Dark theme. Global PB would be interpreted as Note PB under certain circumstances.
- The Surge Synth Team's "Surge" VST/AU plug-in device now has its internal MPE Mode activated by default when started in Live. Deactivating the device's MPE Mode in Live will also cause Surge to deactivate MPE Mode internally.

**Interface Improvements**

- Mouse-clicks on a return track no longer "fall through" to audio/MIDI tracks or Group Tracks that are covered by that return track.
- When left-clicking the CPU meter, the drop-down menu that appears is now aligned at the left-hand of the CPU meter.
- The Launch Macro Variation button can be mapped as expected again.
- Fixed a crash that could occur when dragging an empty frozen MIDI clip to an audio track.
- Fixed a crash that could occur when freezing a track after recording, under certain circumstances.
- Fixed the alignment of the Launch text label that appears in the expanded view of the Clip View's Clip box.
- Previously, when copying a folder with audio files to another folder which was already in Places, the files would not appear in the browser.
- Previously, when saving a Live Set file (such as a clip or preset) in the root folder of the temporary current Project, that file would not be copied over to the final destination Project.
- Fixed the spelling of the "Sostenuto" parameter that appears in the Control chooser when the Clip View's Envelopes tab is visible and the "MIDI Ctrl" is selected in the Device chooser.
- Previously, resizing the Device View, as a result of switching to the Arrangement View, while no clip was selected would result in automation lanes having the wrong height when switching back to the Session View.
- Previously, using Tempo Follower and Tap Tempo at the same time could create a conflict with Live's tempo. To prevent this, Tempo Follower is now disabled as long as Tap Tempo is active.
- Previously, the waveform of an audio clip in the Detail View would be displayed in a dimmed color, although that clip was not audible while Audition Mode was enabled.
- Using pinch gestures to zoom once again works in expression lanes.
- Previously, the vertical zoom level and scroll position in the MIDI Note Editor were sometimes wrong when switching from the Expression tab to the Notes tab.
- Added the following changes for Windows: On Windows 10, Live requires version 1803 or higher to be used on HiDPI screens. Live's second window is no longer shown separately in the list of windows that appears when pressing "Alt"+"Tab". It also cannot be minimized anymore. These changes highlight that the second window is not a stand-alone window, but secondary to the main window. When switching virtual desktops, floating windows are no longer shown on the new virtual desktop. When using virtual desktops, floating windows (e.g., the Max editor, plug-in devices, or Live's Preferences) are now only shown on the virtual desktop where Live is. Fixed a bug that enabled performing certain actions (e.g., stopping playback) while a modal dialog was shown.
- Previously, the selection on an auditioned take lane would look different when Draw Mode was active.
- Previously, adding a device via double-clicking could create two undo steps.
- Fixed a performance regression when loading a Live Set with many devices.
- Previously, when exporting a video, the Export Audio/Video dialog would remain disabled when choosing an export file name that matched an existing video file (but not an existing audio file) and then choosing not to overwrite the existing file.
- Fixed an issue where a Rack's selector buttons for chains and devices would swap places, under certain circumstances. Fixed various minor UI alignment and sizing issues that affected other elements within Racks.
- Fixed a spacing issue in Drum Racks. In all Racks, the Rand and Map buttons now always align with the right border of the Macro Controls section, and they appear as "R" and "M" when six or less Macro Controls are shown.
- For MIDI clips, program change controls now appear in the order [Bank][Sub][Pgm] instead of [Pgm][Bank][Sub].
- Fixed a crash when scrolling in the Clip View's Sample/Note Editor with the mouse button held down.
- Fixed a bug that generated false disk overload indications, even when no sample dropouts occurred.
- Previously, Link would not become disabled when opening a new Set.
- Fixed a crash when unfolding a nested Group Track containing a selected clip.
- The Pitch control in the Clip View's Sample tab once again works as expected when multiple clips are selected.
- The Clip Activator button once again works as expected.
- Previously, after selecting a Group Track header, the track highlight would sometimes immediately jump to a track within that Group Track.

**Max for Live**

- Sending a getpath message to a live.object that operates upon the GroovePool no longer causes an error.
- Sending a getpath message to a live.object that operates upon a Groove no longer causes an error.
- GroovePool, Groove and DeviceIO now all have a canonical_parent property.
- Replacing a licensed Max for Live device with an unlicensed one no longer creates a "fake" device that informs the user of a missing license. Also, it is no longer possible to inadvertently trigger Temporary Demo Mode when attempting to perform another action that breaches any current limitations, in cases where a "fake" device was created.
- The LOM ID of a routable MIDI input/output is now retained after moving and saving the containing Max for Live device.

**MIDI Editing**

- Upon setting Scale Name and Root Note values for a MIDI clip, those values remain visible (but grayed out), even when Scale Mode is disabled.
- When enabled, the Scale (aka Fold to Scale) button becomes disabled (instead of grayed out) whenever folding to scale is not possible.
- Previously, when using the Arrow Up/Down keys in the Velocity or Chance Editor while no notes were selected, a false value was temporarily shown in the respective editor's lane header.
- When multiple MIDI clips are selected and the Envelopes and Expression tabs are not displayed, the Notes tab is now left-aligned.

**MPE Editing**

- Previously, per-note pitch bend editing was unavailable when a MIDI Effect Rack or Instrument Rack was used, under certain circumstances.
- Previously, when the Expression tab was visible, making a rectangular selection of a single note in the MIDI Note Editor would incorrectly set the focus to pitch bend expression editing.
- Fixed a bug that caused a note's per-note pitch bend range to get reset to +/- 48 semitones when copying and pasting a track.
- Fixed a bug that could cause notes to be affected by expression parameters (including pitch bend) from previous notes.
- Previously, when the Expression tab was open and the MIDI Note Editor was folded, zooming to selected notes would sometimes scroll out of view.

**Push**

- Changes to a scale or root note on Push while recording a MIDI clip are now applied to that newly-recorded clip.

**Session View**

- When using a device parameter's "Show Automation" or "Show Modulation" context menu command while a Session clip is playing, Live now switches to the Envelopes tab in the Clip View when no clip is selected.
- Shift-clicking on an empty track slot in the Session View no longer changes the scene and track highlighting.
- Previously, the Follow Action Time marker was sometimes displayed at the wrong position in unwarped clips.
- Improved the text contrast in the Session View's Track Status display for unlooped clips.
- Previously, when triggering a scene with assigned Follow Actions after stopping Live's transport, that scene's tempo was not respected.
- The "Stop" Follow Action now works as expected for scenes.
- Setting the scene tempo or time signature from the Python API (Max and Push) will enable the respective scene control and display the correct value being set.

## 11.0.2

### Bugfixes

- Fixed some licensing issues.

## 11.0.1

### Bugfixes

- Live loads the demo song when Live 11 is started for the first time on a given computer.
- The Live manual has been updated.

## 11.0

Please check the Live 11 Technical FAQ for detailed information on specific topics:

https://help.ableton.com/hc/en-us/articles/360019140859

- Arrangement View Improvements Names of recorded clips in the Arrangement are now simplified and more consistent. The name consists of the track name (without the leading index number), and an index of the take number. Upon creating a MIDI clip in the Arrangement View, the grid will start at a fixed sixteenth-note setting, as opposed to narrow-adaptive. Newly-recorded MIDI clips in the Arrangement will default to a sixteenth-note grid setting. A new "Create Crossfades On Clip Edges" command creates four-millisecond crossfades on clip edges, when either a single or multiple adjacent whole clips are selected, or when a time selection contains more than two adjacent clips. The "Create Crossfades On Clip Edges" command is available in the Create menu, and the context menu of Arrangement clips, or via the "CMD"+"ALT"+"F" (Mac) / "CTRL"+"ALT"+"F" (Win) keyboard shortcut. It is possible to change the selection of automation and take lane headers using the keyboard's Arrow Up/Down keys. The lane header selection can also be extended with using the "Shift" and Arrow Up/Down keys. It is possible to move automation lanes and take lanes using the "CMD" and Arrow Up/Down (Mac) / "CTRL" and Arrow Up/Down (Win) keyboard shortcut. Selected automation lanes or take lanes can be resized vertically by pressing "ALT" and "+" or "ALT" and "-", or by pressing "ALT" while using the mousewheel/pinch gesture. Also, when a track's main lane is selected, only that lane's height is affected. Multiple selected automation lanes or take lanes can be resized by dragging the resize handles with the mouse. When holding the "ALT" modifier, all selected automation lanes or take lanes are resized simultaneously, similar to tracks. A previous lane header selection is preserved after folding and immediately unfolding tracks again or when toggling Automation Mode. When using the Zoom to Time Selection command in the Arrangement, Live now only zooms horizontally at first. When using the command a second time (without changing the time selection), Live then zooms vertically as well. Upon using the command a third time, the Arrangement returns to the first vertical zoom state.
- Automation Updated background and text colors for lane headers and clip backgrounds in Automation Mode. Automation lane headers are now selectable with the mouse. Clicking on an automation lane header now highlights that lane. It is now possible to clear envelopes in automation lanes with selected lane headers, by using the "CMD"+"Backspace" (Mac) / "CTRL"+"Backspace" (Win) keyboard shortcut. Clicking on a selected lane's Remove Automation Lane ("-") button now removes all selected automation lanes. Clicking on an unselected lane's Remove Automation Lane button removes only that lane.
- Browser Improvements A "Templates" label has been added to the Categories section of the browser. It shows template Live Sets from factory packs (including the Core Library), the User Library, and other Project folders. The current Live Set can be saved as a Template Live Set via the File menu's "Save Live Set As Template..." command. The current Live Set can be saved as the default Live Set (which is used when creating new Live Sets) via the File menu's "Save Live Set As Default Set..." command. Any Live Set in Live's browser can be set as the default Live Set (which is used when creating Live Sets) via the "Set Default Live Set" context menu entry. A "Grooves" label has been added to the Categories section of the browser. It shows a flat list, similar to that within the Clips and Samples labels, of all Grooves from the Core Library as well as the User Library. Devices in the Audio Effects label are now grouped into folders. As with other folders in the browser, it is possible to unfold more than one folder at once, by holding "Cmd" (Mac) / "Ctrl" (Win). Ableton’s official Max for Live devices are now listed within the "Audio Effects", "MIDI Effects", and "Instruments" labels. The nodes can be expanded to reveal presets (.adv files) organized in virtual folders, if any exist. Presets outside of matching virtual folders are shown below the last virtual folder. Drum Synth devices are now grouped in their own folder within the Instruments label. The browser now receives the focus when opened via the "Cmd"+"Alt"+"B" (Mac) / "Ctrl"+"Alt"+"B" (Win) keyboard shortcut.
- Capture MIDI Added MPE support to Capture MIDI.
- Clip/Detail View Improvements Removed the Clip View Box selectors from the Clip View. The Clip box now contains controls available for both audio and MIDI clips, such as Start/End, Loop Position/Length, Clip Time Signature and Clip Groove. Clicking the triangular toggle button in the Clip View's title bar shows or hides controls previously found in the Launch box, including Launch Mode, Clip Quantization, and Follow Actions. Controls for editing samples/notes, envelopes, and note expression (for MIDI clips only) are now available in dedicated tabs to the right of the Clip box. Pressing "Alt"+"1" switches to the Sample/Notes tab, pressing "Alt"+"2" switches to the Envelopes tab, and, when a MIDI clip is selected, pressing "Alt"+"3" switches to the Note Expression tab. The Clip Gain slider has been moved below the Transpose controls, and is now a text slider control. The Transpose control now has a dial control for transposing in semitones, and a text slider control for fine-tune in cents (previously named "Detune"). Removed the Clip Color chooser from the Clip box. It is now possible to rename or change the color of a selected clip via the Clip box's context menu. It is now possible to minimize/maximize the Clip box by double-clicking its title bar. "Clip Volume" is now called "Clip Gain" in the Envelope tab's Device/Control choosers, and in the undo history.
- Comping Introduced comping in the Arrangement View. Comping makes it possible to pick the best moments of each recorded performance, and combine them into a composite track. You can record multiple takes of a musical performance without stopping recording. Live will then create and organize individual takes from this recorded material, allowing you to piece your favorite parts together. You can also drag samples from your library and use comping as a creative sample-chopping tool. In the Arrangement View, take lanes are automatically added to armed audio and MIDI tracks during recording. Take lanes can also be inserted manually via the "Insert Take Lane" entry in the Create menu or a track header's context menu, or using the "Shift"+"ALT"+"T" keyboard shortcut. When adding a take lane via the Create menu, the take lane will be inserted after the selected lane. Otherwise, if a track is selected, the take lane will be inserted after the track's main lane. Inserting take lanes also works on multiple selected tracks simultaneously. Take lanes are hidden by default. The visibility of take lanes can be toggled from a track header's "Show Take Lanes" context menu entry, or with a keyboard shortcut "CMD"+"ALT"+"U" (Mac) / "CTRL"+"ALT"+"U" (Win). Take lanes are only visible when Automation Mode is disabled. Recording in the Arrangement View automatically creates a clip in a take lane. Take lane clips can be edited like other Arrangement clips (e.g., they can be moved, copied/pasted, dragged & dropped, consolidated, cropped, etc.) They can also be copied to Session View clip slots by either copying and pasting or dragging and dropping. Samples and MIDI files can be dragged to take lanes from the browser or Finder/File Explorer. When multiple samples are selected, pressing the "CMD" (Mac) / "CTRL" (Win) modifier key and dragging will insert each sample into sequential tracks and/or take lanes. Selected material in take lanes can be placed in the track's main lane by pressing the "ENTER" key or via a take lane's "Copy Selection to Main Lane" context menu entry. It is possible to replace clips in a track's main lane with the next/previous take lane clip, by selecting a clip or by making a time selection, and then pressing "CMD" and Arrow Up/Down (Mac) / "CTRL" and Arrow Up/Down (Win). If the time selection is on a take lane, it switches to the next/previous take lane clip. This also works when there is a selection of clips or time across multiple tracks, and when take lanes are hidden. (Note: empty take lanes are ignored.) In Draw Mode, selected take lane material can be placed in the track's main lane in one single gesture by clicking, dragging and then releasing the mouse. It is also possible to quickly cycle between takes within a time selection by single-clicking on a take lane and immediately releasing the mouse. A take lane can be auditioned by clicking the "Audition Take Lane" button (displayed as a speaker icon) in the take lane’s header, or using the "T" keyboard shortcut. When enabled, clips in the auditioned take lane will become audible and displayed in their full color, and all other lanes will be muted. Pressing "T" toggles Audition Mode on take lanes that contain a time selection (or an insert marker) or if that take lane’s header is selected. Take lanes from different tracks can be auditioned at the same time, however only one take lane per track can be auditioned. If the time selection or lane header selection stretches across multiple lanes on the same track, the last selected lane will be auditioned. For every Arrangement clip, Live will highlight its source material in a take lane by displaying it in full color, while dimming all unused take lane material. This makes it easier to track the recorded material that the clip originally came from. Source highlights will only be shown as long as the positions and the clip properties are matching. Highlighted regions on take lanes can be resized to adjust the split point between two adjacent parts of a comp by dragging the edge of the highlight. When the Clip Color toggle is set to Random in the Look/Feel Preferences, each take will be assigned a random color. Take lane headers are selectable with the mouse. Clicking on a take lane header highlights that lane. Take lanes can be deleted via the Delete/Backspace key when their headers are selected. Take lanes can be renamed in the same way as tracks, via the "Rename" command in the Edit menu or the take lane header context menu, or using the "CMD"+"R" (Mac) / "CTRL"+"R" (Win) keyboard shortcut. Multiple selected take lanes can also be renamed simultaneously. Using the "Tab" or "Shift"+"Tab" keyboard shortcuts allows moving between lanes and tracks while renaming them. Selected take lanes can be reordered within their track via dragging and dropping. Take lanes can be selected and renamed during recording. Take lane headers have a default info text. The info text of take lane headers can be edited using the Edit Info Text command from the context menu or the Edit menu.
- Control Surfaces The "MPK mini" control surface script is no longer available. The specific AKAI MPK mini model control surface script should now be used instead. Control surface scripts that can control multiple banks of device parameters can now control the second set of eight Macro Controls (i.e., Macro 9-16) in Racks.
- Follow Actions Follow Actions controls can now be shown or hidden via the triangular toggle button in the title bar of the Clip View. Follow Actions can now be assigned to scenes via the new Scene View. Clip Follow Actions will continue to run when a scene Follow Action is created or scheduled, however scene Follow Actions take precedence when triggered. Follow Actions can be activated or deactivated using the selected clip/scene's "Follow Action" button. This button is disabled by default, and can be toggled using the "Shift"+"Enter" keyboard shortcut. When enabling Follow Actions in a new clip/scene, Follow Action A is now set to "Next" by default. An "Enable Follow Actions Globally" button has been added next to the Back to Arrangement button in the Session View. When disabled, no Follow Actions will occur in the Live Set, which allows editing running clips while preventing playback from jumping to other clips. When a Live Set does not contain any clip or scene Follow Actions, the "Enable Follow Actions Globally" button will appear grayed out. A Session clip/scene with assigned Follow Actions is now indicated by a modified play button in its clip/scene slot. Follow Action Chance A and Chance B values are now represented as percentages that sum to 100%. These values can be modified using a new slider control. Added a marker to the Sample/MIDI Notes Editor that visualizes the Follow Action Time of a clip. This marker also allows dragging the clip's Follow Action Time. When Follow Actions are disabled via the "Enable Follow Actions Globally" button in the Master track, the Follow Action marker in the Detail View now appears in gray and black instead of green. Added a new "Jump" Follow Action to clips and scenes. When Jump is selected, a new Jump Target slider becomes visible, to allow selecting a target clip slot/scene for the Follow Action to jump to. Added a "Follow Action Linked" switch to the Follow Actions pane for clips. This switch is set to "Linked" by default. When the switch is set to "Linked", the Follow Action is triggered at the end of the clip or after the number of loops set in the "Follow Action Multiplier" field, and the Follow Action Time marker but cannot be moved. When the switch is set to "Unlinked", the Follow Action is triggered after the clip has played for the duration of the Follow Action Time. Added a "Create Follow Action Chain" command to the context menu of Session clips, making it possible to set up Follow Actions so that all selected clips play in a loop. The clip selection does not have to be contiguous.
- Interface Improvements Updated Live's splash screen, application icon, and "About Live" box. The CPU meter in the Control Bar can now display the peak CPU level. Peak CPU is a more reliable measure of CPU usage for the purpose of detecting dropouts. The percentage shown on the meter (indicating either the average or peak CPU level) can be selected from the CPU meter dropdown menu. The Overload indicator (previously named the "Disk Overload" indicator) in the Control Bar has been redesigned, and will light up if a CPU overload has occurred. (Note: CPU overloads usually produce audio dropouts.) CPU overload notifications can now be disabled in the Control Bar via a "CPU Overload Indication" entry in the CPU meter's dropdown menu, and in the Overload indicator's context menu. Clicking on the new "Show/Hide CPU Meter Section" selector in the Session View's Mixer Section will open a per-track CPU metering section. Each track shows a CPU meter with six rectangles that light up to indicate the relative impact of that track on the CPU level of the current Set. Freezing or removing devices from the track with the largest impact will usually reduce the CPU load. In the Look/Feel Preferences, the "Colors" section has been renamed "Customization". Live’s Themes have been redesigned to provide much greater contrast. Added a "Reduced Automatic Colors" toggle to the Look/Feel Preferences, which uses a reduced color palette when assigning colors to clips and tracks. This palette makes clips and tracks easier to tell apart with a deuteranopia, protanopia or tritanopia color vision deficiency. Added a "Grid Line Intensity" slider to the Look/Feel Preferences, allowing for more pronounced or dimmed appearance of grid lines in the Arrangement and Detail Views. On Windows, the progress of dialogs (such as the Export Audio dialog) is now displayed in the taskbar. Progress dialogs now show their progress value below the bar, for easier reading in all Themes. The scrollbar in the Help View now matches the colors of the scrollbar in the browser and the Groove Pool. The vertical zoom level on the piano roll is now increased when dragging horizontally on the Note Ruler. Added an "Arm Track" command to the Edit menu. If multiple tracks are selected, the command appears as "Arm Tracks". If the selected track is armed, the command is replaced with "Disarm Track". It is now possible to arm selected tracks using the "C" shortcut key. Changed the font color of the "Drop Instrument Here" text in the Device View for improved contrast. Reorganized the Edit menu for improved usability and accessibility, and added a new "Solo/Unsolo Track" entry. Key/MIDI-mapped functionality for the "Set Start/End", "Set Loop Position/Length", and "Nudge Backward/Forward" buttons is now disabled whenever the corresponding controls in the GUI are disabled. The "Browse Groove Library" context menu entry has been removed from the Groove Pool. The Groove Pool now opens automatically when: loading a groove file from the browser by double-clicking or pressing the Enter key adding a groove to the Groove Pool (e.g., by dragging and dropping it onto an existing MIDI clip) extracting grooves
- Linked-Track Editing Introduced linked-track editing in the Arrangement View. Linked-track editing makes it possible to use comping workflows and other phase-locked editing operations on multiple tracks at once. Any tracks in the Arrangement View can now be linked so that their content can be edited simultaneously. There can be multiple instances of linked tracks in a Set, however each track can only belong to one of these instances. Linked tracks are indicated by a "link" icon button in their headers. Clicking on a track's link icon selects all tracks that are linked together. Hovering a track's link icon highlights tracks that are linked together. Tracks can be linked by selecting them and then choosing "Link Tracks" from the context menu. To link tracks inside a Group Track, right-click on the Group Track header and choose "Link Tracks" from the context menu. To unlink all tracks in an instance of linked tracks, right-click on the link icon button to select all tracks in that instance and open the context menu, and then choose "Unlink Track(s)" from the context menu. When unlinking tracks inside a Group Track, is it also possible to right-click on the Group Track header and choose "Unlink Track(s)" from the context menu. To link an additional track to an instance of linked tracks, first click on the link icon button, to select all tracks in that instance. Then, add more tracks to the selection while holding the "CMD" (Mac) / "CTRL" (Win) key, and choose "Link Tracks" from the context menu. To remove one or more tracks from an instance of linked tracks, select the corresponding track header(s) and choose "Unlink Track(s)" from the context menu. Any subset of linked tracks, or a mix of linked and unlinked tracks, can be linked together by selecting their track headers and clicking the "Link Tracks" command in the context menu. The following controls and operations are synced on linked tracks: Track editing and time selection operations (e.g., Cut, Copy, Duplicate Time, Delete Time, etc.) The state of Arm buttons Take lane editing and time selection operations, such as auditioning, renaming, inserting and deleting take lanes (note: this also applies when take lanes are hidden in some linked tracks) Fade operations, when clip edges have matching time positions When one or more track headers are selected, pressing "Cmd" (Mac) / "Ctrl" (Win) and clicking on a track's link icon will select the originally selected track, as well as all linked tracks belonging to the linked track's instance. When one or more track headers are selected, pressing "Shift" and clicking on a track's link icon will select all tracks from the originally selected track to the newly-clicked track, as well as all linked tracks belonging to the linked track's instance. Matching fades on linked tracks can be adjusted relative to their original values. When linked tracks have matching fades, dragging the fade handles to their original start/end clip edges, then releasing the mouse, and then dragging the fade handles to their opposite clip edges will still result in fades of equal length.
- Max for Live Improvements Updated the bundled Max build to version 8.1.9. For the changelog, visit: http://cycling74.s3.amazonaws.com/support/version_8_1_9.html When a parameter is controlled by a Max for Live device, a message in the Status Bar now shows exactly which device controls the parameter, and which track contains the device. The context menu of the controlled parameter now provides a "Go to Controlling Device" option. A parameter that is controlled or automated by a Max for Live device will no longer incur a one-buffer delay in the signal sent by Max for Live, if the device containing the controlled parameter is positioned later than the Max for Live device in the device chain. The original delay behavior can be restored using the "-AlwaysDelayMaxForLiveMappings" debug option in the Options.txt file. The following improvements have been added to MIDI routing: It is now possible to route MIDI to and from Max for Live audio effects. Max for Live instruments can now send out MIDI. The new inputs and outputs are routable and show up in a track's "MIDI From" and "MIDI To" choosers. Similar to audio routings, the Live API can control the routable MIDI inputs and outputs. The Max for Live API now has access to: A redesigned, extendable note API for Live 11's new note features (i.e., note probability, velocity range and release velocity). This new API is required for modifying notes without losing MPE data. The sample rate of a Sample loaded in Simpler. The slices of a Sample loaded in Simpler. A Clip or Sample's warp markers. The Clip launch properties: Legato mode, Launch mode, Clip quantization and Velocity amount. Arrangement View Clip IDs in a Track. Adding or removing Macro Controls in a Rack. Macro randomization. Macro Control variations. The Live Set's Groove Pool. A Groove's properties. The Max for Live category in the Max Patcher Inspector window contains a new attribute "Patch supports MPE", to enable MPE for devices that make use of MPE features.
- MIDI Clip Scales A new Scale Mode can be enabled/disabled via the "Scale" button in the Clip box of MIDI clips. At the right side, "Root Note" and "Scale Name" choosers allow setting a root note and scale for the selected clip(s). When a selected clip has Scale Mode enabled and a scale is selected, notes belonging to the scale are highlighted in the piano roll. By default, key tracks belonging to the selected scale are highlighted in the MIDI Note Editor, and the root note is indicated by a prominent highlight in the piano roll. Scale highlighting can be toggled on or off, by pressing the "K" shortcut key while the MIDI Note Editor is in focus, or via the "Highlight Clip Scale" context menu and View menu entry. Newly-created MIDI clips inherit the previously edited or viewed clip scale, even if they have Scale Mode disabled. When editing multiple clips with different key and scale settings, any foreground clip with Scale Mode enabled now updates the global settings that are used to initialize the next created clips, as well as Push's key and scale. When a selected clip has Scale Mode enabled and a scale is selected, pressing the new "Scale" ("Fold to Scale") button (at the right of the "Fold" button) folds to key tracks containing notes, as well as key tracks belonging to the scale. It is now possible to set a preference for spelling a clip's notes with flats, sharps, or both, via the piano roll's context menu. An additional "Auto" option automatically selects flats or sharps based on the position of the root note in the circle of fifths.
- MIDI Note Editing A new Chance Editor allows setting the probability of a MIDI note occurring in a playing clip. Dragging a note's probability marker up and down changes the probability value between 0-100%. The Chance Editor lane is hidden by default. The Velocity and Chance Editor lanes can be shown or hidden via the lane selector toggle buttons at the left. Underneath the lane selector toggle buttons, a triangular toggle button allows showing/hiding all enabled lanes at once. When both lane selectors are hidden/disabled, pressing the triangular toggle button will show both lanes at once. The Velocity and Chance Editor lanes can be resized individually via their split lines. The Velocity and Chance Editor lanes can be resized at once by dragging the split line between the lanes and the MIDI Note Editor. A "Randomize" button allows randomizing velocity/probability values for selected notes (or notes with selected markers), depending on the focused lane. If no markers are selected, values for all notes will be randomized. A "Randomize Range" slider, at the right of the Randomize button, allows specifying a randomization range that can be applied to velocity/probability values. The slider's randomization value can be typed as a number with the keyboard, and triggers randomization when validated using the "Enter" key. Notes with probability values less than 100% will display a little triangle on their upper-left corners. When a key track height is low enough, this triangle will disappear. It is possible to edit probabilities for selected notes in Draw Mode. Updated the appearance of Velocity markers. The value of dragged velocity/probability markers is now indicated on the scale inside the respective lane header, instead of with a value box. It is now possible to edit values for selected velocity/probability markers using numerical keys. Holding the "Shift" key allows fine-tuning the values of selected velocity/probability markers. When using the Arrow Up/Down keys with "Cmd" (Mac) / "Ctrl" (Win) held down, the values of selected velocity/probability markers are incremented by +/-10. It is now possible to edit velocity values for selected notes using numerical keys. It is now possible to see and edit a velocity range, from which a velocity value is selected when a note is played. In the Notes tab, a "Velocity Range" slider allows assigning velocity ranges to selected notes (or all notes in a single clip, if none are selected). Alternatively, holding "Cmd" (Mac) / "Ctrl" (Win) and dragging vertically on a velocity marker reveals a horizontal handle, which, when dragged up or down, sets the maximum or minimum velocity range value. The velocity range is indicated by the shaded area between the horizontal handle and the velocity marker. Double-clicking the velocity marker will reset the range to 0. In the Velocity Editor, when using the Arrow Up/Down keys with "Cmd" (Mac) / "Ctrl" (Win) held down, the velocity ranges of selected notes are incremented by +/-10. In the Velocity and Chance Editors, drawing ramps for selected notes or notes in a selected key track is now possible by holding the "Cmd" (Mac) / "Ctrl" (Win) modifier when Draw Mode is activated. It is now possible to choose between two different Draw Mode options. In the Record/Warp/Launch tab of the Preferences, a new "MIDI Note Drawing" section has a "Draw Mode with Pitch Lock" option. When enabled, drawing MIDI notes is constrained to one single key track (or pitch) at a time, while holding the "ALT" key allows freehand melodic drawing. When disabled, Draw Mode defaults to melodic drawing, and holding the "ALT" key enables pitch-locked drawing. The "Melodic" Draw Mode can be used to erase notes, when drawing starts on an existing note. When the MIDI Note Editor is focused, the "Draw Mode" entry in the Options and context menu now display the currently selected state of the "Draw Mode with Pitch Lock" preference, as "Pitch Lock On/Off". It is now possible to change the note selection in the MIDI Note Editor using the "Alt"+Arrow Up/Down keys (Mac) / "Ctrl"+Arrow Up/Down keys (Win).
- MPE Support & Editing Added support for MIDI Polyphonic Expression (MPE). It is now possible for Live to receive per-note expression from an MPE-capable MIDI controller, by enabling MPE Mode in the Link/Tempo/MIDI Preferences. When a MIDI controller that has MPE Mode enabled is selected as an input device on a track, the channel input routing is fixed to "All Channels" and no individual channels can be selected. The Clip View's new Note Expression tab allows editing five dimensions of MIDI Polyphonic Expression (MPE) for each note in a clip: Pitch (per-note pitch bend), Slide (per-note Y-Axis), Pressure (Poly Aftertouch/MPE Press), Velocity and Release Velocity (Note-Off Velocity). This makes it possible to refine the expression of recorded material, or to automate polyphonic sound variations for MPE-capable instruments. The Slide, Pressure, Velocity, and Release Velocity dimensions are displayed inside new expression lanes below the MIDI Note Editor. Each expression lane can be shown or hidden via the lane selector toggle buttons at the left. Underneath the lane selector toggle buttons, a triangular toggle button allows showing/hiding all enabled lanes at once. When all expression lane selectors are hidden/disabled, pressing the triangular toggle button will show all expression lanes at once. Each expression lane can be resized individually via their split lines. All expression lanes can be resized at once by dragging the split line between the lanes and the MIDI Note Editor. Pressing "ALT" and clicking the "Show/Hide All Expression Editors" button displays all expression lanes, regardless of their previous states. When hiding the expression lanes using the "Show/Hide All Expression Editors" button, or by dragging the "Expression Editor View Split", the lane visibility toggles are hidden as well. When clicking a note (or any of its expression dimensions) in the MIDI Note Editor while the Note Expression tab is open, the note will appear in a transparent overlay. Breakpoints appear, allowing to edit the note's Pitch, Slide, and Pressure envelopes, while markers can be used to edit the note's Velocity and Release Velocity values. Unselected notes will appear grayed out, and their expression envelopes will be dimmed. It is possible to edit expression envelopes for multiple selected notes at once. The expressions are scaled proportionally, similar to that of velocities for multiple selected notes. In the Note Expression tab, the grid is disabled by default for easier editing at a finer resolution. The grid's settings are separate from the grid in the other tabs, and they are saved with the clip. All expression dimensions can be edited in Draw Mode. When a note is moved, its expression envelopes will move along with it. Pitch envelopes are displayed on top of their corresponding notes in the MIDI Note Editor. Pitch breakpoints snap to the nearest semitone when pressing "Cmd" (Mac) / "Alt" (Win) while the grid is off. This also works for Pitch values in Draw Mode. This behaviour can be inverted using the same shortcuts when the grid is on. Pitch envelopes are hidden when Fold Mode is enabled in the Note Expression tab.
- Multi-Clip Editing It is now possible to select and edit notes from multiple selected clips at the same time in the MIDI Note Editor. The new "Focus" button enables Focus Mode, which allows editing the current foreground clip only. Focus Mode can be toggled via the "N" keyboard shortcut. Holding "N" while editing with the mouse toggles Focus Mode momentarily. Loops are now visible and editable via mouse interactions. It is possible to select/edit several multi-clip loop bars at once, by clicking them/dragging their loop markers while pressing the "Cmd" (Mac) / "Ctrl" (Win) modifier key. In Focus Mode, it is not possible to select more than one multi-clip loop bar at a time, and any existing multi-selection is ignored. When Focus Mode is disabled, It is possible to create a contiguous multi-selection of multi-clip loop bars by clicking them while holding the "Shift" modifier key. When Focus Mode is enabled, any existing multi-selection is ignored. When multiple clip loops or or their loop start/end markers are selected, the selection is retained when dragging another one of these parameters without using keyboard modifiers. The loop bar region is vertically resizable. All controls in the Clip box and Notes tab of the Detail View that were previously only visible for a single selected MIDI clip now also appear when multiple MIDI clips are selected. When Focus Mode is enabled while multi-clip editing, the loop length controls and Notes tools are now available for editing the active clip. Previously when crossing a loop boundary while making a rubberband selection, all notes were selected. Now, only the notes that are inside the selection rectangle are selected. When Focus Mode is enabled, the title bar of the Clip box in the Detail View now appears in the active clip's color. When Focus Mode is disabled, "Scale" is enabled and will fold key tracks according to the scales of all clips in the selection that have Scale Mode enabled. "Scale" is disabled if none of the clips in the selection has Scale Mode enabled. When Focus mode is enabled, "Scale" is enabled and folds key tracks to the scale of the foreground clip, if the foreground clip has Scale Mode enabled. "Scale" is disabled if the foreground clip has Scale Mode disabled. It is now possible to transpose notes across multiple selected clips using the Transpose control in the Notes tab. The Invert button is now enabled in the Notes tab when at least one note is selected, and it is possible to invert selected notes from multiple clips at the same time. The inversion is not applied on a per-clip basis, but for the selection as a whole - as if all selected notes belonged to one clip. It is now possible to use the Set Loop Position and Set Loop Length buttons when multiple MIDI clips are selected and playing. It is now possible to use the Loop Position and Loop Length controls when multiple MIDI clips are selected. It is now possible to use the Nudge Backward/Forward buttons when multiple MIDI clips are selected.
- New Devices and Device Improvements The old Chorus, Flanger, and Phaser devices have been deprecated. They are still accessible via a Legacy folder in the Core Library under Devices → Audio Effects. The number of visible Macro Controls in Instrument Racks can now be controlled from a Max for Live device or a control surface. Added MPE support to Drum Racks and Instrument Racks. Per-note expression is forwarded through Racks. Added MPE support to all built-in MIDI effect devices. Per-note expression is forwarded through these devices. The Arpeggiator device now supports modulating the root notes of an arpeggio via MPE. (Note: MPE modulation is not applied to transpositions generated by the device.) Added support for MPE and Push 2's "Poly" Pressure mode to the External Instrument device. Toggling MPE Mode in a plug-in device is now possible via the device's context menu. When MPE is enabled, an indicator appears on the device's title bar. Plug-in devices that support MPE now have MPE Mode enabled by default. Sampler: Sampler now supports MPE. It is now possible to use MPE/Push 2's Pressure mode to modulate individual notes in the Sampler device. MPE modulation can be dialled in via Sampler's MIDI tab. In the MIDI tab, the Pitch Bend Range control has been repositioned and two new modulation sources have been added: "Note PB" (per-note pitch bend) and "Slide" (per-note Y-Axis). In the MIDI tab, Aftertouch has been repositioned and renamed to "Press". Depending on the data sent to the instrument, Press is handled either monophonically (as Channel Aftertouch) or polyphonically (as Poly Aftertouch or MPE Press). Added an "MPE" text label to the right corner of the Sampler device's title bar. Simpler: Simpler now supports MPE. It is now possible to use MPE/Push 2's Pressure mode to modulate individual notes in the Simpler device. By default, Simpler supports Note PB (per-note pitch bend) with a range of +48 semitones. It is possible to use Sampler's MPE Slide and Press parameters in Simpler, after an instance has been converted from Sampler. Added an "MPE" text label to the right corner of the Simpler device's title bar. Wavetable: In the MIDI tab, "AT" (Aftertouch) has been renamed to "Press". Depending on the data sent to the instrument, Press is handled either monophonically (as Channel Aftertouch) or polyphonically (as Poly Aftertouch or MPE Press). Wavetable can now be fully controlled using MPE controllers. MPE modulation can be dialled in via the new MPE tab, which contains four columns: Velocity, Note PB (per-note pitch bend), Slide (per-note Y-Axis) and Press (aftertouch). All MPE modulation sources now appear in the device's expanded view. Added an "MPE" text label to the right corner of the Wavetable device's title bar. Collision: Updated the appearance of the Collision device's UI. Corpus: Updated the appearance of the Corpus device's UI. Electric: Updated the appearance of the Electric device's UI. The "Tine" and "Tone Bar" parameters are now consistently named. Tension: Updated the appearance of the Tension device's UI. Chorus-Ensemble: Introduced "Chorus-Ensemble", a new audio effect device for Live. Chorus-Ensemble provides three different effect modes: Classic is a thickening chorus effect. A high-pass filter allows removing the chorus signal from low frequencies. The width of the chorus signal can be adjusted; this is useful for complex mixing tasks. The feedback signal can be inverted, which results in a "hollow" sound when combined with high feedback values. Ensemble is based on and shares controls with the Classic mode, while adding a third phase-shifted delay line for a thicker chorus sound. Vibrato applies stronger modulation than a chorus to create pitch variation. The shape of the modulation waveform can morph seamlessly from a sine to a triangle, and be used to create well-known "police siren" sounds. Global controls allow setting the modulation rate and amount, output gain, and harmonic saturation (via the "Warmth" parameter). Hybrid Reverb: Introduced "Hybrid Reverb", a new audio effect which allows blending a convolution reverb with a number of reverb algorithms. Besides providing a selection of impulse responses, the device allows dragging any audio file into the device to be used for the convolution processing, as well as shaping the envelope and size of impulse responses via dedicated controls. An algorithmic section contains several reverb modes, each providing a different set of parameters and sonic properties: Dark Hall, Prism, Quartz, Shimmer, and Tides. The convolution and algorithmic sections can be routed either in series or parallel, and their volume relationship can be continuously adjusted via a Blend control. An EQ section can be used to shape the reverb sound, and a "Pre Algo" toggle allows excluding the convolution engine from the EQ. A "Vintage" control introduces a degradation of the signals, to emulate the behavior of older digital reverb units. MPE Control: Introduced "MPE Control", a Max for Live MIDI effect that allows shaping and transforming incoming MPE modulation for Pressure (polyphonic aftertouch, Slide (per-note Y-Axis) and Pitch (per-note pitch bend). The MPE data is transformed via curves, which can consist of either two or three breakpoints. MPE Control also allows smoothing modulation data and can convert MPE data to global MIDI, so that non-MPE instruments can be modulated monophonically via an MPE controller as well. Phaser-Flanger: Introduced "Phaser-Flanger", a new audio effect device for Live. Phaser-Flanger combines the functionalities of the Phaser and Flanger devices into one, as separate effect modes. The Phaser mode has a new, lusher sound with increased frequency and modulation ranges, while the previous Earth and Space modes have been replaced with more expressive parameters. Also included is a new Doubler effect mode. Redux: Upgraded the Redux device. New parameters allow creating a wider range of sounds, from harsh distortion to digital and aliasing artifacts, through to warm and fat 8-bit sounds. Jitter adds noise to the downsampling process. Filters can be enabled pre/post downsampling, while the post-filter cutoff frequency can be adjusted. A Shape parameter allows transforming the quantizer's curve. DC Shift and Dry/Wet controls are also available. Spectral Resonator: Introduced "Spectral Resonator", a new audio effect device for Live. Based on spectral processing, Spectral Resonator uses spectral resonances and pitched overtones to add tonal character to any audio source. MIDI sidechain parameters allow processing any material in key with its surrounding musical elements. Spectral Resonator can be played polyphonically in MIDI mode with up to 16 voices. Spectral Resonator offers several spectral processing types on the input signal, including spectral filtering, spectral chorus, and granularization. Spectral Time: Introduced "Spectral Time", a new audio effect device for Live. Spectral Time combines time freezing and spectral delay effects in a single inspiring device. The freeze and delay effects can be used together or independently, allowing for a wide range of possibilities, such as sustaining any sound infinitely, or combining delays with time-synced fade transitions. Max for Live Device Updates Added support for MPE input to/output from Max for Live devices. When a Max for Live device has MPE Mode enabled, MIDI output from the device will be interpreted as MPE. Additionally, when a Max for Live device is disabled, MPE will be forwarded through the device's dry signal path. The Expression Control device now allows assigning an additional parameter as a mapping target. Pressing a new button in the upper right corner of the LED opens a new view, where each modulation target can be transformed via curves and breakpoints. New modulation sources have been added to the device: Expression (Expression Controller, MIDI CC 11) Random (allows generating a random modulation value per note) Incremental (allows adding a fixed amount to the modulation value with each new note) Slide (per-note Y-Axis, converted to monophonic modulation data; useful when controlling effects in a device chain via an MPE controller) Sustain (Sustain Pedal, MIDI CC 64) All Max for Live devices have been moved inside the application bundle (previously, they lived in the Core Library), to ensure that using Collect All and Save will not create redundant copies of the devices. Improved waveform drawing in the Shaper and Envelope Follower devices.
- Push Added a "Pressure" switch to Push 2's Setup Menu (shown when pressing the Setup button) that allows toggling between monophonic and polyphonic aftertouch when playing melodic instruments. The state of this switch is stored in Live's preferences. Push 2 and MIDI controllers sending polyphonic aftertouch can be used with plug-in devices that support polyphonic aftertouch. When Push 2's Pressure mode is set to "Poly", the Repeat button now produces notes at full velocity when Accent is enabled. When a Rack contains a parameter mapped to one of the new Macro Controls (i.e., Macro 9-16), the additional Macro Control parameters will appear in a new device within the Rack. Degree symbol icons (Push 1) or bullet point icons (Push 2) are used to differentiate the Rack from the device. The new device is only visible when the Rack is open, but otherwise behaves exactly the same as the Rack.
- Push MIDI Clip Mode When Push's In Key/Chromatic is set to In Key Mode, and the selected MIDI clip has Scale Mode enabled, selecting a scale on Push will update that clip’s scale in Live. If Focus Mode is enabled in multi-clip editing, only the foreground clip's key and scale will be updated in Live. When Push's In Key/Chromatic is set to In Key Mode, and the selected MIDI clip has Scale Mode enabled, selecting a scale in Live will change the pad layout on Push.
- Rack and Macro Control Improvements Pressing the "Rand" button in the title bar of a Rack randomizes the values of mapped Macro Controls. A mapped Macro Control can be excluded from randomization via the "Exclude Macro from Randomization" context menu option. Volume Macros in Instrument Rack presets are excluded from randomization by default. A new "Show/Hide Macro Variations" view selector button in Racks opens a view that allows storing the state of the Macro Controls as a variation preset via the "New" button. By default, each stored variation will be named sequentially as "Variation 1", "Variation 2", etc. A variation can be renamed, duplicated or deleted via its context menu, the Edit menu, or using keyboard shortcuts. A variation can be launched in its stored state via the "Launch Macro Variation" button to the right, or overwritten via the "Overwrite Macro Variation" button to the left. Additional controls are visible in Key/MIDI Map Mode. The maximum number of available Macro Controls in Live has been doubled to 16. New "+" and "-" view selector buttons in Racks allow setting how many Macro Controls are shown or hidden. The state of the shown and hidden Macro Controls is saved in the Live Set. When the title bar of a Rack is narrow enough, the Rand and Map buttons will appear as "R" and "M". Added a context menu entry that excludes a Macro Control from changing when a different Macro Control variation is launched. Unchecking the context menu entry will re-enable changes to that control as before, as the values are still stored in the variation.
- Session View Improvements In the Default Live Set, scene name fields will be empty and no longer contain numbers. Scene numbers are now displayed in a new column in the Master track. Scene numbers are determined by their position. When a scene is moved, its number changes according to the scene's new position. Selecting a scene (or multiple scenes) now opens the new Scene View, which allows editing the selected scene's tempo, time signature and Follow Actions. Dragging the left edge of the Master track's title header reveals two new controls, which allow assigning a tempo or time signature to a scene. When enabled, these controls can be disabled and reset via a context menu or pressing the Delete key. It is also possible to disable the controls by double-clicking them. Clicking a Scene Tempo or Scene Time Signature control opens the Scene View. When a scene or clip slot is selected, the Arrow Right/Left keys can now be used to navigate to the Scene Tempo/Time Signature controls. When a Scene Tempo/Time Signature control is selected in the Master track, pressing "Enter" once will select the respective scene header. Pressing "Enter" again launches the selected scene. When editing a scene name, tempo or time signature value in the Master track using the keyboard, using the "Tab" or "Shift"+"Tab" keyboard shortcut navigates to the next or previous control, to allow editing these controls quickly. The navigation moves to the next or previous scene when reaching the last or first control in a scene. Sets created in Live 10 that have tempo and/or time signature values specified by scene names will have their values migrated to the new Scene Tempo/Time Signature controls, and, when such Sets are first opened in Live 11, the Master track is widened so that the Scene Tempo/Time Signature columns are visible. In the Scene View, if a scene does not have a name, and only one scene is selected, the word "Scene" is displayed in the title bar. The scene number is displayed on the right-hand side of the title bar. It is now possible to rename multiple selected clips at once, via the Rename command in the context menu or Edit menu, or using the "CMD"+"R" (Mac) / "CTRL"+"R" (Win) keyboard shortcut. Added a "Cancel Scene Launch" entry to the Master track's context menu. Clicking this entry cancels the launch of any previously triggered scene. Added a "Cancel Scene Launch" button to the Master track in Key/MIDI Map Mode. It is now possible to make the Master track narrower, so that Master Volume value labels can be hidden. The "Solo" label of the Solo/Cue Mode switch in the Master track now appears centered. The "Stop All Clips" button in the Master track now flashes when clicked, and blinks while fired and waiting for the next launch period, similar to all other "Clip/Scene Launch" and "Clip/Scene Stop" buttons. This also works when a scene's "Stop" Follow Action is triggered.
- Setup Live requires macOS 10.13 or later. Live's Status Bar will now indicate when an update for Live is being downloaded. Once it is downloaded, the Status Bar will state that Live must be restarted in order to apply the update. It is possible to change this default behavior, so that Live will first ask for permission before applying a new available update. To do so, go to Preferences → Licenses/Maintenance and set Get Automatic Updates to Ask Me. The next time an update for Live is available, the Status Bar will display buttons for choosing whether or not to apply the update. ReWire support has been removed.
- Tempo Follower Introduced the Tempo Follower, which adapts Live’s tempo to stay in time with a drummer or another rhythmic audio source. In the Preferences via the "Link/Tempo/MIDI" tab (previously named "Link/MIDI"), a "Tempo Follower" section has been added below the "Link" section. A "Show Tempo Follower Toggle" switch shows/hides the "Follow" button in the Control Bar (Note: the Tempo Follower does not run when hidden). Its state is stored in the Preferences.cfg file. An "Input Channel (Ext. In)" chooser allows choosing the channel from which the tempo will be tracked, and displays a level meter for each channel. Its state is stored in the Preferences.cfg file. When the "Follow" switch is visible in the Control Bar, it can be used to toggle the Tempo Follower on and off. Mappings can be assigned to this switch in Key/MIDI Map Mode. Link, Tempo Follower, and External Sync are mutually exclusive (for instance, activating Tempo Follower will deactivate Link). When the Tempo Follower cannot be connected to the audio input device channel specified in the Preferences, its Follow button is disabled in the Control Bar. When the Follow button is disabled, it is automatically set to Off and will not automatically switch on again when a valid audio source is selected.
- Live Bugfixes Fixed a crash that could occur while attempting to automate some controls in certain plug-ins. Fixed some bugs in Max for Live devices: The LFO device's modulation would not work if the device was instantiated while the audio engine was turned off. The MPE Control device would cause stuck notes when automating multiple curve parameters during playback. Fixed a bug in the browser's content pane that prevented the column settings from being correctly retained. Live no longer crashes when right-clicking on a Send parameter in the Arrangement View, when that Send parameter is controlled by a Max device (e.g. LFO). Fixed a bug where the Indexer would crash on macOS 10.15. Fixed a bug where the Live index would quit unexpectedly. On macOS, Live does not crash in rare circumstances when audio interfaces change. Previously, when dragging an audio sample into Live's browser after renaming it, the sample would appear with the wrong name. Previously, the Session View would jump unexpectedly when selecting return tracks. The text that appears upon successfully authorizing Live is now improved in all available Live languages. Fixed a bug where dragging warp markers to the left in a long clip would reset the clip's segment BPM to the lowest value. Additionally, zoom-scrolling in the Detail View has received a complete technical overhaul that should be mostly unnoticeable, but will be the basis for smoother workflows in the future. Fixed a bug that prevented the "Show in Places" context menu entry from appearing for folders in the browser's Collections section. Fixed a redundant log that could appear, under certain circumstances. Fixed some crashes that could occur, under certain circumstances. Previously, when hot-swapping certain devices or chains, the search function did not work as expected in labels within the browser's "Places" section. Previously, trying to drag a sample or preset from the browser would select all elements below it, under certain circumstances.
- Max for Live Bugfixes The way Max for Live devices are rendered and positioned in Live's UI has been overhauled. This fixes a range of bugs and improves the general experience of working with Max for Live devices, including improvements to focus, positioning, scrolling behavior and performance: Trackpad scrolling did not work correctly when the mouse was over a Max for Live device. Scrolling the Device View with a device containing a jit.pwindow on macOS would cause Live's UI to hang. The Max for Live window was drawn alone and the focus was not regained by Live after saving a Max for Live device when Live was minimized. A graphic lag would occur when switching between channels containing some Max for Live devices. Dropping a Max for Live device onto Live's app icon while Live was minimized resulted in a floating Max for Live device. Opening a Max for Live device from the system file manager while Live is minimized resulted in a floating Max for Live device. Scrolling in the Device View would result in unsynchronized movements of the Max for Live device and the other devices in Live.
