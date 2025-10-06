from django.urls import path
from . import views

app_name = "messaging"

urlpatterns = [
    path("recruiter/", views.recruiter_messages, name="recruiter_inbox"),
    path("user/", views.user_messages, name="user_inbox"),
]
