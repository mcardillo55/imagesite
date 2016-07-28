from django.shortcuts import render
from forms import UploadImageForm
from models import Image
from hashids import Hashids
from imagesite import settings
import time

# Create your views here.


def getHash():
    hashids = Hashids(salt=settings.SECRET_KEY)
    curTime = int(round(time.time() * 1000))
    return hashids.encode(curTime)


def home(request):
    if request.method == 'POST':
        submit(request)
    form = UploadImageForm()
    latest_imgs_objs = Image.objects.all().order_by('-created_at')
    latest_imgs = [latest_imgs_objs[:4], latest_imgs_objs[4:8]]
    return render(request, 'home.html', {'latest_imgs': latest_imgs, 'form': form})


def submit(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        newImage = None
        if form.is_valid():
            newImage = form.save(commit=False)
            newImage.img_hash = getHash()
            newImage.save()
        return render(request, "submit_post.html", {'newImage': newImage})
    form = UploadImageForm()
    return render(request, 'submit.html', {'form': form})


def delete(request):
    return render(request, 'delete.html')


def view(request, img_hash):
    img = Image.objects.get(img_hash=img_hash)
    form = UploadImageForm()
    return render(request, 'view.html', {'image': img, 'form': form})