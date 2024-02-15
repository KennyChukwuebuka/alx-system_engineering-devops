#!/usr/bin/python3
"""Write a function that queries the Reddit API
and prints the titles of the first 10 hot posts
listed for a given subreddit.

Requirements:

Prototype: def top_ten(subreddit)
If not a valid subreddit, print None.
"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API
    and prints the titles of the first 10 hot posts
    listed for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            print(post['data']['title'])
    else:
        print(None)


if __name__ == '__main__':
    import sys
    top_ten(sys.argv[1])
