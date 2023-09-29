import unittest


def add(a, b):
    return a + b


def is_zero(a):
    return a == 0


def add2(a, b):
    if type(a) != int or type(b) != int:
        raise TypeError("Inputs must be integers")
    return a + b


class test(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(1, 2), 3)

    def test_is_zero(self):
        self.assertTrue(is_zero(1))

    def test_add2(self):
        self.assertRaises(TypeError, add2, "a", "b")
        raise AssertionError
