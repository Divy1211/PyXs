from __future__ import annotations

import math
from functools import cached_property

class Vector:
    """
    A mathematical entity, not a list. Supports:

    - +, +=
    - \-
    - -, -=
    - \* (scale & dot), *= (scale)
    - /, /=
    - //, //=
    - **, **= (cross)
    - ==, !=
    - length
    - unit
    - x
    - y
    - z
    """
    def __init__(self, x: float, y: float, z: float = 0):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def z(self):
        return self._z

    @x.setter
    def x(self, val: float):
        self._x = val

    @y.setter
    def y(self, val: float):
        self._y = val

    @z.setter
    def z(self, val: float):
        self._z = val

    @cached_property
    def length(self) -> float:
        return (self.x**2 + self.y**2 + self.z**2)**0.5

    @cached_property
    def unit(self) -> Vector:
        return Vector(self.x/self.length, self.y/self.length, self.z/self.length)

    def __add__(self, other) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
        if isinstance(other, int | float):
            return Vector(self.x+other, self.y+other, self.z+other)
        raise TypeError(f"Cannot add type '{type(other)} to Vector")

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other) -> Vector:
        if isinstance(other, Vector):
            self.x += other.x
            self.y += other.y
            self.z += other.z
            return self
        if isinstance(other, int | float):
            self.x += other
            self.y += other
            self.z += other
            return self
        raise TypeError(f"Cannot add type '{type(other)} to Vector")

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)

    def __sub__(self, other) -> Vector:
        if isinstance(other, Vector):
            return Vector(self.x-other.x, self.y-other.y, self.z-other.z)
        if isinstance(other, int | float):
            return Vector(self.x-other, self.y-other, self.z-other)
        raise TypeError(f"Cannot subtract type '{type(other)} from Vector")

    def __rsub__(self, other):
        return (-self).__add__(other)

    def __isub__(self, other) -> Vector:
        if isinstance(other, Vector):
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
            return self
        if isinstance(other, int | float):
            self.x -= other
            self.y -= other
            self.z -= other
            return self
        raise TypeError(f"Cannot subtract type '{type(other)} to Vector")

    def __mul__(self, other) -> Vector | float:
        if isinstance(other, float | int):
            return Vector(self.x*other, self.y*other, self.z*other)
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        raise TypeError(f"Cannot scale Vector by type '{type(other)}")

    def __rmul__(self, other) -> Vector:
        return self.__mul__(other)

    def __imul__(self, other) -> Vector:
        if isinstance(other, int | float):
            self.x *= other
            self.y *= other
            self.z *= other
            return self
        raise TypeError(f"Cannot scale Vector by type '{type(other)}'")

    def __truediv__(self, other) -> Vector:
        return self.__mul__(1/other)

    def __itruediv__(self, other) -> Vector:
        return self.__imul__(1/other)

    def __floordiv__(self, other) -> Vector:
        if isinstance(other, float | int):
            return Vector(self.x//other, self.y//other, self.z//other)
        raise TypeError(f"Cannot scale Vector by type '{type(other)}")

    def __ifloordiv__(self, other) -> Vector:
        if isinstance(other, int | float):
            self.x //= other
            self.y //= other
            self.z //= other
            return self
        raise TypeError(f"Cannot scale Vector by type '{type(other)}'")

    # cross product
    def __pow__(self, other) -> Vector:
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot cross type '{type(other)} with Vector")
        return Vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y + self.y*other.x)

    def __ipow__(self, other) -> Vector:
        vec = self**other
        self.x = vec.x
        self.y = vec.y
        self.z = vec.z
        return self

    def __repr__(self) -> str:
        return f'<{self.x}, {self.y}, {self.z}>'

    def __eq__(self, other) -> bool:
        if not isinstance(other, Vector):
            return False
        return all([
            math.isclose(self.x, other.x),
            math.isclose(self.y, other.y),
            math.isclose(self.z, other.z),
        ])

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)
