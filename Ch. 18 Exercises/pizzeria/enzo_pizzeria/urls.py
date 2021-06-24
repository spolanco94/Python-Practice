"""Define URL pattern for enzo_pizzeria."""

from django.urls import path

from . import views

app_name = "enzo_pizzeria"
urlpatterns = [
    path('', views.index, name="index"),
]