from django import forms
from .models import Message
from accounts.models import CustomUser  # you already have CustomUser with roles

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['receiver', 'content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")  # logged-in user
        super().__init__(*args, **kwargs)

        if user.role == "recruiter":
            self.fields['receiver'].queryset = CustomUser.objects.filter(role="user")
        elif user.role == "user":
            self.fields['receiver'].queryset = CustomUser.objects.filter(role="recruiter")
