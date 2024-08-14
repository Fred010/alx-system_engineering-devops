#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit

    Args:
        subreddit (str): name of the subreddit

    Returns:
        int: number of subs for the subreddit. Returns 0 if the
        subreddit is invalid
    """
    # Reddit API endpoint for fetching subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    # Set custom User-Agent to avoid Too Many Requests error
    headers = {'User-Agent': 'Custom-User-Agent'}

    # Send GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is successful
    if response.status_code == 200:
        # Extract number of subscribers from the response JSON
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Invalid subreddit or other error occurred
        return 0
