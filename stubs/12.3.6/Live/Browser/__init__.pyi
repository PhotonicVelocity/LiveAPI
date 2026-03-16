from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')
from .Browser import Browser

if TYPE_CHECKING:
    from Live.Base import Vector



class BrowserItem:
    """This class represents an item of the browser hierarchy."""

    @property
    def children(self) -> BrowserItemVector:
        """Const access to the descendants of this browser item."""
        ...

    @property
    def is_device(self) -> bool:
        """Indicates if the browser item represents a device."""
        ...

    @property
    def is_folder(self) -> bool:
        """Indicates if the browser item represents folder."""
        ...

    @property
    def is_loadable(self) -> bool:
        """True if item can be loaded via the Browser's 'load_item' method."""
        ...

    @property
    def is_selected(self) -> bool:
        """True if the item is ancestor of or the actual selection."""
        ...

    @property
    def iter_children(self) -> BrowserItemIterator:
        """Const iterable access to the descendants of this browser item."""
        ...

    @property
    def name(self) -> str:
        """Const access to the canonical display name of this browser item."""
        ...

    @property
    def source(self) -> str:
        """Specifies where does item come from -- i.e. Live pack, user library..."""
        ...

    @property
    def uri(self) -> str:
        """The uri describes a unique identifier for a browser item."""
        ...

class BrowserItemIterator(Vector[BrowserItem]):
    """This class iterates over children of another BrowserItem."""

class BrowserItemVector(Vector[BrowserItem]):
    """A container for returning browser items from Live."""

    def append(self, value: BrowserItem | None) -> None:
        ...

    def extend(self, values: Iterable[BrowserItem] | None) -> None:
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

__all__ = ['Browser', 'BrowserItem', 'BrowserItemIterator', 'BrowserItemVector', 'FilterType', 'Relation']
