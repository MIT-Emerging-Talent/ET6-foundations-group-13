#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the find_min_max function.

Created on 02 Jan 2025

@author: Tosan Okome
"""

import unittest

from ..find_min_max import find_min_max


class TestFindMinMax(unittest.TestCase):
    """Test the find_min_max function"""

    def test_positive_numbers(self):
        """It should return (1, 4)"""
        actual = find_min_max([1, 2, 3, 4])
        expected = (1, 4)
        self.assertEqual(actual, expected)

    def test_negative_numbers(self):
        """It should return (-10, -1)"""
        actual = find_min_max([-10, -5, -1])
        expected = (-10, -1)
        self.assertEqual(actual, expected)

    def test_mixed_numbers(self):
        """It should return (-1, 10)"""
        actual = find_min_max([-1, 0, 5, 10])
        expected = (-1, 10)
        self.assertEqual(actual, expected)

    def test_decimal_numbers(self):
        """It should return (0.5526, 0.765)"""
        actual = find_min_max([0.765, 0.651, 0.5526, 0.653])
        expected = (0.5526, 0.765)
        self.assertEqual(actual, expected)

    def test_single_element(self):
        """It should return (7, 7)"""
        actual = find_min_max([7])
        expected = (7, 7)
        self.assertEqual(actual, expected)

    def test_empty_list(self):
        """It should return a ValueError with an empty list"""
        with self.assertRaises(ValueError):
            find_min_max([])

    def test_non_numeric_elements(self):
        """It should return a ValueError with a non-numeric list"""
        with self.assertRaises(ValueError):
            find_min_max([1, "a", 2.5])
