from django import forms
from django.db import models

from .models import Topic

class TopicForm(forms.ModelForm):
    """Form for users to create new topics."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}