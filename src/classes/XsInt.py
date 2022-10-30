from src.classes.XsObject import XsObject


class XsInt(XsObject, int):
    def __init__(self, val, op = None):
        super().__init__(op)

    def cast_to(self, dtype: type) -> XsObject | None:
        from src.classes.XsFloat import XsFloat
        if dtype is XsFloat:
            xsobj = XsFloat(self)
            xsobj.op = self.op
            return xsobj
        return None
