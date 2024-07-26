from django.template import loader
# from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    template = loader.get_template('demoapp/home.html')
    context = {}
    return HttpResponse(template.render(context, request))


def menuitems(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle made from combination of wheat, water or eggs',
        'falafel': 'Falafel are deep fried patties or balls made from',
        'cheescake': 'Cheesecake is a type of dessert made with'
    }

    description = items[dish]

    return HttpResponse(f"<h2>{dish}</h2>"+description)


def index(request):
    return HttpResponse(
        "Hello, world. This is the index view of DemoApp.")
