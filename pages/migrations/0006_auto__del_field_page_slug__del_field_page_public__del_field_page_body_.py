# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Page.slug'
        db.delete_column('pages_page', 'slug')

        # Deleting field 'Page.public'
        db.delete_column('pages_page', 'public')

        # Deleting field 'Page.body'
        db.delete_column('pages_page', 'body')

        # Deleting field 'Page.title'
        db.delete_column('pages_page', 'title')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Page.slug'
        raise RuntimeError("Cannot reverse this migration. 'Page.slug' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Page.slug'
        db.add_column('pages_page', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50),
                      keep_default=False)

        # Adding field 'Page.public'
        db.add_column('pages_page', 'public',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Page.body'
        raise RuntimeError("Cannot reverse this migration. 'Page.body' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Page.body'
        db.add_column('pages_page', 'body',
                      self.gf('django.db.models.fields.TextField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Page.title'
        raise RuntimeError("Cannot reverse this migration. 'Page.title' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Page.title'
        db.add_column('pages_page', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=64),
                      keep_default=False)


    models = {
        'pages.page': {
            'Meta': {'object_name': 'Page'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['pages']