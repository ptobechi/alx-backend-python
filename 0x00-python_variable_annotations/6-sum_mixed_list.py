#!/usr/bin/env python3
"""
This module provides a function to sum a list of integers and floats.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    :param mxd_lst: List of integers and float numbers to sum.
    :return: The sum of the list as a float.
    """
    return sum(mxd_lst)
