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
    fname = models.CharField(max_length=30, blank=True, default='')
    lname = models.CharField(max_length=30, blank=True, default='')
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


    @property
    def visible_attributes(self):
        attrs = {}
        if self.show_headline and self.headline:
            attrs['Headline'] = self.headline
        if self.show_skills and self.skills:
            attrs['Skills'] = self.skills
        if self.show_education and self.education:
            attrs['Education'] = self.education
        if self.show_work_experience and self.work_experience:
            attrs['Work Experience'] = self.work_experience
        if self.show_location and self.location:
            attrs['Location'] = self.location
        if self.show_links and self.links:
            attrs['Links'] = self.links
        return attrs


