from types import ModuleType
from typing import Callable


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
