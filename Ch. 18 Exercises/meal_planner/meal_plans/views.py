from django.http import request
from django.shortcuts import render

def index(request):
    """Display home page for Meal Plans."""
    return render(request, 'meal_plans/index.html')