#!/usr/bin/env python3
"""Test cases for utils.py module which compromises of integration and
unittest
"""

from utils import access_nested_map
import unittest


nested_val = {"some": {"thing": 1}}
print(access_nested_map(nested_val, nested_val))


class TestAccessNestedMap(unittest.testCase):
    """Testing the nested_map function and its return values"""

    @parameterized.expand(nested_map={"a": 1}, path=("a",))
    @parameterized.expand(nested_map={"a": 1}, path=("a",))
    def test_access_nested_map(self):
        """chc"""
        self.assertEqual()