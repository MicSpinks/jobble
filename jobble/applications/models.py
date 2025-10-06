from django.conf import settings
from django.db import models
from jobs.models import JobPosting

class Application(models.Model):
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Use the string here directly
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'user'}
    )
    note = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('job', 'applicant')

    def __str__(self):
        return f"{self.applicant.username} applied to {self.job.title}"
