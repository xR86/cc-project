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

def get_bookings(username):
    datastore_client = datastore.Client()

    kind = 'Reservations'
    query = datastore_client.query(kind=kind)
    query.add_filter("username", "=", username)

    reservations = list(query.fetch())
    d = {}
    for r in reservations: 
        d[str(r.key.name)] = { 
                "comment": r["comment"],
                "location": r["location"],
                "status": r["status"],
                "username": r["username"]}
    return d