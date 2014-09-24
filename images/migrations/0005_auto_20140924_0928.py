# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0004_auto_20140912_2101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='basename',
        ),
        migrations.RemoveField(
            model_name='image',
            name='collection',
        ),
        migrations.DeleteModel(
            name='Collection',
        ),
        migrations.RemoveField(
            model_name='image',
            name='original_basename',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.AlterField(
            model_name='image',
            name='original',
            field=models.ImageField(height_field='original_height', upload_to='image_uploads', width_field='original_width'),
        ),
    ]
