from google.cloud import datastore

client = datastore.Client()
query = client.query(kind='Task')
query.add_filter('done', '=', False)
query.add_filter('priority', '=', 4)

results = list(query.fetch())
print(results)
