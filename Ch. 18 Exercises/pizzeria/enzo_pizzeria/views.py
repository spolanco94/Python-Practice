from django.shortcuts import render

from .models import Pizza

def index(request):
    """Display home page for Enzo's Pizzeria."""
    return render(request, 'enzo_pizzeria/index.html')

def pizzas(request):
    """Display page listing pizzas."""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas' : pizzas }
    return render(request, 'enzo_pizzeria/pizzas.html', context)

def pizza(request, pizza_name):
    """Display's details about the toppings of a specific pizza."""
    pizza = Pizza.objects.get(pizza_name)
    toppings = pizzas.topping_set.order_by('name')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'enzo_pizzeria/pizza.html', context)