#!/usr/bin/python3
"""
Script that queries Reddit API and returns a list containing the titles
of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Return list of the titles of all hot articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/0.1)"}
    params = {"after": after, "limit": 100}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get('data')
        if not data:
            return None

        posts = data.get('children', [])
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data.get('after')
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except (ValueError, KeyError):
        return None
