#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/0.1)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Debug prints to check the status code and response content
    print(f"Status Code: {response.status_code}")
    print(f"Response Content: {response.content}")

    if response.status_code == 200:
        try:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        except (ValueError, KeyError) as e:
            print(f"Error parsing JSON: {e}")
            return 0
    else:
        return 0
