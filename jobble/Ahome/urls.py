from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='Ahome.index'),
 path('manageposts/', views.manageposts, name='Ahome.manageposts'),
 path('manageusers/', views.manageusers, name='Ahome.manageusers'),
]