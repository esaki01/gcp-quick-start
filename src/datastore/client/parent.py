from google.cloud import datastore

client = datastore.Client()
parent_kind = 'Management'
kind = 'Task'

parent_key = client.key(parent_kind, 'managementA')
key = client.key(kind, 'taskA', parent=parent_key)

task = datastore.Entity(key)
task.update({
    'category': 'Personal',
    'done': False,
    'priority': 4,
    'description': 'Learn Cloud Datastore'
})

client.put(task)
