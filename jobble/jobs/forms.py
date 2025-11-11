from django import forms
from .models import JobPosting

class JobPostingForm(forms.ModelForm):
    latitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    longitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    city = forms.CharField(widget=forms.HiddenInput(), required=False)
    state = forms.CharField(widget=forms.HiddenInput(), required=False)
    country = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = JobPosting
        fields = [
            'title',
            'skills',
            'location',
            'latitude',
            'longitude',
            'city',
            'state',
            'country',
            'min_salary',
            'max_salary',
            'remote_or_onsite',
            'visa_sponsorship',
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'location-input',
                'placeholder': 'Enter city, state, or address'
            }),
            'min_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'max_salary': forms.NumberInput(attrs={'class': 'form-control'}),
            'remote_or_onsite': forms.Select(attrs={'class': 'form-select'}),
            'visa_sponsorship': forms.Select(attrs={'class': 'form-select'}),
        }