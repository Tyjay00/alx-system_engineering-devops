import requests

def number_of_subscribers(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'YourCustomUserAgent'}  # Replace with an appropriate user agent

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)

        data = response.json().get("data")
        subscribers = data.get("subscribers")
        return subscribers
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            print(f"Subreddit '{subreddit}' not found.")
        else:
            print(f"HTTP error: {e}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

    return 0  # Return 0 if there's an error or if the subreddit is not found

# Example usage:
subreddit_name = 'programming'
subscribers_count = number_of_subscribers(subreddit_name)
print(f"The subreddit r/{subreddit_name} has {subscribers_count} subscribers.")
