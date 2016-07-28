from django import forms
from models import Image
from django.contrib.auth.models import User


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': 'image/*'}),
        }

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }