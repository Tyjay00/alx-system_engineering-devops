#!/usr/bin/python3
"""
A script that utilizes a REST API to retrieve and display the progress
of a given employee's TODO list.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    json_req = employee.json()
    name = employeeName.json()['name']

    totalTasks = 0

    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
