#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the length of a string.

Module contents:
    - string_length: A function that calculates the length of given string.

Created on 06 January 2025
@author: Safiya Hash

"""


def string_length(string: str) -> int:
    """
    The function calculates the length of a given string.

    Parameters:
        String (str): The string whose length is to be calculated.

    Returns:
        int: The length of the string as an integer.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> string_length("Hey")
        3
        >>> string_length("Second challenge!")
        17
        >>> string_length("#(!)@") # special characters are counted as strings
        5
        >>> string_length("") # empty string
        0
        >>> string_length("Documenting,testing and debugging")
        33
        >>> string_length("    ") # spaces are counted as strings
        4
    """

    if not isinstance(string, str):
        raise TypeError("The input must be a string.")

    return len(string)
