from django.shortcuts import render, redirect

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display a blank form
        form = UserCreationForm()
    else:
        # Validate submitted form
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            # Save new user information
            new_user = form.save()
            # Log in and redirect to home
            login(request, new_user)
            return redirect('learning_logs:index')
    
    context = {'form': form}
    return redirect(request, 'learning_logs/register.html', context)
