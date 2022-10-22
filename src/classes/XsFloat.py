from src.classes.XsObject import XsObject


class XsFloat(XsObject, float):
    def __init__(self, val, op = None):
        super().__init__(op)

