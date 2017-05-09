from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from models import login as _login
from models import register as _register
from models import locations as _locations
from models import book as _book

import datetime

global_vars = {
    "app_name": "cc-project",
    "message" : ""
}

def index(request):
    return render(request, 'index.html', global_vars)

def get_register_page(request):
    return render(request, 'register.html', global_vars)

def get_login_page(request):
    return render(request, 'login.html', global_vars)

def add_location(request):
    username = request.COOKIES['username']
    _locations.add_location(username, request.POST)

    return render(request, 'provider.html', global_vars)

def get_locations_client(request):
    locations = _locations.get_locations_client()
    return JsonResponse(locations)

def get_locations_provider(request):
    username = request.COOKIES['username']
    locations = _locations.get_locations_provider(username)
    return JsonResponse(locations)

def get_reservations_provider(request):
    location_name = request.GET['name']
    reservations = _locations.get_reservations(location_name)
    return JsonResponse(reservations)

def confirm_reservations_provider(request):
    key = request.GET['key']
    _locations.confirm_reservation(key)
    return JsonResponse({"response": "yes"})


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
        response = render(request, 'client.html', global_vars)
    elif status == "provider":
        response = render(request, 'provider.html', global_vars)
    else:
        return render(request, 'error.html', global_vars)
    response.set_cookie('username', username)
    return response

def login(request):
    username = request.POST["username"]
    passwd = request.POST["password"]
    user = _login.get_user(username, passwd)
    if user:
        if user["status"] == "client":
            response = render(request, 'client.html', global_vars)
        else:
            response = render(request, 'provider.html', global_vars)
        response.set_cookie('username', username)
        print username
        return response
    else:
        return render(request, 'error.html', {"name": "caca"})


def reserve_location(request):
    location = request.GET['name']
    comment = request.GET['comment']
    username = request.COOKIES['username']
    _book.add_book(location, username, comment)
    return JsonResponse({"success": "yes"})