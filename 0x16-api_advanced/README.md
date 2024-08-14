# API ADVANCED README

# Reddit API Subscriber Count

## Project Description

This project contains a Python script that queries the Reddit API to return the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function returns 0.

## Requirements

- Python 3
- `requests` library

## Files

- `0-subs.py`: Contains the function `number_of_subscribers` which interacts with the Reddit API.
- `0-main.py`: A script to test the `number_of_subscribers` function.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/reddit_api_project.git
    cd reddit_api_project
    ```

2. **Install the required dependencies:**

    ```bash
    pip install requests
    ```

## Usage

To use the `number_of_subscribers` function, you can run the `0-main.py` script with a subreddit name as an argument:

```bash
python3 0-main.py programming

