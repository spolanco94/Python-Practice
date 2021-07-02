from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    """Form for users to create new topics."""
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    """Form for users to add new entries to a topic."""
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}