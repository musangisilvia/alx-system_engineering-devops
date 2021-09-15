#!/usr/bin/python3
"""
    A python script that, using a REST API, for a given
    employee ID, returns information about his/her TODO
    list progress.
"""


import requests
from sys import argv


if __name__ == "__main__":
    empId = argv[1]
    empname = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(empId)).json().get("name")

    c_tasks = []  # list of completed tasks
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                     .format(empId)).json()
    tasks = len(r)
    for task in r:
            if task["completed"]:
                c_tasks.append(task["title"])

    print("Employee {} is done with tasks({:d}/{:d}):"
          .format(empname, len(c_tasks), tasks))

    for item in c_tasks:
        print("\t {}".format(item))
