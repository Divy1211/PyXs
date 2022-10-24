class XsObject:
    def __init__(self, op = None):
        self.op = {} if op is None else op

    def __set_name__(self, cls, name):
        self.p_name = name
        self.s_name = f"_{name}"

    def __set__(self, instance, value):
        setattr(instance, self.s_name, value)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        return getattr(instance, self.s_name)

    def __add__(self, other):
        xsobj = self.__class__(super().__add__(other))
        xsobj.op['+'] = self, other
        return xsobj

    def __iadd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        xsobj = self.__class__(super().__sub__(other))
        xsobj.op['-'] = self, other
        return xsobj

    def __isub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        xsobj = self.__class__(super().__mul__(other))
        xsobj.op['*'] = self, other
        return xsobj

    def __imul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        xsobj = self.__class__(super().__truediv__(other))
        xsobj.op['/'] = self, other
        return xsobj

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __floordiv__(self, other):
        xsobj = self.__class__(super().__floordiv__(other))
        xsobj.op['//'] = self, other
        return xsobj

    def __ifloordiv__(self, other):
        return self.__floordiv__(other)
