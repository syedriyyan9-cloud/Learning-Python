"""Blogs urls"""

from django.urls import path

from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('add_blogs/', views.add_blog, name = 'add_blog'),
    path('edit_blogs/<int:blog_id>', views.edit_blog, name = 'edit_blog'),
]