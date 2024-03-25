#!/usr/bin/python3
"""exports information about todo list progress to JSON"""
from requests import get
from json import dump
res = get("https://jsonplaceholder.typicode.com/users").json()
users = [{"userId": usr["id"], "username": usr["username"]} for usr in res]
res = get("https://jsonplaceholder.typicode.com/todos").json()
with open("todo_all_employees.json", "w") as file:
    dump({usr["userId"]: [{"username": usr["username"], "task": task["title"],
         "completed": task["completed"]} for task in res
          if task["userId"] == usr["userId"]] for usr in users}, file)
