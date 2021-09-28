#!/usr/bin/python3
"""
    This module contains a function that queries the
    Reddit API and prints the top 10 hottest post for
    a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
        Prints Top ten hottest posts of a subreddit
        or None
    """
    u_agent = {'User-Agent': '/u/Suspicious-Jelly920'}
    url = 'https://api.reddit.com/r/{}/hot/'.format(subreddit)
    res = requests.get(url,  headers=u_agent)
    if res.status_code == 200:
        hottest_ten = res.json()["data"]["children"]

        count = 0
        for hot in hottest_ten:
            if count == 10:
                break
            print(hot["data"]["title"])
            count += 1
    else:
        print("None")
