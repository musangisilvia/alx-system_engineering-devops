#!/usr/bin/python3
"""
    A python script that, using a REST API, for a given
    employee ID, returns information about his/her TODO
    list progress and exports it in CSV format in
    csv file.
"""


import csv
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

    with open('{}.csv'.format(empId), 'w') as csvfile:
        taskwrite = csv.writer(csvfile, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)
        for tasks in r:
            taskwrite.writerow([empId,
                               empname,
                               tasks['completed'],
                               tasks['title']])
