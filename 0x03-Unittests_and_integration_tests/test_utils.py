#!/usr/bin/env python3
"""
This module contains unit tests for the utils module.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


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
            expected: The expected result of accessing the nested dictionary
            with the given path.
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a",), "KeyError: 'a'"),
        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
        ])
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """
        Test access_nested_map function raises KeyError for specific inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The path of keys to access within the nested dict.
            expected_message (str): The expected exception message.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)

class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function with mocked requests.get.

        Args:
            test_url (str): The URL to mock in requests.get.
            test_payload (dict): The expected JSON payload to be returned.
            mock_get (Mock): Mock object for requests.get.
        """
        # Mock the return value of requests.get().json()
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call the function under test
        result = get_json(test_url)

        # Assertions
        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)

class TestMemoize(unittest.TestCase):
    """
    Test case for the memoize decorator.
    """

    def test_memoize(self):
        """
        Test the memoize decorator to ensure it caches results.
        """
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)  # First call
            self.assertEqual(test_instance.a_property, 42)  # Second call
            mock_method.assert_called_once()

if __name__ == '__main__':
    unittest.main()
