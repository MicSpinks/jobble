from django.urls import path
from . import views

app_name = 'applications'

urlpatterns = [
    path('apply/<int:job_id>/', views.apply_to_job, name='apply_to_job'),
    path('my/', views.my_applications, name='my_applications'),
    path('recruiter/', views.recruiter_applicants, name='recruiter_applicants'),
]
