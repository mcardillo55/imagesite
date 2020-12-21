
from django.contrib.auth.forms import AuthenticationForm
from .forms import UploadImageForm, UserForm

def login_form_renderer(request):
    return {
        'signup_form': UserForm(),
        'upload_form': UploadImageForm(),
        'login_form': AuthenticationForm(request),
    }