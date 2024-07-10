#!/usr/bin/env python3
"""
This module contains unit tests for the client module.
"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from utils import get_json


class TestGithubOrgClient(unittest.TestCase):
    """
    Test case for the GithubOrgClient class.
    """

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, expected, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.

        Args:
            org_name (str): The organization name to test.
            expected (dict): The expected JSON response.
            mock_get_json (Mock): Mock object for get_json.
        """
        # Mock the return value of get_json
        mock_get_json.return_value = expected

        # Create an instance of GithubOrgClient with the org_name
        client = GithubOrgClient(org_name)

        # Call the org property
        result = client.org

        # Assertions
        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, expected)

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test the _public_repos_url property of GithubOrgClient.

        Args:
            mock_org (PropertyMock): Mock object for the
            GithubOrgClient.org property.
        """
        # Define the mocked return value
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the _public_repos_url property
        result = client._public_repos_url

        # Assertions
        self.assertEqual(result, "https://api.github.com/orgs/google/repos")

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test the public_repos method of GithubOrgClient.

        Args:
            mock_public_repos_url (PropertyMock): Mock object for the
            GithubOrgClient._public_repos_url property.
            mock_get_json (Mock): Mock object for get_json.
        """
        # Define the mocked payload and repos_url
        mocked_repos_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mocked_repos_url = "https://api.github.com/orgs/google/repos"

        # Mock the return values
        mock_get_json.return_value = mocked_repos_payload
        mock_public_repos_url.return_value = mocked_repos_url

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method
        result = client.public_repos()

        # Assertions
        self.assertEqual(result, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(mocked_repos_url)

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock)
    def test_public_repos_with_license(self, mock_public_repos_url, mock_get_json):
        """
        Test the public_repos method of GithubOrgClient with a license filter.

        Args:
            mock_public_repos_url (PropertyMock): Mock object for the
            GithubOrgClient._public_repos_url property.
            mock_get_json (Mock): Mock object for get_json.
        """
        # Define the mocked payload and repos_url
        mocked_repos_payload = [
                {"name": "repo1", "license": {"key": "apache-2.0"}},
                {"name": "repo2", "license": {"key": "mit"}},
                {"name": "repo3", "license": {"key": "apache-2.0"}}
                ]
        mocked_repos_url = "https://api.github.com/orgs/google/repos"

        # Mock the return values
        mock_get_json.return_value = mocked_repos_payload
        mock_public_repos_url.return_value = mocked_repos_url

        # Create an instance of GithubOrgClient
        client = GithubOrgClient("google")

        # Call the public_repos method with a license filter
        result = client.public_repos(license="apache-2.0")

        # Assertions
        self.assertEqual(result, ["repo1", "repo3"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(mocked_repos_url)


if __name__ == '__main__':
    unittest.main()
