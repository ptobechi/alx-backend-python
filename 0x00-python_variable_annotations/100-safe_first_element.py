#!/usr/bin/env python3
"""
This module provides a function that safely returns the first element of a sequence.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a sequence if it exists, otherwise returns None.

    :param lst: A sequence of any type.
    :return: The first element of the sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
