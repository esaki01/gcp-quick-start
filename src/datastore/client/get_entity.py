from google.cloud import datastore

client = datastore.Client()
kind = 'Task'

key = client.key('Task', 1)
task = client.get(key)
# tasks = client.get_multi(keys)

print(f'Kindの取得: {task.kind}')
print(f'Keyの取得：{task.key.id_or_name}')  # Keyが整数値の場合はid, Keyが文字列の場合はnameでも良い
print(f'Propertyの取得: {task["category"]}')
