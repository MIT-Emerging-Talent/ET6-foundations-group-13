import unittest

from ..temperature_converter import celsius_to_fahrenheit


class TestConverter(unittest.TestCase):
    def test_positive_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(1), 33.8)

    def test_negative_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(-1), 30.2)

    def test_float_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(32.77), 90.986)

    def test_zero_temperature(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32)
