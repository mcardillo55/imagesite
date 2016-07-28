from django.shortcuts import render
from forms import UploadImageForm, UserForm
from models import Image
from hashids import Hashids
from imagesite import settings
from django.contrib.auth.views import login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404
import time

# Create your views here.


def getHash():
    hashids = Hashids(salt=settings.SECRET_KEY)
    curTime = int(round(time.time() * 1000))
    return hashids.encode(curTime)


def home(request):
    if request.method == 'POST':
        submit(request)
    latest_imgs_objs = Image.objects.all().order_by('-created_at')
    latest_imgs = [latest_imgs_objs[:4], latest_imgs_objs[4:8]]
    return render(request, 'home.html', {'latest_imgs': latest_imgs})


def submit(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        newImage = None
        if form.is_valid():
            newImage = form.save(commit=False)
            newImage.img_hash = getHash()
            if request.user.is_authenticated():
                newImage.uploaded_by = request.user
            newImage.save()
        return render(request, "submit_post.html", {'newImage': newImage})
    form = UploadImageForm()
    if request.GET.get('ref') == 'modal':
        return render(request, 'modal_form.html', {'title': 'Upload an Image', 'form': form})
    else:
        return render(request, 'submit.html', {'form': form})


def login_view(request):
    if request.GET.get('ref') == 'modal':
        return login(request, template_name='modal_form.html', extra_context={'title': 'Log In'})
    else:
        return login(request, template_name='login.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password'])
            login(request, new_user)
            return render(request, "profile.html")
    else:
        form = UserForm()
        if request.GET.get('ref') == 'modal':
            return render(request, 'modal_form.html', {'title': 'Sign Up', 'form': form})
        else:
            return True
            #non-modal signup code here

def delete(request):
    return render(request, 'delete.html')

@login_required
def profile(request):
    return render(request, 'profile.html')


def view(request, img_hash):
    try:
        img = Image.objects.get(img_hash=img_hash)
    except:
        raise Http404("Image does not exist.")
    img.view_count += 1
    img.save()
    return render(request, 'view.html', {'image': img})