#!/usr/bin/env python3
"""
This module provides a function to safely get a value from a dictionary.
"""


from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the value from the dictionary for the given key if it exists, otherwise returns the default value.

    :param dct: The dictionary to get the value from.
    :param key: The key to look for in the dictionary.
    :param default: The default value to return if the key is not in the dictionary.
    :return: The value from the dictionary or the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
