from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.index, name='Ahome.index'),
 path("jobs/", include("jobs.urls")),
 path('manageposts/', views.manageposts, name='Ahome.manageposts'),
 path('manageusers/', views.manageusers, name='Ahome.manageusers'),
 path("jobs/<int:job_id>/delete/", views.delete_job, name="Ahome.delete_job"),
 path("users/<int:user_id>/delete/", views.delete_user, name="Ahome.delete_user"),
 path("users/<int:user_id>/change-role/", views.change_role, name="Ahome.change_role"),
]