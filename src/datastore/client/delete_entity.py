from google.cloud import datastore

client = datastore.Client()
kind = 'Task'

key = client.key('Task', 1)
client.delete(key)
# client.delete_multi(keys)
