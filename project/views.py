from django.shortcuts import render
from django.http import HttpResponse

global_vars = {
    "app_name": "cc-project"
}

def insert_db():
    from google.cloud import datastore

    # Instantiates a client
    datastore_client = datastore.Client()

    # The kind for the new entity
    kind = 'Task'
    # The name/ID for the new entity
    name = 'sampletask3'
    # The Cloud Datastore key for the new entity
    task_key = datastore_client.key(kind, name)

    # Prepares the new entity
    task = datastore.Entity(key=task_key)
    task['description'] = 'Buy'

    # Saves the entity
    datastore_client.put(task)

    #print('Saved {}: {}'.format(task.key.name, task['description']))
    # [END datastore_quickstart]

    # query = datastore_client.query(kind='Task')
    # print dir(list(query.fetch())[0])
    # print "------------------------------"
    # print vars(list(query.fetch())[0])
    # print "------------------------------"
    # print dir(list(query.fetch())[0].key)
    # print "------------------------------"
    # print list(query.fetch())[0].key.name

# def username_exists():



def index(request):
    # return HttpResponse("Hello, world.")
    #insert_db()
    return render(request, 'index.html', global_vars)

def get_register_page(request):
    return render(request, 'register.html', global_vars)

def register(request):
    
    username = request.POST["username"]
    passwd = request.POST["password"]
    vpasswd = request.POST["verify_password"]
    status = request.POST["status"]
    
    # if passwd == vpasswd and not username_exists(username):
    #     create_user(username, passwd, status)
        
    if status == "client":
        return render(request, 'client.html', global_vars)
    elif status == "provider":
        return render(request, 'provider.html', global_vars)