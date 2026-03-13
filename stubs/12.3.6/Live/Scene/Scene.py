from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from Live.Song import Song



class Scene:
    """
    This class represents an series of ClipSlots in Lives Sessionview matrix.
    """

    @property
    def _live_ptr(self) -> int:
        ...

    @property
    def canonical_parent(self) -> Song:
        """
        Get the canonical parent of the scene.
        """
        ...

    @property
    def clip_slots(self) -> tuple:
        """
        return a list of clipslots (see class AClipSlot) that this scene covers.
        """
        ...

    @property
    def color(self) -> int:
        """
        Get/set access to the color of the scene (RGB).
        """
        ...

    @color.setter
    def color(self, value) -> None:
        ...

    @property
    def color_index(self) -> None:
        """
        Get/set access to the color index of the scene. Can be None for no color.
        """
        ...

    @color_index.setter
    def color_index(self, value) -> None:
        ...

    @property
    def is_empty(self) -> bool:
        """
        Returns True if all clip slots of this scene are empty.
        """
        ...

    @property
    def is_triggered(self) -> bool:
        """
        Const access to the scene's trigger state.
        """
        ...

    @property
    def name(self) -> str:
        """
        Get/Set the name of the scene.
        """
        ...

    @name.setter
    def name(self, value) -> None:
        ...

    @property
    def tempo(self) -> float:
        """
        Get/Set the tempo value of the scene.The song will use the scene's tempo as soon as the scene is fired.Returns -1 if the scene has no tempo property.
        """
        ...

    @tempo.setter
    def tempo(self, value) -> None:
        ...

    @property
    def tempo_enabled(self) -> bool:
        """
        Get/Set the active state of the scene tempo.When disabled, the scene will use the song's tempo,and the tempo value returned will be -1Returns a bool indicating the state of the scene's tempo
        """
        ...

    @tempo_enabled.setter
    def tempo_enabled(self, value) -> None:
        ...

    @property
    def time_signature_denominator(self) -> int:
        """
        Get/Set the scene's time signature denominator.The song will use the scene's time signature as soon as the scene is fired.Returns -1 if the scene has no time signature property.
        """
        ...

    @time_signature_denominator.setter
    def time_signature_denominator(self, value) -> None:
        ...

    @property
    def time_signature_enabled(self) -> bool:
        """
        Get the active state of the scene time signature.When disabled, the scene will use the song's time signature,and the time signature values returned will be -1Returns a bool indicating the state of the scene's time signature
        """
        ...

    @time_signature_enabled.setter
    def time_signature_enabled(self, value) -> None:
        ...

    @property
    def time_signature_numerator(self) -> int:
        """
        Get/Set the scene's time signature numerator.The song will use the scene's time signature as soon as the scene is fired.Returns -1 if the scene has no time signature property.
        """
        ...

    @time_signature_numerator.setter
    def time_signature_numerator(self, value) -> None:
        ...

    def add_clip_slots_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "clip_slots" has changed.
        """
        ...

    def add_color_index_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "color_index" has changed.
        """
        ...

    def add_color_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "color" has changed.
        """
        ...

    def add_is_triggered_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "is_triggered" has changed.
        """
        ...

    def add_name_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "name" has changed.
        """
        ...

    def add_tempo_enabled_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "tempo_enabled" has changed.
        """
        ...

    def add_tempo_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "tempo" has changed.
        """
        ...

    def add_time_signature_denominator_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "time_signature_denominator" has changed.
        """
        ...

    def add_time_signature_enabled_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "time_signature_enabled" has changed.
        """
        ...

    def add_time_signature_numerator_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "time_signature_numerator" has changed.
        """
        ...

    def clip_slots_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "clip_slots".
        """
        ...

    def color_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "color".
        """
        ...

    def color_index_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "color_index".
        """
        ...

    def fire(self, force_legato: bool=False, can_select_scene_on_launch: bool=True) -> None:
        """
        Fire the scene directly. Will fire all clipslots that this scene owns and select the scene itself.
        """
        ...

    def fire_as_selected(self, force_legato: bool=False) -> None:
        """
        Fire the selected scene. Will fire all clipslots that this scene owns and select the next scene if necessary.
        """
        ...

    def is_triggered_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "is_triggered".
        """
        ...

    def name_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "name".
        """
        ...

    def remove_clip_slots_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "clip_slots".
        """
        ...

    def remove_color_index_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "color_index".
        """
        ...

    def remove_color_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "color".
        """
        ...

    def remove_is_triggered_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "is_triggered".
        """
        ...

    def remove_name_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "name".
        """
        ...

    def remove_tempo_enabled_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "tempo_enabled".
        """
        ...

    def remove_tempo_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "tempo".
        """
        ...

    def remove_time_signature_denominator_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "time_signature_denominator".
        """
        ...

    def remove_time_signature_enabled_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "time_signature_enabled".
        """
        ...

    def remove_time_signature_numerator_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "time_signature_numerator".
        """
        ...

    def set_fire_button_state(self, arg2: bool) -> None:
        """
        Set the scene's fire button state directly. Supports all launch modes.
        """
        ...

    def tempo_enabled_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "tempo_enabled".
        """
        ...

    def tempo_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "tempo".
        """
        ...

    def time_signature_denominator_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "time_signature_denominator".
        """
        ...

    def time_signature_enabled_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "time_signature_enabled".
        """
        ...

    def time_signature_numerator_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "time_signature_numerator".
        """
        ...


__all__ = ['Scene']
