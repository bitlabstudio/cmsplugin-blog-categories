# flake8: noqa
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.parent'
        db.add_column('cmsplugin_blog_categories_category', 'parent',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_blog_categories.Category'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Category.parent'
        db.delete_column('cmsplugin_blog_categories_category', 'parent_id')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 6, 4, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
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
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog_categories.Category']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '512'})
        },
        'cmsplugin_blog_categories.categoryplugin': {
            'Meta': {'object_name': 'CategoryPlugin', 'db_table': "'cmsplugin_categoryplugin'", '_ormbases': ['cms.CMSPlugin']},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cmsplugin_blog_categories.Category']", 'symmetrical': 'False'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'template_argument': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'cmsplugin_blog_categories.categorytitle': {
            'Meta': {'object_name': 'CategoryTitle'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_blog_categories.Category']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'cmsplugin_blog_categories.entrycategory': {
            'Meta': {'object_name': 'EntryCategory'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'entry_categories'", 'to': "orm['cmsplugin_blog_categories.Category']"}),
            'entry': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': "orm['cmsplugin_blog.Entry']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['cmsplugin_blog_categories']
