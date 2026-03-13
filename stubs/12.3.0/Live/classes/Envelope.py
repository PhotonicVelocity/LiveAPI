from types import ModuleType
from typing import Callable


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
