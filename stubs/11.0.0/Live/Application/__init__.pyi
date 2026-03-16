from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable, Generic, Iterable, Iterator, TypeVar, overload

T = TypeVar('T')
from .Application import Application

if TYPE_CHECKING:
    from Live.Base import Vector



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

__all__ = ['Application', 'UnavailableFeature', 'UnavailableFeatureVector', 'combine_apcs', 'encrypt_challenge', 'encrypt_challenge2', 'get_application', 'get_random_int']
