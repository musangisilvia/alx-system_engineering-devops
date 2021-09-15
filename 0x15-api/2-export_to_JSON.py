#!/usr/bin/python3
"""
    A python script that, using a REST API, for a given
    employee ID, returns information about his/her TODO
    list progress and exports it in CSV format in
    json file.
"""


import json
import requests
from sys import argv

if __name__ == "__main__":
    empId = argv[1]
    empname = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                           .format(empId)).json().get("name")

    tasks = 0  # total number of tasks
    c_tasks = []  # list of completed tas
    r = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                     .format(empId)).json()

    empJSON = {empId: []}

    for tasks in r:
        empJSON[empId].append({'task': tasks['title'],
                               'completed': tasks['completed'],
                               'username': empname})

    with open('{}.json'.format(empId), 'w') as f:
        json.dump(empJSON, f)
