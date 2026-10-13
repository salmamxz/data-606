
import unittest
from calculator import subtract


class TestCalculator(unittest.TestCase):

    # test subtraction with positive numbers
    def test_subtract_positive(self):
        self.assertEqual(subtract(5, 3), 2)

    # test subtraction with negative numbers
    def test_subtract_negative(self):
        self.assertEqual(subtract(-5, -3), -2)

    # test subtraction with zero
    def test_subtract_zero(self):
        self.assertEqual(subtract(5, 0), 5)


if __name__ == "__main__":
    unittest.main()
