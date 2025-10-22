from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
    path('my/', views.my_applications, name='my_applications'),
    path('recruiter/', views.recruiter_applicants, name='recruiter_applicants'),
    path('application/<int:application_id>/update_status/', views.update_status, name='update_status'),
    path('withdraw/<int:pk>/', views.withdraw_application, name='withdraw_application'),
]
