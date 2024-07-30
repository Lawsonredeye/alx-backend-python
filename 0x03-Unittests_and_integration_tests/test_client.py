#!/usr/bin/env python3
"""In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.
"""
import unittest
from client import GithubOrgClient
from unittest.mock import patch
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """test that GithubOrgClient.org returns the correct value."""

    @parameterized.expand([
        ("google", {"payload": True}), ("abc", {"payload": False}),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, output, mock_get):
        """Mocked the get_json function thats called within the
        client module to be able prevent external calls"""
        mock_get.return_value = output

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, output)
        mock_get.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
            )


if __name__ == "__main__":
    unittest.main()
