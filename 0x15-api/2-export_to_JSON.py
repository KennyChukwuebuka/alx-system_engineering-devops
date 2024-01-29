#!/usr/bin/python3
"""Using what you did in the 0-gather_data_from_an_API.py, extend
your Python script to export data in the JSON format.
Requirements:
    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE",
    "completed": "TASK_COMPLETED_STATUS", "username": "USERNAME"},
    {"task": "TASK_TITLE", "completed": "TASK_COMPLETED_STATUS",
    "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(userId))
    name = user.json().get('username')
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump({userId: [{
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': name
        } for task in todos.json() if task.get('userId') == int(userId)]}, f)
