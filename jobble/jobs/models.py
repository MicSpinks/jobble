from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class JobPosting(models.Model):
    REMOTE_CHOICES = [
        ("remote", "Remote"),
        ("onsite", "On-site"),
        ("hybrid", "Hybrid"),
    ]

    VISA_CHOICES = [
        ("yes", "Yes"),
        ("no", "No"),
    ]

    title = models.CharField(max_length=200)
    skills = models.TextField(
        help_text="List required skills, separated by commas",
        default=""  # ✅ ensures safe migrations
    )
    location = models.CharField(max_length=100, default="Not specified")  # ✅
    salary_range = models.CharField(
        max_length=100,
        help_text="e.g. $60,000 - $80,000",
        default="Not specified"  # ✅
    )
    remote_or_onsite = models.CharField(
        max_length=20,
        choices=REMOTE_CHOICES,
        default="onsite"  # ✅ avoids null issues
    )
    visa_sponsorship = models.CharField(
        max_length=3,
        choices=VISA_CHOICES,
        default="no"  # ✅ avoids null issues
    )

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.location})"
