#!/usr/bin/python3
"""
    This module contains a function that queries the
    Reddit API and returns a list of the hottest post for
    a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        returns a list of the hottest posts of a subreddit
        or None
    """
    u_agent = {'User-Agent': '/u/Suspicious-Jelly920'}
    url = 'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after)
    res = requests.get(url,  headers=u_agent)
    h_list = []
    if res.status_code == 200:
        hottest = res.json()["data"]["children"]
        after = res.json()["data"]["after"]

        if after is None:
            h_list = get_children(hottest, len(hottest))
            return h_list
        h_list.append(recurse(subreddit, h_list, after=after))
        h_list = get_children(hottest, len(hottest))
    else:
        return None
    return h_list


def get_children(h_list, count, new_hlist=[]):
    """
        gets the children from the data
    """
    if count == 0:
        return new_hlist
    new_hlist.append(h_list[count - 1]["data"]["title"])
    return (get_children(h_list, count - 1, new_hlist))
