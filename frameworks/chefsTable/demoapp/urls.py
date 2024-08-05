#!/usr/bin/env python3
from django.urls import path
from . import views

app_name = 'demoapp'
urlpatterns = [
    path('dishes/<str:dish>', views.menuitems),  # dish=pasta
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
]
