from src.classes.XsObject import XsObject
from src.utils import get_dtype_map


class XsContext:
    _used = False
    _params = {}

    def __init__(self):
        for param, val in self.__class__._params.items():
            setattr(self, f"_{param}", val)

    def __setattr__(self, key, value):
        if key.startswith("_"):
            self.__dict__[key] = value
            return

        if (xsobj := getattr(self.__class__, key, None)) is None:
            dtype_map = get_dtype_map()
            reverse_dtype_map = {v: k for k, v in dtype_map.items()}

            xsobj = XsObject(reverse_dtype_map[type(value)])
            xsobj.__set_name__(self.__class__, key)
            setattr(self.__class__, key, xsobj)

        xsobj.__set__(self, value)
