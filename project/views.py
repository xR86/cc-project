from django.shortcuts import render
from django.http import HttpResponse

from models import login as _login
from models import register as _register

import datetime

global_vars = {
    "app_name": "cc-project"
}

def index(request):
    return render(request, 'index.html', global_vars)

def get_register_page(request):
    return render(request, 'register.html', global_vars)

def get_login_page(request):
    return render(request, 'login.html', global_vars)

def test(request):
    value = request.COOKIES['username']
    print value
    return render(request, 'index.html', global_vars)

   
def register(request):
    username = request.POST["username"]
    passwd = request.POST["password"]
    vpasswd = request.POST["verify_password"]
    status = request.POST["status"]
    
    if passwd == vpasswd and not _register.username_exists(username):
        _register.create_user(username, passwd, status)
    else:
        return render(request, 'error.html', global_vars)
        
    if status == "client":
        return render(request, 'client.html', global_vars)
    elif status == "provider":
        return render(request, 'provider.html', global_vars)
    else:
        return render(request, 'error.html', global_vars)

def login(request):
    username = request.POST["username"]
    passwd = request.POST["password"]
    print "#######################################"
    user = _login.get_user(username, passwd)
    if user:
        if user["status"] == "client":
            response = render(request, 'client.html', global_vars)
        else:
            response = render(request, 'provider.html', global_vars)
        max_age = 365 * 24 * 60 * 60  #one year
        expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), "%a, %d-%b-%Y %H:%M:%S GMT")
        response.set_cookie('username', username)#, max_age=max_age, expires=expires)
        print username
        return response
    else:
        return render(request, 'error.html', {"name": "caca"})
