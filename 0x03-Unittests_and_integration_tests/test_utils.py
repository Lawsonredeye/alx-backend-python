#!/usr/bin/env python3
"""Test cases for utils.py module which compromises of integration and
unittest
"""

from utils import access_nested_map
import unittest
from parameterized import parameterized


nested_val = {"some": {"thing": 1}}
print(access_nested_map(nested_val, nested_val))


class TestAccessNestedMap(unittest.testCase):
    """Testing the nested_map function and its return values"""

    @parameterized.expand(
        nested_map={"a": 1}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a",),
        nested_map={"a": {"b": 2}}, path=("a", "b")
        )
    def test_access_nested_map(self):
        """chc"""
        self.assertEqual()