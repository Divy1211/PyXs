from src.classes.Vector import Vector
from src.classes.XsObject import XsObject


class XsInt(XsObject, Vector):
    def __init__(self, x, y, z, op = None):
        super().__init__(op)
