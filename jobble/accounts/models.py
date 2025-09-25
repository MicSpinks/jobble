from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ("recruiter", "Recruiter"),
        ("user", "User"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="user")
    # Profile fields for users (visible to recruiters depending on privacy flags)
    headline = models.CharField(max_length=255, blank=True, default='')
    skills = models.TextField(blank=True, default='')
    education = models.TextField(blank=True, default='')
    work_experience = models.TextField(blank=True, default='')
    location = models.CharField(max_length=255, blank=True, default='')
    links = models.TextField(blank=True, default='')

    # Privacy flags - whether recruiters can see each field
    show_headline = models.BooleanField(default=True)
    show_skills = models.BooleanField(default=True)
    show_education = models.BooleanField(default=True)
    show_work_experience = models.BooleanField(default=True)
    show_location = models.BooleanField(default=True)
    show_links = models.BooleanField(default=True)