from functools import wraps
import inspect
from typing import Type

from src.classes.XsContext import XsContext
from src.classes.XsObject import XsObject
from src.utils import get_dtype_map, dtype_name

def xs_function(ctx: Type[XsContext]):
    if ctx._used:
        raise TypeError(f"Context '{ctx.__name__}' has already been used!")

    def decorator(func):
        dtype_map = get_dtype_map()
        reverse_dtype_map = {v: k for k, v in dtype_map.items()}

        def class_name_map(x):
            if x is None or x is inspect.Parameter.empty:
                return 'void'
            return dtype_name[reverse_dtype_map[x]]

        signature = inspect.signature(func)

        sign = f"{class_name_map(signature.return_annotation)} {func.__name__}("
        for param, val in signature.parameters.items():
            if val.default is inspect.Parameter.empty:
                raise ValueError(f"parameter {param} of function {func.__name__} is missing a default value")
            if not isinstance(val.default, val.annotation):
                raise TypeError(f"Cannot assign object of type '{type(val.default).__name__}' to object of type '{val.annotation.__name__}'")

            xsobj = XsObject(reverse_dtype_map[val.annotation])
            xsobj.__set_name__(ctx, param)
            setattr(ctx, param, xsobj)
            ctx._params[param] = val.default
            ctx._params[param].var_name = param
            ctx._used = True

            sign += f"{class_name_map(val.annotation)} {param} = {val.default}, "
        sign = sign[:-2]+") {"

        print(sign)
        val: XsObject = func()
        print(f"return ({val.recursively_build_expr()});")
        print("}")

        @wraps(func)
        def wrapper(*args, **kwargs):
            print("func called")
            return func(*args, **kwargs)

        return wrapper
    return decorator
