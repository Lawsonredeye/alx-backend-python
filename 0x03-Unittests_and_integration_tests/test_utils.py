#!/usr/bin/env python3
"""Test cases for utils.py module which compromises of integration and
unittest
"""

from utils import access_nested_map
import unittest
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Testing the nested_map function and its return values"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), ({"b": 2})),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, input, expected, output):
        """check if the output is correct"""
        self.assertEqual(access_nested_map(input, expected), output)


if __name__ == "__main__":
    unittest.main()
