#!/usr/bin/python3
"""exports information about todo list progress to JSON"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    from json import dump
    url = "https://jsonplaceholder.typicode.com/users"
    res = get(f"{url}/{argv[1]}").json()
    username = res["username"]
    res = get(f"{url}/{argv[1]}/todos").json()
    with open(f"{argv[1]}.json", "w") as file:
        dump({argv[1]: [{"task": task["title"], "completed": task["completed"],
                        "username": username} for task in res]}, file)
