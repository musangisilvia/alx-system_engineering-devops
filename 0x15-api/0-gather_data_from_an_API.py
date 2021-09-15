#!/usr/bin/python3
"""
    A python script that, using a REST API, for a given
    employee ID, returns information about his/her TODO
    list progress.
"""


from sys import argv
import requests


if __name__ == "__main__":
    empId = argv[1]
    empname = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(empId)).json().get("name")

    tasks = 0  # total number of tasks
    c_tasks = []  # list of completed tasks
    r = requests.get("https://jsonplaceholder.typicode.com/todos").json()

    for task in r:
        if task.get("userId") == int(empId):
            tasks += 1
            if task.get("completed"):
                c_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({:d}/{:d}):"
          .format(empname, len(c_tasks), tasks))

    for item in c_tasks:
        print("\t {}".format(item))
