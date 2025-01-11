#!/usr/bin/env python3
# -- coding: utf-8 --
"""
Test module for the string_length function.

This file includes unittest to verify the correctness of the string_length function.
It tests the function with standard cases and edge cases.
Test categories:
    - Standard cases: strings with mixed characters, empty strings
    - Edge cases: string with spaces, strings with special characters

Created on 06 January 2025
@author: Safiya Hash

"""

import unittest

from solutions.string_length import string_length


class TestStringLength(unittest.TestCase):
    """
    These unittest cases will verify the correctness of the string_length function.
    """


def test_empty_string(self):
    """It should return zero for an empty string."""
    self.assertEqual(string_length(""), 0)


def test_word(self):
    """It should return the correct length for a word."""
    self.assertEqual(string_length("Hey"), 3)


def test_sentence(self):
    """It should return the correct length for a sentence with spaces."""
    self.assertEqual(string_length("Second challenge!"), 17)


def test_numerics_as_string(self):
    """It should return the correct length for numeric characters in a string."""
    self.assertEqual(string_length("12345"), 5)


def test_special_characters(self):
    """It should return the correct length for a string with special characters."""
    self.assertEqual(string_length("!@#$%"), 5)


def test_spaces_as_string(self):
    """It should return the correct length of spaces in a string."""
    self.assertEqual(string_length("          "), 10)


def test_mixed_characters(self):
    """It should return the correct length for a string with mixed characters."""
    self.assertEqual(string_length("Documenting,testing and debugging"), 33)


def test_non_string_values(self):
    """It should return a TypeError with non string values"""
    with self.assertRaises(TypeError):
        string_length([1, 2, 5.5, 5])
