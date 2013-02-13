# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('cmsplugin_blog_categories_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=512)),
        ))
        db.send_create_signal('cmsplugin_blog_categories', ['Category'])

        # Adding model 'CategoryTitle'
        db.create_table('cmsplugin_blog_categories_categorytitle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_blog_categories.Category'])),
            ('language', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('cmsplugin_blog_categories', ['CategoryTitle'])

        # Adding model 'EntryCategory'
        db.create_table('cmsplugin_blog_categories_entrycategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('entry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_blog.Entry'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_blog_categories.Category'])),
        ))
        db.send_create_signal('cmsplugin_blog_categories', ['EntryCategory'])

        # Adding unique constraint on 'EntryCategory', fields ['entry', 'category']
        db.create_unique('cmsplugin_blog_categories_entrycategory', ['entry_id', 'category_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'EntryCategory', fields ['entry', 'category']
        db.delete_unique('cmsplugin_blog_categories_entrycategory', ['entry_id', 'category_id'])

        # Deleting model 'Category'
        db.delete_table('cmsplugin_blog_categories_category')

        # Deleting model 'CategoryTitle'
        db.delete_table('cmsplugin_blog_categories_categorytitle')

        # Deleting model 'EntryCategory'
        db.delete_table('cmsplugin_blog_categories_entrycategory')


    models = {
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_blog.entry': {
            'Meta': {'ordering': "('-pub_date',)", 'object_name': 'Entry'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'placeholders': ('djangocms_utils.fields.M2MPlaceholderField', [], {'to': "orm['cms.Placeholder']", 'symmetrical': 'False'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'tags': ('tagging.fields.TagField', [], {})
        },
        'cmsplugin_blog_categories.category': {
            'Meta': {'object_name': 'Category'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '512'})
        },
        'cmsplugin_blog_categories.categorytitle': {
            'Meta': {'object_name': 'CategoryTitle'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog_categories.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'cmsplugin_blog_categories.entrycategory': {
            'Meta': {'unique_together': "(('entry', 'category'),)", 'object_name': 'EntryCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog_categories.Category']"}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog.Entry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['cmsplugin_blog_categories']
