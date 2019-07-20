from google.cloud import datastore

client = datastore.Client()
ancestor = client.key('Management', 'managementA')
query = client.query(kind='Task', ancestor=ancestor)

results = list(query.fetch())
print(results)
