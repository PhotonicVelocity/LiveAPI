from types import ModuleType
from typing import Callable


class Scene(ModuleType):

    class Scene(object):
        def __init__(self, *a, **k):
            """
            This class represents an series of ClipSlots in Lives Sessionview matrix.
            """
            ...

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
            Get/set access to the color of the Scene (RGB).
            """
            ...

        @color.setter
        def color(self, value) -> None:
            ...

        @property
        def color_index(self) -> None:
            """
            Get/set access to the color index of the Scene. Can be None for no color.
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
            Get/Set the name of the scene. Might contain the substring BPM, whichidentifies that the scene will change the tempo when fired. To Get/Setthe temp, use the 'tempo' property of the scene.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def tempo(self) -> float:
            """
            Get/Set the tempo value of the scene.The Song will use the Scenes tempo as soon as the Scene is fired.Returns -1 if the Scene has no tempo property.
            """
            ...

        @tempo.setter
        def tempo(self, value) -> None:
            ...

        def add_clip_slots_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "clip_slots" has changed.
            """
            ...

        def add_color_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "color_index" has changed.
            """
            ...

        def add_color_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "color" has changed.
            """
            ...

        def add_is_triggered_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_triggered" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def clip_slots_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "clip_slots".
            """
            ...

        def color_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "color".
            """
            ...

        def color_index_has_listener(self, arg2: Callable) -> bool:
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

        def is_triggered_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_triggered".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def remove_clip_slots_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "clip_slots".
            """
            ...

        def remove_color_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "color_index".
            """
            ...

        def remove_color_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "color".
            """
            ...

        def remove_is_triggered_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_triggered".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def set_fire_button_state(self, arg2: bool) -> None:
            """
            Set the scene's fire button state directly. Supports all launch modes.
            """
            ...
