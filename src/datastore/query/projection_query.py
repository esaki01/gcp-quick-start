from google.cloud import datastore

client = datastore.Client()
query = client.query(kind='Task')
query.projection = ['priority']

results = list(query.fetch())
print(results)
