from google.cloud import datastore

def add_location(username, data):
    location_name = data["location_name"]
    location_type = data["location_type"]
    location_address = data["location_address"]

    datastore_client = datastore.Client()

    kind = 'Location'
    task_key = datastore_client.key(kind, location_name)
    task = datastore.Entity(key=task_key)
    task["username"] = username
    task["location_type"] = location_type
    task["location_address"] = location_address
    datastore_client.put(task)

def get_locations():
    
    datastore_client = datastore.Client()

    kind = 'Location'
    query = datastore_client.query(kind=kind)

    locations = list(query.fetch())
    d = {}
    for l in locations:
        d[l.key.name] = { "address": l["location_address"], "type": l["location_type"]}
    return d
