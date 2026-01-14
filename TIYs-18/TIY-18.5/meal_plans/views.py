from django.shortcuts import render

# Create your views here.
def index(request):
    """render homepage"""
    return render(request, 'meal_plans/index.html')