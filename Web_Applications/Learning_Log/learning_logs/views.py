from django.shortcuts import render

from .models import Topics

# Create your views here.
def index(request):
    """renders Home page"""
    return render(request,'learning_logs/index.html')

def topics(request):
    """Displays topics to topic.html template"""
    topics = Topics.objects.order_by('date')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """show a single topic and all its entries"""
    topic = Topics.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)