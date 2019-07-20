from google.cloud import datastore

client = datastore.Client()
query = client.query(kind='Task')
query.order = ['-priority']

results = list(query.fetch())
print(results)
