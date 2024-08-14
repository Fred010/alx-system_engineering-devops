#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Retrieve the number of subscribers for a given subreddit.

    Args:
        subreddit (str): name of the subreddit

    Returns:
        int: number of subscribers for the subreddit. Returns 0 if the
        subreddit is invalid.
    """
    # Reddit API endpoint for fetching subreddit information
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/58.0.3029.110 Safari/537.3"
        )
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0

        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    except Exception:
        return 0
