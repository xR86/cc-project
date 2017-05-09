from google.cloud import datastore

def valid_username(username):
    import re
    if re.match("[\w._-]+?@\w+?\.\w+?", username) != None:
        return True
    return False

def create_user(username, passwd, status):
    datastore_client = datastore.Client()
    kind = 'Users'
    task_key = datastore_client.key(kind, username)
    task = datastore.Entity(key=task_key)
    task["password"] = passwd
    task["status"] = status
    datastore_client.put(task)

def username_exists(username):
    datastore_client = datastore.Client()

    kind = 'Users'
    task_key = datastore_client.key(kind, username)

    q = datastore_client.get(task_key)
    return q  