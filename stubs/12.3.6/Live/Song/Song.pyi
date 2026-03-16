from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable

if TYPE_CHECKING:
    from . import BeatTime, CaptureDestination, CaptureMode, CuePoint, Quantization, RecordingQuantization, SmptTime
    from Live.Base import IntVector, Vector
    from Live.Chain import Chain
    from Live.Clip import Clip
    from Live.ClipSlot import ClipSlot
    from Live.Device import Device
    from Live.Envelope import Envelope
    from Live.GroovePool import GroovePool
    from Live.Scene import Scene
    from Live.Track import Track
    from Live.TuningSystem import TuningSystem



class Song:
    """This class represents a Live set."""

    class View:
        """Representing the view aspects of a Live document: The Session and Arrangerview."""

        @property
        def _live_ptr(self) -> int:
            ...

        def add_detail_clip_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "detail_clip" has changed.
            """
            ...

        def add_draw_mode_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "draw_mode" has changed.
            """
            ...

        def add_follow_song_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "follow_song" has changed.
            """
            ...

        def add_selected_chain_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "selected_chain" has changed.
            """
            ...

        def add_selected_parameter_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "selected_parameter" has changed.
            """
            ...

        def add_selected_scene_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "selected_scene" has changed.
            """
            ...

        def add_selected_track_listener(self, callback: Callable | None) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "selected_track" has changed.
            """
            ...

        @property
        def canonical_parent(self) -> Song:
            """Get the canonical parent of the song view."""
            ...

        @property
        def detail_clip(self) -> None:
            """Get/Set the Clip that is currently visible in Lives Detailview."""
            ...

        @detail_clip.setter
        def detail_clip(self, value: None) -> None: ...

        def detail_clip_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "detail_clip".
            """
            ...

        @property
        def draw_mode(self) -> bool:
            """Get/Set if the Envelope/Note draw mode is enabled."""
            ...

        @draw_mode.setter
        def draw_mode(self, value: bool) -> None: ...

        def draw_mode_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "draw_mode".
            """
            ...

        @property
        def follow_song(self) -> bool:
            """Get/Set if the Arrangerview should scroll to show the playmarker."""
            ...

        @follow_song.setter
        def follow_song(self, value: bool) -> None: ...

        def follow_song_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "follow_song".
            """
            ...

        @property
        def highlighted_clip_slot(self) -> ClipSlot:
            """Get/Set the clip slot, defined via the selected track and scene in the Session.Will be None for Main- and Sendtracks."""
            ...

        @highlighted_clip_slot.setter
        def highlighted_clip_slot(self, value: ClipSlot) -> None: ...

        def remove_detail_clip_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "detail_clip".
            """
            ...

        def remove_draw_mode_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "draw_mode".
            """
            ...

        def remove_follow_song_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "follow_song".
            """
            ...

        def remove_selected_chain_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "selected_chain".
            """
            ...

        def remove_selected_parameter_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "selected_parameter".
            """
            ...

        def remove_selected_scene_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "selected_scene".
            """
            ...

        def remove_selected_track_listener(self, callback: Callable | None) -> None:
            """
            Remove a previously set listener function or method from
            property "selected_track".
            """
            ...

        def select_device(self, device: Device | None, should_appoint_device: bool = True) -> None:
            """Select the given device."""
            ...

        @property
        def selected_chain(self) -> None:
            """Get the highlighted chain if available."""
            ...

        @selected_chain.setter
        def selected_chain(self, value: None) -> None: ...

        def selected_chain_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "selected_chain".
            """
            ...

        @property
        def selected_parameter(self) -> None:
            """Get the currently selected device parameter."""
            ...

        def selected_parameter_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "selected_parameter".
            """
            ...

        @property
        def selected_scene(self) -> Scene:
            """Get/Set the current selected scene in Lives Sessionview."""
            ...

        @selected_scene.setter
        def selected_scene(self, value: Scene) -> None: ...

        def selected_scene_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "selected_scene".
            """
            ...

        @property
        def selected_track(self) -> Track:
            """Get/Set the current selected Track in Lives Session or Arrangerview."""
            ...

        @selected_track.setter
        def selected_track(self, value: Track) -> None: ...

        def selected_track_has_listener(self, callback: Callable | None) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "selected_track".
            """
            ...

    @property
    def _live_ptr(self) -> int:
        ...

    def add_appointed_device_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "appointed_device" has changed.
        """
        ...

    def add_arrangement_overdub_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "arrangement_overdub" has changed.
        """
        ...

    def add_back_to_arranger_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "back_to_arranger" has changed.
        """
        ...

    def add_can_capture_midi_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "can_capture_midi" has changed.
        """
        ...

    def add_can_jump_to_next_cue_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "can_jump_to_next_cue" has changed.
        """
        ...

    def add_can_jump_to_prev_cue_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "can_jump_to_prev_cue" has changed.
        """
        ...

    def add_clip_trigger_quantization_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "clip_trigger_quantization" has changed.
        """
        ...

    def add_count_in_duration_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "count_in_duration" has changed.
        """
        ...

    def add_cue_points_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "cue_points" has changed.
        """
        ...

    def add_current_song_time_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "current_song_time" has changed.
        """
        ...

    def add_data_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "data" has changed.
        """
        ...

    def add_exclusive_arm_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "exclusive_arm" has changed.
        """
        ...

    def add_groove_amount_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "groove_amount" has changed.
        """
        ...

    def add_is_ableton_link_enabled_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_ableton_link_enabled" has changed.
        """
        ...

    def add_is_ableton_link_start_stop_sync_enabled_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_ableton_link_start_stop_sync_enabled" has changed.
        """
        ...

    def add_is_counting_in_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_counting_in" has changed.
        """
        ...

    def add_is_playing_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "is_playing" has changed.
        """
        ...

    def add_loop_length_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "loop_length" has changed.
        """
        ...

    def add_loop_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "loop" has changed.
        """
        ...

    def add_loop_start_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "loop_start" has changed.
        """
        ...

    def add_metronome_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "metronome" has changed.
        """
        ...

    def add_midi_recording_quantization_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "midi_recording_quantization" has changed.
        """
        ...

    def add_nudge_down_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "nudge_down" has changed.
        """
        ...

    def add_nudge_up_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "nudge_up" has changed.
        """
        ...

    def add_overdub_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "overdub" has changed.
        """
        ...

    def add_punch_in_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "punch_in" has changed.
        """
        ...

    def add_punch_out_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "punch_out" has changed.
        """
        ...

    def add_re_enable_automation_enabled_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "re_enable_automation_enabled" has changed.
        """
        ...

    def add_record_mode_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "record_mode" has changed.
        """
        ...

    def add_return_tracks_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "return_tracks" has changed.
        """
        ...

    def add_root_note_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "root_note" has changed.
        """
        ...

    def add_scale_information_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "scale_information" has changed.
        """
        ...

    def add_scale_intervals_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "scale_intervals" has changed.
        """
        ...

    def add_scale_mode_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "scale_mode" has changed.
        """
        ...

    def add_scale_name_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "scale_name" has changed.
        """
        ...

    def add_scenes_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "scenes" has changed.
        """
        ...

    def add_session_automation_record_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "session_automation_record" has changed.
        """
        ...

    def add_session_record_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "session_record" has changed.
        """
        ...

    def add_session_record_status_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "session_record_status" has changed.
        """
        ...

    def add_signature_denominator_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "signature_denominator" has changed.
        """
        ...

    def add_signature_numerator_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "signature_numerator" has changed.
        """
        ...

    def add_song_length_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "song_length" has changed.
        """
        ...

    def add_start_time_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "start_time" has changed.
        """
        ...

    def add_swing_amount_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "swing_amount" has changed.
        """
        ...

    def add_tempo_follower_enabled_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "tempo_follower_enabled" has changed.
        """
        ...

    def add_tempo_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "tempo" has changed.
        """
        ...

    def add_tracks_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "tracks" has changed.
        """
        ...

    def add_tuning_system_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "tuning_system" has changed.
        """
        ...

    def add_visible_tracks_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "visible_tracks" has changed.
        """
        ...

    @property
    def appointed_device(self) -> Device:
        """Read, write, and listen access to the appointed Device"""
        ...

    @appointed_device.setter
    def appointed_device(self, value: Device) -> None: ...

    def appointed_device_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "appointed_device".
        """
        ...

    @property
    def arrangement_overdub(self) -> bool:
        """Get/Set the global arrangement overdub state."""
        ...

    @arrangement_overdub.setter
    def arrangement_overdub(self, value: bool) -> None: ...

    def arrangement_overdub_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "arrangement_overdub".
        """
        ...

    @property
    def back_to_arranger(self) -> bool:
        """
        Get/Set if triggering a Clip in the Session, disabled the playback of
        Clips in the Arranger.
        """
        ...

    @back_to_arranger.setter
    def back_to_arranger(self, value: bool) -> None: ...

    def back_to_arranger_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "back_to_arranger".
        """
        ...

    def begin_undo_step(self) -> None:
        ...

    @property
    def can_capture_midi(self) -> bool:
        """Get whether there currently is material to be captured on any tracks."""
        ...

    def can_capture_midi_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "can_capture_midi".
        """
        ...

    @property
    def can_jump_to_next_cue(self) -> bool:
        """
        Returns true when there is a cue marker right to the playing pos that
        we could jump to.
        """
        ...

    def can_jump_to_next_cue_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "can_jump_to_next_cue".
        """
        ...

    @property
    def can_jump_to_prev_cue(self) -> bool:
        """
        Returns true when there is a cue marker left to the playing pos that
        we could jump to.
        """
        ...

    def can_jump_to_prev_cue_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "can_jump_to_prev_cue".
        """
        ...

    @property
    def can_redo(self) -> bool:
        """Returns true if there is an undone action that we can redo."""
        ...

    @property
    def can_undo(self) -> bool:
        """Returns true if there is an action that we can restore."""
        ...

    @property
    def canonical_parent(self) -> None:
        """Get the canonical parent of the song."""
        ...

    def capture_and_insert_scene(self, capture_mode: CaptureMode | int = 0) -> None:
        """
        Capture currently playing clips and insert them as a new scene after
        the selected scene. Raises a runtime error if creating a new scene would exceed the limitations.
        """
        ...

    def capture_midi(self, destination: CaptureDestination | int = 0) -> None:
        """
        Capture recently played MIDI material from audible tracks.
        If no Destination is given or Destination is set to CaptureDestination.auto, the captured material is inserted into the Session or Arrangement depending on which is visible.
        If Destination is set to CaptureDestination.session or CaptureDestination.arrangement, inserts the material into Session or Arrangement, respectively.
        Raises a limitation error when capturing into the Session and a new scene would have to be created but can't because it would exceed the limitations.
        """
        ...

    @property
    def clip_trigger_quantization(self) -> Quantization:
        """
        Get/Set access to the quantization settings that are used to fire
        Clips in the Session.
        """
        ...

    @clip_trigger_quantization.setter
    def clip_trigger_quantization(self, value: Quantization) -> None: ...

    def clip_trigger_quantization_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "clip_trigger_quantization".
        """
        ...

    def continue_playing(self) -> None:
        """Continue playing the song from the current position"""
        ...

    @property
    def count_in_duration(self) -> int:
        """
        Get the count in duration. Returns an index, mapped as follows:
        0 - None, 1 - 1 Bar, 2 - 2 Bars, 3 - 4 Bars.
        """
        ...

    def count_in_duration_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "count_in_duration".
        """
        ...

    def create_audio_track(self, index: int | None = None) -> Track:
        """
        Create a new audio track at the optional given index and return it.If the index is -1,
        the new track is added at the end. It will create a default audio track if possible.
        If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item
        """
        ...

    def create_midi_track(self, index: int | None = None) -> Track:
        """
        Create a new midi track at the optional given index and return it.If the index is -1,
        the new track is added at the end.It will create a default midi track if possible.
        If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item
        """
        ...

    def create_return_track(self) -> Track:
        """
        Create a new return track at the end and return it. If the new track would exceed
        the limitations, a limitation error is raised.
        If the maximum number of return tracks is exceeded, a RuntimeError is raised.
        """
        ...

    def create_scene(self, index: int | None) -> Scene:
        """
        Create a new scene at the given index. If the index is -1,
        the new scene is added at the end. If the index is invalid or
        the new scene would exceed the limitations, a limitation error is raised.
        """
        ...

    @property
    def cue_points(self) -> Vector[CuePoint]:
        """Const access to a list of all cue points of the Live Song."""
        ...

    def cue_points_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "cue_points".
        """
        ...

    @property
    def current_song_time(self) -> float:
        """Get/Set access to the songs current playing position in beats."""
        ...

    @current_song_time.setter
    def current_song_time(self, value: float) -> None: ...

    def current_song_time_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "current_song_time".
        """
        ...

    def data_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "data".
        """
        ...

    def delete_return_track(self, index: int | None) -> None:
        """
        Delete the return track with the given index. If no track with this index
        exists, an exception will be raised.
        """
        ...

    def delete_scene(self, index: int | None) -> None:
        """
        Delete the scene with the given index. If no scene with this index
        exists, an exception will be raised.
        """
        ...

    def delete_track(self, index: int | None) -> None:
        """
        Delete the track with the given index. If no track with this index
        exists, an exception will be raised.
        """
        ...

    def duplicate_scene(self, index: int | None) -> None:
        """
        Duplicates a scene and selects the new one.
        Raises a limitation error if creating a new scene would exceed the limitations.
        """
        ...

    def duplicate_track(self, index: int | None) -> None:
        """
        Duplicates a track and selects the new one.
        If the track is inside a folded group track, the group track is unfolded.
        Raises a limitation error if creating a new track would exceed the limitations.
        """
        ...

    def end_undo_step(self) -> None:
        ...

    @property
    def exclusive_arm(self) -> bool:
        """Get if Tracks should be armed exclusively by default."""
        ...

    def exclusive_arm_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "exclusive_arm".
        """
        ...

    @property
    def exclusive_solo(self) -> bool:
        """Get if Tracks should be soloed exclusively by default."""
        ...

    @property
    def file_path(self) -> str:
        """Get the current Live Set's path on disk."""
        ...

    def find_device_position(self, device: Device | None, target: Track | Chain | None, target_position: int | None) -> int:
        """
        Returns the closest possible position to the given target, where the
        device can be inserted. If inserting is not possible at all (i.e. if
        the device type is wrong), -1 is returned.
        """
        ...

    def force_link_beat_time(self) -> None:
        """
        Force the Link timeline to jump to Lives current beat time.
        Danger: This can cause beat time discontinuities in other connected apps.
        """
        ...

    def get_beats_loop_length(self) -> BeatTime:
        """
        Get const access to the songs loop length, using a
        BeatTime class with the current global set signature.
        """
        ...

    def get_beats_loop_start(self) -> BeatTime:
        """
        Get const access to the songs loop start, using a
        BeatTime class with the current global set signature.
        """
        ...

    def get_current_beats_song_time(self) -> BeatTime:
        """
        Get const access to the songs current playing position, using a
        BeatTime class with the current global set signature.
        """
        ...

    def get_current_smpte_song_time(self, format: int | None) -> SmptTime:
        """
        Get const access to the songs current playing position, by specifying
        the SMPTE format in which you would like to receive the time.
        """
        ...

    def get_data(self, key: str | None, default_value: Any | None) -> Any:
        """Get data for the given key, that was previously stored using set_data."""
        ...

    @property
    def groove_amount(self) -> float:
        """
        Get/Set the global groove amount, that adjust all setup grooves
        in all clips.
        """
        ...

    @groove_amount.setter
    def groove_amount(self, value: float) -> None: ...

    def groove_amount_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "groove_amount".
        """
        ...

    @property
    def groove_pool(self) -> GroovePool:
        """Get the groove pool."""
        ...

    @property
    def is_ableton_link_enabled(self) -> bool:
        """Enable/disable Ableton Link."""
        ...

    @is_ableton_link_enabled.setter
    def is_ableton_link_enabled(self, value: bool) -> None: ...

    def is_ableton_link_enabled_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "is_ableton_link_enabled".
        """
        ...

    @property
    def is_ableton_link_start_stop_sync_enabled(self) -> bool:
        """Enable/disable Ableton Link Start Stop Sync."""
        ...

    @is_ableton_link_start_stop_sync_enabled.setter
    def is_ableton_link_start_stop_sync_enabled(self, value: bool) -> None: ...

    def is_ableton_link_start_stop_sync_enabled_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "is_ableton_link_start_stop_sync_enabled".
        """
        ...

    @property
    def is_counting_in(self) -> bool:
        """Get whether currently counting in."""
        ...

    def is_counting_in_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "is_counting_in".
        """
        ...

    def is_cue_point_selected(self) -> bool:
        """Return true if the global playing pos is currently on a cue point."""
        ...

    @property
    def is_playing(self) -> bool:
        """Returns true if the Song is currently playing."""
        ...

    @is_playing.setter
    def is_playing(self, value: bool) -> None: ...

    def is_playing_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "is_playing".
        """
        ...

    def jump_by(self, beats: float | None) -> None:
        """Set a new playing pos, relative to the current one."""
        ...

    def jump_to_next_cue(self) -> None:
        """Jump to the next cue (marker) if possible."""
        ...

    def jump_to_prev_cue(self) -> None:
        """Jump to the prior cue (marker) if possible."""
        ...

    @property
    def last_event_time(self) -> float:
        """
        Return the time of the last set event in the song. In contrary to
        song_length, this will not add some extra beats that are mostly needed
        for Display purposes in the Arrangerview.
        """
        ...

    @property
    def loop(self) -> bool:
        """
        Get/Set the looping flag that en/disables the usage of the global
        loop markers in the song.
        """
        ...

    @loop.setter
    def loop(self, value: bool) -> None: ...

    def loop_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "loop".
        """
        ...

    @property
    def loop_length(self) -> float:
        """Get/Set the length of the global loop marker position in beats."""
        ...

    @loop_length.setter
    def loop_length(self, value: float) -> None: ...

    def loop_length_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "loop_length".
        """
        ...

    @property
    def loop_start(self) -> float:
        """Get/Set the start of the global loop marker position in beats."""
        ...

    @loop_start.setter
    def loop_start(self, value: float) -> None: ...

    def loop_start_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "loop_start".
        """
        ...

    @property
    def master_track(self) -> Track:
        """Access to the Main Track (always available)"""
        ...

    @property
    def metronome(self) -> bool:
        """Get/Set if the metronom is audible."""
        ...

    @metronome.setter
    def metronome(self, value: bool) -> None: ...

    def metronome_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "metronome".
        """
        ...

    @property
    def midi_recording_quantization(self) -> RecordingQuantization:
        """
        Get/Set access to the settings that are used to quantize
        MIDI recordings.
        """
        ...

    @midi_recording_quantization.setter
    def midi_recording_quantization(self, value: RecordingQuantization) -> None: ...

    def midi_recording_quantization_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "midi_recording_quantization".
        """
        ...

    def move_device(self, device: Device | None, target: Track | Chain | None, target_position: int | None) -> int:
        """Move a device into the target at the given position, where 0 moves it before the first device and len(devices) moves it to the end of the device chain.If the device cannot be moved to this position, the nearest possible position is chosen. If the device type is not valid, a runtime error is raised.Returns the index, where the device was moved to."""
        ...

    @property
    def name(self) -> str:
        """Get the current Live Set's name."""
        ...

    @property
    def nudge_down(self) -> bool:
        """Get/Set the status of the nudge down button."""
        ...

    @nudge_down.setter
    def nudge_down(self, value: bool) -> None: ...

    def nudge_down_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "nudge_down".
        """
        ...

    @property
    def nudge_up(self) -> bool:
        """Get/Set the status of the nudge up button."""
        ...

    @nudge_up.setter
    def nudge_up(self, value: bool) -> None: ...

    def nudge_up_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "nudge_up".
        """
        ...

    @property
    def overdub(self) -> bool:
        """
        Legacy hook for Live 8 overdub state. Now hooks to
        session record, but never starts playback.
        """
        ...

    @overdub.setter
    def overdub(self, value: bool) -> None: ...

    def overdub_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "overdub".
        """
        ...

    def play_selection(self) -> None:
        """
        Start playing the current set selection, or do nothing if
        no selection is set.
        """
        ...

    @property
    def punch_in(self) -> bool:
        """
        Get/Set the flag that will enable recording as soon as the Song plays
        and hits the global loop start region.
        """
        ...

    @punch_in.setter
    def punch_in(self, value: bool) -> None: ...

    def punch_in_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "punch_in".
        """
        ...

    @property
    def punch_out(self) -> bool:
        """
        Get/Set the flag that will disable recording as soon as the Song plays
        and hits the global loop end region.
        """
        ...

    @punch_out.setter
    def punch_out(self, value: bool) -> None: ...

    def punch_out_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "punch_out".
        """
        ...

    def re_enable_automation(self) -> None:
        """Discards overrides of automated parameters."""
        ...

    @property
    def re_enable_automation_enabled(self) -> bool:
        """Returns true if some automated parameter has been overriden"""
        ...

    def re_enable_automation_enabled_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "re_enable_automation_enabled".
        """
        ...

    @property
    def record_mode(self) -> bool:
        """Get/Set the state of the global recording flag."""
        ...

    @record_mode.setter
    def record_mode(self, value: bool) -> None: ...

    def record_mode_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "record_mode".
        """
        ...

    def redo(self) -> str:
        """Redo the last action that was undone."""
        ...

    def remove_appointed_device_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "appointed_device".
        """
        ...

    def remove_arrangement_overdub_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "arrangement_overdub".
        """
        ...

    def remove_back_to_arranger_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "back_to_arranger".
        """
        ...

    def remove_can_capture_midi_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "can_capture_midi".
        """
        ...

    def remove_can_jump_to_next_cue_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "can_jump_to_next_cue".
        """
        ...

    def remove_can_jump_to_prev_cue_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "can_jump_to_prev_cue".
        """
        ...

    def remove_clip_trigger_quantization_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "clip_trigger_quantization".
        """
        ...

    def remove_count_in_duration_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "count_in_duration".
        """
        ...

    def remove_cue_points_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "cue_points".
        """
        ...

    def remove_current_song_time_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "current_song_time".
        """
        ...

    def remove_data_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "data".
        """
        ...

    def remove_exclusive_arm_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "exclusive_arm".
        """
        ...

    def remove_groove_amount_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "groove_amount".
        """
        ...

    def remove_is_ableton_link_enabled_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "is_ableton_link_enabled".
        """
        ...

    def remove_is_ableton_link_start_stop_sync_enabled_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "is_ableton_link_start_stop_sync_enabled".
        """
        ...

    def remove_is_counting_in_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "is_counting_in".
        """
        ...

    def remove_is_playing_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "is_playing".
        """
        ...

    def remove_loop_length_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "loop_length".
        """
        ...

    def remove_loop_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "loop".
        """
        ...

    def remove_loop_start_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "loop_start".
        """
        ...

    def remove_metronome_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "metronome".
        """
        ...

    def remove_midi_recording_quantization_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "midi_recording_quantization".
        """
        ...

    def remove_nudge_down_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "nudge_down".
        """
        ...

    def remove_nudge_up_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "nudge_up".
        """
        ...

    def remove_overdub_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "overdub".
        """
        ...

    def remove_punch_in_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "punch_in".
        """
        ...

    def remove_punch_out_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "punch_out".
        """
        ...

    def remove_re_enable_automation_enabled_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "re_enable_automation_enabled".
        """
        ...

    def remove_record_mode_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "record_mode".
        """
        ...

    def remove_return_tracks_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "return_tracks".
        """
        ...

    def remove_root_note_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "root_note".
        """
        ...

    def remove_scale_information_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "scale_information".
        """
        ...

    def remove_scale_intervals_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "scale_intervals".
        """
        ...

    def remove_scale_mode_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "scale_mode".
        """
        ...

    def remove_scale_name_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "scale_name".
        """
        ...

    def remove_scenes_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "scenes".
        """
        ...

    def remove_session_automation_record_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "session_automation_record".
        """
        ...

    def remove_session_record_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "session_record".
        """
        ...

    def remove_session_record_status_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "session_record_status".
        """
        ...

    def remove_signature_denominator_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "signature_denominator".
        """
        ...

    def remove_signature_numerator_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "signature_numerator".
        """
        ...

    def remove_song_length_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "song_length".
        """
        ...

    def remove_start_time_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "start_time".
        """
        ...

    def remove_swing_amount_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "swing_amount".
        """
        ...

    def remove_tempo_follower_enabled_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "tempo_follower_enabled".
        """
        ...

    def remove_tempo_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "tempo".
        """
        ...

    def remove_tracks_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "tracks".
        """
        ...

    def remove_tuning_system_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "tuning_system".
        """
        ...

    def remove_visible_tracks_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "visible_tracks".
        """
        ...

    @property
    def return_tracks(self) -> Vector[Track]:
        """Const access to the list of available Return Tracks."""
        ...

    def return_tracks_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "return_tracks".
        """
        ...

    @property
    def root_note(self) -> int:
        """Set and access the root (i.e. key) of the song. The root can be a number between 0 and 11, with 0 corresponding to C and 11 corresponding to B."""
        ...

    @root_note.setter
    def root_note(self, value: int) -> None: ...

    def root_note_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "root_note".
        """
        ...

    def scale_information_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "scale_information".
        """
        ...

    @property
    def scale_intervals(self) -> IntVector:
        """Reports the current scale's intervals as a list of integers, starting with the root and representing the number of halfsteps (e.g. Major -> 0, 2, 4, 5, 7, 9, 11)"""
        ...

    def scale_intervals_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "scale_intervals".
        """
        ...

    @property
    def scale_mode(self) -> bool:
        """Access to the Scale Mode setting in Live. When on, key tracks that belong to the currently selected scale are highlighted in Live's MIDI Note Editor, and pitch-based parameters in MIDI Tools and Devices can be edited in scale degrees rather than semitones."""
        ...

    @scale_mode.setter
    def scale_mode(self, value: bool) -> None: ...

    def scale_mode_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "scale_mode".
        """
        ...

    @property
    def scale_name(self) -> str:
        """
        Set and access the currently selected scale by name. The default scale names that can be saved with a set and recalled are
        'Major', 'Minor', 'Dorian', 'Mixolydian' ,'Lydian' ,'Phrygian' ,'Locrian',
        'Whole Tone', 'Half-whole Dim.', 'Whole-half Dim.', 'Minor Blues',
        'Minor Pentatonic', 'Major Pentatonic', 'Harmonic Minor', 'Harmonic Major',
        'Dorian #4', 'Phrygian Dominant', 'Melodic Minor', 'Lydian Augmented',
        'Lydian Dominant', 'Super Locrian', 'Bhairav', 'Hungarian Minor',
        '8-Tone Spanish', 'Hirajoshi', 'In-Sen', 'Iwato', 'Kumoi', 'Pelog Selisir',
        'Pelog Tembung', 'Messiaen 3', 'Messiaen 4', 'Messiaen 5', 'Messiaen 6',
        'Messiaen 7'
        """
        ...

    @scale_name.setter
    def scale_name(self, value: str) -> None: ...

    def scale_name_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "scale_name".
        """
        ...

    @property
    def scenes(self) -> Vector[Scene]:
        """Const access to a list of all Scenes in the Live Song."""
        ...

    def scenes_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "scenes".
        """
        ...

    def scrub_by(self, beats: float | None) -> None:
        """Same as jump_by, but does not stop playback."""
        ...

    @property
    def select_on_launch(self) -> bool:
        """Get if Scenes and Clips should be selected when fired."""
        ...

    @property
    def session_automation_record(self) -> bool:
        """Returns true if automation recording is enabled."""
        ...

    @session_automation_record.setter
    def session_automation_record(self, value: bool) -> None: ...

    def session_automation_record_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "session_automation_record".
        """
        ...

    @property
    def session_record(self) -> bool:
        """Get/Set the session record state."""
        ...

    @session_record.setter
    def session_record(self, value: bool) -> None: ...

    def session_record_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "session_record".
        """
        ...

    @property
    def session_record_status(self) -> int:
        """Get the session slot-recording state."""
        ...

    def session_record_status_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "session_record_status".
        """
        ...

    def set_data(self, key: str | None, value: Any | None) -> None:
        """Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set."""
        ...

    def set_or_delete_cue(self) -> None:
        """
        When a cue is selected, it gets deleted. If no cue is selected,
        a new cue is created at the current global songtime.
        """
        ...

    @property
    def signature_denominator(self) -> int:
        """Get/Set access to the global signature denominator of the Song."""
        ...

    @signature_denominator.setter
    def signature_denominator(self, value: int) -> None: ...

    def signature_denominator_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "signature_denominator".
        """
        ...

    @property
    def signature_numerator(self) -> int:
        """Get/Set access to the global signature numerator of the Song."""
        ...

    @signature_numerator.setter
    def signature_numerator(self, value: int) -> None: ...

    def signature_numerator_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "signature_numerator".
        """
        ...

    @property
    def song_length(self) -> float:
        """
        Return the time of the last set event in the song, plus som extra beats
        that are usually added for better navigation in the arrangerview.
        """
        ...

    def song_length_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "song_length".
        """
        ...

    def start_playing(self) -> None:
        """Start playing from the startmarker"""
        ...

    @property
    def start_time(self) -> float:
        """
        Get/Set access to the songs current start time in beats. The set time
        may be overridden by the current loop/locator start time.
        """
        ...

    @start_time.setter
    def start_time(self, value: float) -> None: ...

    def start_time_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "start_time".
        """
        ...

    def stop_all_clips(self, quantized: bool = True) -> None:
        """Stop all playing Clips (if any) but continue playing the Song."""
        ...

    def stop_playing(self) -> None:
        """Stop playing the Song."""
        ...

    @property
    def swing_amount(self) -> float:
        """Get/Set access to the amount of swing that is applied when adding or quantizing notes to MIDI clips"""
        ...

    @swing_amount.setter
    def swing_amount(self, value: float) -> None: ...

    def swing_amount_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "swing_amount".
        """
        ...

    def tap_tempo(self) -> None:
        """Trigger the tap tempo function."""
        ...

    @property
    def tempo(self) -> float:
        """Get/Set the global project tempo."""
        ...

    @tempo.setter
    def tempo(self, value: float) -> None: ...

    @property
    def tempo_follower_enabled(self) -> bool:
        """Get/Set whether the Tempo Follower is controlling the tempo. The Tempo Follower Toggle must be made visible in the preferences for this property to be effective."""
        ...

    @tempo_follower_enabled.setter
    def tempo_follower_enabled(self, value: bool) -> None: ...

    def tempo_follower_enabled_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "tempo_follower_enabled".
        """
        ...

    def tempo_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "tempo".
        """
        ...

    @property
    def tracks(self) -> Vector[Track]:
        """
        Const access to a list of all Player Tracks in the Live Song, excluding
        the return and Main Track (see also Song.send_tracks and Song.master_track).
        At least one MIDI or Audio Track is always available.
        """
        ...

    def tracks_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "tracks".
        """
        ...

    def trigger_session_record(self, record_length: float = 1.7976931348623157e+308) -> None:
        """Triggers a new session recording."""
        ...

    @property
    def tuning_system(self) -> TuningSystem:
        """Access the currently active tuning system."""
        ...

    def tuning_system_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "tuning_system".
        """
        ...

    def undo(self) -> str:
        """Undo the last action that was made."""
        ...

    @property
    def view(self) -> View:
        """
        Representing the view aspects of a Live document:
        The Session and Arrangerview.
        """
        ...

    @property
    def visible_tracks(self) -> Vector[Track]:
        """
        Const access to a list of all visible Player Tracks in the Live Song, excluding
        the return and Main Track (see also Song.send_tracks and Song.master_track).
        At least one MIDI or Audio Track is always available.
        """
        ...

    def visible_tracks_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "visible_tracks".
        """
        ...

__all__ = ['Song']
