from django.shortcuts import render

# Create your views here.
def index(request):
    """renders homepage"""
    return render(request, 'pizza/index.html')