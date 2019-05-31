# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0005_image_view_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
