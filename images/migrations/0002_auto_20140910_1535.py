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
            name='original',
            field=models.ImageField(upload_to="images.models.get_image_path", width_field='original_width', height_field='original_height'),
        ),
    ]
