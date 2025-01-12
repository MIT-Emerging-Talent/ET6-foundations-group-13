#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for testing the count_vowels function.

Created on 29 Dec 2024
@author: Daniel Oluwaluyi
"""

import unittest

from solutions.count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    """A class for testing the count_vowels function."""

    def test_empty_string(self):
        """Test the count_vowels function with an empty string."""
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """Test the count_vowels function with a string containing no vowels."""
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_all_vowels(self):
        """Test the count_vowels function with a string containing all vowels."""
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_mixed_string(self):
        """Test the count_vowels function with a string containing vowels and consonants."""
        self.assertEqual(count_vowels("Hello, World!"), 3)

    def test_numeric_and_special_characters(self):
        """Test the count_vowels function with a string containing numbers and special characters."""
        self.assertEqual(count_vowels("12345!@#$%^&*()"), 0)

    def test_vowels_in_words(self):
        """Test the count_vowels function with a string containing multiple words."""
        self.assertEqual(count_vowels("Python programming is fun!"), 6)

    def test_string_with_whitespace(self):
        """Test the count_vowels function with a string containing leading and trailing whitespace."""
        self.assertEqual(count_vowels("  aeiou  "), 5)

    def test_non_string_input(self):
        """Test the count_vowels function with a non-string input."""
        with self.assertRaises(AssertionError):
            count_vowels(12345)


if __name__ == "__main__":
    unittest.main()
