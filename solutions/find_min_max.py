#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for generating the min and max of a list of numbers.

Module contents:
    > find_min_max: generates the min and max of a list of numbers.

Created on the 02 Jan 2025
@author: Tosan Okome
"""


def find_min_max(numbers: list[float]) -> tuple[float, float]:
    """Find the minimum and maximum values in a list of numbers.

    Parameters:
    numbers:list[float]: A list of numbers (floats or integers).

    Returns:
        tuple[float, float]: A tuple where:
            - The first element is the smallest number in the list.
            - The second element is the largest number in the list.

    Raises:
        ValueError: If the list is empty.
        ValueError: If the list contains non-numeric elements.

    Example:
        >>> find_min_max([3, 1, 4, 1, 5, 9])
        (1, 9)
        >>> find_min_max([-5, -1, -3])
        (-5, -1)
        >>> find_min_max([9.7, 67.9, 8, 9.2])
        (8, 67.9)
    """
    if not numbers:
        raise ValueError("The list cannot be empty.")

    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements in the list must be numbers.")

    return min(numbers), max(numbers)
