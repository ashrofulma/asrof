from django.urls import path

from . import views

ulpatterns = [
    path('', views.index),
]
