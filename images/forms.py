from django import forms
from models import Image


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'file']
        widgets = {
            'file': forms.FileInput(attrs={'accept': 'image/*'}),
        }