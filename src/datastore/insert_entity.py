from google.cloud import datastore

client = datastore.Client()
kind = 'Task'

with client.transaction():

    key = client.key(kind, 1)
    task = datastore.Entity(key)
    task.update({
        'category': 'Personal',
        'done': False,
        'priority': 4,
        'description': 'Learn Cloud Datastore'
    })

    client.put(task)
