from src.classes.Vector import Vector
from src.classes.XsObject import XsObject


class XsVector(XsObject, Vector):
    def __init__(self, x, y, z = 0, op = None):
        super().__init__(op)
