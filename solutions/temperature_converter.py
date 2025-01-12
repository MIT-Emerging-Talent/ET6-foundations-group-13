#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for converting temperatures from Celsius to Fahrenheit.

Created on 02 Jan 2025
@author: Daniel Oluwaluyi
"""

from typing import Union


def temperature_converter(celsius: Union[int, float]) -> float:
    """
    Convert a temperature from Celsius to Fahrenheit.

    The formula used is:
        Fahrenheit = (Celsius * 9/5) + 32

    Args:
        celsius (int or float): The temperature in Celsius to be converted.

    Returns:
        float: The equivalent temperature in Fahrenheit.

    Raises:
        AssertionError: If the input is not an integer or float.

    Doctests:
        >>> celsius_to_fahrenheit(0)
        32.0
        >>> celsius_to_fahrenheit(100)
        212.0
        >>> celsius_to_fahrenheit(-40)
        -40.0
        >>> celsius_to_fahrenheit(37)
        98.6
        >>> celsius_to_fahrenheit(15.5)
        59.9
    """
    # Defensive assertion to ensure the input is numeric
    assert isinstance(celsius, (int, float)), "Input must be an integer or a float"

    # Convert Celsius to Fahrenheit using the formula
    return round((celsius * 9 / 5) + 32, 2)
