# LOM - The Live Object Model

*Objects which comprise the Live API described by their structure, properties and functions.*
The Live Object Model lists a number of Live object classes with their properties and functions, as well as their parent-child relations through which a hierarchy is formed. Please refer to the [Live API overview chapter](/userguide/m4l/live_api/)for definitions of the basic Live API terms and a list of the Max objects used to access it.   
  
*This document refers to Ableton Live version 12.3b9*

## Object Model Overview

| *Click on the classes to navigate to their description.* |
| --- |

Expand

## API Objects

| Item | Description |
| --- | --- |
| [Application](/apiref/lom/application/) | This class represents the Live application. It is reachable by the root path live_app ... |
| [Application.View](/apiref/lom/application_view/) | This class represents the aspects of the Live application related to viewing the application.... |
| [Chain](/apiref/lom/chain/) | This class represents a group device chain in Live. |
| [ChainMixerDevice](/apiref/lom/chainmixerdevice/) | This class represents a chain's mixer device in Live. |
| [Clip](/apiref/lom/clip/) | This class represents a clip in Live. It can be either an audio clip or a MIDI clip in the Arr... |
| [Clip.View](/apiref/lom/clip_view/) | Representing the view aspects of a Clip. |
| [ClipSlot](/apiref/lom/clipslot/) | This class represents an entry in Live's Session View matrix. The properties ... |
| [CompressorDevice](/apiref/lom/compressordevice/) | This class represents a Compressor device in Live. A CompressorDevice shares all of the ch... |
| [ControlSurface](/apiref/lom/controlsurface/) | A ControlSurface can be reached either directly by the root path control_surfaces N or by g... |
| [CuePoint](/apiref/lom/cuepoint/) | Represents a locator in the Arrangement View. |
| [Device](/apiref/lom/device/) | This class represents a MIDI or audio device in Live. |
| [Device.View](/apiref/lom/device_view/) | Representing the view aspects of a Device. |
| [DeviceIO](/apiref/lom/deviceio/) | This class represents an input or output bus of a Live device. |
| [DeviceParameter](/apiref/lom/deviceparameter/) | This class represents an (automatable) parameter within a MIDI or audio device. To modify a de... |
| [DriftDevice](/apiref/lom/driftdevice/) | This class represents an instance of a Drift device in Live. A DriftDevice has all the... |
| [DrumCellDevice](/apiref/lom/drumcelldevice/) | This class represents an instance of a Drum Sampler device in Live. A DrumCell has all... |
| [DrumChain](/apiref/lom/drumchain/) | This class represents a Drum Rack device chain in Live. A DrumChain is a type ... |
| [DrumPad](/apiref/lom/drumpad/) | This class represents a Drum Rack pad in Live. |
| [Eq8Device](/apiref/lom/eq8device/) | This class represents an instance of an EQ Eight device in Live. An Eq8Device has all ... |
| [Eq8Device.View](/apiref/lom/eq8device_view/) | Represents the view aspects of an Eq8Device. An Eq8Device.View has all the children, p... |
| [Groove](/apiref/lom/groove/) | This class represents a groove in Live. Available since Live 11.0. ... |
| [GroovePool](/apiref/lom/groovepool/) | This class represents the groove pool in Live. It provides access to the current set's list of groov... |
| [HybridReverbDevice](/apiref/lom/hybridreverbdevice/) | This class represents an instance of a Hybrid Reverb device in Live. A HybridReverbDev... |
| [LooperDevice](/apiref/lom/looperdevice/) | This class represents an instance of a Looper device in Live. An LooperDevice has all ... |
| [MaxDevice](/apiref/lom/maxdevice/) | This class represents a Max for Live device in Live. A MaxDevice is a type of Device... |
| [MeldDevice](/apiref/lom/melddevice/) | This class represents an instance of a Meld device in Live. A MeldDevice has all the p... |
| [MixerDevice](/apiref/lom/mixerdevice/) | This class represents a mixer device in Live. It provides access to volume, panning and other ... |
| [PluginDevice](/apiref/lom/plugindevice/) | This class represents a plug-in device. A PluginDevice is a type of Device, meaning ... |
| [RackDevice](/apiref/lom/rackdevice/) | This class represents a Live Rack Device. A RackDevice is a type of Device, meaning th... |
| [RackDevice.View](/apiref/lom/rackdevice_view/) | Represents the view aspects of a Rack Device. A RackDevice.View is a type of Device.Vi... |
| [RoarDevice](/apiref/lom/roardevice/) | This class represents an instance of a Roar device in Live. A RoarDevice has all the p... |
| [Sample](/apiref/lom/sample/) | This class represents a sample file loaded into Simpler. |
| [Scene](/apiref/lom/scene/) | This class represents a series of clip slots in Live's Session View matrix.... |
| [ShifterDevice](/apiref/lom/shifterdevice/) | This class represents an instance of the Shifter audio effect. A ShifterDevice is a ty... |
| [SimplerDevice](/apiref/lom/simplerdevice/) | This class represents an instance of Simpler. A SimplerDevice is a type of device, mea... |
| [SimplerDevice.View](/apiref/lom/simplerdevice_view/) | Represents the view aspects of a SimplerDevice. A SimplerDevice.View is a type of Device.V... |
| [Song](/apiref/lom/song/) | This class represents a Live Set. The current Live Set is reachable by the root path li... |
| [Song.View](/apiref/lom/song_view/) | This class represents the view aspects of a Live document: the Session and Arrangement Views.... |
| [SpectralResonatorDevice](/apiref/lom/spectralresonatordevice/) | This class represents an instance of a Spectral Resonator device in Live. An SpectralR... |
| [TakeLane](/apiref/lom/takelane/) | This class represents a take lane in Live. Tracks in Live can have take lanes in Arrangement View, w... |
| [this_device](/apiref/lom/this_device/) | This root path represents the device containing the live.path object to which the ... |
| [Track](/apiref/lom/track/) | This class represents a track in Live. It can either be an audio track, a MIDI track, a return... |
| [Track.View](/apiref/lom/track_view/) | Representing the view aspects of a track. |
| [TuningSystem](/apiref/lom/tuningsystem/) | This class represents a tuning system in Live. |
| [WavetableDevice](/apiref/lom/wavetabledevice/) | This class represents a Wavetable instrument. A WavetableDevice shares all of the ch... |
