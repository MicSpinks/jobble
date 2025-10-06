from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'applicant', 'applied_at')  # Columns to show in admin list view
    list_filter = ('applied_at',)                      # Filter sidebar
    search_fields = ('job__title', 'applicant__username', 'note')  # Searchable fields
    ordering = ('-applied_at',)                        # Default ordering
