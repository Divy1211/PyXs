from math import ceil, log

from src.enums.XsType import XsType


def bigger_pow_2(num: float) -> int:
    if num < 8:
        return 8
    return 2 ** ceil(log(num))


op_prec = {
    '//': 1,
    '/': 1,
    '*': 1,
    '+': 0,
    '-': 0,
}
dtype_name = {
    XsType.INT: "int",
    XsType.FLOAT: "float",
    XsType.BOOL: "bool",
    XsType.STRING: "string",
    XsType.VECTOR: "vector",
}

def get_dtype_map():
    from src.classes.XsInt import XsInt
    from src.classes.XsFloat import XsFloat
    from src.classes.XsString import XsString
    from src.classes.XsVector import XsVector

    return {
        XsType.INT: XsInt,
        XsType.FLOAT: XsFloat,
        XsType.BOOL: bool,
        XsType.STRING: XsString,
        XsType.VECTOR: XsVector,
    }
