import unittest
from unittest import result
import UnitTesting

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(UnitTesting.add(20, 5), 25)
        self.assertEqual(UnitTesting.add(-20, 5), -15)
        self.assertEqual(UnitTesting.add(-20, -5), -25)

    def test_subtract(self):
        self.assertEqual(UnitTesting.subtract(10, 5), 5)
        self.assertEqual(UnitTesting.subtract(-1, 1), -2)
        self.assertEqual(UnitTesting.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(UnitTesting.multiply(10, 5), 50)
        self.assertEqual(UnitTesting.multiply(-1, 1), -1)
        self.assertEqual(UnitTesting.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(UnitTesting.divide(10, 5), 2)
        self.assertEqual(UnitTesting.divide(-1, 1), -1)
        self.assertEqual(UnitTesting.divide(-1, -1), 1)
        self.assertEqual(UnitTesting.divide(5, 2), 2.5)

        with self.assertRaises(ValueError):
            UnitTesting.divide(10, 0)


if __name__ == '__main__':
    unittest.main()