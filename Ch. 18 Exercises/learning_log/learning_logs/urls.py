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
]