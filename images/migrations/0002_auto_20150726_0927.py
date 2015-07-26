# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(upload_to=images.models.content_file_name),
        ),
    ]
