#!/usr/bin/python3
"""Using Reddit API"""
from requests import get


def number_of_subscribers(subreddit):
    """returns the number of subscribers"""
    res = get(f"http://www.reddit.com/r/{subreddit}/about.json",
              headers={"User-Agent": "app"})
    return res.json()["data"]["subscribers"] if res.status_code == 200 else 0
