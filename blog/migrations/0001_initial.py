# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=256)),
                ('slug', models.SlugField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('body', models.TextField()),
                ('summary', models.CharField(null=True, blank=True, max_length=256)),
                ('public', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(null=True, blank=True, to='blog.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
