from django.contrib import admin
from django.http import HttpResponse
import csv
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "role", "fname", "lname", "location")
    search_fields = ("username", "email", "fname", "lname", "skills")
    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        """Admin action to export selected CustomUser objects to CSV."""
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="users.csv"'

        writer = csv.writer(response)
        
        writer.writerow([
            "Username", "Email", "Role", "First Name", "Last Name",
            "Headline", "Skills", "Education", "Work Experience",
            "Location", "Links"
        ])

        for user in queryset:
            writer.writerow([
                user.username,
                user.email,
                user.role,
                user.fname,
                user.lname,
                user.headline,
                user.skills,
                user.education,
                user.work_experience,
                user.location,
                user.links
            ])

        return response

    export_as_csv.short_description = "Export Selected Users to CSV"