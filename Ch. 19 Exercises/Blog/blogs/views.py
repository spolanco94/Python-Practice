import blogs
from django.shortcuts import render

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """Home page listing the blogs in chronological order."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)
