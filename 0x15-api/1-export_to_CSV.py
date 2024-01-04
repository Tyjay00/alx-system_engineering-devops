#!/usr/bin/python3
"""
A script that utilizes a REST API to retrieve and export information
about a given employee's TODO list progress in CSV format.
"""

import csv
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

    # Calculate the total number of completed tasks
    totalTasks = 0
    for done_tasks in json_req:
        if done_tasks['completed']:
            totalTasks += 1

    # Create a CSV file with employee data
    fileCSV = idEmp + '.csv'
    with open(fileCSV, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for i in json_req:
            writer.writerow([idEmp, usr, i.get('completed'), i.get('title')])
