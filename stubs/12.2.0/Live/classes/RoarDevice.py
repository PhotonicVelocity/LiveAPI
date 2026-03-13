from types import ModuleType
from typing import Callable


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
