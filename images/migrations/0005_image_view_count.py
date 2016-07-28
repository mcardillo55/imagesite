# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_image_uploaded_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='view_count',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
