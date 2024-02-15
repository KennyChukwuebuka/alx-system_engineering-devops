#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers
"""


def number_of_subscribers(subreddit):
    """Returns the number of subscribers"""
    import requests
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("data").get("subscribers")
    else:
        return 0
