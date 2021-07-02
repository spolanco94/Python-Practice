"""Defines URL patterns for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that displays topics
    path('topics/', views.topics, name='topics'),
    # Detail page for specific topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Form page for creating a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Form page to creating a new entry for a specific topic
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # Form page for editing an existing entry
    path('new_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]