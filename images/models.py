from django.db import models

# Create your models here.

def content_file_name(instance, filename):
    return '/'.join(['image_data', instance.img_hash])

class Image(models.Model):
    title = models.CharField(max_length=100)
    file = models.ImageField(upload_to=content_file_name)
    img_hash = models.CharField(max_length=20)