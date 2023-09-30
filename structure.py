import inspect
import sys


class Structure:
    _fields = ()

    @staticmethod
    def _init():
        # Reaches stack of another function and examines its variables
        locs = sys._getframe(1).f_locals
        self = locs.pop("self")
        for name, val in locs.items():
            setattr(self, name, val)

    def __init__(self, *args) -> None:
        if len(self._fields) != len(args):
            e = f"Expected {len(self._fields)} arguments"
            raise TypeError(e)
        for field, arg in zip(self._fields, args):
            self.__setattr__(field, arg)

    def __repr__(self):
        return f"""{self.__class__.__name__}({','.join(str(getattr(self, s)) for s in self._fields)})"""

    def __setattr__(self, __name, __value) -> None:
        if __name.startswith("_") or __name in self._fields:
            super().__setattr__(__name, __value)
        else:
            e = f"No attribute {__name}"
            raise AttributeError(e)

    @classmethod
    def set_fields(cls):
        sig = inspect.signature(cls)
        cls._fields = tuple(sig.parameters)
