from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'demoapp/home.html')


def index(request):
    return HttpResponse(
        "Hello, world. This is the index view of DemoApp.")
