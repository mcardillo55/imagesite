from django.shortcuts import render
from django.http import Http404, HttpResponse
from images.models import Image


def latest(request):
    """Infinite-scroll endpoint: return next batch of thumbnails."""
    last = request.GET.get("last")
    try:
        last_image = Image.objects.get(img_hash=last)
    except Image.DoesNotExist:
        return HttpResponse("")
    latest_imgs = (
        Image.objects.filter(created_at__lt=last_image.created_at)
        .order_by("-created_at")[:24]
    )
    return render(request, "latest_images_stub.html", {"latest_imgs": latest_imgs})


def home(request):
    """Gallery home page — newest 24 images."""
    latest_imgs = Image.objects.all().order_by("-created_at")[:24]
    return render(request, "home.html", {"latest_imgs": latest_imgs})


def view(request, img_hash):
    """Single-image detail page."""
    try:
        img = Image.objects.get(img_hash=img_hash)
    except Image.DoesNotExist:
        raise Http404("Image does not exist.")
    # Read-only: no view_count increment.
    return render(request, "view.html", {"image": img})
