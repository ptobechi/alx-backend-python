#!/usr/bin/env python3
"""
This module provides a function to sum a list of floats.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    :param input_list: List of float numbers to sum.
    :return: The sum of the list of floats.
    """
    return sum(input_list)
