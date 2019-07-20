from google.cloud import datastore

client = datastore.Client()
query = client.query(kind='Task')
first_key = client.key('Management', 'managementA', 'Task', 'taskA')
query.key_filter(first_key, '=')

results = list(query.fetch())
print(results)
