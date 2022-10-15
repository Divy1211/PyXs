from classes.ArrayType import ArrayType
from classes.Vector import Vector
from utils import bigger_pow_2


class Array:
    _last_id = 0
    _dtype_name = {
        ArrayType.INT:    "int",
        ArrayType.FLOAT:  "float",
        ArrayType.BOOL:   "bool",
        ArrayType.STRING: "string",
        ArrayType.VECTOR: "vector",
    }
    _dtype = {
        ArrayType.INT: int,
        ArrayType.FLOAT: float,
        ArrayType.BOOL: bool,
        ArrayType.STRING: str,
        ArrayType.VECTOR: Vector,
    }

    def __init__(self, dtype: ArrayType, ls: list[int] = None):
        if ls is None:
            ls = []

        self.dtype_name = Array._dtype_name[dtype].title()
        self.dtype: type = Array._dtype[dtype]

        self._len = bigger_pow_2(len(ls))
        Array._last_id += 1
        self._id = Array._last_id

        print(self._define())

        for i, ele in enumerate(ls):
            if not isinstance(ele, self.dtype): # type: ignore # pycharm bug https://stackoverflow.com/a/56494823/15379178
                raise TypeError(f"{ele} of type '{type(ele)}' cannot be assigned to an array of type {self.dtype}")
            print(self._set(i, ele))

        self._ls = ls

    def _define(self):
        return f'int array{self._id} = xsArrayCreate{self.dtype_name}(-1, {self._len}, "array{self._id}");'

    def _check_bounds(self, idx):
        if idx >= len(self._ls) or idx < -len(self._ls):
            raise IndexError(f"Index = {idx} is out of bounds")

        if idx < 0:
            idx += len(self._ls)

        return idx

    def _open_slice(self, slc: slice):
        start, stop, step = slc.start or 0, slc.stop or len(self._ls), slc.step or 1

        if step == 0:
            raise ValueError("Step size cannot be 0")

        if not all([isinstance(start, int | None), isinstance(start, int | None), isinstance(start, int | None)]):
            raise TypeError(f"slice indices must be of type 'None' or 'int'")

        if start < 0:
            start += len(self._ls)
        if stop < 0:
            stop += len(self._ls)
        if step < 0:
            start, stop, step = stop, start, -step

        return start, stop, step

    def __getitem__(self, item: int | slice):
        if isinstance(item, int):
            item = self._check_bounds(item)
            print(self._get(item))
            return self._ls[item]
        elif not isinstance(item, slice):
            raise TypeError(f"Array indices must be of type 'int' or 'slice'")

        start, stop, step = self._open_slice(item)

        for idx in range(start, stop, step):
            print(self._get(idx))

        return self._ls[start:stop:step]

    def __setitem__(self, item: int | slice, val):
        if isinstance(item, int):
            item = self._check_bounds(item)
            print(self._set(item, val))
            self._ls[item] = val
            return
        elif not isinstance(item, slice):
            raise IndexError

        start, stop, step = self._open_slice(item)

        for idx, ele in zip(range(start, stop, step), val):
            if not isinstance(ele, self.dtype): # type: ignore # pycharm bug https://stackoverflow.com/a/56494823/15379178
                raise Exception
            print(self._set(idx, ele))

        self._ls[start:stop:step] = val

    def _get(self, idx: int) -> str:
        return f'xsArrayGet{self.dtype_name}(array{self._id}, {idx});'

    def _set(self, idx: int, val) -> str:
        return f'xsArraySet{self.dtype_name}(array{self._id}, {idx}, {val});'
