#!/usr/bin/python3
"""Using what you did in the 0-gather_data_from_an_API.py, extend
your Python script to export data in the JSON format.
Requirements:
    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [ {"username": "USERNAME",
    "task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS}, {"username": "USERNAME",
    "task": "TASK_TITLE", "completed":
    TASK_COMPLETED_STATUS}, ... ], "USER_ID":
    [ {"username": "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, {"username":
    "USERNAME", "task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS}, ... ]}
    File name must be: USER_ID.json
"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    users = requests.get("https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()
    todoAll = {}

    for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todoAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
