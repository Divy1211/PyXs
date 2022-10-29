from enum import IntEnum
from src.classes.Vector import Vector


class XsType(IntEnum):
    INT = 0
    FLOAT = 1
    BOOL = 2
    STRING = 3
    VECTOR = 4

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