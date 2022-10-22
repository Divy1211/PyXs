class XsObject:
    def __init__(self, op = None):
        self.op = {} if op is None else op

    def __add__(self, other):
        xsobj = self.__class__(super().__add__(other))
        xsobj.op['+'] = self, other
        return xsobj

    def __sub__(self, other):
        xsobj = self.__class__(super().__sub__(other))
        xsobj.op['-'] = self, other
        return xsobj

    def __mul__(self, other):
        xsobj = self.__class__(super().__mul__(other))
        xsobj.op['*'] = self, other
        return xsobj

    def __truediv__(self, other):
        xsobj = self.__class__(super().__truediv__(other))
        xsobj.op['/'] = self, other
        return xsobj

    def __floordiv__(self, other):
        xsobj = self.__class__(super().__floordiv__(other))
        xsobj.op['//'] = self, other
        return xsobj
