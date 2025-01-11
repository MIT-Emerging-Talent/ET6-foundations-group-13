#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the product_of_digits function

Created on 5 Jan 2024
@author: Noorelsalam Almakki
"""

import unittest

from solutions.product_of_digits import product_of_digits


class TestProductOfDigits(unittest.TestCase):
    """A class for testing the product_of_digits function"""

    def test_0(self):
        """Test the product_of_digits function with 0"""
        self.assertEqual(product_of_digits(0), 0)

    def test_one_digit(self):
        """Test the product_of_digits function with one digit"""
        self.assertEqual(product_of_digits(5), 5)

    def test_2_digits(self):
        """Test the product_of_digits function with a 2-digit number"""
        self.assertEqual(product_of_digits(12), 2)

    def test_4_digits(self):
        """Test the product_of_digits function with a 4-digit number"""
        self.assertEqual(product_of_digits(1234), 24)

    def test_large_number(self):
        """Test the product_of_digits function with a large number"""
        self.assertEqual(product_of_digits(123456), 720)

    def test_negative_number(self):
        """Test the product_of_digits function with a negative number"""
        self.assertEqual(product_of_digits(-123), -6)

    def test_large_negative_number(self):
        """Test the product_of_digits function with a large negative number"""
        self.assertEqual(product_of_digits(-123456), -720)

    def test_not_an_integer(self):
        """Test the product_of_digits function with a non-integer number"""
        with self.assertRaises(AssertionError):
            product_of_digits(12.4)
