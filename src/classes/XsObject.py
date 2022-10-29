from src.enums.XsType import XsType, dtype_name


op_prec = {
    '//': 1,
    '/': 1,
    '*': 1,
    '+': 0,
    '-': 0,
}


class XsObject:

    def __init__(self, dtype: XsType, op = None):
        self.dtype = dtype
        self.op = {} if op is None else op

    def recursively_build_expr(self, p_op = None) -> str:
        if len(self.op) == 0:
            return getattr(self, "var_name", self)

        for op, (left_opr, right_orp) in self.op.items():  # type: XsObject
            expr = f"{left_opr.recursively_build_expr(op)} {op} {right_orp.recursively_build_expr(op)}"
            if p_op is not None and op_prec[p_op] > op_prec[op]:
                expr = f"({expr})"
            return expr


    def __set_name__(self, cls, name):
        self.p_name = name
        self.s_name = f"_{name}"

    def __set__(self, instance, value):
        if not isinstance(value, XsObject):
            raise TypeError(f"{self.p_name} can only be assigned an XsType")

        defn = ""
        if getattr(instance, self.s_name, None) is None:
            defn += f"{dtype_name[self.dtype]} "

        expr = value.recursively_build_expr()
        print(f"{defn}{self.p_name} = {expr};")

        value.var_name = self.p_name
        value.op = {}
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
