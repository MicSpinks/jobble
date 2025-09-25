from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import JobPosting

@admin.register(JobPosting)
class JobPostingAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_by', 'date_posted')
    search_fields = ('title', 'company', 'location')
    list_filter = ('company', 'location', 'date_posted')