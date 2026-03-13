from types import ModuleType
from typing import Callable


class Application(ModuleType):

    @staticmethod
    def combine_apcs() -> bool:
        """
        Returns true if multiple APCs should be combined.
        """
        ...

    @staticmethod
    def encrypt_challenge(dongle1: int, dongle2: int, key_index: int=0) -> tuple:
        """
        Returns an encrypted challenge based on the TEA algortithm
        """
        ...

    @staticmethod
    def encrypt_challenge2(arg1: int) -> int:
        """
        Returns the UMAC hash for the given challenge.
        """
        ...

    @staticmethod
    def get_application() -> Application:
        """
        Returns the application instance.
        """
        ...

    @staticmethod
    def get_random_int(arg1: int, arg2: int) -> int:
        """
        Returns a random integer from the given range.
        """
        ...

    class Application(object):
        def __init__(self, *a, **k):
            """
            This class represents the Live application.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def average_process_usage(self) -> float:
            """
            Reports Live's average CPU load.
            """
            ...

        @property
        def browser(self) -> Browser:
            """
            Returns an interface to the browser.
            """
            ...

        @property
        def canonical_parent(self) -> None:
            """
            Returns the canonical parent of the application.
            """
            ...

        @property
        def control_surfaces(self) -> tuple[object, ...]:
            """
            Const access to a list of the control surfaces selected in preferences, in the same order.The list contains None if no control surface is active at that index.
            """
            ...

        @property
        def current_dialog_button_count(self) -> int:
            """
            Number of buttons on the current dialog.
            """
            ...

        @property
        def current_dialog_message(self) -> str:
            """
            Text of the last dialog that appeared; Empty if all dialogs just disappeared.
            """
            ...

        @property
        def open_dialog_count(self) -> int:
            """
            The number of open dialogs in Live. 0 if not dialog is open.
            """
            ...

        @property
        def peak_process_usage(self) -> float:
            """
            Reports Live's peak CPU load.
            """
            ...

        @property
        def unavailable_features(self) -> tuple[UnavailableFeature, ...]:
            """
            List of features that are unavailable due to limitations of the current Live edition.
            """
            ...

        @property
        def view(self) -> View:
            """
            Returns the applications view component.
            """
            ...

        def add_average_process_usage_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "average_process_usage" has changed.
            """
            ...

        def add_control_surfaces_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "control_surfaces" has changed.
            """
            ...

        def add_open_dialog_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "open_dialog_count" has changed.
            """
            ...

        def add_peak_process_usage_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "peak_process_usage" has changed.
            """
            ...

        def add_unavailable_features_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "unavailable_features" has changed.
            """
            ...

        def average_process_usage_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "average_process_usage".
            """
            ...

        def control_surfaces_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "control_surfaces".
            """
            ...

        def get_bugfix_version(self) -> int:
            """
            Returns an integer representing the bugfix version of Live.
            """
            ...

        def get_document(self) -> Song:
            """
            Returns the current Live Set.
            """
            ...

        def get_major_version(self) -> int:
            """
            Returns an integer representing the major version of Live.
            """
            ...

        def get_minor_version(self) -> int:
            """
            Returns an integer representing the minor version of Live.
            """
            ...

        def has_option(self, arg2: object) -> bool:
            """
            Returns True if the given entry exists in Options.txt, False otherwise.
            """
            ...

        def open_dialog_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "open_dialog_count".
            """
            ...

        def peak_process_usage_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "peak_process_usage".
            """
            ...

        def press_current_dialog_button(self, arg2: int) -> None:
            """
            Press a button, by index, on the current message box.
            """
            ...

        def remove_average_process_usage_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "average_process_usage".
            """
            ...

        def remove_control_surfaces_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "control_surfaces".
            """
            ...

        def remove_open_dialog_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "open_dialog_count".
            """
            ...

        def remove_peak_process_usage_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "peak_process_usage".
            """
            ...

        def remove_unavailable_features_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "unavailable_features".
            """
            ...

        def unavailable_features_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "unavailable_features".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                This class represents the view aspects of the Live application.
                """
                ...

            @property
            def _live_ptr(self):
                ...

            @property
            def browse_mode(self):
                """
                Return true if HotSwap mode is active for any target.
                """
                ...

            @property
            def canonical_parent(self):
                """
                Get the canonical parent of the application view.
                """
                ...

            @property
            def focused_document_view(self):
                """
                Return the name of the document view ('Session' or 'Arranger')shown in the currently selected window.
                """
                ...

            def add_browse_mode_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "browse_mode" has changed.
                """
                ...

            def add_focused_document_view_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "focused_document_view" has changed.
                """
                ...

            def add_is_view_visible_listener(self, arg2: Callable, arg3: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_view_visible" has changed.
                """
                ...

            def add_view_focus_changed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "view_focus_changed" has changed.
                """
                ...

            def available_main_views(self) -> StringVector:
                """
                Return a list of strings with the available subcomponent views, which is to be specified, when using the rest of this classes functions. A 'subcomponent view' is a main view component of a document view, like the Session view, the Arranger or Detailview and so on...
                """
                ...

            def browse_mode_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "browse_mode".
                """
                ...

            def focus_view(self, arg2: object) -> None:
                """
                Show and focus one through the identifier string specified view.
                """
                ...

            def focused_document_view_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "focused_document_view".
                """
                ...

            def hide_view(self, arg2: object) -> None:
                """
                Hide one through the identifier string specified view.
                """
                ...

            def is_view_visible(self, identifier: object, main_window_only: bool=True) -> bool:
                """
                Return true if the through the identifier string specified view is currently visible. If main_window_only is set to False, this will also check in second window. Notifications from the second window are not yet supported.
                """
                ...

            def is_view_visible_has_listener(self, arg2: Callable, arg3: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_view_visible".
                """
                ...

            def remove_browse_mode_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "browse_mode".
                """
                ...

            def remove_focused_document_view_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "focused_document_view".
                """
                ...

            def remove_is_view_visible_listener(self, arg2: Callable, arg3: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_view_visible".
                """
                ...

            def remove_view_focus_changed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "view_focus_changed".
                """
                ...

            def scroll_view(self, arg2: int, arg3: object, arg4: bool) -> None:
                """
                Scroll through the identifier string specified view into the given direction, if possible.  Will silently return if the specified view can not perform the requested action.
                """
                ...

            def show_view(self, arg2: object) -> None:
                """
                Show one through the identifier string specified view. Will throw a runtime error if this is called in Live's initialization scope.
                """
                ...

            def toggle_browse(self) -> None:
                """
                Reveals the device chain, the browser and starts hot swap for the selected device. Calling this function again stops hot swap.
                """
                ...

            def view_focus_changed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "view_focus_changed".
                """
                ...

            def zoom_view(self, arg2: int, arg3: object, arg4: bool) -> None:
                """
                Zoom through the identifier string specified view into the given direction, if possible.  Will silently return if the specified view can not perform the requested action.
                """
                ...

            class NavDirection:
                up: int = 0
                down: int = 1
                left: int = 2
                right: int = 3

    class ControlDescription(object):
        def __init__(self, *a, **k):
            """
            Describes a control present in a control surface proxy
            """
            ...

        @property
        def id(self):
            ...

        @property
        def name(self):
            ...

    class ControlDescriptionVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning control descriptions.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class ControlSurfaceProxy(object):
        def __init__(self, *a, **k):
            """
            Represents a control surface running in a different process. For use by M4L
            """
            ...

        @property
        def control_descriptions(self):
            ...

        @property
        def type_name(self):
            ...

        def add_control_values_arrived_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "control_values_arrived" has changed.
            """
            ...

        def control_values_arrived_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "control_values_arrived".
            """
            ...

        def fetch_received_values(self) -> tuple:
            ...

        def grab_control(self, arg2: int) -> None:
            ...

        def release_control(self, arg2: int) -> None:
            ...

        def remove_control_values_arrived_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "control_values_arrived".
            """
            ...

        def send_value(self, arg2: tuple) -> None:
            ...

    class UnavailableFeature:
        note_velocity_ranges_and_probabilities: int = 0

    class UnavailableFeatureVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning unavailable features.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...
