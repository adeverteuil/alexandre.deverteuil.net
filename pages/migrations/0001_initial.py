# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flatpages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('flatpage_ptr', models.OneToOneField(primary_key=True, auto_created=True, serialize=False, parent_link=True, to='flatpages.FlatPage')),
                ('description', models.CharField(max_length=256)),
                ('pub_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=('flatpages.flatpage',),
        ),
    ]
