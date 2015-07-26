from django.db import models

# Create your models here.

class Image(models.Model):
	title = CharField(max_length=100)
	img_hash = CharField(max_length=20)