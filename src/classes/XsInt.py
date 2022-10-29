from src.classes.XsObject import XsObject


class XsInt(XsObject, int):
    def __init__(self, val, op = None):
        super().__init__(op)
