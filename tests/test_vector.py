import unittest

from src.classes.Vector import Vector


class TestVector(unittest.TestCase):
    def test_addition(self):
        a = Vector(1, 2, 3)
        b = a+a
        c = a+5
        d = 5+a
        self.assertEqual(b, Vector(2, 4, 6))
        self.assertEqual(c, Vector(6, 7, 8))
        self.assertEqual(d, Vector(6, 7, 8))
        a += a
        self.assertEqual(a, Vector(2, 4, 6))

    def test_negation(self):
        a = Vector(1, 2, 3)
        self.assertEqual(-a, Vector(-1, -2, -3))

    def test_subtraction(self):
        a = Vector(1, 2, 3)
        b = a-a
        c = a-5
        d = 5-a
        self.assertEqual(b, Vector(0, 0, 0))
        self.assertEqual(c, Vector(-4, -3, -2))
        self.assertEqual(d, Vector(4, 3, 2))
        a -= a
        self.assertEqual(a, Vector(0, 0, 0))

    def test_multiplication(self):
        a = Vector(1, 2, 3)
        c = a*5
        d = 5*a
        self.assertEqual(c, Vector(5, 10, 15))
        self.assertEqual(d, Vector(5, 10, 15))
        a *= 5
        self.assertEqual(a, Vector(5, 10, 15))

    def test_truedivision(self):
        a = Vector(1, 2, 3)
        c = a/5
        self.assertEqual(c, Vector(1/5, 2/5, 3/5))
        a /= 5
        self.assertEqual(a, Vector(1/5, 2/5, 3/5))

    def test_floordivision(self):
        a = Vector(1, 5, 10)
        c = a//5
        self.assertEqual(c, Vector(0, 1, 2))
        a //= 5
        self.assertEqual(a, Vector(0, 1, 2))

    def test_cross(self):
        i = Vector(1, 0, 0)
        j = Vector(0, 1, 0)
        k = Vector(0, 0, 1)
        self.assertEqual(i**j, k)
        self.assertEqual(j**k, i)
        self.assertEqual(k**i, j)

    def test_eq(self):
        i = Vector(1, 0, 0)
        j = Vector(0, 1, 0)
        self.assertTrue(i == i)
        self.assertFalse(i == j)
        self.assertFalse(i == 1)
        self.assertTrue(i != j)
        self.assertFalse(i != i)
        self.assertTrue(i != 1)

    def test_length(self):
        i = Vector(1, 0, 0)
        a = Vector(1, 2, 3)
        self.assertEqual(i.length, 1)
        self.assertEqual(a.length, 14**0.5)

    def test_unit(self):
        a = Vector(5, 0, 0)
        b = Vector(3, 3, 3)
        self.assertEqual(a.unit, Vector(1, 0, 0))
        self.assertEqual(b.unit, Vector(1/3**0.5, 1/3**0.5, 1/3**0.5))

    def test_dot(self):
        a = Vector(5, 1, 2)
        b = Vector(3, 3, 3)
        self.assertEqual(a*b, 24)


if __name__ == '__main__':
    unittest.main()
