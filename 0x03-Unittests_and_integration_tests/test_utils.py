#!/usr/bin/env python3

"""
this module is a Parameterize a unit test
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map  # Import your function here


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with various inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path of keys to access within the
            nested dictionary.expected:
            The expected result of accessing the nested dictionary
            with the given path.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
