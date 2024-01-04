#!/usr/bin/python3
"""
A script that utilizes a REST API, for a given employee ID, retrieves
information about their TODO list progress,
and exports data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    # Extract employee ID from command line arguments
    idEmp = argv[1]
    
    # API URLs for TODO list and employee details
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    # Fetch data from the API
    employee = sessionReq.get(idURL)
    employeeName = sessionReq.get(nameURL)

    # Parse JSON responses
    json_req = employee.json()
    usr = employeeName.json()['username']

    # Prepare data for JSON export
    totalTasks = []
    updateUser = {}

    for all_Emp in json_req:
        totalTasks.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    updateUser[idEmp] = totalTasks

    # Export data to a JSON file
    file_Json = idEmp + ".json"
    with open(file_Json, 'w') as f:
        json.dump(updateUser, f)
