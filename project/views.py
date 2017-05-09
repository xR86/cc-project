from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from models import login as _login
from models import register as _register
from models import locations as _locations
from models import book as _book
from models import mail as _mail

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
    status = request.GET['status']
    _locations.confirm_reservation(key, status)
    return JsonResponse({"response": "yes"})


def register(request):
    username = request.POST["username"]
    passwd = request.POST["password"]
    vpasswd = request.POST["verify_password"]
    status = request.POST["status"]
    
    if passwd != vpasswd:
        return render(request, 'register.html', {"message": "Password and password validate are not the same."})
    elif _register.username_exists(username):
        return render(request, 'register.html', {"message": "Username already exists."})
    elif not _register.valid_username(username):
        return render(request, 'register.html', {"message": "Invalid username. An e-mail is required."})
    else:
        _register.create_user(username, passwd, status)
        
    if status == "client":
        response = render(request, 'client.html')
    else:
        response = render(request, 'provider.html')
    _mail.send_register_mail(username)
    response.set_cookie('username', username)
    return response

def get_client_bookings(request):
    username =  request.COOKIES['username']
    bookings = _book.get_bookings(username)
    return JsonResponse(bookings)


def login(request):
    username = request.POST["username"]
    passwd = request.POST["password"]
    user = _login.get_user(username, passwd)
    if user:
        if user["status"] == "client":
            response = render(request, 'client.html', {"message": ""})
        else:
            response = render(request, 'provider.html', {"message": ""})
        response.set_cookie('username', username)
        return response
    else:
        return render(request, 'login.html', {"message": "Invalid log in data"})


def reserve_location(request):
    location = request.GET['name']
    if request.GET['comment'] == '':
        comment = "No comment provided by user"
    else:
        comment = request.GET['comment']
    username = request.COOKIES['username']
    _book.add_book(location, username, comment)
    return JsonResponse({"success": "yes"})