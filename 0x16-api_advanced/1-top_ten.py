#!/usr/bin/python3
"""Script to display the titles of the top 10 hot posts on a specified Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts for a given subreddit."""
    # Reddit API endpoint for fetching hot posts
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    
    # Set the user-agent header for the request
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    
    # Parameters to limit the number of posts to 10
    params = {
        "limit": 10
    }
    
    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    # Check if the subreddit exists (HTTP 404 status code)
    if response.status_code == 404:
        print("None")
        return
    
    # Extract and print the titles of the top 10 hot posts
    results = response.json().get("data")
    [print(c.get("data").get("title")) for c in results.get("children")]
