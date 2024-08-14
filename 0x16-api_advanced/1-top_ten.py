#!/usr/bin/python3
"""
Script that queries the Reddit API and prints the titles of the first
10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Print titles of first 10 hot posts listed for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/0.1)"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        except (ValueError, KeyError) as e:
            print(None)
    else:
        print(None)
