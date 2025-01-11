#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating the product of the digits of an integer number

Module contents:
    - product_of_digits: calculate the product of the digits of an integer number.

Created on 5 Jan 2024
@author: Noorelsalam Almakki
"""


def product_of_digits(number: int) -> int:
    """The product_of_digits function takes an integer number and returns the product of
    its digits.

    Parameters:
        - number (int): any integer number.

    Returns:
        - product (int): the product of the digits of the input number.

    Raises:
        - AssertionError: if the input number is not an integer.

    Example:
    >>> product_of_digits(123)
    6

    >>> product_of_digits(1234)
    24

    >>> product_of_digits(-123)
    -6
    """
    assert isinstance(number, int), "The input number must be an integer"

    digit_product = 1
    absolute_number = abs(number)

    for digit in str(absolute_number):
        digit_product *= int(digit)

    if number < 0:
        digit_product *= -1

    return digit_product
