#!/usr/bin/python3
"""exports information about todo list progress to CSV"""
if __name__ == "__main__":
    from requests import get
    from sys import argv
    from csv import writer, QUOTE_ALL
    url = "https://jsonplaceholder.typicode.com/users"
    res = get(f"{url}/{argv[1]}").json()
    username = res["username"]
    res = get(f"{url}/{argv[1]}/todos").json()
    with open(f"{argv[1]}.csv", "w") as file:
        for task in res:
            writer(file, quoting=QUOTE_ALL).writerow(
                [task["userId"], username, task["completed"], task["title"]])
