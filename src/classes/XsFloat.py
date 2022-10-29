from src.classes.XsObject import XsObject


class XsFloat(XsObject, float):
    def __init__(self, val, op = None):
        super().__init__(op)

    def cast_to(self, dtype: type) -> XsObject | None:
        if dtype is int:
            from src.classes.XsInt import XsInt
            xsobj = XsInt(self)
            xsobj.op = self.op
            return xsobj
        return None

