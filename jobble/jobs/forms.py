from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    class Meta:
        model = JobPosting
        fields = [
            'title',
            'skills',
            'location',
            'min_salary',
            'max_salary',
            'remote_or_onsite',
            'visa_sponsorship',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'min_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'remote_or_onsite': forms.Select(attrs={'class': 'form-select'}),
            'visa_sponsorship': forms.Select(attrs={'class': 'form-select'}),
        }
