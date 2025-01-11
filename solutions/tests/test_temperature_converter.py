import unittest

from solutions.temperature_converter import temperature_converter


class TestConverter(unittest.TestCase):
    """Test to convert temperature"""

    def test_positive_temperature(self):
        """It should return a a positive value"""
        self.assertEqual(temperature_converter(1), 33.8)

    def test_negative_temperature(self):
        """It should return a value even when negative inputs are made"""
        self.assertEqual(temperature_converter(-1), 30.2)

    def test_float_temperature(self):
        """It should give an output in spite of the float value"""
        self.assertEqual(temperature_converter(32.77), 90.986)

    def test_zero_temperature(self):
        """It gives an output for when input is 0"""
        self.assertEqual(temperature_converter(0), 32)


if __name__ == "__main__":
    unittest.main()
