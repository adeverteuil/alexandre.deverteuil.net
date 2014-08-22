# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('blog_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=64, unique=True)),
        ))
        db.send_create_signal('blog', ['Category'])

        # Adding field 'Post.summary'
        db.add_column('blog_post', 'summary',
                      self.gf('django.db.models.fields.TextField')(null=True),
                      keep_default=False)

        # Adding M2M table for field categories on 'Post'
        m2m_table_name = db.shorten_name('blog_post_categories')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('post', models.ForeignKey(orm['blog.post'], null=False)),
            ('category', models.ForeignKey(orm['blog.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['post_id', 'category_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('blog_category')

        # Deleting field 'Post.summary'
        db.delete_column('blog_post', 'summary')

        # Removing M2M table for field categories on 'Post'
        db.delete_table(db.shorten_name('blog_post_categories'))


    models = {
        'blog.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'unique': 'True'})
        },
        'blog.post': {
            'Meta': {'object_name': 'Post'},
            'body': ('django.db.models.fields.TextField', [], {}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['blog.Category']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summary': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['blog']