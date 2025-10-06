from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home.index'),
    path('jobs', views.jobs, name='home.jobs'),
    path('maps', views.maps, name='home.maps'),
]