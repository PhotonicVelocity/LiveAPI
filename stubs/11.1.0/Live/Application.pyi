from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')

if TYPE_CHECKING:
    from Live.Base import StringVector, Vector
    from Live.Browser import Browser
    from Live.LomObject import LomObject
    from Live.Song import Song



class Application(LomObject):
    """This class represents the Live application."""

    class View(LomObject):
        """This class represents the view aspects of the Live application."""

        class NavDirection(int):
            up: int = 0
            down: int = 1
            left: int = 2
            right: int = 3

        @property
        def _live_ptr(self) -> int:
            ...

        def add_browse_mode_listener(self, callback: Callable | None, /) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "browse_mode" has changed.
            """
            ...

        def add_focused_document_view_listener(self, callback: Callable | None, /) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "focused_document_view" has changed.
            """
            ...

        def add_is_view_visible_listener(self, view_name: str | None, callback: Callable | None, /) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "is_view_visible" has changed.
            """
            ...

        def add_view_focus_changed_listener(self, callback: Callable | None, /) -> None:
            """
            Add a listener function or method, which will be called as soon as the
            property "view_focus_changed" has changed.
            """
            ...

        def available_main_views(self) -> StringVector:
            """
            Return a list of strings with the available subcomponent views, which
            is to be specified, when using the rest of this classes functions.
            A 'subcomponent view' is a main view component of a document view, like
            the Session view, the Arranger or Detailview and so on...
            """
            ...

        @property
        def browse_mode(self) -> bool:
            """Return true if HotSwap mode is active for any target."""
            ...

        def browse_mode_has_listener(self, callback: Callable | None, /) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "browse_mode".
            """
            ...

        @property
        def canonical_parent(self) -> Application:
            """Get the canonical parent of the application view."""
            ...

        def focus_view(self, view: str | None, /) -> None:
            """Show and focus one through the identifier string specified view."""
            ...

        @property
        def focused_document_view(self) -> str:
            """
            Return the name of the document view ('Session' or 'Arranger')
            shown in the currently selected window.
            """
            ...

        def focused_document_view_has_listener(self, callback: Callable | None, /) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "focused_document_view".
            """
            ...

        def hide_view(self, view_name: str | None, /) -> None:
            """Hide one through the identifier string specified view."""
            ...

        def is_view_visible(self, identifier: str | None, main_window_only: bool = True, /) -> bool:
            """
            Return true if the through the identifier string specified view is currently
            visible. If main_window_only is set to False, this will also check in second
            window. Notifications from the second window are not yet supported.
            """
            ...

        def is_view_visible_has_listener(self, view_name: str | None, callback: Callable | None, /) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "is_view_visible".
            """
            ...

        def remove_browse_mode_listener(self, callback: Callable | None, /) -> None:
            """
            Remove a previously set listener function or method from
            property "browse_mode".
            """
            ...

        def remove_focused_document_view_listener(self, callback: Callable | None, /) -> None:
            """
            Remove a previously set listener function or method from
            property "focused_document_view".
            """
            ...

        def remove_is_view_visible_listener(self, view_name: str | None, callback: Callable | None, /) -> None:
            """
            Remove a previously set listener function or method from
            property "is_view_visible".
            """
            ...

        def remove_view_focus_changed_listener(self, callback: Callable | None, /) -> None:
            """
            Remove a previously set listener function or method from
            property "view_focus_changed".
            """
            ...

        def scroll_view(self, direction: int | None, view_name: str | None, modifier_pressed: bool | None, /) -> None:
            """
            Scroll through the identifier string specified view into the given
            direction, if possible. Will silently return if the specified view
            can not perform the requested action.
            """
            ...

        def show_view(self, view: str | None, /) -> None:
            """
            Show one through the identifier string specified view. Will throw a
            runtime error if this is called in Live's initialization scope.
            """
            ...

        def toggle_browse(self) -> None:
            """
            Reveals the device chain, the browser and starts hot swap for
            the selected device. Calling this function again stops hot swap.
            """
            ...

        def view_focus_changed_has_listener(self, callback: Callable | None, /) -> bool:
            """
            Returns true, if the given listener function or method is connected
            to the property "view_focus_changed".
            """
            ...

        def zoom_view(self, direction: int | None, view_name: str | None, modifier_pressed: bool | None, /) -> None:
            """
            Zoom through the identifier string specified view into the given
            direction, if possible. Will silently return if the specified view
            can not perform the requested action.
            """
            ...

    def add_average_process_usage_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "average_process_usage" has changed.
        """
        ...

    def add_control_surfaces_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "control_surfaces" has changed.
        """
        ...

    def add_open_dialog_count_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "open_dialog_count" has changed.
        """
        ...

    def add_peak_process_usage_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "peak_process_usage" has changed.
        """
        ...

    def add_unavailable_features_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "unavailable_features" has changed.
        """
        ...

    @property
    def average_process_usage(self) -> float:
        """Reports Live's average CPU load."""
        ...

    def average_process_usage_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "average_process_usage".
        """
        ...

    @property
    def browser(self) -> Browser:
        """Returns an interface to the browser."""
        ...

    @property
    def canonical_parent(self) -> None:
        """Returns the canonical parent of the application."""
        ...

    @property
    def control_surfaces(self) -> Vector[object]:
        """
        Const access to a list of the control surfaces selected in preferences, in the same order.
        The list contains None if no control surface is active at that index.
        """
        ...

    def control_surfaces_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "control_surfaces".
        """
        ...

    @property
    def current_dialog_button_count(self) -> int:
        """Number of buttons on the current dialog."""
        ...

    @property
    def current_dialog_message(self) -> str:
        """Text of the last dialog that appeared; Empty if all dialogs just disappeared."""
        ...

    def get_bugfix_version(self) -> int:
        """Returns an integer representing the bugfix version of Live."""
        ...

    def get_document(self) -> Song:
        """Returns the current Live Set."""
        ...

    def get_major_version(self) -> int:
        """Returns an integer representing the major version of Live."""
        ...

    def get_minor_version(self) -> int:
        """Returns an integer representing the minor version of Live."""
        ...

    def has_option(self, option_name: str | None, /) -> bool:
        """Returns True if the given entry exists in Options.txt, False otherwise."""
        ...

    @property
    def open_dialog_count(self) -> int:
        """The number of open dialogs in Live. 0 if not dialog is open."""
        ...

    def open_dialog_count_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "open_dialog_count".
        """
        ...

    @property
    def peak_process_usage(self) -> float:
        """Reports Live's peak CPU load."""
        ...

    def peak_process_usage_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "peak_process_usage".
        """
        ...

    def press_current_dialog_button(self, index: int | None, /) -> None:
        """Press a button, by index, on the current message box."""
        ...

    def remove_average_process_usage_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "average_process_usage".
        """
        ...

    def remove_control_surfaces_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "control_surfaces".
        """
        ...

    def remove_open_dialog_count_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "open_dialog_count".
        """
        ...

    def remove_peak_process_usage_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "peak_process_usage".
        """
        ...

    def remove_unavailable_features_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "unavailable_features".
        """
        ...

    @property
    def unavailable_features(self) -> UnavailableFeatureVector:
        """List of features that are unavailable due to limitations of the current Live edition."""
        ...

    def unavailable_features_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "unavailable_features".
        """
        ...

    @property
    def view(self) -> View:
        """Returns the applications view component."""
        ...

class ControlDescription:
    """Describes a control present in a control surface proxy"""

    def __init__(self) -> None: ...

    @property
    def id(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

class ControlDescriptionVector(Vector[ControlDescription]):
    """A container for returning control descriptions."""

    def append(self, value: ControlDescription | None, /) -> None:
        ...

    def extend(self, values: Iterable[ControlDescription] | None, /) -> None:
        ...

class ControlSurfaceProxy:
    """Represents a control surface running in a different process. For use by M4L"""

    def add_control_values_arrived_listener(self, callback: Callable | None, /) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "control_values_arrived" has changed.
        """
        ...

    @property
    def control_descriptions(self) -> ControlDescriptionVector:
        ...

    def control_values_arrived_has_listener(self, callback: Callable | None, /) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "control_values_arrived".
        """
        ...

    def fetch_received_values(self) -> tuple[tuple[int, Any], ...]:
        ...

    def grab_control(self, control: int | None, /) -> None:
        ...

    def release_control(self, control: int | None, /) -> None:
        ...

    def remove_control_values_arrived_listener(self, callback: Callable | None, /) -> None:
        """
        Remove a previously set listener function or method from
        property "control_values_arrived".
        """
        ...

    def send_value(self, value: tuple[Any, ...] | None, /) -> None:
        ...

    @property
    def type_name(self) -> str:
        ...

class UnavailableFeature(int):
    note_velocity_ranges_and_probabilities: int = 0

class UnavailableFeatureVector(Vector[UnavailableFeature]):
    """A container for returning unavailable features."""

    def append(self, value: UnavailableFeature | None, /) -> None:
        ...

    def extend(self, values: Iterable[UnavailableFeature] | None, /) -> None:
        ...

def combine_apcs() -> bool:
    """Returns true if multiple APCs should be combined."""
    ...

def encrypt_challenge(dongle1: int | None, dongle2: int | None, key_index: int = 0, /) -> tuple[int, ...]:
    """Returns an encrypted challenge based on the TEA algortithm"""
    ...

def encrypt_challenge2(challenge: int | None, /) -> int:
    """Returns the UMAC hash for the given challenge."""
    ...

def get_application() -> Application:
    """Returns the application instance."""
    ...

def get_random_int(min_value: int | None, max_value: int | None, /) -> int:
    """Returns a random integer from the given range."""
    ...

__all__ = ['Application', 'ControlDescription', 'ControlDescriptionVector', 'ControlSurfaceProxy', 'UnavailableFeature', 'UnavailableFeatureVector', 'combine_apcs', 'encrypt_challenge', 'encrypt_challenge2', 'get_application', 'get_random_int']
