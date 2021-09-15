#!/usr/bin/python3
"""
    A python script that, using a REST API,
    returns information about all employeer TODO
    list progress and exports it in CSV format in
    json file.
"""


import json
import requests
from sys import argv


if __name__ == "__main__":
    emps = requests.get("https://jsonplaceholder.typicode.com/users").json()

    employees = {}
    for emp in emps:
        empId = emp['id']
        employees.update({empId: []})
        task_url = "https://jsonplaceholder.typicode.com/users/{}/todos".\
                   format(empId)
        tasks = requests.get(task_url).json()

        for task in tasks:
            employees[empId].append({'username': emp['username'],
                                     'task': task['title'],
                                     'completed': task['completed']})

    with open('todo_all_employees.json', 'w') as f:
        json.dump(employees, f)
