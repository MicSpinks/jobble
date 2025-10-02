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
        default=""
    )
    location = models.CharField(max_length=100, default="Not specified")

    # ✅ Split salary into two integer fields
    min_salary = models.IntegerField(default=0, help_text="Minimum annual salary (USD)")
    max_salary = models.IntegerField(default=0, help_text="Maximum annual salary (USD)")

    remote_or_onsite = models.CharField(
        max_length=20,
        choices=REMOTE_CHOICES,
        default="onsite"
    )
    visa_sponsorship = models.CharField(
        max_length=3,
        choices=VISA_CHOICES,
        default="no"
    )

    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.location})"

    @property
    def salary_display(self):
        """Convenient formatted salary range"""
        if self.min_salary and self.max_salary:
            return f"${self.min_salary:,} - ${self.max_salary:,}"
        elif self.min_salary:
            return f"From ${self.min_salary:,}"
        elif self.max_salary:
            return f"Up to ${self.max_salary:,}"
        return "Not specified"
