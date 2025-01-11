import unittest

from ..count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    def test_empty_string(self):
        """Test that an empty string returns 0."""
        self.assertEqual(count_vowels(""), 0)

    def test_no_vowels(self):
        """Test a string with no vowels."""
        self.assertEqual(count_vowels("bcdfghjklmnpqrstvwxyz"), 0)

    def test_all_vowels(self):
        """Test a string with all vowels (lowercase and uppercase)."""
        self.assertEqual(count_vowels("aeiouAEIOU"), 10)

    def test_mixed_string(self):
        """Test a string with a mix of vowels and consonants."""
        self.assertEqual(count_vowels("Hello, World!"), 3)

    def test_numeric_and_special_characters(self):
        """Test a string with numbers and special characters."""
        self.assertEqual(count_vowels("12345!@#$%^&*()"), 0)

    def test_vowels_in_words(self):
        """Test a string with words containing vowels."""
        self.assertEqual(count_vowels("Python programming is fun!"), 8)


if __name__ == "__main__":
    unittest.main()
