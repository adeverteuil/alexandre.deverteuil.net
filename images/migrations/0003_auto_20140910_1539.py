# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_auto_20140910_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='original_height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='image',
            name='original_width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
