#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    Return the total number of subscribers on a given subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        return 0
    
    try:
        data = response.json().get("data", {})
        num_subs = data.get("subscribers", 0)
    except (ValueError, TypeError):
        return 0
    
    return num_subs
