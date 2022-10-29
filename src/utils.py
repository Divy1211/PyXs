from math import ceil, log

from src.classes.Vector import Vector
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
dtype_map = {
    XsType.INT: int,
    XsType.FLOAT: float,
    XsType.BOOL: bool,
    XsType.STRING: str,
    XsType.VECTOR: Vector,
}
