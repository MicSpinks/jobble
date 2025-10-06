from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['note']
        widgets = {
            'note': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a personal note...',
                'class': 'form-control',  # ✅ Must be here
            }),
        }
