#!/usr/bin/env python3
"""
This module provides a function that converts a string and a number to a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string `k` and the second element
    is the square of the number `v` as a float.

    :param k: The input string.
    :param v: The input number (int or float).
    :return: A tuple (k, v^2) with the second element as a float.
    """
    return (k, float(v ** 2))
