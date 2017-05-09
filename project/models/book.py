from google.cloud import datastore

import uuid

def add_book(location, username, comment):
    datastore_client = datastore.Client()

    kind = 'Reservations'
    task_key = datastore_client.key(kind, str(uuid.uuid4()))
    task = datastore.Entity(key=task_key)
    task["username"] = username
    task["location"] = location
    task["comment"] = comment
    task["status"] = "pending"
    datastore_client.put(task)