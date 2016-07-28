import os
from django.db import models

# Create your models here.


def content_file_name(instance, filename):
    extension = os.path.splitext(instance.file.name)[1]
    return instance.img_hash + extension.lower()


class Image(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to=content_file_name)
    img_hash = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)
    uploaded_by = models.ForeignKey('auth.User', blank=True, null=True)