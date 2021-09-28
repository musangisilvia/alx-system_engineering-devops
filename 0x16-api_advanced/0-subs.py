#!/usr/bin/python3
"""
    This module contains a function that queries the
    Reddit API and returns the number of subscribers
    for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
        Returns number of subscribers
        or 0
    """
    u_agent = {'User-Agent': '/u/Suspicious-Jelly920'}
    url = 'https://api.reddit.com/r/{}/about/'.format(subreddit)
    res = requests.get(url,  headers=u_agent)
    if res.status_code == 200:
        subs = res.json()["data"]["subscribers"]
    else:
        subs = 0
    return subs
