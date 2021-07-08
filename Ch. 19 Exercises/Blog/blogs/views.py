import blogs
from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """Home page listing the blogs in chronological order."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)

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

def edit_post(request, blog_id):
    """Edit a blog post."""
    post = BlogPost.objects.get(id=blog_id)

    if request.method != 'POST':
        # Pre-fill with what is saved in the database
        form = BlogForm(instance=post)
    else:
        # Data submitted, validate
        form = BlogForm(instance= post, data= request.POST)
        if form.is_valid():
            form.save()
            redirect('blogs:index')

    # Show a new edit entry form, or an invalidated form
    context = {'post': post, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
