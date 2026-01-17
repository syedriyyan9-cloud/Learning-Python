"""urls for the app"""

from django.urls import path


from . import views

app_name = 'pizza'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('pizza/', views.pizza, name = 'pizza'),
    path('pizza/<int:pizza_id>', views.topping, name = 'topping'),
]