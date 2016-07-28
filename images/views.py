from django.shortcuts import render
from forms import UploadImageForm
from models import Image
from hashids import Hashids
from imagesite import settings
from django.contrib.auth.views import login
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

def delete(request):
    return render(request, 'delete.html')


def view(request, img_hash):
    img = Image.objects.get(img_hash=img_hash)
    return render(request, 'view.html', {'image': img})