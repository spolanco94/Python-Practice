from django import forms
from django.forms import widgets

from .models import BlogPost

class BlogForm(forms.ModelForm):
    """Form to create new blog posts."""
    class Meta:
        blog = BlogPost
        fields = ['title', 'text']
        labels = {
            'title': 'Title', 
            'text': ''
        }
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}
