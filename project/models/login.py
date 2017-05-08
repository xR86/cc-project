from google.cloud import datastore

def get_user(username, passwd):
    datastore_client = datastore.Client()

    kind = 'Users'
    task_key = datastore_client.key(kind, username)

    q = datastore_client.get(task_key)
    if q["password"] == passwd:
        return q
    else:
        return None