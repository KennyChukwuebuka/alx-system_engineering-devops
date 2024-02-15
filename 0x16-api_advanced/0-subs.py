#!/usr/bin/python3
"""function that queries the Reddit API
and returns the number of subscribers
"""
import requests
import sys
import json


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers
    """
    username = 'kenny123'
    password = 'kenny72'
    user_dict = {'user': username, 'passwd': password, 'api_type': 'json'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
