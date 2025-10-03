from django.urls import path
from . import views
urlpatterns = [
    path('', views.landing, name='home.landing'),
    path('dashboard/', views.index, name='home.index'),
    path('applications', views.applications, name='home.applications'),
    path('jobs', views.jobs, name='home.jobs'),
    path('maps', views.maps, name='home.maps'),
    path('messages', views.messages, name='home.messages'),
]