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
        def number_of_push_apps_running(self) -> int:
            """
            Returns the number of connected Push apps.
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

        def get_build_id(self) -> str:
            """
            Returns a string identifying the build.
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

        def get_variant(self) -> str:
            """
            Returns one of the strings in Live.Application.Variants.
            """
            ...

        def get_version_string(self) -> str:
            """
            Returns the full version string of Live.
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

        def show_message(self, text: Text, buttons: int=Application.MessageButtons.OK_BUTTON, enable_markup: bool=False, show_success_icon: bool=False) -> int:
            """
            Shows a message box, returning the position of the pressed button.
            """
            ...

        def show_on_the_fly_message(self, message: str, buttons: int=Application.MessageButtons.OK_BUTTON, enable_markup: bool=False, show_success_icon: bool=False, push_dialog_type: int=Application.PushDialogType.MESSAGE_BOX) -> int:
            """
            Same as show_message, but for when there is no predefined Text object.
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
        def pad_layout(self):
            """
            The layout of pads on Push.
            """
            ...

        @property
        def type_name(self):
            ...

        def add_control_values_arrived_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "control_values_arrived" has changed.
            """
            ...

        def add_midi_received_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_received" has changed.
            """
            ...

        def add_pad_layout_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pad_layout" has changed.
            """
            ...

        def control_values_arrived_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "control_values_arrived".
            """
            ...

        def enable_receive_midi(self, arg2: bool) -> None:
            ...

        def fetch_received_midi_messages(self) -> tuple:
            ...

        def fetch_received_values(self) -> tuple:
            ...

        def grab_control(self, arg2: int) -> None:
            ...

        def midi_received_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_received".
            """
            ...

        def pad_layout_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pad_layout".
            """
            ...

        def release_control(self, arg2: int) -> None:
            ...

        def remove_control_values_arrived_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "control_values_arrived".
            """
            ...

        def remove_midi_received_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_received".
            """
            ...

        def remove_pad_layout_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pad_layout".
            """
            ...

        def send_midi(self, arg2: tuple) -> None:
            ...

        def send_value(self, arg2: tuple) -> None:
            ...

        def subscribe_to_control(self, arg2: int) -> None:
            ...

        def unsubscribe_from_control(self, arg2: int) -> None:
            ...

    class MessageButtons:
        """
        Specifies the characteristics of the message box, e.g. which buttons to show.
        """
        OK_BUTTON: int = 0
        OK_NEW_SET_BUTTON: int = 1
        OK_RETRY_BUTTON: int = 2
        SAVE_DONT_SAVE_BUTTON: int = 3
        OK_ACCOUNT_BUTTON: int = 4
        OK_PURCHASE_BUTTON: int = 5

    class PushDialogType:
        """
        Specifies the dialog type for Push.
        """
        MESSAGE_BOX: int = 0
        OUT_OF_UNLOCKS_DIALOG: int = 5
        RENT_TO_OWN_LICENSE_EXPIRED_DIALOG: int = 7

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

    class Variants(object):
        def __init__(self, *a, **k):
            """
            Holds strings representing what type of Live is running.
            """
            ...


class Base(ModuleType):

    @staticmethod
    def get_text(classname: str, textname: str) -> Text:
        """
        Retrieves the (translated) Text identified by `classname` and `textname`.
        """
        ...

    @staticmethod
    def log(arg1: str) -> None:
        ...

    @staticmethod
    def subst_args(text: Text, arg1: str='', arg2: str='', arg3: str='', arg4: str='', arg5: str='') -> str:
        ...

    class FloatVector(object):
        def __init__(self, *a, **k):
            """
            A simple container for returning floats from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class IntU64Vector(object):
        def __init__(self, *a, **k):
            """
            A simple container for returning unsigned long integers from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class IntVector(object):
        def __init__(self, *a, **k):
            """
            A simple container for returning integers from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class LimitationError(object):
        def __init__(self, *a, **k):
            ...

    class ObjectVector(object):
        def __init__(self, *a, **k):
            """
            A simple read only container for returning python objects.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class StringVector(object):
        def __init__(self, *a, **k):
            """
            A simple container for returning strings from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class Text(object):
        def __init__(self, *a, **k):
            """
            A translatable, immutable string.
            """
            ...

        @property
        def text(self):
            ...

    class Timer(object):
        def __init__(self, *a, **k):
            """
            A timer that will trigger a callback after a certain inverval. The timer can be repeated and will trigger the callback every interval. Errors in the callback will stop the timer.
            """
            ...

        @property
        def running(self) -> bool:
            ...

        def restart(self) -> None:
            ...

        def start(self) -> None:
            ...

        def stop(self) -> None:
            ...

    class Vector(object):
        def __init__(self, *a, **k):
            """
            A simple read only container for returning objects from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...


class Browser(ModuleType):

    class Browser(object):
        def __init__(self, *a, **k):
            """
            This class represents the live browser data base.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def audio_effects(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Audio Effects content.
            """
            ...

        @property
        def clips(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Clips content.
            """
            ...

        @property
        def colors(self) -> tuple[BrowserItem, ...]:
            """
            Returns a list of browser items containing the configured colors.
            """
            ...

        @property
        def current_project(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Current Project content.
            """
            ...

        @property
        def drums(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Drums content.
            """
            ...

        @property
        def filter_type(self) -> int:
            """
            Bang triggered when the hotswap target has changed.
            """
            ...

        @filter_type.setter
        def filter_type(self, value) -> None:
            ...

        @property
        def hotswap_target(self) -> None:
            """
            Bang triggered when the hotswap target has changed.
            """
            ...

        @hotswap_target.setter
        def hotswap_target(self, value) -> None:
            ...

        @property
        def instruments(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Instruments content.
            """
            ...

        @property
        def legacy_libraries(self) -> tuple[BrowserItem, ...]:
            """
            Returns a list of browser items containing the installed legacy libraries. The list is always empty as legacy library handling has been removed.
            """
            ...

        @property
        def max_for_live(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Max For Live content.
            """
            ...

        @property
        def midi_effects(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Midi Effects content.
            """
            ...

        @property
        def packs(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Packs content.
            """
            ...

        @property
        def plugins(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Plugins content.
            """
            ...

        @property
        def samples(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Samples content.
            """
            ...

        @property
        def sounds(self) -> BrowserItem:
            """
            Returns a browser item with access to all the Sounds content.
            """
            ...

        @property
        def user_folders(self) -> tuple[BrowserItem, ...]:
            """
            Returns a list of browser items containing all the user folders.
            """
            ...

        @property
        def user_library(self) -> BrowserItem:
            """
            Returns a browser item with access to all the User Library content.
            """
            ...

        def add_filter_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "filter_type" has changed.
            """
            ...

        def add_full_refresh_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "full_refresh" has changed.
            """
            ...

        def add_hotswap_target_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "hotswap_target" has changed.
            """
            ...

        def filter_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "filter_type".
            """
            ...

        def full_refresh_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "full_refresh".
            """
            ...

        def hotswap_target_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "hotswap_target".
            """
            ...

        def load_item(self, arg2: BrowserItem) -> None:
            """
            Loads the provided browser item.
            """
            ...

        def preview_item(self, arg2: BrowserItem) -> None:
            """
            Previews the provided browser item.
            """
            ...

        def relation_to_hotswap_target(self, arg2: BrowserItem) -> Relation:
            """
            Returns the relation between the given browser item and the current hotswap target
            """
            ...

        def remove_filter_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "filter_type".
            """
            ...

        def remove_full_refresh_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "full_refresh".
            """
            ...

        def remove_hotswap_target_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "hotswap_target".
            """
            ...

        def stop_preview(self) -> None:
            """
            Stop the current preview.
            """
            ...

    class BrowserItem(object):
        def __init__(self, *a, **k):
            """
            This class represents an item of the browser hierarchy.
            """
            ...

        @property
        def children(self) -> tuple[BrowserItem, ...]:
            """
            Const access to the descendants of this browser item.
            """
            ...

        @property
        def is_device(self) -> bool:
            """
            Indicates if the browser item represents a device.
            """
            ...

        @property
        def is_folder(self) -> bool:
            """
            Indicates if the browser item represents folder.
            """
            ...

        @property
        def is_loadable(self) -> bool:
            """
            True if item can be loaded via the Browser's 'load_item' method.
            """
            ...

        @property
        def is_selected(self) -> bool:
            """
            True if the item is ancestor of or the actual selection.
            """
            ...

        @property
        def iter_children(self) -> BrowserItemIterator:
            """
            Const iterable access to the descendants of this browser item.
            """
            ...

        @property
        def name(self) -> str:
            """
            Const access to the canonical display name of this browser item.
            """
            ...

        @property
        def source(self) -> str:
            """
            Specifies where does item come from -- i.e. Live pack, user library...
            """
            ...

        @property
        def uri(self) -> str:
            """
            The uri describes a unique identifier for a browser item.
            """
            ...

    class BrowserItemIterator(object):
        def __init__(self, *a, **k):
            """
            This class iterates over children of another BrowserItem.
            """
            ...

    class BrowserItemVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning browser items from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class FilterType:
        disabled: int = -1
        hotswap_off: int = 0
        instrument_hotswap: int = 1
        audio_effect_hotswap: int = 2
        midi_effect_hotswap: int = 3
        drum_pad_hotswap: int = 4
        midi_track_devices: int = 5
        samples: int = 6
        count: int = 7

    class Relation:
        ancestor: int = 0
        equal: int = 1
        descendant: int = 2
        none: int = 3


class CcControlDevice(ModuleType):

    class CcControlDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a CcControl device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def custom_bool_target(self) -> int:
            """
            Return the custom bool target
            """
            ...

        @custom_bool_target.setter
        def custom_bool_target(self, value) -> None:
            ...

        @property
        def custom_bool_target_list(self) -> tuple[str, ...]:
            """
            Return the custom bool target list
            """
            ...

        @property
        def custom_float_target_0(self) -> int:
            """
            Return the custom float target 0
            """
            ...

        @custom_float_target_0.setter
        def custom_float_target_0(self, value) -> None:
            ...

        @property
        def custom_float_target_0_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 0 list
            """
            ...

        @property
        def custom_float_target_1(self) -> int:
            """
            Return the custom float target 1
            """
            ...

        @custom_float_target_1.setter
        def custom_float_target_1(self, value) -> None:
            ...

        @property
        def custom_float_target_10(self) -> int:
            """
            Return the custom float target 10
            """
            ...

        @custom_float_target_10.setter
        def custom_float_target_10(self, value) -> None:
            ...

        @property
        def custom_float_target_10_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 10 list
            """
            ...

        @property
        def custom_float_target_11(self) -> int:
            """
            Return the custom float target 11
            """
            ...

        @custom_float_target_11.setter
        def custom_float_target_11(self, value) -> None:
            ...

        @property
        def custom_float_target_11_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 11 list
            """
            ...

        @property
        def custom_float_target_1_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 1 list
            """
            ...

        @property
        def custom_float_target_2(self) -> int:
            """
            Return the custom float target 2
            """
            ...

        @custom_float_target_2.setter
        def custom_float_target_2(self, value) -> None:
            ...

        @property
        def custom_float_target_2_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 2 list
            """
            ...

        @property
        def custom_float_target_3(self) -> int:
            """
            Return the custom float target 3
            """
            ...

        @custom_float_target_3.setter
        def custom_float_target_3(self, value) -> None:
            ...

        @property
        def custom_float_target_3_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 3 list
            """
            ...

        @property
        def custom_float_target_4(self) -> int:
            """
            Return the custom float target 4
            """
            ...

        @custom_float_target_4.setter
        def custom_float_target_4(self, value) -> None:
            ...

        @property
        def custom_float_target_4_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 4 list
            """
            ...

        @property
        def custom_float_target_5(self) -> int:
            """
            Return the custom float target 5
            """
            ...

        @custom_float_target_5.setter
        def custom_float_target_5(self, value) -> None:
            ...

        @property
        def custom_float_target_5_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 5 list
            """
            ...

        @property
        def custom_float_target_6(self) -> int:
            """
            Return the custom float target 6
            """
            ...

        @custom_float_target_6.setter
        def custom_float_target_6(self, value) -> None:
            ...

        @property
        def custom_float_target_6_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 6 list
            """
            ...

        @property
        def custom_float_target_7(self) -> int:
            """
            Return the custom float target 7
            """
            ...

        @custom_float_target_7.setter
        def custom_float_target_7(self, value) -> None:
            ...

        @property
        def custom_float_target_7_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 7 list
            """
            ...

        @property
        def custom_float_target_8(self) -> int:
            """
            Return the custom float target 8
            """
            ...

        @custom_float_target_8.setter
        def custom_float_target_8(self, value) -> None:
            ...

        @property
        def custom_float_target_8_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 8 list
            """
            ...

        @property
        def custom_float_target_9(self) -> int:
            """
            Return the custom float target 9
            """
            ...

        @custom_float_target_9.setter
        def custom_float_target_9(self, value) -> None:
            ...

        @property
        def custom_float_target_9_list(self) -> tuple[str, ...]:
            """
            Return the custom float target 9 list
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_custom_bool_target_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_bool_target" has changed.
            """
            ...

        def add_custom_float_target_0_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_0" has changed.
            """
            ...

        def add_custom_float_target_10_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_10" has changed.
            """
            ...

        def add_custom_float_target_11_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_11" has changed.
            """
            ...

        def add_custom_float_target_1_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_1" has changed.
            """
            ...

        def add_custom_float_target_2_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_2" has changed.
            """
            ...

        def add_custom_float_target_3_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_3" has changed.
            """
            ...

        def add_custom_float_target_4_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_4" has changed.
            """
            ...

        def add_custom_float_target_5_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_5" has changed.
            """
            ...

        def add_custom_float_target_6_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_6" has changed.
            """
            ...

        def add_custom_float_target_7_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_7" has changed.
            """
            ...

        def add_custom_float_target_8_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_8" has changed.
            """
            ...

        def add_custom_float_target_9_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "custom_float_target_9" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def custom_bool_target_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_bool_target".
            """
            ...

        def custom_float_target_0_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_0".
            """
            ...

        def custom_float_target_10_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_10".
            """
            ...

        def custom_float_target_11_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_11".
            """
            ...

        def custom_float_target_1_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_1".
            """
            ...

        def custom_float_target_2_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_2".
            """
            ...

        def custom_float_target_3_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_3".
            """
            ...

        def custom_float_target_4_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_4".
            """
            ...

        def custom_float_target_5_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_5".
            """
            ...

        def custom_float_target_6_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_6".
            """
            ...

        def custom_float_target_7_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_7".
            """
            ...

        def custom_float_target_8_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_8".
            """
            ...

        def custom_float_target_9_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "custom_float_target_9".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_custom_bool_target_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_bool_target".
            """
            ...

        def remove_custom_float_target_0_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_0".
            """
            ...

        def remove_custom_float_target_10_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_10".
            """
            ...

        def remove_custom_float_target_11_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_11".
            """
            ...

        def remove_custom_float_target_1_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_1".
            """
            ...

        def remove_custom_float_target_2_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_2".
            """
            ...

        def remove_custom_float_target_3_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_3".
            """
            ...

        def remove_custom_float_target_4_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_4".
            """
            ...

        def remove_custom_float_target_5_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_5".
            """
            ...

        def remove_custom_float_target_6_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_6".
            """
            ...

        def remove_custom_float_target_7_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_7".
            """
            ...

        def remove_custom_float_target_8_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_8".
            """
            ...

        def remove_custom_float_target_9_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "custom_float_target_9".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def resend(self) -> None:
            """
            Resend all CC values.
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> CcControlDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class Chain(ModuleType):

    class Chain(object):
        def __init__(self, *a, **k):
            """
            This class represents a group device chain in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> RackDevice:
            """
            Get the canonical parent of the chain.
            """
            ...

        @property
        def color(self) -> int:
            """
            Access the color index of the Chain.
            """
            ...

        @color.setter
        def color(self, value) -> None:
            ...

        @property
        def color_index(self) -> int:
            """
            Access the color index of the Chain.
            """
            ...

        @color_index.setter
        def color_index(self, value) -> None:
            ...

        @property
        def devices(self) -> tuple:
            """
            Return const access to all available Devices that are present in the chains
            """
            ...

        @property
        def has_audio_input(self) -> bool:
            """
            return True, if this Chain can be feed with an Audio signal. This istrue for all Audio Chains.
            """
            ...

        @property
        def has_audio_output(self) -> bool:
            """
            return True, if this Chain sends out an Audio signal. This istrue for all Audio Chains, and MIDI chains with an Instrument.
            """
            ...

        @property
        def has_midi_input(self) -> bool:
            """
            return True, if this Chain can be feed with an Audio signal. This istrue for all MIDI Chains.
            """
            ...

        @property
        def has_midi_output(self) -> bool:
            """
            return True, if this Chain sends out MIDI events. This istrue for all MIDI Chains with no Instruments.
            """
            ...

        @property
        def is_auto_colored(self) -> bool:
            """
            Get/set access to the auto color flag of the Chain.If True, the Chain will always have the same color as the containingTrack or Chain.
            """
            ...

        @is_auto_colored.setter
        def is_auto_colored(self, value) -> None:
            ...

        @property
        def mixer_device(self) -> ChainMixerDevice:
            """
            Return access to the mixer device that holds the chain's mixer parameters:the Volume, Pan, and Sendamounts.
            """
            ...

        @property
        def mute(self) -> bool:
            """
            Mute/unmute the chain.
            """
            ...

        @mute.setter
        def mute(self, value) -> None:
            ...

        @property
        def muted_via_solo(self) -> bool:
            """
            Return const access to whether this chain is muted due to some other chainbeing soloed.
            """
            ...

        @property
        def name(self) -> str:
            """
            Read/write access to the name of the Chain, as visible in the track header.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def solo(self) -> bool:
            """
            Get/Set the solo status of the chain. Note that this will not disable thesolo state of any other Chain in the same rack. If you want exclusive solo, you have to disable the solo state of the other Chains manually.
            """
            ...

        @solo.setter
        def solo(self, value) -> None:
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

        def add_devices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "devices" has changed.
            """
            ...

        def add_is_auto_colored_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_auto_colored" has changed.
            """
            ...

        def add_mute_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mute" has changed.
            """
            ...

        def add_muted_via_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "muted_via_solo" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "solo" has changed.
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

        def delete_device(self, arg2: int) -> None:
            """
            Remove a device identified by its index from the chain. Throws runtime error if bad index.
            """
            ...

        def devices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "devices".
            """
            ...

        def duplicate_device(self, arg2: int) -> None:
            """
            Duplicate the device at the given index in the chain.
            """
            ...

        def insert_device(self, DeviceName: str, DeviceIndex: int=-1) -> LomObject:
            """
            Add a device at a given index in the chain. At end if -1.
            """
            ...

        def is_auto_colored_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_auto_colored".
            """
            ...

        def mute_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mute".
            """
            ...

        def muted_via_solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "muted_via_solo".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
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

        def remove_devices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "devices".
            """
            ...

        def remove_is_auto_colored_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_auto_colored".
            """
            ...

        def remove_mute_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mute".
            """
            ...

        def remove_muted_via_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "muted_via_solo".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "solo".
            """
            ...

        def solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "solo".
            """
            ...


class ChainMixerDevice(ModuleType):

    class ChainMixerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Chain's Mixer Device in Live, which gives youaccess to the Volume, Panning, and Send properties of a Chain.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Chain:
            """
            Get the canonical parent of the mixer device.
            """
            ...

        @property
        def chain_activator(self) -> DeviceParameter:
            """
            Const access to the Chain's Activator Device Parameter.
            """
            ...

        @property
        def panning(self) -> DeviceParameter:
            """
            Const access to the Chain's Panning Device Parameter.
            """
            ...

        @property
        def sends(self) -> tuple:
            """
            Const access to the Chain's list of Send Amount Device Parameters.
            """
            ...

        @property
        def volume(self) -> DeviceParameter:
            """
            Const access to the Chain's Volume Device Parameter.
            """
            ...

        def add_sends_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "sends" has changed.
            """
            ...

        def remove_sends_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "sends".
            """
            ...

        def sends_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sends".
            """
            ...


class Clip(ModuleType):

    class Clip(object):
        def __init__(self, *a, **k):
            """
            This class represents a Clip in Live. It can be either an AudioClip or a MIDI Clip, in an Arrangement or the Session, dependingon the Track (Slot) it lives in.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def automation_envelopes(self) -> tuple:
            """
            Const access to a list of all automation envelopes for this clip.
            """
            ...

        @property
        def available_warp_modes(self) -> tuple[int, ...]:
            """
            Available for AudioClips only.Get/Set the available warp modes, that can be used.
            """
            ...

        @property
        def canonical_parent(self) -> ClipSlot:
            """
            Get the canonical parent of the Clip.
            """
            ...

        @property
        def color(self) -> int:
            """
            Get/set access to the color of the Clip (RGB).
            """
            ...

        @color.setter
        def color(self, value) -> None:
            ...

        @property
        def color_index(self) -> int:
            """
            Get/set access to the color index of the Clip.
            """
            ...

        @color_index.setter
        def color_index(self, value) -> None:
            ...

        @property
        def end_marker(self) -> float:
            """
            Get/Set the Clips end marker pos in beats/seconds (unit depends on warping).
            """
            ...

        @end_marker.setter
        def end_marker(self, value) -> None:
            ...

        @property
        def end_time(self) -> float:
            """
            Get the clip's end time.
            """
            ...

        @property
        def file_path(self) -> str:
            """
            Get the path of the file represented by the Audio Clip.
            """
            ...

        @property
        def gain(self) -> float:
            """
            Available for AudioClips only.Read/write access to the gain setting of theAudio Clip
            """
            ...

        @gain.setter
        def gain(self, value) -> None:
            ...

        @property
        def gain_display_string(self) -> str:
            """
            Return a string with the gain as dB value
            """
            ...

        @property
        def groove(self) -> None:
            """
            Get the groove associated with this clip.
            """
            ...

        @groove.setter
        def groove(self, value) -> None:
            ...

        @property
        def has_envelopes(self) -> bool:
            """
            Will notify if the clip gets his first envelope or the last envelope is removed.
            """
            ...

        @property
        def has_groove(self) -> bool:
            """
            Returns true if a groove is associated with this clip.
            """
            ...

        @property
        def is_arrangement_clip(self) -> bool:
            """
            return true if this Clip is an Arrangement Clip.A Clip can be either a Session or Arrangement Clip.
            """
            ...

        @property
        def is_audio_clip(self) -> bool:
            """
            Return true if this Clip is an Audio Clip.A Clip can be either an Audioclip or a MIDI Clip.
            """
            ...

        @property
        def is_midi_clip(self) -> bool:
            """
            return true if this Clip is a MIDI Clip.A Clip can be either an Audioclip or a MIDI Clip.
            """
            ...

        @property
        def is_overdubbing(self) -> bool:
            """
            returns true if the Clip is recording overdubs
            """
            ...

        @property
        def is_playing(self) -> bool:
            """
            Get/Set if this Clip is currently playing. If the Clips trigger modeis set to a quantization value, the Clip will not start playing immediately.If you need to know wether the Clip was triggered, use the is_triggered property.
            """
            ...

        @is_playing.setter
        def is_playing(self, value) -> None:
            ...

        @property
        def is_recording(self) -> bool:
            """
            returns true if the Clip was triggered to record or is recording.
            """
            ...

        @property
        def is_session_clip(self) -> bool:
            """
            return true if this Clip is a Session Clip.A Clip can be either a Session or Arrangement Clip.
            """
            ...

        @property
        def is_take_lane_clip(self) -> bool:
            """
            return true if this Clip is a Take Lane Clip.A Take Lane Clip is also always an Arrangement Clip.
            """
            ...

        @property
        def is_triggered(self) -> bool:
            """
            returns true if the Clip was triggered or is playing.
            """
            ...

        @property
        def launch_mode(self) -> int:
            """
            Get/Set access to the launch mode setting of the Clip.
            """
            ...

        @launch_mode.setter
        def launch_mode(self, value) -> None:
            ...

        @property
        def launch_quantization(self) -> int:
            """
            Get/Set access to the launch quantization setting of the Clip.
            """
            ...

        @launch_quantization.setter
        def launch_quantization(self, value) -> None:
            ...

        @property
        def legato(self) -> bool:
            """
            Get/Set access to the legato setting of the Clip
            """
            ...

        @legato.setter
        def legato(self, value) -> None:
            ...

        @property
        def length(self) -> float:
            """
            Get to the Clips length in beats/seconds (unit depends on warping).
            """
            ...

        @property
        def loop_end(self) -> float:
            """
            Get/Set the loop end pos of this Clip in beats/seconds (unit depends on warping).
            """
            ...

        @loop_end.setter
        def loop_end(self, value) -> None:
            ...

        @property
        def loop_start(self) -> float:
            """
            Get/Set the Clips loopstart pos in beats/seconds (unit depends on warping).
            """
            ...

        @loop_start.setter
        def loop_start(self, value) -> None:
            ...

        @property
        def looping(self) -> bool:
            """
            Get/Set the Clips 'loop is enabled' flag.Only Warped Audio Clips or MIDI Clip can be looped.
            """
            ...

        @looping.setter
        def looping(self, value) -> None:
            ...

        @property
        def muted(self) -> bool:
            """
            Read/write access to the mute state of the Clip.
            """
            ...

        @muted.setter
        def muted(self, value) -> None:
            ...

        @property
        def name(self) -> str:
            """
            Read/write access to the name of the Clip.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def pitch_coarse(self) -> int:
            """
            Available for AudioClips only.Read/write access to the pitch (in halftones) setting of theAudio Clip, ranging from -48 to 48
            """
            ...

        @pitch_coarse.setter
        def pitch_coarse(self, value) -> None:
            ...

        @property
        def pitch_fine(self) -> float:
            """
            Available for AudioClips only.Read/write access to the pitch fine setting of theAudio Clip, ranging from -500 to 500
            """
            ...

        @pitch_fine.setter
        def pitch_fine(self, value) -> None:
            ...

        @property
        def playing_position(self) -> float:
            """
            Constant access to the current playing position of the clip.The returned value is the position in beats for midi and warped audio clips,or in seconds for unwarped audio clips. Stopped clips will return 0.
            """
            ...

        @property
        def position(self) -> float:
            """
            Get/Set the loop position of this Clip in beats/seconds (unit depends on warping).
            """
            ...

        @position.setter
        def position(self, value) -> None:
            ...

        @property
        def ram_mode(self) -> bool:
            """
            Available for AudioClips only.Read/write access to the Ram mode setting of the Audio Clip
            """
            ...

        @ram_mode.setter
        def ram_mode(self, value) -> None:
            ...

        @property
        def sample_length(self) -> int:
            """
            Available for AudioClips only.Get the sample length in sample time or -1 if there is no sample available.
            """
            ...

        @property
        def sample_rate(self) -> float:
            """
            Available for AudioClips only.Read-only access to the Clip's sampling rate.
            """
            ...

        @property
        def signature_denominator(self) -> int:
            """
            Get/Set access to the global signature denominator of the Clip.
            """
            ...

        @signature_denominator.setter
        def signature_denominator(self, value) -> None:
            ...

        @property
        def signature_numerator(self) -> int:
            """
            Get/Set access to the global signature numerator of the Clip.
            """
            ...

        @signature_numerator.setter
        def signature_numerator(self, value) -> None:
            ...

        @property
        def start_marker(self) -> float:
            """
            Get/Set the Clips start marker pos in beats/seconds (unit depends on warping).
            """
            ...

        @start_marker.setter
        def start_marker(self, value) -> None:
            ...

        @property
        def start_time(self) -> float:
            """
            Get the clip's start time offset. For Session View clips, this is the time the clip was started. For Arrangement View clips, this is the offset within the arrangement.
            """
            ...

        @property
        def velocity_amount(self) -> float:
            """
            Get/Set access to the velocity to volume amount of the Clip.
            """
            ...

        @velocity_amount.setter
        def velocity_amount(self, value) -> None:
            ...

        @property
        def view(self) -> View:
            """
            Get the view of the Clip.
            """
            ...

        @property
        def warp_markers(self) -> tuple[WarpMarker, ...]:
            """
            Available for AudioClips only.Get the warp markers for this audio clip.
            """
            ...

        @property
        def warp_mode(self) -> int:
            """
            Available for AudioClips only.Get/Set the warp mode for this audio clip.
            """
            ...

        @warp_mode.setter
        def warp_mode(self, value) -> None:
            ...

        @property
        def warping(self) -> bool:
            """
            Available for AudioClips only.Get/Set if this Clip is timestreched.
            """
            ...

        @warping.setter
        def warping(self, value) -> None:
            ...

        @property
        def will_record_on_start(self) -> bool:
            """
            returns true if the Clip will record on being started.
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

        def add_end_marker_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "end_marker" has changed.
            """
            ...

        def add_end_time_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "end_time" has changed.
            """
            ...

        def add_file_path_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "file_path" has changed.
            """
            ...

        def add_gain_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "gain" has changed.
            """
            ...

        def add_groove_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "groove" has changed.
            """
            ...

        def add_has_envelopes_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_envelopes" has changed.
            """
            ...

        def add_is_overdubbing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_overdubbing" has changed.
            """
            ...

        def add_is_recording_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_recording" has changed.
            """
            ...

        def add_launch_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "launch_mode" has changed.
            """
            ...

        def add_launch_quantization_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "launch_quantization" has changed.
            """
            ...

        def add_legato_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "legato" has changed.
            """
            ...

        def add_loop_end_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "loop_end" has changed.
            """
            ...

        def add_loop_jump_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "loop_jump" has changed.
            """
            ...

        def add_loop_start_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "loop_start" has changed.
            """
            ...

        def add_looping_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "looping" has changed.
            """
            ...

        def add_muted_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "muted" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_new_notes(self, arg2: object) -> IntU64Vector:
            """
            Expects a Python iterable holding a number of Live.Clip.MidiNoteSpecification objects. The objects will be used to construct new notes in the clip.
            """
            ...

        def add_notes_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "notes" has changed.
            """
            ...

        def add_pitch_coarse_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_coarse" has changed.
            """
            ...

        def add_pitch_fine_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_fine" has changed.
            """
            ...

        def add_playing_position_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_position" has changed.
            """
            ...

        def add_playing_status_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_status" has changed.
            """
            ...

        def add_position_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "position" has changed.
            """
            ...

        def add_ram_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "ram_mode" has changed.
            """
            ...

        def add_signature_denominator_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "signature_denominator" has changed.
            """
            ...

        def add_signature_numerator_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "signature_numerator" has changed.
            """
            ...

        def add_start_marker_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "start_marker" has changed.
            """
            ...

        def add_start_time_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "start_time" has changed.
            """
            ...

        def add_velocity_amount_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "velocity_amount" has changed.
            """
            ...

        def add_warp_marker(self, warp_marker: object) -> None:
            """
            Available for AudioClips only. Adds the specified warp marker, if possible.
            """
            ...

        def add_warp_markers_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warp_markers" has changed.
            """
            ...

        def add_warp_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warp_mode" has changed.
            """
            ...

        def add_warping_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warping" has changed.
            """
            ...

        def apply_note_modifications(self, arg2: MidiNoteVector) -> None:
            """
            Expects a list of notes as returned from get_notes_extended. The content of the list will be used to modify existing notes in the clip, based on matching note IDs. This function should be used when modifying existing notes, e.g. changing the velocity or start time. The function ensures that per-note events attached to the modified notes are preserved. This is NOT the case when replacing notes via a combination of remove_notes_extended and add_new_notes. The given list can be a subset of the notes in the clip, but it must not contain any notes that are not present in the clip.
            """
            ...

        def automation_envelope(self, arg2: DeviceParameter) -> Envelope:
            """
            Return the envelope for the given parameter.Returns None if the envelope doesn't exist.Returns None for Arrangement clips.Returns None for parameters from a different track.
            """
            ...

        def beat_to_sample_time(self, beat_time: float) -> float:
            """
            Available for AudioClips only. Converts the given beat time to sample time. Raises an error if the sample is not warped.
            """
            ...

        def clear_all_envelopes(self) -> None:
            """
            Clears all envelopes for this clip.
            """
            ...

        def clear_envelope(self, arg2: DeviceParameter) -> None:
            """
            Clears the envelope of this clips given parameter.
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

        def create_automation_envelope(self, arg2: DeviceParameter) -> Envelope:
            """
            Creates an envelope for a given parameter and returns it.This should only be used if the envelope doesn't exist.Raises an error if the envelope can't be created.
            """
            ...

        def crop(self) -> None:
            """
            Crops the clip. The region that is cropped depends on whether the clip is looped or not. If looped, the region outside of the loop is removed. If not looped, the region outside the start and end markers is removed.
            """
            ...

        def deselect_all_notes(self) -> None:
            """
            De-selects all notes present in the clip.
            """
            ...

        def duplicate_loop(self) -> None:
            """
            Make the loop two times longer and duplicates notes and envelopes. Duplicates the clip start/end range if the clip is not looped.
            """
            ...

        def duplicate_notes_by_id(self, note_ids: object, destination_time: object=None, transposition_amount: int=0) -> IntU64Vector:
            """
            Duplicate all notes matching the given note IDs. If the optional destination_time is not provided, new notes will be inserted after the last selected note. This behavior can be observed when duplicating notes in the Live GUI. If the transposition_amount is specified, the notes in the region will be transposed by the number of semitones. Raises an error on audio clips.
            """
            ...

        def duplicate_region(self, region_start: float, region_length: float, destination_time: float, pitch: int=-1, transposition_amount: int=0) -> None:
            """
            Duplicate the notes in the specified region to the destination_time. Only notes of the specified pitch are duplicated or all if pitch is -1. If the transposition_amount is not 0, the notes in the region will be transposed by the transpose_amount of semitones.Raises an error on audio clips.
            """
            ...

        def end_marker_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "end_marker".
            """
            ...

        def end_time_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "end_time".
            """
            ...

        def file_path_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "file_path".
            """
            ...

        def fire(self) -> None:
            """
            (Re)Start playing this Clip.
            """
            ...

        def gain_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "gain".
            """
            ...

        def get_all_notes_extended(self) -> MidiNoteVector:
            """
            Returns a list of all MIDI notes from the clip, regardless of their position relative to the start and end markers/loop start and loop end. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.
            """
            ...

        def get_notes(self, from_time: float, from_pitch: int, time_span: float, pitch_span: int) -> tuple:
            """
            Returns a tuple of tuples where each inner tuple represents a note starting in the given pitch- and time range. The inner tuple contains pitch, time, duration, velocity, and mute state.
            """
            ...

        def get_notes_by_id(self, note_ids: object) -> MidiNoteVector:
            """
            Return a list of MIDI notes matching the given note IDs.
            """
            ...

        def get_notes_extended(self, from_pitch: int, pitch_span: int, from_time: float, time_span: float) -> MidiNoteVector:
            """
            Returns a list of MIDI notes from the given pitch and time range. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.
            """
            ...

        def get_selected_notes(self) -> tuple:
            """
            Returns a tuple of tuples where each inner tuple represents a selected note. The inner tuple contains pitch, time, duration, velocity, and mute state.
            """
            ...

        def get_selected_notes_extended(self) -> MidiNoteVector:
            """
            Returns a list of all MIDI notes from the clip that are currently selected. Each note is represented by a Live.Clip.MidiNote object. The returned list can be modified freely, but modifications will not be reflected in the MIDI clip until apply_note_modifications is called.
            """
            ...

        def groove_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "groove".
            """
            ...

        def has_envelopes_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_envelopes".
            """
            ...

        def is_overdubbing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_overdubbing".
            """
            ...

        def is_recording_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_recording".
            """
            ...

        def launch_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "launch_mode".
            """
            ...

        def launch_quantization_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "launch_quantization".
            """
            ...

        def legato_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "legato".
            """
            ...

        def loop_end_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "loop_end".
            """
            ...

        def loop_jump_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "loop_jump".
            """
            ...

        def loop_start_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "loop_start".
            """
            ...

        def looping_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "looping".
            """
            ...

        def move_playing_pos(self, arg2: float) -> None:
            """
            Jump forward or backward by the specified relative amount in beats. Will do nothing, if the Clip is not playing.
            """
            ...

        def move_warp_marker(self, marker_beat_time: float, beat_time_distance: float) -> None:
            """
            Available for AudioClips only. Moves the specified warp marker by the specified beat time amount, if possible.
            """
            ...

        def muted_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "muted".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def note_number_to_name(self, midi_pitch: int) -> str:
            """
            Return a human-readable name for the given MIDI note number. Takes into account the scale and tonal spelling settings of the clip, as well as the current tuning system (if any)
            """
            ...

        def notes_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "notes".
            """
            ...

        def pitch_coarse_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_coarse".
            """
            ...

        def pitch_fine_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_fine".
            """
            ...

        def playing_position_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_position".
            """
            ...

        def playing_status_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_status".
            """
            ...

        def position_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "position".
            """
            ...

        def quantize(self, arg2: int, arg3: float) -> None:
            """
            Quantize all notes in a clip or align warp markers.
            """
            ...

        def quantize_pitch(self, arg2: int, arg3: int, arg4: float) -> None:
            """
            Quantize all the notes of a given pitch.  Raises an error on audio clips.
            """
            ...

        def ram_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "ram_mode".
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

        def remove_end_marker_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "end_marker".
            """
            ...

        def remove_end_time_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "end_time".
            """
            ...

        def remove_file_path_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "file_path".
            """
            ...

        def remove_gain_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "gain".
            """
            ...

        def remove_groove_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "groove".
            """
            ...

        def remove_has_envelopes_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_envelopes".
            """
            ...

        def remove_is_overdubbing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_overdubbing".
            """
            ...

        def remove_is_recording_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_recording".
            """
            ...

        def remove_launch_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "launch_mode".
            """
            ...

        def remove_launch_quantization_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "launch_quantization".
            """
            ...

        def remove_legato_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "legato".
            """
            ...

        def remove_loop_end_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "loop_end".
            """
            ...

        def remove_loop_jump_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "loop_jump".
            """
            ...

        def remove_loop_start_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "loop_start".
            """
            ...

        def remove_looping_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "looping".
            """
            ...

        def remove_muted_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "muted".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_notes(self, arg2: float, arg3: int, arg4: float, arg5: int) -> None:
            """
            Delete all notes starting in the given pitch- and time range.
            """
            ...

        def remove_notes_by_id(self, arg2: object) -> None:
            """
            Delete all notes matching the given note IDs. This function should NOT be used to implement modification of existing notes (i.e. in combination with add_new_notes), as that leads to loss of per-note events. apply_note_modifications must be used instead for modifying existing notes.
            """
            ...

        def remove_notes_extended(self, from_pitch: int, pitch_span: int, from_time: float, time_span: float) -> None:
            """
            Delete all notes starting in the given pitch and time range. This function should NOT be used to implement modification of existing notes (i.e. in combination with add_new_notes), as that leads to loss of per-note events. apply_note_modifications must be used instead for modifying existing notes.
            """
            ...

        def remove_notes_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "notes".
            """
            ...

        def remove_pitch_coarse_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_coarse".
            """
            ...

        def remove_pitch_fine_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_fine".
            """
            ...

        def remove_playing_position_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_position".
            """
            ...

        def remove_playing_status_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_status".
            """
            ...

        def remove_position_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "position".
            """
            ...

        def remove_ram_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "ram_mode".
            """
            ...

        def remove_signature_denominator_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "signature_denominator".
            """
            ...

        def remove_signature_numerator_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "signature_numerator".
            """
            ...

        def remove_start_marker_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "start_marker".
            """
            ...

        def remove_start_time_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "start_time".
            """
            ...

        def remove_velocity_amount_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "velocity_amount".
            """
            ...

        def remove_warp_marker(self, beat_time: float) -> None:
            """
            Available for AudioClips only. Removes the specified warp marker, if possible.
            """
            ...

        def remove_warp_markers_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warp_markers".
            """
            ...

        def remove_warp_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warp_mode".
            """
            ...

        def remove_warping_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warping".
            """
            ...

        def replace_selected_notes(self, arg2: tuple) -> None:
            """
            Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_selected_notes. The notes described that way will then be used to replace the old selection.
            """
            ...

        def sample_to_beat_time(self, sample_time: float) -> float:
            """
            Available for AudioClips only. Converts the given sample time to beat time. Raises an error if the sample is not warped.
            """
            ...

        def scrub(self, scrub_position: float) -> None:
            """
            Scrubs inside a clip. scrub_position defines the position in beats that the scrub will start from. The scrub will continue until stop_scrub is called. Global quantization applies to the scrub's position and length.
            """
            ...

        def seconds_to_sample_time(self, seconds: float) -> float:
            """
            Available for AudioClips only. Converts the given seconds to sample time. Raises an error if the sample is warped.
            """
            ...

        def select_all_notes(self) -> None:
            """
            Selects all notes present in the clip.
            """
            ...

        def select_notes_by_id(self, arg2: object) -> None:
            """
            Selects all notes matching the given note IDs.
            """
            ...

        def set_fire_button_state(self, arg2: bool) -> None:
            """
            Set the clip's fire button state directly. Supports all launch modes.
            """
            ...

        def set_notes(self, arg2: tuple) -> None:
            """
            Called with a tuple of tuples where each inner tuple represents a note in the same format as returned by get_notes. The notes described that way will then be added to the clip.
            """
            ...

        def signature_denominator_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "signature_denominator".
            """
            ...

        def signature_numerator_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "signature_numerator".
            """
            ...

        def start_marker_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "start_marker".
            """
            ...

        def start_time_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "start_time".
            """
            ...

        def stop(self) -> None:
            """
            Stop playing this Clip.
            """
            ...

        def stop_scrub(self) -> None:
            """
            Stops the current scrub.
            """
            ...

        def velocity_amount_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "velocity_amount".
            """
            ...

        def warp_markers_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warp_markers".
            """
            ...

        def warp_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warp_mode".
            """
            ...

        def warping_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warping".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a Clip.
                """
                ...

            @property
            def _live_ptr(self):
                ...

            @property
            def canonical_parent(self):
                """
                Get the canonical parent of the clip view.
                """
                ...

            @property
            def grid_is_triplet(self):
                """
                Get/set wether the grid is showing in triplet mode.
                """
                ...

            @property
            def grid_quantization(self):
                """
                Get/set clip grid quantization resolution.
                """
                ...

            def hide_envelope(self) -> None:
                """
                Hide the envelope view.
                """
                ...

            def select_envelope_parameter(self, arg2: DeviceParameter) -> None:
                """
                Select the given device parameter in the envelope view.
                """
                ...

            def show_envelope(self) -> None:
                """
                Show the envelope view.
                """
                ...

            def show_loop(self) -> None:
                """
                Show the entire loop in the detail view.
                """
                ...

    class ClipLaunchQuantization:
        q_global: int = 0
        q_none: int = 1
        q_8_bars: int = 2
        q_4_bars: int = 3
        q_2_bars: int = 4
        q_bar: int = 5
        q_half: int = 6
        q_half_triplet: int = 7
        q_quarter: int = 8
        q_quarter_triplet: int = 9
        q_eighth: int = 10
        q_eighth_triplet: int = 11
        q_sixteenth: int = 12
        q_sixteenth_triplet: int = 13
        q_thirtysecond: int = 14

    class GridQuantization:
        no_grid: int = 0
        g_8_bars: int = 1
        g_4_bars: int = 2
        g_2_bars: int = 3
        g_bar: int = 4
        g_half: int = 5
        g_quarter: int = 6
        g_eighth: int = 7
        g_sixteenth: int = 8
        g_thirtysecond: int = 9
        count: int = 10

    class LaunchMode:
        trigger: int = 0
        gate: int = 1
        toggle: int = 2
        repeat: int = 3

    class MidiNote(object):
        def __init__(self, *a, **k):
            """
            An object representing a MIDI Note
            """
            ...

        @property
        def duration(self) -> float:
            ...

        @duration.setter
        def duration(self, value) -> None:
            ...

        @property
        def mute(self) -> bool:
            ...

        @mute.setter
        def mute(self, value) -> None:
            ...

        @property
        def note_id(self) -> int:
            """
            A numerical ID that's unique within the originating clip of the note. Not to beused directly, but important for other API calls, namely apply_note_modifications.
            """
            ...

        @property
        def pitch(self) -> int:
            ...

        @pitch.setter
        def pitch(self, value) -> None:
            ...

        @property
        def probability(self) -> float:
            ...

        @probability.setter
        def probability(self, value) -> None:
            ...

        @property
        def release_velocity(self) -> float:
            ...

        @release_velocity.setter
        def release_velocity(self, value) -> None:
            ...

        @property
        def start_time(self) -> float:
            ...

        @start_time.setter
        def start_time(self, value) -> None:
            ...

        @property
        def velocity(self) -> float:
            ...

        @velocity.setter
        def velocity(self, value) -> None:
            ...

        @property
        def velocity_deviation(self) -> float:
            ...

        @velocity_deviation.setter
        def velocity_deviation(self, value) -> None:
            ...

    class MidiNoteSpecification(object):
        def __init__(self, *a, **k):
            """
            An object specifying the data for creating a MIDI note. To be used with the add_new_notes function.
            """
            ...

    class MidiNoteVector(object):
        def __init__(self, *a, **k):
            """
            A container for holding MIDI notes from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class WarpMarker(object):
        def __init__(self, *a, **k):
            """
            This class represents a WarpMarker type.
            """
            ...

        @property
        def beat_time(self) -> float:
            """
            A WarpMarker's beat time.
            """
            ...

        @property
        def sample_time(self) -> float:
            """
            A WarpMarker's sample time.
            """
            ...

    class WarpMarkerVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning warp markers from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class WarpMode:
        beats: int = 0
        tones: int = 1
        texture: int = 2
        repitch: int = 3
        complex: int = 4
        rex: int = 5
        complex_pro: int = 6
        count: int = 7


class ClipSlot(ModuleType):

    class ClipSlot(object):
        def __init__(self, *a, **k):
            """
            This class represents an entry in Lives Session view matrix.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the ClipSlot.
            """
            ...

        @property
        def clip(self) -> Clip:
            """
            Returns the Clip which this clipslots currently owns. Might be None.
            """
            ...

        @property
        def color(self) -> None:
            """
            Returns the canonical color for the clip slot or None if it does not exist.
            """
            ...

        @property
        def color_index(self) -> None:
            """
            Returns the canonical color index for the clip slot or None if it does not exist.
            """
            ...

        @property
        def controls_other_clips(self) -> bool:
            """
            Returns true if firing this slot will fire clips in other slots.Can only be true for slots in group tracks.
            """
            ...

        @property
        def has_clip(self) -> bool:
            """
            Returns true if this Clipslot owns a Clip.
            """
            ...

        @property
        def has_stop_button(self) -> bool:
            """
            Get/Set if this Clip has a stop button, which will, if fired, stop anyother Clip that is currently playing the Track we do belong to.
            """
            ...

        @has_stop_button.setter
        def has_stop_button(self, value) -> None:
            ...

        @property
        def is_group_slot(self) -> bool:
            """
            Returns whether this clip slot is a group track slot (group slot).
            """
            ...

        @property
        def is_playing(self) -> bool:
            """
            Returns whether the clip associated with the slot is playing.
            """
            ...

        @property
        def is_recording(self) -> bool:
            """
            Returns whether the clip associated with the slot is recording.
            """
            ...

        @property
        def is_triggered(self) -> bool:
            """
            Const access to the triggering state of the clip slot.
            """
            ...

        @property
        def playing_status(self) -> ClipSlotPlayingState:
            """
            Const access to the playing state of the clip slot.Can be either stopped, playing, or recording.
            """
            ...

        @property
        def will_record_on_start(self) -> bool:
            """
            returns true if the clip slot will record on being fired.
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

        def add_controls_other_clips_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "controls_other_clips" has changed.
            """
            ...

        def add_has_clip_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_clip" has changed.
            """
            ...

        def add_has_stop_button_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_stop_button" has changed.
            """
            ...

        def add_is_triggered_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_triggered" has changed.
            """
            ...

        def add_playing_status_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_status" has changed.
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

        def controls_other_clips_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "controls_other_clips".
            """
            ...

        def create_audio_clip(self, arg2: object) -> Clip:
            """
            Creates an audio clip referencing the file at the given absolute path in the slot. Throws an error when called on non-empty slots or slots in non-audio or frozen tracks, or when the path doesn't point at a valid audio file.
            """
            ...

        def create_clip(self, arg2: float) -> Clip:
            """
            Creates an empty clip with the given length in the slot. Throws an error when called on non-empty slots or slots in non-MIDI tracks.
            """
            ...

        def delete_clip(self) -> None:
            """
            Removes the clip contained in the slot. Raises an exception if the slot was empty.
            """
            ...

        def duplicate_clip_to(self, arg2: ClipSlot) -> None:
            """
            Duplicates the slot's clip to the passed in target slot. Overrides the target's clip if it's not empty. Raises an exception if the (source) slot itself is empty, or if source and target have different track types (audio vs. MIDI). Also raises if the source or target slot is in a group track (so called group slot).
            """
            ...

        def fire(self) -> None:
            """
            Fire a Clip if this Clipslot owns one, else trigger the stop button, if we have one.
            """
            ...

        def has_clip_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_clip".
            """
            ...

        def has_stop_button_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_stop_button".
            """
            ...

        def is_triggered_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_triggered".
            """
            ...

        def playing_status_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_status".
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

        def remove_controls_other_clips_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "controls_other_clips".
            """
            ...

        def remove_has_clip_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_clip".
            """
            ...

        def remove_has_stop_button_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_stop_button".
            """
            ...

        def remove_is_triggered_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_triggered".
            """
            ...

        def remove_playing_status_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_status".
            """
            ...

        def set_fire_button_state(self, arg2: bool) -> None:
            """
            Set the clipslot's fire button state directly. Supports all launch modes.
            """
            ...

        def stop(self) -> None:
            """
            Stop playing the contained Clip, if there is a Clip and its currently playing.
            """
            ...

    class ClipSlotPlayingState:
        stopped: int = 0
        started: int = 1
        recording: int = 2


class CompressorDevice(ModuleType):

    class CompressorDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Compressor device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def available_input_routing_channels(self) -> tuple[RoutingChannel, ...]:
            """
            Return a list of source channels for input routing in the sidechain.
            """
            ...

        @property
        def available_input_routing_types(self) -> tuple[RoutingType, ...]:
            """
            Return a list of source types for input routing in the sidechain.
            """
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def input_routing_channel(self) -> RoutingChannel:
            """
            Get and set the current source channel for input routing in the sidechain.Raises ValueError if the channel isn't one of the current values inavailable_input_routing_channels.
            """
            ...

        @input_routing_channel.setter
        def input_routing_channel(self, value) -> None:
            ...

        @property
        def input_routing_type(self) -> RoutingType:
            """
            Get and set the current source type for input routing in the sidechain.Raises ValueError if the type isn't one of the current values inavailable_input_routing_types.
            """
            ...

        @input_routing_type.setter
        def input_routing_type(self, value) -> None:
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_available_input_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_input_routing_channels" has changed.
            """
            ...

        def add_available_input_routing_types_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_input_routing_types" has changed.
            """
            ...

        def add_input_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routing_channel" has changed.
            """
            ...

        def add_input_routing_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routing_type" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def available_input_routing_channels_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_input_routing_channels".
            """
            ...

        def available_input_routing_types_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_input_routing_types".
            """
            ...

        def input_routing_channel_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routing_channel".
            """
            ...

        def input_routing_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routing_type".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_available_input_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_input_routing_channels".
            """
            ...

        def remove_available_input_routing_types_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_input_routing_types".
            """
            ...

        def remove_input_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routing_channel".
            """
            ...

        def remove_input_routing_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routing_type".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> CompressorDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class Conversions(ModuleType):

    @staticmethod
    def audio_to_midi_clip(song: Song, audio_clip: Clip, audio_to_midi_type: int) -> None:
        """
        Creates a MIDI clip in a new MIDI track with the notes extracted from the given audio_clip. The `audio_to_midi_type` decides which algorithm is used in the process. Raises error when called with an inconvertible clip or invalid `audio_to_midi_type`.
        """
        ...

    @staticmethod
    def create_drum_rack_from_audio_clip(song: Song, audio_clip: Clip) -> None:
        """
        Creates a new track with a drum rack with a simpler on the first pad with the specified audio clip.
        """
        ...

    @staticmethod
    def create_midi_track_from_drum_pad(song: Song, drum_pad: DrumPad) -> None:
        """
        Creates a new Midi track containing the specified Drum Pad's device chain.
        """
        ...

    @staticmethod
    def create_midi_track_with_simpler(song: Song, audio_clip: Clip) -> None:
        """
        Creates a new Midi track with a simpler including the specified audio clip.
        """
        ...

    @staticmethod
    def is_convertible_to_midi(song: Song, audio_clip: Clip) -> bool:
        """
        Returns whether `audio_clip` can be converted to MIDI. Raises error when called with a MIDI clip
        """
        ...

    @staticmethod
    def move_devices_on_track_to_new_drum_rack_pad(song: Song, track_index: int) -> LomObject:
        """
        Moves the entire device chain of the track according to the track index onto the C1 (note 36) drum pad of a new drum rack in a new track.If the track associated with the track index does not contain any devices nothing changes (i.e. a new track and new drum rack are not created).
        """
        ...

    @staticmethod
    def sliced_simpler_to_drum_rack(song: Song, simpler: SimplerDevice) -> None:
        """
        Converts the Simpler into a Drum Rack, assigning each slice to a drum pad. Calling it on a non-sliced simpler raises an error.
        """
        ...

    class AudioToMidiType:
        harmony_to_midi: int = 0
        melody_to_midi: int = 1
        drums_to_midi: int = 2


class Device(ModuleType):

    class ATimeableValueVector(object):
        def __init__(self, *a, **k):
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class Device(object):
        def __init__(self, *a, **k):
            """
            This class represents a MIDI or Audio DSP-Device in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> Device:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...

    class DeviceType:
        """
        The type of the device.
        """
        undefined: int = 0
        instrument: int = 1
        audio_effect: int = 2
        midi_effect: int = 4


class DeviceIO(ModuleType):

    class DeviceIO(object):
        def __init__(self, *a, **k):
            """
            This class represents a specific input or output bus of a device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def available_routing_channels(self) -> tuple[RoutingChannel, ...]:
            """
            Return a list of channels for this IO endpoint.
            """
            ...

        @property
        def available_routing_types(self) -> tuple[RoutingType, ...]:
            """
            Return a list of available routing types for this IO endpoint.
            """
            ...

        @property
        def canonical_parent(self) -> MaxDevice:
            """
            Get the canonical parent of the device IO.
            """
            ...

        @property
        def default_external_routing_channel_is_none(self) -> bool:
            """
            Get and set whether the default routing channel for External routing types is none.
            """
            ...

        @default_external_routing_channel_is_none.setter
        def default_external_routing_channel_is_none(self, value) -> None:
            ...

        @property
        def routing_channel(self) -> RoutingChannel:
            """
            Get and set the current routing channel.Raises ValueError if the channel isn't one of the current values inavailable_routing_channels.
            """
            ...

        @routing_channel.setter
        def routing_channel(self, value) -> None:
            ...

        @property
        def routing_type(self) -> RoutingType:
            """
            Get and set the current routing type.Raises ValueError if the type isn't one of the current values inavailable_routing_types.
            """
            ...

        @routing_type.setter
        def routing_type(self, value) -> None:
            ...

        def add_available_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_routing_channels" has changed.
            """
            ...

        def add_available_routing_types_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_routing_types" has changed.
            """
            ...

        def add_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "routing_channel" has changed.
            """
            ...

        def add_routing_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "routing_type" has changed.
            """
            ...

        def available_routing_channels_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_routing_channels".
            """
            ...

        def available_routing_types_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_routing_types".
            """
            ...

        def remove_available_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_routing_channels".
            """
            ...

        def remove_available_routing_types_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_routing_types".
            """
            ...

        def remove_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "routing_channel".
            """
            ...

        def remove_routing_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "routing_type".
            """
            ...

        def routing_channel_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "routing_channel".
            """
            ...

        def routing_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "routing_type".
            """
            ...


class DeviceParameter(ModuleType):

    class AutomationState:
        none: int = 0
        playing: int = 1
        overridden: int = 2

    class DeviceParameter(object):
        def __init__(self, *a, **k):
            """
            This class represents a (automatable) parameter within a MIDI orAudio DSP-Device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def automation_state(self) -> int:
            """
            Returns state of type AutomationState.
            """
            ...

        @property
        def canonical_parent(self) -> MixerDevice:
            """
            Get the canonical parent of the device parameter.
            """
            ...

        @property
        def default_value(self) -> float:
            """
            Return the default value for this parameter.  A Default value is onlyavailable for non-quantized parameter types (see 'is_quantized').
            """
            ...

        @property
        def display_value(self) -> float:
            """
            Get/Set the current value (as visible in the GUI) this parameter.The value must be inside the min/max properties of this device.
            """
            ...

        @display_value.setter
        def display_value(self, value) -> None:
            ...

        @property
        def is_enabled(self) -> bool:
            """
            Returns false if the parameter has been macro mapped or disabled by Max.
            """
            ...

        @property
        def is_quantized(self) -> bool:
            """
            Returns True, if this value is a boolean or integer like switch.Non quantized values are continues float values.
            """
            ...

        @property
        def max(self) -> float:
            """
            Returns const access to the upper value of the allowed range forthis parameter
            """
            ...

        @property
        def min(self) -> float:
            """
            Returns const access to the lower value of the allowed range forthis parameter
            """
            ...

        @property
        def name(self) -> str:
            """
            Returns const access the name of this parameter, as visible in Livesautomation choosers.
            """
            ...

        @property
        def original_name(self) -> str:
            """
            Returns const access the original name of this parameter, unaffected ofany renamings.
            """
            ...

        @property
        def short_value_items(self) -> tuple[str, ...]:
            """
            Return the list of possible values for this parameter. Like value_items, but prefers short value names if available. Raises an error if 'is_quantized' is False.
            """
            ...

        @property
        def state(self) -> int:
            """
            Returns the state of the parameter:- enabled - the parameter's value can be changed,- irrelevant - the parameter is enabled, but value changes will not take any effect until it gets enabled,- disabled - the parameter's value cannot be changed.
            """
            ...

        @property
        def value(self) -> float:
            """
            Get/Set the current internal value of this parameter.The value must be inside the min/max properties of this device.
            """
            ...

        @value.setter
        def value(self, value) -> None:
            ...

        @property
        def value_items(self) -> tuple[str, ...]:
            """
            Return the list of possible values for this parameter. Raises an error if 'is_quantized' is False.
            """
            ...

        def add_automation_state_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "automation_state" has changed.
            """
            ...

        def add_display_value_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "display_value" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_state_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "state" has changed.
            """
            ...

        def add_value_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "value" has changed.
            """
            ...

        def automation_state_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "automation_state".
            """
            ...

        def begin_gesture(self) -> None:
            """
            Notify the begin of a modification of the parameter, when a sequence of modifications have to be consider a consistent group -- for Sexample, when recording automation.
            """
            ...

        def display_value_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "display_value".
            """
            ...

        def end_gesture(self) -> None:
            """
            Notify the end of a modification of the parameter. See begin_gesture.
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def re_enable_automation(self) -> None:
            """
            Reenable automation for this parameter.
            """
            ...

        def remove_automation_state_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "automation_state".
            """
            ...

        def remove_display_value_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "display_value".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_state_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "state".
            """
            ...

        def remove_value_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "value".
            """
            ...

        def state_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "state".
            """
            ...

        def str_for_value(self, arg2: float) -> str:
            """
            Return a string representation of the given value. To be used for display purposes only.  This value can include characters like 'db' or 'hz', depending on the type of the parameter.
            """
            ...

        def value_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "value".
            """
            ...

    class ParameterState:
        enabled: int = 0
        irrelevant: int = 1
        disabled: int = 2


class DriftDevice(ModuleType):

    class DriftDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Drift device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def mod_matrix_filter_source_1_index(self) -> int:
            """
            Return the filter mod source 1 index
            """
            ...

        @mod_matrix_filter_source_1_index.setter
        def mod_matrix_filter_source_1_index(self, value) -> None:
            ...

        @property
        def mod_matrix_filter_source_1_list(self) -> tuple[str, ...]:
            """
            Return the filter mod source 1 list
            """
            ...

        @property
        def mod_matrix_filter_source_2_index(self) -> int:
            """
            Return the filter mod source 2 index
            """
            ...

        @mod_matrix_filter_source_2_index.setter
        def mod_matrix_filter_source_2_index(self, value) -> None:
            ...

        @property
        def mod_matrix_filter_source_2_list(self) -> tuple[str, ...]:
            """
            Return the filter mod source 2 list
            """
            ...

        @property
        def mod_matrix_lfo_source_index(self) -> int:
            """
            Return the lfo mod source index
            """
            ...

        @mod_matrix_lfo_source_index.setter
        def mod_matrix_lfo_source_index(self, value) -> None:
            ...

        @property
        def mod_matrix_lfo_source_list(self) -> tuple[str, ...]:
            """
            Return the lfo mod source list
            """
            ...

        @property
        def mod_matrix_pitch_source_1_index(self) -> int:
            """
            Return the pitch mod source 1 index
            """
            ...

        @mod_matrix_pitch_source_1_index.setter
        def mod_matrix_pitch_source_1_index(self, value) -> None:
            ...

        @property
        def mod_matrix_pitch_source_1_list(self) -> tuple[str, ...]:
            """
            Return the pitch mod source 1 list
            """
            ...

        @property
        def mod_matrix_pitch_source_2_index(self) -> int:
            """
            Return the pitch mod source 2 index
            """
            ...

        @mod_matrix_pitch_source_2_index.setter
        def mod_matrix_pitch_source_2_index(self, value) -> None:
            ...

        @property
        def mod_matrix_pitch_source_2_list(self) -> tuple[str, ...]:
            """
            Return the pitch mod source 2 list
            """
            ...

        @property
        def mod_matrix_shape_source_index(self) -> int:
            """
            Return the shape mod source index
            """
            ...

        @mod_matrix_shape_source_index.setter
        def mod_matrix_shape_source_index(self, value) -> None:
            ...

        @property
        def mod_matrix_shape_source_list(self) -> tuple[str, ...]:
            """
            Return the shape mod source list
            """
            ...

        @property
        def mod_matrix_source_1_index(self) -> int:
            """
            Return the custom mod source 1 index
            """
            ...

        @mod_matrix_source_1_index.setter
        def mod_matrix_source_1_index(self, value) -> None:
            ...

        @property
        def mod_matrix_source_1_list(self) -> tuple[str, ...]:
            """
            Return the custom mod source 1 list
            """
            ...

        @property
        def mod_matrix_source_2_index(self) -> int:
            """
            Return the custom mod source 2 index
            """
            ...

        @mod_matrix_source_2_index.setter
        def mod_matrix_source_2_index(self, value) -> None:
            ...

        @property
        def mod_matrix_source_2_list(self) -> tuple[str, ...]:
            """
            Return the custom mod source 2 list
            """
            ...

        @property
        def mod_matrix_source_3_index(self) -> int:
            """
            Return the custom mod source 3 index
            """
            ...

        @mod_matrix_source_3_index.setter
        def mod_matrix_source_3_index(self, value) -> None:
            ...

        @property
        def mod_matrix_source_3_list(self) -> tuple[str, ...]:
            """
            Return the custom mod source 3 list
            """
            ...

        @property
        def mod_matrix_target_1_index(self) -> int:
            """
            Return the custom mod target 1 index
            """
            ...

        @mod_matrix_target_1_index.setter
        def mod_matrix_target_1_index(self, value) -> None:
            ...

        @property
        def mod_matrix_target_1_list(self) -> tuple[str, ...]:
            """
            Return the custom mod target 1 list
            """
            ...

        @property
        def mod_matrix_target_2_index(self) -> int:
            """
            Return the custom mod target 2 index
            """
            ...

        @mod_matrix_target_2_index.setter
        def mod_matrix_target_2_index(self, value) -> None:
            ...

        @property
        def mod_matrix_target_2_list(self) -> tuple[str, ...]:
            """
            Return the custom mod target 2 list
            """
            ...

        @property
        def mod_matrix_target_3_index(self) -> int:
            """
            Return the custom mod target 3 index
            """
            ...

        @mod_matrix_target_3_index.setter
        def mod_matrix_target_3_index(self, value) -> None:
            ...

        @property
        def mod_matrix_target_3_list(self) -> tuple[str, ...]:
            """
            Return the custom mod target 3 list
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def pitch_bend_range(self) -> int:
            """
            Return the Pitch Bend Range
            """
            ...

        @pitch_bend_range.setter
        def pitch_bend_range(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        @property
        def voice_count_index(self) -> int:
            """
            Return the voice count index
            """
            ...

        @voice_count_index.setter
        def voice_count_index(self, value) -> None:
            ...

        @property
        def voice_count_list(self) -> tuple[str, ...]:
            """
            Return the voice count list
            """
            ...

        @property
        def voice_mode_index(self) -> int:
            """
            Return the voice mode index
            """
            ...

        @voice_mode_index.setter
        def voice_mode_index(self, value) -> None:
            ...

        @property
        def voice_mode_list(self) -> tuple[str, ...]:
            """
            Return the voice mode list
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_mod_matrix_filter_source_1_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_filter_source_1_index" has changed.
            """
            ...

        def add_mod_matrix_filter_source_2_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_filter_source_2_index" has changed.
            """
            ...

        def add_mod_matrix_lfo_source_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_lfo_source_index" has changed.
            """
            ...

        def add_mod_matrix_pitch_source_1_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_pitch_source_1_index" has changed.
            """
            ...

        def add_mod_matrix_pitch_source_2_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_pitch_source_2_index" has changed.
            """
            ...

        def add_mod_matrix_shape_source_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_shape_source_index" has changed.
            """
            ...

        def add_mod_matrix_source_1_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_source_1_index" has changed.
            """
            ...

        def add_mod_matrix_source_2_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_source_2_index" has changed.
            """
            ...

        def add_mod_matrix_source_3_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_source_3_index" has changed.
            """
            ...

        def add_mod_matrix_target_1_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_target_1_index" has changed.
            """
            ...

        def add_mod_matrix_target_2_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_target_2_index" has changed.
            """
            ...

        def add_mod_matrix_target_3_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_matrix_target_3_index" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_bend_range" has changed.
            """
            ...

        def add_voice_count_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "voice_count_index" has changed.
            """
            ...

        def add_voice_mode_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "voice_mode_index" has changed.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def mod_matrix_filter_source_1_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_filter_source_1_index".
            """
            ...

        def mod_matrix_filter_source_2_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_filter_source_2_index".
            """
            ...

        def mod_matrix_lfo_source_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_lfo_source_index".
            """
            ...

        def mod_matrix_pitch_source_1_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_pitch_source_1_index".
            """
            ...

        def mod_matrix_pitch_source_2_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_pitch_source_2_index".
            """
            ...

        def mod_matrix_shape_source_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_shape_source_index".
            """
            ...

        def mod_matrix_source_1_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_source_1_index".
            """
            ...

        def mod_matrix_source_2_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_source_2_index".
            """
            ...

        def mod_matrix_source_3_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_source_3_index".
            """
            ...

        def mod_matrix_target_1_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_target_1_index".
            """
            ...

        def mod_matrix_target_2_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_target_2_index".
            """
            ...

        def mod_matrix_target_3_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_matrix_target_3_index".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def pitch_bend_range_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_bend_range".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_mod_matrix_filter_source_1_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_filter_source_1_index".
            """
            ...

        def remove_mod_matrix_filter_source_2_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_filter_source_2_index".
            """
            ...

        def remove_mod_matrix_lfo_source_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_lfo_source_index".
            """
            ...

        def remove_mod_matrix_pitch_source_1_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_pitch_source_1_index".
            """
            ...

        def remove_mod_matrix_pitch_source_2_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_pitch_source_2_index".
            """
            ...

        def remove_mod_matrix_shape_source_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_shape_source_index".
            """
            ...

        def remove_mod_matrix_source_1_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_source_1_index".
            """
            ...

        def remove_mod_matrix_source_2_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_source_2_index".
            """
            ...

        def remove_mod_matrix_source_3_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_source_3_index".
            """
            ...

        def remove_mod_matrix_target_1_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_target_1_index".
            """
            ...

        def remove_mod_matrix_target_2_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_target_2_index".
            """
            ...

        def remove_mod_matrix_target_3_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_matrix_target_3_index".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_bend_range".
            """
            ...

        def remove_voice_count_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "voice_count_index".
            """
            ...

        def remove_voice_mode_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "voice_mode_index".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def voice_count_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "voice_count_index".
            """
            ...

        def voice_mode_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "voice_mode_index".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> DriftDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class DrumCellDevice(ModuleType):

    class DrumCellDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a DrumCell device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def gain(self) -> float:
            """
            Return the Gain value
            """
            ...

        @gain.setter
        def gain(self, value) -> None:
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_gain_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "gain" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def gain_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "gain".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_gain_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "gain".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> DrumCellDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class DrumChain(ModuleType):

    class DrumChain(object):
        def __init__(self, *a, **k):
            """
            This class represents a drum group device chain in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> RackDevice:
            """
            Get the canonical parent of the chain.
            """
            ...

        @property
        def choke_group(self) -> int:
            """
            Access to the chain's choke group setting.
            """
            ...

        @choke_group.setter
        def choke_group(self, value) -> None:
            ...

        @property
        def color(self) -> int:
            """
            Access the color index of the Chain.
            """
            ...

        @color.setter
        def color(self, value) -> None:
            ...

        @property
        def color_index(self) -> int:
            """
            Access the color index of the Chain.
            """
            ...

        @color_index.setter
        def color_index(self, value) -> None:
            ...

        @property
        def devices(self) -> tuple:
            """
            Return const access to all available Devices that are present in the chains
            """
            ...

        @property
        def has_audio_input(self) -> bool:
            """
            return True, if this Chain can be feed with an Audio signal. This istrue for all Audio Chains.
            """
            ...

        @property
        def has_audio_output(self) -> bool:
            """
            return True, if this Chain sends out an Audio signal. This istrue for all Audio Chains, and MIDI chains with an Instrument.
            """
            ...

        @property
        def has_midi_input(self) -> bool:
            """
            return True, if this Chain can be feed with an Audio signal. This istrue for all MIDI Chains.
            """
            ...

        @property
        def has_midi_output(self) -> bool:
            """
            return True, if this Chain sends out MIDI events. This istrue for all MIDI Chains with no Instruments.
            """
            ...

        @property
        def in_note(self) -> int:
            """
            Access to the incoming MIDI note that will trigger this chain.
            """
            ...

        @in_note.setter
        def in_note(self, value) -> None:
            ...

        @property
        def is_auto_colored(self) -> bool:
            """
            Get/set access to the auto color flag of the Chain.If True, the Chain will always have the same color as the containingTrack or Chain.
            """
            ...

        @is_auto_colored.setter
        def is_auto_colored(self, value) -> None:
            ...

        @property
        def mixer_device(self) -> ChainMixerDevice:
            """
            Return access to the mixer device that holds the chain's mixer parameters:the Volume, Pan, and Sendamounts.
            """
            ...

        @property
        def mute(self) -> bool:
            """
            Mute/unmute the chain.
            """
            ...

        @mute.setter
        def mute(self, value) -> None:
            ...

        @property
        def muted_via_solo(self) -> bool:
            """
            Return const access to whether this chain is muted due to some other chainbeing soloed.
            """
            ...

        @property
        def name(self) -> str:
            """
            Read/write access to the name of the Chain, as visible in the track header.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def out_note(self) -> int:
            """
            Access to the MIDI note sent to the devices in the chain.
            """
            ...

        @out_note.setter
        def out_note(self, value) -> None:
            ...

        @property
        def solo(self) -> bool:
            """
            Get/Set the solo status of the chain. Note that this will not disable thesolo state of any other Chain in the same rack. If you want exclusive solo, you have to disable the solo state of the other Chains manually.
            """
            ...

        @solo.setter
        def solo(self, value) -> None:
            ...

        def add_choke_group_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "choke_group" has changed.
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

        def add_devices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "devices" has changed.
            """
            ...

        def add_in_note_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "in_note" has changed.
            """
            ...

        def add_is_auto_colored_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_auto_colored" has changed.
            """
            ...

        def add_mute_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mute" has changed.
            """
            ...

        def add_muted_via_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "muted_via_solo" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_out_note_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "out_note" has changed.
            """
            ...

        def add_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "solo" has changed.
            """
            ...

        def choke_group_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "choke_group".
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

        def delete_device(self, arg2: int) -> None:
            """
            Remove a device identified by its index from the chain. Throws runtime error if bad index.
            """
            ...

        def devices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "devices".
            """
            ...

        def duplicate_device(self, arg2: int) -> None:
            """
            Duplicate the device at the given index in the chain.
            """
            ...

        def in_note_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "in_note".
            """
            ...

        def insert_device(self, DeviceName: str, DeviceIndex: int=-1) -> LomObject:
            """
            Add a device at a given index in the chain. At end if -1.
            """
            ...

        def is_auto_colored_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_auto_colored".
            """
            ...

        def mute_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mute".
            """
            ...

        def muted_via_solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "muted_via_solo".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def out_note_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "out_note".
            """
            ...

        def remove_choke_group_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "choke_group".
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

        def remove_devices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "devices".
            """
            ...

        def remove_in_note_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "in_note".
            """
            ...

        def remove_is_auto_colored_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_auto_colored".
            """
            ...

        def remove_mute_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mute".
            """
            ...

        def remove_muted_via_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "muted_via_solo".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_out_note_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "out_note".
            """
            ...

        def remove_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "solo".
            """
            ...

        def solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "solo".
            """
            ...


class DrumPad(ModuleType):

    class DrumPad(object):
        def __init__(self, *a, **k):
            """
            This class represents a drum group device pad in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> RackDevice:
            """
            Get the canonical parent of the drum pad.
            """
            ...

        @property
        def chains(self) -> tuple:
            """
            Return const access to the list of chains in this drum pad.
            """
            ...

        @property
        def mute(self) -> bool:
            """
            Mute/unmute the pad.
            """
            ...

        @mute.setter
        def mute(self, value) -> None:
            ...

        @property
        def name(self) -> str:
            """
            Return const access to the drum pad's name. It depends on the contained chains.
            """
            ...

        @property
        def note(self) -> int:
            """
            Get the MIDI note of the drum pad.
            """
            ...

        @property
        def solo(self) -> bool:
            """
            Solo/unsolo the pad.
            """
            ...

        @solo.setter
        def solo(self, value) -> None:
            ...

        def add_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "chains" has changed.
            """
            ...

        def add_mute_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mute" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "solo" has changed.
            """
            ...

        def chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "chains".
            """
            ...

        def delete_all_chains(self) -> None:
            """
            Deletes all chains associated with a drum pad. This is equivalent to deleting a drum rack pad in Live.
            """
            ...

        def mute_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mute".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def remove_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "chains".
            """
            ...

        def remove_mute_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mute".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "solo".
            """
            ...

        def solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "solo".
            """
            ...


class Envelope(ModuleType):

    class Envelope(object):
        def __init__(self, *a, **k):
            """
            This class represents an automation or modulation envelope in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Clip:
            """
            Get the canonical parent of the envelope.
            """
            ...

        def delete_events_in_range(self, arg2: float, arg3: float) -> None:
            """
            Deletes the events in the specified time range.
            """
            ...

        def events_in_range(self, arg2: float, arg3: float) -> EnvelopeEventVector:
            """
            Returns the events in the specified time range.
            """
            ...

        def insert_step(self, arg2: float, arg3: float, arg4: float) -> None:
            """
            Given a start time, a step length and a value, creates a step in the envelope.
            """
            ...

        def value_at_time(self, arg2: float) -> float:
            """
            Returns the parameter value at the specified time.
            """
            ...

    class EnvelopeEvent(object):
        def __init__(self, *a, **k):
            """
            This is a class that represents an envelope event.
            """
            ...

        @property
        def control_coefficients(self) -> EnvelopeEventControlCoefficients:
            ...

        @control_coefficients.setter
        def control_coefficients(self, value) -> None:
            ...

        @property
        def time(self) -> float:
            ...

        @time.setter
        def time(self, value) -> None:
            ...

        @property
        def value(self) -> float:
            ...

        @value.setter
        def value(self, value) -> None:
            ...

    class EnvelopeEventControlCoefficients(object):
        def __init__(self, *a, **k):
            """
            This class represents the control coefficients of an envelope event.
            """
            ...

        @property
        def x1(self) -> float:
            ...

        @x1.setter
        def x1(self, value) -> None:
            ...

        @property
        def x2(self) -> float:
            ...

        @x2.setter
        def x2(self, value) -> None:
            ...

        @property
        def y1(self) -> float:
            ...

        @y1.setter
        def y1(self, value) -> None:
            ...

        @property
        def y2(self) -> float:
            ...

        @y2.setter
        def y2(self, value) -> None:
            ...

    class EnvelopeEventVector(object):
        def __init__(self, *a, **k):
            """
            A container for holding envelope events.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...


class Eq8Device(ModuleType):

    class EditMode:
        a: int = 0
        b: int = 1

    class Eq8Device(object):
        def __init__(self, *a, **k):
            """
            This class represents an Eq8 device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def edit_mode(self) -> bool:
            """
            Access to Eq8's edit mode.
            """
            ...

        @edit_mode.setter
        def edit_mode(self, value) -> None:
            ...

        @property
        def global_mode(self) -> int:
            """
            Access to Eq8's global mode.
            """
            ...

        @global_mode.setter
        def global_mode(self, value) -> None:
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def oversample(self) -> bool:
            """
            Access to Eq8's oversample value.
            """
            ...

        @oversample.setter
        def oversample(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_edit_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "edit_mode" has changed.
            """
            ...

        def add_global_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "global_mode" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_oversample_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oversample" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def edit_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "edit_mode".
            """
            ...

        def global_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "global_mode".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def oversample_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oversample".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_edit_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "edit_mode".
            """
            ...

        def remove_global_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "global_mode".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_oversample_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oversample".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of an Eq8 device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> Eq8Device:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            @property
            def selected_band(self) -> int:
                """
                Access to the selected filter band.
                """
                ...

            @selected_band.setter
            def selected_band(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def add_selected_band_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_band" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...

            def remove_selected_band_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_band".
                """
                ...

            def selected_band_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_band".
                """
                ...

    class GlobalMode:
        stereo: int = 0
        left_right: int = 1
        mid_side: int = 2


class Groove(ModuleType):

    class Base:
        gb_four: int = 0
        gb_eight: int = 1
        gb_eight_triplet: int = 2
        gb_sixteen: int = 3
        gb_sixteen_triplet: int = 4
        gb_thirtytwo: int = 5
        count: int = 6

    class Groove(object):
        def __init__(self, *a, **k):
            """
            This class represents a groove in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def base(self) -> Base:
            """
            Get/set the groove's base grid.
            """
            ...

        @base.setter
        def base(self, value) -> None:
            ...

        @property
        def canonical_parent(self) -> GroovePool:
            """
            Get the canonical parent of the groove.
            """
            ...

        @property
        def name(self) -> str:
            """
            Read/write/listen access to the groove's name
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def quantization_amount(self) -> float:
            """
            Read/write/listen access to the groove's quantization amount.
            """
            ...

        @quantization_amount.setter
        def quantization_amount(self, value) -> None:
            ...

        @property
        def random_amount(self) -> float:
            """
            Read/write/listen access to the groove's random amount.
            """
            ...

        @random_amount.setter
        def random_amount(self, value) -> None:
            ...

        @property
        def timing_amount(self) -> float:
            """
            Read/write/listen access to the groove's timing amount.
            """
            ...

        @timing_amount.setter
        def timing_amount(self, value) -> None:
            ...

        @property
        def velocity_amount(self) -> float:
            """
            Read/write/listen access to the groove's velocity amount.
            """
            ...

        @velocity_amount.setter
        def velocity_amount(self, value) -> None:
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_quantization_amount_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "quantization_amount" has changed.
            """
            ...

        def add_random_amount_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "random_amount" has changed.
            """
            ...

        def add_timing_amount_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "timing_amount" has changed.
            """
            ...

        def add_velocity_amount_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "velocity_amount" has changed.
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def quantization_amount_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "quantization_amount".
            """
            ...

        def random_amount_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "random_amount".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_quantization_amount_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "quantization_amount".
            """
            ...

        def remove_random_amount_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "random_amount".
            """
            ...

        def remove_timing_amount_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "timing_amount".
            """
            ...

        def remove_velocity_amount_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "velocity_amount".
            """
            ...

        def timing_amount_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "timing_amount".
            """
            ...

        def velocity_amount_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "velocity_amount".
            """
            ...


class GroovePool(ModuleType):

    class GroovePool(object):
        def __init__(self, *a, **k):
            """
            This class represents the groove pool in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Song:
            """
            Get the canonical parent of the groove pool.
            """
            ...

        @property
        def grooves(self) -> tuple:
            """
            Access to the list of grooves
            """
            ...

        def add_grooves_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "grooves" has changed.
            """
            ...

        def grooves_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "grooves".
            """
            ...

        def remove_grooves_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "grooves".
            """
            ...


class HybridReverbDevice(ModuleType):

    class HybridReverbDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Hybrid Reverb device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def ir_attack_time(self) -> float:
            """
            Return the current IrAttackTime
            """
            ...

        @ir_attack_time.setter
        def ir_attack_time(self, value) -> None:
            ...

        @property
        def ir_category_index(self) -> int:
            """
            Return the current IR category index
            """
            ...

        @ir_category_index.setter
        def ir_category_index(self, value) -> None:
            ...

        @property
        def ir_category_list(self) -> tuple[str, ...]:
            """
            Return the current IR categories list
            """
            ...

        @property
        def ir_decay_time(self) -> float:
            """
            Return the current IrDecayTime
            """
            ...

        @ir_decay_time.setter
        def ir_decay_time(self, value) -> None:
            ...

        @property
        def ir_file_index(self) -> int:
            """
            Return the current IR file index
            """
            ...

        @ir_file_index.setter
        def ir_file_index(self, value) -> None:
            ...

        @property
        def ir_file_list(self) -> tuple[str, ...]:
            """
            Return the current IR file list
            """
            ...

        @property
        def ir_size_factor(self) -> float:
            """
            Return the current IrSizeFactor
            """
            ...

        @ir_size_factor.setter
        def ir_size_factor(self, value) -> None:
            ...

        @property
        def ir_time_shaping_on(self) -> bool:
            """
            Return the current IrTimeShapingOn
            """
            ...

        @ir_time_shaping_on.setter
        def ir_time_shaping_on(self, value) -> None:
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_ir_attack_time_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "ir_attack_time" has changed.
            """
            ...

        def add_ir_category_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "ir_category_index" has changed.
            """
            ...

        def add_ir_decay_time_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "ir_decay_time" has changed.
            """
            ...

        def add_ir_file_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "ir_file_index" has changed.
            """
            ...

        def add_ir_file_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "ir_file_list" has changed.
            """
            ...

        def add_ir_size_factor_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "ir_size_factor" has changed.
            """
            ...

        def add_ir_time_shaping_on_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "ir_time_shaping_on" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def ir_attack_time_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "ir_attack_time".
            """
            ...

        def ir_category_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "ir_category_index".
            """
            ...

        def ir_decay_time_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "ir_decay_time".
            """
            ...

        def ir_file_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "ir_file_index".
            """
            ...

        def ir_file_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "ir_file_list".
            """
            ...

        def ir_size_factor_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "ir_size_factor".
            """
            ...

        def ir_time_shaping_on_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "ir_time_shaping_on".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_ir_attack_time_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "ir_attack_time".
            """
            ...

        def remove_ir_category_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "ir_category_index".
            """
            ...

        def remove_ir_decay_time_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "ir_decay_time".
            """
            ...

        def remove_ir_file_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "ir_file_index".
            """
            ...

        def remove_ir_file_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "ir_file_list".
            """
            ...

        def remove_ir_size_factor_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "ir_size_factor".
            """
            ...

        def remove_ir_time_shaping_on_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "ir_time_shaping_on".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> HybridReverbDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class Licensing(ModuleType):

    @staticmethod
    def authorization_clock_days_ahead() -> int:
        """
        Advances the current date by the number of days specified by _AuthClockDaysAhead
        """
        ...

    @staticmethod
    def get_authorization_page_url(reauthorize: bool, is_trial: bool) -> str:
        """
        Retrieves the appopriate URL on ableton.com where the unser can initiate the authorization.
        """
        ...

    @staticmethod
    def get_purchase_live_url() -> str:
        """
        Returns the environment-aware purchase URL for purchasing Live licenses
        """
        ...

    @staticmethod
    def get_services_url() -> str:
        """
        Returns the URL against which service calls (e.g. for authorization) can be performed.
        """
        ...

    @staticmethod
    def get_unlock_dir() -> tuple:
        """
        Returns a tuple containing the unlock file directory and a flag indicating if the unlock file is in the system domain.
        """
        ...

    @staticmethod
    def launch_web_browser(url: str) -> None:
        """
        Opens a web browser at the specified URL on the user's computer.
        """
        ...

    class ProgressDialog(object):
        def __init__(self, *a, **k):
            """
            A modal dialog showing a message and a progress animation.
            """
            ...

        def end_modal_loop(self) -> None:
            ...

        def run_in_modal_loop(self) -> None:
            ...

        def set_status_message(self, msg: str) -> None:
            ...

    class PythonLicensingBridge(object):
        def __init__(self, *a, **k):
            """
            Interface to the internal licensing services.
            """
            ...

        @property
        def base_product_id(self):
            """
            Returns Live's current base product ID.
            """
            ...

        @property
        def in_sassafras_mode(self):
            ...

        @property
        def license_must_match_variant(self):
            """
            Returns a bool indicating if we require the license information returned by the server to match the variant of Live.
            """
            ...

        @property
        def random_number_for_trial_authorization(self):
            """
            Returns the integer to send along with the Trial authorization request. This same integer will be checked for in `process_trial_response` (and then changed).
            """
            ...

        @property
        def set_has_unsaved_changes(self):
            """
            Returns true if the set has unsaved changes.
            """
            ...

        def authorize_with_sassafras(self) -> None:
            ...

        def create_new_live_set(self) -> None:
            """
            Creates a new live set and discards unsaved changes.
            """
            ...

        def deauthenticate_user(self) -> None:
            """
            Deletes the current session ID.
            """
            ...

        def get_progress_dialog(self) -> ProgressDialog:
            """
            Retrieves an instance of ProgressDialog.
            """
            ...

        def get_session_id(self) -> str:
            """
            Retrieve stored session ID.
            """
            ...

        def get_startup_dialog(self, authorize_callable: object, authorize_later_callable: object) -> StartupDialog:
            """
            Retrieves an instance of the startup dialog with the passed callables connected to its buttons.
            """
            ...

        def get_trial_time_left(self) -> str:
            """
            Returns remaining time on a trial as a formatted string.
            """
            ...

        def invoke_pack_installation_callback(self) -> None:
            """
            Call package installation callback.
            """
            ...

        def load_and_convert_legacy_unlock_cfg(self) -> dict:
            """
            Loads the Unlock.cfg file and returns either an empty dict or one that can be converted to an UnlockData object.
            """
            ...

        def process_license_response(self, license_response_lines: list) -> UnlockStatus:
            """
            Processes a list of strings, each representing a server response to a product authorization.
            """
            ...

        def process_trial_response(self, trial_response_line: str) -> bool:
            """
            Process the server's response to a Trial authorization.
            """
            ...

        def request_exit(self, exit_code: int=0) -> None:
            ...

        def save_current_set(self) -> None:
            """
            Saves the current Live session.
            """
            ...

        def set_network_timer(self, callback: object, interval_in_ms: int) -> None:
            """
            Starts or stops a timer meant for driving network operations. Pass None as callback to stop the timer. If any callback invocation raises an exception, the timer is stopped.
            """
            ...

        def store_session_id(self, session_id: str) -> None:
            """
            Securely stores the user's session ID (aka cookie, aka credentials).
            """
            ...

    class StartupDialog(object):
        def __init__(self, *a, **k):
            """
            Serves as an entry point for the user to authorize Live on first launch
            """
            ...

        def end_modal_loop(self) -> None:
            ...

        def run_in_modal_loop(self) -> None:
            ...

        def set_notification_message(self, show_progress_bar: bool) -> None:
            ...

    class TrialContext:
        SAVE: int = 0
        FORCE_UPDATE: int = 2
        STARTUP: int = 3

    class UnlockStatus(object):
        def __init__(self, *a, **k):
            """
            Returns relevant information after unlock
            """
            ...

        @property
        def authorization_deactivated(self):
            ...

        @property
        def authorization_expired(self):
            ...

        @property
        def has_max_unlock_products(self):
            ...

        @property
        def temp_demo_mode(self):
            ...

        @property
        def time_limited(self):
            ...

        @property
        def unlock_error(self):
            ...

        @property
        def unlocked(self):
            ...


class Listener(ModuleType):

    class ListenerHandle(object):
        def __init__(self, *a, **k):
            """
            This class represents a Python listener when connected to a Live property.
            """
            ...

        @property
        def listener_func(self):
            """
            Returns the original function
            """
            ...

        @property
        def listener_self(self):
            """
            Returns the weak reference to original self, if it was a bound method
            """
            ...

        @property
        def name(self):
            """
            Prints the name of the property that this listener is connected to
            """
            ...

        def disconnect(self) -> None:
            """
            Disconnects the listener from its property
            """
            ...

    class ListenerVector(object):
        def __init__(self, *a, **k):
            """
            A read only container for accessing a list of listeners.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...


class LomObject(ModuleType):

    class LomObject(object):
        def __init__(self, *a, **k):
            """
            this is the base class for an object that is accessible via the LOM
            """
            ...

        @property
        def _live_ptr(self):
            ...


class LooperDevice(ModuleType):

    class LooperDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Looper device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def loop_length(self) -> float:
            """
            The length of Looper's buffer.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def overdub_after_record(self) -> bool:
            """
            If true, Looper will switch to overdub after recording, when recording a fixed number of bars. Otherwise, the switch will be to playback without overdubbing.
            """
            ...

        @overdub_after_record.setter
        def overdub_after_record(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def record_length_index(self) -> int:
            """
            Access to the Record Length chooser entry index.
            """
            ...

        @record_length_index.setter
        def record_length_index(self, value) -> None:
            ...

        @property
        def record_length_list(self) -> tuple[str, ...]:
            """
            Read-only access to the list of Record Length chooser entry strings.
            """
            ...

        @property
        def tempo(self) -> float:
            """
            The tempo of Looper's buffer.
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_loop_length_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "loop_length" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_overdub_after_record_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "overdub_after_record" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_record_length_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "record_length_index" has changed.
            """
            ...

        def add_tempo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tempo" has changed.
            """
            ...

        def clear(self) -> None:
            """
            Erase Looper's recorded content.
            """
            ...

        def double_length(self) -> None:
            """
            Double the length of Looper's buffer.
            """
            ...

        def double_speed(self) -> None:
            """
            Double the speed of Looper's playback.
            """
            ...

        def export_to_clip_slot(self, arg2: ClipSlot) -> None:
            """
            Export Looper's content to a Session Clip Slot.
            """
            ...

        def half_length(self) -> None:
            """
            Halve the length of Looper's buffer.
            """
            ...

        def half_speed(self) -> None:
            """
            Halve the speed of Looper's playback.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def loop_length_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "loop_length".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def overdub(self) -> None:
            """
            Play back while adding additional layers of incoming audio.
            """
            ...

        def overdub_after_record_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "overdub_after_record".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def play(self) -> None:
            """
            Play back without overdubbing.
            """
            ...

        def record(self) -> None:
            """
            Record incoming audio.
            """
            ...

        def record_length_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "record_length_index".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_loop_length_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "loop_length".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_overdub_after_record_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "overdub_after_record".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_record_length_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "record_length_index".
            """
            ...

        def remove_tempo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tempo".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def stop(self) -> None:
            """
            Stop Looper's playback.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def tempo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tempo".
            """
            ...

        def undo(self) -> None:
            """
            Erase everything that was recorded since the last time Overdub was enabled. Calling a second time will restore the material erased by the previous undooperation.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> LooperDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class MaxDevice(ModuleType):

    class MaxDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Max for Live device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def audio_inputs(self) -> tuple:
            """
            Const access to a list of all audio inputs of the device.
            """
            ...

        @property
        def audio_outputs(self) -> tuple:
            """
            Const access to a list of all audio outputs of the device.
            """
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self):
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def midi_inputs(self) -> tuple:
            """
            Const access to a list of all midi outputs of the device.
            """
            ...

        @property
        def midi_outputs(self) -> tuple:
            """
            Const access to a list of all midi outputs of the device.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_audio_inputs_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "audio_inputs" has changed.
            """
            ...

        def add_audio_outputs_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "audio_outputs" has changed.
            """
            ...

        def add_bank_parameters_changed_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "bank_parameters_changed" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_midi_inputs_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_inputs" has changed.
            """
            ...

        def add_midi_outputs_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_outputs" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def audio_inputs_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "audio_inputs".
            """
            ...

        def audio_outputs_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "audio_outputs".
            """
            ...

        def bank_parameters_changed_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "bank_parameters_changed".
            """
            ...

        def get_bank_count(self) -> int:
            """
            Get the number of parameter banks. This is related to hardware control surfaces.
            """
            ...

        def get_bank_name(self, arg2: int) -> str:
            """
            Get the name of a parameter bank given by index. This is related to hardware control surfaces.
            """
            ...

        def get_bank_parameters(self, arg2: int) -> list:
            """
            Get the indices of parameters of the given bank index. Empty slots are marked as -1. Bank index -1 refers to the best-of bank. This function is related to hardware control surfaces.
            """
            ...

        def get_value_item_icons(self, arg2: DeviceParameter) -> list:
            """
            Get a list of icon identifier strings for a list parameter's values.An empty string is given where no icon should be displayed.An empty list is given when no icons should be displayed.This is related to hardware control surfaces.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def midi_inputs_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_inputs".
            """
            ...

        def midi_outputs_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_outputs".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_audio_inputs_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "audio_inputs".
            """
            ...

        def remove_audio_outputs_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "audio_outputs".
            """
            ...

        def remove_bank_parameters_changed_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "bank_parameters_changed".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_midi_inputs_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_inputs".
            """
            ...

        def remove_midi_outputs_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_outputs".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> MaxDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class MeldDevice(ModuleType):

    class MeldDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Meld device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def mono_poly(self) -> int:
            """
            Returns the mode of Polyphony
            """
            ...

        @mono_poly.setter
        def mono_poly(self, value) -> None:
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def poly_voices(self) -> int:
            """
            Return the Poly Voice count
            """
            ...

        @poly_voices.setter
        def poly_voices(self, value) -> None:
            ...

        @property
        def selected_engine(self) -> bool:
            """
            Return what Voice Engine is selected
            """
            ...

        @selected_engine.setter
        def selected_engine(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def unison_voices(self) -> int:
            """
            Return the Unison Voice count
            """
            ...

        @unison_voices.setter
        def unison_voices(self, value) -> None:
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_mono_poly_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mono_poly" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_poly_voices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "poly_voices" has changed.
            """
            ...

        def add_selected_engine_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "selected_engine" has changed.
            """
            ...

        def add_unison_voices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "unison_voices" has changed.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def mono_poly_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mono_poly".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def poly_voices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "poly_voices".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_mono_poly_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mono_poly".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_poly_voices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "poly_voices".
            """
            ...

        def remove_selected_engine_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "selected_engine".
            """
            ...

        def remove_unison_voices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "unison_voices".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def selected_engine_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "selected_engine".
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def unison_voices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "unison_voices".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> MeldDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class MidiMap(ModuleType):

    @staticmethod
    def forward_midi_cc(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool=True) -> bool:
        ...

    @staticmethod
    def forward_midi_note(arg1: int, arg2: int, arg3: int, arg4: int, ShouldConsumeEvent: bool=True) -> bool:
        ...

    @staticmethod
    def forward_midi_pitchbend(arg1: int, arg2: int, arg3: int) -> bool:
        ...

    @staticmethod
    def map_midi_cc(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, avoid_takeover: bool, sensitivity: float=1.0) -> bool:
        ...

    @staticmethod
    def map_midi_cc_with_feedback_map(midi_map_handle: int, parameter: DeviceParameter, midi_channel: int, controller_number: int, map_mode: MapMode, feedback_rule: CCFeedbackRule, avoid_takeover: bool, sensitivity: float=1.0) -> bool:
        ...

    @staticmethod
    def map_midi_note(arg1: int, arg2: DeviceParameter, arg3: int, arg4: int) -> bool:
        ...

    @staticmethod
    def map_midi_note_with_feedback_map(arg1: int, arg2: DeviceParameter, arg3: int, arg4: int, arg5: NoteFeedbackRule) -> bool:
        ...

    @staticmethod
    def map_midi_pitchbend(arg1: int, arg2: DeviceParameter, arg3: int, arg4: bool) -> bool:
        ...

    @staticmethod
    def map_midi_pitchbend_with_feedback_map(arg1: int, arg2: DeviceParameter, arg3: int, arg4: PitchBendFeedbackRule, arg5: bool) -> bool:
        ...

    @staticmethod
    def send_feedback_for_parameter(arg1: int, arg2: DeviceParameter) -> None:
        ...

    class CCFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            ...

        @property
        def cc_no(self) -> int:
            ...

        @cc_no.setter
        def cc_no(self, value) -> None:
            ...

        @property
        def cc_value_map(self) -> tuple:
            ...

        @cc_value_map.setter
        def cc_value_map(self, value) -> None:
            ...

        @property
        def channel(self) -> int:
            ...

        @channel.setter
        def channel(self, value) -> None:
            ...

        @property
        def delay_in_ms(self) -> float:
            ...

        @delay_in_ms.setter
        def delay_in_ms(self, value) -> None:
            ...

        @property
        def enabled(self) -> bool:
            ...

        @enabled.setter
        def enabled(self, value) -> None:
            ...

    class MapMode:
        absolute: int = 0
        relative_signed_bit: int = 1
        relative_binary_offset: int = 2
        relative_two_compliment: int = 3
        relative_signed_bit2: int = 4
        absolute_14_bit: int = 5
        relative_smooth_signed_bit: int = 6
        relative_smooth_binary_offset: int = 7
        relative_smooth_two_compliment: int = 8
        relative_smooth_signed_bit2: int = 9

    class NoteFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            ...

        @property
        def channel(self) -> int:
            ...

        @channel.setter
        def channel(self, value) -> None:
            ...

        @property
        def delay_in_ms(self) -> float:
            ...

        @delay_in_ms.setter
        def delay_in_ms(self, value) -> None:
            ...

        @property
        def enabled(self) -> bool:
            ...

        @enabled.setter
        def enabled(self, value) -> None:
            ...

        @property
        def note_no(self) -> int:
            ...

        @note_no.setter
        def note_no(self, value) -> None:
            ...

        @property
        def vel_map(self) -> tuple:
            ...

        @vel_map.setter
        def vel_map(self, value) -> None:
            ...

    class PitchBendFeedbackRule(object):
        def __init__(self, *a, **k):
            """
            Structure to define feedback properties of MIDI mappings.
            """
            ...

        @property
        def channel(self) -> int:
            ...

        @channel.setter
        def channel(self, value) -> None:
            ...

        @property
        def delay_in_ms(self) -> float:
            ...

        @delay_in_ms.setter
        def delay_in_ms(self, value) -> None:
            ...

        @property
        def enabled(self) -> bool:
            ...

        @enabled.setter
        def enabled(self, value) -> None:
            ...

        @property
        def value_pair_map(self) -> tuple:
            ...

        @value_pair_map.setter
        def value_pair_map(self, value) -> None:
            ...


class MixerDevice(ModuleType):

    class MixerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Mixer Device in Live, which gives youaccess to the Volume and Panning properties of a Track.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the mixer device.
            """
            ...

        @property
        def crossfade_assign(self) -> int:
            """
            Player- and ReturnTracks only: Access to the Track's Crossfade Assign State.
            """
            ...

        @crossfade_assign.setter
        def crossfade_assign(self, value) -> None:
            ...

        @property
        def crossfader(self) -> DeviceParameter:
            """
            MainTrack only: Const access to the Crossfader.
            """
            ...

        @property
        def cue_volume(self) -> DeviceParameter:
            """
            MainTrack only: Const access to the Cue Volume Parameter.
            """
            ...

        @property
        def left_split_stereo(self) -> DeviceParameter:
            """
            Const access to the Track's Left Split Stereo Panning Device Parameter.
            """
            ...

        @property
        def panning(self) -> DeviceParameter:
            """
            Const access to the Tracks Panning Device Parameter.
            """
            ...

        @property
        def panning_mode(self) -> int:
            """
            Access to the Track's Panning Mode.
            """
            ...

        @panning_mode.setter
        def panning_mode(self, value) -> None:
            ...

        @property
        def right_split_stereo(self) -> DeviceParameter:
            """
            Const access to the Track's Right Split Stereo Panning Device Parameter.
            """
            ...

        @property
        def sends(self) -> tuple:
            """
            Const access to the Tracks list of Send Amount Device Parameters.
            """
            ...

        @property
        def song_tempo(self) -> DeviceParameter:
            """
            MainTrack only: Const access to the Song's Tempo.
            """
            ...

        @property
        def track_activator(self) -> DeviceParameter:
            """
            Const access to the Tracks Activator Device Parameter.
            """
            ...

        @property
        def volume(self) -> DeviceParameter:
            """
            Const access to the Tracks Volume Device Parameter.
            """
            ...

        def add_crossfade_assign_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "crossfade_assign" has changed.
            """
            ...

        def add_panning_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "panning_mode" has changed.
            """
            ...

        def add_sends_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "sends" has changed.
            """
            ...

        def crossfade_assign_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "crossfade_assign".
            """
            ...

        def panning_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "panning_mode".
            """
            ...

        def remove_crossfade_assign_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "crossfade_assign".
            """
            ...

        def remove_panning_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "panning_mode".
            """
            ...

        def remove_sends_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "sends".
            """
            ...

        def sends_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sends".
            """
            ...

        class crossfade_assignments:
            A: int = 0
            NONE: int = 1
            B: int = 2

        class panning_modes:
            stereo: int = 0
            stereo_split: int = 1


class PluginDevice(ModuleType):

    class PluginDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a plugin device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self):
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def presets(self) -> tuple[str, ...]:
            """
            Get the list of presets the plugin offers.
            """
            ...

        @property
        def selected_preset_index(self) -> int:
            """
            Access to the index of the currently selected preset.
            """
            ...

        @selected_preset_index.setter
        def selected_preset_index(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_presets_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "presets" has changed.
            """
            ...

        def add_selected_preset_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "selected_preset_index" has changed.
            """
            ...

        def get_parameter_names(self, begin: int=0, end: int=-1) -> StringVector:
            """
            Get the range of plugin parameter names, bound by begin and end. If end is smaller than 0 it is interpreted as the parameter count.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def presets_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "presets".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_presets_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "presets".
            """
            ...

        def remove_selected_preset_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "selected_preset_index".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def selected_preset_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "selected_preset_index".
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> PluginDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class RackDevice(ModuleType):

    class RackDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Rack device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def can_show_chains(self) -> bool:
            """
            return True, if this Rack contains a rack instrument device that is capable of showing its chains in session view.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def chain_selector(self) -> DeviceParameter:
            """
            Const access to the chain selector parameter.
            """
            ...

        @property
        def chains(self) -> tuple:
            """
            Return const access to the list of chains in this device. Throws an exception if can_have_chains is false.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def drum_pads(self) -> tuple:
            """
            Return const access to the list of drum pads in this device. Throws an exception if can_have_drum_pads is false.
            """
            ...

        @property
        def has_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack which has drum pads. Throws an exception if can_have_drum_pads is false.
            """
            ...

        @property
        def has_macro_mappings(self) -> bool:
            """
            Returns true if any of the rack's macros are mapped to a parameter.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_showing_chains(self) -> bool:
            """
            Returns True, if it is showing chains.
            """
            ...

        @is_showing_chains.setter
        def is_showing_chains(self, value) -> None:
            ...

        @property
        def is_using_compare_preset_b(self):
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def macros_mapped(self) -> tuple:
            """
            A list of booleans, one for each macro parameter, which is True iffthat macro is mapped to something
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def return_chains(self) -> tuple:
            """
            Return const access to the list of return chains in this device. Throws an exception if can_have_chains is false.
            """
            ...

        @property
        def selected_variation_index(self) -> int:
            """
            Access to the index of the currently selected macro variation.Throws an exception if the index is out of range.
            """
            ...

        @selected_variation_index.setter
        def selected_variation_index(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def variation_count(self) -> int:
            """
            Access to the number of macro variations currently stored.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        @property
        def visible_drum_pads(self) -> tuple:
            """
            Return const access to the list of visible drum pads in this device. Throws an exception if can_have_drum_pads is false.
            """
            ...

        @property
        def visible_macro_count(self) -> int:
            """
            Access to the number of macros that are currently visible.
            """
            ...

        def add_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "chains" has changed.
            """
            ...

        def add_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "drum_pads" has changed.
            """
            ...

        def add_has_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_drum_pads" has changed.
            """
            ...

        def add_has_macro_mappings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_macro_mappings" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_showing_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_showing_chains" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_macro(self) -> None:
            """
            Increases the number of visible macro controls in the rack. Throws an exception if the maximum number of macro controls is reached.
            """
            ...

        def add_macros_mapped_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "macros_mapped" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_return_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "return_chains" has changed.
            """
            ...

        def add_variation_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "variation_count" has changed.
            """
            ...

        def add_visible_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "visible_drum_pads" has changed.
            """
            ...

        def add_visible_macro_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "visible_macro_count" has changed.
            """
            ...

        def chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "chains".
            """
            ...

        def copy_pad(self, arg2: int, arg3: int) -> None:
            """
            Copies all contents of a drum pad from a source pad into a destination pad. copy_pad(source_index, destination_index) where source_index and destination_index correspond to the note number/index of the drum pad in a drum rack. Throws an exception when the source pad is empty, or when the source or destination indices are not between 0 - 127.
            """
            ...

        def delete_selected_variation(self) -> None:
            """
            Deletes the currently selected macro variation.Does nothing if there is no selected variation.
            """
            ...

        def drum_pads_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "drum_pads".
            """
            ...

        def has_drum_pads_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_drum_pads".
            """
            ...

        def has_macro_mappings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_macro_mappings".
            """
            ...

        def insert_chain(self, Index: int=-1) -> LomObject:
            """
            Inserts a new chain, either at the specified index or, if not index was specified, at the end of the chain sequence.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_showing_chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_showing_chains".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def macros_mapped_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "macros_mapped".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def randomize_macros(self) -> None:
            """
            Randomizes the values for all macro controls not excluded from randomization.
            """
            ...

        def recall_last_used_variation(self) -> None:
            """
            Recalls the macro variation that was recalled most recently.Does nothing if no variation has been recalled yet.
            """
            ...

        def recall_selected_variation(self) -> None:
            """
            Recalls the currently selected macro variation.Does nothing if there are no variations.
            """
            ...

        def remove_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "chains".
            """
            ...

        def remove_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "drum_pads".
            """
            ...

        def remove_has_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_drum_pads".
            """
            ...

        def remove_has_macro_mappings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_macro_mappings".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_showing_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_showing_chains".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_macro(self) -> None:
            """
            Decreases the number of visible macro controls in the rack. Throws an exception if the minimum number of macro controls is reached.
            """
            ...

        def remove_macros_mapped_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "macros_mapped".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_return_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "return_chains".
            """
            ...

        def remove_variation_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "variation_count".
            """
            ...

        def remove_visible_drum_pads_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "visible_drum_pads".
            """
            ...

        def remove_visible_macro_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "visible_macro_count".
            """
            ...

        def return_chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "return_chains".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def store_variation(self) -> None:
            """
            Stores a new variation of the values of all currently mapped macros
            """
            ...

        def variation_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "variation_count".
            """
            ...

        def visible_drum_pads_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "visible_drum_pads".
            """
            ...

        def visible_macro_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "visible_macro_count".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a rack device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> RackDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def drum_pads_scroll_position(self) -> int:
                """
                Access to the index of the lowest visible row of pads. Throws an exception if can_have_drum_pads is false.
                """
                ...

            @drum_pads_scroll_position.setter
            def drum_pads_scroll_position(self, value) -> None:
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            @property
            def is_showing_chain_devices(self) -> bool:
                """
                Return whether the devices in the currently selected chain are visible. Throws an exception if can_have_chains is false.
                """
                ...

            @is_showing_chain_devices.setter
            def is_showing_chain_devices(self, value) -> None:
                ...

            @property
            def selected_chain(self) -> None:
                """
                Return access to the currently selected chain.
                """
                ...

            @selected_chain.setter
            def selected_chain(self, value) -> None:
                ...

            @property
            def selected_drum_pad(self) -> DrumPad:
                """
                Return access to the currently selected drum pad. Throws an exception if can_have_drum_pads is false.
                """
                ...

            @selected_drum_pad.setter
            def selected_drum_pad(self, value) -> None:
                ...

            def add_drum_pads_scroll_position_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "drum_pads_scroll_position" has changed.
                """
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def add_is_showing_chain_devices_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_showing_chain_devices" has changed.
                """
                ...

            def add_selected_chain_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_chain" has changed.
                """
                ...

            def add_selected_drum_pad_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_drum_pad" has changed.
                """
                ...

            def drum_pads_scroll_position_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "drum_pads_scroll_position".
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def is_showing_chain_devices_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_showing_chain_devices".
                """
                ...

            def remove_drum_pads_scroll_position_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "drum_pads_scroll_position".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...

            def remove_is_showing_chain_devices_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_showing_chain_devices".
                """
                ...

            def remove_selected_chain_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_chain".
                """
                ...

            def remove_selected_drum_pad_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_drum_pad".
                """
                ...

            def selected_chain_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_chain".
                """
                ...

            def selected_drum_pad_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_drum_pad".
                """
                ...


class RoarDevice(ModuleType):

    class RoarDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Roar device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def env_listen(self) -> bool:
            """
            Return the Envelope Input Listen toggle state
            """
            ...

        @env_listen.setter
        def env_listen(self, value) -> None:
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def routing_mode_index(self) -> int:
            """
            Return the routing mode index
            """
            ...

        @routing_mode_index.setter
        def routing_mode_index(self, value) -> None:
            ...

        @property
        def routing_mode_list(self) -> tuple[str, ...]:
            """
            Return the routing mode list
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_env_listen_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "env_listen" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_routing_mode_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "routing_mode_index" has changed.
            """
            ...

        def env_listen_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "env_listen".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def remove_env_listen_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "env_listen".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_routing_mode_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "routing_mode_index".
            """
            ...

        def routing_mode_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "routing_mode_index".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> RoarDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class Sample(ModuleType):

    class Sample(object):
        def __init__(self, *a, **k):
            """
            This class represents a sample file loaded into a Simpler instance.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def beats_granulation_resolution(self) -> int:
            """
            Access to the Granulation Resolution parameter in Beats Warp Mode.
            """
            ...

        @beats_granulation_resolution.setter
        def beats_granulation_resolution(self, value) -> None:
            ...

        @property
        def beats_transient_envelope(self) -> float:
            """
            Access to the Transient Envelope parameter in Beats Warp Mode.
            """
            ...

        @beats_transient_envelope.setter
        def beats_transient_envelope(self, value) -> None:
            ...

        @property
        def beats_transient_loop_mode(self) -> int:
            """
            Access to the Transient Loop Mode parameter in Beats Warp Mode.
            """
            ...

        @beats_transient_loop_mode.setter
        def beats_transient_loop_mode(self, value) -> None:
            ...

        @property
        def canonical_parent(self) -> SimplerDevice:
            """
            Access to the sample's canonical parent.
            """
            ...

        @property
        def complex_pro_envelope(self) -> float:
            """
            Access to the Envelope parameter in Complex Pro Mode.
            """
            ...

        @complex_pro_envelope.setter
        def complex_pro_envelope(self, value) -> None:
            ...

        @property
        def complex_pro_formants(self) -> float:
            """
            Access to the Formants parameter in Complex Pro Warp Mode.
            """
            ...

        @complex_pro_formants.setter
        def complex_pro_formants(self, value) -> None:
            ...

        @property
        def end_marker(self) -> int:
            """
            Access to the position of the sample's end marker.
            """
            ...

        @end_marker.setter
        def end_marker(self, value) -> None:
            ...

        @property
        def file_path(self) -> str:
            """
            Get the path of the sample file.
            """
            ...

        @property
        def gain(self) -> float:
            """
            Access to the sample gain.
            """
            ...

        @gain.setter
        def gain(self, value) -> None:
            ...

        @property
        def length(self) -> int:
            """
            Get the length of the sample file in sample frames.
            """
            ...

        @property
        def sample_rate(self) -> float:
            """
            Access to the audio sample rate of the sample.
            """
            ...

        @property
        def slices(self) -> tuple:
            """
            Access to the list of slice points in sample time in the sample.
            """
            ...

        @property
        def slicing_beat_division(self) -> int:
            """
            Access to sample's slicing step size.
            """
            ...

        @slicing_beat_division.setter
        def slicing_beat_division(self, value) -> None:
            ...

        @property
        def slicing_region_count(self) -> int:
            """
            Access to sample's slicing split count.
            """
            ...

        @slicing_region_count.setter
        def slicing_region_count(self, value) -> None:
            ...

        @property
        def slicing_sensitivity(self) -> float:
            """
            Access to sample's slicing sensitivity whose sensitivity is in between 0.0 and 1.0.The higher the sensitivity, the more slices will be available.
            """
            ...

        @slicing_sensitivity.setter
        def slicing_sensitivity(self, value) -> None:
            ...

        @property
        def slicing_style(self) -> int:
            """
            Access to sample's slicing style.
            """
            ...

        @slicing_style.setter
        def slicing_style(self, value) -> None:
            ...

        @property
        def start_marker(self) -> int:
            """
            Access to the position of the sample's start marker.
            """
            ...

        @start_marker.setter
        def start_marker(self, value) -> None:
            ...

        @property
        def texture_flux(self) -> float:
            """
            Access to the Flux parameter in Texture Warp Mode.
            """
            ...

        @texture_flux.setter
        def texture_flux(self, value) -> None:
            ...

        @property
        def texture_grain_size(self) -> float:
            """
            Access to the Grain Size parameter in Texture Warp Mode.
            """
            ...

        @texture_grain_size.setter
        def texture_grain_size(self, value) -> None:
            ...

        @property
        def tones_grain_size(self) -> float:
            """
            Access to the Grain Size parameter in Tones Warp Mode.
            """
            ...

        @tones_grain_size.setter
        def tones_grain_size(self, value) -> None:
            ...

        @property
        def warp_markers(self) -> tuple[WarpMarker, ...]:
            """
            Get the warp markers for this sample.
            """
            ...

        @property
        def warp_mode(self) -> int:
            """
            Access to the sample's warp mode.
            """
            ...

        @warp_mode.setter
        def warp_mode(self, value) -> None:
            ...

        @property
        def warping(self) -> bool:
            """
            Access to the sample's warping property.
            """
            ...

        @warping.setter
        def warping(self, value) -> None:
            ...

        def add_beats_granulation_resolution_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "beats_granulation_resolution" has changed.
            """
            ...

        def add_beats_transient_envelope_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "beats_transient_envelope" has changed.
            """
            ...

        def add_beats_transient_loop_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "beats_transient_loop_mode" has changed.
            """
            ...

        def add_complex_pro_envelope_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "complex_pro_envelope" has changed.
            """
            ...

        def add_complex_pro_formants_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "complex_pro_formants" has changed.
            """
            ...

        def add_end_marker_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "end_marker" has changed.
            """
            ...

        def add_file_path_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "file_path" has changed.
            """
            ...

        def add_gain_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "gain" has changed.
            """
            ...

        def add_slices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slices" has changed.
            """
            ...

        def add_slicing_beat_division_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_beat_division" has changed.
            """
            ...

        def add_slicing_region_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_region_count" has changed.
            """
            ...

        def add_slicing_sensitivity_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_sensitivity" has changed.
            """
            ...

        def add_slicing_style_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_style" has changed.
            """
            ...

        def add_start_marker_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "start_marker" has changed.
            """
            ...

        def add_texture_flux_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "texture_flux" has changed.
            """
            ...

        def add_texture_grain_size_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "texture_grain_size" has changed.
            """
            ...

        def add_tones_grain_size_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tones_grain_size" has changed.
            """
            ...

        def add_warp_markers_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warp_markers" has changed.
            """
            ...

        def add_warp_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warp_mode" has changed.
            """
            ...

        def add_warping_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "warping" has changed.
            """
            ...

        def beat_to_sample_time(self, beat_time: float) -> float:
            """
            Converts the given beat time to sample time. Raises an error if the sample is not warped.
            """
            ...

        def beats_granulation_resolution_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "beats_granulation_resolution".
            """
            ...

        def beats_transient_envelope_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "beats_transient_envelope".
            """
            ...

        def beats_transient_loop_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "beats_transient_loop_mode".
            """
            ...

        def clear_slices(self) -> None:
            """
            Clears all slices created in Simpler's manual mode.
            """
            ...

        def complex_pro_envelope_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "complex_pro_envelope".
            """
            ...

        def complex_pro_formants_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "complex_pro_formants".
            """
            ...

        def end_marker_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "end_marker".
            """
            ...

        def file_path_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "file_path".
            """
            ...

        def gain_display_string(self) -> str:
            """
            Get the gain's display value as a string.
            """
            ...

        def gain_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "gain".
            """
            ...

        def insert_slice(self, slice_time: int) -> None:
            """
            Add a slice point at the provided time if there is none.
            """
            ...

        def move_slice(self, old_time: int, new_time: int) -> int:
            """
            Move the slice point at the provided time.
            """
            ...

        def remove_beats_granulation_resolution_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "beats_granulation_resolution".
            """
            ...

        def remove_beats_transient_envelope_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "beats_transient_envelope".
            """
            ...

        def remove_beats_transient_loop_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "beats_transient_loop_mode".
            """
            ...

        def remove_complex_pro_envelope_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "complex_pro_envelope".
            """
            ...

        def remove_complex_pro_formants_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "complex_pro_formants".
            """
            ...

        def remove_end_marker_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "end_marker".
            """
            ...

        def remove_file_path_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "file_path".
            """
            ...

        def remove_gain_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "gain".
            """
            ...

        def remove_slice(self, slice_time: int) -> None:
            """
            Remove the slice point at the provided time if there is one.
            """
            ...

        def remove_slices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slices".
            """
            ...

        def remove_slicing_beat_division_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_beat_division".
            """
            ...

        def remove_slicing_region_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_region_count".
            """
            ...

        def remove_slicing_sensitivity_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_sensitivity".
            """
            ...

        def remove_slicing_style_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_style".
            """
            ...

        def remove_start_marker_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "start_marker".
            """
            ...

        def remove_texture_flux_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "texture_flux".
            """
            ...

        def remove_texture_grain_size_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "texture_grain_size".
            """
            ...

        def remove_tones_grain_size_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tones_grain_size".
            """
            ...

        def remove_warp_markers_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warp_markers".
            """
            ...

        def remove_warp_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warp_mode".
            """
            ...

        def remove_warping_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "warping".
            """
            ...

        def reset_slices(self) -> None:
            """
            Resets all edited slices to their original positions.
            """
            ...

        def sample_to_beat_time(self, sample_time: float) -> float:
            """
            Converts the given sample time to beat time. Raises an error if the sample is not warped.
            """
            ...

        def slices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slices".
            """
            ...

        def slicing_beat_division_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_beat_division".
            """
            ...

        def slicing_region_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_region_count".
            """
            ...

        def slicing_sensitivity_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_sensitivity".
            """
            ...

        def slicing_style_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_style".
            """
            ...

        def start_marker_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "start_marker".
            """
            ...

        def texture_flux_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "texture_flux".
            """
            ...

        def texture_grain_size_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "texture_grain_size".
            """
            ...

        def tones_grain_size_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tones_grain_size".
            """
            ...

        def warp_markers_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warp_markers".
            """
            ...

        def warp_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warp_mode".
            """
            ...

        def warping_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "warping".
            """
            ...

    class SlicingBeatDivision:
        sixteenth: int = 0
        sixteenth_triplett: int = 1
        eighth: int = 2
        eighth_triplett: int = 3
        quarter: int = 4
        quarter_triplett: int = 5
        half: int = 6
        half_triplett: int = 7
        one_bar: int = 8
        two_bars: int = 9
        four_bars: int = 10

    class SlicingStyle:
        transient: int = 0
        beat: int = 1
        region: int = 2
        manual: int = 3

    class TransientLoopMode:
        off: int = 0
        forward: int = 1
        alternate: int = 2


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

        def add_tempo_enabled_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tempo_enabled" has changed.
            """
            ...

        def add_tempo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tempo" has changed.
            """
            ...

        def add_time_signature_denominator_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "time_signature_denominator" has changed.
            """
            ...

        def add_time_signature_enabled_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "time_signature_enabled" has changed.
            """
            ...

        def add_time_signature_numerator_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "time_signature_numerator" has changed.
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

        def remove_tempo_enabled_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tempo_enabled".
            """
            ...

        def remove_tempo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tempo".
            """
            ...

        def remove_time_signature_denominator_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "time_signature_denominator".
            """
            ...

        def remove_time_signature_enabled_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "time_signature_enabled".
            """
            ...

        def remove_time_signature_numerator_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "time_signature_numerator".
            """
            ...

        def set_fire_button_state(self, arg2: bool) -> None:
            """
            Set the scene's fire button state directly. Supports all launch modes.
            """
            ...

        def tempo_enabled_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tempo_enabled".
            """
            ...

        def tempo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tempo".
            """
            ...

        def time_signature_denominator_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "time_signature_denominator".
            """
            ...

        def time_signature_enabled_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "time_signature_enabled".
            """
            ...

        def time_signature_numerator_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "time_signature_numerator".
            """
            ...


class ShifterDevice(ModuleType):

    class ShifterDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Shifter device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def pitch_bend_range(self) -> int:
            """
            Return the pitch bend range for MIDI pitch mode
            """
            ...

        @pitch_bend_range.setter
        def pitch_bend_range(self, value) -> None:
            ...

        @property
        def pitch_mode_index(self) -> int:
            """
            Return the current pitch mode index
            """
            ...

        @pitch_mode_index.setter
        def pitch_mode_index(self, value) -> None:
            ...

        @property
        def pitch_mode_list(self) -> tuple[str, ...]:
            """
            Return the current pitch mode list
            """
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_bend_range" has changed.
            """
            ...

        def add_pitch_mode_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_mode_index" has changed.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def pitch_bend_range_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_bend_range".
            """
            ...

        def pitch_mode_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_mode_index".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_bend_range".
            """
            ...

        def remove_pitch_mode_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_mode_index".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> ShifterDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class SimplerDevice(ModuleType):

    @staticmethod
    def get_available_voice_numbers() -> IntVector:
        """
        Get a vector of valid Simpler voice numbers.
        """
        ...

    class PlaybackMode:
        classic: int = 0
        one_shot: int = 1
        slicing: int = 2

    class SimplerDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Simpler device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def can_warp_as(self) -> bool:
            """
            Returns true if warp_as is available.
            """
            ...

        @property
        def can_warp_double(self) -> bool:
            """
            Returns true if warp_double is available.
            """
            ...

        @property
        def can_warp_half(self) -> bool:
            """
            Returns true if warp_half is available.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def multi_sample_mode(self) -> bool:
            """
            Returns whether Simpler is in mulit-sample mode.
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def note_pitch_bend_range(self) -> int:
            """
            Access to the Note Pitch Bend Range in Simpler.
            """
            ...

        @note_pitch_bend_range.setter
        def note_pitch_bend_range(self, value) -> None:
            ...

        @property
        def pad_slicing(self) -> bool:
            """
            When set to true, slices can be added in slicing mode by playing notes .that are not assigned to slices, yet.
            """
            ...

        @pad_slicing.setter
        def pad_slicing(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def pitch_bend_range(self) -> int:
            """
            Access to the Pitch Bend Range in Simpler.
            """
            ...

        @pitch_bend_range.setter
        def pitch_bend_range(self, value) -> None:
            ...

        @property
        def playback_mode(self) -> int:
            """
            Access to Simpler's playback mode.
            """
            ...

        @playback_mode.setter
        def playback_mode(self, value) -> None:
            ...

        @property
        def playing_position(self) -> float:
            """
            Constant access to the current playing position in the sample.The returned value is the normalized position between sample start and end.
            """
            ...

        @property
        def playing_position_enabled(self) -> bool:
            """
            Returns whether Simpler is showing the playing position.The returned value is True while the sample is played back
            """
            ...

        @property
        def retrigger(self) -> bool:
            """
            Access to Simpler's retrigger mode.
            """
            ...

        @retrigger.setter
        def retrigger(self, value) -> None:
            ...

        @property
        def sample(self) -> None:
            """
            Get the loaded Sample.
            """
            ...

        @property
        def slicing_playback_mode(self) -> int:
            """
            Access to Simpler's slicing playback mode.
            """
            ...

        @slicing_playback_mode.setter
        def slicing_playback_mode(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        @property
        def voices(self) -> int:
            """
            Access to the number of voices in Simpler.
            """
            ...

        @voices.setter
        def voices(self, value) -> None:
            ...

        def add_can_warp_as_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_warp_as" has changed.
            """
            ...

        def add_can_warp_double_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_warp_double" has changed.
            """
            ...

        def add_can_warp_half_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_warp_half" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_multi_sample_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "multi_sample_mode" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_note_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "note_pitch_bend_range" has changed.
            """
            ...

        def add_pad_slicing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pad_slicing" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_bend_range" has changed.
            """
            ...

        def add_playback_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playback_mode" has changed.
            """
            ...

        def add_playing_position_enabled_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_position_enabled" has changed.
            """
            ...

        def add_playing_position_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_position" has changed.
            """
            ...

        def add_retrigger_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "retrigger" has changed.
            """
            ...

        def add_sample_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "sample" has changed.
            """
            ...

        def add_slicing_playback_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "slicing_playback_mode" has changed.
            """
            ...

        def add_voices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "voices" has changed.
            """
            ...

        def can_warp_as_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_warp_as".
            """
            ...

        def can_warp_double_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_warp_double".
            """
            ...

        def can_warp_half_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_warp_half".
            """
            ...

        def crop(self) -> None:
            """
            Crop the loaded sample to the active area between start- and end marker. Calling this method on an empty simpler raises an error.
            """
            ...

        def guess_playback_length(self) -> float:
            """
            Return an estimated beat time for the playback length between start- and end-marker. Calling this method on an empty simpler raises an error.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def multi_sample_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "multi_sample_mode".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def note_pitch_bend_range_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "note_pitch_bend_range".
            """
            ...

        def pad_slicing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pad_slicing".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def pitch_bend_range_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_bend_range".
            """
            ...

        def playback_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playback_mode".
            """
            ...

        def playing_position_enabled_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_position_enabled".
            """
            ...

        def playing_position_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_position".
            """
            ...

        def remove_can_warp_as_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_warp_as".
            """
            ...

        def remove_can_warp_double_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_warp_double".
            """
            ...

        def remove_can_warp_half_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_warp_half".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_multi_sample_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "multi_sample_mode".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_note_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "note_pitch_bend_range".
            """
            ...

        def remove_pad_slicing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pad_slicing".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_bend_range".
            """
            ...

        def remove_playback_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playback_mode".
            """
            ...

        def remove_playing_position_enabled_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_position_enabled".
            """
            ...

        def remove_playing_position_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_position".
            """
            ...

        def remove_retrigger_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "retrigger".
            """
            ...

        def remove_sample_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "sample".
            """
            ...

        def remove_slicing_playback_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "slicing_playback_mode".
            """
            ...

        def remove_voices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "voices".
            """
            ...

        def retrigger_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "retrigger".
            """
            ...

        def reverse(self) -> None:
            """
            Reverse the loaded sample. Calling this method on an empty simpler raises an error.
            """
            ...

        def sample_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "sample".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def slicing_playback_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "slicing_playback_mode".
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def voices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "voices".
            """
            ...

        def warp_as(self, beat_time: float) -> None:
            """
            Warp the playback region between start- and end-marker as the given length. Calling this method on an empty simpler raises an error.
            """
            ...

        def warp_double(self) -> None:
            """
            Doubles the tempo for region between start- and end-marker.
            """
            ...

        def warp_half(self) -> None:
            """
            Halves the tempo for region between start- and end-marker.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a simpler device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> SimplerDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            @property
            def sample_end(self) -> int:
                """
                Access to the modulated samples end position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_env_fade_in(self) -> int:
                """
                Access to the envelope fade-in time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_env_fade_out(self) -> int:
                """
                Access to the envelope fade-out time in samples. Returned value is only in use when Simpler is in one-shot mode. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_loop_end(self) -> int:
                """
                Access to the modulated samples loop end position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_loop_fade(self) -> int:
                """
                Access to the modulated samples loop fade position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_loop_start(self) -> int:
                """
                Access to the modulated samples loop start position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def sample_start(self) -> int:
                """
                Access to the modulated samples start position in samples. Returns -1 in case there is no sample loaded.
                """
                ...

            @property
            def selected_slice(self) -> int:
                """
                Access to the selected slice.
                """
                ...

            @selected_slice.setter
            def selected_slice(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def add_sample_end_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_end" has changed.
                """
                ...

            def add_sample_env_fade_in_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_env_fade_in" has changed.
                """
                ...

            def add_sample_env_fade_out_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_env_fade_out" has changed.
                """
                ...

            def add_sample_loop_end_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_loop_end" has changed.
                """
                ...

            def add_sample_loop_fade_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_loop_fade" has changed.
                """
                ...

            def add_sample_loop_start_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_loop_start" has changed.
                """
                ...

            def add_sample_start_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "sample_start" has changed.
                """
                ...

            def add_selected_slice_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_slice" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...

            def remove_sample_end_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_end".
                """
                ...

            def remove_sample_env_fade_in_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_env_fade_in".
                """
                ...

            def remove_sample_env_fade_out_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_env_fade_out".
                """
                ...

            def remove_sample_loop_end_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_loop_end".
                """
                ...

            def remove_sample_loop_fade_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_loop_fade".
                """
                ...

            def remove_sample_loop_start_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_loop_start".
                """
                ...

            def remove_sample_start_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "sample_start".
                """
                ...

            def remove_selected_slice_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_slice".
                """
                ...

            def sample_end_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_end".
                """
                ...

            def sample_env_fade_in_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_env_fade_in".
                """
                ...

            def sample_env_fade_out_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_env_fade_out".
                """
                ...

            def sample_loop_end_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_loop_end".
                """
                ...

            def sample_loop_fade_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_loop_fade".
                """
                ...

            def sample_loop_start_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_loop_start".
                """
                ...

            def sample_start_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "sample_start".
                """
                ...

            def selected_slice_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_slice".
                """
                ...

    class SlicingPlaybackMode:
        mono: int = 0
        poly: int = 1
        thru: int = 2


class Song(ModuleType):

    @staticmethod
    def get_all_scales_ordered() -> tuple:
        """
        Get an ordered tuple of tuples of all available scale names to intervals.
        """
        ...

    class BeatTime(object):
        def __init__(self, *a, **k):
            """
            Represents a Time, splitted into Bars, Beats, SubDivision and Ticks.
            """
            ...

        @property
        def bars(self) -> int:
            ...

        @bars.setter
        def bars(self, value) -> None:
            ...

        @property
        def beats(self) -> int:
            ...

        @beats.setter
        def beats(self, value) -> None:
            ...

        @property
        def sub_division(self) -> int:
            ...

        @sub_division.setter
        def sub_division(self, value) -> None:
            ...

        @property
        def ticks(self) -> int:
            ...

        @ticks.setter
        def ticks(self, value) -> None:
            ...

    class CaptureDestination:
        """
        The destination for MIDI capture.
        """
        auto: int = 0
        session: int = 1
        arrangement: int = 2

    class CaptureMode:
        """
        The capture mode that is used for capture and insert scene.
        """
        all: int = 0
        all_except_selected: int = 1

    class CuePoint(object):
        def __init__(self, *a, **k):
            """
            Represents a 'Marker' in the arrangement.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Song:
            """
            Get the canonical parent of the cue point.
            """
            ...

        @property
        def name(self) -> str:
            """
            Get/Set/Listen to the name of this CuePoint, as visible in the arranger.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def time(self) -> float:
            """
            Get/Listen to the CuePoint's time in beats.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_time_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "time" has changed.
            """
            ...

        def jump(self) -> None:
            """
            When the Song is playing, set the playing-position quantized to this Cuepoint's time. When not playing, simply move the start playing position.
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_time_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "time".
            """
            ...

        def time_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "time".
            """
            ...

    class Quantization:
        q_no_q: int = 0
        q_8_bars: int = 1
        q_4_bars: int = 2
        q_2_bars: int = 3
        q_bar: int = 4
        q_half: int = 5
        q_half_triplet: int = 6
        q_quarter: int = 7
        q_quarter_triplet: int = 8
        q_eight: int = 9
        q_eight_triplet: int = 10
        q_sixtenth: int = 11
        q_sixtenth_triplet: int = 12
        q_thirtytwoth: int = 13

    class RecordingQuantization:
        rec_q_no_q: int = 0
        rec_q_quarter: int = 1
        rec_q_eight: int = 2
        rec_q_eight_triplet: int = 3
        rec_q_eight_eight_triplet: int = 4
        rec_q_sixtenth: int = 5
        rec_q_sixtenth_triplet: int = 6
        rec_q_sixtenth_sixtenth_triplet: int = 7
        rec_q_thirtysecond: int = 8

    class SessionRecordStatus:
        off: int = 0
        on: int = 1
        transition: int = 2

    class SmptTime(object):
        def __init__(self, *a, **k):
            """
            Represents a Time, split into Hours, Minutes, Seconds and Frames.The frame type must be specified when calling a function that returnsa SmptTime.
            """
            ...

        @property
        def frames(self) -> int:
            ...

        @frames.setter
        def frames(self, value) -> None:
            ...

        @property
        def hours(self) -> int:
            ...

        @hours.setter
        def hours(self, value) -> None:
            ...

        @property
        def minutes(self) -> int:
            ...

        @minutes.setter
        def minutes(self, value) -> None:
            ...

        @property
        def seconds(self) -> int:
            ...

        @seconds.setter
        def seconds(self, value) -> None:
            ...

    class Song(object):
        def __init__(self, *a, **k):
            """
            This class represents a Live set.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def appointed_device(self) -> None:
            """
            Read, write, and listen access to the appointed Device
            """
            ...

        @appointed_device.setter
        def appointed_device(self, value) -> None:
            ...

        @property
        def arrangement_overdub(self) -> bool:
            """
            Get/Set the global arrangement overdub state.
            """
            ...

        @arrangement_overdub.setter
        def arrangement_overdub(self, value) -> None:
            ...

        @property
        def back_to_arranger(self) -> bool:
            """
            Get/Set if triggering a Clip in the Session, disabled the playback ofClips in the Arranger.
            """
            ...

        @back_to_arranger.setter
        def back_to_arranger(self, value) -> None:
            ...

        @property
        def can_capture_midi(self) -> bool:
            """
            Get whether there currently is material to be captured on any tracks.
            """
            ...

        @property
        def can_jump_to_next_cue(self) -> bool:
            """
            Returns true when there is a cue marker right to the playing pos thatwe could jump to.
            """
            ...

        @property
        def can_jump_to_prev_cue(self) -> bool:
            """
            Returns true when there is a cue marker left to the playing pos thatwe could jump to.
            """
            ...

        @property
        def can_redo(self) -> bool:
            """
            Returns true if there is an undone action that we can redo.
            """
            ...

        @property
        def can_undo(self) -> bool:
            """
            Returns true if there is an action that we can restore.
            """
            ...

        @property
        def canonical_parent(self) -> None:
            """
            Get the canonical parent of the song.
            """
            ...

        @property
        def clip_trigger_quantization(self) -> Quantization:
            """
            Get/Set access to the quantization settings that are used to fireClips in the Session.
            """
            ...

        @clip_trigger_quantization.setter
        def clip_trigger_quantization(self, value) -> None:
            ...

        @property
        def count_in_duration(self) -> int:
            """
            Get the count in duration. Returns an index, mapped as follows: 0 - None, 1 - 1 Bar, 2 - 2 Bars, 3 - 4 Bars.
            """
            ...

        @property
        def cue_points(self) -> tuple:
            """
            Const access to a list of all cue points of the Live Song.
            """
            ...

        @property
        def current_song_time(self) -> float:
            """
            Get/Set access to the songs current playing position in beats.
            """
            ...

        @current_song_time.setter
        def current_song_time(self, value) -> None:
            ...

        @property
        def exclusive_arm(self) -> bool:
            """
            Get if Tracks should be armed exclusively by default.
            """
            ...

        @property
        def exclusive_solo(self) -> bool:
            """
            Get if Tracks should be soloed exclusively by default.
            """
            ...

        @property
        def file_path(self) -> str:
            """
            Get the current Live Set's path on disk.
            """
            ...

        @property
        def groove_amount(self) -> float:
            """
            Get/Set the global groove amount, that adjust all setup groovesin all clips.
            """
            ...

        @groove_amount.setter
        def groove_amount(self, value) -> None:
            ...

        @property
        def groove_pool(self) -> GroovePool:
            """
            Get the groove pool.
            """
            ...

        @property
        def is_ableton_link_enabled(self) -> bool:
            """
            Enable/disable Ableton Link.
            """
            ...

        @is_ableton_link_enabled.setter
        def is_ableton_link_enabled(self, value) -> None:
            ...

        @property
        def is_ableton_link_start_stop_sync_enabled(self) -> bool:
            """
            Enable/disable Ableton Link Start Stop Sync.
            """
            ...

        @is_ableton_link_start_stop_sync_enabled.setter
        def is_ableton_link_start_stop_sync_enabled(self, value) -> None:
            ...

        @property
        def is_counting_in(self) -> bool:
            """
            Get whether currently counting in.
            """
            ...

        @property
        def is_playing(self) -> bool:
            """
            Returns true if the Song is currently playing.
            """
            ...

        @is_playing.setter
        def is_playing(self, value) -> None:
            ...

        @property
        def last_event_time(self) -> float:
            """
            Return the time of the last set event in the song. In contrary tosong_length, this will not add some extra beats that are mostly neededfor Display purposes in the Arrangerview.
            """
            ...

        @property
        def loop(self) -> bool:
            """
            Get/Set the looping flag that en/disables the usage of the globalloop markers in the song.
            """
            ...

        @loop.setter
        def loop(self, value) -> None:
            ...

        @property
        def loop_length(self) -> float:
            """
            Get/Set the length of the global loop marker position in beats.
            """
            ...

        @loop_length.setter
        def loop_length(self, value) -> None:
            ...

        @property
        def loop_start(self) -> float:
            """
            Get/Set the start of the global loop marker position in beats.
            """
            ...

        @loop_start.setter
        def loop_start(self, value) -> None:
            ...

        @property
        def master_track(self) -> Track:
            """
            Access to the Main Track (always available)
            """
            ...

        @property
        def metronome(self) -> bool:
            """
            Get/Set if the metronom is audible.
            """
            ...

        @metronome.setter
        def metronome(self, value) -> None:
            ...

        @property
        def midi_recording_quantization(self) -> RecordingQuantization:
            """
            Get/Set access to the settings that are used to quantizeMIDI recordings.
            """
            ...

        @midi_recording_quantization.setter
        def midi_recording_quantization(self, value) -> None:
            ...

        @property
        def name(self) -> str:
            """
            Get the current Live Set's name.
            """
            ...

        @property
        def nudge_down(self) -> bool:
            """
            Get/Set the status of the nudge down button.
            """
            ...

        @nudge_down.setter
        def nudge_down(self, value) -> None:
            ...

        @property
        def nudge_up(self) -> bool:
            """
            Get/Set the status of the nudge up button.
            """
            ...

        @nudge_up.setter
        def nudge_up(self, value) -> None:
            ...

        @property
        def overdub(self) -> bool:
            """
            Legacy hook for Live 8 overdub state. Now hooks tosession record, but never starts playback.
            """
            ...

        @overdub.setter
        def overdub(self, value) -> None:
            ...

        @property
        def punch_in(self) -> bool:
            """
            Get/Set the flag that will enable recording as soon as the Song playsand hits the global loop start region.
            """
            ...

        @punch_in.setter
        def punch_in(self, value) -> None:
            ...

        @property
        def punch_out(self) -> bool:
            """
            Get/Set the flag that will disable recording as soon as the Song playsand hits the global loop end region.
            """
            ...

        @punch_out.setter
        def punch_out(self, value) -> None:
            ...

        @property
        def re_enable_automation_enabled(self) -> bool:
            """
            Returns true if some automated parameter has been overriden
            """
            ...

        @property
        def record_mode(self) -> bool:
            """
            Get/Set the state of the global recording flag.
            """
            ...

        @record_mode.setter
        def record_mode(self, value) -> None:
            ...

        @property
        def return_tracks(self) -> tuple:
            """
            Const access to the list of available Return Tracks.
            """
            ...

        @property
        def root_note(self) -> int:
            """
            Set and access the root (i.e. key) of the song. The root can be a number between 0 and 11, with 0 corresponding to C and 11 corresponding to B.
            """
            ...

        @root_note.setter
        def root_note(self, value) -> None:
            ...

        @property
        def scale_intervals(self) -> tuple[int, ...]:
            """
            Reports the current scale's intervals as a list of integers, starting with the root and representing the number of halfsteps (e.g. Major -> 0, 2, 4, 5, 7, 9, 11)
            """
            ...

        @property
        def scale_mode(self) -> bool:
            """
            Access to the Scale Mode setting in Live. When on, key tracks that belong to the currently selected scale are highlighted in Live's MIDI Note Editor, and pitch-based parameters in MIDI Tools and Devices can be edited in scale degrees rather than semitones.
            """
            ...

        @scale_mode.setter
        def scale_mode(self, value) -> None:
            ...

        @property
        def scale_name(self) -> str:
            """
            Set and access the currently selected scale by name. The default scale names that can be saved with a set and recalled are'Major', 'Minor', 'Dorian', 'Mixolydian' ,'Lydian' ,'Phrygian' ,'Locrian', 'Whole Tone', 'Half-whole Dim.', 'Whole-half Dim.', 'Minor Blues', 'Minor Pentatonic', 'Major Pentatonic', 'Harmonic Minor', 'Harmonic Major', 'Dorian #4', 'Phrygian Dominant', 'Melodic Minor', 'Lydian Augmented', 'Lydian Dominant', 'Super Locrian', 'Bhairav', 'Hungarian Minor', '8-Tone Spanish', 'Hirajoshi', 'In-Sen', 'Iwato', 'Kumoi', 'Pelog Selisir', 'Pelog Tembung', 'Messiaen 3', 'Messiaen 4', 'Messiaen 5', 'Messiaen 6', 'Messiaen 7'
            """
            ...

        @scale_name.setter
        def scale_name(self, value) -> None:
            ...

        @property
        def scenes(self) -> tuple:
            """
            Const access to a list of all Scenes in the Live Song.
            """
            ...

        @property
        def select_on_launch(self) -> bool:
            """
            Get if Scenes and Clips should be selected when fired.
            """
            ...

        @property
        def session_automation_record(self) -> bool:
            """
            Returns true if automation recording is enabled.
            """
            ...

        @session_automation_record.setter
        def session_automation_record(self, value) -> None:
            ...

        @property
        def session_record(self) -> bool:
            """
            Get/Set the session record state.
            """
            ...

        @session_record.setter
        def session_record(self, value) -> None:
            ...

        @property
        def session_record_status(self) -> int:
            """
            Get the session slot-recording state.
            """
            ...

        @property
        def signature_denominator(self) -> int:
            """
            Get/Set access to the global signature denominator of the Song.
            """
            ...

        @signature_denominator.setter
        def signature_denominator(self, value) -> None:
            ...

        @property
        def signature_numerator(self) -> int:
            """
            Get/Set access to the global signature numerator of the Song.
            """
            ...

        @signature_numerator.setter
        def signature_numerator(self, value) -> None:
            ...

        @property
        def song_length(self) -> float:
            """
            Return the time of the last set event in the song, plus som extra beatsthat are usually added for better navigation in the arrangerview.
            """
            ...

        @property
        def start_time(self) -> float:
            """
            Get/Set access to the songs current start time in beats. The set timemay be overridden by the current loop/locator start time.
            """
            ...

        @start_time.setter
        def start_time(self, value) -> None:
            ...

        @property
        def swing_amount(self) -> float:
            """
            Get/Set access to the amount of swing that is applied when adding or quantizing notes to MIDI clips
            """
            ...

        @swing_amount.setter
        def swing_amount(self, value) -> None:
            ...

        @property
        def tempo(self) -> float:
            """
            Get/Set the global project tempo.
            """
            ...

        @tempo.setter
        def tempo(self, value) -> None:
            ...

        @property
        def tempo_follower_enabled(self) -> bool:
            """
            Get/Set whether the Tempo Follower is controlling the tempo. The Tempo Follower Toggle must be made visible in the preferences for this property to be effective.
            """
            ...

        @tempo_follower_enabled.setter
        def tempo_follower_enabled(self, value) -> None:
            ...

        @property
        def tracks(self) -> tuple:
            """
            Const access to a list of all Player Tracks in the Live Song, excludingthe return and Main Track (see also Song.send_tracks and Song.master_track).At least one MIDI or Audio Track is always available.
            """
            ...

        @property
        def tuning_system(self) -> TuningSystem:
            """
            Access the currently active tuning system.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a Live document: The Session and Arrangerview.
            """
            ...

        @property
        def visible_tracks(self) -> tuple:
            """
            Const access to a list of all visible Player Tracks in the Live Song, excludingthe return and Main Track (see also Song.send_tracks and Song.master_track).At least one MIDI or Audio Track is always available.
            """
            ...

        def add_appointed_device_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "appointed_device" has changed.
            """
            ...

        def add_arrangement_overdub_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "arrangement_overdub" has changed.
            """
            ...

        def add_back_to_arranger_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "back_to_arranger" has changed.
            """
            ...

        def add_can_capture_midi_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_capture_midi" has changed.
            """
            ...

        def add_can_jump_to_next_cue_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_jump_to_next_cue" has changed.
            """
            ...

        def add_can_jump_to_prev_cue_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "can_jump_to_prev_cue" has changed.
            """
            ...

        def add_clip_trigger_quantization_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "clip_trigger_quantization" has changed.
            """
            ...

        def add_count_in_duration_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "count_in_duration" has changed.
            """
            ...

        def add_cue_points_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "cue_points" has changed.
            """
            ...

        def add_current_song_time_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_song_time" has changed.
            """
            ...

        def add_data_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "data" has changed.
            """
            ...

        def add_exclusive_arm_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "exclusive_arm" has changed.
            """
            ...

        def add_groove_amount_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "groove_amount" has changed.
            """
            ...

        def add_is_ableton_link_enabled_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_ableton_link_enabled" has changed.
            """
            ...

        def add_is_ableton_link_start_stop_sync_enabled_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_ableton_link_start_stop_sync_enabled" has changed.
            """
            ...

        def add_is_counting_in_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_counting_in" has changed.
            """
            ...

        def add_is_playing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_playing" has changed.
            """
            ...

        def add_loop_length_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "loop_length" has changed.
            """
            ...

        def add_loop_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "loop" has changed.
            """
            ...

        def add_loop_start_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "loop_start" has changed.
            """
            ...

        def add_metronome_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "metronome" has changed.
            """
            ...

        def add_midi_recording_quantization_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_recording_quantization" has changed.
            """
            ...

        def add_nudge_down_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "nudge_down" has changed.
            """
            ...

        def add_nudge_up_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "nudge_up" has changed.
            """
            ...

        def add_overdub_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "overdub" has changed.
            """
            ...

        def add_punch_in_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "punch_in" has changed.
            """
            ...

        def add_punch_out_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "punch_out" has changed.
            """
            ...

        def add_re_enable_automation_enabled_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "re_enable_automation_enabled" has changed.
            """
            ...

        def add_record_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "record_mode" has changed.
            """
            ...

        def add_return_tracks_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "return_tracks" has changed.
            """
            ...

        def add_root_note_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "root_note" has changed.
            """
            ...

        def add_scale_information_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "scale_information" has changed.
            """
            ...

        def add_scale_intervals_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "scale_intervals" has changed.
            """
            ...

        def add_scale_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "scale_mode" has changed.
            """
            ...

        def add_scale_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "scale_name" has changed.
            """
            ...

        def add_scenes_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "scenes" has changed.
            """
            ...

        def add_session_automation_record_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "session_automation_record" has changed.
            """
            ...

        def add_session_record_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "session_record" has changed.
            """
            ...

        def add_session_record_status_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "session_record_status" has changed.
            """
            ...

        def add_signature_denominator_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "signature_denominator" has changed.
            """
            ...

        def add_signature_numerator_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "signature_numerator" has changed.
            """
            ...

        def add_song_length_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "song_length" has changed.
            """
            ...

        def add_start_time_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "start_time" has changed.
            """
            ...

        def add_swing_amount_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "swing_amount" has changed.
            """
            ...

        def add_tempo_follower_enabled_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tempo_follower_enabled" has changed.
            """
            ...

        def add_tempo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tempo" has changed.
            """
            ...

        def add_tracks_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tracks" has changed.
            """
            ...

        def add_tuning_system_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "tuning_system" has changed.
            """
            ...

        def add_visible_tracks_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "visible_tracks" has changed.
            """
            ...

        def appointed_device_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "appointed_device".
            """
            ...

        def arrangement_overdub_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "arrangement_overdub".
            """
            ...

        def back_to_arranger_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "back_to_arranger".
            """
            ...

        def begin_undo_step(self) -> None:
            ...

        def can_capture_midi_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_capture_midi".
            """
            ...

        def can_jump_to_next_cue_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_jump_to_next_cue".
            """
            ...

        def can_jump_to_prev_cue_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "can_jump_to_prev_cue".
            """
            ...

        def capture_and_insert_scene(self, CaptureMode: int=Song.CaptureMode.all) -> None:
            """
            Capture currently playing clips and insert them as a new scene after the selected scene. Raises a runtime error if creating a new scene would exceed the limitations.
            """
            ...

        def capture_midi(self, Destination: int=Song.CaptureDestination.auto) -> None:
            """
            Capture recently played MIDI material from audible tracks. If no Destination is given or Destination is set to CaptureDestination.auto, the captured material is inserted into the Session or Arrangement depending on which is visible. If Destination is set to CaptureDestination.session or CaptureDestination.arrangement, inserts the material into Session or Arrangement, respectively. Raises a limitation error when capturing into the Session and a new scene would have to be created but can't because it would exceed the limitations.
            """
            ...

        def clip_trigger_quantization_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "clip_trigger_quantization".
            """
            ...

        def continue_playing(self) -> None:
            """
            Continue playing the song from the current position
            """
            ...

        def count_in_duration_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "count_in_duration".
            """
            ...

        def create_audio_track(self, Index: object=None) -> Track:
            """
            Create a new audio track at the optional given index and return it.If the index is -1, the new track is added at the end. It will create a default audio track if possible. If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item
            """
            ...

        def create_midi_track(self, Index: object=None) -> Track:
            """
            Create a new midi track at the optional given index and return it.If the index is -1,  the new track is added at the end.It will create a default midi track if possible. If the index is invalid or the new track would exceed the limitations, a limitation error is raised.If the index is missing, the track is created after the last selected item
            """
            ...

        def create_return_track(self) -> Track:
            """
            Create a new return track at the end and return it. If the new track would exceed  the limitations, a limitation error is raised.  If the maximum number of return tracks is exceeded, a RuntimeError is raised.
            """
            ...

        def create_scene(self, arg2: int) -> Scene:
            """
            Create a new scene at the given index. If the index is -1, the new scene is added at the end. If the index is invalid or the new scene would exceed the limitations, a limitation error is raised.
            """
            ...

        def cue_points_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "cue_points".
            """
            ...

        def current_song_time_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_song_time".
            """
            ...

        def data_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "data".
            """
            ...

        def delete_return_track(self, arg2: int) -> None:
            """
            Delete the return track with the given index. If no track with this index exists, an exception will be raised.
            """
            ...

        def delete_scene(self, arg2: int) -> None:
            """
            Delete the scene with the given index. If no scene with this index exists, an exception will be raised.
            """
            ...

        def delete_track(self, arg2: int) -> None:
            """
            Delete the track with the given index. If no track with this index exists, an exception will be raised.
            """
            ...

        def duplicate_scene(self, arg2: int) -> None:
            """
            Duplicates a scene and selects the new one. Raises a limitation error if creating a new scene would exceed the limitations.
            """
            ...

        def duplicate_track(self, arg2: int) -> None:
            """
            Duplicates a track and selects the new one. If the track is inside a folded group track, the group track is unfolded. Raises a limitation error if creating a new track would exceed the limitations.
            """
            ...

        def end_undo_step(self) -> None:
            ...

        def exclusive_arm_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "exclusive_arm".
            """
            ...

        def find_device_position(self, device: Device, target: LomObject, target_position: int) -> int:
            """
            Returns the closest possible position to the given target, where the device can be inserted. If inserting is not possible at all (i.e. if the device type is wrong), -1 is returned.
            """
            ...

        def force_link_beat_time(self) -> None:
            """
            Force the Link timeline to jump to Lives current beat time. Danger: This can cause beat time discontinuities in other connected apps.
            """
            ...

        def get_beats_loop_length(self) -> BeatTime:
            """
            Get const access to the songs loop length, using a BeatTime class with the current global set signature.
            """
            ...

        def get_beats_loop_start(self) -> BeatTime:
            """
            Get const access to the songs loop start, using a BeatTime class with the current global set signature.
            """
            ...

        def get_current_beats_song_time(self) -> BeatTime:
            """
            Get const access to the songs current playing position, using a BeatTime class with the current global set signature.
            """
            ...

        def get_current_smpte_song_time(self, arg2: int) -> SmptTime:
            """
            Get const access to the songs current playing position, by specifying the SMPTE format in which you would like to receive the time.
            """
            ...

        def get_data(self, key: object, default_value: object) -> object:
            """
            Get data for the given key, that was previously stored using set_data.
            """
            ...

        def groove_amount_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "groove_amount".
            """
            ...

        def is_ableton_link_enabled_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_ableton_link_enabled".
            """
            ...

        def is_ableton_link_start_stop_sync_enabled_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_ableton_link_start_stop_sync_enabled".
            """
            ...

        def is_counting_in_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_counting_in".
            """
            ...

        def is_cue_point_selected(self) -> bool:
            """
            Return true if the global playing pos is currently on a cue point.
            """
            ...

        def is_playing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_playing".
            """
            ...

        def jump_by(self, arg2: float) -> None:
            """
            Set a new playing pos, relative to the current one.
            """
            ...

        def jump_to_next_cue(self) -> None:
            """
            Jump to the next cue (marker) if possible.
            """
            ...

        def jump_to_prev_cue(self) -> None:
            """
            Jump to the prior cue (marker) if possible.
            """
            ...

        def loop_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "loop".
            """
            ...

        def loop_length_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "loop_length".
            """
            ...

        def loop_start_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "loop_start".
            """
            ...

        def metronome_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "metronome".
            """
            ...

        def midi_recording_quantization_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_recording_quantization".
            """
            ...

        def move_device(self, device: Device, target: LomObject, target_position: int) -> int:
            """
            Move a device into the target at the given position, where 0 moves it before the first device and len(devices) moves it to the end of the device chain.If the device cannot be moved to this position, the nearest possible position is chosen. If the device type is not valid, a runtime error is raised.Returns the index, where the device was moved to.
            """
            ...

        def nudge_down_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "nudge_down".
            """
            ...

        def nudge_up_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "nudge_up".
            """
            ...

        def overdub_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "overdub".
            """
            ...

        def play_selection(self) -> None:
            """
            Start playing the current set selection, or do nothing if no selection is set.
            """
            ...

        def punch_in_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "punch_in".
            """
            ...

        def punch_out_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "punch_out".
            """
            ...

        def re_enable_automation(self) -> None:
            """
            Discards overrides of automated parameters.
            """
            ...

        def re_enable_automation_enabled_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "re_enable_automation_enabled".
            """
            ...

        def record_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "record_mode".
            """
            ...

        def redo(self) -> str:
            """
            Redo the last action that was undone.
            """
            ...

        def remove_appointed_device_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "appointed_device".
            """
            ...

        def remove_arrangement_overdub_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "arrangement_overdub".
            """
            ...

        def remove_back_to_arranger_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "back_to_arranger".
            """
            ...

        def remove_can_capture_midi_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_capture_midi".
            """
            ...

        def remove_can_jump_to_next_cue_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_jump_to_next_cue".
            """
            ...

        def remove_can_jump_to_prev_cue_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "can_jump_to_prev_cue".
            """
            ...

        def remove_clip_trigger_quantization_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "clip_trigger_quantization".
            """
            ...

        def remove_count_in_duration_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "count_in_duration".
            """
            ...

        def remove_cue_points_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "cue_points".
            """
            ...

        def remove_current_song_time_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_song_time".
            """
            ...

        def remove_data_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "data".
            """
            ...

        def remove_exclusive_arm_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "exclusive_arm".
            """
            ...

        def remove_groove_amount_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "groove_amount".
            """
            ...

        def remove_is_ableton_link_enabled_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_ableton_link_enabled".
            """
            ...

        def remove_is_ableton_link_start_stop_sync_enabled_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_ableton_link_start_stop_sync_enabled".
            """
            ...

        def remove_is_counting_in_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_counting_in".
            """
            ...

        def remove_is_playing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_playing".
            """
            ...

        def remove_loop_length_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "loop_length".
            """
            ...

        def remove_loop_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "loop".
            """
            ...

        def remove_loop_start_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "loop_start".
            """
            ...

        def remove_metronome_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "metronome".
            """
            ...

        def remove_midi_recording_quantization_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_recording_quantization".
            """
            ...

        def remove_nudge_down_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "nudge_down".
            """
            ...

        def remove_nudge_up_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "nudge_up".
            """
            ...

        def remove_overdub_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "overdub".
            """
            ...

        def remove_punch_in_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "punch_in".
            """
            ...

        def remove_punch_out_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "punch_out".
            """
            ...

        def remove_re_enable_automation_enabled_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "re_enable_automation_enabled".
            """
            ...

        def remove_record_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "record_mode".
            """
            ...

        def remove_return_tracks_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "return_tracks".
            """
            ...

        def remove_root_note_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "root_note".
            """
            ...

        def remove_scale_information_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "scale_information".
            """
            ...

        def remove_scale_intervals_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "scale_intervals".
            """
            ...

        def remove_scale_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "scale_mode".
            """
            ...

        def remove_scale_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "scale_name".
            """
            ...

        def remove_scenes_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "scenes".
            """
            ...

        def remove_session_automation_record_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "session_automation_record".
            """
            ...

        def remove_session_record_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "session_record".
            """
            ...

        def remove_session_record_status_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "session_record_status".
            """
            ...

        def remove_signature_denominator_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "signature_denominator".
            """
            ...

        def remove_signature_numerator_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "signature_numerator".
            """
            ...

        def remove_song_length_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "song_length".
            """
            ...

        def remove_start_time_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "start_time".
            """
            ...

        def remove_swing_amount_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "swing_amount".
            """
            ...

        def remove_tempo_follower_enabled_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tempo_follower_enabled".
            """
            ...

        def remove_tempo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tempo".
            """
            ...

        def remove_tracks_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tracks".
            """
            ...

        def remove_tuning_system_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "tuning_system".
            """
            ...

        def remove_visible_tracks_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "visible_tracks".
            """
            ...

        def return_tracks_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "return_tracks".
            """
            ...

        def root_note_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "root_note".
            """
            ...

        def scale_information_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "scale_information".
            """
            ...

        def scale_intervals_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "scale_intervals".
            """
            ...

        def scale_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "scale_mode".
            """
            ...

        def scale_name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "scale_name".
            """
            ...

        def scenes_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "scenes".
            """
            ...

        def scrub_by(self, arg2: float) -> None:
            """
            Same as jump_by, but does not stop playback.
            """
            ...

        def session_automation_record_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "session_automation_record".
            """
            ...

        def session_record_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "session_record".
            """
            ...

        def session_record_status_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "session_record_status".
            """
            ...

        def set_data(self, key: object, value: object) -> None:
            """
            Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.
            """
            ...

        def set_or_delete_cue(self) -> None:
            """
            When a cue is selected, it gets deleted. If no cue is selected, a new cue is created at the current global songtime.
            """
            ...

        def signature_denominator_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "signature_denominator".
            """
            ...

        def signature_numerator_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "signature_numerator".
            """
            ...

        def song_length_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "song_length".
            """
            ...

        def start_playing(self) -> None:
            """
            Start playing from the startmarker
            """
            ...

        def start_time_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "start_time".
            """
            ...

        def stop_all_clips(self, Quantized: bool=True) -> None:
            """
            Stop all playing Clips (if any) but continue playing the Song.
            """
            ...

        def stop_playing(self) -> None:
            """
            Stop playing the Song.
            """
            ...

        def swing_amount_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "swing_amount".
            """
            ...

        def tap_tempo(self) -> None:
            """
            Trigger the tap tempo function.
            """
            ...

        def tempo_follower_enabled_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tempo_follower_enabled".
            """
            ...

        def tempo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tempo".
            """
            ...

        def tracks_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tracks".
            """
            ...

        def trigger_session_record(self, record_length: float=1.7976931348623157e+308) -> None:
            """
            Triggers a new session recording.
            """
            ...

        def tuning_system_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "tuning_system".
            """
            ...

        def undo(self) -> str:
            """
            Undo the last action that was made.
            """
            ...

        def visible_tracks_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "visible_tracks".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a Live document: The Session and Arrangerview.
                """
                ...

            @property
            def _live_ptr(self):
                ...

            @property
            def canonical_parent(self):
                """
                Get the canonical parent of the song view.
                """
                ...

            @property
            def detail_clip(self):
                """
                Get/Set the Clip that is currently visible in Lives Detailview.
                """
                ...

            @property
            def draw_mode(self):
                """
                Get/Set if the Envelope/Note draw mode is enabled.
                """
                ...

            @property
            def follow_song(self):
                """
                Get/Set if the Arrangerview should scroll to show the playmarker.
                """
                ...

            @property
            def highlighted_clip_slot(self):
                """
                Get/Set the clip slot, defined via the selected track and scene in the Session.Will be None for Main- and Sendtracks.
                """
                ...

            @property
            def selected_chain(self):
                """
                Get the highlighted chain if available.
                """
                ...

            @property
            def selected_parameter(self):
                """
                Get the currently selected device parameter.
                """
                ...

            @property
            def selected_scene(self):
                """
                Get/Set the current selected scene in Lives Sessionview.
                """
                ...

            @property
            def selected_track(self):
                """
                Get/Set the current selected Track in Lives Session or Arrangerview.
                """
                ...

            def add_detail_clip_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "detail_clip" has changed.
                """
                ...

            def add_draw_mode_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "draw_mode" has changed.
                """
                ...

            def add_follow_song_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "follow_song" has changed.
                """
                ...

            def add_selected_chain_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_chain" has changed.
                """
                ...

            def add_selected_parameter_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_parameter" has changed.
                """
                ...

            def add_selected_scene_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_scene" has changed.
                """
                ...

            def add_selected_track_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_track" has changed.
                """
                ...

            def detail_clip_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "detail_clip".
                """
                ...

            def draw_mode_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "draw_mode".
                """
                ...

            def follow_song_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "follow_song".
                """
                ...

            def remove_detail_clip_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "detail_clip".
                """
                ...

            def remove_draw_mode_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "draw_mode".
                """
                ...

            def remove_follow_song_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "follow_song".
                """
                ...

            def remove_selected_chain_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_chain".
                """
                ...

            def remove_selected_parameter_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_parameter".
                """
                ...

            def remove_selected_scene_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_scene".
                """
                ...

            def remove_selected_track_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_track".
                """
                ...

            def select_device(self, arg2: Device, ShouldAppointDevice: bool=True) -> None:
                """
                Select the given device.
                """
                ...

            def selected_chain_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_chain".
                """
                ...

            def selected_parameter_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_parameter".
                """
                ...

            def selected_scene_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_scene".
                """
                ...

            def selected_track_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_track".
                """
                ...

    class TimeFormat:
        ms_time: int = 0
        smpte_24: int = 1
        smpte_25: int = 2
        smpte_30: int = 3
        smpte_30_drop: int = 4
        smpte_29: int = 5


class SpectralResonatorDevice(ModuleType):

    class SpectralResonatorDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Spectral Resonator device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def frequency_dial_mode(self) -> int:
            """
            Return the current frequency dial mode index
            """
            ...

        @frequency_dial_mode.setter
        def frequency_dial_mode(self, value) -> None:
            ...

        @property
        def frequency_dial_mode_list(self) -> tuple[str, ...]:
            """
            Return the current frequency dial mode list
            """
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def midi_gate(self) -> int:
            """
            Return the current midi gate index
            """
            ...

        @midi_gate.setter
        def midi_gate(self, value) -> None:
            ...

        @property
        def midi_gate_list(self) -> tuple[str, ...]:
            """
            Return the current midi gate list
            """
            ...

        @property
        def mod_mode(self) -> int:
            """
            Return the current mod mode index
            """
            ...

        @mod_mode.setter
        def mod_mode(self, value) -> None:
            ...

        @property
        def mod_mode_list(self) -> tuple[str, ...]:
            """
            Return the current mod mode list
            """
            ...

        @property
        def mono_poly(self) -> int:
            """
            Return the current mono poly mode index
            """
            ...

        @mono_poly.setter
        def mono_poly(self, value) -> None:
            ...

        @property
        def mono_poly_list(self) -> tuple[str, ...]:
            """
            Return the current mono poly mode list
            """
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def pitch_bend_range(self) -> int:
            """
            Return the current pitch bend range
            """
            ...

        @pitch_bend_range.setter
        def pitch_bend_range(self, value) -> None:
            ...

        @property
        def pitch_mode(self) -> int:
            """
            Return the current pitch mode index
            """
            ...

        @pitch_mode.setter
        def pitch_mode(self, value) -> None:
            ...

        @property
        def pitch_mode_list(self) -> tuple[str, ...]:
            """
            Return the current pitch mode list
            """
            ...

        @property
        def polyphony(self) -> int:
            """
            Return the current polyphony
            """
            ...

        @polyphony.setter
        def polyphony(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        def add_frequency_dial_mode_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "frequency_dial_mode_list" has changed.
            """
            ...

        def add_frequency_dial_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "frequency_dial_mode" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_midi_gate_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_gate_list" has changed.
            """
            ...

        def add_midi_gate_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "midi_gate" has changed.
            """
            ...

        def add_mod_mode_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_mode_list" has changed.
            """
            ...

        def add_mod_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mod_mode" has changed.
            """
            ...

        def add_mono_poly_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mono_poly_list" has changed.
            """
            ...

        def add_mono_poly_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mono_poly" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_bend_range" has changed.
            """
            ...

        def add_pitch_mode_list_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_mode_list" has changed.
            """
            ...

        def add_pitch_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "pitch_mode" has changed.
            """
            ...

        def add_polyphony_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "polyphony" has changed.
            """
            ...

        def frequency_dial_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "frequency_dial_mode".
            """
            ...

        def frequency_dial_mode_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "frequency_dial_mode_list".
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def midi_gate_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_gate".
            """
            ...

        def midi_gate_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "midi_gate_list".
            """
            ...

        def mod_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_mode".
            """
            ...

        def mod_mode_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mod_mode_list".
            """
            ...

        def mono_poly_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mono_poly".
            """
            ...

        def mono_poly_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mono_poly_list".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def pitch_bend_range_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_bend_range".
            """
            ...

        def pitch_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_mode".
            """
            ...

        def pitch_mode_list_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "pitch_mode_list".
            """
            ...

        def polyphony_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "polyphony".
            """
            ...

        def remove_frequency_dial_mode_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "frequency_dial_mode_list".
            """
            ...

        def remove_frequency_dial_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "frequency_dial_mode".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_midi_gate_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_gate_list".
            """
            ...

        def remove_midi_gate_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "midi_gate".
            """
            ...

        def remove_mod_mode_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_mode_list".
            """
            ...

        def remove_mod_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mod_mode".
            """
            ...

        def remove_mono_poly_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mono_poly_list".
            """
            ...

        def remove_mono_poly_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mono_poly".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_pitch_bend_range_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_bend_range".
            """
            ...

        def remove_pitch_mode_list_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_mode_list".
            """
            ...

        def remove_pitch_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "pitch_mode".
            """
            ...

        def remove_polyphony_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "polyphony".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> SpectralResonatorDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...


class TakeLane(ModuleType):

    class TakeLane(object):
        def __init__(self, *a, **k):
            """
            This class represents a take lane in Live.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def arrangement_clips(self) -> tuple:
            """
            Read-only access to the arrangement clips in the take lane.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the take lane.
            """
            ...

        @property
        def name(self) -> str:
            """
            Read/write access to the name of the TakeLane, as visible in the take lane header.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        def add_arrangement_clips_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "arrangement_clips" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def arrangement_clips_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "arrangement_clips".
            """
            ...

        def create_audio_clip(self, arg2: object, arg3: float) -> Clip:
            """
            Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time. Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.
            """
            ...

        def create_midi_clip(self, arg2: float, arg3: float) -> Clip:
            """
            Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def remove_arrangement_clips_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "arrangement_clips".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...


class Track(ModuleType):

    class DeviceContainer(object):
        def __init__(self, *a, **k):
            """
            This class is a common super class of Track and Chain
            """
            ...

        @property
        def _live_ptr(self):
            ...

    class DeviceInsertMode:
        default: int = 0
        selected_left: int = 1
        selected_right: int = 2
        count: int = 3

    class RoutingChannel(object):
        def __init__(self, *a, **k):
            """
            This class represents a routing channel.
            """
            ...

        @property
        def display_name(self) -> str:
            """
            Display name of routing channel.
            """
            ...

        @property
        def layout(self) -> RoutingChannelLayout:
            """
            The routing channel's Layout, e.g., mono or stereo.
            """
            ...

    class RoutingChannelLayout:
        midi: int = 0
        mono: int = 1
        stereo: int = 2

    class RoutingChannelVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning routing channels from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class RoutingType(object):
        def __init__(self, *a, **k):
            """
            This class represents a routing type.
            """
            ...

        @property
        def attached_object(self) -> None:
            """
            Live object associated with the routing type.
            """
            ...

        @property
        def category(self) -> int:
            """
            Category of the routing type.
            """
            ...

        @property
        def display_name(self) -> str:
            """
            Display name of routing type.
            """
            ...

    class RoutingTypeCategory:
        external: int = 0
        rewire: int = 1
        resampling: int = 2
        master: int = 3
        track: int = 4
        parent_group_track: int = 5
        none: int = 6
        invalid: int = 7

    class RoutingTypeVector(object):
        def __init__(self, *a, **k):
            """
            A container for returning routing types from Live.
            """
            ...

        def append(self, arg2: object) -> None:
            ...

        def extend(self, arg2: object) -> None:
            ...

    class Track(object):
        def __init__(self, *a, **k):
            """
            This class represents a track in Live. It can be either an Audio track, a MIDI Track, a Return Track or the Main track. The Main Track and at least one Audio or MIDI track will be always present.Return Tracks are optional.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def arm(self) -> bool:
            """
            Arm the track for recording. Not available for Main- and Send Tracks.
            """
            ...

        @arm.setter
        def arm(self, value) -> None:
            ...

        @property
        def arrangement_clips(self) -> tuple:
            """
            const access to the list of clips in arrangement viewThe list will be empty for the main, send and group tracks.
            """
            ...

        @property
        def available_input_routing_channels(self) -> tuple[RoutingChannel, ...]:
            """
            Return a list of source channels for input routing.
            """
            ...

        @property
        def available_input_routing_types(self) -> tuple[RoutingType, ...]:
            """
            Return a list of source types for input routing.
            """
            ...

        @property
        def available_output_routing_channels(self) -> tuple[RoutingChannel, ...]:
            """
            Return a list of destination channels for output routing.
            """
            ...

        @property
        def available_output_routing_types(self) -> tuple[RoutingType, ...]:
            """
            Return a list of destination types for output routing.
            """
            ...

        @property
        def back_to_arranger(self) -> bool:
            """
            Indicates if it's possible to go back to playing back the clips in the Arranger.Setting a value 0 will go back to the Arranger playback. Setting on grouptracks will go back to the Arranger on all grouped tracks.
            """
            ...

        @back_to_arranger.setter
        def back_to_arranger(self, value) -> None:
            ...

        @property
        def can_be_armed(self) -> bool:
            """
            return True, if this Track has a valid arm property. Not all trackscan be armed (for example return Tracks or the Main Tracks).
            """
            ...

        @property
        def can_be_frozen(self) -> bool:
            """
            return True, if this Track can be frozen.
            """
            ...

        @property
        def can_show_chains(self) -> bool:
            """
            return True, if this Track contains a rack instrument device that is capable of showing its chains in session view.
            """
            ...

        @property
        def canonical_parent(self) -> Song:
            """
            Get the canonical parent of the track.
            """
            ...

        @property
        def clip_slots(self) -> tuple:
            """
            const access to the list of clipslots (see class AClipSlot) for this track.The list will be empty for the main and sendtracks.
            """
            ...

        @property
        def color(self) -> int:
            """
            Get/set access to the color of the Track (RGB).
            """
            ...

        @color.setter
        def color(self, value) -> None:
            ...

        @property
        def color_index(self) -> int:
            """
            Get/Set access to the color index of the track. Can be None for no color.
            """
            ...

        @color_index.setter
        def color_index(self, value) -> None:
            ...

        @property
        def current_input_routing(self) -> str:
            """
            Get/Set the name of the current active input routing.When setting a new routing, the new routing must be one of the available ones.
            """
            ...

        @current_input_routing.setter
        def current_input_routing(self, value) -> None:
            ...

        @property
        def current_input_sub_routing(self) -> str:
            """
            Get/Set the current active input sub routing.When setting a new routing, the new routing must be one of the available ones.
            """
            ...

        @current_input_sub_routing.setter
        def current_input_sub_routing(self, value) -> None:
            ...

        @property
        def current_monitoring_state(self) -> int:
            """
            Get/Set the track's current monitoring state.
            """
            ...

        @current_monitoring_state.setter
        def current_monitoring_state(self, value) -> None:
            ...

        @property
        def current_output_routing(self) -> str:
            """
            Get/Set the current active output routing.When setting a new routing, the new routing must be one of the available ones.
            """
            ...

        @current_output_routing.setter
        def current_output_routing(self, value) -> None:
            ...

        @property
        def current_output_sub_routing(self) -> str:
            """
            Get/Set the current active output sub routing.When setting a new routing, the new routing must be one of the available ones.
            """
            ...

        @current_output_sub_routing.setter
        def current_output_sub_routing(self, value) -> None:
            ...

        @property
        def devices(self) -> tuple:
            """
            Return const access to all available Devices that are present in the TracksDevicechain. This tuple will also include the 'mixer_device' that every Trackalways has.
            """
            ...

        @property
        def fired_slot_index(self) -> int:
            """
            const access to the index of the fired (and thus blinking) clipslot in this track.This index is -1 if no slot is fired and -2 if the track's stop button has been fired.
            """
            ...

        @property
        def fold_state(self) -> bool:
            """
            Get/Set whether the track is folded or not. Only available if is_foldable is True.
            """
            ...

        @fold_state.setter
        def fold_state(self, value) -> None:
            ...

        @property
        def group_track(self) -> Track:
            """
            return the group track if is_grouped.
            """
            ...

        @property
        def has_audio_input(self) -> bool:
            """
            return True, if this Track can be feed with an Audio signal. This istrue for all Audio Tracks.
            """
            ...

        @property
        def has_audio_output(self) -> bool:
            """
            return True, if this Track sends out an Audio signal. This istrue for all Audio Tracks, and MIDI tracks with an Instrument.
            """
            ...

        @property
        def has_midi_input(self) -> bool:
            """
            return True, if this Track can be feed with an Audio signal. This istrue for all MIDI Tracks.
            """
            ...

        @property
        def has_midi_output(self) -> bool:
            """
            return True, if this Track sends out MIDI events. This istrue for all MIDI Tracks with no Instruments.
            """
            ...

        @property
        def implicit_arm(self) -> bool:
            """
            Arm the track for recording. When The track is implicitly armed, it showsin a weaker color in the live GUI and is not saved in the set.
            """
            ...

        @implicit_arm.setter
        def implicit_arm(self, value) -> None:
            ...

        @property
        def input_meter_left(self) -> float:
            """
            Momentary value of left input channel meter, 0.0 to 1.0. For Audio Tracks only.
            """
            ...

        @property
        def input_meter_level(self) -> float:
            """
            Return the MIDI or Audio meter value of the Tracks input, depending on thetype of the Track input. Meter values (MIDI or Audio) are always scaledfrom 0.0 to 1.0.
            """
            ...

        @property
        def input_meter_right(self) -> float:
            """
            Momentary value of right input channel meter, 0.0 to 1.0. For Audio Tracks only.
            """
            ...

        @property
        def input_routing_channel(self) -> RoutingChannel:
            """
            Get and set the current source channel for input routing.Raises ValueError if the type isn't one of the current values inavailable_input_routing_channels.
            """
            ...

        @input_routing_channel.setter
        def input_routing_channel(self, value) -> None:
            ...

        @property
        def input_routing_type(self) -> RoutingType:
            """
            Get and set the current source type for input routing.Raises ValueError if the type isn't one of the current values inavailable_input_routing_types.
            """
            ...

        @input_routing_type.setter
        def input_routing_type(self, value) -> None:
            ...

        @property
        def input_routings(self) -> tuple[str, ...]:
            """
            Const access to the list of available input routings.
            """
            ...

        @property
        def input_sub_routings(self) -> tuple[str, ...]:
            """
            Return a list of all available input sub routings.
            """
            ...

        @property
        def is_foldable(self) -> bool:
            """
            return True if the track can be (un)folded to hide/reveal contained tracks.
            """
            ...

        @property
        def is_frozen(self) -> bool:
            """
            return True if this Track is currently frozen. No changes should be applied to the track's devices or clips while it is frozen.
            """
            ...

        @property
        def is_grouped(self) -> bool:
            """
            return True if this Track is current part of a group track.
            """
            ...

        @property
        def is_part_of_selection(self) -> bool:
            """
            return False if the track is not selected.
            """
            ...

        @property
        def is_showing_chains(self) -> bool:
            """
            Get/Set whether a track with a rack device is showing its chains in session view.
            """
            ...

        @is_showing_chains.setter
        def is_showing_chains(self, value) -> None:
            ...

        @property
        def is_visible(self) -> bool:
            """
            return False if the track is hidden within a folded group track.
            """
            ...

        @property
        def mixer_device(self) -> MixerDevice:
            """
            Return access to the special Device that every Track has: This Device containsthe Volume, Pan, Sendamounts, and Crossfade assignment parameters.
            """
            ...

        @property
        def mute(self) -> bool:
            """
            Mute/unmute the track.
            """
            ...

        @mute.setter
        def mute(self, value) -> None:
            ...

        @property
        def muted_via_solo(self) -> bool:
            """
            Returns true if the track is muted because another track is soloed.
            """
            ...

        @property
        def name(self) -> str:
            """
            Read/write access to the name of the Track, as visible in the track header.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def output_meter_left(self) -> float:
            """
            Momentary value of left output channel meter, 0.0 to 1.0.For tracks with audio output only.
            """
            ...

        @property
        def output_meter_level(self) -> float:
            """
            Return the MIDI or Audio meter value of the Track output (behind themixer_device), depending on the type of the Track input, this can be a MIDIor Audio meter. Meter values (MIDI or Audio) are always scaled from 0.0 to 1.0.
            """
            ...

        @property
        def output_meter_right(self) -> float:
            """
            Momentary value of right output channel meter, 0.0 to 1.0.For tracks with audio output only.
            """
            ...

        @property
        def output_routing_channel(self) -> RoutingChannel:
            """
            Get and set the current destination channel for output routing.Raises ValueError if the channel isn't one of the current values inavailable_output_routing_channels.
            """
            ...

        @output_routing_channel.setter
        def output_routing_channel(self, value) -> None:
            ...

        @property
        def output_routing_type(self) -> RoutingType:
            """
            Get and set the current destination type for output routing.Raises ValueError if the type isn't one of the current values inavailable_output_routing_types.
            """
            ...

        @output_routing_type.setter
        def output_routing_type(self, value) -> None:
            ...

        @property
        def output_routings(self) -> tuple[str, ...]:
            """
            Const access to the list of all available output routings.
            """
            ...

        @property
        def output_sub_routings(self) -> tuple[str, ...]:
            """
            Return a list of all available output sub routings.
            """
            ...

        @property
        def performance_impact(self) -> float:
            """
            Reports the performance impact of this track.
            """
            ...

        @property
        def playing_slot_index(self) -> int:
            """
            const access to the index of the currently playing clip in the track.Will be -1 when no clip is playing.
            """
            ...

        @property
        def solo(self) -> bool:
            """
            Get/Set the solo status of the track. Note that this will not disable thesolo state of any other track. If you want exclusive solo, you have to disable the solo state of the other Tracks manually.
            """
            ...

        @solo.setter
        def solo(self, value) -> None:
            ...

        @property
        def take_lanes(self) -> tuple:
            """
            returns the take lanes.
            """
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a Track.
            """
            ...

        def add_arm_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "arm" has changed.
            """
            ...

        def add_arrangement_clips_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "arrangement_clips" has changed.
            """
            ...

        def add_available_input_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_input_routing_channels" has changed.
            """
            ...

        def add_available_input_routing_types_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_input_routing_types" has changed.
            """
            ...

        def add_available_output_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_output_routing_channels" has changed.
            """
            ...

        def add_available_output_routing_types_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "available_output_routing_types" has changed.
            """
            ...

        def add_back_to_arranger_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "back_to_arranger" has changed.
            """
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

        def add_current_input_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_input_routing" has changed.
            """
            ...

        def add_current_input_sub_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_input_sub_routing" has changed.
            """
            ...

        def add_current_monitoring_state_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_monitoring_state" has changed.
            """
            ...

        def add_current_output_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_output_routing" has changed.
            """
            ...

        def add_current_output_sub_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "current_output_sub_routing" has changed.
            """
            ...

        def add_data_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "data" has changed.
            """
            ...

        def add_devices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "devices" has changed.
            """
            ...

        def add_fired_slot_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "fired_slot_index" has changed.
            """
            ...

        def add_has_audio_input_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_audio_input" has changed.
            """
            ...

        def add_has_audio_output_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_audio_output" has changed.
            """
            ...

        def add_has_midi_input_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_midi_input" has changed.
            """
            ...

        def add_has_midi_output_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "has_midi_output" has changed.
            """
            ...

        def add_implicit_arm_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "implicit_arm" has changed.
            """
            ...

        def add_input_meter_left_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_meter_left" has changed.
            """
            ...

        def add_input_meter_level_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_meter_level" has changed.
            """
            ...

        def add_input_meter_right_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_meter_right" has changed.
            """
            ...

        def add_input_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routing_channel" has changed.
            """
            ...

        def add_input_routing_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routing_type" has changed.
            """
            ...

        def add_input_routings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_routings" has changed.
            """
            ...

        def add_input_sub_routings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "input_sub_routings" has changed.
            """
            ...

        def add_is_frozen_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_frozen" has changed.
            """
            ...

        def add_is_showing_chains_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_showing_chains" has changed.
            """
            ...

        def add_mute_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mute" has changed.
            """
            ...

        def add_muted_via_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "muted_via_solo" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_output_meter_left_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_meter_left" has changed.
            """
            ...

        def add_output_meter_level_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_meter_level" has changed.
            """
            ...

        def add_output_meter_right_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_meter_right" has changed.
            """
            ...

        def add_output_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_routing_channel" has changed.
            """
            ...

        def add_output_routing_type_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_routing_type" has changed.
            """
            ...

        def add_output_routings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_routings" has changed.
            """
            ...

        def add_output_sub_routings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "output_sub_routings" has changed.
            """
            ...

        def add_performance_impact_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "performance_impact" has changed.
            """
            ...

        def add_playing_slot_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "playing_slot_index" has changed.
            """
            ...

        def add_solo_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "solo" has changed.
            """
            ...

        def add_take_lanes_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "take_lanes" has changed.
            """
            ...

        def arm_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "arm".
            """
            ...

        def arrangement_clips_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "arrangement_clips".
            """
            ...

        def available_input_routing_channels_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_input_routing_channels".
            """
            ...

        def available_input_routing_types_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_input_routing_types".
            """
            ...

        def available_output_routing_channels_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_output_routing_channels".
            """
            ...

        def available_output_routing_types_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "available_output_routing_types".
            """
            ...

        def back_to_arranger_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "back_to_arranger".
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

        def create_audio_clip(self, arg2: object, arg3: float) -> Clip:
            """
            Creates an audio clip referencing the file at the given path and inserts it into the arrangement at the specified time. Throws an error when called on a non-audio or a frozen track, when the specified time is outside the [0., 1576800.] range, when the track is currently being recorded into, or when the path doesn't point to a valid audio file.
            """
            ...

        def create_midi_clip(self, arg2: float, arg3: float) -> Clip:
            """
            Creates an empty MIDI clip and inserts it into the arrangement at the specified time. Throws an error when called on a non-MIDI track or a frozen track, when the specified time is outside the [0., 1576800.] range, or when the track is currently being recorded into.
            """
            ...

        def create_take_lane(self) -> LomObject:
            """
            Create a new TakeLane for this track.
            """
            ...

        def current_input_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_input_routing".
            """
            ...

        def current_input_sub_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_input_sub_routing".
            """
            ...

        def current_monitoring_state_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_monitoring_state".
            """
            ...

        def current_output_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_output_routing".
            """
            ...

        def current_output_sub_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "current_output_sub_routing".
            """
            ...

        def data_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "data".
            """
            ...

        def delete_clip(self, arg2: Clip) -> None:
            """
            Delete the given clip. Raises a runtime error when the clip belongs to another track.
            """
            ...

        def delete_device(self, arg2: int) -> None:
            """
            Delete a device identified by the index in the 'devices' list.
            """
            ...

        def devices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "devices".
            """
            ...

        def duplicate_clip_slot(self, arg2: int) -> int:
            """
            Duplicate a clip and put it into the next free slot and return the index of the destination slot. A new scene is created if no free slot is available. If creating the new scene would exceed the limitations, a runtime error is raised.
            """
            ...

        def duplicate_clip_to_arrangement(self, clip: Clip, destination_time: float) -> Clip:
            """
            Duplicate the given clip into the arrangement of this track at the provided destination time and return it. When the type of the clip and the type of the track are incompatible, a runtime error is raised.
            """
            ...

        def duplicate_device(self, arg2: int) -> None:
            """
            Duplicate a device at a given index in the 'devices' list.
            """
            ...

        def fired_slot_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "fired_slot_index".
            """
            ...

        def get_data(self, key: object, default_value: object) -> object:
            """
            Get data for the given key, that was previously stored using set_data.
            """
            ...

        def has_audio_input_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_audio_input".
            """
            ...

        def has_audio_output_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_audio_output".
            """
            ...

        def has_midi_input_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_midi_input".
            """
            ...

        def has_midi_output_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "has_midi_output".
            """
            ...

        def implicit_arm_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "implicit_arm".
            """
            ...

        def input_meter_left_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_meter_left".
            """
            ...

        def input_meter_level_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_meter_level".
            """
            ...

        def input_meter_right_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_meter_right".
            """
            ...

        def input_routing_channel_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routing_channel".
            """
            ...

        def input_routing_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routing_type".
            """
            ...

        def input_routings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_routings".
            """
            ...

        def input_sub_routings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "input_sub_routings".
            """
            ...

        def insert_device(self, DeviceName: str, DeviceIndex: int=-1) -> LomObject:
            """
            Add a device at a given index in the 'devices' list. At end if -1.
            """
            ...

        def is_frozen_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_frozen".
            """
            ...

        def is_showing_chains_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_showing_chains".
            """
            ...

        def jump_in_running_session_clip(self, arg2: float) -> None:
            """
            Jump forward or backward in the currently running Sessionclip (if any) by the specified relative amount in beats. Does nothing if no Session Clip is currently running.
            """
            ...

        def mute_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mute".
            """
            ...

        def muted_via_solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "muted_via_solo".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def output_meter_left_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_meter_left".
            """
            ...

        def output_meter_level_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_meter_level".
            """
            ...

        def output_meter_right_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_meter_right".
            """
            ...

        def output_routing_channel_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_routing_channel".
            """
            ...

        def output_routing_type_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_routing_type".
            """
            ...

        def output_routings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_routings".
            """
            ...

        def output_sub_routings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "output_sub_routings".
            """
            ...

        def performance_impact_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "performance_impact".
            """
            ...

        def playing_slot_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "playing_slot_index".
            """
            ...

        def remove_arm_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "arm".
            """
            ...

        def remove_arrangement_clips_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "arrangement_clips".
            """
            ...

        def remove_available_input_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_input_routing_channels".
            """
            ...

        def remove_available_input_routing_types_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_input_routing_types".
            """
            ...

        def remove_available_output_routing_channels_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_output_routing_channels".
            """
            ...

        def remove_available_output_routing_types_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "available_output_routing_types".
            """
            ...

        def remove_back_to_arranger_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "back_to_arranger".
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

        def remove_current_input_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_input_routing".
            """
            ...

        def remove_current_input_sub_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_input_sub_routing".
            """
            ...

        def remove_current_monitoring_state_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_monitoring_state".
            """
            ...

        def remove_current_output_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_output_routing".
            """
            ...

        def remove_current_output_sub_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "current_output_sub_routing".
            """
            ...

        def remove_data_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "data".
            """
            ...

        def remove_devices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "devices".
            """
            ...

        def remove_fired_slot_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "fired_slot_index".
            """
            ...

        def remove_has_audio_input_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_audio_input".
            """
            ...

        def remove_has_audio_output_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_audio_output".
            """
            ...

        def remove_has_midi_input_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_midi_input".
            """
            ...

        def remove_has_midi_output_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "has_midi_output".
            """
            ...

        def remove_implicit_arm_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "implicit_arm".
            """
            ...

        def remove_input_meter_left_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_meter_left".
            """
            ...

        def remove_input_meter_level_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_meter_level".
            """
            ...

        def remove_input_meter_right_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_meter_right".
            """
            ...

        def remove_input_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routing_channel".
            """
            ...

        def remove_input_routing_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routing_type".
            """
            ...

        def remove_input_routings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_routings".
            """
            ...

        def remove_input_sub_routings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "input_sub_routings".
            """
            ...

        def remove_is_frozen_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_frozen".
            """
            ...

        def remove_is_showing_chains_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_showing_chains".
            """
            ...

        def remove_mute_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mute".
            """
            ...

        def remove_muted_via_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "muted_via_solo".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_output_meter_left_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_meter_left".
            """
            ...

        def remove_output_meter_level_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_meter_level".
            """
            ...

        def remove_output_meter_right_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_meter_right".
            """
            ...

        def remove_output_routing_channel_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_routing_channel".
            """
            ...

        def remove_output_routing_type_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_routing_type".
            """
            ...

        def remove_output_routings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_routings".
            """
            ...

        def remove_output_sub_routings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "output_sub_routings".
            """
            ...

        def remove_performance_impact_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "performance_impact".
            """
            ...

        def remove_playing_slot_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "playing_slot_index".
            """
            ...

        def remove_solo_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "solo".
            """
            ...

        def remove_take_lanes_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "take_lanes".
            """
            ...

        def set_data(self, key: object, value: object) -> None:
            """
            Store data for the given key in this object. The data is persistent and will be restored when loading the Live Set.
            """
            ...

        def solo_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "solo".
            """
            ...

        def stop_all_clips(self, Quantized: bool=True) -> None:
            """
            Stop running and triggered clip and slots on this track.
            """
            ...

        def take_lanes_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "take_lanes".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a Track.
                """
                ...

            @property
            def _live_ptr(self):
                ...

            @property
            def canonical_parent(self):
                """
                Get the canonical parent of the track view.
                """
                ...

            @property
            def device_insert_mode(self):
                """
                Get/Listen the device insertion mode of the track.  By default, it will insert devices at the end, but it can be changed to make it relative to current selection.
                """
                ...

            @property
            def is_collapsed(self):
                """
                Get/Set/Listen if the track is shown collapsed in the arranger view.
                """
                ...

            @property
            def selected_device(self):
                """
                Get/Set/Listen the insertion mode of the device.  While in insertion mode, loading new devices from the browser will place devices at the selected position.
                """
                ...

            def add_device_insert_mode_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "device_insert_mode" has changed.
                """
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def add_selected_device_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "selected_device" has changed.
                """
                ...

            def device_insert_mode_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "device_insert_mode".
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_device_insert_mode_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "device_insert_mode".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...

            def remove_selected_device_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "selected_device".
                """
                ...

            def select_instrument(self) -> bool:
                """
                Selects the track's instrument if it has one.
                """
                ...

            def selected_device_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "selected_device".
                """
                ...

        class monitoring_states:
            IN: int = 0
            AUTO: int = 1
            OFF: int = 2


class TuningSystem(ModuleType):

    class PitchClassAndOctave(object):
        def __init__(self, *a, **k):
            """
            This class represents a PitchClassAndOctave type.
            """
            ...

        @property
        def index_in_octave(self) -> int:
            """
            A PitchClassAndOctave's index within the pseudo octave.
            """
            ...

        @property
        def octave(self) -> int:
            """
            A PitchClassAndOctave's octave.
            """
            ...

    class ReferencePitch(object):
        def __init__(self, *a, **k):
            """
            This class represents a ReferencePitch type.
            """
            ...

        @property
        def frequency(self) -> float:
            """
            A ReferencePitch's frequency in Hz.
            """
            ...

        @property
        def index_in_octave(self) -> int:
            """
            A ReferencePitch's index within the pseudo octave.
            """
            ...

        @property
        def octave(self) -> int:
            """
            A ReferencePitch's octave.
            """
            ...

    class TuningSystem(object):
        def __init__(self, *a, **k):
            """
            Represents a Tuning System and its properties.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def canonical_parent(self) -> Song:
            """
            Get the canonical parent of the TuningSystem.
            """
            ...

        @property
        def highest_note(self) -> PitchClassAndOctave:
            """
            Get/Set the highest note of the current tuning system, where the first entry isthe index within the pseudo octave and the second entry is the octave.
            """
            ...

        @highest_note.setter
        def highest_note(self, value) -> None:
            ...

        @property
        def lowest_note(self) -> PitchClassAndOctave:
            """
            Get/Set the lowest note of the current tuning system, where the first entry isthe index within the pseudo octave and the second entry is the octave.
            """
            ...

        @lowest_note.setter
        def lowest_note(self, value) -> None:
            ...

        @property
        def name(self) -> str:
            """
            Get/Set the name of the currently active tuning system.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def note_tunings(self) -> list:
            """
            Get/Set the currently active tuning system's note tunings, specified in Cents, where 100 Cents is one semi-tone in equal temperament.
            """
            ...

        @note_tunings.setter
        def note_tunings(self, value) -> None:
            ...

        @property
        def number_of_notes_in_pseudo_octave(self) -> int:
            """
            Get the number of notes in the pseudo octave.
            """
            ...

        @property
        def pseudo_octave_in_cents(self) -> float:
            """
            Get the pseudo octave in cents for the currently active tuning system.
            """
            ...

        @property
        def reference_pitch(self) -> ReferencePitch:
            """
            Get/Set the reference pitch the currently active tuning system.
            """
            ...

        @reference_pitch.setter
        def reference_pitch(self, value) -> None:
            ...

        def add_highest_note_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "highest_note" has changed.
            """
            ...

        def add_lowest_note_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "lowest_note" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_note_tunings_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "note_tunings" has changed.
            """
            ...

        def add_reference_pitch_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "reference_pitch" has changed.
            """
            ...

        def highest_note_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "highest_note".
            """
            ...

        def lowest_note_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "lowest_note".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def note_tunings_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "note_tunings".
            """
            ...

        def reference_pitch_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "reference_pitch".
            """
            ...

        def remove_highest_note_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "highest_note".
            """
            ...

        def remove_lowest_note_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "lowest_note".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_note_tunings_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "note_tunings".
            """
            ...

        def remove_reference_pitch_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "reference_pitch".
            """
            ...


class WavetableDevice(ModuleType):

    class EffectMode:
        none: int = 0
        frequency_modulation: int = 1
        sync_and_pulse_width: int = 2
        warp_and_fold: int = 3

    class FilterRouting:
        serial: int = 0
        parallel: int = 1
        split: int = 2

    class ModulationSource:
        amp_envelope: int = 0
        envelope_2: int = 1
        envelope_3: int = 2
        lfo_1: int = 3
        lfo_2: int = 4
        midi_velocity: int = 5
        midi_note: int = 6
        midi_pitch_bend: int = 7
        midi_channel_pressure: int = 8
        midi_mod_wheel: int = 9
        midi_random: int = 10

    class UnisonMode:
        none: int = 0
        classic: int = 1
        slow_shimmer: int = 2
        fast_shimmer: int = 3
        phase_sync: int = 4
        position_spread: int = 5
        random_note: int = 6

    class VoiceCount:
        two: int = 0
        three: int = 1
        four: int = 2
        five: int = 3
        six: int = 4
        seven: int = 5
        eight: int = 6

    class Voicing:
        mono: int = 0
        poly: int = 1

    class WavetableDevice(object):
        def __init__(self, *a, **k):
            """
            This class represents a Wavetable device.
            """
            ...

        @property
        def _live_ptr(self) -> int:
            ...

        @property
        def can_compare_ab(self) -> bool:
            """
            Returns true if the Device has the capability to AB compare.
            """
            ...

        @property
        def can_have_chains(self) -> bool:
            """
            Returns true if the device is a rack.
            """
            ...

        @property
        def can_have_drum_pads(self) -> bool:
            """
            Returns true if the device is a drum rack.
            """
            ...

        @property
        def canonical_parent(self) -> Track:
            """
            Get the canonical parent of the Device.
            """
            ...

        @property
        def class_display_name(self) -> str:
            """
            Return const access to the name of the device's class name as displayed in Live's browser and device chain
            """
            ...

        @property
        def class_name(self) -> str:
            """
            Return const access to the name of the device's class.
            """
            ...

        @property
        def filter_routing(self) -> int:
            """
            Return the current filter routing.
            """
            ...

        @filter_routing.setter
        def filter_routing(self, value) -> None:
            ...

        @property
        def is_active(self) -> bool:
            """
            Return const access to whether this device is active. This will be false bothwhen the device is off and when it's inside a rack device which is off.
            """
            ...

        @property
        def is_using_compare_preset_b(self) -> bool:
            """
            Returns whether the Device has loaded the preset in compare slot B. Only relevant if can_compare_ab, otherwise errors.
            """
            ...

        @is_using_compare_preset_b.setter
        def is_using_compare_preset_b(self, value) -> None:
            ...

        @property
        def latency_in_ms(self) -> float:
            """
            Returns the latency of the device in ms.
            """
            ...

        @property
        def latency_in_samples(self) -> int:
            """
            Returns the latency of the device in samples.
            """
            ...

        @property
        def mono_poly(self) -> int:
            """
            Return the current voicing mode.
            """
            ...

        @mono_poly.setter
        def mono_poly(self, value) -> None:
            ...

        @property
        def name(self) -> str:
            """
            Return access to the name of the device.
            """
            ...

        @name.setter
        def name(self, value) -> None:
            ...

        @property
        def oscillator_1_effect_mode(self) -> int:
            """
            Return the current effect mode of the oscillator 1.
            """
            ...

        @oscillator_1_effect_mode.setter
        def oscillator_1_effect_mode(self, value) -> None:
            ...

        @property
        def oscillator_1_wavetable_category(self) -> int:
            """
            Return the current wavetable category of the oscillator 1.
            """
            ...

        @oscillator_1_wavetable_category.setter
        def oscillator_1_wavetable_category(self, value) -> None:
            ...

        @property
        def oscillator_1_wavetable_index(self) -> int:
            """
            Return the current wavetable index of the oscillator 1.
            """
            ...

        @oscillator_1_wavetable_index.setter
        def oscillator_1_wavetable_index(self, value) -> None:
            ...

        @property
        def oscillator_1_wavetables(self) -> tuple[str, ...]:
            """
            Get a vector of oscillator 1's wavetable names.
            """
            ...

        @property
        def oscillator_2_effect_mode(self) -> int:
            """
            Return the current effect mode of the oscillator 2.
            """
            ...

        @oscillator_2_effect_mode.setter
        def oscillator_2_effect_mode(self, value) -> None:
            ...

        @property
        def oscillator_2_wavetable_category(self) -> int:
            """
            Return the current wavetable category of the oscillator 2.
            """
            ...

        @oscillator_2_wavetable_category.setter
        def oscillator_2_wavetable_category(self, value) -> None:
            ...

        @property
        def oscillator_2_wavetable_index(self) -> int:
            """
            Return the current wavetable index of the oscillator 2.
            """
            ...

        @oscillator_2_wavetable_index.setter
        def oscillator_2_wavetable_index(self, value) -> None:
            ...

        @property
        def oscillator_2_wavetables(self) -> tuple[str, ...]:
            """
            Get a vector of oscillator 2's wavetable names.
            """
            ...

        @property
        def oscillator_wavetable_categories(self) -> tuple[str, ...]:
            """
            Get a vector of the available wavetable categories.
            """
            ...

        @property
        def parameters(self) -> tuple[ATimeableValue, ...]:
            """
            Const access to the list of available automatable parameters for this device.
            """
            ...

        @property
        def poly_voices(self) -> int:
            """
            Return the current number of polyphonic voices. Uses the VoiceCount enumeration.
            """
            ...

        @poly_voices.setter
        def poly_voices(self, value) -> None:
            ...

        @property
        def type(self) -> DeviceType:
            """
            Return the type of the device.
            """
            ...

        @property
        def unison_mode(self) -> int:
            """
            Return the current unison mode.
            """
            ...

        @unison_mode.setter
        def unison_mode(self, value) -> None:
            ...

        @property
        def unison_voice_count(self) -> int:
            """
            Return the current number of unison voices.
            """
            ...

        @unison_voice_count.setter
        def unison_voice_count(self, value) -> None:
            ...

        @property
        def view(self) -> View:
            """
            Representing the view aspects of a device.
            """
            ...

        @property
        def visible_modulation_target_names(self) -> tuple[str, ...]:
            """
            Get the names of all the visible modulation targets.
            """
            ...

        def add_filter_routing_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "filter_routing" has changed.
            """
            ...

        def add_is_active_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_active" has changed.
            """
            ...

        def add_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "is_using_compare_preset_b" has changed.
            """
            ...

        def add_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_ms" has changed.
            """
            ...

        def add_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "latency_in_samples" has changed.
            """
            ...

        def add_modulation_matrix_changed_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "modulation_matrix_changed" has changed.
            """
            ...

        def add_mono_poly_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "mono_poly" has changed.
            """
            ...

        def add_name_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "name" has changed.
            """
            ...

        def add_oscillator_1_effect_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_1_effect_mode" has changed.
            """
            ...

        def add_oscillator_1_wavetable_category_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetable_category" has changed.
            """
            ...

        def add_oscillator_1_wavetable_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetable_index" has changed.
            """
            ...

        def add_oscillator_1_wavetables_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_1_wavetables" has changed.
            """
            ...

        def add_oscillator_2_effect_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_2_effect_mode" has changed.
            """
            ...

        def add_oscillator_2_wavetable_category_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetable_category" has changed.
            """
            ...

        def add_oscillator_2_wavetable_index_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetable_index" has changed.
            """
            ...

        def add_oscillator_2_wavetables_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "oscillator_2_wavetables" has changed.
            """
            ...

        def add_parameter_to_modulation_matrix(self, parameter: DeviceParameter) -> int:
            """
            Add a non-pitch parameter to the modulation matrix.
            """
            ...

        def add_parameters_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "parameters" has changed.
            """
            ...

        def add_poly_voices_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "poly_voices" has changed.
            """
            ...

        def add_unison_mode_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "unison_mode" has changed.
            """
            ...

        def add_unison_voice_count_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "unison_voice_count" has changed.
            """
            ...

        def add_visible_modulation_target_names_listener(self, arg2: Callable) -> None:
            """
            Add a listener function or method, which will be called as soon as the property "visible_modulation_target_names" has changed.
            """
            ...

        def filter_routing_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "filter_routing".
            """
            ...

        def get_modulation_target_parameter_name(self, target_index: int) -> str:
            """
            Get the parameter name of the modulation target at the given index.
            """
            ...

        def get_modulation_value(self, target_index: int, source: int) -> float:
            """
            Get the value of a modulation amount for the given target-source connection.
            """
            ...

        def is_active_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_active".
            """
            ...

        def is_parameter_modulatable(self, parameter: DeviceParameter) -> bool:
            """
            Indicate whether the parameter is modulatable. Note that pitch parameters only exist in python and must be handled there.
            """
            ...

        def is_using_compare_preset_b_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "is_using_compare_preset_b".
            """
            ...

        def latency_in_ms_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_ms".
            """
            ...

        def latency_in_samples_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "latency_in_samples".
            """
            ...

        def modulation_matrix_changed_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "modulation_matrix_changed".
            """
            ...

        def mono_poly_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "mono_poly".
            """
            ...

        def name_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "name".
            """
            ...

        def oscillator_1_effect_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_1_effect_mode".
            """
            ...

        def oscillator_1_wavetable_category_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetable_category".
            """
            ...

        def oscillator_1_wavetable_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetable_index".
            """
            ...

        def oscillator_1_wavetables_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_1_wavetables".
            """
            ...

        def oscillator_2_effect_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_2_effect_mode".
            """
            ...

        def oscillator_2_wavetable_category_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetable_category".
            """
            ...

        def oscillator_2_wavetable_index_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetable_index".
            """
            ...

        def oscillator_2_wavetables_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "oscillator_2_wavetables".
            """
            ...

        def parameters_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "parameters".
            """
            ...

        def poly_voices_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "poly_voices".
            """
            ...

        def remove_filter_routing_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "filter_routing".
            """
            ...

        def remove_is_active_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_active".
            """
            ...

        def remove_is_using_compare_preset_b_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "is_using_compare_preset_b".
            """
            ...

        def remove_latency_in_ms_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_ms".
            """
            ...

        def remove_latency_in_samples_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "latency_in_samples".
            """
            ...

        def remove_modulation_matrix_changed_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "modulation_matrix_changed".
            """
            ...

        def remove_mono_poly_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "mono_poly".
            """
            ...

        def remove_name_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "name".
            """
            ...

        def remove_oscillator_1_effect_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_1_effect_mode".
            """
            ...

        def remove_oscillator_1_wavetable_category_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_1_wavetable_category".
            """
            ...

        def remove_oscillator_1_wavetable_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_1_wavetable_index".
            """
            ...

        def remove_oscillator_1_wavetables_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_1_wavetables".
            """
            ...

        def remove_oscillator_2_effect_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_2_effect_mode".
            """
            ...

        def remove_oscillator_2_wavetable_category_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_2_wavetable_category".
            """
            ...

        def remove_oscillator_2_wavetable_index_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_2_wavetable_index".
            """
            ...

        def remove_oscillator_2_wavetables_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "oscillator_2_wavetables".
            """
            ...

        def remove_parameters_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "parameters".
            """
            ...

        def remove_poly_voices_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "poly_voices".
            """
            ...

        def remove_unison_mode_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "unison_mode".
            """
            ...

        def remove_unison_voice_count_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "unison_voice_count".
            """
            ...

        def remove_visible_modulation_target_names_listener(self, arg2: Callable) -> None:
            """
            Remove a previously set listener function or method from property "visible_modulation_target_names".
            """
            ...

        def save_preset_to_compare_ab_slot(self) -> None:
            """
            Saves the current state of the device to the compare AB slot. Only relevant if can_compare_ab, otherwise throws.
            """
            ...

        def set_modulation_value(self, target_index: int, source: int, value: float) -> None:
            """
            Set the value of a modulation amount for the given target-source connection.
            """
            ...

        def store_chosen_bank(self, arg2: int, arg3: int) -> None:
            """
            Set the selected bank in the device for persistency.
            """
            ...

        def unison_mode_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "unison_mode".
            """
            ...

        def unison_voice_count_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "unison_voice_count".
            """
            ...

        def visible_modulation_target_names_has_listener(self, arg2: Callable) -> bool:
            """
            Returns true, if the given listener function or method is connected to the property "visible_modulation_target_names".
            """
            ...

        class View(object):
            def __init__(self, *a, **k):
                """
                Representing the view aspects of a device.
                """
                ...

            @property
            def _live_ptr(self) -> int:
                ...

            @property
            def canonical_parent(self) -> WavetableDevice:
                """
                Get the canonical parent of the View.
                """
                ...

            @property
            def is_collapsed(self) -> bool:
                """
                Get/Set/Listen if the device is shown collapsed in the device chain.
                """
                ...

            @is_collapsed.setter
            def is_collapsed(self, value) -> None:
                ...

            def add_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Add a listener function or method, which will be called as soon as the property "is_collapsed" has changed.
                """
                ...

            def is_collapsed_has_listener(self, arg2: Callable) -> bool:
                """
                Returns true, if the given listener function or method is connected to the property "is_collapsed".
                """
                ...

            def remove_is_collapsed_listener(self, arg2: Callable) -> None:
                """
                Remove a previously set listener function or method from property "is_collapsed".
                """
                ...
