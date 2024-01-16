#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        if response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
            return 0

        results = response.json().get("data")
        return results.get("subscribers")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: {} <subreddit>".format(sys.argv[0]))
    else:
        subreddit = sys.argv[1]
        subscribers = number_of_subscribers(subreddit)
        print(f"Subreddit '{subreddit}' has {subscribers} subscribers.")
