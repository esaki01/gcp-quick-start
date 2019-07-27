from google.cloud import datastore

client = datastore.Client()
kind = 'Task'

key = client.key(kind)
print(client.allocate_ids(key, 3))
