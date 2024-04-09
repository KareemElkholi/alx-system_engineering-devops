#!/usr/bin/python3
"""Using Reddit API"""
from requests import get


def recurse(subreddit, hot_list=[], after=""):
    """returns a list containing the titles of all hot posts"""
    res = get(f"http://www.reddit.com/r/{subreddit}/hot.json?after={after}",
              headers={"User-Agent": "app"})
    if res.status_code == 200:
        for post in res.json()["data"]["children"]:
            hot_list.append(post["data"]["title"])
        if res.json()["data"]["after"]:
            recurse(subreddit, hot_list, after=res.json()["data"]["after"])
        return hot_list
    else:
        return None
