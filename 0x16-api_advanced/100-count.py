#!/usr/bin/python3
"""
Script that queries the Reddit API and counts the occurrence of keywords
in the titles of all hot articles for a given subreddit.
"""

import requests
from collections import Counter


def count_words(subreddit, word_list, after=None, word_count=None):
    """Recursively count words in hot article titles on a given subreddit."""
    if word_count is None:
        word_count = Counter()

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0 (compatible; MyRedditBot/0.1)"}
    params = {"limit": 100, "after": after}
    response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    try:
        data = response.json().get('data', {})
        children = data.get('children', [])

        for child in children:
            title = child['data']['title'].lower()
            for word in word_list:
                word_count[word.lower()] += title.split().count(word.lower())

        after = data.get('after')
        if after:
            return count_words(subreddit, word_list, after, word_count)
        else:
            print_sorted_counts(word_count)
    except (ValueError, KeyError):
        return


def print_sorted_counts(word_count):
    """Print the sorted word count dictionary."""
    sorted_counts = sorted(
            word_count.items(), key=lambda item: (-item[1], item[0]))
    for word, count in sorted_counts:
        if count > 0:
            print(f"{word}: {count}")
