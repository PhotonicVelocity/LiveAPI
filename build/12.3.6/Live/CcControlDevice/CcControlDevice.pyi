from __future__ import annotations
from typing import TYPE_CHECKING, Any, Callable


class CcControlDevice:
    """This class represents a CcControl device."""

    @property
    def _live_ptr(self) -> int:
        ...

    def add_custom_bool_target_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_bool_target" has changed.
        """
        ...

    def add_custom_float_target_0_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_0" has changed.
        """
        ...

    def add_custom_float_target_10_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_10" has changed.
        """
        ...

    def add_custom_float_target_11_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_11" has changed.
        """
        ...

    def add_custom_float_target_1_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_1" has changed.
        """
        ...

    def add_custom_float_target_2_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_2" has changed.
        """
        ...

    def add_custom_float_target_3_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_3" has changed.
        """
        ...

    def add_custom_float_target_4_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_4" has changed.
        """
        ...

    def add_custom_float_target_5_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_5" has changed.
        """
        ...

    def add_custom_float_target_6_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_6" has changed.
        """
        ...

    def add_custom_float_target_7_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_7" has changed.
        """
        ...

    def add_custom_float_target_8_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_8" has changed.
        """
        ...

    def add_custom_float_target_9_listener(self, callback: Callable) -> None:
        """
        Add a listener function or method, which will be called as soon as the
        property "custom_float_target_9" has changed.
        """
        ...

    @property
    def custom_bool_target(self) -> int:
        """Return the custom bool target"""
        ...

    @custom_bool_target.setter
    def custom_bool_target(self, value: int) -> None: ...

    def custom_bool_target_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_bool_target".
        """
        ...

    @property
    def custom_bool_target_list(self) -> tuple[str, ...]:
        """Return the custom bool target list"""
        ...

    @property
    def custom_float_target_0(self) -> int:
        """Return the custom float target 0"""
        ...

    @custom_float_target_0.setter
    def custom_float_target_0(self, value: int) -> None: ...

    def custom_float_target_0_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_0".
        """
        ...

    @property
    def custom_float_target_0_list(self) -> tuple[str, ...]:
        """Return the custom float target 0 list"""
        ...

    @property
    def custom_float_target_1(self) -> int:
        """Return the custom float target 1"""
        ...

    @custom_float_target_1.setter
    def custom_float_target_1(self, value: int) -> None: ...

    @property
    def custom_float_target_10(self) -> int:
        """Return the custom float target 10"""
        ...

    @custom_float_target_10.setter
    def custom_float_target_10(self, value: int) -> None: ...

    def custom_float_target_10_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_10".
        """
        ...

    @property
    def custom_float_target_10_list(self) -> tuple[str, ...]:
        """Return the custom float target 10 list"""
        ...

    @property
    def custom_float_target_11(self) -> int:
        """Return the custom float target 11"""
        ...

    @custom_float_target_11.setter
    def custom_float_target_11(self, value: int) -> None: ...

    def custom_float_target_11_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_11".
        """
        ...

    @property
    def custom_float_target_11_list(self) -> tuple[str, ...]:
        """Return the custom float target 11 list"""
        ...

    def custom_float_target_1_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_1".
        """
        ...

    @property
    def custom_float_target_1_list(self) -> tuple[str, ...]:
        """Return the custom float target 1 list"""
        ...

    @property
    def custom_float_target_2(self) -> int:
        """Return the custom float target 2"""
        ...

    @custom_float_target_2.setter
    def custom_float_target_2(self, value: int) -> None: ...

    def custom_float_target_2_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_2".
        """
        ...

    @property
    def custom_float_target_2_list(self) -> tuple[str, ...]:
        """Return the custom float target 2 list"""
        ...

    @property
    def custom_float_target_3(self) -> int:
        """Return the custom float target 3"""
        ...

    @custom_float_target_3.setter
    def custom_float_target_3(self, value: int) -> None: ...

    def custom_float_target_3_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_3".
        """
        ...

    @property
    def custom_float_target_3_list(self) -> tuple[str, ...]:
        """Return the custom float target 3 list"""
        ...

    @property
    def custom_float_target_4(self) -> int:
        """Return the custom float target 4"""
        ...

    @custom_float_target_4.setter
    def custom_float_target_4(self, value: int) -> None: ...

    def custom_float_target_4_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_4".
        """
        ...

    @property
    def custom_float_target_4_list(self) -> tuple[str, ...]:
        """Return the custom float target 4 list"""
        ...

    @property
    def custom_float_target_5(self) -> int:
        """Return the custom float target 5"""
        ...

    @custom_float_target_5.setter
    def custom_float_target_5(self, value: int) -> None: ...

    def custom_float_target_5_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_5".
        """
        ...

    @property
    def custom_float_target_5_list(self) -> tuple[str, ...]:
        """Return the custom float target 5 list"""
        ...

    @property
    def custom_float_target_6(self) -> int:
        """Return the custom float target 6"""
        ...

    @custom_float_target_6.setter
    def custom_float_target_6(self, value: int) -> None: ...

    def custom_float_target_6_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_6".
        """
        ...

    @property
    def custom_float_target_6_list(self) -> tuple[str, ...]:
        """Return the custom float target 6 list"""
        ...

    @property
    def custom_float_target_7(self) -> int:
        """Return the custom float target 7"""
        ...

    @custom_float_target_7.setter
    def custom_float_target_7(self, value: int) -> None: ...

    def custom_float_target_7_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_7".
        """
        ...

    @property
    def custom_float_target_7_list(self) -> tuple[str, ...]:
        """Return the custom float target 7 list"""
        ...

    @property
    def custom_float_target_8(self) -> int:
        """Return the custom float target 8"""
        ...

    @custom_float_target_8.setter
    def custom_float_target_8(self, value: int) -> None: ...

    def custom_float_target_8_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_8".
        """
        ...

    @property
    def custom_float_target_8_list(self) -> tuple[str, ...]:
        """Return the custom float target 8 list"""
        ...

    @property
    def custom_float_target_9(self) -> int:
        """Return the custom float target 9"""
        ...

    @custom_float_target_9.setter
    def custom_float_target_9(self, value: int) -> None: ...

    def custom_float_target_9_has_listener(self, callback: Callable) -> bool:
        """
        Returns true, if the given listener function or method is connected
        to the property "custom_float_target_9".
        """
        ...

    @property
    def custom_float_target_9_list(self) -> tuple[str, ...]:
        """Return the custom float target 9 list"""
        ...

    def remove_custom_bool_target_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_bool_target".
        """
        ...

    def remove_custom_float_target_0_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_0".
        """
        ...

    def remove_custom_float_target_10_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_10".
        """
        ...

    def remove_custom_float_target_11_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_11".
        """
        ...

    def remove_custom_float_target_1_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_1".
        """
        ...

    def remove_custom_float_target_2_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_2".
        """
        ...

    def remove_custom_float_target_3_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_3".
        """
        ...

    def remove_custom_float_target_4_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_4".
        """
        ...

    def remove_custom_float_target_5_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_5".
        """
        ...

    def remove_custom_float_target_6_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_6".
        """
        ...

    def remove_custom_float_target_7_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_7".
        """
        ...

    def remove_custom_float_target_8_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_8".
        """
        ...

    def remove_custom_float_target_9_listener(self, callback: Callable) -> None:
        """
        Remove a previously set listener function or method from
        property "custom_float_target_9".
        """
        ...

    def resend(self) -> None:
        """Resend all CC values."""
        ...

__all__ = ['CcControlDevice']
