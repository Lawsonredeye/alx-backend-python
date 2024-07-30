#!/usr/bin/env python3
"""In a new test_client.py file, declare the
TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.
"""
import unittest
from client import GithubOrgClient
from unittest.mock import (patch, PropertyMock)
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

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
    ])
    def test_public_repos_url(self, input, output):
        """Mock the repo url of an api response call from git based on input"""

        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_repo:
            mock_repo.return_value = output
            client = GithubOrgClient(input)
            self.assertEqual(client.org, output)
            self.assertEqual(client._public_repos_url, output['repos_url'])

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """Testing both patch decorator and context manager"""
        mock_json.return_value = ["YOLO", "of", "repos"]

        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_client:
            mock_client.return_value = ["YOLO", "CONTEXT", "MANAGER"]
            mock_client()
            self.assertEqual(mock_json(), ["YOLO", "of", "repos"])

            mock_client.assert_called_once()

        mock_json.assert_called_once()
    
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, KeyError),
        ({"license": {"key": "other_license"}}, KeyError),
    ])
    def test_has_license(self):
        """Mocks the output if it has a license"""
        with self.assertRaises(KeyError) as err:
            client = GithubOrgClient


if __name__ == "__main__":
    unittest.main()
