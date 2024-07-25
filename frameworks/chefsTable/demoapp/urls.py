#!/usr/bin/env python3
from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('', views.index, name='index'),
]
