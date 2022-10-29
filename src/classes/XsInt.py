from src.classes.XsObject import XsObject
from src.enums.XsType import XsType


class XsInt(XsObject, int):
    def __init__(self, val, op = None):
        super().__init__(op)


class Ctx:
    x = XsObject(XsType.INT)
    y = XsObject(XsType.INT)
    z = XsObject(XsType.INT)

a = Ctx()

a.x = XsInt(1)
a.y = XsInt(2)
a.z = a.x
a.z = (a.z+a.x)/a.y
a.x = a.z
a.x = XsInt(10)

