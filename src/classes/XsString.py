from src.classes.XsObject import XsObject


class XsString(XsObject, str):
    def __init__(self, val, op = None):
        super().__init__(op)
