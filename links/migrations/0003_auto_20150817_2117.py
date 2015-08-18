# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_bookmark_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmark',
            options={'ordering': ('-datetime_added',)},
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
