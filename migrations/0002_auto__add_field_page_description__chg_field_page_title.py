# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.description'
        db.add_column('pages_page', 'description',
                      self.gf('django.db.models.fields.TextField')(default='Description not provided.'),
                      keep_default=False)


        # Changing field 'Page.title'
        db.alter_column('pages_page', 'title', self.gf('django.db.models.fields.CharField')(max_length=64))

    def backwards(self, orm):
        # Deleting field 'Page.description'
        db.delete_column('pages_page', 'description')


        # Changing field 'Page.title'
        db.alter_column('pages_page', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

    models = {
        'pages.page': {
            'Meta': {'object_name': 'Page'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '64'})
        }
    }

    complete_apps = ['pages']