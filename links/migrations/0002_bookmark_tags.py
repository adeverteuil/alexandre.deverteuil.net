# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0001_initial'),
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='tags',
            field=taggit.managers.TaggableManager(verbose_name='Tags', blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag'),
            preserve_default=True,
        ),
    ]
