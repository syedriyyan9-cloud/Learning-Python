from django.shortcuts import render

from .models import Pizza

# Create your views here.
def index(request):
    """renders homepage"""
    return render(request, 'pizza/index.html')

def pizza(request):
    """renders pizzas to pizza page"""
    pizzas = Pizza.objects.order_by('name')
    content = {'pizzas':pizzas}
    return render(request, 'pizza/pizza.html',content)

def topping(request, pizza_id):
    """renders toppings based on pizza id that is in topping table as FK"""
    pizza = Pizza.objects.get(id = pizza_id)
    topping = pizza.topping_set.order_by('name')
    content = {"pizza":pizza, 'toppings':topping}
    return render(request, 'pizza/topping.html',content)