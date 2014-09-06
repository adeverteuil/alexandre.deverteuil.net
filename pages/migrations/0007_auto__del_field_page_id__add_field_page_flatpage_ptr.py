# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Page.id'
        db.delete_column('pages_page', 'id')

        # Adding field 'Page.flatpage_ptr'
        db.add_column('pages_page', 'flatpage_ptr',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=1, to=orm['flatpages.FlatPage'], unique=True, primary_key=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Page.id'
        raise RuntimeError("Cannot reverse this migration. 'Page.id' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Page.id'
        db.add_column('pages_page', 'id',
                      self.gf('django.db.models.fields.AutoField')(primary_key=True),
                      keep_default=False)

        # Deleting field 'Page.flatpage_ptr'
        db.delete_column('pages_page', 'flatpage_ptr_id')


    models = {
        'flatpages.flatpage': {
            'Meta': {'object_name': 'FlatPage', 'db_table': "'django_flatpage'", 'ordering': "('url',)"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '100'})
        },
        'pages.page': {
            'Meta': {'_ormbases': ['flatpages.FlatPage'], 'ordering': "('url',)", 'object_name': 'Page'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'flatpage_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['flatpages.FlatPage']", 'unique': 'True', 'primary_key': 'True'})
        },
        'sites.site': {
            'Meta': {'object_name': 'Site', 'db_table': "'django_site'", 'ordering': "('domain',)"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['pages']