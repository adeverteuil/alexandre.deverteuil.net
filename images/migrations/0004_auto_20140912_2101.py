# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_auto_20140910_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='slug',
        ),
        migrations.AddField(
            model_name='image',
            name='basename',
            field=models.CharField(max_length=128, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='original_basename',
            field=models.CharField(blank=True, max_length=128, editable=False, default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='original',
            field=models.ImageField(width_field='original_width', height_field='original_height', upload_to='images/uploads'),
        ),
        migrations.AlterField(
            model_name='image',
            name='original_height',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='original_width',
            field=models.IntegerField(blank=True),
        ),
    ]
