from django.template import loader
# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template = loader.get_template('demoapp/home.html')
    context = {}
    return HttpResponse(template.render(context, request))


def index(request):
    return HttpResponse(
        "Hello, world. This is the index view of DemoApp.")
