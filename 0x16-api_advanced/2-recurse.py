#!/usr/bin/python3
"""Write a recursive function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[]):
    """function that queries the Reddit API
    and returns a list containing the titles of
    all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        if data['data']['after']:
            return recurse(subreddit, hot_list)
        else:
            return hot_list
    else:
        return None
