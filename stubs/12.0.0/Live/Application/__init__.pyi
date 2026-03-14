from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable
from .Application import Application


class ControlDescription:
    """Describes a control present in a control surface proxy"""

    def __init__(self) -> None: ...

    @property
    def id(self) -> int:
        ...

    @property
    def name(self) -> str:
        ...

class ControlDescriptionVector:
    """A container for returning control descriptions."""

    def append(self, value: ControlDescription | None) -> None:
        ...

    def extend(self, values: ControlDescription | None) -> None:
        ...

class ControlSurfaceProxy:
    """Represents a control surface running in a different process. For use by M4L"""

    def add_control_values_arrived_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "control_values_arrived" has changed.
        """
        ...

    def add_midi_received_listener(self, callback: Callable | None) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "midi_received" has changed.
        """
        ...

    @property
    def control_descriptions(self) -> tuple[ControlDescription, ...]:
        ...

    def control_values_arrived_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "control_values_arrived".
        """
        ...

    def enable_receive_midi(self, enabled: bool | None) -> None:
        ...

    def fetch_received_midi_messages(self) -> tuple:
        ...

    def fetch_received_values(self) -> tuple:
        ...

    def grab_control(self, control: int | None) -> None:
        ...

    def midi_received_has_listener(self, callback: Callable | None) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "midi_received".
        """
        ...

    def release_control(self, control: int | None) -> None:
        ...

    def remove_control_values_arrived_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "control_values_arrived".
        """
        ...

    def remove_midi_received_listener(self, callback: Callable | None) -> None:
        """
        Remove a previously set listener function or method from
        property "midi_received".
        """
        ...

    def send_midi(self, midi_event_bytes: tuple | None) -> None:
        ...

    def send_value(self, value: tuple | None) -> None:
        ...

    def subscribe_to_control(self, control: int | None) -> None:
        ...

    @property
    def type_name(self) -> str:
        ...

    def unsubscribe_from_control(self, control: int | None) -> None:
        ...

class MessageButtons:
    """Specifies the characteristics of the message box, e.g. which buttons to show."""
    OK_BUTTON: int = 0

class UnavailableFeature:
    note_velocity_ranges_and_probabilities: int = 0

class UnavailableFeatureVector:
    """A container for returning unavailable features."""

    def append(self, value: UnavailableFeature | None) -> None:
        ...

    def extend(self, values: UnavailableFeature | None) -> None:
        ...

class Variants:
    """Holds strings representing what type of Live is running."""
    BETA: str = "Beta"
    INTRO: str = "Intro"
    LITE: str = "Lite"
    STANDARD: str = "Standard"
    SUITE: str = "Suite"
    TRIAL: str = "Trial"

def combine_apcs() -> bool:
    """Returns true if multiple APCs should be combined."""
    ...

def encrypt_challenge(dongle1: int | None, dongle2: int | None, key_index: int = 0) -> tuple:
    """Returns an encrypted challenge based on the TEA algortithm"""
    ...

def encrypt_challenge2(challenge: int | None) -> int:
    """Returns the UMAC hash for the given challenge."""
    ...

def get_application() -> Application:
    """Returns the application instance."""
    ...

def get_random_int(min_value: int | None, max_value: int | None) -> int:
    """Returns a random integer from the given range."""
    ...

__all__ = ['Application', 'ControlDescription', 'ControlDescriptionVector', 'ControlSurfaceProxy', 'MessageButtons', 'UnavailableFeature', 'UnavailableFeatureVector', 'Variants', 'combine_apcs', 'encrypt_challenge', 'encrypt_challenge2', 'get_application', 'get_random_int']
