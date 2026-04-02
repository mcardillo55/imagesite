from django.urls import path, re_path
from images import views

urlpatterns = [
    path("latest/", views.latest, name="latest"),
    path("", views.home, name="home"),
    # Catch-all: any other path is treated as an image hash.
    # This must be last.
    re_path(r"^(?P<img_hash>.+)$", views.view, name="view"),
]
