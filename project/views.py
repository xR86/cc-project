from django.shortcuts import render
from django.http import HttpResponse

global_vars = {
	"app_name": "cc-project"
}

def index(request):
    # return HttpResponse("Hello, world.")
    return render(request, 'index.html', global_vars)