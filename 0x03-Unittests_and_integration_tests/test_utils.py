#!/usr/bin/env python3
"""Test cases for utils.py module which compromises of integration and
unittest
"""

from unittest.mock import patch
from utils import access_nested_map
from utils import get_json
from utils import memoize
from parameterized import parameterized
import unittest


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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nest_map, path):
        """Testing for invalid parameters that doesnt match the key or value"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(nest_map, path)

        self.assertEqual(err.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    """Mocking HTTP calls from a mocked API"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("requests.get")
    def test_get_json(self, test_url, test_payload, mock_request):
        """Mocking the requests library to see the if when another
        instance of the object being called would use the actual Fetching
        or from a mocked data"""
        test_payload = {"payload": True}

        # chained the requests.get(url).json() return value
        mock_request.return_value.json.return_value = test_payload
        mock_request(test_url)
        mock_request.assert_called_once_with(test_url)

        self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """Testing the memoising decorator and see its output"""
    def test_memoize(self):
        """test method for the memoizing function"""
        class TestClass:
            """Test case for a_method and a_property"""
            def a_method(self):
                """Test case for a_method"""
                return 42

            @memoize
            def a_property(self):
                """Test case for a_property"""
                return self.a_method()

        test_instance = TestClass()
        with patch.object(TestClass,
                          'a_method', return_value=42) as mock_method:
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
