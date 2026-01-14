from django.db import models

# Create your models here
class Pizza(models.Model):
    """a class to represent pizzas"""
    name = models.TextField(max_length=100)

    def __str__(self):
        """method to allow names of objects to display"""
        return self.name

class Topping(models.Model):
    """a class to represent toppings"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)

    def __str__(self):
        """method to allow names of objects to display"""
        return self.name
