#!/usr/bin/python3
"""Script to retrieve the number of subscribers for a Reddit subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Return the total number of subscribers for a given subreddit."""
    # Reddit API endpoint for subreddit information
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    
    # Set the user-agent header for the request
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the subreddit exists (HTTP 404 status code)
    if response.status_code == 404:
        return 0
    
    # Extract the subscriber count from the JSON response
    results = response.json().get("data")
    return results.get("subscribers")
