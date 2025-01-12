#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the number of vowels in a given string.

Created on 29 Dec 2024
@author: Daniel Oluwaluyi
"""


def count_vowels(input_string: str) -> int:
    """
    Count the number of vowels in the provided string.

    This function takes a string as input and counts the occurrences
    of vowels (a, e, i, o, u), including both lowercase and uppercase letters.

    Args:
        input_string (str): The input string to process.

    Returns:
        int: The count of vowels in the input string.

    Raises:
        AssertionError: If the input is not a string.

    Doctests:
        >>> count_vowels("hello")
        2
        >>> count_vowels("HELLO")
        2
        >>> count_vowels("12345!@#$%^&*()")
        0
        >>> count_vowels("aeiouAEIOU")
        10
        >>> count_vowels("")
        0
    """
    # Defensive assertion to ensure the input is a string
    assert isinstance(input_string, str), "Input must be a string"

    # Define a set of vowels for quick lookup
    vowels = set("aeiouAEIOU")

    # Count and return the number of vowels in the string
    return sum(1 for char in input_string if char in vowels)
