from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import JobPosting


@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'min_salary', 'max_salary', 'remote_or_onsite', 'visa_sponsorship', 'posted_by', 'date_posted')
    list_filter = ('location', 'remote_or_onsite', 'visa_sponsorship', 'date_posted')
    search_fields = ('title', 'skills', 'location')
