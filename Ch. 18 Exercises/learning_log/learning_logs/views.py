import learning_logs
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http.response import Http404

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def check_topic_owner(request, topic):
    """Checks if the requesting user owns the topic."""
    if topic.owner != request.user:
        raise Http404

def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Display all topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Display a topic and its entries."""
    topic = Topic.objects.get(id=topic_id)
    # Match requesting user against topic owner
    check_topic_owner(request, topic)
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Create a new topic."""
    
    if request.method != 'POST':
        # No data submitted, create a blank form
        form = TopicForm()
    else:
        # POST data submitted, process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('learning_logs:topics')

    # Display a blank or invalid form
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Create a new entry for a topic."""

    topic = Topic.objects.get(id=topic_id)
    check_topic_owner(request, topic)
    
    if request.method != "POST":
        # No data submitted, create a blank form
        form = EntryForm()
    else:
        # Post data submitted, process data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)

    # Display a blank or invalid form
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry for a topic."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    check_topic_owner(request, topic)

    if request.method != "POST":
        # Generate a form pre-filled with the existing entry
        form = EntryForm(instance=entry)
    else:
        # Post data submitted, updating existing entry with any new information
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    # Display a blank or invalid form
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
    