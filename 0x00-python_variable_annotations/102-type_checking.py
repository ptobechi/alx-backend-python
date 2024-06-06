#!/usr/bin/env python3
"""
This module provides a function to zoom into an array by a given factor.
"""


from typing import List, Tuple, Union


def zoom_array(lst: Tuple[Union[int, float], ...], factor: int = 2) -> List[Union[int, float]]:
    """
    Returns a list where each element in the tuple is repeated `factor` times.

    :param lst: A tuple of integers or floats.
    :param factor: The factor by which to zoom into the array (default is 2).
    :return: A list with elements repeated according to the factor.
    """
    zoomed_in: List[Union[int, float]] = [
            item for item in lst
            for i in range(factor)
            ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
