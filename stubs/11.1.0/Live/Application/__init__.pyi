from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')
from .Application import Application

if TYPE_CHECKING:
    from Live.Base import Vector



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
