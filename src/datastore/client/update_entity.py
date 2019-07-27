from google.cloud import datastore

client = datastore.Client()
kind = 'Task'

with client.transaction():
    key = client.key('Task', 1)
    task = client.get(key)

    task['done'] = True

    client.put(task)
