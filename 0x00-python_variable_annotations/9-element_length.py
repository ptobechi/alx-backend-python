#!/usr/bin/env python3
"""
This module provides a function that returns the lengths of elements in a list.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, where each tuple contains an element from the input iterable
    and its corresponding length.

    :param lst: An iterable of sequences.
    :return: A list of tuples containing each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
