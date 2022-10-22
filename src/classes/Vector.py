from functools import cached_property


class Vector:
    def __init__(self, x: float, y: float, z: float):
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

    def normalise(self) -> 'Vector':
        return Vector(self.x/self.length, self.y/self.length, self.z/self.length)

    def __iadd__(self, other) -> None:
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot add type '{type(other)} to 'Vector'")

        self.x += other.x
        self.y += other.y
        self.z += other.z

    def __isub__(self, other) -> None:
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot subtract type '{type(other)} to 'Vector'")

        self.x -= other.x
        self.y -= other.y
        self.z -= other.z

    def __ipow__(self, other) -> None:
        if not isinstance(other, int | float):
            raise TypeError(f"Cannot add type '{type(other)} to 'Vector'")

        self.x *= other
        self.y *= other
        self.z *= other

    def __add__(self, other) -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot add type '{type(other)} to 'Vector'")
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __sub__(self, other) -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot subtract type '{type(other)} from 'Vector'")
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __mul__(self, other) -> float:
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot dot type '{type(other)} with 'Vector'")
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __rmul__(self, other) -> 'Vector':
        if not isinstance(other, int | float):
            raise TypeError(f"Cannot scale 'Vector' by type '{type(other)}'")
        return Vector(self.x*other, self.y*other, self.z*other)

    def __pow__(self, other) -> 'Vector':
        if not isinstance(other, Vector):
            raise TypeError(f"Cannot cross type '{type(other)} with 'Vector'")
        return Vector(self.y*other.z - self.z*other.y, self.z*other.x - self.x*other.z, self.x*other.y + self.y*other.x)

    def __repr__(self) -> str:
        return f'<{self.x}, {self.y}, {self.z}>'
