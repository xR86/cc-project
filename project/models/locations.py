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

def get_locations_client():
    
    datastore_client = datastore.Client()

    kind = 'Location'
    query = datastore_client.query(kind=kind)

    locations = list(query.fetch())
    d = {}
    for l in locations:
        d[l.key.name] = { "address": l["location_address"], "type": l["location_type"]}
    return d


def get_locations_provider(username):
    
    datastore_client = datastore.Client()

    kind = 'Location'
    query = datastore_client.query(kind=kind)

    locations = list(query.fetch())
    d = {}
    for l in locations:
        if l["username"] == username:
            d[l.key.name] = { "address": l["location_address"], "type": l["location_type"]}
    return d

def confirm_reservation(key):
    datastore_client = datastore.Client()

    kind = 'Reservations'
    with datastore_client.transaction():
        key = datastore_client.key(kind, key)
        task = datastore_client.get(key)

        if not task:
            raise ValueError(
                'Task does not exist.')

        task['status'] = 'approved'

        datastore_client.put(task)


def get_reservations(location):
    datastore_client = datastore.Client()

    kind = 'Reservations'
    query = datastore_client.query(kind=kind)

    reservations = list(query.fetch())
    d = {}
    for r in reservations: 
    # IF AICI       
        d[r.key.name] = { 
                "comment": r["comment"],
                "location": r["location"],
                "status": r["status"],
                "username": r["username"]}
    return d

