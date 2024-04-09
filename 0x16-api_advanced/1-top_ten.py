#!/usr/bin/python3
"""Using Reddit API"""
from requests import get


def top_ten(subreddit):
    """prints the titles of the first 10 hot posts"""
    res = get(f"http://www.reddit.com/r/{subreddit}/hot.json",
              headers={"User-Agent": "app"}, params={"limit": 10})
    if res.status_code == 200:
        for post in res.json()["data"]["children"]:
            print(post["data"]["title"])
    else:
        print(None)
