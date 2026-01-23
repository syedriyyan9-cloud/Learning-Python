from django.shortcuts import render, redirect

from .models import Topics

from .forms import TopicForm, EntryForm
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

def new_topic(request):
    """adds new topics"""
    if request.method != 'POST': # no data submitted, create new form
        form = TopicForm()
    else:   # data submitted, process data
        form = TopicForm(data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    # display a blank or invalid form
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html',context)

def new_entry(request, topic_id):
    """add new entires"""
    topic = Topics.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id = topic_id)
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)