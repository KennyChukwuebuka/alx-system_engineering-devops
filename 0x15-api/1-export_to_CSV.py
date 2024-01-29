#!/usr/bin/python3
"""Using what you did in the 0-gather_data_from_an_API.py, extend
your Python script to export data in the CSV format.
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(id)
    response = requests.get(url)
    name = response.json().get('name')

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(id)
    response = requests.get(url)
    tasks = response.json()

    with open("{}.csv".format(id), 'w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in tasks:
            writer.writerow([id, name, task.get('completed'),
                             task.get('title')])
