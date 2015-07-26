from django.shortcuts import render
from django.http import HttpResponse
from forms import UploadImageForm
from models import Image
import base64
import time


# Create your views here.

def getHash():
	return base64.b64encode(str(time.time()))[8:-2]

def submit(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            newImage = form.save(commit=False)
            newImage.img_hash = getHash()
            newImage.save()
            return HttpResponse("Submitted! Hash: " + newImage.img_hash)
    form = UploadImageForm()
    return render(request, 'submit.html', {'form': form})

def view(request):
    url = Image.objects.get(img_hash=request.path[1:])
    return render(request, 'view.html', {'title': url.title, 'image': url.file.url})