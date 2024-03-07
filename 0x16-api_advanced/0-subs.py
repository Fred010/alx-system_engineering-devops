import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # If the subreddit is invalid or not found, return 0
        return 0

# Example usage:
subreddit = "AskReddit"
print(f"Number of subscribers in subreddit '{subreddit}': {number_of_subscribers(subreddit)}")

# Example with invalid subreddit:
invalid_subreddit = "nonexistent_subreddit"
print(f"Number of subscribers in subreddit '{invalid_subreddit}': {number_of_subscribers(invalid_subreddit)}")
