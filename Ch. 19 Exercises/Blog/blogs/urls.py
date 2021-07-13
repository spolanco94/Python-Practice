"""Defines URL patterns for Blogs app"""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Create a new blog post
    path('new_post', views.new_post, name='new_post'),
    # Edit blog posts
    path('edit_post/<int:blog_id>/', views.edit_post, name='edit_post'),
]
