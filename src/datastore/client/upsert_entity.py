from google.cloud import datastore

client = datastore.Client()
kind = 'Task'

key = client.key(kind)
# key = client.key(kind, 1)
task = datastore.Entity(key)
task.update({
    'category': 'Personal',
    'done': False,
    'priority': 4,
    'description': 'Learn Cloud Datastore'
})

client.put(task)
# client.put_multi([task1, task2])
