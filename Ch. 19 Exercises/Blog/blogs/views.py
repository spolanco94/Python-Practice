from django.db import reset_queries
import blogs
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import BlogPost
from .forms import BlogForm

def check_post_owner(request, post):
    """Checks if the requesting user is the post owner"""
    if post.owner != request.user:
        raise Http404

def index(request):
    """Home page listing the blogs in chronological order."""
    return render(request, 'blogs/index.html')

@login_required
def blogs(request):
    """Displays a list of blogposts."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

@login_required
def new_post(request):
    """Create a new blog post."""
    if request.method != 'POST':
        # No form has been submitted, create a new one.
        form = BlogForm()
    else:
        # Data submitted, process and save if valid
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

@login_required
def edit_post(request, blog_id):
    """Edit a blog post."""
    post = BlogPost.objects.get(id=blog_id)
    text = post.text
    title = post.title
    check_post_owner(request, post)

    if request.method != 'POST':
        # Pre-fill with what is saved in the database
        form = BlogForm(instance=post)
    else:
        # Data submitted, validate
        form = BlogForm(instance= post, data= request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')

    # Show a new edit entry form, or an invalidated form
    context = {'title': title, 'text': text, 'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
