import unittest
from solutions.count_string import count_string


"""
Test module for the count_string function.
This file includes unittest to verify the correctness of the count_string function.
It tests the function with standard cases and edge cases.
Test categories:
    - Standard cases: Test that the function correctly counts a single occurrence of a letter.
    - Edge cases: empty sentence and empty letter
    - Large input: lists with a large range of strings (e.g., thousands)
Created on: 07 January 2025
Author: Hope Udoh
"""


class TestCountString(unittest.TestCase):
    """
    Test suite for the count_string function.
    """

    # Standard Cases
    def test_single_occurrence(self):
        """
        Standard Case: Test that the function correctly counts a single occurrence of a letter.

        Example:
        >>> count_string("hello", "e")
        'The letter 'e' appears 1 times'
        """
        self.assertEqual(count_string("hello", "e"), "The letter 'e' appears 1 times")

    def test_multiple_occurrences(self):
        """
        Standard Case: Test that the function correctly counts multiple occurrences of a letter.

        Example:
        >>> count_string("banana", "a")
        'The letter 'a' appears 3 times'
        """
        self.assertEqual(count_string("banana", "a"), "The letter 'a' appears 3 times")

    def test_no_occurrence(self):
        """
        Standard Case: Test that the function returns zero when the letter does not occur.

        Example:
        >>> count_string("world", "x")
        'The letter 'x' appears 0 times'
        """
        self.assertEqual(count_string("world", "x"), "The letter 'x' appears 0 times")

    # Edge Cases
    def test_empty_sentence(self):
        """
        Edge Case: Test that the function returns zero when the sentence is empty.

        Example:
        >>> count_string("", "a")
        'The letter 'a' appears 0 times'
        """
        self.assertEqual(count_string("", "a"), "The letter 'a' appears 0 times")

    def test_empty_letter(self):
        """
        Edge Case: Test that the function raises a ValueError when the letter is empty.

        Raises:
            ValueError: If the letter is an empty string.

        Example:
        >>> count_string("hello", "")
        Traceback (most recent call last):
        ...
        ValueError: The letter to count must not be empty.
        """
        with self.assertRaises(ValueError):
            count_string("hello", "")

    # Large Input Cases
    def test_large_input(self):
        """
        Large Input Case: Test the function with a large input sentence.

        Example:
        >>> count_string("a" * 10000, "a")
        'The letter 'a' appears 10000 times'
        """
        self.assertEqual(
            count_string("a" * 10000, "a"), "The letter 'a' appears 10000 times"
        )


if __name__ == "__main__":
    unittest.main()
