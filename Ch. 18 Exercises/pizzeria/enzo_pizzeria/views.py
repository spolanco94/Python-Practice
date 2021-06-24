from django.shortcuts import render

def index(request):
    """Display home page for Enzo's Pizzeria."""
    return render(request, 'enzo_pizzeria/index.html')