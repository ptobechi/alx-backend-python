#!/usr/bin/env python3

"""
This module is a Parameterize a unit test for the access_nested_map function.
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
            path (tuple): The path of keys to access within the nested dict.
            expected: The expected result of accessing the
            nested dictionary with the given path.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), KeyError("Key 'a' not found in nested_map")),
        ({"a": 1}, ("a", "b"), KeyError("Key 'b' not found in {'a': 1}")),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """
        Test access_nested_map function raises KeyError for specific inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path of keys to access within the nested dict.
            expected_exception: Expected exception object or its type and msg.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), str(expected_exception))

if __name__ == '__main__':
    unittest.main()
