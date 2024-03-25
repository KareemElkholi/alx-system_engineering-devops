#!/usr/bin/python3
"""returns information about todo list progress"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    url = "https://jsonplaceholder.typicode.com/users"
    res = get(f"{url}/{argv[1]}").json()
    name = res["name"]
    res = get(f"{url}/{argv[1]}/todos").json()
    completed = [task for task in res if task["completed"] is True]
    print(f"Employee {name} is done with tasks({len(completed)}/{len(res)}):")
    for task in completed:
        print(f"\t {task['title']}")
