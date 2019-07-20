from google.cloud import datastore

client = datastore.Client()
query = client.query(kind='Task')

results = list(query.fetch(offset=0, limit=5))
print(results)
