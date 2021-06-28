"""Define URL pattern for enzo_pizzeria."""

from django.urls import path

from . import views

app_name = "enzo_pizzeria"
urlpatterns = [
    # Home page
    path('', views.index, name="index"),
    # Pizza's page
    path('pizzas/', views.pizzas, name="pizzas"),
    # Pizza detail page
    path('pizzas/<str:pizza_name>/', views.pizza, name="pizza")
]