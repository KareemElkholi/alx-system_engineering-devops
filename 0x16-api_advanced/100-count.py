#!/usr/bin/python3
"""Using Reddit API"""
from requests import get


def count_words(subreddit, word_list, after=""):
    """returns a list containing the titles of all hot posts"""
    if type(word_list) is list:
        word_list = {word.lower(): 0 for word in word_list}
        count_words(subreddit, word_list)
    else:
        res = get(f"http://reddit.com/r/{subreddit}/hot.json?after={after}",
                  headers={"User-Agent": "app"})
        if res.status_code != 200:
            return None
        try:
            after = res.json()["data"]["after"]
            posts = res.json()["data"]["children"]
            for post in posts:
                title = post["data"]["title"].lower().split()
                for word in word_list:
                    word_list[word] += title.count(word)
            if after:
                count_words(subreddit, word_list, after=after)
            else:
                sorted_dict = dict(sorted(word_list.items(),
                                          key=lambda x: x[1], reverse=True))
                for key, value in sorted_dict.items():
                    print(f"{key}: {value}")
        except Exception:
            return None
