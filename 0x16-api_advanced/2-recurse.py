#!/usr/bin/python3
"""Script using Reddit's API to recursively fetch top post titles."""
import requests

# Variable to keep track of the 'after' parameter for pagination
after = None

def recurse(subreddit, hot_list=[]):
    """Return top post titles recursively from a given subreddit."""
    global after
    user_agent = {'User-Agent': 'api_advanced-project'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'after': after}
    
    # Send a GET request to the Reddit API
    results = requests.get(url, params=parameters, headers=user_agent,
                           allow_redirects=False)

    # Check if the request was successful (HTTP 200 status code)
    if results.status_code == 200:
        after_data = results.json().get("data").get("after")
        
        # Update the 'after' variable for pagination
        if after_data is not None:
            after = after_data
            recurse(subreddit, hot_list)
        
        # Extract and append titles from the JSON response
        all_titles = results.json().get("data").get("children")
        for title_ in all_titles:
            hot_list.append(title_.get("data").get("title"))
        
        return hot_list
    else:
        return None
