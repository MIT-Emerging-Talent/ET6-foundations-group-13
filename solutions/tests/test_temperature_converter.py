#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the celsius_to_fahrenheit function.

Created on 01 Jan 2025
@author: Daniel Oluwaluyi
"""

import unittest

from solutions.temperature_converter import temperature_converter


class TestCelsiusToFahrenheit(unittest.TestCase):
    """A class for testing the celsius_to_fahrenheit function."""

    def test_freezing_point(self):
        """Test the freezing point of water."""
        self.assertEqual(temperature_converter(0), 32.0)

    def test_boiling_point(self):
        """Test the boiling point of water."""
        self.assertEqual(temperature_converter(100), 212.0)

    def test_negative_temperature(self):
        """Test a negative temperature (Celsius and Fahrenheit are the same at -40)."""
        self.assertEqual(temperature_converter(-40), -40.0)

    def test_body_temperature(self):
        """Test normal human body temperature."""
        self.assertEqual(temperature_converter(37), 98.6)

    def test_fractional_temperature(self):
        """Test a fractional Celsius temperature."""
        self.assertEqual(temperature_converter(15.5), 59.9)

    def test_large_temperature(self):
        """Test a very large Celsius temperature."""
        self.assertEqual(temperature_converter(1000), 1832.0)

    def test_non_numeric_input(self):
        """Test a non-numeric input."""
        with self.assertRaises(AssertionError):
            temperature_converter("not a number")


if __name__ == "__main__":
    unittest.main()
