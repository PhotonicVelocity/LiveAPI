from types import ModuleType
from typing import Callable


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
