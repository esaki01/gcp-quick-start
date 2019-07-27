from google.cloud import datastore

client = datastore.Client()
kind = 'Task'

with client.transaction():

    key = client.key(kind)
    task = datastore.Entity(key, exclude_from_indexes=['description'])
    task.update({
        'category': 'Personal',
        'done': False,
        'priority': 4,
        'description': 'Learn Cloud Datastore'
    })

    client.put(task)
