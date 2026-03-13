from __future__ import annotations
from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from . import BrowserItem, Relation



class Browser:
    """
    This class represents the live browser data base.
    """

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

    def add_filter_type_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "filter_type" has changed.
        """
        ...

    def add_full_refresh_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "full_refresh" has changed.
        """
        ...

    def add_hotswap_target_listener(self, listener: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the property "hotswap_target" has changed.
        """
        ...

    def filter_type_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "filter_type".
        """
        ...

    def full_refresh_has_listener(self, listener: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected to the property "full_refresh".
        """
        ...

    def hotswap_target_has_listener(self, listener: Callable) -> bool:
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

    def remove_filter_type_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "filter_type".
        """
        ...

    def remove_full_refresh_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "full_refresh".
        """
        ...

    def remove_hotswap_target_listener(self, listener: Callable) -> None:
        """
        Remove a previously set listener function or method from property "hotswap_target".
        """
        ...

    def stop_preview(self) -> None:
        """
        Stop the current preview.
        """
        ...


__all__ = ['Browser']
