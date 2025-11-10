from django.urls import path
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),
    path('create/', views.create_job, name='create_job'),
    path('<int:job_id>/edit/', views.edit_job, name='edit_job'),
]